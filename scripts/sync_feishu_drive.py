#!/usr/bin/env python3
"""
Sync Feishu drive folder files into 03-raw/feishu.

Supported inputs:
- Markdown files: downloaded directly.
- Feishu online docx documents: fetched through docx raw_content API.
"""
import hashlib
import json
import os
import sys
from pathlib import Path

import requests

FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID")
FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET")
FOLDER_TOKEN = os.environ.get("FEISHU_FOLDER_TOKEN")

RAW_DIR = Path("03-raw/feishu")
HASH_FILE = Path("03-raw/.synced_hashes.json")
SKIP_MARKER = "勿同步"
DOCX_PERMISSION_CODE = 99991672


class FeishuPermissionError(RuntimeError):
    pass


def get_token():
    missing = [
        name
        for name, value in (
            ("FEISHU_APP_ID", FEISHU_APP_ID),
            ("FEISHU_APP_SECRET", FEISHU_APP_SECRET),
            ("FEISHU_FOLDER_TOKEN", FOLDER_TOKEN),
        )
        if not value
    ]
    if missing:
        raise RuntimeError(f"Missing env vars: {', '.join(missing)}")

    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(
        url,
        json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET},
        timeout=30,
    )
    data = resp.json()
    if resp.status_code != 200 or data.get("code") != 0:
        raise RuntimeError(f"Auth failed: {data.get('msg') or resp.status_code}")
    return data["tenant_access_token"]


def list_files(token, folder_token=None, folder_path=""):
    folder_token = folder_token or FOLDER_TOKEN
    url = "https://open.feishu.cn/open-apis/drive/v1/files"
    headers = {"Authorization": f"Bearer {token}"}
    files = []
    page_token = None

    while True:
        params = {"folder_token": folder_token, "page_size": 200}
        if page_token:
            params["page_token"] = page_token

        resp = requests.get(url, headers=headers, params=params, timeout=30)
        data = resp.json()

        if data.get("code") != 0:
            msg = data.get("msg") or "unknown error"
            code = data.get("code")
            hint = ""
            if code == 1061002:
                hint = " Check FEISHU_FOLDER_TOKEN: it must be a drive folder token, not a wiki/doc page token."
            raise RuntimeError(f"List files failed: code={code}, msg={msg}.{hint}")

        for item in data.get("data", {}).get("files", []):
            item_type = item.get("type")
            item_name = item.get("name", "")
            item_token = item.get("token")

            if not item_token:
                print(f"  Skip item without token: {item_name}")
                continue

            if is_folder(item_type):
                next_path = join_display_path(folder_path, item_name)
                print(f"  Folder: {next_path}")
                files.extend(list_files(token, item_token, next_path))
                continue

            files.append(
                {
                    "token": item_token,
                    "name": item_name,
                    "type": item_type,
                    "folder_path": folder_path,
                }
            )

        if not data.get("data", {}).get("has_more"):
            break
        page_token = data.get("data", {}).get("next_page_token")

    return files


def is_folder(item_type):
    return item_type in ("folder", "1", 1)


def join_display_path(parent, name):
    return f"{parent}/{name}" if parent else name


def download_md(token, file_token):
    url = f"https://open.feishu.cn/open-apis/drive/v1/files/{file_token}/download"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers, timeout=60)
    if resp.status_code == 200:
        return resp.content
    print(f"  Markdown download failed: {resp.status_code} {resp.text[:200]}")
    return None


