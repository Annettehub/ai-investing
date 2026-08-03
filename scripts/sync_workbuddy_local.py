#!/usr/bin/env python3
"""
Import local WorkBuddy documents into 03-raw/feishu/local-workbuddy.

This is a local fallback/complement to Feishu API sync. It converts readable text
formats to Markdown and emits the same manifest shape as sync_feishu_drive.py so
review_feishu_ingest.py can process the new files.
"""
import argparse
import hashlib
import html
import json
import os
import re
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path


DEFAULT_SOURCE = Path(r"D:\WorkBuddy\Claw")
RAW_DIR = Path("03-raw/feishu/local-workbuddy")
STATE_FILE = Path("03-raw/.local_workbuddy_hashes.json")
DEFAULT_MANIFEST = Path(".workbuddy-local-sync-manifest.json")
TEXT_EXTENSIONS = {".md", ".markdown", ".txt", ".html", ".htm"}
UNSUPPORTED_EXTENSIONS = {".pdf", ".docx", ".pptx", ".xlsx"}
BOILERPLATE_FILES = {
    "readme.md",
    "requirements.txt",
    "index.html",
    "行情更新日志.txt",
}
SKIP_DIRS = {
    ".git",
    ".cache",
    ".workbuddy",
    ".venv",
    "__pycache__",
    "node_modules",
    "site",
    "dist",
    "outputs",
    "_archive",
    "99-backup",
    "backup",
}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "noscript"}:
            self.skip_depth += 1
        elif tag in {"p", "div", "section", "article", "br", "li", "tr", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
        elif tag in {"p", "div", "section", "article", "li", "tr", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip_depth:
            text = data.strip()
            if text:
                self.parts.append(text)

    def text(self):
        joined = " ".join(self.parts)
        joined = html.unescape(joined)
        joined = re.sub(r"[ \t]+", " ", joined)
        joined = re.sub(r"\n\s+", "\n", joined)
        joined = re.sub(r"\n{3,}", "\n\n", joined)
        return joined.strip()


def safe_path_part(name, max_len=100):
    invalid = '<>:"/\\|?*'
    safe = name.strip()
    for ch in invalid:
        safe = safe.replace(ch, "_")
    safe = safe.rstrip(". ")
    if not safe:
        safe = "untitled"
    return safe[:max_len]


def is_repo_root(path):
    return (path / ".git").exists() and (path / "02-kb").exists() and (path / "03-raw").exists()


def should_skip_dir(path, source_root, target_root):
    if path.resolve() == target_root:
        return True
    if path.name in SKIP_DIRS:
        return True
    if is_repo_root(path) and path != source_root:
        return True
    return False


def iter_files(source_root, target_root):
    stack = [source_root]
    while stack:
        current = stack.pop()
        try:
            entries = list(current.iterdir())
        except OSError:
            continue
        for entry in entries:
            if entry.is_dir():
                if not should_skip_dir(entry, source_root, target_root):
                    stack.append(entry)
                continue
            if entry.exists() and (entry.suffix.lower() in TEXT_EXTENSIONS or entry.suffix.lower() in UNSUPPORTED_EXTENSIONS):
                yield entry


def read_text_file(path):
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="ignore")


def convert_to_markdown(path, source_root):
    ext = path.suffix.lower()
    rel_source = path.relative_to(source_root).as_posix()
    if ext in {".html", ".htm"}:
        parser = TextExtractor()
        parser.feed(read_text_file(path))
        body = parser.text()
    else:
        body = read_text_file(path).strip()

    if not body:
        return None

    title = path.stem
    modified = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    return f"""---
source_platform: "WorkBuddy local"
source_path: "{rel_source}"
source_modified_at: "{modified}"
source_format: "{ext.lstrip('.')}"
---

# {title}

{body}
"""


def unsupported_note(path, source_root):
    rel_source = path.relative_to(source_root).as_posix()
    modified = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    return f"""---
source_platform: "WorkBuddy local"
source_path: "{rel_source}"
source_modified_at: "{modified}"
source_format: "{path.suffix.lower().lstrip('.')}"
conversion_status: "unsupported"
---

# {path.stem}

本地文件 `{rel_source}` 是 `{path.suffix.lower()}` 格式，当前脚本只记录占位信息，未自动抽取正文。需要人工转换为 Markdown 后再进入 distill。
"""


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def digest_text(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:16]


def output_path(source_root, path):
    rel_parts = path.relative_to(source_root).parts
    folder_parts = [safe_path_part(part) for part in rel_parts[:-1]]
    filename = safe_path_part(path.stem) + ".md"
    return RAW_DIR.joinpath(*folder_parts, filename)


def write_manifest(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Sync local WorkBuddy docs into raw Feishu inbox.")
    parser.add_argument("--source", default=str(DEFAULT_SOURCE), help="Local WorkBuddy source directory")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="Output manifest path")
    parser.add_argument("--include-unsupported", action="store_true", help="Create placeholder notes for PDF/DOCX/PPTX/XLSX")
    parser.add_argument("--include-boilerplate", action="store_true", help="Import README/index/log/config text files too")
    parser.add_argument("--since-days", type=int, default=30, help="Only import files modified in the last N days; use 0 for no limit")
    parser.add_argument("--since-date", help="Only import files modified on or after YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be imported without writing files")
    args = parser.parse_args()

    source_root = Path(args.source).resolve()
    if not source_root.exists():
        raise RuntimeError(f"Source directory does not exist: {source_root}")

    target_root = Path.cwd().resolve()
    state = load_state()
    saved_files = []
    skipped = 0
    unsupported = []
    if args.since_date:
        since = datetime.strptime(args.since_date, "%Y-%m-%d")
    elif args.since_days and args.since_days > 0:
        since = datetime.now() - timedelta(days=args.since_days)
    else:
        since = None

    for source_file in iter_files(source_root, target_root):
        if not args.include_boilerplate and source_file.name.lower() in BOILERPLATE_FILES:
            skipped += 1
            continue
        try:
            stat = source_file.stat()
        except OSError:
            skipped += 1
            continue
        if since and datetime.fromtimestamp(stat.st_mtime) < since:
            skipped += 1
            continue

        ext = source_file.suffix.lower()
        if ext in UNSUPPORTED_EXTENSIONS:
            unsupported.append(source_file.relative_to(source_root).as_posix())
            if not args.include_unsupported:
                skipped += 1
                continue
            content = unsupported_note(source_file, source_root)
        else:
            content = convert_to_markdown(source_file, source_root)
            if not content:
                skipped += 1
                continue

        digest = digest_text(content)
        state_key = source_file.relative_to(source_root).as_posix()
        out = output_path(source_root, source_file)
        if state.get(state_key) == digest and out.exists():
            skipped += 1
            continue

        if args.dry_run:
            print(f"Would import: {source_file} -> {out}")
            saved_files.append(out.as_posix())
            continue

        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        state[state_key] = digest
        saved_files.append(out.as_posix())
        print(f"Imported: {source_file} -> {out}")

    if not args.dry_run:
        save_state(state)
        write_manifest(
            Path(args.manifest),
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "source": str(source_root),
                "saved_count": len(saved_files),
                "skipped_count": skipped,
                "unsupported_count": len(unsupported),
                "saved_files": saved_files,
                "unsupported_files": unsupported[:200],
            },
        )

    print(f"Saved: {len(saved_files)}, skipped: {skipped}, unsupported: {len(unsupported)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
