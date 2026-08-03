#!/usr/bin/env python3
"""
Review newly synced Feishu raw files against the current knowledge-ingest rules.

The script is intentionally conservative:
- it writes raw sync review reports under 05-meta/ingest-reviews;
- it can create source-card drafts for G2 storage-relevant files;
- it does not update hypotheses, concepts, entities, or certainty automatically.
"""
import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


RAW_ROOT = Path("03-raw/feishu")
SOURCE_DIR = Path("02-kb/sources")
LOG_FILE = Path("02-kb/log.md")
REVIEW_DIR = Path("05-meta/ingest-reviews")

G2_KEYWORDS = {
    "hbm": ("HBM", "HBM"),
    "hbm3e": ("HBM", "HBM3E"),
    "hbm4": ("HBM", "HBM4"),
    "dram": ("DRAM", "DRAM"),
    "ddr5": ("DRAM", "DDR5"),
    "nand": ("NAND", "NAND"),
    "ssd": ("NAND", "SSD"),
    "qlc": ("NAND", "QLC"),
    "存储": ("memory", "存储"),
    "內存": ("memory", "内存"),
    "内存": ("memory", "内存"),
    "海力士": ("company", "SK Hynix"),
    "hynix": ("company", "SK Hynix"),
    "美光": ("company", "Micron"),
    "micron": ("company", "Micron"),
    "三星": ("company", "Samsung"),
    "samsung": ("company", "Samsung"),
    "台积电": ("company", "TSMC"),
    "tsmc": ("company", "TSMC"),
    "cowos": ("supply_chain", "CoWoS"),
    "b200": ("ai_compute", "B200"),
    "blackwell": ("ai_compute", "Blackwell"),
    "capex": ("ai_compute", "CAPEX"),
    "长约": ("contract", "LTA"),
    "lta": ("contract", "LTA"),
    "产能": ("capacity", "产能"),
    "价格": ("pricing", "价格"),
    "涨价": ("pricing", "涨价"),
}

QUESTION_RULES = [
    ("HBM 产能、长约、认证、稼动率", {"hbm", "hbm3e", "hbm4", "海力士", "hynix", "美光", "micron", "三星", "samsung", "长约", "lta", "产能"}),
    ("HBM4/HBM4e 单 GPU 价值量", {"hbm4", "hbm", "b200", "blackwell", "价格", "涨价"}),
    ("DDR5 产能是否被 HBM 挤占", {"ddr5", "dram", "hbm", "产能"}),
    ("NAND/SSD 是否被 AI 推理或企业 SSD 拉动", {"nand", "ssd", "qlc", "存储"}),
    ("SK Hynix、Micron、Samsung、TSMC 与 HBM 供应链关系", {"海力士", "hynix", "美光", "micron", "三星", "samsung", "台积电", "tsmc", "cowos", "hbm"}),
]


@dataclass
class ReviewItem:
    path: Path
    title: str
    raw_date: str
    score: int
    matched_terms: list[str]
    matched_questions: list[str]
    should_distill: bool
    reason: str
    source_card: Path | None = None


def read_text(path):
    return path.read_text(encoding="utf-8", errors="ignore")


def normalize_rel(path):
    return Path(path).as_posix()


def title_from_path(path):
    return path.stem.strip()


def date_from_title(title):
    match = re.search(r"(20\d{2})[-_.年 ]?(\d{1,2})[-_.月 ]?(\d{1,2})", title)
    if not match:
        return datetime.now().strftime("%Y-%m-%d")
    year, month, day = match.groups()
    return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"


def file_digest(path):
    return hashlib.md5(path.read_bytes()).hexdigest()[:10]


def classify(path, min_score):
    title = title_from_path(path)
    text = read_text(path)
    haystack = f"{title}\n{text[:50000]}".lower()

    matched = []
    categories = set()
    for key, (category, label) in G2_KEYWORDS.items():
        if key.lower() in haystack:
            matched.append(label)
            categories.add(category)

    matched_questions = []
    for question, terms in QUESTION_RULES:
        if any(term.lower() in haystack for term in terms):
            matched_questions.append(question)

    score = len(set(matched)) + len(matched_questions)
    has_core_memory_term = bool({"HBM", "DRAM", "DDR5", "NAND", "SSD", "SK Hynix", "Micron", "Samsung"} & set(matched))
    should_distill = score >= min_score and has_core_memory_term

    if should_distill:
        reason = "命中当前 G2 存储小循环，建议进入 distill 人工复核。"
    elif matched:
        reason = "有弱相关信号，但未达到当前 G2 入库门槛，保留在 raw。"
    else:
        reason = "未命中当前 G2 入库关键词，保留在 raw。"

    return ReviewItem(
        path=path,
        title=title,
        raw_date=date_from_title(title),
        score=score,
        matched_terms=sorted(set(matched)),
        matched_questions=matched_questions,
        should_distill=should_distill,
        reason=reason,
    )


