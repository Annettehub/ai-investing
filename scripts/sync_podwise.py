#!/usr/bin/env python3
"""
Podwise 播客同步脚本 v1.2
通过 podwise CLI 拉取 Inbox 中 Ready(已AI处理)的播客内容，
导出为 Markdown（summary/chapters/qa/highlights/keywords/transcript）
- 中文播客：导出中文原文
- 英文播客：导出英文原文 + 中文翻译（合并为双语文件）
保存到 03-raw/podwise/
支持自动推送到 GitHub (Annettehub/podwise-readings)

用法:
  python sync_podwise.py              # 同步最近7天的已处理节目
  python sync_podwise.py --days 30    # 同步最近30天
  python sync_podwise.py --dry-run    # 预览模式，不实际下载
  python sync_podwise.py --push       # 同步后自动推送到 GitHub

依赖:
  - podwise CLI 已安装且已认证 (podwise auth)
  - VPN 已开启 (app.podwise.ai 需要外网访问)
  - git (用于 --push 推送到 GitHub)
"""

import os
import sys
import json
import subprocess
import re
from datetime import datetime, timedelta
from pathlib import Path

# Fix Windows console encoding for UTF-8 output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── 配置 ──────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = PROJECT_ROOT / "03-raw" / "podwise"
PODWISE_EXE = PROJECT_ROOT / "tools" / "podwise.exe"
STATE_FILE = OUTPUT_DIR / ".sync_state.json"
DEFAULT_DAYS = 7
GITHUB_REMOTE = "https://github.com/Annettehub/podwise-readings.git"
GITHUB_BRANCH = "main"
PODWISE_GIT_DIR = OUTPUT_DIR / ".git_sync"  # 内部 git 仓库目录

# ── 工具函数 ──────────────────────────────────────────


def run_podwise(args: list, timeout: int = 60) -> str:
    """运行 podwise CLI 命令，返回 stdout"""
    cmd = [str(PODWISE_EXE)] + args
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        print(f"  [WARN] CLI error (rc={result.returncode}): {result.stderr[:200]}")
        return ""
    return result.stdout


def load_state() -> dict:
    """加载已同步记录"""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text("utf-8"))
        except Exception:
            pass
    return {"synced": {}, "last_sync": None}


def save_state(state: dict):
    """保存同步状态"""
    state["last_sync"] = datetime.now().isoformat()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), "utf-8")


def parse_episodes(text: str) -> list[dict]:
    """解析 list episodes 输出，提取已处理的节目信息"""
    episodes = []
    current = {}

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue

        # 匹配数字序号开头的行（新节目标题）
        m = re.match(r"^(\d+)\.\s+(.+)", line)
        if m:
            if current.get("url") and current.get("title"):
                episodes.append(current)
            current = {"index": int(m.group(1)), "title": m.group(2).strip()}
            continue

        # 匹配 Podcast
        m2 = re.match(r"^\*?\*?Podcast:\*\*\s*(.+)", line)
        if m2:
            current["podcast"] = m2.group(1).strip()
            continue

        # 匹配 Published
        m3 = re.match(r"^\*?\*?Published:\*\*\s*(.+)", line)
        if m3:
            current["published"] = m3.group(1).strip()
            continue

        # 匹配 Processed
        if "Processed:" in line:
            current["processed"] = "Yes" in line or "yes" in line
            continue

        # 匹配 Episode URL
        m4 = re.search(r"https://podwise\.ai/dashboard/episodes/(\d+)", line)
        if m4:
            current["url"] = f"https://podwise.ai/dashboard/episodes/{m4.group(1)}"
            current["episode_id"] = m4.group(1)
            continue

        # 匹配 Language
        m5 = re.match(r"^\*?\*?Language:\*\*\s*(.+)", line)
        if m5:
            current["language"] = m5.group(1).strip()
            continue

        # 匹配 Read 状态
        if "Read:" in line:
            current["read"] = "Yes" in line or "yes" in line
            continue

        # 匹配 Duration
        m6 = re.match(r"^\*?\*?Duration:\*\*\s*(.+)", line)
        if m6:
            current["duration"] = m6.group(1).strip()
            continue

    # 最后一个
    if current.get("url") and current.get("title"):
        episodes.append(current)

    return episodes


def sanitize_filename(title: str, max_len: int = 80) -> str:
    """将标题转为安全的文件名"""
    name = title.replace("/", "-").replace("\\", "-").replace(":", "-")
    name = re.sub(r'[<>|"?*]', "", name)
    name = name.strip(". ")
    if len(name) > max_len:
        name = name[:max_len].rsplit(" ", 1)[0]
    return name


