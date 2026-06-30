#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""小苔花投研 — 环境检查脚本"""
from __future__ import annotations

import sys
import io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

OK = "[OK]"
FAIL = "[FAIL]"


def check(label: str, condition: bool, detail: str = "") -> bool:
    mark = OK if condition else FAIL
    print(f"  {mark}  {label}" + (f" - {detail}" if detail else ""))
    return condition


def main():
    print("=" * 50)
    print("  xiaotaihua invest - setup check")
    print("=" * 50)

    project_root = Path(__file__).resolve().parent.parent
    all_ok = True

    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    all_ok &= check(f"Python {py_ver}", sys.version_info >= (3, 10), "needs 3.10+")

    for pkg in ("requests",):
        try:
            __import__(pkg)
            all_ok &= check(f"pip: {pkg}", True)
        except ImportError:
            all_ok &= check(f"pip: {pkg}", False, "pip install requests")

    try:
        from dotenv import dotenv_values
        all_ok &= check("pip: python-dotenv", True)
    except ImportError:
        all_ok &= check("pip: python-dotenv", False, "pip install python-dotenv")

    # API Keys
    env_paths = [project_root / "config" / ".env", project_root / ".env"]
    env_path = None
    for p in env_paths:
        if p.is_file():
            env_path = p
            break

    if env_path:
        all_ok &= check(".env file", True, str(env_path))
        from dotenv import dotenv_values
        raw = env_path.read_text(encoding="utf-8-sig")
        env = dotenv_values(stream=raw)
        fmp = env.get("FMP_API_KEY", "").strip()
        ts = env.get("TUSHARE_TOKEN", "").strip()
        all_ok &= check("FMP_API_KEY", bool(fmp), "configured" if fmp else "not configured")
        all_ok &= check("TUSHARE_TOKEN", bool(ts), "configured" if ts else "not configured")
    else:
        all_ok &= check(".env file", False, "copy config/.env.example -> config/.env")

    for f in ["01-commands/today.md", "02-kb/snapshot.md", "AGENTS.md", "active-context.md"]:
        all_ok &= check(f, (project_root / f).is_file())

    for s in ["fetch_market_data.py", "fetch_macro_data.py"]:
        all_ok &= check(f"scripts/{s}", (project_root / "scripts" / s).is_file())

    print("\n" + "-" * 50)
    print("  data source test")
    print("-" * 50)

    if env_path:
        from dotenv import dotenv_values
        raw = env_path.read_text(encoding="utf-8-sig")
        env = dotenv_values(stream=raw)
        fmp_key = env.get("FMP_API_KEY", "").strip()
        if fmp_key:
            try:
                import requests
                resp = requests.get(
                    "https://financialmodelingprep.com/api/v3/quote/AAPL",
                    params={"apikey": fmp_key},
                    timeout=10,
                )
                ok = resp.status_code == 200 and isinstance(resp.json(), list)
                all_ok &= check("FMP connection", ok, "AAPL quote OK" if ok else f"HTTP {resp.status_code}")
            except Exception as e:
                all_ok &= check("FMP connection", False, str(e))

    print("\n" + "=" * 50)
    if all_ok:
        print("  [OK]  all checks passed")
    else:
        print("  [FAIL]  some checks failed, fix and retry")
    print("=" * 50)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
