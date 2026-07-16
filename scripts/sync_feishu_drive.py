#!/usr/bin/env python3
"""
飞书云盘文件夹 → GitHub 03-raw/ 同步
支持 .md 直接下载 + .docx 导出为 markdown
"""
import os
import json
import hashlib
import sys
import time
import requests

FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID")
FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET")
FOLDER_TOKEN = os.environ.get("FEISHU_FOLDER_TOKEN")

RAW_DIR = "03-raw/feishu"
HASH_FILE = "03-raw/.synced_hashes.json"


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
    resp = requests.post(url, json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET}, timeout=30)
    data = resp.json()
    if resp.status_code != 200 or data.get("code") != 0:
        raise RuntimeError(f"Auth failed: {data.get('msg') or resp.status_code}")
    return data["tenant_access_token"]


def list_files(token):
    url = "https://open.feishu.cn/open-apis/drive/v1/files"
    headers = {"Authorization": f"Bearer {token}"}
    files = []
    page_token = None

    while True:
        params = {"folder_token": FOLDER_TOKEN, "page_size": 200}
        if page_token:
            params["page_token"] = page_token

        resp = requests.get(url, headers=headers, params=params)
        data = resp.json()

        if data.get("code") != 0:
            raise RuntimeError(f"List files failed: code={data.get('code')}, msg={data.get('msg')}")

        for item in data.get("data", {}).get("files", []):
            if item.get("type") != "folder":
                files.append({
                    "token": item["token"],
                    "name": item.get("name", ""),
                    "type": item.get("type"),
                })

        if not data.get("data", {}).get("has_more"):
            break
        page_token = data["data"]["next_page_token"]

    return files


def download_md(token, file_token):
    """直接下载 .md 文件"""
    url = f"https://open.feishu.cn/open-apis/drive/v1/files/{file_token}/download"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers, timeout=60)
    if resp.status_code == 200:
        return resp.content
    print(f"  Download failed: {resp.status_code} {resp.text[:200]}")
    return None


def export_docx_to_md(token, doc_token):
    """将 docx 导出为 markdown，返回导出后的 file_token"""
    export_url = "https://open.feishu.cn/open-apis/drive/v1/export_tasks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    body = {
        "file_extension": "md",
        "token": doc_token,
        "type": "docx",
    }
    resp = requests.post(export_url, headers=headers, json=body, timeout=30)
    data = resp.json()
    if data.get("code") != 0:
        print(f"  Export task creation failed: {data.get('msg')}")
        return None

    ticket = data["data"]["ticket"]

    # 轮询等待导出完成（最多 60 秒）
    status_url = f"https://open.feishu.cn/open-apis/drive/v1/export_tasks/{ticket}"
    for _ in range(30):
        time.sleep(2)
        resp = requests.get(status_url, headers={"Authorization": f"Bearer {token}"}, timeout=30)
        result = resp.json()
        if result.get("code") != 0:
            print(f"  Export status check failed: {result.get('msg')}")
            return None
        task_result = result.get("data", {}).get("result", {})
        if task_result.get("file_token"):
            return task_result["file_token"]

    print("  Export timeout")
    return None


def download_exported_file(token, file_token):
    """下载导出后的文件"""
    url = f"https://open.feishu.cn/open-apis/drive/v1/export_tasks/download?file_token={file_token}"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers, timeout=60)
    if resp.status_code == 200:
        return resp.content
    print(f"  Download exported file failed: {resp.status_code}")
    return None


def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def save_hashes(hashes):
    os.makedirs(os.path.dirname(HASH_FILE), exist_ok=True)
    with open(HASH_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(hashes), f, ensure_ascii=False)


def safe_filename(name):
    invalid = '<>:"/\\|?*'
    for ch in invalid:
        name = name.replace(ch, "_")
    return name


def main():
    os.makedirs(RAW_DIR, exist_ok=True)

    print("Getting token...")
    token = get_token()

    print("Listing files...")
    files = list_files(token)
    print(f"Total files: {len(files)}")

    md_files = [f for f in files if f["name"].endswith(".md")]
    docx_files = [f for f in files if f["type"] == "docx"]
    other_files = [f for f in files if f not in md_files and f not in docx_files]

    print(f"  .md files: {len(md_files)}")
    print(f"  .docx files: {len(docx_files)}")
    if other_files:
        print(f"  Other (skipped): {len(other_files)}")

    synced_hashes = load_hashes()
    new_count = 0

    # 处理 .md 文件
    for file_info in md_files:
        try:
            file_token = file_info["token"]
            file_name = safe_filename(file_info["name"])
            print(f"\n[MD] {file_name}")

            content = download_md(token, file_token)
            if not content:
                continue

            content_hash = hashlib.md5(content).hexdigest()[:16]
            if content_hash in synced_hashes:
                print("  Already synced")
                continue

            filepath = os.path.join(RAW_DIR, file_name)
            with open(filepath, "wb") as f:
                f.write(content)

            synced_hashes.add(content_hash)
            new_count += 1
            print("  Saved")

        except Exception as e:
            print(f"  Error: {e}")
            continue

    # 处理 .docx 文件 → 导出为 .md
    for file_info in docx_files:
        try:
            doc_token = file_info["token"]
            original_name = file_info["name"]
            md_name = safe_filename(os.path.splitext(original_name)[0] + ".md")
            print(f"\n[DOCX→MD] {original_name} → {md_name}")

            exported_token = export_docx_to_md(token, doc_token)
            if not exported_token:
                continue

            content = download_exported_file(token, exported_token)
            if not content:
                continue

            content_hash = hashlib.md5(content).hexdigest()[:16]
            if content_hash in synced_hashes:
                print("  Already synced")
                continue

            filepath = os.path.join(RAW_DIR, md_name)
            with open(filepath, "wb") as f:
                f.write(content)

            synced_hashes.add(content_hash)
            new_count += 1
            print("  Saved")

        except Exception as e:
            print(f"  Error: {e}")
            continue

    save_hashes(synced_hashes)
    print(f"\n{'='*50}")
    print(f"Processed: {len(md_files)} md + {len(docx_files)} docx, New: {new_count}")
    print(f"{'='*50}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Sync failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
