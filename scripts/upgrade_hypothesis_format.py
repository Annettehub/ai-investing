"""
Upgrade all hypothesis files to new format:
- Kill Metric table (threshold + time window)
- Evidence timeline (date + impact + source label)
- Kill Thesis monthly review
- Source label format in change records
"""

import re
import os
from pathlib import Path

HYPOTHESES_DIR = Path("D:/WorkBuddy/Claw/ai-investing/02-kb/hypotheses")


def extract_field(content, field_name):
    """Extract a field value from the hypothesis frontmatter list items."""
    pattern = rf"-\s+\*\*{re.escape(field_name)}\*\*:\s*(.+)"
    m = re.search(pattern, content)
    if m:
        return m.group(1).strip()
    return ""


def extract_data_anchors(content):
    """Extract all data anchor entries (lines starting with '  - [' under 数据锚点)."""
    anchors = []
    in_section = False
    for line in content.split("\n"):
        if "**数据锚点**" in line:
            in_section = True
            continue
        if in_section:
            if line.strip().startswith("- [") or line.strip().startswith("- [待补充"):
                anchors.append(line.strip("- ").strip())
            elif line.strip() == "":
                continue
            elif line.strip().startswith("#"):
                break
            elif line.strip().startswith("##"):
                break
            elif line.strip().startswith("- **"):
                break
            elif anchors:  # we've collected some, next non-anchor line means end
                break
    return anchors


def extract_falsification(content):
    """Extract falsification conditions from 证伪条件 field."""
    fals = extract_field(content, "证伪条件")
    if fals:
        # Split by common separators
        conditions = re.split(r'[，。,、]|\bor\b|或', fals)
        conditions = [c.strip() for c in conditions if c.strip() and len(c.strip()) > 5]
        return conditions
    return []


def extract_change_records(content):
    """Extract change record table rows."""
    records = []
    in_table = False
    for line in content.split("\n"):
        if line.strip().startswith("| 日期 | certainty%"):
            in_table = True
            continue
        if in_table:
            if line.strip().startswith("|------"):
                continue
            if line.strip().startswith("| ") and "|" in line[2:]:
                records.append(line.strip())
            elif line.strip() == "":
                continue
            elif not line.strip().startswith("|"):
                break
    return records


def to_kill_metric(conditions):
    """Convert falsification conditions to Kill Metric table rows."""
    if not conditions:
        return """| 证伪条件 | 阈值 | 时间窗口 | 当前状态 |
|----------|------|----------|----------|
| 待用户定义 | 待定义 | 2个季度 | 待观测 |
| 待用户定义 | 待定义 | 2个季度 | 待观测 |"""
    
    rows = []
    for i, cond in enumerate(conditions):
        # Try to extract threshold and time window from the condition text
        threshold = "待校准"
        time_window = "待校准"
        
        # Extract percentage thresholds
        pct_match = re.search(r'[<>]\s*\d+%', cond)
        if pct_match:
            threshold = pct_match.group()
        
        # Extract time windows
        time_match = re.search(r'(\d+\s*个?[季度月周]|[Qq]\d|202\d)', cond)
        if time_match:
            time_window = time_match.group(1)
        
        status = "待观测"
        rows.append(f"| {cond} | {threshold} | {time_window} | {status} |")
    
    header = "| 证伪条件 | 阈值 | 时间窗口 | 当前状态 |\n|----------|------|----------|----------|"
    return header + "\n" + "\n".join(rows)


