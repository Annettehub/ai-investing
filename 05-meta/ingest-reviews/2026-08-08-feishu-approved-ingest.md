# 2026-08-08 Feishu approved ingest

本文件记录 2026-08-08 用户确认后的正式入库动作。边界：已做 review，用户确认“按照建议和优先级入库”后，才写入 `02-kb`。

## 入库清单

| 来源卡 | 主路由 | 处理 |
|---|---|---|
| `02-kb/sources/2026-08-03-feishu-sk-hynix-memory-expert.md` | G2 | 已作为本批次高优先级资料，补充 G2、SK Hynix 与存储概念 |
| `02-kb/sources/2026-08-03-feishu-bytedance-tencent-workbuddy-r2.md` | R2 / S3 | 已作为本批次高优先级资料，补充 R2、S3、腾讯与应用概念 |
| `02-kb/sources/2026-08-03-feishu-leopold-ai-volatility.md` | G1/G2 风险旁证 | 仅作为市场风险与周期旁证，不作为产业事实 |
| `02-kb/sources/2026-08-04-feishu-amazon-aws-2027-capex.md` | G1 / G2 / S1 | 新增来源卡与 AWS 实体 |
| `02-kb/sources/2026-08-06-feishu-microsoft-cloud-copilot.md` | G1 / R1 / R2 / S3 | 新增来源卡与 Microsoft 实体 |
| `02-kb/sources/2026-08-04-feishu-coherent-optical-module-qa.md` | S2 / R1 / G1 | 新增来源卡与 Coherent 实体 |
| `02-kb/sources/2026-08-05-feishu-agi-economics-alex-imas-phil-trammell.md` | S3 / R2 / concept | 新增来源卡，不新增公司实体 |
| `02-kb/sources/2026-08-02-feishu-ai-math-science-astra-grant.md` | G3 / L4 concept | 合并 Grant/Astra/Symborg 相关资料为一张来源卡，不新增公司实体 |

## 人工边界

- 未把所有 `03-raw` 自动写入知识库。
- 未创建 OpenAI、Anthropic、Nebius、Lumentum 等实体；这些暂作为来源卡或概念中的关联对象。
- 未更新网页部署；本次仅更新 GitHub 知识库内容。

## 实际写入层级

| 层级 | 写入内容 |
|---|---|
| 来源层 | 新增/保留 8 张 Feishu 来源卡，并更新 `02-kb/sources/_index.md` |
| 实体层 | 新增 AWS、Microsoft、Coherent；更新 SK Hynix、腾讯、NVIDIA、中际旭创、字节跳动 |
| 假设层 | 更新 G1/G2/G3、S1/S2/S3、R1/R2 |
| 概念层 | 更新云厂商采购节奏、基础设施触发器、存储周期、应用商业模式、应用渗透率、模型架构演进、技术-金融-投资交叉框架 |

## 后续待核验

1. AWS 2027 约 7GW、Trainium/NVIDIA GPU 采购比例、单 GW 存储价值量。
2. Microsoft Copilot 实际 revenue、AI token 用量、Nebius 容量上线。
3. Coherent NPO 2027 需求口径冲突、200G EML 价格和 Lumentum 产能。
4. WorkBuddy “百万级付费用户”、豆包成本打平和 C 端 AI 付费场景。