def slug_for(item):
    term_slugs = []
    mapping = {
        "SK Hynix": "sk-hynix",
        "Micron": "micron",
        "Samsung": "samsung",
        "TSMC": "tsmc",
        "HBM": "hbm",
        "HBM3E": "hbm3e",
        "HBM4": "hbm4",
        "DRAM": "dram",
        "DDR5": "ddr5",
        "NAND": "nand",
        "SSD": "ssd",
        "CoWoS": "cowos",
        "B200": "b200",
        "Blackwell": "blackwell",
        "CAPEX": "capex",
        "LTA": "lta",
    }
    for term in item.matched_terms:
        if term in mapping and mapping[term] not in term_slugs:
            term_slugs.append(mapping[term])
    base = "-".join(term_slugs[:4]) or f"doc-{file_digest(item.path)}"
    return f"{item.raw_date}-feishu-{base}"


def existing_source_card_for(raw_path):
    rel = normalize_rel(raw_path)
    if not SOURCE_DIR.exists():
        return None
    for path in SOURCE_DIR.glob("*.md"):
        try:
            if rel in read_text(path):
                return path
        except UnicodeDecodeError:
            continue
    return None


def build_source_card(item):
    existing = existing_source_card_for(item.path)
    if existing:
        item.source_card = existing
        return existing

    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    base = slug_for(item)
    out = SOURCE_DIR / f"{base}.md"
    counter = 2
    while out.exists():
        out = SOURCE_DIR / f"{base}-{counter}.md"
        counter += 1

    rel_raw = normalize_rel(item.path)
    now = datetime.now().strftime("%Y-%m-%d")
    questions = "\n".join(f"- {q}" for q in item.matched_questions) or "- 待人工判断"
    terms = "、".join(item.matched_terms) or "无"
    content = f"""---
title: "来源摘要：{item.title}"
source_type: "feishu/auto-review"
source_path: "{rel_raw}"
author: "Feishu 同步资料"
published_at: "{item.raw_date}"
ingested_at: "{now}"
confidence: "待人工复核"
---

# 来源摘要：{item.title}

## 信源信息

| 字段 | 内容 |
|---|---|
| 来源平台 | Feishu |
| 来源类型 | auto-review raw sync |
| 原始资料 | `{rel_raw}` |
| 重复/同源资料 | 待人工判断 |
| 原始标题 | {item.title} |
| 作者/机构 | 未知 |
| 原始发布日期 | {item.raw_date} |
| 入库日期 | {now} |
| 原始链接 | 无 |
| 外部核验 | 未核验 |
| 置信度 | 待人工复核 |

> 说明：本卡由脚本按当前 G2 存储入库规则预生成，只代表“值得人工 distill”，不等同于外部事实核验，也不自动调整 hypotheses certainty。

## 一句话结论

待人工阅读原文后补充。机器预筛命中：{terms}。

## 相关入库问题

{questions}

## 核心观点

1. **待人工提炼**
   - 请从原文中保留关键数字、公司名、时间口径和证据方向。

2. **证据方向待判断**
   - 标注为支持、反驳、中性或待验证；社区观点、传闻和未核验数据不要直接写成事实。

## 可入库信息

| 入库位置 | 信息 | 用途 |
|---|---|---|
| `hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | 待人工判断 | 判断是否改变 G2 证据链或反证边界 |
| `concepts/L2-芯片层（Chips）/供需周期与供应链/存储产业链与周期（HBM、DRAM、NAND）.md` | 待人工判断 | 判断是否补充存储周期/成长分层框架 |
| `entities/...` | 待人工判断 | 判断是否涉及 SK Hynix、Micron、Samsung、TSMC 或其他实体 |

## 需要跟踪的指标

1. 待人工补充。
2. 待人工补充。
3. 待人工补充。

## 置信度说明

- 机器预筛分数：{item.score}。
- 仍需外部核验：涉及产能、价格、市场份额、订单、CAPEX 或公司行为的判断。
"""
    out.write_text(content, encoding="utf-8")
    item.source_card = out
    return out


