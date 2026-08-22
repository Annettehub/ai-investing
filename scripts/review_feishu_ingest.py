#!/usr/bin/env python3
"""
Review newly synced Feishu raw files against the current knowledge-ingest rules.

The script is intentionally conservative:
- it writes raw sync review reports under 05-meta/ingest-reviews;
- it classifies material across G/S/R routes before recommending distill;
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

# Review routing is deliberately broader than the current G2 storage loop.
# A document may have one primary route and several cross-routes.
ROUTE_RULES = [
    {
        "route": "G1",
        "label": "需求与资本开支",
        "keywords": {"capex", "资本开支", "资本支出", "算力需求", "数据中心", "电力"},
        "targets": ["02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md"],
    },
    {
        "route": "G2",
        "label": "存储成长与周期",
        "keywords": {"hbm", "dram", "ddr5", "nand", "ssd", "qlc", "存储", "内存", "产能", "价格", "涨价", "长约", "lta"},
        "targets": ["02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md"],
    },
    {
        "route": "G3",
        "label": "推理需求与规模",
        "keywords": {"推理", "inference", "token", "agent", "模型调用", "用户量", "算力规模"},
        "targets": ["02-kb/hypotheses/G-需求与周期/G3-inference-demand-scale.md"],
    },
    {
        "route": "S1",
        "label": "芯片与加速器竞争结构",
        "keywords": {"gpu", "asic", "加速器", "cuda", "nvidia", "英伟达", "博通", "主权ai"},
        "targets": ["02-kb/hypotheses/S-产业结构与价值捕获/S1.1-chip-accelerator-competition.md"],
    },
    {
        "route": "S2",
        "label": "先进制造、封装与国产替代",
        "keywords": {
            "光刻", "光刻机", "全息光刻", "euv", "duv", "asml", "stepper", "scanner",
            "投影物镜", "先进封装", "曝光设备", "光刻胶", "纳米压印", "国产替代",
            "overlay", "throughput", "mask aligner", "芯碁微装", "上海微电子", "制程节点",
        },
        "targets": [
            "02-kb/hypotheses/S-产业结构与价值捕获/S2.1-advanced-manufacturing-packaging-localization.md",
            "02-kb/concepts/L2-芯片层（Chips）/技术路线/国产光刻机突围路线.md",
            "02-kb/concepts/L2-芯片层（Chips）/供需周期与供应链/先进封装生态（CoWoS、2.5D、3D封装）.md",
        ],
    },
    {
        "route": "S3",
        "label": "应用层价值捕获",
        "keywords": {"应用层", "roi", "回报", "商业化", "收入兑现", "价值捕获", "广告", "软件收入"},
        "targets": ["02-kb/hypotheses/S-产业结构与价值捕获/S3.1-application-value-capture.md"],
    },
    {
        "route": "R1",
        "label": "上游业绩兑现",
        "keywords": {"ai收入", "营收增长", "毛利率", "订单", "backlog", "业绩", "财报", "盈利"},
        "targets": ["02-kb/hypotheses/R-业绩兑现/R1-upstream-ai-infrastructure-earnings.md"],
    },
    {
        "route": "R2",
        "label": "下游回报兑现",
        "keywords": {"客户roi", "客户回报", "最终用户", "采用者", "留存率", "arr", "付费", "现金流"},
        "targets": ["02-kb/hypotheses/R-业绩兑现/R2-end-user-sustainable-roi.md"],
    },
]


@dataclass
class ReviewItem:
    path: Path
    title: str
    raw_date: str
    score: int
    matched_terms: list[str]
    matched_questions: list[str]
    routes: list[str]
    primary_route: str | None
    route_targets: list[str]
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
    route_scores = {}
    route_labels = {}
    route_targets = {}
    for rule in ROUTE_RULES:
        hits = sorted({keyword for keyword in rule["keywords"] if keyword.lower() in haystack})
        if hits:
            route = rule["route"]
            route_scores[route] = len(hits)
            route_labels[route] = rule["label"]
            route_targets[route] = rule["targets"]

    # One isolated word such as "收入" or "产能" is not enough to classify
    # a document. Keep only routes with at least two independent signals.
    routes = sorted(
        (route for route, route_score in route_scores.items() if route_score >= 2),
        key=lambda route: (-route_scores[route], route),
    )
    primary_route = routes[0] if routes else None
    primary_score = route_scores.get(primary_route, 0)
    should_distill = bool(primary_route and (primary_score >= 2 or score >= min_score))

    if should_distill:
        route_text = ", ".join(f"{route} {route_labels[route]}" for route in routes)
        reason = f"主路由为 {primary_route} {route_labels[primary_route]}；交叉命中：{route_text}，建议进入 distill 人工复核。"
    elif routes:
        reason = f"命中 {', '.join(routes)}，但证据密度不足，暂保留 raw。"
    else:
        reason = "未命中 G/S/R 入库路由，保留在 raw。"

    return ReviewItem(
        path=path,
        title=title,
        raw_date=date_from_title(title),
        score=score,
        matched_terms=sorted(set(matched)),
        matched_questions=matched_questions,
        routes=routes,
        primary_route=primary_route,
        route_targets=route_targets.get(primary_route, []),
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
        "本报告按 G/S/R 多维路由规则生成；每个路由至少需要两个主题信号。它只做预筛，不代表事实核验，也不自动更新假设 certainty。",
        "",
        "## 建议进入 distill",
        "",
    ]

    if candidates:
        lines.extend(["| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 来源卡 | 判断 |", "|---|---:|---|---|---|---|---|---|"])
        for item in candidates:
            source = normalize_rel(item.source_card) if item.source_card else "未创建"
            targets = "<br>".join(f"`{target}`" for target in item.route_targets) or "待人工判断"
            lines.append(f"| `{normalize_rel(item.path)}` | {item.score} | {item.primary_route or '无'} | {', '.join(item.routes) or '无'} | {targets} | {', '.join(item.matched_terms)} | `{source}` | {item.reason} |")
    else:
        lines.append("无。")

    lines.extend(["", "## 仅保留 raw", ""])
    if raw_only:
        lines.extend(["| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 判断 |", "|---|---:|---|---|---|---|---|"])
        for item in raw_only:
            terms = ", ".join(item.matched_terms) if item.matched_terms else "无"
            targets = "<br>".join(f"`{target}`" for target in item.route_targets) or "无"
            lines.append(f"| `{normalize_rel(item.path)}` | {item.score} | {item.primary_route or '无'} | {', '.join(item.routes) or '无'} | {targets} | {terms} | {item.reason} |")
    else:
        lines.append("无。")

    lines.extend(["", "## 当前入库门槛", ""])
    lines.extend([
        "- 先判断 G/S/R 主路由，再判断是否存在交叉证据。",
        "- 是否改变主路由对应假设的判断方向或 certainty。",
        "- 是否补强或反驳对应假设、概念框架或公司档案。",
        "- 涉及多个路由时，分别记录证据，不把偶然关键词当作主题归类。",
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
