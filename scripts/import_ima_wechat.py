#!/usr/bin/env python3
"""
Import original IMA exports into 03-raw/wechat without rewriting content.

The script copies source files byte-for-byte, records hashes for dedupe, and can
optionally commit/push the imported raw files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INBOX = Path(r"D:\WorkBuddy\Claw\ima-inbox")
OUTPUT_DIR = ROOT / "03-raw" / "wechat"
STATE_FILE = ROOT / "05-meta" / "ima-wechat-import-state.json"
SUPPORTED_EXTENSIONS = {".md", ".txt", ".html", ".htm", ".pdf", ".docx"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"files": {}}


def write_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def safe_name(name: str, max_len: int = 140) -> str:
    safe = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name.strip())
    safe = re.sub(r"\s+", " ", safe).rstrip(". ")
    return (safe or "untitled")[:max_len]


def infer_date(path: Path) -> str:
    text = path.name
    match = re.search(r"(20\d{2})[-_\.年]?(0[1-9]|1[0-2])[-_\.月]?(0[1-9]|[12]\d|3[01])", text)
    if match:
        return "".join(match.groups())
    return datetime.now().strftime("%Y%m%d")


def destination_path(source: Path) -> Path:
    date_prefix = infer_date(source)
    stem = safe_name(source.stem)
    suffix = source.suffix.lower()
    if not stem.startswith(date_prefix):
        filename = f"{date_prefix}-IMA-{stem}{suffix}"
    else:
        filename = f"IMA-{stem}{suffix}"
    return OUTPUT_DIR / filename


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    counter = 1
    while True:
        candidate = path.with_name(f"{stem}_{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def iter_sources(inbox: Path) -> list[Path]:
    if not inbox.exists():
        inbox.mkdir(parents=True, exist_ok=True)
        return []
    return sorted(
        path
        for path in inbox.rglob("*")
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
        and not path.name.startswith("~$")
    )


def copy_original(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def run_git(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def ensure_clean_for_push() -> None:
    result = run_git(["status", "--short"])
    dirty_lines = [
        line
        for line in result.stdout.splitlines()
        if not line.endswith("03-raw/wechat/20260711-NOTE-2026-07-11-20VC-Glean-ArvindJain.md")
    ]
    if dirty_lines:
        raise RuntimeError(
            "Working tree has unrelated changes. Commit or clean them before --push:\n"
            + "\n".join(dirty_lines)
        )


def commit_and_push(imported: list[Path], message: str) -> None:
    add_paths = [str(path.relative_to(ROOT)).replace("\\", "/") for path in imported]
    add_paths.append(str(STATE_FILE.relative_to(ROOT)).replace("\\", "/"))

    add_result = run_git(["add", "--", *add_paths])
    if add_result.returncode != 0:
        raise RuntimeError(add_result.stdout)

    diff_result = run_git(["diff", "--cached", "--quiet"])
    if diff_result.returncode == 0:
        print("No staged changes to commit.")
        return

    commit_result = run_git(["commit", "-m", message])
    print(commit_result.stdout.strip())
    if commit_result.returncode != 0:
        raise RuntimeError("git commit failed")

    push_result = run_git(["push", "origin", "HEAD:main"])
    print(push_result.stdout.strip())
    if push_result.returncode != 0:
        raise RuntimeError("git push failed")


def main() -> int:
    parser = argparse.ArgumentParser(description="Import IMA original exports into 03-raw/wechat.")
    parser.add_argument("--inbox", default=str(DEFAULT_INBOX), help="Folder containing IMA exported original files.")
    parser.add_argument("--push", action="store_true", help="Commit and push imported files to GitHub main.")
    parser.add_argument("--delete-source", action="store_true", help="Delete source files from inbox after successful import.")
    parser.add_argument("--message", default=None, help="Commit message used with --push.")
    args = parser.parse_args()

    inbox = Path(args.inbox).expanduser()
    sources = iter_sources(inbox)
    state = read_state()
    seen = state.setdefault("files", {})
    imported: list[Path] = []
    skipped = 0

    print(f"IMA inbox: {inbox}")
    print(f"Files found: {len(sources)}")

    if args.push:
        ensure_clean_for_push()

    for source in sources:
        digest = sha256_file(source)
        if digest in seen:
            skipped += 1
            print(f"Skip duplicate: {source.name}")
            continue

        target = unique_path(destination_path(source))
        copy_original(source, target)
        imported.append(target)
        seen[digest] = {
            "source_name": source.name,
            "target": str(target.relative_to(ROOT)).replace("\\", "/"),
            "sha256": digest,
            "imported_at": datetime.now().isoformat(timespec="seconds"),
        }
        print(f"Imported: {source.name} -> {target.relative_to(ROOT)}")

        if args.delete_source:
            source.unlink()

    if imported:
        write_state(state)

    print(f"\nImported: {len(imported)}")
    print(f"Skipped duplicates: {skipped}")

    if args.push and imported:
        message = args.message or f"sync: IMA originals {datetime.now().strftime('%Y-%m-%d-%H:%M')}"
        commit_and_push(imported, message)
    elif args.push:
        print("Nothing new to push.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"IMA import failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