def setup_git_repo() -> bool:
    """初始化或更新内部 git 仓库用于推送"""
    git_dir = PODWISE_GIT_DIR
    if not (git_dir / ".git").exists():
        print(f"  📂 初始化 Git 仓库: {git_dir}")
        subprocess.run(["git", "init"], cwd=git_dir, capture_output=True)
        subprocess.run(
            ["git", "remote", "add", "origin", GITHUB_REMOTE],
            cwd=git_dir, capture_output=True,
        )
        # 创建初始分支
        subprocess.run(
            ["git", "checkout", "-b", GITHUB_BRANCH],
            cwd=git_dir, capture_output=True,
        )
    return True


def push_to_github(new_files: list[str]) -> bool:
    """将新文件推送到 GitHub podwise-readings 仓库"""
    if not new_files:
        return True

    print(f"\n🚀 Step 5: 推送到 GitHub ({len(new_files)} 个文件)...")

    git_dir = PODWISE_GIT_DIR

    # 确保 git 仓库就绪
    if not setup_git_repo():
        print("  [ERROR] Git 仓库初始化失败")
        return False

    # 复制新文件到 git 目录
    for fname in new_files:
        src = OUTPUT_DIR / fname
        dst = git_dir / fname
        if src.exists():
            import shutil
            shutil.copy2(src, dst)

    # Stage, commit, push
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = f"📻 Sync {len(new_files)} episode(s) | {date_str}"

    r1 = subprocess.run(["git", "add", "-A"], cwd=git_dir, capture_output=True, text=True)
    r2 = subprocess.run(["git", "commit", "-m", msg], cwd=git_dir, capture_output=True, text=True)

    if "nothing to commit" in r2.stderr or r2.returncode == 0:
        r3 = subprocess.run(
            ["git", "push", "-u", "origin", GITHUB_BRANCH],
            cwd=git_dir, capture_output=True, text=True, timeout=120,
        )
        if r3.returncode == 0:
            print(f"  ✓ 推送成功! → {GITHUB_REMOTE.replace('.git','')}")
            return True
        else:
            print(f"  [WARN] 推送失败: {r3.stderr[:200]}")
            return False
    else:
        print(f"  [WARN] commit 失败: {r2.stderr[:200]}")
        return False


