#!/usr/bin/env python3
"""
飞书云盘 docx 文件 → 下载 → markitdown 转 Markdown → 03-raw/feishu/
"""
import os, json, hashlib, sys, subprocess, tempfile
import requests

FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID")
FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET")
FOLDER_TOKEN = os.environ.get("FEISHU_FOLDER_TOKEN")

RAW_DIR = "03-raw/feishu"
HASH_FILE = "03-raw/.synced_docx_hashes.json"

# markitdown executable path
MARKITDOWN_PYTHON = r"C:\Users\Annette Zhang\.workbuddy\binaries\python\versions\3.13.12\python.exe"

def get_token():
    missing = [name for name, value in (
        ("FEISHU_APP_ID", FEISHU_APP_ID),
        ("FEISHU_APP_SECRET", FEISHU_APP_SECRET),
        ("FEISHU_FOLDER_TOKEN", FOLDER_TOKEN),
    ) if not value]
    if missing:
        raise RuntimeError(f"Missing env vars: {', '.join(missing)}")
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET}, timeout=30)
    data = resp.json()
    if resp.status_code != 200 or data.get("code") != 0:
        raise RuntimeError(f"Token failed: {data.get('msg')}")
    return data.get("tenant_access_token")

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
            raise RuntimeError(f"List failed: {data.get('msg')}")
        items = data.get("data", {}).get("files", [])
        for item in items:
            file_type = item.get("type")
            file_name = item.get("name", "")
            if file_type not in ("1", 1):
                files.append({"token": item.get("token"), "name": file_name, "type": file_type})
        if not data.get("data", {}).get("has_more"):
            break
        page_token = data.get("data", {}).get("next_page_token")
    return files

def download_file(token, file_token, file_type):
    headers = {"Authorization": f"Bearer {token}"}
    if file_type == "docx":
        url = f"https://open.feishu.cn/open-apis/drive/v1/files/{file_token}/export"
        resp = requests.post(url, headers=headers, params={"file_extension": "docx"})
    else:
        url = f"https://open.feishu.cn/open-apis/drive/v1/files/{file_token}/download"
        resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.content
    print(f"  Download failed: {resp.status_code}")
    try:
        err = resp.json()
        print(f"  Error: code={err.get('code')}, msg={err.get('msg')}")
    except:
        print(f"  Body: {resp.text[:300]}")
    return None

def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r', encoding='utf-8') as f:
            return set(json.load(f))
    return set()

def save_hashes(hashes):
    os.makedirs(os.path.dirname(HASH_FILE), exist_ok=True)
    with open(HASH_FILE, 'w', encoding='utf-8') as f:
        json.dump(sorted(hashes), f, ensure_ascii=False)

def docx_to_md(docx_bytes, title):
    """Convert docx bytes to markdown using markitdown"""
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
        tmp.write(docx_bytes)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            [MARKITDOWN_PYTHON, "-m", "markitdown", tmp_path],
            capture_output=True, text=True, timeout=120,
            encoding='utf-8', errors='replace'
        )
        if result.returncode == 0 and result.stdout.strip():
            md = result.stdout.strip()
        else:
            # If markitdown fails, save the docx file directly and note it
            print(f"  markitdown conversion failed: {result.stderr[:200]}")
            return None
    finally:
        os.unlink(tmp_path)

    return md

def make_safe_filename(name):
    safe = name.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_')
    safe = safe.replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
    return safe

def main():
    os.makedirs(RAW_DIR, exist_ok=True)

    print("Getting token...")
    token = get_token()

    print("Listing files...")
    all_files = list_files(token)
    print(f"Found {len(all_files)} files total")

    # Filter for docx type documents, skip "本文档勿同步"
    docx_files = [f for f in all_files
                  if f["type"] == "docx"
                  and "勿同步" not in f["name"]]
    print(f"DOCX files to process: {len(docx_files)}")

    if not docx_files:
        print("No new .docx files to process")
        return 0

    for f in docx_files:
        print(f"  - {f['name']}")

    synced_hashes = load_hashes()
    new_count = 0

    for file_info in docx_files:
        try:
            file_token = file_info["token"]
            file_name = file_info["name"]

            print(f"\nDownloading: {file_name}")
            content = download_file(token, file_token, file_info["type"])
            if not content:
                continue

            # Use content hash for dedup
            content_hash = hashlib.md5(content).hexdigest()[:16]
            if content_hash in synced_hashes:
                print(f"  Already synced (hash: {content_hash})")
                continue

            # Convert to markdown
            md_content = docx_to_md(content, file_name)
            if md_content is None:
                print(f"  Conversion failed, skipping")
                continue

            # Generate output filename
            base_name = os.path.splitext(file_name)[0]
            safe_name = make_safe_filename(base_name)
            out_name = f"{safe_name}.md"
            out_path = os.path.join(RAW_DIR, out_name)

            # Handle duplicates
            counter = 1
            original = out_path
            while os.path.exists(out_path):
                name_part, _ = os.path.splitext(original)
                out_path = f"{name_part}_{counter}.md"
                counter += 1

            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(md_content)

            synced_hashes.add(content_hash)
            new_count += 1
            print(f"  Saved: {os.path.basename(out_path)} ({len(md_content)} chars)")

        except Exception as e:
            print(f"  Error: {e}")
            continue

    save_hashes(synced_hashes)
    print(f"\n{'='*50}")
    print(f"Total docx: {len(docx_files)}, New: {new_count}")
    print(f"{'='*50}")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Sync failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
