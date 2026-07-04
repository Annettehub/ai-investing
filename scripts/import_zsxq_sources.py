"""
Import all 751 ZsxqCrawler topics + 139 AI-packaged articles into sources.
Two separate sections since they use different ID systems:
  - Section 1: 139 AI专栏 (from ai_package index.csv, with clean titles)
  - Section 2: 751 topics (from all_topics_complete.json, raw posts)
"""
import json
import csv
import os
import re
from datetime import datetime

BASE = "D:/Users/Annette Zhang/Documents/Project1/ZsxqCrawler/output"
KB_SOURCES = "C:/Users/Annette Zhang/WorkBuddy/Claw/ai-investing/02-kb/sources"
RAW_ZSXQ = "C:/Users/Annette Zhang/WorkBuddy/Claw/ai-investing/03-raw/zsxq"

# 1. Load AI package articles (139 专栏)
ai_articles = []
with open(f"{BASE}/ai_package_linked_articles_88888812815442/index.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = row.get("title", "").strip()
        article_dir = row.get("article_dir", "").strip()
        dir_name = os.path.basename(article_dir) if article_dir else ""
        # Extract the slug id
        match = re.search(r'id_([a-z0-9]+)_', dir_name)
        slug_id = match.group(1) if match else ""
        ai_articles.append({
            "title": title,
            "slug_id": slug_id,
            "dir_name": dir_name,
            "image_count": row.get("image_count", "0"),
            "article_md": f"{BASE}/ai_package_linked_articles_88888812815442/{article_dir}/article.md" if article_dir else "",
        })

print(f"Loaded {len(ai_articles)} AI articles")

# Check which are already in 03-raw/zsxq/
existing_raw = set()
if os.path.isdir(RAW_ZSXQ):
    for f in os.listdir(RAW_ZSXQ):
        if f.endswith(".md"):
            existing_raw.add(f)

# Check raw presence
for a in ai_articles:
    a["in_raw"] = any(a["slug_id"] in f for f in existing_raw) if a["slug_id"] else False

in_raw_count = sum(1 for a in ai_articles if a["in_raw"])
print(f"  Already in 03-raw/zsxq/: {in_raw_count}/{len(ai_articles)}")

# 2. Load all 751 topics
with open(f"{BASE}/all_topics_complete.json", "r", encoding="utf-8") as f:
    topics = json.load(f)

print(f"Loaded {len(topics)} topics from JSON")

# Build title set from AI articles for overlap detection
ai_titles = set(a["title"] for a in ai_articles if a["title"])

# 3. Load category mapping (nested: category/subcategory/article_folder)
category_map = {}
cat_base = f"{BASE}/articles_by_category"
if os.path.isdir(cat_base):
    for root, dirs, files in os.walk(cat_base):
        for d in dirs:
            match = re.search(r'id_([a-z0-9]+)_', d)
            if match:
                slug = match.group(1)
                rel = os.path.relpath(root, cat_base)
                parts = rel.split(os.sep)
                top_cat = parts[0] if parts and parts[0] != '.' else '未分类'
                sub_cat = parts[1] if len(parts) > 1 else ''
                category_map[slug] = f'{top_cat}/{sub_cat}' if sub_cat else top_cat

print(f"Loaded {len(category_map)} category mappings")

# 4. Build the comprehensive index
lines = []
lines.append("# 知识星球来源总索引")
lines.append("")
lines.append("> 星球「半导体大佬的会议室」(group_id=88888812815442) · 作者：吴梓豪")
lines.append(f"> 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
lines.append("")
qa_count = sum(1 for t in topics if t.get('type') == 'q&a')
talk_count = sum(1 for t in topics if t.get('type') == 'talk')
lines.append(f"> 总计 **{len(topics)} 篇 topics**（{qa_count} Q&A + {talk_count} talk）")
lines.append(f"> 其中 **{len(ai_articles)} 篇专栏** 经过 AI 深度整理（含结构化摘要+图片关联）")
lines.append("")
lines.append("---")
lines.append("")

# Section 1: AI 专栏
lines.append("## 一、AI 深度整理专栏（139篇）")
lines.append("")
lines.append("> 这些长文经过 AI 处理，包含结构化内容和图片关联。")
lines.append("> 原始文件位于 `03-raw/zsxq/`（已复制）和 ZsxqCrawler `ai_package` 目录。")
lines.append("")

# Category stats for AI articles
ai_cats = {}
for a in ai_articles:
    cat = category_map.get(a["slug_id"], "未分类")
    ai_cats[cat] = ai_cats.get(cat, 0) + 1

lines.append("### 分类统计")
lines.append("")
lines.append("| 分类 | 篇数 |")
lines.append("|------|------|")
for cat in sorted(ai_cats.keys(), key=lambda x: -ai_cats[x]):
    lines.append(f"| {cat} | {ai_cats[cat]} |")
lines.append("")
lines.append("### 完整列表")
lines.append("")
lines.append("| # | 标题 | 分类 | 图片 | 已入库 |")
lines.append("|---|------|------|------|--------|")

for i, a in enumerate(ai_articles, 1):
    title = a["title"].replace("|", "\\|")[:70]
    cat = category_map.get(a["slug_id"], "未分类")
    img = a["image_count"]
    in_raw = "✅" if a["in_raw"] else "❌"
    lines.append(f"| {i} | {title} | {cat} | {img} | {in_raw} |")

lines.append("")
lines.append("---")
lines.append("")

# Section 2: All 751 topics
lines.append(f"## 二、全量 topics（{len(topics)}篇）")
lines.append("")
lines.append("> 包含星球全部帖子。标有「专栏」的已在上方第一部分列出。")
lines.append("> 通过 topic_id 可在 `all_topics_complete.json` 中检索全文。")
lines.append("")

# Type stats
lines.append("### 类型统计")
lines.append("")
lines.append("| 类型 | 篇数 |")
lines.append("|------|------|")
lines.append(f"| Q&A 问答 | {qa_count} |")
lines.append(f"| talk 发言 | {talk_count} |")
lines.append("")
lines.append("### 完整列表")
lines.append("")
lines.append("| # | 类型 | 标题/摘要 | 日期 | 阅读 | 评论 | 专栏 |")
lines.append("|---|------|----------|------|------|------|------|")

for i, t in enumerate(topics, 1):
    title = t.get("title", "")
    if not title or len(title) < 5:
        # Try to use text content snippet
        title = "(无标题/短帖)"
    title = title.replace("|", "\\|").replace("\n", " ")[:60]

    ttype = t.get("type", "unknown")
    dt = t.get("create_time", "")
    if isinstance(dt, (int, float)):
        try:
            dt = datetime.fromtimestamp(dt).strftime("%Y-%m-%d")
        except:
            dt = str(dt)[:10]
    elif isinstance(dt, str):
        dt = dt[:10]

    reads = t.get("reading_count", 0) or 0
    comments = t.get("comments_count", 0) or 0

    # Check if this topic's title matches any AI article
    is_column = "✅" if title[:15] in " ".join(ai_titles) else ""

    lines.append(f"| {i} | {ttype} | {title} | {dt} | {reads} | {comments} | {is_column} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## 使用方式")
lines.append("")
lines.append("1. **AI 专栏**：已复制到 `03-raw/zsxq/`，可直接在知识库中引用")
lines.append("2. **全量 topics**：通过 topic_id 在 `all_topics_complete.json` 中检索全文")
lines.append("3. **入料命令**：说\"入库这篇\" + 标题关键词，AI 会从原始数据提取摘要写入 `SRC-ZSXQ-*.md`")
lines.append("4. **数据源路径**：`D:/Users/Annette Zhang/Documents/Project1/ZsxqCrawler/output/`")

# Write the index
index_path = os.path.join(KB_SOURCES, "_index-zsxq.md")
with open(index_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nWritten index to {index_path}")
print(f"  - AI articles (Section 1): {len(ai_articles)}")
print(f"  - All topics (Section 2): {len(topics)}")
print(f"  - Already in 03-raw: {in_raw_count}/{len(ai_articles)}")
