# 小苔花 · AI投研系统 — Agent 入口协议

> 本文件是 WorkBuddy / Claude / Kimi 等 AI Agent 进入此目录后的第一站。
> 协议不在模型里，在文件里。改行为 = 改 Markdown，不写代码。

---

## 一、进入后必读顺序

1. `active-context.md` — 上次在哪中断，直接续上
2. `ENV-GUIDE.md` — 当前环境（公司🏢/家里🏠/手机📱），决定能做什么
3. `00-system/SYSTEM.md` — 系统哲学和架构
4. `02-kb/index.md` — 知识库总览
5. 如有待处理 → `03-raw/` 检查新原始材料

---

## 二、李龙·AI五层蛋糕（投研透镜）

```
L5 AI应用: TSLA, ServiceNow, Cursor, 老铺黄金
L4 基础模型: OpenAI, Anthropic, xAI（跟踪不交易）
L3 AI基建: 数据中心, 光模块, ANET, VRT, DELL, AIDC电源
L2 芯片: NVDA, TSM, MU, AVGO, 村田, 中际旭创, 00981
L1 电力: 电网/发电/能源（不碰）
```

层错位=α：L4烧钱时，L2/L3卖铲子赚钱。

---

## 三、七个工作流命令

| 命令 | 用途 | 执行方式 |
|------|------|---------|
| `/idea` | 信号收集 | 粘贴信号 → AI 分类定位 |
| `/ingest` | 信息入库 | 给原始材料 → AI 编译入 02-kb/sources/ |
| `/research` | 深度研究 | 7步法：定位→价值链→竞争→财务→假设→城墙→错位 |
| `/today` | 每日检查 | 检查假设+城墙+跨层信号 |
| `/weekly` | 周度复盘 | 汇总变化+模式发现+规则晋升 |
| `/trade` | 交易决策 | 认知→映射→矩阵→退出预演 |
| `/update` | 系统体检 | 每月清理孤岛/过时规则/假设僵尸 |

调用方式：`执行 /today 命令`，或粘贴命令文件内容。

---

## 四、知识库三层结构

| 层 | 目录 | 内容 | 规则 |
|----|------|------|------|
| 原料层 | `02-kb/sources/` | 研报/纪要/新闻摘要 | 只读不删，保留原始出处 |
| 提炼层 | `02-kb/entities/` + `02-kb/concepts/` | 公司档案 + 概念 | 双向链接，来源可追溯 |
| 判断层 | `02-kb/hypotheses/` + `02-kb/walls/` | 假设 + 城墙 | 带certainty%，可证伪 |

---

## 五、三闭环

1. **假设验证闭环**：设假设 → /today 跟踪 → 升降 certainty% → 回写（错→false-beliefs）
2. **知识沉淀闭环**：外部材料 → /ingest → sources → 渗透 entities/concepts → /research 引用
3. **规则晋升闭环**：观察到模式 → 验证≥3次 → 晋升 `00-system/rules.md`（被推翻→false-beliefs）

---

## 六、多源信息管道

| 源 | 状态 | 输入方式 | 到达位置 |
|----|------|---------|---------|
| GitHub | ✅ | Star/Watch → WebFetch | 03-raw/github/ |
| 飞书云盘 | ⚡ | sync_feishu_drive.py → GitHub Actions | 03-raw/feishu/ |
| Gmail | 🔜 | 过滤器+标签 → connector | 03-raw/gmail/ |
| 微信读书 | ✅ | API自动同步 → GitHub Actions | 03-raw/weread/ |
| 知识星球 | ✅ | 手动导入 → 03-raw/zsxq/ | 03-raw/zsxq/ |
| 行情数据 | 🔑 | fetch_market_data.py → watchlist | Step 0 of /today |
| WebSearch | ✅ | 内置浏览器搜索 | 直接进入研究 |

详见 `00-system/connectors.md`

---
### 六点五、Python 工具脚本

| 脚本 | 用途 | 前置条件 |
|------|------|---------|
| `scripts/fetch_market_data.py --watchlist` | 拉取股票池行情（多源兜底） | .env 配好 FMP_API_KEY 或 TUSHARE_TOKEN |
| `scripts/fetch_macro_data.py` | 拉取 VIX/SPY/QQQ/原油/黄金/BTC | FMP_API_KEY |
| `scripts/check_setup.py` | 环境诊断 | — |
| `scripts/sync_feishu_drive.py` | 飞书云盘同步 | ACTION=download |
| `scripts/sync_weread.py` | 微信读书笔记同步 | WEREAD_API_KEY |

详见 `config/.env.example` → 复制为 `config/.env` 配好 key。

---

## 七、行为规范

### 研究时
1. **先查 02-kb/** → 本地已有知识优先
2. 再调外部源
3. 写输出时：**事实与推测分开**，标注来源
4. 不确定的事实标记 `[待核实]`

### 操作后
1. 更新 `02-kb/index.md`（如有新条目）
2. 追加 `02-kb/log.md`（操作记录）
3. 更新 `active-context.md`（断点续传）

### 核心规则（不可违背）
1. 原始资料只读不改
2. 每个判断尽量指向来源（`[[双向链接]]`）
3. 更新完必须同步 index.md 和 log.md
4. 不确定的事实标记为 `[待核实]`
5. 不强行关联孤立节点
6. 没有人工验收的 Loop = 自动制造垃圾
