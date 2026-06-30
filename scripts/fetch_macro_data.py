#!/usr/bin/env python3
"""
小苔花投研 — 宏观数据拉取器
改编自 Daily Watchlist (Benboerba620/daily-watchlist)

拉取 VIX 恐慌指数 + 美股三大指数 ETF (SPY/QQQ/IWM) + 大宗商品 + 比特币
需要 FMP_API_KEY。

用法:
    python fetch_macro_data.py
    python fetch_macro_data.py -o data/macro.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from io import StringIO
from pathlib import Path
from typing import Any

import requests
from dotenv import dotenv_values

FMP_BASE = "https://financialmodelingprep.com/api/v3"
VIX_ENDPOINT = "quote/%5EVIX"

MACRO_TICKERS = {
    "indices": ["SPY", "QQQ", "IWM"],
    "commodities": {"GLD": "Gold", "USO": "Oil ETF", "CLUSD": "WTI Crude", "BZUSD": "Brent Crude"},
    "crypto": ["BTCUSD"],
    "volatility": ["VIXY"],
}


def configure_stdio() -> None:
    for name in ("stdout", "stderr"):
        s = getattr(sys, name, None)
        if s and hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def find_project_root() -> Path:
    current = Path(__file__).resolve().parent
    for c in (current, *current.parents):
        if (c / "AGENTS.md").is_file() or (c / "config").is_dir():
            return c
    return current.parent


def load_env(project_root: Path) -> str:
    for p in [project_root / "config" / ".env", project_root / ".env"]:
        if p.is_file():
            raw = p.read_text(encoding="utf-8-sig")
            for k, v in dotenv_values(stream=StringIO(raw)).items():
                if v is not None and k not in os.environ:
                    os.environ[k] = v
            log(f"[env] loaded from {p}")
            break
    else:
        log("[env] no .env found, using system env only")
    return os.environ.get("FMP_API_KEY", "").strip()


def fmp_get(endpoint: str) -> Any:
    url = f"{FMP_BASE}/{endpoint}"
    key = os.environ.get("FMP_API_KEY", "")
    try:
        resp = requests.get(url, params={"apikey": key}, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        log(f"[warn] FMP {endpoint}: {e}")
        return None


def vix_status(v: float | None) -> str:
    if v is None:
        return "Unknown"
    if v < 15:
        return "Optimistic"
    if v < 20:
        return "Normal"
    if v < 30:
        return "Cautious"
    return "Panic"


def main():
    configure_stdio()
    parser = argparse.ArgumentParser(description="小苔花投研 — 宏观数据拉取")
    parser.add_argument("-o", "--output", help="输出 JSON 文件路径（默认 stdout）")
    args = parser.parse_args()

    root = find_project_root()
    log(f"[init] project root: {root}")
    api_key = load_env(root)

    if not api_key:
        log("[error] FMP_API_KEY not set")
        result = {"error": "FMP_API_KEY not set"}
    else:
        result: dict[str, Any] = {
            "macro": {},
            "sentiment": "Unknown",
            "meta": {"timestamp": datetime.now().isoformat(), "missing_symbols": []},
        }

        # VIX
        log("Fetching VIX...")
        vix_data = fmp_get(VIX_ENDPOINT)
        vix_quote = vix_data[0] if isinstance(vix_data, list) and vix_data else None
        vix_price = (
            float(vix_quote["price"]) if vix_quote and vix_quote.get("price") is not None else None
        )
        result["macro"]["VIX"] = {
            "price": vix_price,
            "change": float(vix_quote["change"]) if vix_quote and vix_quote.get("change") is not None else None,
            "change_pct": float(vix_quote["changesPercentage"]) if vix_quote and vix_quote.get("changesPercentage") is not None else None,
            "status": vix_status(vix_price),
        }

        # 批量拉取所有 macro tickers
        all_tickers = []
        for group in MACRO_TICKERS.values():
            if isinstance(group, list):
                all_tickers.extend(group)
            else:
                all_tickers.extend(group.keys())

        log(f"Fetching {len(all_tickers)} macro tickers...")
        quotes = fmp_get(f"quote/{','.join(all_tickers)}") or []
        quote_map = {q["symbol"]: q for q in quotes if isinstance(q, dict) and "symbol" in q}

        # 指数
        for t in MACRO_TICKERS["indices"]:
            q = quote_map.get(t, {})
            result["macro"][t] = {
                "price": q.get("price"), "change_pct": q.get("changesPercentage"), "change": q.get("change"),
            }
            if t not in quote_map:
                result["meta"]["missing_symbols"].append(t)

        # 大宗商品
        for t, label in MACRO_TICKERS["commodities"].items():
            q = quote_map.get(t, {})
            result["macro"][t] = {
                "label": label, "price": q.get("price"),
                "change_pct": q.get("changesPercentage"), "change": q.get("change"),
            }
            if t not in quote_map:
                result["meta"]["missing_symbols"].append(t)

        # Brent-WTI 价差
        wti = quote_map.get("CLUSD", {}).get("price")
        brent = quote_map.get("BZUSD", {}).get("price")
        if isinstance(wti, (int, float)) and isinstance(brent, (int, float)):
            result["macro"]["BW_spread"] = round(brent - wti, 2)

        # BTC
        btc = quote_map.get("BTCUSD", {})
        result["macro"]["BTC"] = {"price": btc.get("price"), "change_pct": btc.get("changesPercentage")}
        if "BTCUSD" not in quote_map:
            result["meta"]["missing_symbols"].append("BTCUSD")

        # VIXY
        vixy = quote_map.get("VIXY", {})
        result["macro"]["VIXY"] = {"price": vixy.get("price"), "change_pct": vixy.get("changesPercentage")}

        # 综合情绪
        spy_change = result["macro"]["SPY"].get("change_pct")
        sentiment = result["macro"]["VIX"]["status"]
        if isinstance(spy_change, (int, float)):
            if spy_change > 1:
                sentiment += ", risk-on"
            elif spy_change < -1:
                sentiment += ", risk-off"
        result["sentiment"] = sentiment

        received = len(quote_map) + (1 if vix_quote else 0)
        result["meta"]["requested_symbols"] = len(all_tickers) + 1
        result["meta"]["received_symbols"] = received

    json_str = json.dumps(result, ensure_ascii=False, indent=2, default=str)
    if args.output:
        Path(args.output).write_text(json_str, encoding="utf-8")
        log(f"[done] saved to {args.output}")
    else:
        sys.stdout.write(json_str)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
