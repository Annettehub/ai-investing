#!/usr/bin/env python3
"""Generate Starlight docs from 02-kb and 04-output.

The generated website publishes structured knowledge pages while keeping
03-raw out of the site content tree. References to raw files are rendered as
small expandable source boxes linking back to GitHub.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = ROOT / "site" / "src" / "content" / "docs"
KB_SRC = ROOT / "02-kb"
OUTPUT_SRC = ROOT / "04-output"
KB_DEST = DOCS_ROOT / "kb"
OUTPUT_DEST = DOCS_ROOT / "outputs"
SIDEBAR_DEST = ROOT / "site" / "sidebar.generated.mjs"
DASHBOARD_FILES = {
    OUTPUT_SRC / "data" / "H1.2-storage-dashboard.json": ROOT / "site" / "src" / "data" / "h12-dashboard.json",
    OUTPUT_SRC / "data" / "R1-upstream-dashboard.json": ROOT / "site" / "src" / "data" / "r1-dashboard.json",
    OUTPUT_SRC / "data" / "R2-downstream-dashboard.json": ROOT / "site" / "src" / "data" / "r2-dashboard.json",
}
GITHUB_BLOB = "https://github.com/Annettehub/ai-investing/blob/main"

CATEGORY_LABELS = {
    "concepts": "概念框架",
    "entities": "公司与标的",
    "hypotheses": "投资假设",
    "sources": "来源摘要",
    "research": "研究报告",
    "reports": "研究报告",
    "tracking": "长期跟踪",
    "today": "每日跟踪",
    "weekly": "周度复盘",
}

SLUG_OVERRIDES = {
    "concepts": "concepts",
    "entities": "entities",
    "hypotheses": "hypotheses",
    "sources": "sources",
    "research": "research",
    "today": "today",
    "weekly": "weekly",
}

DIR_LABEL_OVERRIDES = {
    "L1-能源层（Energy）": "L1 能源层（触发器）",
    "L2-芯片层（Chips）": "L2 芯片层（长期观察）",
    "L3-基础设施层（Infrastructure）": "L3 基础设施层（触发器）",
    "L4-模型层（Models）": "L4 模型层（长期观察）",
    "L5-应用层（Applications）": "L5 应用层（长期观察）",
    "跨层-方法论（Cross-Layer）": "跨层动态",
}


def is_within(path: Path, parent: Path) -> bool:
    path = path.resolve()
    parent = parent.resolve()
    return path == parent or parent in path.parents


def reset_dir(path: Path) -> None:
    if path.exists():
        if not is_within(path, DOCS_ROOT):
            raise RuntimeError(f"Refusing to remove outside docs root: {path}")
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def slugify(value: str) -> str:
    value = value.replace(".md", "")
    if value in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[value]
    ascii_part = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]
    if ascii_part:
        return f"{ascii_part[:42]}-{digest}"
    return f"p-{digest}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def normalize_heading(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def remove_duplicate_h1(body: str, title: str) -> str:
    lines = body.splitlines()
    if not lines:
        return body

    match = re.match(r"^#\s+(.+?)\s*$", lines[0])
    if not match:
        return body

    if normalize_heading(match.group(1)) != normalize_heading(title):
        return body

    remaining = "\n".join(lines[1:]).lstrip()
    return remaining + ("\n" if remaining else "")


def get_title(path: Path, text: str) -> str:
    for line in strip_frontmatter(text).splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return path.stem


def frontmatter(title: str, description: str) -> str:
    return (
        "---\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        f"description: {json.dumps(description, ensure_ascii=False)}\n"
        "---\n\n"
    )


def clean_dir_label(value: str) -> str:
    if value in CATEGORY_LABELS:
        return CATEGORY_LABELS[value]
    if value in DIR_LABEL_OVERRIDES:
        return DIR_LABEL_OVERRIDES[value]
    label = re.sub(r"-(?:[0-9a-f]{8}|[0-9a-f]{7})$", "", value, flags=re.IGNORECASE)
    label = re.sub(r"^p-[0-9a-f]{8}$", "页面", label, flags=re.IGNORECASE)
    label = re.sub(r"[（(][A-Za-z][A-Za-z0-9 /\-_.]*[）)]", "", label)
    label = label.replace("-", " ")
    label = re.sub(r"\s+", " ", label).strip()
    return label or value


def relative_posix(path: Path, base: Path) -> str:
    return path.relative_to(base).as_posix()


def sidebar_slug_for(source_path: Path, source_root: Path, dest_root: Path) -> str:
    out_path = output_path_for(source_path, source_root, dest_root)
    route = relative_posix(out_path.with_suffix(""), DOCS_ROOT)
    if route.endswith("/index"):
        route = route[: -len("/index")]
    return route


def output_dir_for_source_dir(source_dir: Path, source_root: Path, dest_root: Path) -> Path:
    rel = source_dir.relative_to(source_root)
    if rel == Path("."):
        return dest_root
    return dest_root.joinpath(*[slugify(part) for part in rel.parts])


def sidebar_slug_for_source_dir(source_dir: Path, source_root: Path, dest_root: Path) -> str:
    route = relative_posix(output_dir_for_source_dir(source_dir, source_root, dest_root), DOCS_ROOT)
    return route


def normalize_rel(source_path: Path, source_root: Path) -> Path:
    rel = source_path.relative_to(source_root)
    if source_root != OUTPUT_SRC or rel.parent != Path(".") or rel.name.lower() == "index.md":
        return rel

    stem = rel.stem
    if stem.startswith("today-"):
        return Path("today") / rel.name
    if re.search(r"\d{4}-W\d{2}", stem, flags=re.IGNORECASE) or "周度复盘" in stem:
        return Path("weekly") / rel.name
    return Path("research") / rel.name


def output_path_for(source_path: Path, source_root: Path, dest_root: Path) -> Path:
    rel = normalize_rel(source_path, source_root)
    if rel.name.lower() == "index.md":
        if rel.parent == Path("."):
            return dest_root / "index.md"
        return dest_root.joinpath(*[slugify(part) for part in rel.parent.parts], "index.md")

    parts = [slugify(part) for part in rel.parent.parts]
    filename = f"{slugify(source_path.stem)}.md"
    return dest_root.joinpath(*parts, filename)


def build_maps() -> tuple[dict[str, str], dict[str, str]]:
    path_map: dict[str, str] = {}
    basename_map: dict[str, str] = {}

    for source_root, dest_root, route_root in (
        (KB_SRC, KB_DEST, "kb"),
        (OUTPUT_SRC, OUTPUT_DEST, "outputs"),
    ):
        for source_path in source_root.rglob("*.md"):
            rel = relative_posix(source_path, source_root)
            out_path = output_path_for(source_path, source_root, dest_root)
            route = relative_posix(out_path.with_suffix(""), DOCS_ROOT)
            if route.endswith("/index"):
                route = route[: -len("/index")]
            url = f"/ai-investing/{route}/"

            keys = {
                rel,
                rel[:-3] if rel.endswith(".md") else rel,
                f"{source_root.name}/{rel}",
                f"{source_root.name}/{rel[:-3]}" if rel.endswith(".md") else f"{source_root.name}/{rel}",
            }
            for key in keys:
                path_map[key] = url

            basename = source_path.stem
            if basename not in basename_map:
                basename_map[basename] = url
            else:
                basename_map[basename] = ""

    return path_map, basename_map


def raw_link(path_text: str) -> str:
    cleaned = path_text.strip().strip("`'\"，。；;),")
    href = f"{GITHUB_BLOB}/{quote(cleaned, safe='/()[]-_.~')}"
    label = cleaned.replace("03-raw/", "") or cleaned
    return (
        '<details class="raw-ref">'
        "<summary>查看原始资料</summary>"
        f'<a href="{href}" target="_blank" rel="noreferrer">{label}</a>'
        "</details>"
    )


def transform_wikilinks(text: str, path_map: dict[str, str], basename_map: dict[str, str]) -> str:
    pattern = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

    def repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = (match.group(2) or Path(target).stem).strip()
        normalized = target[:-3] if target.endswith(".md") else target

        if normalized.startswith("03-raw/"):
            return raw_link(normalized)

        url = path_map.get(target) or path_map.get(normalized)
        if not url and "/" not in normalized:
            url = basename_map.get(normalized)
        if url:
            return f"[{label}]({url})"
        return label

    return pattern.sub(repl, text)


RAW_FILE_PATTERN = re.compile(r"(03-raw/.*?\.md)")
RAW_DIR_PATTERN = re.compile(r"(?<![\w/])(03-raw/[A-Za-z0-9_\-/]+/?)")


def append_raw_reference_boxes(text: str) -> str:
    refs: list[str] = []
    for pattern in (RAW_FILE_PATTERN, RAW_DIR_PATTERN):
        for match in pattern.finditer(text):
            ref = match.group(1).strip().strip("`'\"，。；;),")
            if ref not in refs:
                refs.append(ref)
    refs = [
        ref
        for ref in refs
        if not any(other != ref and other.startswith(ref) for other in refs)
    ]
    if not refs:
        return text

    boxes = "\n\n## 原始资料链接\n\n" + "\n".join(raw_link(ref) for ref in refs) + "\n"
    return text.rstrip() + boxes


def transform_markdown(
    source_path: Path,
    source_root: Path,
    path_map: dict[str, str],
    basename_map: dict[str, str],
) -> str:
    original = read_text(source_path)
    title = get_title(source_path, original)
    body = strip_frontmatter(original).lstrip()
    body = remove_duplicate_h1(body, title)
    body = transform_wikilinks(body, path_map, basename_map)
    body = append_raw_reference_boxes(body)
    source_rel = relative_posix(source_path, ROOT)
    source_href = f"{GITHUB_BLOB}/{quote(source_rel, safe='/()[]-_.~')}"
    body += (
        "\n\n---\n\n"
        '<p class="source-path">仓库源文件：'
        f'<a href="{source_href}" target="_blank" rel="noreferrer">{source_rel}</a>'
        "</p>\n"
    )
    return frontmatter(title, f"Generated from {source_rel}") + body


def write_index(dest: Path, title: str, description: str, links: list[tuple[str, str]]) -> None:
    lines = [frontmatter(title, description)]
    for label, href in links:
        lines.append(f"- [{label}]({href})")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def directory_sort_key(item: Path) -> tuple[int, str]:
    if item.parent == KB_SRC / "hypotheses":
        prefix = item.name.split("-", 1)[0].upper()
        return ({"G": 0, "S": 1, "R": 2}.get(prefix, 99), item.name.lower())
    return (0, item.name.lower())


def append_index_tree(lines: list[str], source_dir: Path, source_root: Path, dest_root: Path, depth: int = 2) -> None:
    for source_path in markdown_files(source_dir):
        link = f"/ai-investing/{sidebar_slug_for(source_path, source_root, dest_root)}/"
        title = get_title(source_path, read_text(source_path))
        lines.append(f"- [{title}]({link})")

    for child in sorted((item for item in source_dir.iterdir() if item.is_dir()), key=directory_sort_key):
        child_title = clean_dir_label(child.name)
        child_link = f"/ai-investing/{sidebar_slug_for_source_dir(child, source_root, dest_root)}/"
        lines.append("")
        lines.append(f"{'#' * depth} [{child_title}]({child_link})")
        lines.append("")
        append_index_tree(lines, child, source_root, dest_root, min(depth + 1, 6))


def write_directory_overview(source_dir: Path, source_root: Path, dest_root: Path) -> None:
    rel = source_dir.relative_to(source_root)
    if rel == Path("."):
        return

    title = clean_dir_label(source_dir.name)
    description = f"{title} 下的全部子标题索引"
    lines = [frontmatter(title, description)]
    lines.append("这个页面汇总当前栏目下所有层级的子标题，方便直接进入最底层内容。")
    lines.append("")
    append_index_tree(lines, source_dir, source_root, dest_root)

    out_path = output_dir_for_source_dir(source_dir, source_root, dest_root) / "index.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_directory_overviews(source_root: Path, dest_root: Path) -> None:
    for source_dir in sorted((item for item in source_root.rglob("*") if item.is_dir()), key=lambda item: item.as_posix()):
        if any(markdown_files(source_dir)) or any(child.is_dir() for child in source_dir.iterdir()):
            write_directory_overview(source_dir, source_root, dest_root)


def sidebar_link(source_path: Path, source_root: Path, dest_root: Path) -> dict[str, str]:
    text = read_text(source_path)
    return {
        "label": get_title(source_path, text),
        "slug": sidebar_slug_for(source_path, source_root, dest_root),
    }


def markdown_files(path: Path) -> list[Path]:
    return sorted(
        (item for item in path.glob("*.md") if item.name.lower() != "index.md"),
        key=lambda item: item.name.lower(),
    )


def build_tree_sidebar(path: Path, source_root: Path, dest_root: Path) -> list[dict[str, object]]:
    items: list[dict[str, object]] = [
        {
            "label": "总览",
            "slug": sidebar_slug_for_source_dir(path, source_root, dest_root),
        },
    ]
    items.extend(
        sidebar_link(source_path, source_root, dest_root)
        for source_path in markdown_files(path)
    )

    for child in sorted((item for item in path.iterdir() if item.is_dir()), key=directory_sort_key):
        child_items = build_tree_sidebar(child, source_root, dest_root)
        if child_items:
            items.append(
                {
                    "label": clean_dir_label(child.name),
                    "collapsed": True,
                    "items": child_items,
                }
            )
    return items


def build_flat_sidebar(path: Path, source_root: Path, dest_root: Path) -> list[dict[str, str]]:
    return [
        {
            "label": "总览",
            "slug": sidebar_slug_for_source_dir(path, source_root, dest_root),
        },
        *[sidebar_link(source_path, source_root, dest_root) for source_path in markdown_files(path)],
    ]


def build_output_sidebar(category: str) -> list[dict[str, str]]:
    items = []
    for source_path in OUTPUT_SRC.rglob("*.md"):
        if source_path.name.lower() == "index.md":
            continue
        rel = normalize_rel(source_path, OUTPUT_SRC)
        if rel.parts and rel.parts[0] == category:
            items.append(sidebar_link(source_path, OUTPUT_SRC, OUTPUT_DEST))
    source_dir = OUTPUT_SRC / category
    overview = {
        "label": "总览",
        "slug": sidebar_slug_for_source_dir(source_dir, OUTPUT_SRC, OUTPUT_DEST),
    }
    return [overview, *sorted(items, key=lambda item: item["label"])]


def write_generated_sidebar() -> None:
    sidebar: list[dict[str, object]] = [
        {
            "label": "02-kb 知识库",
            "items": [
                {"label": "总索引", "slug": "kb"},
                {
                    "label": CATEGORY_LABELS["entities"],
                    "collapsed": True,
                    "items": build_flat_sidebar(KB_SRC / "entities", KB_SRC, KB_DEST),
                },
                {
                    "label": CATEGORY_LABELS["concepts"],
                    "collapsed": True,
                    "items": build_tree_sidebar(KB_SRC / "concepts", KB_SRC, KB_DEST),
                },
                {
                    "label": CATEGORY_LABELS["hypotheses"],
                    "collapsed": True,
                    "items": build_tree_sidebar(KB_SRC / "hypotheses", KB_SRC, KB_DEST),
                },
                {
                    "label": CATEGORY_LABELS["sources"],
                    "collapsed": True,
                    "items": build_flat_sidebar(KB_SRC / "sources", KB_SRC, KB_DEST),
                },
            ],
        },
        {
            "label": "04-output 输出",
            "items": [
                {"label": "输出总览", "slug": "outputs"},
                {
                    "label": CATEGORY_LABELS["reports"],
                    "collapsed": True,
                    "items": build_output_sidebar("reports"),
                },
                {
                    "label": CATEGORY_LABELS["tracking"],
                    "collapsed": True,
                    "items": build_output_sidebar("tracking"),
                },
                {
                    "label": CATEGORY_LABELS["weekly"],
                    "collapsed": True,
                    "items": build_output_sidebar("weekly"),
                },
            ],
        },
    ]
    sidebar_content = "export default " + json.dumps(sidebar, ensure_ascii=False, indent=2) + ";\n"
    with SIDEBAR_DEST.open("w", encoding="utf-8", newline="\n") as file:
        file.write(sidebar_content)


def generate() -> None:
    reset_dir(KB_DEST)
    reset_dir(OUTPUT_DEST)
    path_map, basename_map = build_maps()

    for source_root, dest_root in ((KB_SRC, KB_DEST), (OUTPUT_SRC, OUTPUT_DEST)):
        for source_path in source_root.rglob("*.md"):
            out_path = output_path_for(source_path, source_root, dest_root)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(
                transform_markdown(source_path, source_root, path_map, basename_map),
                encoding="utf-8",
            )

    kb_links = []
    for key in ("entities", "concepts", "hypotheses", "sources"):
        href = f"/ai-investing/kb/{slugify(key)}/"
        kb_links.append((CATEGORY_LABELS[key], href))
    if not (KB_DEST / "index.md").exists():
        write_index(KB_DEST / "index.md", "02-kb 结构化知识库", "02-kb generated entry", kb_links)
    write_directory_overviews(KB_SRC, KB_DEST)

    output_links = []
    for key in ("reports", "tracking", "weekly"):
        href = f"/ai-investing/outputs/{slugify(key)}/"
        output_links.append((CATEGORY_LABELS[key], href))
    write_index(OUTPUT_DEST / "index.md", "04-output 输出区", "04-output generated entry", output_links)
    write_directory_overviews(OUTPUT_SRC, OUTPUT_DEST)
    write_generated_sidebar()

    for source, destination in DASHBOARD_FILES.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)

    print("Generated Starlight content from 02-kb and 04-output.")


if __name__ == "__main__":
    generate()
