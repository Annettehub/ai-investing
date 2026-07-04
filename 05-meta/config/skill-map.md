# skill-map — 能力映射索引

> 把「命令 → 能力 → 工具 → 输出」映射成一张索引，方便 AI 快速定位该调用的能力。

## 能力矩阵

| 命令 | 输入 | 调用能力 | 工具/连接器 | 输出 |
|------|------|---------|------------|------|
| /idea | 任意信号 | 信号分类、五层定位 | WebSearch, 人 | 信号记录 |
| /collect | 多源 | 数据采集、去重 | GitHub, 飞书, Gmail, 微信读书, WebSearch | 03-raw/ |
| /ingest | 原始文本/03-raw | 摘要、关联、结构化 | 人审 | 02-kb/sources/ |
| /research | 标的/概念 | 价值链、竞争格局、财务、假设城墙 | WebSearch, 人 | 04-output/research/ |
| /trade | 研究输出 | 认知层级、仓位映射、退出预演 | 人 | 决策建议 |
| /today | 假设+城墙 | 信号扫描、certainty% 更新 | WebSearch, 03-raw | 04-output/today/ |
| /weekly | 本周日报+新信号 | 模式发现、规则晋升候选 | 人 | 04-output/weekly/ |
| /update | 系统文件 | 孤岛检测、过时规则、上下文膨胀 | 人 | 系统体检报告 |

## 技能文件目录

| 技能 | 文件 | 说明 |
|------|------|------|
| 信息入库 | 05-meta/skills/ingest-skill.md | 原始资料→结构化摘要 |
| 假设跟踪 | 待创建 | 设假设→扫描→更新 certainty% |
| 规则晋升 | 待创建 | 模式发现→验证≥3次→晋升 rules.md |
| 系统体检 | 待创建 | 孤岛/过时/膨胀/僵尸检测 |

## 工具连接器速查

| 工具 | 当前状态 | 负责技能 |
|------|---------|---------|
| WorkBuddy | ✅ | 所有命令执行 |
| GitHub | ✅ | /collect, 自动化 |
| 飞书 | ✅ | /collect, /ingest |
| 微信读书 | ⚡ | /collect, /ingest |
| Gmail | 🔜 | /collect |
| 腾讯云 | ⚡ | 备份/计算 |
| IMA | ⚡ | 检索增强 |
| WebSearch | ✅ | /idea, /research, /today |
| Podwise | ✅ | 播客摘要 |
| ZsxqCrawler | ✅ | 知识星球采集 |
