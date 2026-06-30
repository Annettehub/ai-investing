#!/usr/bin/env python3
"""
飞书云文档 → GitHub 03-raw/ 自动同步
用户只需在云文档里按格式粘贴，脚本自动解析、去重、生成 Markdown
"""
import os
import re
import json
import hashlib
import requests
from datetime import datetime

# ========== 配置 ==========
FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID")
FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET")
DOC_TOKEN = os.environ.get("FEISHU_DOC_TOKEN")

RAW_DIR = "03-raw"
HASH_FILE = "03-raw/.synced_hashes.json"

# ========== 飞书 API 工具 ==========
def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET})
    data = resp.json()
    if data.get("code") != 0:
        print(f"获取token失败: {data}")
        return None
    return data.get("tenant_access_token")

def get_doc_content(token):
    """
    读取飞书云文档内容。
    优先尝试新版 docx API，失败则回退旧版 doc API。
    """
    headers = {"Authorization": f"Bearer {token}"}
    
    # 尝试新版 docx API
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{DOC_TOKEN}/raw_content"
    resp = requests.get(url, headers=headers)
    data = resp.json()
    if data.get("code") == 0:
        content = data.get("data", {}).get("content", "")
        if content:
            return content
    
    # 回退旧版 doc API（纯文本）
    url = f"https://open.feishu.cn/open-apis/doc/v2/{DOC_TOKEN}/content?format=text"
    resp = requests.get(url, headers=headers)
    data = resp.json()
    if data.get("code") == 0:
        return data.get("data", {}).get("content", "")
    
    print(f"读取文档失败: {data}")
    return ""

# ========== 去重机制 ==========
def load_synced_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r', encoding='utf-8') as f:
            return set(json.load(f))
    return set()

def save_synced_hashes(hashes):
    os.makedirs(os.path.dirname(HASH_FILE), exist_ok=True)
    with open(HASH_FILE, 'w', encoding='utf-8') as f:
        json.dump(list(hashes), f, ensure_ascii=False)

def get_content_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()[:16]

# ========== 文档解析 ==========
def parse_doc_records(text):
    """
    解析文档内容，按日期/分隔符分割成多条记录。
    支持格式：
      2026-06-30 | 来源 | 标的
      内容...
      
      2026-06-30 | 来源 | 标的
      内容...
    """
    text = text.strip()
    if not text:
        return []
    
    records = []
    
    # 策略1：按日期行分割（YYYY-MM-DD 开头）
    # 匹配行首的日期，前面可能有空行或空格
    date_pattern = r'(?:^|\n)\s*(?:【)?(\d{4}-\d{2}-\d{2})(?:】)?\s*'
    parts = re.split(date_pattern, text)
    
    if len(parts) > 1:
        # parts[0] 是文档开头说明（忽略）
        for i in range(1, len(parts), 2):
            if i + 1 > len(parts) - 1:
                continue
            
            date_str = parts[i].strip()
            block = parts[i + 1].strip()
            
            lines = block.split('\n')
            meta_line = lines[0] if lines else ""
            content = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""
            
            # 解析元数据行：来源 | 标的
            source = "未知"
            tags = "未分类"
            
            # 尝试 "来源：xxx 标的：xxx" 格式
            s_match = re.search(r'来源[：:]\s*([^|\n]+?)(?:\s+标的[：:]|$)', meta_line)
            if s_match:
                source = s_match.group(1).strip()
                t_match = re.search(r'标的[：:]\s*([^\n]+)', meta_line)
                if t_match:
                    tags = t_match.group(1).strip()
            else:
                # 尝试 "|" 分隔格式
                meta_parts = [p.strip() for p in meta_line.split('|')]
                if len(meta_parts) >= 2:
                    source = meta_parts[0]
                    tags = meta_parts[1]
                elif meta_parts:
                    source = meta_parts[0]
            
            # 如果内容为空，可能用户只写了一行，把 meta_line 当内容
            if not content and meta_line:
                content = meta_line
                source = "未知"
                tags = "未分类"
            
            raw_text = f"{date_str}\n{meta_line}\n{content}"
            records.append({
                'date': date_str,
                'source': source,
                'tags': tags,
                'content': content,
                'raw': raw_text
            })
    
    # 策略2：如果日期分割失败，退化为按双空行分块
    if not records:
        blocks = [b.strip() for b in re.split(r'\n\s*\n', text) if b.strip()]
        for block in blocks:
            lines = block.split('\n')
            first_line = lines[0].strip()
            content = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""
            
            # 尝试从第一行提取日期
            d_match = re.search(r'(\d{4}-\d{2}-\d{2})', first_line)
            date_str = d_match.group(1) if d_match else datetime.now().strftime("%Y-%m-%d")
            
            raw_text = block
            records.append({
                'date': date_str,
                'source': first_line,
                'tags': "未分类",
                'content': content,
                'raw': raw_text
            })
    
    return records

# ========== Markdown 生成 ==========
def record_to_markdown(record, index):
    date_str = record['date']
    source = record['source']
    tags = record['tags']
    content = record['content']
    raw_text = record['raw']
    
    # 文件名
    safe_source = re.sub(r'[^\w\s-]', '', source).strip()[:20]
    safe_source = re.sub(r'[\s]+', '_', safe_source)
    safe_tags = re.sub(r'[^\w\s-]', '', tags).strip()[:20]
    safe_tags = re.sub(r'[\s]+', '_', safe_tags)
    
    filename = f"{date_str.replace('-', '')}_{safe_source}_{safe_tags}_{index}.md"
    
    md_content = f"""---
date: {date_str}
source: {source}
type: 原始信息
tags: [{tags}]
certainty: 中
status: raw
---

## 来源
{source}

## 关联标的
{tags}

## 原始内容
{content}

## 同步记录
- 同步时间: {datetime.now().isoformat()}
- 来源: 飞书云文档
- 内容哈希: {get_content_hash(raw_text)}
"""
    return filename, md_content, raw_text

# ========== 主流程 ==========
def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    
    print("Getting Feishu access token...")
    token = get_tenant_access_token()
    if not token:
        print("Failed to get token")
        return
    
    print("Fetching document content...")
    doc_text = get_doc_content(token)
    if not doc_text:
        print("Document is empty or failed to read")
        return
    
    print(f"Document length: {len(doc_text)} chars")
    
    # 解析记录
    records = parse_doc_records(doc_text)
    print(f"Parsed {len(records)} records from document")
    
    if not records:
        print("No records found")
        return
    
    # 加载已同步哈希
    synced_hashes = load_synced_hashes()
    print(f"Previously synced hashes: {len(synced_hashes)}")
    
    new_count = 0
    skipped_count = 0
    
    for idx, record in enumerate(records, 1):
        raw_text = record['raw']
        content_hash = get_content_hash(raw_text)
        
        # 去重检查
        if content_hash in synced_hashes:
            skipped_count += 1
            continue
        
        filename, md_content, _ = record_to_markdown(record, idx)
        filepath = os.path.join(RAW_DIR, filename)
        
        # 避免文件名冲突
        counter = 1
        original = filepath
        while os.path.exists(filepath):
            name, ext = os.path.splitext(original)
            filepath = f"{name}_{counter}{ext}"
            counter += 1
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        synced_hashes.add(content_hash)
        new_count += 1
        print(f"Synced: {filename}")
    
    # 保存哈希
    save_synced_hashes(synced_hashes)
    
    print(f"\n{'='*50}")
    print(f"Total records in doc: {len(records)}")
    print(f"Newly synced: {new_count}")
    print(f"Skipped (duplicate): {skipped_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