def load_manifest(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [Path(p) for p in data.get("saved_files", [])]


def collect_paths(args):
    paths = []
    if args.files:
        paths.extend(Path(p) for p in args.files)
    if args.from_manifest:
        manifest = Path(args.from_manifest)
        if manifest.exists():
            paths.extend(load_manifest(manifest))
    if args.all:
        paths.extend(RAW_ROOT.rglob("*.md"))

    seen = set()
    existing = []
    for path in paths:
        if path.suffix.lower() != ".md":
            continue
        key = normalize_rel(path)
        if key in seen:
            continue
        seen.add(key)
        if path.exists():
            existing.append(path)
    return existing


def write_review(items, created_cards):
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    out = REVIEW_DIR / f"{today}-feishu-auto-ingest-review.md"
    counter = 2
    while out.exists():
        out = REVIEW_DIR / f"{today}-feishu-auto-ingest-review-{counter}.md"
        counter += 1

    candidates = [item for item in items if item.should_distill]
    raw_only = [item for item in items if not item.should_distill]
    lines = [
        f"# Feishu 自动入库评审：{today}",
        "",
        "## 结论",
        "",
        f"- 本次评审 raw 文件：{len(items)} 个",
        f"- 建议进入 distill：{len(candidates)} 个",
        f"- 仅保留 raw：{len(raw_only)} 个",
        f"- 新建来源卡片：{len(created_cards)} 个",
        "",
        "本报告由脚本按当前 G2 存储小循环规则生成；它只做预筛，不代表事实核验，也不自动更新假设 certainty。",
        "",
        "## 建议进入 distill",
        "",
    ]

    if candidates:
        lines.extend(["| raw 文件 | 分数 | 命中项 | 来源卡 | 判断 |", "|---|---:|---|---|---|"])
        for item in candidates:
            source = normalize_rel(item.source_card) if item.source_card else "未创建"
            lines.append(f"| `{normalize_rel(item.path)}` | {item.score} | {', '.join(item.matched_terms)} | `{source}` | {item.reason} |")
    else:
        lines.append("无。")

    lines.extend(["", "## 仅保留 raw", ""])
    if raw_only:
        lines.extend(["| raw 文件 | 分数 | 命中项 | 判断 |", "|---|---:|---|---|"])
        for item in raw_only:
            terms = ", ".join(item.matched_terms) if item.matched_terms else "无"
            lines.append(f"| `{normalize_rel(item.path)}` | {item.score} | {terms} | {item.reason} |")
    else:
        lines.append("无。")

    lines.extend(["", "## 当前入库门槛", ""])
    lines.extend([
        "- 是否改变 G2 的判断方向或 certainty。",
        "- 是否补强或反驳 G2 的关键证据链。",
        "- 是否更新存储产业链与周期概念框架。",
        "- 是否需要进入周度复盘。",
    ])

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def append_log(report, cards):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    card_text = f"，新建 {len(cards)} 张来源卡" if cards else ""
    line = f"- {timestamp} [auto-review] {normalize_rel(report)} GitHub Actions/Codex Feishu 同步后自动入库预筛{card_text}\n"
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(line)


def main():
    parser = argparse.ArgumentParser(description="Review Feishu raw files for knowledge ingest.")
    parser.add_argument("--from-manifest", help="Path to sync manifest generated by sync_feishu_drive.py")
    parser.add_argument("--files", nargs="*", help="Specific raw markdown files to review")
    parser.add_argument("--all", action="store_true", help="Review all 03-raw/feishu markdown files")
    parser.add_argument("--write-source-cards", action="store_true", help="Create source-card drafts for relevant files")
    parser.add_argument("--write-log", action="store_true", help="Append a line to 02-kb/log.md")
    parser.add_argument("--min-score", type=int, default=4, help="Minimum score for distill recommendation")
    args = parser.parse_args()

    paths = collect_paths(args)
    if not paths:
        print("No Feishu raw files to review.")
        return 0

    items = [classify(path, args.min_score) for path in paths]
    created_cards = []
    if args.write_source_cards:
        for item in items:
            if item.should_distill:
                before = set(SOURCE_DIR.glob("*.md")) if SOURCE_DIR.exists() else set()
                card = build_source_card(item)
                after = set(SOURCE_DIR.glob("*.md")) if SOURCE_DIR.exists() else set()
                if card and card in (after - before):
                    created_cards.append(card)

    report = write_review(items, created_cards)
    if args.write_log:
        append_log(report, created_cards)

    print(f"Reviewed {len(items)} Feishu raw file(s).")
    print(f"Distill candidates: {sum(1 for item in items if item.should_distill)}")
    print(f"Review report: {report}")
    if created_cards:
        print("Created source cards:")
        for card in created_cards:
            print(f"  - {card}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
