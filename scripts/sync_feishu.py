#!/usr/bin/env python3
"""
飞书多维表格 → GitHub 03-raw/ 自动同步
适配你的 ai-investing 仓库结构
"""
import os
import re
import requests
from datetime import datetime

# ========== 配置 ==========
FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID")
FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET")
BASE_TOKEN = os.environ.get("FEISHU_BASE_TOKEN")
TABLE_ID = os.environ.get("FEISHU_TABLE_ID")

RAW_DIR = "03-raw"
PROCESSED_DIR = "03-raw/processed"
SYNCED_STATUS = "已同步"
PENDING_STATUS = "待同步"

# ========== 飞书 API 工具 ==========
def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET})
    data = resp.json()
    if data.get("code") != 0:
        print(f"获取token失败: {data}")
        return None
    return data.get("tenant_access_token")

def get_records(token):
    """读取待同步记录"""
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{BASE_TOKEN}/tables/{TABLE_ID}/records"
    headers = {"Authorization": f"Bearer {token}"}
    
    all_records = []
    page_token = None
    
    while True:
        params = {"page_size": 500}
        if page_token:
            params["page_token"] = page_token
        
        resp = requests.get(url, headers=headers, params=params)
        data = resp.json()
        
        if data.get("code") != 0:
            print(f"获取记录失败: {data}")
            break
        
        items = data.get("data", {}).get("items", [])
        all_records.extend(items)
        
        has_more = data.get("data", {}).get("has_more", False)
        page_token = data.get("data", {}).get("page_token")
        
        if not has_more or not page_token:
            break
    
    # 筛选待同步
    pending = []
    for item in all_records:
        fields = item.get("fields", {})
        status = fields.get("处理状态", "")
        if isinstance(status, dict):
            status = status.get("text", "")
        if status == PENDING_STATUS:
            pending.append(item)
    
    return pending

def update_record_status(token, record_id, status):
    """更新状态"""
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{BASE_TOKEN}/tables/{TABLE_ID}/records/{record_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    body = {"fields": {"处理状态": {"text": status}}}
    resp = requests.put(url, headers=headers, json=body)
    return resp.json()

# ========== 字段解析 ==========
def extract_field_value(field_value):
    if field_value is None:
        return ""
    if isinstance(field_value, (str, int, float, bool)):
        return str(field_value)
    if isinstance(field_value, dict):
        if "text" in field_value:
            return field_value["text"]
        return str(field_value)
    if isinstance(field_value, list):
        texts = []
        for item in field_value:
            if isinstance(item, dict) and "text" in item:
                texts.append(item["text"])
            else:
                texts.append(str(item))
        return ", ".join(texts)
    return str(field_value)

# ========== Markdown 生成 ==========
def record_to_markdown(record):
    fields = record.get("fields", {})
    record_id = record.get("record_id", "")
    
    title = extract_field_value(fields.get("标题", "未命名"))
    source = extract_field_value(fields.get("来源", ""))
    tags = extract_field_value(fields.get("关联标的", ""))
    info_type = extract_field_value(fields.get("信息类型", ""))
    content = extract_field_value(fields.get("原始内容", ""))
    link = extract_field_value(fields.get("链接", ""))
    certainty = extract_field_value(fields.get("可信度", ""))
    comment = extract_field_value(fields.get("我的批注", ""))
    created = extract_field_value(fields.get("创建时间", datetime.now().isoformat()))
    
    # 清理文件名
    safe_title = re.sub(r'[^\w\s-]', '', title).strip()[:50]
    safe_title = re.sub(r'[\s]+', '_', safe_title)
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"{date_str}_{source}_{safe_title}.md"
    
    md_content = f"""---
date: {created}
source: {source}
type: {info_type}
tags: [{tags}]
certainty: {certainty}
feishu_record_id: {record_id}
status: raw
---

## 标题
{title}

## 来源
{source}

## 关联标的
{tags}

## 原始内容
{content}

## 链接
{link if link else "无"}

## 我的批注
{comment if comment else "无"}

## 同步记录
- 同步时间: {datetime.now().isoformat()}
- 来源: 飞书多维表格
- 原始记录ID: {record_id}
"""
    return filename, md_content

# ========== 主流程 ==========
def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    
    print("Getting Feishu access token...")
    token = get_tenant_access_token()
    if not token:
        print("Failed to get token")
        return
    
    print("Fetching pending records...")
    records = get_records(token)
    print(f"Found {len(records)} pending records")
    
    if not records:
        print("No pending records to sync.")
        return
    
    synced_count = 0
    failed_records = []
    
    for record in records:
        try:
            record_id = record.get("record_id")
            filename, content = record_to_markdown(record)
            filepath = os.path.join(RAW_DIR, filename)
            
            # 避免文件名冲突
            counter = 1
            original_filepath = filepath
            while os.path.exists(filepath):
                name, ext = os.path.splitext(original_filepath)
                filepath = f"{name}_{counter}{ext}"
                counter += 1
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            # 更新飞书状态
            result = update_record_status(token, record_id, SYNCED_STATUS)
            if result.get("code") != 0:
                print(f"Warning: failed to update status for {record_id}: {result}")
                failed_records.append(record_id)
            else:
                synced_count += 1
                print(f"Synced: {filename}")
            
        except Exception as e:
            print(f"Error processing record {record.get('record_id')}: {e}")
            failed_records.append(record.get("record_id"))
            continue
    
    print(f"\n{'='*50}")
    print(f"Total processed: {len(records)}")
    print(f"Successfully synced: {synced_count}")
    if failed_records:
        print(f"Failed to update status: {len(failed_records)} ({', '.join(failed_records)})")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
