#!/usr/bin/env python3
"""
飞书云盘文件夹 → GitHub 03-raw/ 同步
直接下载 .md 文件，无需转换
"""
import os
import json
import hashlib
import requests
from datetime import datetime

FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID")
FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET")
FOLDER_TOKEN = os.environ.get("FEISHU_FOLDER_TOKEN")

RAW_DIR = "03-raw/feishu"
HASH_FILE = "03-raw/.synced_hashes.json"

def get_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET})
    return resp.json().get("tenant_access_token")

def list_files(token):
    """列出文件夹内所有文件"""
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
            print(f"列出文件失败: {data}")
            break

        items = data.get("data", {}).get("files", [])
        print(f"API 返回 {len(items)} 个 items")

        for item in items:
            file_type = item.get("type")
            file_name = item.get("name", "")
            print(f"  文件: {file_name} | type: {file_type}")

            # 跳过文件夹(type=1)，其他全部保留
            if file_type != "1" and file_type != 1:
                files.append({
                    "token": item.get("token"),
                    "name": file_name,
                    "size": item.get("size", 0)
                })

        if not data.get("data", {}).get("has_more"):
            break
        page_token = data.get("data", {}).get("next_page_token")

    return files

def download_file(token, file_token):
    """下载文件内容"""
    url = f"https://open.feishu.cn/open-apis/drive/v1/files/{file_token}/download"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        return resp.content
    else:
        print(f"下载失败: {resp.status_code} {resp.text[:200]}")
        return None

def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r', encoding='utf-8') as f:
            return set(json.load(f))
    return set()

def save_hashes(hashes):
    os.makedirs(os.path.dirname(HASH_FILE), exist_ok=True)
    with open(HASH_FILE, 'w', encoding='utf-8') as f:
        json.dump(list(hashes), f, ensure_ascii=False)

def main():
    os.makedirs(RAW_DIR, exist_ok=True)

    print("Getting token...")
    token = get_token()
    if not token:
        print("Failed to get token")
        return

    print("Listing files...")
    files = list_files(token)
    print(f"Found {len(files)} files total")

    # 只处理 .md 文件
    md_files = [f for f in files if f["name"].endswith(".md")]
    print(f"Markdown files: {len(md_files)}")

    if not md_files:
        print("No .md files found")
        return

    synced_hashes = load_hashes()
    new_count = 0

    for file_info in md_files:
        try:
            file_token = file_info["token"]
            file_name = file_info["name"]

            print(f"\nDownloading: {file_name}")
            content = download_file(token, file_token)

            if not content:
                continue

            # 用内容哈希去重
            content_hash = hashlib.md5(content).hexdigest()[:16]
            if content_hash in synced_hashes:
                print(f"  Already synced")
                continue

            # 保存文件
            filepath = os.path.join(RAW_DIR, file_name)
            if os.path.exists(filepath):
                with open(filepath, "rb") as existing:
                    existing_hash = hashlib.md5(existing.read()).hexdigest()[:16]
                if existing_hash == content_hash:
                    synced_hashes.add(content_hash)
                    print(f"  Already exists")
                    continue
            counter = 1
            original = filepath
            while os.path.exists(filepath):
                name, ext = os.path.splitext(original)
                filepath = f"{name}_{counter}{ext}"
                counter += 1

            with open(filepath, "wb") as f:
                f.write(content)

            synced_hashes.add(content_hash)
            new_count += 1
            print(f"  Saved: {os.path.basename(filepath)}")

        except Exception as e:
            print(f"  Error: {e}")
            continue

    save_hashes(synced_hashes)
    print(f"\n{'='*50}")
    print(f"Total: {len(md_files)}, New: {new_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
