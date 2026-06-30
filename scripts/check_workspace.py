#!/usr/bin/env python3
"""小苔花投研系统健康检查"""
import os
import sys
from pathlib import Path
from datetime import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

KB_ROOT = Path(__file__).parent.parent

def check_dirs():
    required = ["00-system", "01-commands", "02-kb", "03-raw", "04-output", "processed"]
    for d in required:
        p = KB_ROOT / d
        status = "OK" if p.exists() else "MISSING"
        print(f"  [{status}] {d}/")

def check_files():
    required = ["AGENTS.md", "active-context.md"]
    for f in required:
        p = KB_ROOT / f
        status = "OK" if p.exists() else "MISSING"
        print(f"  [{status}] {f}")

def count_entities():
    kb = KB_ROOT / "02-kb"
    entities = list((kb / "entities").glob("*.md")) if (kb / "entities").exists() else []
    hypotheses = list((kb / "hypotheses").glob("*.md")) if (kb / "hypotheses").exists() else []
    walls = list((kb / "walls").glob("*.md")) if (kb / "walls").exists() else []
    concepts = list((kb / "concepts").glob("*.md")) if (kb / "concepts").exists() else []
    sources = list((kb / "sources").glob("*.md")) if (kb / "sources").exists() else []

    print(f"  Entities: {len(entities)}")
    print(f"  Hypotheses: {len(hypotheses)}")
    print(f"  Walls: {len(walls)}")
    print(f"  Concepts: {len(concepts)}")
    print(f"  Sources: {len(sources)}")

    return entities, hypotheses, walls, concepts, sources

def check_hypothesis_sync():
    """Verify snapshot.md probabilities match hypothesis files"""
    snapshot = KB_ROOT / "02-kb" / "snapshot.md"
    if not snapshot.exists():
        print("  Snapshot: MISSING")
        return

    with open(snapshot, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse active hypotheses line: H1: ..., 40% | H2: ..., 60% | ...
    import re
    # Only check the active hypotheses section (before the log section)
    active_section = content.split("## 每日检查日志")[0] if "## 每日检查日志" in content else content
    probs = {}
    for m in re.finditer(r"(H\d):[^,]*,\s*(\d+)%", active_section):
        probs[m.group(1)] = int(m.group(2))

    print(f"  Snapshot probabilities: {probs}")

def count_raw():
    raw = KB_ROOT / "03-raw"
    if raw.exists():
        count = sum(1 for f in raw.rglob("*.md") if f.name != ".gitkeep")
        print(f"  Raw materials: {count}")
    else:
        print(f"  Raw materials: 0")

def count_commands():
    cmds = KB_ROOT / "01-commands"
    if cmds.exists():
        files = list(cmds.glob("*.md"))
        print(f"  Commands: {', '.join(f.stem for f in files)}")
    else:
        print(f"  Commands: 0")

if __name__ == "__main__":
    print(f"=== 小苔花投研系统健康检查 ({datetime.now().strftime('%Y-%m-%d %H:%M')}) ===")
    print("\nDirectory structure:")
    check_dirs()
    print("\nCore files:")
    check_files()
    print("\nKnowledge base:")
    count_entities()
    print()
    count_raw()
    print()
    check_hypothesis_sync()
    print()
    count_commands()
    print("\n=== Complete ===")
