#!/usr/bin/env python3
"""Sync official SEC earnings filings and XBRL facts for the US watchlist.

This is intentionally SEC-first: it uses free official EDGAR endpoints and
does not scrape unofficial transcript sites. Company-official earnings
materials filed as 8-K/6-K exhibits are captured as filing links.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import time
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "us-equity-watchlist.json"
STATE_PATH = ROOT / "05-meta" / "sec-earnings-state.json"
RAW_DIR = ROOT / "03-raw" / "sec" / "us-equity-earnings"
OUTPUT_DATA = ROOT / "04-output" / "data" / "us-equity-earnings-dashboard.json"
OUTPUT_TRACKING = ROOT / "04-output" / "tracking" / "us-equity-earnings-tracking.md"
R1_DASHBOARD = ROOT / "04-output" / "data" / "R1-upstream-dashboard.json"
R2_DASHBOARD = ROOT / "04-output" / "data" / "R2-downstream-dashboard.json"

DEFAULT_FORMS = {"10-Q", "10-K", "8-K", "20-F", "6-K"}
FACT_TAGS = {
    "revenue": [
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "Revenues",
        "SalesRevenueNet",
    ],
    "grossProfit": ["GrossProfit"],
    "operatingIncome": ["OperatingIncomeLoss"],
    "netIncome": ["NetIncomeLoss", "ProfitLoss"],
    "operatingCashFlow": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": [
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "PaymentsForAdditionsToPropertyPlantAndEquipment",
    ],
    "inventory": [
        "InventoryNet",
        "InventoryNetOfAllowancesCustomerAdvancesAndProgressBillings",
    ],
    "accountsReceivable": [
        "AccountsReceivableNetCurrent",
        "AccountsReceivableNet",
    ],
    "cash": [
        "CashAndCashEquivalentsAtCarryingValue",
        "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
    ],
    "researchAndDevelopment": ["ResearchAndDevelopmentExpense"],
}
INSTANT_METRICS = {"inventory", "accountsReceivable", "cash"}


def configure_stdio() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream and hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def read_json(path: Path, default: Any | None = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sec_user_agent() -> str:
    configured = os.getenv("SEC_USER_AGENT", "").strip()
    if configured:
        return configured
    return "AnnetteKnowledgeHub/0.1 Annettehub/ai-investing contact: unavailable"


def fetch_json(url: str, headers: dict[str, str] | None = None) -> Any:
    request = Request(url, headers=headers or {"User-Agent": sec_user_agent()})
    context = ssl.create_default_context()
    if hasattr(ssl, "VERIFY_X509_STRICT"):
        context.verify_flags &= ~ssl.VERIFY_X509_STRICT
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urlopen(request, timeout=35, context=context) as response:
                return json.loads(response.read().decode("utf-8-sig"))
        except HTTPError as exc:
            last_error = exc
            if exc.code in {403, 404}:
                raise
        except (URLError, TimeoutError) as exc:
            last_error = exc
        if attempt < 2:
            time.sleep(1.5 + attempt)
    assert last_error is not None
    raise last_error


def flatten_watchlist(config: dict[str, Any], groups: set[str] | None = None) -> list[dict[str, Any]]:
    companies: list[dict[str, Any]] = []
    for group in config.get("groups", []):
        if groups and group["id"] not in groups:
            continue
        for item in group.get("tickers", []):
            companies.append(
                {
                    **item,
                    "groupId": group["id"],
                    "groupLabel": group["label"],
                    "hypothesis": group["hypothesis"],
                }
            )
    return companies


def load_ticker_cik_map(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    data = fetch_json(config["sec"]["companyTickersUrl"])
    result: dict[str, dict[str, Any]] = {}
    for row in data.values():
        ticker = str(row.get("ticker", "")).upper()
        cik = str(row.get("cik_str", "")).zfill(10)
        if ticker and cik:
            result[ticker] = {
                "cik": cik,
                "secName": row.get("title") or ticker,
            }
    return result


def cik_no_zeros(cik: str) -> str:
    return str(int(cik))


def filing_url(cik: str, accession: str, primary_doc: str) -> str:
    accession_clean = accession.replace("-", "")
    return f"https://www.sec.gov/Archives/edgar/data/{cik_no_zeros(cik)}/{accession_clean}/{primary_doc}"


def filing_index_url(cik: str, accession: str) -> str:
    accession_clean = accession.replace("-", "")
    return f"https://www.sec.gov/Archives/edgar/data/{cik_no_zeros(cik)}/{accession_clean}/index.json"


def sec_filing_detail(cik: str, accession: str) -> dict[str, Any]:
    try:
        index = fetch_json(filing_index_url(cik, accession))
    except Exception as exc:
        return {"documents": [], "error": str(exc)}

    docs = []
    for item in index.get("directory", {}).get("item", []):
        name = item.get("name", "")
        if not name:
            continue
        lower = name.lower()
        if lower.endswith((".htm", ".html", ".txt", ".pdf")):
            docs.append(
                {
                    "name": name,
                    "url": filing_url(cik, accession, name),
                    "isEarningsExhibit": bool(re.search(r"(ex-?99|exhibit99|earnings|results)", lower)),
                }
            )
    return {"documents": docs}


def recent_filings(
    config: dict[str, Any],
    company: dict[str, Any],
    cik: str,
    days: int,
    include_forms: set[str],
    with_details: bool,
) -> list[dict[str, Any]]:
    submissions_url = config["sec"]["submissionsUrl"].format(cik=cik)
    data = fetch_json(submissions_url)
    recent = data.get("filings", {}).get("recent", {})
    rows = zip(
        recent.get("accessionNumber", []),
        recent.get("filingDate", []),
        recent.get("reportDate", []),
        recent.get("form", []),
        recent.get("primaryDocument", []),
        recent.get("items", []),
    )
    cutoff = date.today() - timedelta(days=days)
    filings: list[dict[str, Any]] = []
    for accession, filing_date, report_date, form, primary_doc, items in rows:
        if form not in include_forms:
            continue
        try:
            if date.fromisoformat(filing_date) < cutoff:
                continue
        except ValueError:
            pass

        row = {
            "ticker": company["ticker"],
            "name": company["name"],
            "group": company["groupLabel"],
            "hypothesis": company["hypothesis"],
            "cik": cik,
            "form": form,
            "filingDate": filing_date,
            "reportDate": report_date,
            "accessionNumber": accession,
            "items": items,
            "primaryDocument": primary_doc,
            "filingUrl": filing_url(cik, accession, primary_doc),
            "isPeriodicReport": form in {"10-Q", "10-K", "20-F"},
            "isEarningsCandidate": form in {"8-K", "6-K"} and bool(
                re.search(r"(2\.02|results|earnings|99\.1|99)", f"{items} {primary_doc}", re.I)
            ),
        }
        if with_details and row["isEarningsCandidate"]:
            row["detail"] = sec_filing_detail(cik, accession)
        filings.append(row)
    return filings


def unit_facts(concept: dict[str, Any]) -> list[dict[str, Any]]:
    units = concept.get("units", {})
    for unit in ("USD", "USD/shares", "shares", "pure"):
        if unit in units:
            return units[unit]
    return []


def select_latest_fact(company_facts: dict[str, Any], tags: list[str], instant: bool = False) -> dict[str, Any] | None:
    us_gaap = company_facts.get("facts", {}).get("us-gaap", {})
    candidates: list[dict[str, Any]] = []
    selected_tag = ""
    selected_label = ""
    recent_cutoff = date.today() - timedelta(days=730)

    for tag in tags:
        concept = us_gaap.get(tag)
        if not concept:
            continue
        for fact in unit_facts(concept):
            if fact.get("form") not in {"10-Q", "10-K", "20-F", "40-F"}:
                continue
            if fact.get("val") is None or not fact.get("filed") or not fact.get("end"):
                continue
            if not instant and not fact.get("start"):
                continue
            try:
                if date.fromisoformat(fact["end"]) < recent_cutoff:
                    continue
            except ValueError:
                continue
            candidates.append(fact)
        if candidates:
            selected_tag = tag
            selected_label = concept.get("label", tag)
            break

    if not candidates:
        return None

    def score(fact: dict[str, Any]) -> tuple[str, int, str]:
        duration_score = 0
        if not instant:
            try:
                days = (date.fromisoformat(fact["end"]) - date.fromisoformat(fact["start"])).days
                duration_score = 2 if 70 <= days <= 120 else 1 if 250 <= days <= 380 else 0
            except Exception:
                duration_score = 0
        return (fact["end"], duration_score, fact["filed"])

    latest = max(candidates, key=score)
    duration_days = None
    if not instant and latest.get("start"):
        try:
            duration_days = (date.fromisoformat(latest["end"]) - date.fromisoformat(latest["start"])).days
        except ValueError:
            duration_days = None
    return {
        "tag": selected_tag,
        "label": selected_label,
        "value": latest["val"],
        "periodStart": latest.get("start"),
        "periodEnd": latest.get("end"),
        "durationDays": duration_days,
        "filed": latest.get("filed"),
        "form": latest.get("form"),
        "frame": latest.get("frame"),
    }


def fetch_company_facts(config: dict[str, Any], company: dict[str, Any], cik: str) -> dict[str, Any]:
    facts_url = config["sec"]["companyFactsUrl"].format(cik=cik)
    data = fetch_json(facts_url)
    metrics = {
        metric: select_latest_fact(data, tags, instant=metric in INSTANT_METRICS)
        for metric, tags in FACT_TAGS.items()
    }
    revenue_fact = metrics.get("revenue")
    revenue = revenue_fact.get("value") if revenue_fact else None
    gross_fact = align_fact(metrics.get("grossProfit"), revenue_fact)
    operating_fact = align_fact(metrics.get("operatingIncome"), revenue_fact)
    cash_flow_fact = metrics.get("operatingCashFlow")
    capex_fact = align_fact(metrics.get("capex"), cash_flow_fact)
    gross_profit = gross_fact.get("value") if gross_fact else None
    operating_income = operating_fact.get("value") if operating_fact else None
    operating_cash_flow = cash_flow_fact.get("value") if cash_flow_fact else None
    capex = capex_fact.get("value") if capex_fact else None

    derived = {
        "grossMarginPct": pct(gross_profit, revenue),
        "operatingMarginPct": pct(operating_income, revenue),
        "freeCashFlow": (operating_cash_flow - capex) if isinstance(operating_cash_flow, (int, float)) and isinstance(capex, (int, float)) else None,
    }
    if capex_fact is not None:
        metrics["capex"] = capex_fact

    return {
        "ticker": company["ticker"],
        "name": company["name"],
        "secName": data.get("entityName"),
        "group": company["groupLabel"],
        "hypothesis": company["hypothesis"],
        "role": company["role"],
        "focus": company.get("focus", []),
        "cik": cik,
        "facts": metrics,
        "derived": derived,
    }


def pct(numerator: Any, denominator: Any) -> float | None:
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)) or denominator == 0:
        return None
    return round(numerator / denominator * 100, 2)


def align_fact(candidate: dict[str, Any] | None, anchor: dict[str, Any] | None) -> dict[str, Any] | None:
    """Avoid mixing facts from different reporting periods in derived metrics."""
    if not candidate or not anchor:
        return candidate
    if candidate.get("periodEnd") != anchor.get("periodEnd"):
        return None
    if candidate.get("durationDays") and anchor.get("durationDays"):
        if abs(candidate["durationDays"] - anchor["durationDays"]) > 35:
            return None
    return candidate


def money(value: Any) -> str:
    if not isinstance(value, (int, float)):
        return "—"
    abs_value = abs(value)
    if abs_value >= 1e9:
        return f"${value / 1e9:.1f}B"
    if abs_value >= 1e6:
        return f"${value / 1e6:.1f}M"
    return f"${value:,.0f}"


def load_state() -> dict[str, Any]:
    return read_json(STATE_PATH, {"seenAccessions": [], "runs": []})


def save_state(state: dict[str, Any], filings: list[dict[str, Any]]) -> None:
    seen = set(state.get("seenAccessions", []))
    for filing in filings:
        seen.add(filing["accessionNumber"])
    state["seenAccessions"] = sorted(seen)
    state.setdefault("runs", []).append(
        {
            "ranAt": datetime.now(UTC).isoformat(timespec="seconds"),
            "filingsChecked": len(filings),
            "newFilings": sum(1 for filing in filings if filing.get("isNew")),
        }
    )
    state["runs"] = state["runs"][-20:]
    write_json(STATE_PATH, state)


def markdown_report(snapshot: dict[str, Any]) -> str:
    lines = [
        f"# SEC 官方财报同步 {snapshot['asOf']}",
        "",
        "数据来源：SEC EDGAR `submissions` 与 `companyfacts` 官方接口。",
        "范围：半导体、云与应用 watchlist。电话会全文仅在公司通过 8-K/6-K 或附件披露时记录链接。",
        "",
        "## 本次新披露",
        "",
    ]
    new_filings = [filing for filing in snapshot["filings"] if filing.get("isNew")]
    if not new_filings:
        lines.extend(["本次未发现新的 watchlist 披露。", ""])
    else:
        lines.append("| 日期 | ticker | 表格 | 报告期 | 类型 | 官方链接 |")
        lines.append("|---|---|---|---|---|---|")
        for filing in new_filings:
            kind = "定期报告" if filing["isPeriodicReport"] else "业绩/公告候选" if filing["isEarningsCandidate"] else "其他披露"
            lines.append(
                f"| {filing['filingDate']} | {filing['ticker']} | {filing['form']} | {filing.get('reportDate') or '—'} | {kind} | [SEC]({filing['filingUrl']}) |"
            )
        lines.append("")

    lines.extend(["## 最新结构化指标", "", "| ticker | 分组 | 收入 | 毛利率 | 营业利润率 | CapEx | FCF | 指标期末 |"])
    lines.append("|---|---|---:|---:|---:|---:|---:|---|")
    for company in snapshot["companies"]:
        facts = company["facts"]
        derived = company["derived"]
        period = facts.get("revenue", {}).get("periodEnd") if facts.get("revenue") else "—"
        lines.append(
            "| {ticker} | {group} | {revenue} | {gm} | {om} | {capex} | {fcf} | {period} |".format(
                ticker=company["ticker"],
                group=company["group"],
                revenue=money(facts.get("revenue", {}).get("value") if facts.get("revenue") else None),
                gm=f"{derived['grossMarginPct']:.1f}%" if derived.get("grossMarginPct") is not None else "—",
                om=f"{derived['operatingMarginPct']:.1f}%" if derived.get("operatingMarginPct") is not None else "—",
                capex=money(facts.get("capex", {}).get("value") if facts.get("capex") else None),
                fcf=money(derived.get("freeCashFlow")),
                period=period,
            )
        )
    lines.extend(
        [
            "",
            "## G/S/R 使用说明",
            "",
            "- R1：优先看半导体、设备、代工、云厂商的收入、利润率、库存、CapEx 与 FCF 是否同步兑现。",
            "- R2：优先看应用软件和云厂商的 RPO、续费、利润率与现金流是否证明最终采用者愿意持续付费。",
            "- SEC 数字是事实锚点；AI 分部收入、订单、电话会叙事仍需公司 IR、8-K 附件或人工补充材料交叉验证。",
            "",
        ]
    )
    return "\n".join(lines)


def tracking_markdown(snapshot: dict[str, Any]) -> str:
    lines = [
        "---",
        'title: "美股财报长期跟踪表"',
        'description: "半导体与云/应用公司 SEC 官方财报指标跟踪"',
        "---",
        "",
        "# 美股财报长期跟踪表",
        "",
        f"最近更新：{snapshot['asOf']}  ",
        "数据源：SEC EDGAR 官方 filings 与 XBRL companyfacts。",
        "",
        "## 最新指标",
        "",
        "| ticker | 组别 | 角色 | 收入 | 毛利率 | 营业利润率 | CapEx | FCF | 期末 | 最新披露 |",
        "|---|---|---|---:|---:|---:|---:|---:|---|---|",
    ]
    latest_by_ticker: dict[str, dict[str, Any]] = {}
    for filing in snapshot["filings"]:
        current = latest_by_ticker.get(filing["ticker"])
        if not current or filing["filingDate"] > current["filingDate"]:
            latest_by_ticker[filing["ticker"]] = filing

    for company in snapshot["companies"]:
        facts = company["facts"]
        derived = company["derived"]
        filing = latest_by_ticker.get(company["ticker"], {})
        filing_link = f"[{filing.get('form', 'SEC')}]({filing.get('filingUrl')})" if filing else "—"
        lines.append(
            "| {ticker} | {group} | {role} | {revenue} | {gm} | {om} | {capex} | {fcf} | {period} | {filing} |".format(
                ticker=company["ticker"],
                group=company["group"],
                role=company["role"],
                revenue=money(facts.get("revenue", {}).get("value") if facts.get("revenue") else None),
                gm=f"{derived['grossMarginPct']:.1f}%" if derived.get("grossMarginPct") is not None else "—",
                om=f"{derived['operatingMarginPct']:.1f}%" if derived.get("operatingMarginPct") is not None else "—",
                capex=money(facts.get("capex", {}).get("value") if facts.get("capex") else None),
                fcf=money(derived.get("freeCashFlow")),
                period=facts.get("revenue", {}).get("periodEnd") if facts.get("revenue") else "—",
                filing=filing_link,
            )
        )
    lines.extend(
        [
            "",
            "## 待人工补充",
            "",
            "- AI 相关收入口径：多数公司不会在 XBRL 中直接结构化披露，需要从 earnings release、10-Q MD&A 或法说会摘录。",
            "- 电话会全文：只收录公司官方披露或用户提供材料，不抓取不稳定的第三方免费网页。",
            "- R1/R2 判断：本表只更新事实，不自动改变假设置信度。",
            "",
        ]
    )
    return "\n".join(lines)


def build_dashboard(snapshot: dict[str, Any]) -> dict[str, Any]:
    companies = []
    for company in snapshot["companies"]:
        facts = company["facts"]
        revenue = facts.get("revenue")
        latest_filed = max(
            (fact.get("filed") for fact in facts.values() if fact and fact.get("filed")),
            default=None,
        )
        companies.append(
            {
                "ticker": company["ticker"],
                "name": company["name"],
                "group": company["group"],
                "hypothesis": company["hypothesis"],
                "role": company["role"],
                "periodEnd": revenue.get("periodEnd") if revenue else None,
                "latestFiled": latest_filed,
                "revenue": revenue,
                "grossMarginPct": company["derived"].get("grossMarginPct"),
                "operatingMarginPct": company["derived"].get("operatingMarginPct"),
                "capex": facts.get("capex"),
                "freeCashFlow": company["derived"].get("freeCashFlow"),
                "inventory": facts.get("inventory"),
                "cash": facts.get("cash"),
            }
        )

    new_filings = [filing for filing in snapshot["filings"] if filing.get("isNew")]
    return {
        "meta": {
            "title": "美股财报官方跟踪",
            "asOf": snapshot["asOf"],
            "generatedAt": snapshot["generatedAt"],
            "source": "SEC EDGAR",
            "policy": "Free official filings and XBRL facts only.",
            "newFilings": len(new_filings),
            "companies": len(companies),
        },
        "companies": companies,
        "newFilings": new_filings,
        "recentFilings": snapshot["filings"][:80],
        "sourceStatus": [
            {
                "id": "sec",
                "label": "SEC EDGAR",
                "status": "connected",
                "updatedAt": snapshot["generatedAt"],
                "note": f"已检查 {len(companies)} 家公司，新增 {len(new_filings)} 条披露。",
            },
            {
                "id": "transcripts",
                "label": "电话会全文",
                "status": "manual",
                "updatedAt": None,
                "note": "免费官方口径仅收录公司披露的 8-K/6-K 附件；其他电话会材料先人工入库。",
            },
        ],
    }


def company_index(snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {company["ticker"]: company for company in snapshot["companies"]}


def short_metric(company: dict[str, Any] | None, field: str = "revenue") -> str:
    if not company:
        return "—"
    if field == "revenue":
        value = company.get("facts", {}).get("revenue", {}).get("value") if company.get("facts", {}).get("revenue") else None
        return money(value)
    if field == "capex":
        value = company.get("facts", {}).get("capex", {}).get("value") if company.get("facts", {}).get("capex") else None
        return money(value)
    if field == "grossMargin":
        value = company.get("derived", {}).get("grossMarginPct")
        return f"{value:.1f}%" if isinstance(value, (int, float)) else "—"
    if field == "operatingMargin":
        value = company.get("derived", {}).get("operatingMarginPct")
        return f"{value:.1f}%" if isinstance(value, (int, float)) else "—"
    if field == "fcf":
        return money(company.get("derived", {}).get("freeCashFlow"))
    return "—"


def update_research_dashboards(snapshot: dict[str, Any]) -> None:
    companies = company_index(snapshot)
    new_count = sum(1 for filing in snapshot["filings"] if filing.get("isNew"))
    as_of = snapshot["asOf"]
    generated_at = snapshot["generatedAt"]

    if R1_DASHBOARD.exists():
        r1 = read_json(R1_DASHBOARD)
        r1["meta"]["asOf"] = as_of
        r1["meta"]["generatedAt"] = generated_at
        r1["meta"]["status"] = "SEC基线已接入"
        r1["meta"]["reviewPolicy"] = "SEC 自动更新总收入、利润率、CapEx、库存和现金流；AI 分部收入与订单仍需公司 IR、8-K 附件或人工材料交叉验证。"
        updates = {
            "NVIDIA 数据中心与 Broadcom AI 收入": (
                f"SEC总收入基线：NVDA {short_metric(companies.get('NVDA'))}，"
                f"AVGO {short_metric(companies.get('AVGO'))}；AI口径待IR拆分。"
            ),
            "台积电 HPC、先进节点与先进封装兑现": "TSM 6-K 披露已进入SEC监控；HPC/CoWoS仍需月营收、法说会或IR口径补充。",
            "HBM 供应商收入、ASP 与毛利": (
                f"MU SEC基线：收入 {short_metric(companies.get('MU'))}，毛利率 {short_metric(companies.get('MU'), 'grossMargin')}；HBM拆分待IR补充。"
            ),
            "订单、Backlog 与收入确认质量": (
                f"设备链基线：AMAT {short_metric(companies.get('AMAT'))}，"
                f"LRCX {short_metric(companies.get('LRCX'))}，KLAC {short_metric(companies.get('KLAC'))}。"
            ),
            "服务器、网络、液冷与电源盈利质量": "SEC入口已建立；服务器/液冷公司需后续加入watchlist或从03-raw人工补充。",
        }
        for metric in r1.get("metrics", []):
            if metric["indicator"] in updates:
                metric["current"] = updates[metric["indicator"]]
                metric["source"] = "SEC EDGAR + 公司IR补充"
        r1["evidence"] = merge_evidence(
            r1.get("evidence", []),
            {
                "date": as_of,
                "title": "SEC 官方财报基线接入 R1",
                "detail": f"已检查半导体与云/应用共 {len(snapshot['companies'])} 家公司，最近45天披露 {len(snapshot['filings'])} 条，新增 {new_count} 条。当前只作为事实基线，不直接提高置信度。",
                "source": "03-raw/sec/us-equity-earnings",
                "direction": "support",
            },
        )
        r1["intake"] = merge_intake(
            r1.get("intake", []),
            {
                "label": "SEC官方财报",
                "formats": "10-Q / 10-K / 8-K / 20-F / 6-K / XBRL JSON",
                "use": "自动更新总收入、利润率、CapEx、库存、现金流和新披露链接",
            },
        )
        write_json(R1_DASHBOARD, r1)

    if R2_DASHBOARD.exists():
        r2 = read_json(R2_DASHBOARD)
        r2["meta"]["asOf"] = as_of
        r2["meta"]["generatedAt"] = generated_at
        r2["meta"]["status"] = "SEC基线已接入"
        r2["meta"]["reviewPolicy"] = "SEC 自动更新软件和云公司的收入、利润率、现金流；最终采用者ROI、NRR、RPO和AI ARR需要IR披露或人工材料补充。"
        updates = {
            "可量化增收、降本与回收期": "SEC不直接披露采用者ROI；继续依赖客户案例、访谈和公司材料。",
            "AI 试点转规模化生产率": "SEC不直接披露试点转生产率；作为人工补充指标保留。",
            "AI 产品 NRR 与 RPO": (
                f"软件基线：CRM {short_metric(companies.get('CRM'))}，NOW {short_metric(companies.get('NOW'))}，"
                f"ADBE {short_metric(companies.get('ADBE'))}；NRR/RPO待10-Q文本和IR补充。"
            ),
            "基础设施与应用预算的释放节奏": (
                f"云厂商CapEx基线：MSFT {short_metric(companies.get('MSFT'), 'capex')}，"
                f"GOOGL {short_metric(companies.get('GOOGL'), 'capex')}，META {short_metric(companies.get('META'), 'capex')}。"
            ),
            "推理成本、AI 毛利率与经营现金流": (
                f"云/软件FCF基线：MSFT {short_metric(companies.get('MSFT'), 'fcf')}，"
                f"AMZN {short_metric(companies.get('AMZN'), 'fcf')}，PLTR {short_metric(companies.get('PLTR'), 'fcf')}。"
            ),
        }
        for metric in r2.get("metrics", []):
            if metric["indicator"] in updates:
                metric["current"] = updates[metric["indicator"]]
                metric["source"] = "SEC EDGAR + 公司IR/客户案例补充"
        r2["evidence"] = merge_evidence(
            r2.get("evidence", []),
            {
                "date": as_of,
                "title": "SEC 官方财报基线接入 R2",
                "detail": "已建立云与应用公司收入、利润率、现金流和新披露监控；ROI、NRR、RPO和AI ARR不由SEC自动推断，等待公司披露或人工材料。",
                "source": "03-raw/sec/us-equity-earnings",
                "direction": "support",
            },
        )
        r2["intake"] = merge_intake(
            r2.get("intake", []),
            {
                "label": "SEC官方财报",
                "formats": "10-Q / 10-K / 8-K / XBRL JSON",
                "use": "自动更新软件和云公司的收入、利润率、现金流、CapEx和披露链接",
            },
        )
        write_json(R2_DASHBOARD, r2)


def merge_evidence(existing: list[dict[str, Any]], item: dict[str, Any]) -> list[dict[str, Any]]:
    filtered = [row for row in existing if row.get("title") != item["title"]]
    return [item, *filtered][:8]


def merge_intake(existing: list[dict[str, Any]], item: dict[str, Any]) -> list[dict[str, Any]]:
    filtered = [row for row in existing if row.get("label") != item["label"]]
    return [*filtered, item]


def sync(args: argparse.Namespace) -> dict[str, Any]:
    config = read_json(CONFIG_PATH)
    groups = set(args.groups.split(",")) if args.groups else None
    watchlist = flatten_watchlist(config, groups=groups)
    include_forms = set(args.forms.split(",")) if args.forms else set(config.get("forms", DEFAULT_FORMS))
    ticker_map = load_ticker_cik_map(config)
    state = load_state()
    seen_accessions = set(state.get("seenAccessions", []))

    companies: list[dict[str, Any]] = []
    filings: list[dict[str, Any]] = []
    missing: list[str] = []

    for index, company in enumerate(watchlist, start=1):
        ticker = company["ticker"].upper()
        sec_info = ticker_map.get(ticker)
        if not sec_info:
            missing.append(ticker)
            continue
        cik = sec_info["cik"]
        company_facts = fetch_company_facts(config, company, cik)
        companies.append(company_facts)
        company_filings = recent_filings(config, company, cik, args.days, include_forms, args.details)
        for filing in company_filings:
            filing["isNew"] = filing["accessionNumber"] not in seen_accessions
        filings.extend(company_filings)
        time.sleep(args.sleep)

    filings.sort(key=lambda item: (item["filingDate"], item["ticker"], item["accessionNumber"]), reverse=True)
    companies.sort(key=lambda item: (item["group"], item["ticker"]))
    snapshot = {
        "asOf": date.today().isoformat(),
        "generatedAt": datetime.now(UTC).isoformat(timespec="seconds"),
        "config": str(CONFIG_PATH.relative_to(ROOT)),
        "missingTickers": missing,
        "companies": companies,
        "filings": filings,
    }

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    raw_base = RAW_DIR / f"{snapshot['asOf']}-sec-earnings-update"
    write_json(raw_base.with_suffix(".json"), snapshot)
    raw_base.with_suffix(".md").write_text(markdown_report(snapshot), encoding="utf-8", newline="\n")
    write_json(OUTPUT_DATA, build_dashboard(snapshot))
    OUTPUT_TRACKING.write_text(tracking_markdown(snapshot), encoding="utf-8", newline="\n")
    update_research_dashboards(snapshot)
    save_state(state, filings)
    return snapshot


def main() -> None:
    configure_stdio()
    parser = argparse.ArgumentParser(description="Sync free official SEC earnings data.")
    parser.add_argument("--days", type=int, default=45, help="Recent filing window.")
    parser.add_argument("--groups", help="Comma-separated group ids, e.g. semiconductor,cloud_application.")
    parser.add_argument("--forms", help="Comma-separated SEC forms.")
    parser.add_argument("--details", action="store_true", help="Fetch filing index details for 8-K/6-K earnings candidates.")
    parser.add_argument("--sleep", type=float, default=0.12, help="Delay between companies for SEC fair-access friendliness.")
    args = parser.parse_args()

    snapshot = sync(args)
    print(
        json.dumps(
            {
                "companies": len(snapshot["companies"]),
                "filings": len(snapshot["filings"]),
                "newFilings": sum(1 for filing in snapshot["filings"] if filing.get("isNew")),
                "raw": str((RAW_DIR / f"{snapshot['asOf']}-sec-earnings-update.md").relative_to(ROOT)),
                "tracking": str(OUTPUT_TRACKING.relative_to(ROOT)),
                "dashboardData": str(OUTPUT_DATA.relative_to(ROOT)),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
