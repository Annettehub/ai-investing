#!/usr/bin/env python3
"""Build the read-only homepage dashboard from recent Git history."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "site" / "src" / "data" / "home-dashboard.json"
BASE = "/ai-investing"
GITHUB_BLOB = "https://github.com/Annettehub/ai-investing/blob/main"


def slugify(value: str) -> str:
    value = value.replace(".md", "")
    overrides = {
        "concepts": "concepts",
        "entities": "entities",
        "hypotheses": "hypotheses",
        "sources": "sources",
        "research": "research",
        "reports": "reports",
        "tracking": "tracking",
        "today": "today",
        "weekly": "weekly",
    }
    if value in overrides:
        return overrides[value]
    ascii_part = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]
    return f"{ascii_part[:42]}-{digest}" if ascii_part else f"p-{digest}"


def title_for(path: Path) -> str:
    if not path.exists() or path.suffix.lower() != ".md":
        return path.stem
    text = path.read_text(encoding="utf-8", errors="replace")
    frontmatter = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.DOTALL)
    if frontmatter:
        match = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", frontmatter.group(1), flags=re.MULTILINE)
        if match:
            title = match.group(1).strip().strip("\"'")
            if title.casefold() not in {"info", "title", "untitled"}:
                return title
            return path.stem
    match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else path.stem


def excerpt_for(path: Path, title: str) -> str:
    """Return the first useful prose passage instead of frontmatter or headings."""
    if not path.exists() or path.suffix.lower() != ".md":
        return "打开原文查看本次新增内容。"

    text = path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"^---\s*\n.*?\n---\s*", "", text, count=1, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    candidates: list[str] = []
    in_code = False

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line or line.startswith(("#", "|", "---", ":::")):
            continue
        line = re.sub(r"^\s*(?:[-*+] |\d+[.)]\s+|>\s*)", "", line)
        line = re.sub(r"!\[[^]]*]\([^)]*\)", "", line)
        line = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", line)
        line = re.sub(r"[`*_~]", "", line)
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if (
            not line
            or line == title
            or len(line) < 12
            or re.match(
                r"^(概念编号|旧编号|建立日期|最后更新|专栏支撑|核心标的|来源文件|原始来源|"
                r"certainty|status|date|source|tags|aliases)[：:]",
                line,
                flags=re.I,
            )
        ):
            continue
        candidates.append(line)
        if sum(len(item) for item in candidates) >= 150:
            break

    excerpt = " ".join(candidates)
    if not excerpt:
        return "打开原文查看本次新增内容。"
    return excerpt[:180].rstrip("，。；;：: ") + ("…" if len(excerpt) > 180 else "。")


def location_for(kind: str) -> str:
    return {
        "raw": "03-raw 原始资料",
        "review": "05-meta 入库评审",
        "entity": "02-kb 公司档案",
        "concept": "02-kb 五层框架",
        "hypothesis": "02-kb 投资假设",
        "source": "02-kb 来源摘要",
        "report": "04-output 研究报告",
        "tracking": "04-output 长期跟踪",
        "weekly": "04-output 周度复盘",
        "output": "04-output 输出沉淀",
    }.get(kind, "知识库")


def loop_stage_for(kind: str) -> str:
    return {
        "raw": "原料进入",
        "review": "人工评审",
        "entity": "知识回写",
        "concept": "知识回写",
        "hypothesis": "假设回写",
        "source": "来源编译",
        "report": "输出沉淀",
        "tracking": "跟踪更新",
        "weekly": "周期复盘",
        "output": "输出沉淀",
    }.get(kind, "知识循环")


def infer_routes(path_text: str, content: str) -> list[str]:
    """Give the homepage a cautious topic hint, not an automatic ingest decision."""
    tags = gsr_tags(path_text, content)
    if tags:
        return tags[:5]

    haystack = f"{path_text}\n{content}".lower()
    keyword_routes = [
        ("G2", ("hbm", "dram", "nand", "存储", "内存", "lta")),
        ("S2", ("光刻", "先进封装", "cowos", "国产替代", "光科芯图")),
        ("S1", ("gpu", "asic", "blackwell", "加速器", "cpu")),
        ("R2", ("agent", "workbuddy", "应用层", "roi", "token")),
        ("G1", ("capex", "资本开支", "算力", "数据中心")),
    ]
    return [route for route, keywords in keyword_routes if any(keyword in haystack for keyword in keywords)][:5]


def loop_detail(kind: str, path: Path, review_counts: tuple[int, int] | None = None) -> str:
    if kind == "raw":
        return "已归档至 03-raw，尚未写入 02-kb"
    if kind == "review":
        suggested, raw_only = review_counts or (0, 0)
        return f"本批建议进入 distill {suggested} 篇；{raw_only} 篇仅保留原料，等待人工确认"
    if kind in {"entity", "concept", "hypothesis", "source"}:
        return "已写入 02-kb，可继续进入当前知识页核对编译结果"
    if kind in {"report", "tracking", "weekly", "output"}:
        return "已沉淀至 04-output，作为后续复盘和跟踪依据"
    return "已进入知识循环"


def link_label(kind: str) -> str:
    return "查看原文" if kind in {"raw", "review"} else "查看知识页"


def classify(path: str) -> tuple[str, str]:
    if path.startswith("03-raw/"):
        return "raw", "原始资料"
    if path.startswith("05-meta/ingest-reviews/"):
        return "review", "入库评审"
    if path.startswith("02-kb/entities/"):
        return "entity", "公司"
    if path.startswith("02-kb/concepts/"):
        return "concept", "概念"
    if path.startswith("02-kb/hypotheses/"):
        return "hypothesis", "假设"
    if path.startswith("02-kb/sources/"):
        return "source", "来源卡"
    if path.startswith("04-output/reports/") or path.startswith("04-output/research/"):
        return "report", "研究报告"
    if path.startswith("04-output/tracking/"):
        return "tracking", "长期跟踪"
    if path.startswith("04-output/weekly/"):
        return "weekly", "周度复盘"
    if path.startswith("04-output/"):
        return "output", "输出"
    return "other", "系统"


def normalize_output_parts(path: Path) -> tuple[str, list[str]]:
    parts = list(path.parts)
    root = "kb" if parts[0] == "02-kb" else "outputs"
    rel = parts[1:]
    if parts[0] == "04-output" and len(rel) == 1 and path.suffix.lower() == ".md":
        stem = path.stem
        bucket = "today" if stem.startswith("today-") else "weekly" if re.search(r"\d{4}-W\d{2}", stem, re.I) or "周度复盘" in stem else "research"
        rel = [bucket, path.name]
    return root, rel


def href_for(path_text: str) -> str:
    path = Path(path_text)
    if path_text.startswith(("02-kb/", "04-output/")) and path.suffix.lower() == ".md":
        root, rel = normalize_output_parts(path)
        dirs = [slugify(part) for part in rel[:-1]]
        if rel[-1].lower() == "index.md":
            route = "/".join([root, *dirs])
        else:
            route = "/".join([root, *dirs, slugify(Path(rel[-1]).stem)])
        return f"{BASE}/{route}/"
    return f"{GITHUB_BLOB}/{quote(path_text, safe='/()[]-_.~')}"


def git_history() -> list[dict[str, str]]:
    command = [
        "git", "log", "--since=7 days ago", "--date=short",
        "--pretty=format:@@@%H|%ad|%s", "--name-only",
    ]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True)
    commits: list[dict[str, str]] = []
    current: dict[str, object] | None = None
    for raw_line in result.stdout.splitlines():
        line = raw_line.strip()
        if line.startswith("@@@"):
            sha, commit_date, subject = line[3:].split("|", 2)
            current = {"sha": sha, "date": commit_date, "subject": subject, "files": []}
            commits.append(current)  # type: ignore[arg-type]
        elif line and current is not None:
            current["files"].append(line)  # type: ignore[union-attr]
    return commits


def review_summary(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    suggested = re.search(r"建议进入 distill[：:]\s*(\d+)", text)
    raw_only = re.search(r"仅保留 raw[：:]\s*(\d+)", text)
    return int(suggested.group(1)) if suggested else 0, int(raw_only.group(1)) if raw_only else 0


def gsr_tags(path_text: str, content: str = "") -> list[str]:
    haystack = f"{path_text}\n{content}"
    tags = re.findall(r"(?<![A-Z0-9])([GSR]\d(?:\.\d+)?)(?![A-Z0-9])", haystack, flags=re.I)
    return list(dict.fromkeys(tag.upper() for tag in tags))[:6]


def build() -> dict[str, object]:
    today = date.today()
    start = today - timedelta(days=6)
    commits = git_history()
    seen: set[str] = set()
    recent: list[dict[str, object]] = []
    reviews: list[dict[str, object]] = []
    daily: dict[str, Counter[str]] = defaultdict(Counter)
    totals: Counter[str] = Counter()
    impacts: Counter[str] = Counter()

    for commit in commits:
        commit_date = str(commit["date"])
        if commit_date < start.isoformat():
            continue
        for path_text in commit["files"]:  # type: ignore[index]
            if path_text in seen:
                continue
            seen.add(path_text)
            kind, label = classify(path_text)
            if kind == "other":
                continue
            if kind in {"raw", "review", "entity", "concept", "hypothesis", "source", "report", "tracking", "weekly", "output"} and not path_text.lower().endswith(".md"):
                continue
            path = ROOT / path_text
            title = title_for(path)
            content = path.read_text(encoding="utf-8", errors="replace") if path.exists() and path.suffix.lower() == ".md" else ""
            review_counts = review_summary(path) if kind == "review" else None
            routes = infer_routes(path_text, content)
            item = {
                "date": commit_date,
                "title": title,
                "kind": kind,
                "label": label,
                "href": href_for(path_text),
                "path": path_text,
                "subject": commit["subject"],
                "excerpt": excerpt_for(path, title),
                "location": location_for(kind),
                "loopStage": loop_stage_for(kind),
                "loopDetail": loop_detail(kind, path, review_counts),
                "routes": routes,
                "linkLabel": link_label(kind),
            }
            recent.append(item)
            totals[kind] += 1
            daily[commit_date][kind] += 1

            for tag in gsr_tags(path_text, content if kind in {"review", "hypothesis"} else ""):
                impacts[tag] += 1

            if kind == "review":
                suggested, raw_only = review_summary(path)
                reviews.append({**item, "suggested": suggested, "rawOnly": raw_only})

    dates = [(start + timedelta(days=offset)).isoformat() for offset in range(7)]
    series = [
        {
            "date": day,
            "raw": daily[day]["raw"],
            "review": daily[day]["review"],
            "knowledge": sum(daily[day][key] for key in ("entity", "concept", "hypothesis", "source")),
            "output": sum(daily[day][key] for key in ("report", "tracking", "weekly", "output")),
        }
        for day in dates
    ]
    knowledge_kinds = {"entity", "concept", "hypothesis", "source", "report", "tracking", "weekly", "output"}
    knowledge = [item for item in recent if item["kind"] in knowledge_kinds]

    data = {
        "meta": {
            "generatedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
            "start": start.isoformat(),
            "end": today.isoformat(),
        },
        "metrics": {
            "raw": totals["raw"],
            "reviews": totals["review"],
            "knowledge": len(knowledge),
            "outputs": sum(totals[key] for key in ("report", "tracking", "weekly", "output")),
        },
        "series": series,
        "recent": recent[:18],
        "knowledge": knowledge[:10],
        "reviews": reviews[:6],
        "impacts": [{"code": code, "count": count} for code, count in impacts.most_common(8)],
    }
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return data


if __name__ == "__main__":
    dashboard = build()
    print(f"Generated {DEST.relative_to(ROOT)} with {len(dashboard['recent'])} recent items.")
