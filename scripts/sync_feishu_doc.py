#!/usr/bin/env python3
"""
飞书新版 docx → GitHub 03-raw/ 自动同步
使用飞书官方 lark-oapi SDK，自动处理认证和 blocks 遍历
"""
import os
import re
import json
import hashlib
from datetime import datetime

# 飞书官方 Python SDK：pip install lark-oapi
from lark_oapi import Client
from lark_oapi.api.docx.v1 import *

# ========== 配置 ==========
FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID")
FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET")
DOC_TOKEN = os.environ.get("FEISHU_DOC_TOKEN")

RAW_DIR = "03-raw"
HASH_FILE = "03-raw/.synced_hashes.json"

# ========== 初始化飞书客户端 ==========
# lark-oapi 自动处理 tenant_access_token 的获取和刷新
client = Client.builder() \
    .app_id(FEISHU_APP_ID) \
    .app_secret(FEISHU_APP_SECRET) \
    .build()

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

# ========== 文档读取（lark-oapi 封装版）==========
def extract_text_from_block(block):
    """从单个 block 中提取纯文本"""
    block_type = block.block_type
    text_elements = []
    
    # 根据 block 类型获取文本元素
    if block_type == 2 and block.text:           # 文本
        text_elements = block.text.elements
    elif block_type == 3:                         # 标题
        if block.heading1:
            text_elements = block.heading1.elements
        elif block.heading2:
            text_elements = block.heading2.elements
        elif block.heading3:
            text_elements = block.heading3.elements
    elif block_type == 4 and block.quote:        # 引用
        text_elements = block.quote.elements
    elif block_type == 5 and block.bullet:       # 无序列表
        text_elements = block.bullet.elements
    elif block_type == 6 and block.ordered:       # 有序列表
        text_elements = block.ordered.elements
    elif block_type == 14 and block.code:         # 代码块
        text_elements = block.code.elements
    
    # 提取文本内容
    texts = []
    for elem in text_elements:
        if elem.text_run and elem.text_run.content:
            texts.append(elem.text_run.content)
    
    return "".join(texts)

def get_all_doc_text(doc_token):
    """递归获取文档所有文本内容"""
    all_lines = []
    
    # 1. 获取文档根 blocks（分页处理）
    page_token = None
    root_blocks = []
    
    while True:
        req = ListDocumentBlockRequest.builder() \
            .document_id(doc_token) \
            .page_token(page_token) \
            .page_size(500) \
            .build()
        resp = client.docx.v1.document_block.list(req)
        
        if not resp.success():
            print(f"获取文档 blocks 失败: {resp.code} {resp.msg}")
            return ""
        
        items = resp.data.items
        root_blocks.extend(items)
        
        if not resp.data.has_more:
            break
        page_token = resp.data.page_token
    
    # 2. 递归处理 blocks 及其子 blocks
    def process_blocks(blocks):
        for block in blocks:
            text = extract_text_from_block(block)
            if text:
                all_lines.append(text)
            
            # 递归处理子 blocks
            if block.children:
                for child_id in block.children:
                    child_page_token = None
                    while True:
                        child_req = ListDocumentBlockChildrenRequest.builder() \
                            .document_id(doc_token) \
                            .block_id(child_id) \
                            .page_token(child_page_token) \
                            .page_size(500) \
                            .build()
                        child_resp = client.docx.v1.document_block_children.list(child_req)
                        
                        if child_resp.success() and child_resp.data.items:
                            process_blocks(child_resp.data.items)
                        
                        if not child_resp.data.has_more:
                            break
                        child_page_token = child_resp.data.page_token
    
    process_blocks(root_blocks)
    return "\n".join(all_lines)

# ========== 文档解析（按日期分割记录）==========
def parse_doc_records(text):
    """解析文档内容，按日期分割成多条记录"""
    text = text.strip()
    if not text:
        return []
    
    records = []
    
    # 策略1：按日期行分割（YYYY-MM-DD 开头）
    date_pattern = r'(?:^|\n)\s*(?:【)?(\d{4}-\d{2}-\d{2})(?:】)?\s*'
    parts = re.split(date_pattern, text)
    
    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            if i + 1 > len(parts) - 1:
                continue
            
            date_str = parts[i].strip()
            block = parts[i + 1].strip()
            lines = block.split('\n')
            meta_line = lines[0] if lines else ""
            content = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""
            
            # 解析元数据行
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
            
            # 如果内容为空，退化为把 meta_line 当内容
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
    
    # 清理文件名
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
    
    print("Fetching document content via lark-oapi...")
    doc_text = get_all_doc_text(DOC_TOKEN)
    
    if not doc_text:
        print("Document is empty or failed to read")
        return
    
    print(f"Document length: {len(doc_text)} chars")
    
    records = parse_doc_records(doc_text)
    print(f"Parsed {len(records)} records from document")
    
    if not records:
        print("No records found")
        return
    
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
    
    save_synced_hashes(synced_hashes)
    
    print(f"\n{'='*50}")
    print(f"Total records in doc: {len(records)}")
    print(f"Newly synced: {new_count}")
    print(f"Skipped (duplicate): {skipped_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