def to_evidence_timeline(anchors):
    """Convert data anchors to evidence timeline."""
    if not anchors:
        return """| 日期 | 证据 | 影响 | 来源标签 |
|------|------|------|----------|
| 待补充 | 待补充 | 🟡 | [待验证] |"""
    
    rows = []
    for anchor in anchors:
        # Extract date if present
        date_match = re.search(r'(\d{4}[-/]\d{2}[-/]\d{2})', anchor)
        date = date_match.group(1) if date_match else "日期待标注"
        
        # Extract source type
        source_label = "[知识星球]"
        if "[网页]" in anchor:
            source_label = "[网页]"
        elif "[数据]" in anchor:
            source_label = "[数据]"
        elif "[本地]" in anchor:
            source_label = "[本地]"
        elif "[推测]" in anchor:
            source_label = "[推测]"
        elif "[待验证]" in anchor:
            source_label = "[待验证]"
        
        # Determine impact - default to 🟢 (supporting) unless evidence suggests otherwise
        impact = "🟢"
        anchor_lower = anchor.lower()
        if any(kw in anchor_lower for kw in ["不会", "无法", "否认", "伪", "质疑", "不改变", "下滑", "下跌", "过剩", "幻觉", "误导"]):
            impact = "🔴"
        elif any(kw in anchor_lower for kw in ["不确定", "分歧", "争议", "待观察", "两面"]):
            impact = "🟡"
        
        # Clean the anchor text - remove source prefix
        evidence_text = re.sub(r'^\[.*?\]\s*', '', anchor)
        # Truncate if too long
        if len(evidence_text) > 100:
            evidence_text = evidence_text[:97] + "..."
        
        rows.append(f"| {date} | {evidence_text} | {impact} | {source_label} |")
    
    header = "| 日期 | 证据 | 影响 | 来源标签 |\n|------|------|------|----------|"
    return header + "\n" + "\n".join(rows)


def upgrade_file(filepath):
    """Upgrade a single hypothesis file to new format."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    dim_code = extract_field(content, "维度")
    certainty = extract_field(content, "certainty%")
    status = extract_field(content, "状态")
    theme = extract_field(content, "关联 theme")
    company = extract_field(content, "关联 company")
    create_date = extract_field(content, "创建日期")
    update_date = extract_field(content, "最后更新")
    
    falsification = extract_falsification(content)
    anchors = extract_data_anchors(content)
    change_records = extract_change_records(content)
    
    # Extract the title line (first # heading)
    title_match = re.search(r"^#\s+H\d+\.\d+\s+.*$", content, re.MULTILINE)
    title_line = title_match.group(0) if title_match else "# H?.? [Unknown] Unknown"
    
    # Extract source articles section if exists
    source_section = ""
    source_match = re.search(r"## 来源文章\n\n(.*?)(?=\n## |$)", content, re.DOTALL)
    if source_match:
        source_section = f"## 来源文章\n\n{source_match.group(1).strip()}\n"
    
    # Build Kill Metric
    kill_metric = to_kill_metric(falsification)
    
    # Build evidence timeline
    evidence_timeline = to_evidence_timeline(anchors)
    
    # Build change records with source labels
    change_lines = []
    if change_records:
        for rec in change_records:
            # Add source label if missing
            if "[知识星球]" in rec or "[本地]" in rec or "[数据]" in rec or "[网页]" in rec or "[推测]" in rec:
                change_lines.append(rec)
            else:
                # Default to 知识星球 if it mentions 用户 or 星球
                if "星球" in rec or "用户" in rec:
                    rec += " [知识星球]"
                else:
                    rec += " [待标注]"
                change_lines.append(rec)
    
    # Build the new file
    new_content = f"""{title_line}

- **状态**: {status}
- **维度**: {dim_code}
- **certainty%**: {certainty}
- **投资方向**: 纯置信度判断，不绑定仓位

## Kill Metric

> 证伪条件必须可观测、有具体阈值和时间窗口。触发任一条件 → certainty% 归零，移入 false-beliefs。

{kill_metric}

## 证据时间线

> 按日期倒序，🟢=支持假设 / 🔴=削弱假设 / 🟡=方向不明确

{evidence_timeline}

## 关联关系

- **关联 theme**: {theme}
- **关联 company**: {company}
- **创建日期**: {create_date}
- **最后更新**: {update_date}

## 确定性变更记录

| 日期 | certainty% 变更 | 原因 | 来源标签 |
|------|----------------|------|----------|
{chr(10).join(change_records)}

## Kill Thesis 月度回看

> 最近回看日期: {create_date}

1. 当前证据是否仍支持假设方向？如有矛盾，最核心的是什么？
2. 是否有新出现的反方证据被忽视或未纳入时间线？
3. Kill Metric 阈值的紧迫性是否变化？是否需要收紧或放宽？
"""
    
    if source_section:
        new_content += f"\n{source_section}"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    return filepath.name


def main():
    files = sorted(HYPOTHESES_DIR.glob("H*.md"))
    updated = []
    
    for f in files:
        name = upgrade_file(f)
        updated.append(name)
        print(f"✅ {name}")
    
    print(f"\n总计升级 {len(updated)} 条假设")

if __name__ == "__main__":
    main()
