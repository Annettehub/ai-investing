#!/usr/bin/env python3
"""Sync WeRead notes into 03-raw/weread without deleting existing files."""

from __future__ import annotations

import os
import re
import sys
from datetime import datetime
from pathlib import Path

import requests

API_BASE = "https://i.weread.qq.com/api/agent/gateway"
SKILL_VERSION = "1.0.3"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "03-raw" / "weread"


def call_api(api_name: str, **params):
    api_key = os.environ.get("WEREAD_API_KEY", "")
    if not api_key:
        print("ERROR: WEREAD_API_KEY is not set")
        sys.exit(1)

    body = {"api_name": api_name, "skill_version": SKILL_VERSION, **params}
    resp = requests.post(
        API_BASE,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=body,
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if data.get("errcode", 0) != 0:
        print(f"  API Error [{api_name}]: {data.get('errmsg', 'unknown')}")
        return None
    if "upgrade_info" in data:
        print(f"  Skill update notice: {data['upgrade_info'].get('message', '')}")
    return data


def get_all_notebooks() -> list[dict]:
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


def get_book_highlights(book_id: str) -> list[dict]:
    data = call_api("/book/bookmarklist", bookId=book_id)
    if not data:
        return []
    return data.get("updated", [])


def get_book_reviews(book_id: str) -> list[dict]:
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


def format_timestamp(ts) -> str:
    if not ts:
        return "未知"
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")


def safe_filename_part(value: str, max_length: int = 60) -> str:
    value = re.sub(r'[<>:"/\\|?*\r\n\t]+', "-", value).strip(" .-")
    return (value or "unknown")[:max_length]


def find_existing_file(book_id: str, fallback_filename: str) -> Path:
    fallback = OUTPUT_DIR / fallback_filename
    if fallback.exists():
        return fallback

    marker = f"bookId: {book_id}"
    for path in OUTPUT_DIR.glob("*.md"):
        try:
            if marker in path.read_text(encoding="utf-8", errors="ignore"):
                return path
        except OSError:
            continue
    return fallback


def render_book_notes(book: dict, highlights: list[dict], reviews: list[dict]) -> str:
    book_info = book.get("book", {})
    title = book_info.get("title", "未知书名")
    author = book_info.get("author", "未知作者")
    book_id = book.get("bookId", "")

    lines = [
        f"# {title}",
        "",
        f"- **作者：** {author}",
        f"- **来源：** 微信读书 (bookId: {book_id})",
        f"- **阅读进度：** {book.get('readingProgress', 0)}%",
        f"- **读完状态：** {'已读完' if book.get('markedStatus') == 1 else '在读'}",
        f"- **总笔记数：** 划线 {book.get('noteCount', 0)} + 想法 {book.get('reviewCount', 0)} + 书签 {book.get('bookmarkCount', 0)}",
        f"- **微信读书链接：** [打开阅读](weread://reading?bId={book_id})",
        "",
    ]

    chapters: dict[object, dict[str, list[dict]]] = {}
    for highlight in highlights:
        chapter_uid = highlight.get("chapterUid", 0)
        chapters.setdefault(chapter_uid, {"highlights": [], "reviews": []})
        chapters[chapter_uid]["highlights"].append(highlight)

    for review in reviews:
        review_data = review.get("review", {})
        chapter_uid = review_data.get("chapterUid") or review_data.get("chapterIdx") or "misc"
        chapters.setdefault(chapter_uid, {"highlights": [], "reviews": []})
        chapters[chapter_uid]["reviews"].append(review)

    for chapter_uid, chapter_data in chapters.items():
        if chapter_data["highlights"]:
            lines.extend([f"## 第 {chapter_uid} 章", ""])
            for highlight in chapter_data["highlights"]:
                mark_text = highlight.get("markText", "").strip()
                if not mark_text:
                    continue
                lines.extend(
                    [
                        f"> {mark_text}",
                        "",
                        f"*划线时间：{format_timestamp(highlight.get('createTime'))}*",
                        "",
                        "---",
                        "",
                    ]
                )

        if chapter_data["reviews"]:
            lines.extend(["### 想法与点评", ""])
            for review in chapter_data["reviews"]:
                review_data = review.get("review", {})
                content = review_data.get("content", "").strip()
                if not content:
                    continue
                lines.append(f"💭 {content}")
                if review_data.get("abstract"):
                    lines.append(f"  > *原文：{review_data['abstract']}*")
                lines.extend([f"  *{format_timestamp(review_data.get('createTime'))}*", ""])

    return "\n".join(lines).rstrip() + "\n"


def save_if_changed(book: dict, highlights: list[dict], reviews: list[dict]) -> str:
    book_info = book.get("book", {})
    title = book_info.get("title", "未知书名")
    author = book_info.get("author", "未知作者")
    book_id = book.get("bookId", "")
    filename = f"微信读书-{safe_filename_part(title)}-{safe_filename_part(author, 40)}.md"
    filepath = find_existing_file(book_id, filename)
    content = render_book_notes(book, highlights, reviews)

    if not filepath.exists():
        filepath.write_text(content, encoding="utf-8")
        return "new"

    old_content = filepath.read_text(encoding="utf-8", errors="ignore")
    if old_content == content:
        return "unchanged"

    filepath.write_text(content, encoding="utf-8")
    return "updated"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("WeRead notes sync")
    notebooks = get_all_notebooks()
    if not notebooks:
        print("No notebooks found, or the API key is not valid.")
        return

    total_notes = sum(b.get("noteCount", 0) + b.get("reviewCount", 0) for b in notebooks)
    print(f"Found {len(notebooks)} books with {total_notes} notes.")

    counts = {"new": 0, "updated": 0, "unchanged": 0}
    for index, book in enumerate(notebooks, 1):
        book_info = book.get("book", {})
        title = book_info.get("title", "未知")
        book_id = book.get("bookId", "")
        note_count = book.get("noteCount", 0)
        review_count = book.get("reviewCount", 0)

        if note_count == 0 and review_count == 0:
            continue

        print(f"[{index}/{len(notebooks)}] {title}...", end=" ")
        highlights = get_book_highlights(book_id) if note_count > 0 else []
        reviews = get_book_reviews(book_id) if review_count > 0 else []
        status = save_if_changed(book, highlights, reviews)
        counts[status] += 1
        print(status)

    print(
        "Done: "
        f"new={counts['new']}, updated={counts['updated']}, unchanged={counts['unchanged']}"
    )


if __name__ == "__main__":
    main()
