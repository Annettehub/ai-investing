#!/usr/bin/env python3
"""
小苔花投研 — 行情数据拉取器
改编自 Daily Watchlist (Benboerba620/daily-watchlist)

多源兜底链: FMP → Tushare(A股/港股) → Stooq → Finnhub → EOD → yfinance
输出 JSON 到 stdout，日志到 stderr。

用法:
    python fetch_market_data.py --tickers 00981.HK,TSM,0700.HK
    python fetch_market_data.py --watchlist          # 从 config/watchlist.md 读取
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta
from io import StringIO
from pathlib import Path
from typing import Any

import requests
from dotenv import dotenv_values

# ── Constants ──
FMP_BASE_URL = "https://financialmodelingprep.com/api/v3"
DEFAULT_TIMEOUT = 20
CN_SUFFIXES = (".SH", ".SZ")
HK_SUFFIX = ".HK"
TS_SUFFIXES = CN_SUFFIXES + (HK_SUFFIX,)
STOOQ_MARKET_SUFFIX = {"US": "us", "JP": "jp", "DE": "de", "UK": "uk"}
EOD_MARKET_SUFFIX = {"HK": "HK", "KR": "KO", "FI": "HE"}


# ── Helpers ──
def configure_stdio() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream and hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def parse_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace("%", "").replace(",", "")
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def request_json(url: str) -> Any:
    resp = requests.get(url, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.json()


# ── Env / Config ──
def find_project_root() -> Path:
    """向上查找包含 AGENTS.md 或 config/ 的目录作为项目根"""
    current = Path(__file__).resolve().parent
    for candidate in (current, *current.parents):
        if (candidate / "AGENTS.md").is_file():
            return candidate
        if (candidate / "config").is_dir():
            return candidate
    return current.parent  # fallback


def load_env(project_root: Path) -> dict[str, str]:
    candidates = [
        project_root / "config" / ".env",
        project_root / ".env",
    ]
    env_path = None
    for p in candidates:
        if p.is_file():
            env_path = p
            break

    if env_path:
        raw = env_path.read_text(encoding="utf-8-sig")
        for k, v in dotenv_values(stream=StringIO(raw)).items():
            if v is not None and k not in os.environ:
                os.environ[k] = v
        log(f"[env] loaded from {env_path}")
    else:
        log("[env] no .env found, using system env only")

    return {
        "FMP_API_KEY": os.environ.get("FMP_API_KEY", "").strip(),
        "TUSHARE_TOKEN": os.environ.get("TUSHARE_TOKEN", "").strip(),
        "FINNHUB_API_KEY": os.environ.get("FINNHUB_API_KEY", "").strip(),
        "EOD_API_KEY": os.environ.get("EOD_API_KEY", "").strip(),
        "ENABLE_YFINANCE": os.environ.get("ENABLE_YFINANCE", "").strip(),
    }


# ── FMP ──
def fetch_fmp_quote_batch(tickers: list[str], api_key: str) -> list[dict[str, Any]]:
    joined = ",".join(tickers)
    url = f"{FMP_BASE_URL}/quote/{joined}?apikey={api_key}"
    payload = request_json(url)
    return payload if isinstance(payload, list) else []


def fetch_fmp_quotes(tickers: list[str], api_key: str, max_workers: int = 4) -> list[dict[str, Any]]:
    if not tickers or not api_key:
        return []
    quotes: list[dict[str, Any]] = []
    batches = [tickers[i : i + 50] for i in range(0, len(tickers), 50)]
    with ThreadPoolExecutor(max_workers=min(max_workers, len(batches))) as ex:
        futures = {ex.submit(fetch_fmp_quote_batch, b, api_key): b for b in batches}
        for future in as_completed(futures):
            try:
                quotes.extend(future.result())
            except Exception as e:
                log(f"[warn] FMP batch failed: {e}")
    return quotes


# ── Tushare (A 股 / 港股) ──
def load_tushare(token: str) -> Any | None:
    if not token:
        return None
    try:
        import tushare as ts
    except ImportError:
        log("[warn] tushare not installed, skipping CN/HK quotes")
        return None
    try:
        return ts.pro_api(token)
    except Exception as e:
        log(f"[warn] tushare init failed: {e}")
        return None


def fetch_tushare_quote(client: Any, ticker: str) -> dict[str, Any] | None:
    end = date.today()
    start = end - timedelta(days=10)
    try:
        if ticker.endswith(CN_SUFFIXES):
            df = client.daily(ts_code=ticker, start_date=start.strftime("%Y%m%d"), end_date=end.strftime("%Y%m%d"))
        elif ticker.endswith(HK_SUFFIX):
            df = client.hk_daily(ts_code=ticker, start_date=start.strftime("%Y%m%d"), end_date=end.strftime("%Y%m%d"))
        else:
            return None
    except Exception as e:
        log(f"[warn] tushare request failed for {ticker}: {e}")
        return None

    if df is None or df.empty:
        return None

    latest = df.sort_values("trade_date", ascending=False).iloc[0]
    return {
        "symbol": ticker,
        "price": parse_float(latest.get("close")),
        "change": parse_float(latest.get("change")),
        "changesPercentage": parse_float(latest.get("pct_chg")),
        "previousClose": parse_float(latest.get("pre_close")),
        "open": parse_float(latest.get("open")),
        "dayHigh": parse_float(latest.get("high")),
        "dayLow": parse_float(latest.get("low")),
        "volume": parse_float(latest.get("vol")),
        "tradeDate": str(latest.get("trade_date", "")),
        "source": "tushare",
    }


def fetch_tushare_quotes(tickers: list[str], token: str, max_workers: int = 4) -> list[dict[str, Any]]:
    if not tickers or not token:
        return []
    client = load_tushare(token)
    if not client:
        return []
    quotes: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=min(max_workers, len(tickers))) as ex:
        futures = {ex.submit(fetch_tushare_quote, client, t): t for t in tickers}
        for future in as_completed(futures):
            try:
                r = future.result()
                if r:
                    quotes.append(r)
            except Exception as e:
                log(f"[warn] tushare thread failed: {e}")
    return quotes


# ── Fallback chain ──
def fetch_stooq(ticker: str, market: str) -> dict[str, Any] | None:
    suffix = STOOQ_MARKET_SUFFIX.get(market.strip().upper())
    if not suffix:
        return None
    symbol = ticker.split(".")[0].lower()
    url = f"https://stooq.com/q/l/?s={symbol}.{suffix}&f=sd2t2ohlcvp&h&e=csv"
    try:
        resp = requests.get(url, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
        lines = resp.text.strip().splitlines()
        if len(lines) < 2:
            return None
        headers = [h.strip().lower() for h in lines[0].split(",")]
        values = [v.strip() for v in lines[1].split(",")]
        if len(headers) != len(values):
            return None
        row = dict(zip(headers, values))
        if row.get("close", "").upper() in ("", "N/D"):
            return None
        close = parse_float(row.get("close"))
        prev = parse_float(row.get("prev"))
        change = (close - prev) if close is not None and prev is not None else None
        change_pct = (change / prev * 100) if change is not None and prev else None
        return {
            "symbol": ticker, "price": close, "change": change,
            "changesPercentage": change_pct, "previousClose": prev,
            "open": parse_float(row.get("open")), "dayHigh": parse_float(row.get("high")),
            "dayLow": parse_float(row.get("low")), "volume": parse_float(row.get("volume")),
            "tradeDate": row.get("date", ""), "source": "stooq",
        }
    except Exception as e:
        log(f"[warn] stooq fallback failed for {ticker}: {e}")
        return None


def fetch_yfinance(ticker: str) -> dict[str, Any] | None:
    try:
        import yfinance as yf
    except ImportError:
        return None
    try:
        hist = yf.Ticker(ticker).history(period="5d", auto_adjust=False)
        if hist is None or hist.empty:
            return None
        latest = hist.iloc[-1]
        prev_close = float(hist.iloc[-2]["Close"]) if len(hist) >= 2 else None
        close = float(latest["Close"])
        change = (close - prev_close) if prev_close is not None else None
        change_pct = (change / prev_close * 100) if change is not None and prev_close else None
        return {
            "symbol": ticker, "price": close, "change": change,
            "changesPercentage": change_pct, "previousClose": prev_close,
            "open": float(latest["Open"]), "dayHigh": float(latest["High"]),
            "dayLow": float(latest["Low"]), "volume": float(latest["Volume"]),
            "tradeDate": str(latest.name.date()), "source": "yfinance",
        }
    except Exception as e:
        log(f"[warn] yfinance fallback failed for {ticker}: {e}")
        return None


def fetch_fallback(ticker: str, market: str, env: dict[str, str]) -> dict[str, Any] | None:
    """逐个尝试兜底源，返回第一个成功的结果"""
    market_upper = market.strip().upper()

    q = fetch_stooq(ticker, market)
    if q:
        return q

    finnhub_key = env.get("FINNHUB_API_KEY", "")
    if finnhub_key and market_upper == "US":
        try:
            p = request_json(f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={finnhub_key}")
            if isinstance(p, dict) and p.get("c") not in (0, 0.0, None):
                q = {
                    "symbol": ticker, "price": parse_float(p.get("c")),
                    "change": parse_float(p.get("d")), "changesPercentage": parse_float(p.get("dp")),
                    "previousClose": parse_float(p.get("pc")), "open": parse_float(p.get("o")),
                    "dayHigh": parse_float(p.get("h")), "dayLow": parse_float(p.get("l")),
                    "volume": None, "tradeDate": str(p.get("t", "")), "source": "finnhub",
                }
                return q
        except Exception:
            pass

    eod_key = env.get("EOD_API_KEY", "")
    if eod_key and market_upper in EOD_MARKET_SUFFIX:
        suffix = EOD_MARKET_SUFFIX[market_upper]
        try:
            p = request_json(f"https://eodhd.com/api/real-time/{ticker.split('.')[0]}.{suffix}?api_token={eod_key}&fmt=json")
            if isinstance(p, dict) and str(p.get("code", "")).upper() != "NA":
                q = {
                    "symbol": ticker, "price": parse_float(p.get("close")),
                    "change": parse_float(p.get("change")), "changesPercentage": parse_float(p.get("change_p")),
                    "previousClose": parse_float(p.get("previousClose")), "open": parse_float(p.get("open")),
                    "dayHigh": parse_float(p.get("high")), "dayLow": parse_float(p.get("low")),
                    "volume": parse_float(p.get("volume")), "tradeDate": str(p.get("timestamp", "")),
                    "source": "eod",
                }
                return q
        except Exception:
            pass

    if env.get("ENABLE_YFINANCE", "").lower() in ("1", "true", "yes", "on"):
        q = fetch_yfinance(ticker)
        if q:
            return q

    return None


# ── Watchlist parser (Markdown table) ──
def parse_watchlist_md(path: Path) -> list[dict[str, str]]:
    """解析 config/watchlist.md 中的 Markdown 表格"""
    if not path.is_file():
        raise FileNotFoundError(f"Watchlist not found: {path}")

    entries: list[dict[str, str]] = []
    headers: list[str] | None = None
    required = {"ticker", "name", "market"}

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|") or not line.endswith("|"):
                headers = None
                continue

            cells = [c.strip() for c in line.strip("|").split("|")]
            normalized = [c.strip().lower() for c in cells]

            # 跳过表头分隔行
            if all(re.fullmatch(r":?-{3,}:?", c) for c in normalized):
                continue

            if headers is None:
                if required.issubset(set(normalized)):
                    headers = normalized
                continue

            if headers and len(cells) == len(headers):
                row = dict(zip(headers, cells))
                entries.append({
                    "ticker": row["ticker"].strip().upper(),
                    "name": row.get("name", "").strip(),
                    "market": row.get("market", "").strip(),
                })

    return entries


# ── Main ──
def main():
    configure_stdio()
    parser = argparse.ArgumentParser(description="小苔花投研 — 行情拉取器")
    parser.add_argument("--tickers", help="逗号分隔的股票代码，如 00981.HK,TSM,0700.HK")
    parser.add_argument("--watchlist", action="store_true", help="从 config/watchlist.md 读取股票池")
    parser.add_argument("--output", "-o", help="输出 JSON 文件路径（默认 stdout）")
    args = parser.parse_args()

    project_root = find_project_root()
    log(f"[init] project root: {project_root}")
    env = load_env(project_root)

    api_key = env["FMP_API_KEY"]
    tushare_token = env["TUSHARE_TOKEN"]

    # 收集 tickers
    statements: list[dict[str, str]] = []

    if args.tickers:
        for t in re.split(r"[\s,]+", args.tickers):
            t = t.strip().upper()
            if t:
                # 猜测市场
                if t.endswith(CN_SUFFIXES):
                    market = "CN"
                elif t.endswith(HK_SUFFIX):
                    market = "HK"
                else:
                    market = "US"
                statements.append({"ticker": t, "name": t, "market": market})

    if args.watchlist:
        wl_paths = [
            project_root / "config" / "watchlist.md",
            project_root / "config" / "daily-watchlist-watchlist.md",
        ]
        for wp in wl_paths:
            if wp.is_file():
                statements.extend(parse_watchlist_md(wp))
                break
        else:
            log("[warn] no watchlist.md found")

    if not statements:
        # 没有指定 tickers，尝试默认从 watchlist.md 读取
        default_wl = project_root / "config" / "watchlist.md"
        if default_wl.is_file():
            statements = parse_watchlist_md(default_wl)
        else:
            log("[error] no tickers specified (use --tickers or --watchlist)")
            json.dump({"error": "no tickers"}, sys.stdout)
            return 1

    # 去重
    seen: set[str] = set()
    unique: list[dict[str, str]] = []
    for s in statements:
        if s["ticker"] not in seen:
            seen.add(s["ticker"])
            unique.append(s)
    statements = unique

    log(f"[fetch] {len(statements)} tickers: {', '.join(s['ticker'] for s in statements)}")

    # 分拆 FMP / Tushare
    fmp_items = [s for s in statements if not s["ticker"].endswith(TS_SUFFIXES)]
    ts_items = [s for s in statements if s["ticker"].endswith(TS_SUFFIXES)]

    quotes: list[dict[str, Any]] = []
    fetched: set[str] = set()

    # FMP
    if fmp_items:
        fmp_tickers = [s["ticker"] for s in fmp_items]
        for raw in fetch_fmp_quotes(fmp_tickers, api_key):
            sym = str(raw.get("symbol", "")).strip().upper()
            fetched.add(sym)
            quotes.append({
                "ticker": sym, "name": raw.get("name", ""), "market": "US",
                "price": parse_float(raw.get("price")),
                "change": parse_float(raw.get("change")),
                "changesPercentage": parse_float(raw.get("changesPercentage")),
                "previousClose": parse_float(raw.get("previousClose")),
                "open": parse_float(raw.get("open")),
                "dayHigh": parse_float(raw.get("dayHigh")),
                "dayLow": parse_float(raw.get("dayLow")),
                "volume": parse_float(raw.get("volume")),
                "tradeDate": raw.get("timestamp", ""),
                "source": "fmp",
            })

    # Tushare
    if ts_items:
        for raw in fetch_tushare_quotes([s["ticker"] for s in ts_items], tushare_token):
            sym = str(raw.get("symbol", "")).strip().upper()
            fetched.add(sym)
            quotes.append({
                "ticker": sym, "name": sym, "market": "HK" if sym.endswith(HK_SUFFIX) else "CN",
                "price": raw.get("price"),
                "change": raw.get("change"),
                "changesPercentage": raw.get("changesPercentage"),
                "previousClose": raw.get("previousClose"),
                "open": raw.get("open"), "dayHigh": raw.get("dayHigh"),
                "dayLow": raw.get("dayLow"), "volume": raw.get("volume"),
                "tradeDate": raw.get("tradeDate"),
                "source": "tushare",
            })

    # 兜底
    missing = [s for s in statements if s["ticker"] not in fetched]
    if missing:
        available_sources = "stooq"
        if env.get("FINNHUB_API_KEY"):
            available_sources += " > finnhub"
        if env.get("EOD_API_KEY"):
            available_sources += " > eod"
        if env.get("ENABLE_YFINANCE", "").lower() in ("1", "true", "yes", "on"):
            available_sources += " > yfinance"
        log(f"[fallback] {len(missing)} missing tickers → trying {available_sources}")
        for s in missing:
            r = fetch_fallback(s["ticker"], s["market"], env)
            if r:
                quotes.append({
                    "ticker": s["ticker"], "name": s["name"], "market": s["market"],
                    "price": r.get("price"), "change": r.get("change"),
                    "changesPercentage": r.get("changesPercentage"),
                    "previousClose": r.get("previousClose"),
                    "open": r.get("open"), "dayHigh": r.get("dayHigh"),
                    "dayLow": r.get("dayLow"), "volume": r.get("volume"),
                    "tradeDate": r.get("tradeDate"), "source": r.get("source"),
                })
            else:
                log(f"[warn] no data for {s['ticker']} (all sources failed)")
                quotes.append({
                    "ticker": s["ticker"], "name": s["name"], "market": s["market"],
                    "error": "no_data",
                })

    # 异动检测
    movers = []
    for q in quotes:
        pct = q.get("changesPercentage")
        if pct is not None and abs(pct) >= 3:
            movers.append({"ticker": q["ticker"], "name": q.get("name", ""), "change_pct": round(pct, 2)})
    movers.sort(key=lambda m: abs(m["change_pct"]), reverse=True)

    result = {"quotes": quotes, "movers": movers, "fetched_at": date.today().isoformat()}
    json_str = json.dumps(result, ensure_ascii=False, indent=2, default=str)

    if args.output:
        Path(args.output).write_text(json_str, encoding="utf-8")
        log(f"[done] saved to {args.output}")
    else:
        sys.stdout.write(json_str)
        sys.stdout.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