def fetch_docx_raw_content(token, doc_token):
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_token}/raw_content"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers, timeout=60)
    if resp.status_code != 200:
        if resp.status_code == 400 and (
            "docx:document" in resp.text or "docx:document:readonly" in resp.text
        ):
            raise FeishuPermissionError(
                "Feishu app is missing docx read permissions. "
                "Enable scopes `docx:document` and `docx:document:readonly` in Feishu Developer Console, "
                "publish the app version, then rerun this workflow."
            )
        print(f"  Docx raw_content HTTP failed: {resp.status_code} {resp.text[:200]}")
        return None

    data = resp.json()
    if data.get("code") != 0:
        if data.get("code") == DOCX_PERMISSION_CODE:
            raise FeishuPermissionError(
                "Feishu app is missing docx read permissions. "
                "Enable scopes `docx:document` and `docx:document:readonly` in Feishu Developer Console, "
                "publish the app version, then rerun this workflow."
            )
        print(f"  Docx raw_content API failed: code={data.get('code')}, msg={data.get('msg')}")
        return None

    content = data.get("data", {}).get("content")
    if content is None:
        print("  Docx raw_content returned no content")
        return None
    return content.encode("utf-8")


def load_hashes():
    if HASH_FILE.exists():
        with HASH_FILE.open("r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def save_hashes(hashes):
    HASH_FILE.parent.mkdir(parents=True, exist_ok=True)
    with HASH_FILE.open("w", encoding="utf-8") as f:
        json.dump(sorted(hashes), f, ensure_ascii=False)


def safe_path_part(name, max_len=120):
    invalid = '<>:"/\\|?*'
    safe = name.strip()
    for ch in invalid:
        safe = safe.replace(ch, "_")
    safe = safe.rstrip(". ")
    if not safe:
        safe = "untitled"
    return safe[:max_len]


def output_path(file_info):
    folder_parts = [
        safe_path_part(part)
        for part in file_info.get("folder_path", "").split("/")
        if part
    ]
    name = file_info["name"]

    if file_info["type"] == "docx":
        filename = safe_path_part(Path(name).stem) + ".md"
    else:
        filename = safe_path_part(name)

    return RAW_DIR.joinpath(*folder_parts, filename)


def content_hash(content):
    return hashlib.md5(content).hexdigest()[:16]


def write_if_changed(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_bytes() == content:
        return False
    path.write_bytes(content)
    return True


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    print("Getting token...")
    token = get_token()

    print("Listing files recursively...")
    files = list_files(token)
    print(f"Total files found: {len(files)}")

    candidates = [
        f
        for f in files
        if SKIP_MARKER not in f["name"]
        and (f["name"].endswith(".md") or f["type"] == "docx")
    ]
    print(f"Files to process: {len(candidates)}")
    print(f"  Markdown: {sum(1 for f in candidates if f['name'].endswith('.md'))}")
    print(f"  Feishu docx: {sum(1 for f in candidates if f['type'] == 'docx')}")

    synced_hashes = load_hashes()
    new_or_changed = 0
    skipped = 0
    failed = 0

    for file_info in candidates:
        try:
            display_path = join_display_path(file_info.get("folder_path", ""), file_info["name"])
            print(f"\nProcessing: {display_path} | type={file_info['type']}")

            if file_info["name"].endswith(".md"):
                content = download_md(token, file_info["token"])
            elif file_info["type"] == "docx":
                content = fetch_docx_raw_content(token, file_info["token"])
            else:
                skipped += 1
                continue

            if not content:
                failed += 1
                continue

            digest = content_hash(content)
            path = output_path(file_info)

            if digest in synced_hashes and path.exists():
                print("  Already synced")
                skipped += 1
                continue

            changed = write_if_changed(path, content)
            synced_hashes.add(digest)
            if changed:
                new_or_changed += 1
                print(f"  Saved: {path}")
            else:
                skipped += 1
                print("  Already exists; hash state updated")

        except FeishuPermissionError:
            raise
        except Exception as exc:
            failed += 1
            print(f"  Error: {exc}")

    save_hashes(synced_hashes)

    print(f"\n{'=' * 50}")
    print(f"Processed: {len(candidates)}, Saved: {new_or_changed}, Skipped: {skipped}, Failed: {failed}")
    print(f"{'=' * 50}")

    if failed:
        raise RuntimeError(f"Feishu sync finished with {failed} failed file(s)")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Sync failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
