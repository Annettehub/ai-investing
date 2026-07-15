#!/usr/bin/env python3
"""Refresh the G2 storage dashboard (legacy H1.2) with official public data.

Official feeds are observation signals only. This script never changes the
hypothesis certainty or any qualitative trigger status.
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
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "trackers" / "H1.2-storage.json"
DASHBOARD_PATH = ROOT / "04-output" / "data" / "H1.2-storage-dashboard.json"
TRENDFORCE_PATH = ROOT / "04-output" / "data" / "H1.2-trendforce.json"
TWSE_URL = "https://openapi.twse.com.tw/v1/opendata/t187ap05_L"
SEC_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
OPENDART_LIST_URL = "https://opendart.fss.or.kr/api/list.json"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        file.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def load_local_env() -> None:
    env_path = ROOT / "config" / ".env"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def fetch_json(url: str, headers: dict[str, str] | None = None) -> Any:
    request = Request(url, headers=headers or {"User-Agent": "AnnetteKnowledgeHub/0.1"})
    ssl_context = ssl.create_default_context()
    if hasattr(ssl, "VERIFY_X509_STRICT"):
        ssl_context.verify_flags &= ~ssl.VERIFY_X509_STRICT
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urlopen(request, timeout=35, context=ssl_context) as response:
                return json.loads(response.read().decode("utf-8-sig"))
        except (URLError, TimeoutError) as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(attempt + 1)
    assert last_error is not None
    raise last_error


def status_entry(source_id: str, label: str, status: str, note: str) -> dict[str, Any]:
    return {
        "id": source_id,
        "label": label,
        "status": status,
        "updatedAt": datetime.now(UTC).isoformat(timespec="seconds") if status == "connected" else None,
        "note": note,
    }


def select_latest_fact(company_facts: dict[str, Any], candidates: list[str], instant: bool = False) -> dict[str, Any] | None:
    us_gaap = company_facts.get("facts", {}).get("us-gaap", {})
    facts: list[dict[str, Any]] = []
    selected_tag = ""
    label = ""
    for tag in candidates:
        concept = us_gaap.get(tag)
        if not concept:
            continue
        units = concept.get("units", {})
        for unit_name in ("USD", "USD/shares", "shares", "pure"):
            if unit_name in units:
                facts = units[unit_name]
                break
        if facts:
            selected_tag = tag
            label = concept.get("label", tag)
            break
    if not facts:
        return None

    valid = [
        fact
        for fact in facts
        if fact.get("form") in {"10-Q", "10-K", "20-F", "40-F"}
        and fact.get("filed")
        and fact.get("end")
        and fact.get("val") is not None
    ]
    if not valid:
        return None

    def score(fact: dict[str, Any]) -> tuple[str, int, str]:
        duration = 9999
        if not instant and fact.get("start"):
            try:
                duration = (date.fromisoformat(fact["end"]) - date.fromisoformat(fact["start"])).days
            except ValueError:
                pass
        quarterly_preference = 0 if instant or 70 <= duration <= 120 else 1
        return (fact["filed"], -quarterly_preference, fact["end"])

    latest = max(valid, key=score)
    return {
        "tag": selected_tag,
        "label": label,
        "value": latest["val"],
        "unit": "USD",
        "periodEnd": latest["end"],
        "filed": latest["filed"],
        "form": latest.get("form"),
        "frame": latest.get("frame"),
    }


def fetch_sec(config: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    user_agent = os.getenv("SEC_USER_AGENT") or "AnnetteKnowledgeHub/0.1 github.com/Annettehub/ai-investing"
    headers = {"User-Agent": user_agent}
    companies = []

    for company in config["sources"]["sec"]["companies"]:
        ticker = company["ticker"].upper()
        cik = company["cik"]
        facts = fetch_json(SEC_FACTS_URL.format(cik=cik), headers=headers)
        companies.append(
            {
                **company,
                "cik": cik,
                "entityName": facts.get("entityName", company["name"]),
                "revenue": select_latest_fact(
                    facts,
                    [
                        "RevenueFromContractWithCustomerExcludingAssessedTax",
                        "Revenues",
                        "SalesRevenueNet",
                    ],
                ),
                "capex": select_latest_fact(
                    facts,
                    [
                        "PaymentsToAcquirePropertyPlantAndEquipment",
                        "PaymentsForAdditionsToPropertyPlantAndEquipment",
                    ],
                ),
                "inventory": select_latest_fact(facts, ["InventoryNet", "InventoryNetOfAllowancesCustomerAdvancesAndProgressBillings"], instant=True),
            }
        )

    latest_filed = max(
        (
            metric["filed"]
            for company in companies
            for metric in (company.get("revenue"), company.get("capex"), company.get("inventory"))
            if metric
        ),
        default="unknown",
    )
    return {"companies": companies}, status_entry("sec", "SEC EDGAR", "connected", f"已读取{len(companies)}家公司，最新申报{latest_filed}")


def fetch_twse(config: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    rows = fetch_json(TWSE_URL)
    code_key = "公司代號"
    companies = []
    wanted = {company["code"]: company for company in config["sources"]["twse"]["companies"]}
    for row in rows:
        code = str(row.get(code_key, "")).strip()
        if code not in wanted:
            continue
        companies.append(
            {
                **wanted[code],
                "dataMonth": twse_month_to_iso(row.get("資料年月")),
                "monthlyRevenueTwdThousand": number_or_none(row.get("營業收入-當月營收")),
                "monthlyYoYPct": number_or_none(row.get("營業收入-去年同月增減(%)")),
                "ytdRevenueTwdThousand": number_or_none(row.get("累計營業收入-當月累計營收")),
                "ytdYoYPct": number_or_none(row.get("累計營業收入-前期比較增減(%)")),
            }
        )
    latest_month = max((company.get("dataMonth") or "" for company in companies), default="unknown")
    return {"companies": companies}, status_entry("twse", "TWSE OpenAPI", "connected", f"已读取{len(companies)}家公司，资料年月{latest_month}")


def number_or_none(value: Any) -> float | None:
    if value in (None, "", "--"):
        return None
    try:
        return float(str(value).replace(",", ""))
    except ValueError:
        return None


def twse_month_to_iso(value: Any) -> str | None:
    raw = str(value or "").strip()
    if not re.fullmatch(r"\d{5,6}", raw):
        return raw or None
    roc_year, month = int(raw[:-2]), int(raw[-2:])
    return f"{roc_year + 1911:04d}-{month:02d}"


def fetch_opendart(config: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    api_key = os.getenv("OPENDART_API_KEY", "").strip()
    if not api_key:
        return {"companies": []}, status_entry("opendart", "OpenDART", "unconfigured", "需要OPENDART_API_KEY")

    end_date = date.today()
    start_date = end_date - timedelta(days=180)
    companies = []
    for company in config["sources"]["opendart"]["companies"]:
        params = urlencode(
            {
                "crtfc_key": api_key,
                "corp_code": company["corpCode"],
                "bgn_de": start_date.strftime("%Y%m%d"),
                "end_de": end_date.strftime("%Y%m%d"),
                "page_count": 20,
            }
        )
        data = fetch_json(f"{OPENDART_LIST_URL}?{params}")
        if data.get("status") not in {"000", "013"}:
            raise RuntimeError(f"OpenDART {company['name']}: {data.get('message', data.get('status'))}")
        filings = [
            {
                "reportName": row.get("report_nm"),
                "receiptDate": row.get("rcept_dt"),
                "receiptNumber": row.get("rcept_no"),
            }
            for row in data.get("list", [])[:5]
        ]
        companies.append({**company, "recentFilings": filings})
    return {"companies": companies}, status_entry("opendart", "OpenDART", "connected", f"已读取{len(companies)}家公司近期披露")


def merge_trendforce() -> tuple[dict[str, Any], dict[str, Any]]:
    if not TRENDFORCE_PATH.exists():
        return {"metrics": []}, status_entry("trendforce", "TrendForce Excel", "unconfigured", "等待Excel导入")
    data = read_json(TRENDFORCE_PATH)
    metrics = data.get("metrics", [])
    note = f"已导入{len(metrics)}项，数据日期{data.get('asOf', 'unknown')}"
    return data, status_entry("trendforce", "TrendForce Excel", "connected", note)


def apply_trendforce_observations(dashboard: dict[str, Any], feed: dict[str, Any]) -> None:
    metric_map = {item.get("metricId"): item for item in feed.get("metrics", [])}
    trigger_map = {item.get("id"): item for item in dashboard.get("triggers", [])}
    mappings = {
        "server_ddr5_contract_qoq": "server-ddr5-price",
        "enterprise_ssd_contract_qoq": "enterprise-ssd-orders",
        "consumer_ssd_contract_qoq": "consumer-inventory",
    }
    for metric_id, trigger_id in mappings.items():
        metric = metric_map.get(metric_id)
        trigger = trigger_map.get(trigger_id)
        if not metric or not trigger:
            continue
        unit = metric.get("unit", "")
        trigger["current"] = f"{metric.get('period') or metric.get('asOf')}：{metric.get('value'):g}{unit}"
        trigger["updatedAt"] = metric.get("asOf") or trigger.get("updatedAt")
        trigger["source"] = "TrendForce Excel导入"


def refresh(offline: bool = False) -> dict[str, Any]:
    load_local_env()
    config = read_json(CONFIG_PATH)
    dashboard = read_json(DASHBOARD_PATH)
    existing_status = {item["id"]: item for item in dashboard.get("sourceStatus", [])}
    feeds = dashboard.setdefault("officialFeeds", {})

    collectors = [] if offline else [
        ("sec", "SEC EDGAR", fetch_sec),
        ("twse", "TWSE OpenAPI", fetch_twse),
        ("opendart", "OpenDART", fetch_opendart),
    ]
    for source_id, label, collector in collectors:
        try:
            feed, status = collector(config)
            feeds[source_id] = feed
            existing_status[source_id] = status
        except (HTTPError, URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
            if isinstance(exc, HTTPError) and exc.code == 403:
                note = "当前网络被官方接口限制，采集器已保留"
            else:
                note = str(exc)
            existing_feed = feeds.get(source_id, {})
            has_cached_data = any(isinstance(value, list) and value for value in existing_feed.values())
            if has_cached_data:
                cached_note = f"本次刷新失败，沿用上次数据；{note}"
                existing_status[source_id] = status_entry(source_id, label, "stale", cached_note)
            else:
                existing_status[source_id] = status_entry(source_id, label, "error", note)

    trendforce_feed, trendforce_status = merge_trendforce()
    feeds["trendforce"] = trendforce_feed
    existing_status["trendforce"] = trendforce_status
    apply_trendforce_observations(dashboard, trendforce_feed)
    dashboard["sourceStatus"] = [existing_status[key] for key in ("sec", "twse", "opendart", "trendforce")]
    dashboard["meta"]["generatedAt"] = datetime.now(UTC).isoformat(timespec="seconds")
    write_json(DASHBOARD_PATH, dashboard)
    return dashboard


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh G2 storage dashboard data")
    parser.add_argument("--offline", action="store_true", help="Only merge local imports")
    args = parser.parse_args()
    dashboard = refresh(offline=args.offline)
    print(f"Updated {DASHBOARD_PATH.relative_to(ROOT)}")
    for status in dashboard["sourceStatus"]:
        print(f"- {status['label']}: {status['status']} ({status['note']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
