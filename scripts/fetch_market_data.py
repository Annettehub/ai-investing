#!/usr/bin/env python3
"""
Annette投研系统投研 — 行情数据拉取器 v2.0

数据源策略:
  主源: yfinance (免费, 全球市场, HK/US/CN 全覆盖)
  增强: FMP /stable/quote-short (免费版仅支持美股, 更快更可靠)

输出 JSON 到 stdout，日志到 stderr。

用法:
    python fetch_market_data.py --tickers 00981.HK,TSM,0700.HK
    python fetch_market_data.py --from-watchlist      # 从 config/watchlist.md 读取全部
    python fetch_market_data.py --core                # 只拉🔴核心标的
    python fetch_market_data.py                       # 默认拉全部 watchlist
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from typing import Any

import requests
from dotenv import dotenv_values

# ── Constants ──
FMP_STABLE_URL = "https://financialmodelingprep.com/stable"
DEFAULT_TIMEOUT = 15
CN_SUFFIXES = (".SH", ".SZ")
HK_SUFFIX = ".HK"
TS_SUFFIXES = CN_SUFFIXES + (HK_SUFFIX,)


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


# ── Env / Config ──
def find_project_root() -> Path:
    current = Path(__file__).resolve().parent
    for candidate in (current, *current.parents):
        if (candidate / "AGENTS.md").is_file():
            return candidate
        if (candidate / "config").is_dir():
            return candidate
    return current.parent


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
        for k, v in dotenv_values(stream=sys.modules.get("io", __import__("io")).StringIO(raw)).items():
            if v is not None and k not in os.environ:
                os.environ[k] = v
        log(f"[env] loaded from {env_path}")
    else:
        log("[env] no .env found, using system env only")

    return {
        "FMP_API_KEY": os.environ.get("FMP_API_KEY", "").strip(),
    }


# ── FMP (US stocks only, free plan) ──
def fetch_fmp_us(tickers: list[str], api_key: str) -> dict[str, dict[str, Any]]:
    """逐只拉 FMP quote-short（免费版不支持 batch）"""
    results: dict[str, dict[str, Any]] = {}
    if not api_key:
        return results

    def _one(sym: str) -> tuple[str, dict[str, Any] | None]:
        try:
            url = f"{FMP_STABLE_URL}/quote-short?symbol={sym}&apikey={api_key}"
            resp = requests.get(url, timeout=DEFAULT_TIMEOUT)
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list) and len(data) > 0:
                item = data[0]
                return sym, {
                    "price": parse_float(item.get("price")),
                    "change": parse_float(item.get("change")),
                    "volume": parse_float(item.get("volume")),
                    "source": "fmp",
                }
        except Exception:
            pass
        return sym, None

    with ThreadPoolExecutor(max_workers=min(5, len(tickers))) as ex:
        futures = {ex.submit(_one, t): t for t in tickers}
        for future in as_completed(futures):
            sym, data = future.result()
            if data:
                results[sym] = data

    return results


# ── Yahoo Finance ticker 格式转换 ──
# yfinance 的 HK 股去前导零 (00981.HK → 0981.HK)，A 股上交所用 .SS
def _to_yf_ticker(ticker: str) -> str:
    """将标准 ticker 转为 Yahoo Finance 格式"""
    if ticker.endswith(".HK"):
        code = ticker[:-3]
        # 去前导零: 00981 → 0981, 06181 → 6181, 09992 → 9992
        stripped = code.lstrip("0") or "0"
        return f"{stripped}.HK"
    if ticker.endswith(".SH"):
        return ticker[:-3] + ".SS"
    return ticker


# ── yfinance (global markets, free) ──
def _has_yfinance() -> bool:
    try:
        import yfinance  # noqa: F401
        return True
    except ImportError:
        return False


def fetch_yfinance_one(ticker: str) -> dict[str, Any] | None:
    """拉一只股票的 yfinance 数据"""
    import yfinance as yf

    # 避免沙盒拦截 AppData 缓存
    cache_dir = os.environ.get("YF_CACHE_DIR", "")
    if not cache_dir:
        cache_dir = str(Path(__file__).resolve().parent.parent / ".yfcache")
        os.environ["YF_CACHE_DIR"] = cache_dir

    yf_ticker = _to_yf_ticker(ticker)
    try:
        t = yf.Ticker(yf_ticker)
        hist = t.history(period="5d", auto_adjust=False)
        if hist is None or hist.empty:
            return None
        latest = hist.iloc[-1]
        close = float(latest["Close"])
        prev = float(hist.iloc[-2]["Close"]) if len(hist) >= 2 else None
        change = (close - prev) if prev is not None else None
        change_pct = (change / prev * 100) if change is not None and prev else None
        return {
            "price": close,
            "change": round(change, 4) if change is not None else None,
            "changesPercentage": round(change_pct, 2) if change_pct is not None else None,
            "previousClose": prev,
            "open": float(latest.get("Open", float("nan"))),
            "dayHigh": float(latest.get("High", float("nan"))),
            "dayLow": float(latest.get("Low", float("nan"))),
            "volume": int(latest.get("Volume", 0)),
            "tradeDate": str(latest.name.date()) if hasattr(latest, "name") else "",
            "source": "yfinance",
        }
    except Exception as e:
        log(f"[warn] yfinance failed for {ticker}: {e}")
        return None


def fetch_yfinance_batch(tickers: list[str]) -> dict[str, dict[str, Any]]:
    """并行拉多只 yfinance"""
    results: dict[str, dict[str, Any]] = {}
    if not tickers:
        return results

    with ThreadPoolExecutor(max_workers=min(8, len(tickers))) as ex:
        futures = {ex.submit(fetch_yfinance_one, t): t for t in tickers}
        for future in as_completed(futures):
            t = futures[future]
            try:
                r = future.result()
                if r:
                    results[t] = r
            except Exception:
                pass
    return results


# ── Watchlist parser ──
def parse_watchlist_md(path: Path, core_only: bool = False) -> list[dict[str, str]]:
    """解析 config/watchlist.md Markdown 表格"""
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

            if all(re.fullmatch(r":?-{3,}:?", c) for c in normalized):
                continue

            if headers is None:
                if required.issubset(set(normalized)):
                    headers = normalized
                continue

            if headers and len(cells) == len(headers):
                row = dict(zip(headers, cells))
                ticker_raw = row.get("ticker", "").strip()

                # 跳过多余行
                if ticker_raw.startswith("^") or ticker_raw.upper() in ("DXY", "BTC-USD"):
                    continue
                if not ticker_raw or ticker_raw in ("---", "(待添加)", "TBD") or ticker_raw.startswith("*"):
                    continue

                if core_only:
                    tier_val = (row.get("tier", "") or "").strip()
                    if "核心" not in tier_val and "🔴" not in tier_val:
                        continue

                entries.append({
                    "ticker": ticker_raw.upper(),
                    "name": row.get("name", "").strip(),
                    "market": row.get("market", "").strip(),
                })

    return entries


# ── Main ──
def main():
    configure_stdio()
    parser = argparse.ArgumentParser(description="Annette投研系统投研 — 行情拉取器 v2.0")
    parser.add_argument("--tickers", help="逗号分隔的股票代码")
    parser.add_argument("--watchlist", "--from-watchlist", action="store_true",
                        help="从 config/watchlist.md 读取全部股票池")
    parser.add_argument("--core", action="store_true",
                        help="只拉取🔴核心标的")
    parser.add_argument("--output", "-o", help="输出 JSON 文件路径（默认 stdout）")
    args = parser.parse_args()

    project_root = find_project_root()
    log(f"[init] project root: {project_root}")
    env = load_env(project_root)

    # 收集 tickers
    statements: list[dict[str, str]] = []

    if args.tickers:
        for t in re.split(r"[\s,]+", args.tickers):
            t = t.strip().upper()
            if t:
                if t.endswith(CN_SUFFIXES):
                    market = "CN"
                elif t.endswith(HK_SUFFIX):
                    market = "HK"
                else:
                    market = "US"
                statements.append({"ticker": t, "name": t, "market": market})

    if args.watchlist:
        wl_path = project_root / "config" / "watchlist.md"
        if wl_path.is_file():
            statements.extend(parse_watchlist_md(wl_path, core_only=args.core))
        else:
            log("[warn] no watchlist.md found")

    if args.core and not args.watchlist:
        wl_path = project_root / "config" / "watchlist.md"
        if wl_path.is_file():
            statements = parse_watchlist_md(wl_path, core_only=True)
            log("[core] filtering 🔴核心标的 only")

    if not statements:
        wl_path = project_root / "config" / "watchlist.md"
        if wl_path.is_file():
            statements = parse_watchlist_md(wl_path)
        else:
            log("[error] no tickers specified")
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

    # 数据拉取
    all_data: dict[str, dict[str, Any]] = {}

    # 第一优先级: yfinance (全球市场)
    if _has_yfinance():
        all_tickers = [s["ticker"] for s in statements]
        log("[yfinance] fetching all tickers...")
        yf_results = fetch_yfinance_batch(all_tickers)
        for sym, data in yf_results.items():
            all_data[sym] = data
        log(f"[yfinance] got {len(yf_results)}/{len(all_tickers)}")
    else:
        log("[warn] yfinance not installed — run: pip install yfinance")

    # 第二优先级: FMP 增强美股数据 (覆盖 yfinance 的 US 结果)
    api_key = env["FMP_API_KEY"]
    us_tickers = [s["ticker"] for s in statements if not s["ticker"].endswith(TS_SUFFIXES)]
    if us_tickers and api_key:
        log(f"[fmp] enhancing {len(us_tickers)} US tickers...")
        fmp_results = fetch_fmp_us(us_tickers, api_key)
        for sym, data in fmp_results.items():
            # FMP 覆盖 yfinance（保留 yfinance 的 changesPercentage 等字段）
            if sym in all_data:
                all_data[sym].update(data)
            else:
                all_data[sym] = data
        log(f"[fmp] enhanced {len(fmp_results)} US tickers")

    # 组装输出
    quotes: list[dict[str, Any]] = []
    for s in statements:
        sym = s["ticker"]
        if sym in all_data:
            d = all_data[sym]
            quotes.append({
                "ticker": sym,
                "name": s["name"],
                "market": s["market"],
                "price": d.get("price"),
                "change": d.get("change"),
                "changesPercentage": d.get("changesPercentage"),
                "previousClose": d.get("previousClose"),
                "open": d.get("open"),
                "dayHigh": d.get("dayHigh"),
                "dayLow": d.get("dayLow"),
                "volume": d.get("volume"),
                "tradeDate": d.get("tradeDate", ""),
                "source": d.get("source", "unknown"),
            })
        else:
            log(f"[warn] no data for {sym}")
            quotes.append({
                "ticker": sym, "name": s["name"], "market": s["market"],
                "error": "no_data",
            })

    # 异动检测 (≥5%)
    movers = []
    for q in quotes:
        pct = q.get("changesPercentage")
        if pct is not None and abs(pct) >= 5:
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
