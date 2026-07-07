# Annette投研系统 · AI投研系统 — Agent 入口协议

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

## 二、黄仁勋·AI五层蛋糕（投研透镜）

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
| `/research` | 深度研究 (Stage 3) | 8章模板(产业链→驱动因素→客户供应商→受益场景→竞争→机会风险→假设雷达→风险提示/待验证) + 顶部深度更新日志。首次入库或追加更新 |
| `/track` | **跟踪研究 (Stage 6)** | **持续闭环**：识别新信号 → 加载entity假设雷达 → 7维度逐层扫描 → 更新certainty% → 影响决策 |
| `/today` | 每日检查 | 全部活跃entity快速扫描 + 假设雷达刷新 + 城墙预警 + 跨层信号 |
| `/scan` | 全池扫描 | 持仓+观察标的异动检测 + 产业方向 + 宏观快照 |
| `/report` | 周度复盘 | 持仓周报 + 观察动态 + 产业信号 + 仓位诊断（周六自动） |
| `/trade` | 交易决策 | 认知→映射→矩阵→退出预演 |
| `/update` | 系统体检 | 每月清理孤岛/过时规则/假设僵尸 |

> ⚠️ **关键区分**: `/research`(Stage3) = 建档案(首次)； `/track`(Stage6) = 盯变化(持续)。7维度假设判断的主场在 `/track`。

调用方式：`执行 /today 命令`，或粘贴命令文件内容。

---

## 四、知识库三层结构

| 层 | 目录 | 内容 | 规则 |
|----|------|------|------|
| 原料层 | `02-kb/sources/` | 研报/纪要/新闻摘要 | 只读不删，保留原始出处 |
| 提炼层 | `02-kb/entities/` + `02-kb/concepts/` | 公司档案 + 概念 | 双向链接，来源可追溯 |
| 判断层 | `02-kb/hypotheses/` + `entities/*.md` | 假设 + 城墙 + **每个entity内置假设雷达** | 带certainty%，可证伪；**7维度扫描在Stage6 /track中执行** |

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

### 来源标注（必须遵守）

每条事实/数据/证据必须标注以下标签之一，绝不让推测伪装成事实：

| 标签 | 含义 | 示例 |
|------|------|------|
| `[本地]` | 来自本知识库 wiki/sources/ 已沉淀内容 | `[本地] wiki/概念/AI-Capex.md` |
| `[网页]` | 来自 websearch / URL 的公开信息 | `[网页] TSMC Q2 法说会` |
| `[数据]` | 来自数据库/API 的定量数据 | `[数据] FMP: NVDA Q2 rev` |
| `[知识星球]` | 来自知识星球的付费内容 | `[知识星球] 吴梓豪：xxx` |
| `[推测]` | 无法验证、基于推理的判断 | `[推测] ASIC份额推断，待验证` |
| `[待验证]` | 已提出但尚待查证的事实 | `[待验证] 需查财报确认` |

### 矛盾扫描（研究时必须执行）

读取新材料时，主动对比 wiki/existing 已有结论：
- 发现方向冲突 → 立即标注"⚠️矛盾: `{现有文件}` 认为 `{已有结论}`，新证据指向 `{新方向}`"
- 矛盾不一定是旧结论错，可能是情境差异
- 补盲点，不是证错；用矛盾驱动假设更新

### 研究时
1. **先查 02-kb/** → 本地已有知识优先
2. 再调外部源
3. 写输出时：**事实与推测分开**，标注来源
4. 不确定的事实标记 `[待验证]`
5. **矛盾扫描**：发现新材料与本地结论冲突 → 标注并追问

### 操作后
1. 更新 `02-kb/index.md`（如有新条目）
2. 追加 `02-kb/log.md`（操作记录）
3. 更新 `active-context.md`（断点续传）

### 核心规则（不可违背）
1. 原始资料只读不改
2. 每个判断尽量指向来源（`[[双向链接]]`）
3. 更新完必须同步 index.md 和 log.md
4. 不确定的事实标记为 `[待验证]`
5. 不强行关联孤立节点
6. 没有人工验收的 Loop = 自动制造垃圾
