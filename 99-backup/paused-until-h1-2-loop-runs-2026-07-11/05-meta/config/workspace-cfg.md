# workspace-cfg — 项目配置

> 本文件是项目级路由。任何 AI 进入 `ai-investing/` 目录后，先读 `00-system/SYSTEM.md`，再读本文件。

---

## 项目信息

| 字段 | 值 |
|------|-----|
| 项目名称 | Annette投研系统 · AI 投研系统 |
| 根目录 | `D:/WorkBuddy/Claw/ai-investing/` |
| 工作模式 | Markdown 文件协议，零代码优先 |
| 核心标的 | 00981 中芯国际（当前） |
| 投资框架 | AI 五层蛋糕（L2-L5） |

## 目录结构

```
ai-investing/
├── 00-system/          # 系统协议：SYSTEM.md, connectors.md, false-beliefs.md
├── 01-commands/        # 快捷命令：idea, ingest, research, trade, today, weekly, collect, update
├── 02-kb/              # 知识库：entities, concepts, sources, hypotheses, walls, rules, index, log
├── 03-raw/             # 原料层：feishu, gmail, podwise, wechat, weread, zsxq
├── 04-output/          # 输出层：today, weekly, research
├── 05-meta/            # 元系统：config, skills, commands, maintenance, evolution
└── scripts/            # 可复用脚本
```

## 必读顺序

1. `00-system/SYSTEM.md` — 核心理念、原则、框架
2. `00-system/connectors.md` — 多源信息管道状态
3. `workspace-cfg.md` — 本文件
4. `02-kb/index.md` — 知识库总索引
5. `active-context.md` — 断点续传

## 命令速查

| 命令 | 用途 | 对应文件 |
|------|------|---------|
| /idea | 信号收集 | 01-commands/idea.md |
| /collect | 多源采集 | 01-commands/collect.md |
| /ingest | 信息入库 | 01-commands/ingest.md |
| /research | 深度研究 | 01-commands/research.md |
| /trade | 决策 | 01-commands/trade.md |
| /today | 每日跟踪 | 01-commands/today.md |
| /weekly | 周度复盘 | 01-commands/weekly.md |
| /update | 系统体检 | 01-commands/update.md |

## 三闭环入口

| 闭环 | 触发命令 | 核心文件 |
|------|---------|---------|
| 假设验证 | /today + /weekly | 02-kb/hypotheses/ + 02-kb/walls/ |
| 知识沉淀 | /ingest | 03-raw/ → 02-kb/sources/ → entities/concepts |
| 规则晋升 | /weekly | 02-kb/rules.md + 00-system/false-beliefs.md |

## 工具链映射

| 工具 | 用途 | 接入状态 | 配置文件/路径 |
|------|------|---------|--------------|
| WorkBuddy | 主 harness，执行所有命令 | ✅ | 本目录 |
| GitHub | 代码/趋势/Actions 自动化 | ✅ | .github/workflows/ |
| 飞书 | 文档/会议纪要同步 | ✅ 已连接 | 03-raw/feishu/ |
| 微信读书 | 读书笔记导出 | ⚡ 配置中 | 03-raw/weread/ |
| Gmail | 行业邮件/研报 | 🔜 待配置 | 03-raw/gmail/ |
| 腾讯云 | 数据存储/备份/计算 | ⚡ 配置中 | 05-meta/config/cloud.md |
| IMA | 知识库问答/检索增强 | ⚡ 配置中 | 05-meta/config/ima.md |
| WebSearch | 实时搜索 | ✅ | 内置 |
| Podwise | 播客摘要 | ✅ | tools/podwise.exe |
| ZsxqCrawler | 知识星球爬虫 | ✅ | D:/Users/.../ZsxqCrawler/ |
