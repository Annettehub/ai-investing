#!/usr/bin/env python3
"""
重新下载已有英文播客为双语版本（英文原文 + 中文翻译）
只处理已存在于 03-raw/podwise/ 中的文件
"""
import subprocess
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PODWISE_EXE = Path(r"C:\Users\Annette Zhang\WorkBuddy\Claw\ai-investing\tools\podwise.exe")
OUTPUT_DIR = Path(r"C:\Users\Annette Zhang\WorkBuddy\Claw\ai-investing\03-raw\podwise")

# 从文件名中提取 episode_id
episode_ids = []
for f in OUTPUT_DIR.glob("*.md"):
    m = re.search(r"_(\d+)\.md$", f.name)
    if m and f.name != "README.md":
        eid = m.group(1)
        url = f"https://podwise.ai/dashboard/episodes/{eid}"
        episode_ids.append((eid, url, f))

print(f"找到 {len(episode_ids)} 个已有文件需要检查\n")

import tempfile

success = 0
fail = 0
skipped = 0

for eid, url, filepath in episode_ids:
    print(f"[{eid}] {filepath.name[:60]}...")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # 先导出英文原文
        en_dir = tmp / "en"
        en_dir.mkdir()
        r1 = subprocess.run(
            [str(PODWISE_EXE), "export", "markdown", url, "--output", str(en_dir)],
            capture_output=True, text=True, timeout=120, encoding="utf-8", errors="replace"
        )

        # 再导出中文翻译
        zh_dir = tmp / "zh"
        zh_dir.mkdir()
        r2 = subprocess.run(
            [str(PODWISE_EXE), "export", "markdown", url, "--lang", "Chinese", "--output", str(zh_dir)],
            capture_output=True, text=True, timeout=120, encoding="utf-8", errors="replace"
        )

        en_files = list(en_dir.glob("*.md"))
        zh_files = list(zh_dir.glob("*.md"))

        if en_files and zh_files:
            en_content = en_files[0].read_text("utf-8")
            zh_content = zh_files[0].read_text("utf-8")

            # 检查是否中文播客（如果英文版和中文版内容一样，说明是中文播客）
            if en_content == zh_content:
                # 中文播客，只保留原文
                filepath.write_text(en_content, "utf-8")
                print(f"  -> 中文播客，保留原文 ({len(en_content)} chars)")
                skipped += 1
            else:
                # 英文播客，合并双语
                merged = en_content.rstrip() + "\n\n---\n\n# 中文翻译 (Chinese Translation)\n\n" + zh_content.rstrip() + "\n"
                filepath.write_text(merged, "utf-8")
                print(f"  -> 双语合并成功 ({len(merged)} chars, {merged.count(chr(10))} lines)")
                success += 1
        elif en_files:
            # 只有英文原文（中文翻译未完成）
            en_content = en_files[0].read_text("utf-8")
            # 检查是否已经是双语（之前手动合并的）
            if "中文翻译" in filepath.read_text("utf-8"):
                print(f"  -> 已是双语，跳过")
                skipped += 1
            else:
                filepath.write_text(en_content, "utf-8")
                print(f"  -> 仅英文原文（中文翻译未完成）")
                success += 1
        else:
            print(f"  -> ✗ 下载失败")
            fail += 1

print(f"\n{'='*50}")
print(f"完成! 双语更新: {success} | 中文保留: {skipped} | 失败: {fail}")