# ── 主流程 ────────────────────────────────────────────


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Podwise 播客内容同步")
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS, help=f"拉取最近N天的节目 (默认{DEFAULT_DAYS})")
    parser.add_argument("--dry-run", action="store_true", help="预览模式，不实际下载")
    parser.add_argument("--force", action="store_true", help="强制重新下载已有的")
    parser.add_argument("--push", action="store_true", help="同步后自动推送到 GitHub")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"Podwise 播客同步 | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}")

    # 检查环境
    if not PODWISE_EXE.exists():
        print(f"[ERROR] podwise CLI 未找到: {PODWISE_EXE}")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PODWISE_GIT_DIR.mkdir(parents=True, exist_ok=True)
    state = load_state()

    # Step 1: 列出 Inbox 中最近的节目
    print(f"\n📥 Step 1: 拉取最近 {args.days} 天的节目列表...")
    output = run_podwise(["list", "episodes", "--latest", str(args.days)])
    if not output:
        print("[ERROR] 无法获取节目列表，请检查 VPN 连接和 podwise 认证")
        sys.exit(1)

    episodes = parse_episodes(output)
    total = len(episodes)
    ready = [e for e in episodes if e.get("processed")]
    not_ready = [e for e in episodes if not e.get("processed")]

    print(f"  总计 {total} 期 | ✅ Ready(已处理): {len(ready)} | ⏳ 未处理: {len(not_ready)}")

    if not_ready:
        print(f"  ⏳ 未处理节目 ({len(not_ready)}期):")
        for e in not_ready[:5]:
            print(f"     - [{e.get('published','?')}] {e['title'][:60]}...")
        if len(not_ready) > 5:
            print(f"     ... 还有 {len(not_ready)-5} 期未处理")
        print(f"  提示: 未处理节目需在 Podwise 网页端点击 Process 后才能下载")

    # Step 2: 过滤需要下载的 Ready 节目
    to_download = []
    skipped = 0
    for ep in ready:
        eid = ep["episode_id"]
        if eid in state["synced"] and not args.force:
            skipped += 1
            continue
        to_download.append(ep)

    print(f"\n📦 Step 2: 待下载: {len(to_download)} 期 (跳过已存在: {skipped})")
    if args.dry_run:
        print("\n[DRY RUN] 将要下载:")
        for ep in to_download:
            print(f"  ✓ [{ep.get('published','?')}] {ep.get('podcast','')} | {ep['title'][:60]}")
        print(f"\n共 {len(to_download)} 期。去掉 --dry-run 执行实际下载。")
        return

    # Step 3: 逐个下载
    success_count = 0
    fail_count = 0

    for i, ep in enumerate(to_download, 1):
        eid = ep["episode_id"]
        title = ep["title"]
        podcast = ep.get("podcast", "Unknown")
        published = ep.get("published", "?")
        fname = sanitize_filename(title) + f"_{eid}.md"
        outpath = OUTPUT_DIR / fname

        print(f"\n[{i}/{len(to_download)}] {title[:50]}...")
        print(f"       来源: {podcast} | 发布: {published}")
        print(f"       输出: {fname}")

        # 导出逻辑：
        # - 中文播客：直接导出原文（不加 --lang）
        # - 英文播客：导出两次（原文 + 中文翻译），合并为双语文件
        lang = ep.get("language", "")
        is_chinese = lang and "Chinese" in lang

        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)

            if is_chinese:
                # 中文播客：只导出原文
                cmd = ["export", "markdown", ep["url"], "--output", str(tmp)]
                run_podwise(cmd, timeout=120)
                # 找到生成的文件并复制到输出目录
                md_files = list(tmp.glob("*.md"))
                if md_files:
                    md_files[0].rename(outpath)
            else:
                # 英文播客：导出英文原文 + 中文翻译，合并
                # 1. 导出英文原文
                cmd_en = ["export", "markdown", ep["url"], "--output", str(tmp / "en")]
                (tmp / "en").mkdir()
                run_podwise(cmd_en, timeout=120)
                en_files = list((tmp / "en").glob("*.md"))

                # 2. 导出中文翻译
                cmd_zh = ["export", "markdown", ep["url"], "--lang", "Chinese", "--output", str(tmp / "zh")]
                (tmp / "zh").mkdir()
                run_podwise(cmd_zh, timeout=120)
                zh_files = list((tmp / "zh").glob("*.md"))

                if en_files and zh_files:
                    en_content = en_files[0].read_text("utf-8")
                    zh_content = zh_files[0].read_text("utf-8")

                    # 合并：英文原文在上，中文翻译在下
                    merged = en_content.rstrip() + "\n\n---\n\n# 中文翻译 (Chinese Translation)\n\n" + zh_content.rstrip() + "\n"
                    outpath.write_text(merged, "utf-8")
                elif en_files:
                    # 只有英文原文（中文翻译可能未完成）
                    en_files[0].rename(outpath)
                    print(f"       [WARN] 中文翻译未完成，仅导出英文原文")

        if outpath.exists():
            size = outpath.stat().st_size
            print(f"       ✓ 成功 ({size//1024}KB)" + (" [双语]" if not is_chinese else " [中文原文]"))
            state["synced"][eid] = {
                "title": title,
                "podcast": podcast,
                "published": published,
                "file": fname,
                "synced_at": datetime.now().isoformat(),
            }
            success_count += 1
        else:
            print(f"       ✗ 失败 (文件未生成)")
            fail_count += 1

    # Step 4: 保存状态和摘要
    save_state(state)

    # 收集新增文件列表
    new_files = []
    for eid, info in sorted(state["synced"].items(), key=lambda x: x[1].get("synced_at",""), reverse=True)[:success_count]:
        new_files.append(info["file"])

    # 打印汇总
    print(f"\n{'='*60}")
    print(f"✅ 同步完成!")
    print(f"   新增: {success_count} 期 | 失败: {fail_count} 期 | 跳过已有: {skipped} 期")
    print(f"   目录: {OUTPUT_DIR}")
    print(f"   状态文件: {STATE_FILE.name}")
    print(f"{'='*60}\n")

    # 输出新文件列表供后续入库参考
    if success_count > 0:
        print("新增文件列表:")
        for f in new_files:
            print(f"  - {f}")

    # Step 5: 推送到 GitHub (如果指定 --push)
    if args.push and new_files:
        push_to_github(new_files)
    elif args.push:
        print("\n🚀 没有新文件需要推送")


if __name__ == "__main__":
    main()
