#!/usr/bin/env python3
"""
微信读书笔记同步脚本
通过 Weread Agent API Gateway 拉取全部划线+想法，输出到 03-raw/weread/
"""
import os
import sys
import json
import requests
from datetime import datetime

API_BASE = "https://i.weread.qq.com/api/agent/gateway"
SKILL_VERSION = "1.0.3"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "03-raw", "weread")

def call_api(api_name: str, **params):
    """调用微信读书 Agent API Gateway"""
    api_key = os.environ.get("WEREAD_API_KEY", "")
    if not api_key:
        print("ERROR: WEREAD_API_KEY 未设置")
        sys.exit(1)

    body = {"api_name": api_name, "skill_version": SKILL_VERSION, **params}
    resp = requests.post(API_BASE,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json=body,
        timeout=30
    )
    data = resp.json()
    if data.get("errcode", 0) != 0:
        print(f"  API Error [{api_name}]: {data.get('errmsg', 'unknown')}")
        return None
    # Check for upgrade
    if "upgrade_info" in data:
        print(f"  ⚠️  Skill 版本更新: {data['upgrade_info'].get('message', '')}")
    return data


def get_all_notebooks():
    """获取所有有笔记的书籍"""
    all_books = []
    params = {"count": 50}
    while True:
        data = call_api("/user/notebooks", **params)
        if not data:
            break
        books = data.get("books", [])
        all_books.extend(books)
        if data.get("hasMore") != 1:
            break
        if books:
            params["lastSort"] = books[-1]["sort"]
    return all_books


def get_book_highlights(book_id: str):
    """获取单本书的划线"""
    data = call_api("/book/bookmarklist", bookId=book_id)
    if not data:
        return []
    return data.get("updated", [])


def get_book_reviews(book_id: str):
    """获取单本书的想法/点评（全量翻页）"""
    all_reviews = []
    params = {"bookid": book_id, "count": 50}
    while True:
        data = call_api("/review/list/mine", **params)
        if not data:
            break
        reviews = data.get("reviews", [])
        all_reviews.extend(reviews)
        if data.get("hasMore") != 1:
            break
        params["synckey"] = data.get("synckey", 0)
    return all_reviews


def format_timestamp(ts):
    """Unix timestamp → YYYY-MM-DD"""
    if not ts:
        return "未知"
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")


def save_book_notes(book: dict, highlights: list, reviews: list) -> str:
    """将一本书的笔记保存为 .md 文件"""
    book_info = book.get("book", {})
    title = book_info.get("title", "未知书名")
    author = book_info.get("author", "未知作者")
    book_id = book.get("bookId", "")

    safe_title = title.replace("/", "-").replace(":", "-")[:60]
    filename = f"微信读书-{safe_title}-{author}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    lines = []
    lines.append(f"# {title}")
    lines.append(f"")
    lines.append(f"- **作者：** {author}")
    lines.append(f"- **来源：** 微信读书 (bookId: {book_id})")
    lines.append(f"- **同步日期：** {datetime.now().strftime('%Y-%m-%d')}")
    lines.append(f"- **阅读进度：** {book.get('readingProgress', 0)}%")
    lines.append(f"- **读完状态：** {'已读完' if book.get('markedStatus') == 1 else '在读'}")
    lines.append(f"- **总笔记数：** 划线 {book.get('noteCount', 0)} + 想法 {book.get('reviewCount', 0)} + 书签 {book.get('bookmarkCount', 0)}")
    lines.append(f"- **微信读书链接：** [打开阅读](weread://reading?bId={book_id})")
    lines.append(f"")

    # 按章节分组
    chapters = {}
    for h in highlights:
        ch_uid = h.get("chapterUid", 0)
        if ch_uid not in chapters:
            chapters[ch_uid] = {"highlights": [], "reviews": []}
        chapters[ch_uid]["highlights"].append(h)

    # 关联想法到章节
    for r in reviews:
        review_data = r.get("review", {})
        ch_name = review_data.get("chapterName", "")
        # 尝试通过章节名匹配
        matched = False
        for ch_uid, ch_data in chapters.items():
            for h in ch_data["highlights"]:
                # 想法关联到对应章节（粗略匹配）
                if not ch_name or ch_name:
                    break
            if not matched:
                ch_data["reviews"].append(r)
                matched = True
                break
        if not matched:
            # 无章节关联的想法放最后
            if "misc" not in chapters:
                chapters["misc"] = {"highlights": [], "reviews": []}
            chapters["misc"]["reviews"].append(r)

    # 输出
    for ch_uid, ch_data in chapters.items():
        if ch_data["highlights"]:
            # 取第一条划线的章节名
            first_hl = ch_data["highlights"][0]
            ch_title = ""
            for h in highlights[:1]:
                pass
            lines.append(f"## 第{ch_uid}章")
            lines.append(f"")

            for hl in ch_data["highlights"]:
                lines.append(f"> {hl.get('markText', '').strip()}")
                lines.append(f"")
                lines.append(f"*划线时间：{format_timestamp(hl.get('createTime'))}*")
                lines.append(f"")
                lines.append(f"---")
                lines.append(f"")

        if ch_data["reviews"]:
            lines.append(f"### 想法与点评")
            lines.append(f"")
            for rv in ch_data["reviews"]:
                review_data = rv.get("review", {})
                content = review_data.get("content", "").strip()
                if content:
                    lines.append(f"💭 {content}")
                    if review_data.get("abstract"):
                        lines.append(f"  > *原文：{review_data['abstract']}*")
                    lines.append(f"  *{format_timestamp(review_data.get('createTime'))}*")
                    lines.append(f"")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return filename


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("📚 微信读书笔记同步")
    print(f"   版本: {SKILL_VERSION}")
    print()

    # 1. 获取笔记本列表
    print("📋 获取笔记本列表...")
    notebooks = get_all_notebooks()
    if not notebooks:
        print("   未找到有笔记的书籍（或 API Key 未生效）")
        return

    total_notes = sum(
        b.get("noteCount", 0) + b.get("reviewCount", 0)
        for b in notebooks
    )
    print(f"   找到 {len(notebooks)} 本有笔记的书，共 {total_notes} 条笔记")
    print()

    # 2. 逐本拉取内容
    synced = 0
    for i, book in enumerate(notebooks, 1):
        book_info = book.get("book", {})
        title = book_info.get("title", "未知")
        book_id = book.get("bookId", "")

        note_count = book.get("noteCount", 0)
        review_count = book.get("reviewCount", 0)

        if note_count == 0 and review_count == 0:
            continue

        print(f"  [{i}/{len(notebooks)}] {title} (划线{note_count}, 想法{review_count})...", end=" ")

        highlights = get_book_highlights(book_id) if note_count > 0 else []
        reviews = get_book_reviews(book_id) if review_count > 0 else []

        filename = save_book_notes(book, highlights, reviews)
        print(f"✅ {len(highlights)}条划线 + {len(reviews)}条想法 → {filename}")
        synced += 1

    print()
    print(f"✅ 同步完成：{synced} 本书 → {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
