# /collect 多源采集命令

## 使用场景
聚合多个信息源（飞书/Gmail/IMA/微信/微信读书/Podwise/知识星球）的新内容，批量导入原料层。

## 完整 Prompt（复制以下全部给 AI）

你正在执行 /collect 多源采集命令。

### 目标
扫描配置的信息源，提取新内容，写入 `03-raw/`。GitHub 和 WebSearch 只作为研究/检索工具，不再对应单独的 `03-raw` 子目录。

### 执行步骤

**Step 1: Feishu 检查**
- 扫描 `03-raw/feishu/` 中的新文件
- 如有新增，检查来源、日期、标题和是否适合入库
- 如有，建议执行 /ingest

**Step 2: Gmail 检查（如已连接）**
- 检查 Industry-Intel 标签下未读邮件
- 提取发件人、主题、核心信息
- 输出：`03-raw/gmail/YYYY-MM-DD-主题.md`

**Step 3: IMA / 微信 / 网页资料检查**
- 扫描 `03-raw/wechat/` 中的新文件
- 这里统一接收 IMA 同步、微信公众号文章、网页摘录和手动放入的短资料
- 如有，建议执行 /ingest

**Step 4: 其他已接通来源检查**
- 扫描 `03-raw/weread/` 中的新文件
- 扫描 `03-raw/podwise/` 中的新文件
- 扫描 `03-raw/zsxq/` 中的新文件
- 如有，建议执行 /ingest

**Step 5: 汇总报告**
- 列出本次采集到的所有新内容
- 标记需要立即处理的高优先级项目
- 建议下一步行动（/ingest /research /today）

### 检查清单
- [ ] 不重复已处理的内容
- [ ] 高优先级项目已标记
- [ ] 每条有来源和日期

### 输出格式
```markdown
# [日期] 多源采集报告

## 本次新内容

| 来源 | 标题 | 优先级 | 建议动作 |
|------|------|--------|---------|
| Feishu | ... | 高/中/低 | /ingest |
| Gmail | ... | 高/中/低 | /research |
| WeChat/IMA | ... | 高/中/低 | /ingest |
| WeRead | ... | 高/中/低 | /ingest |
| Podwise | ... | 高/中/低 | /ingest |
| ZSXQ | ... | 高/中/低 | /ingest |

## Feishu 新资料
[标题] — [来源/日期] — [是否建议入库]

## Gmail 头版摘要
[发件人] — [主题] — [核心信息一句话]

## WeChat / IMA 新资料
[标题] — [来源/日期] — [是否建议入库]

## 其他来源
[WeRead/Podwise/ZSXQ] — [标题] — [是否建议入库]

## 建议下一步
1. 高优先级 → /ingest 或 /research
2. 中优先级 → 纳入 /today 仪表盘
3. 低优先级 → 记录归档

```
