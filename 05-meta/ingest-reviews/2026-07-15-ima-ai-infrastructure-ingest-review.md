---
title: "IMA AI 基础设施资料入库审阅单"
date: "2026-07-15"
raw_commit: "bb0b44c"
ingest_commit: "4e4ab80"
status: "retrospective-review"
---

# IMA AI 基础设施资料入库审阅单

> 这是对 2026-07-15 IMA 批次的回溯审阅单。  
> 本文件用于说明“这次本应先给用户确认的入库内容”。不改变已经写入知识库的内容。

## 一、本批次 raw 判重

本次 GitHub 新增 raw 文件 6 个，但存在 2 组重复，实际唯一资料 4 篇。

| raw 文件 | 判定 | 处理 |
|---|---|---|
| `03-raw/wechat/20260624-NOTE-2026-06-24-Sequoia Capital-记忆与持续学习.md` | 与下方文件重复 | 不单独沉淀，作为重复路径记录 |
| `03-raw/wechat/20260624-NOTE-2026-06-24-Sequoia-记忆与持续学习.md` | 唯一资料 | 入库为 Engram 记忆与持续学习 |
| `03-raw/wechat/20260630-NOTE-2026-06-30-Sequoia-DylanPatel.md` | 唯一资料 | 入库为 Dylan Patel 软硬件协同设计 |
| `03-raw/wechat/20260712-NOTE-2026-07-12-Lenny-Podcast.md` | 唯一资料 | 入库为 AI 工作情绪调查 |
| `03-raw/wechat/20260715-NOTE-2026-07-15 The a16z Show 还有谁能追.md` | 与下方文件重复 | 不单独沉淀，作为重复路径记录 |
| `03-raw/wechat/20260715-NOTE-2026-07-15-Thea16zShow.md` | 唯一资料 | 入库为 a16z / 谁能追上 NVIDIA |

## 二、入库价值判断

| 资料 | 价值评级 | 入库理由 | 需要注意的边界 |
|---|---|---|---|
| Sequoia / Engram 记忆与持续学习 | A- | 补充企业 AI 的“记忆层、持续学习、RAG 局限、token 成本”线索 | 播客观点，具体 token 节省幅度需要客户案例验证 |
| Sequoia / Dylan Patel 软硬件协同设计 | A | 补充软硬件协同、NeoCloud、revenue per GW、推理供给和数据中心运营变量 | Dylan Patel 观点质量较高，但仍需公司财报和产业数据交叉验证 |
| Lenny Podcast 2026 AI 工作情绪调查 | B+ | 补充应用层 ROI 的组织摩擦：倦怠、经理能力、认知衰退、同薪酬更高产出预期 | 调查样本代表性需要看原报告，不直接作为行业总体结论 |
| a16z / 谁能追上 NVIDIA | A- | 补充 NVIDIA 系统级护城河、自研 ASIC 威胁、物理基础设施瓶颈、router 商业模式 | 其中对 GPT-5、公司执行和政策影响的判断应作为线索，不直接当作事实 |

## 三、拟写入知识库的位置

| 资料 | Source 摘要 | G 层 | S 层 | R 层 | Concept | Entity |
|---|---|---|---|---|---|---|
| Engram 记忆与持续学习 | `02-kb/sources/2026-07-15-ima-sequoia-engram-memory.md` | G3 | S3 | R2 | L4 模型架构；L5 应用商业模式 | 暂不新增实体 |
| Dylan Patel 软硬件协同设计 | `02-kb/sources/2026-07-15-ima-sequoia-dylanpatel-codesign.md` | G1 | S1、S2 | R1 | L3 基础设施；L4 云厂商算力采购 | NVIDIA |
| Lenny AI 工作情绪调查 | `02-kb/sources/2026-07-15-ima-lenny-ai-workforce-sentiment.md` | G3 | 暂不进入 S | R2 | L5 AI 渗透率观察 | 暂不新增实体 |
| a16z NVIDIA 访谈 | `02-kb/sources/2026-07-15-ima-a16z-nvidia-infra-future.md` | G1 | S1、S3 | R1、R2 | L3、L4、L5 | NVIDIA |

## 四、实际写入内容摘要

### 1. Source 层

新增 4 个 source 摘要：

- `02-kb/sources/2026-07-15-ima-sequoia-engram-memory.md`
- `02-kb/sources/2026-07-15-ima-sequoia-dylanpatel-codesign.md`
- `02-kb/sources/2026-07-15-ima-lenny-ai-workforce-sentiment.md`
- `02-kb/sources/2026-07-15-ima-a16z-nvidia-infra-future.md`

每个 source 摘要都包含：

- 原始 raw 路径
- 一句话结论
- 可入库信息表
- 对 G/S/R 的影响
- 后续跟踪指标
- 置信度说明

### 2. IMA 来源索引

更新文件：

- `02-kb/sources/_index-ima.md`

新增内容：

- 记录 `bb0b44c` 批次
- 标注“6 个 raw 文件，2 组重复，实际 4 篇唯一资料”
- 给出每篇资料的价值评级和处理方式
- 列出本批次沉淀的 4 个 source 文件

### 3. G 层：需求与周期

更新文件：

- `02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md`
- `02-kb/hypotheses/G-需求与周期/G3-ai-adoption-and-industrial-demand.md`

写入内容：

| 文件 | 新增判断 |
|---|---|
| G1 | headline CAPEX 需要继续拆成“钱是否进入 AI 硬件、硬件是否完成上电/并网、算力是否以足够高的利用率和价格转成收入” |
| G1 | 增加 power smoothing、revenue per GW、NeoCloud 交付能力和物理基础设施瓶颈 |
| G3 | 企业 AI 需求可能从“更多通用模型调用”转向“组织记忆、持续学习和私有工作流内化” |
| G3 | AI 采用不能只看使用量和 token 消耗，还要看组织能否承接，尤其是倦怠、经理能力和认知衰退 |

### 4. S 层：产业结构与价值捕获

更新文件：

- `02-kb/hypotheses/S-产业结构与价值捕获/S1.1-chip-accelerator-competition.md`
- `02-kb/hypotheses/S-产业结构与价值捕获/S2.1-advanced-manufacturing-packaging-localization.md`
- `02-kb/hypotheses/S-产业结构与价值捕获/S3.1-application-value-capture.md`

写入内容：

| 文件 | 新增判断 |
|---|---|
| S1 | GPU vs ASIC 的问题不是“谁更快”，而是哪个系统能在模型变化、推理成本、供应链约束和客户负载变化中保持最低总成本和最高可交付性 |
| S1 | NVIDIA 护城河从单一 CUDA/芯片性能扩展为系统级护城河：网络、HBM、工艺节点、供应链、软件和交付 |
| S1 | Google TPU、Amazon Trainium、Meta MTIA 的威胁主要来自 captive customer 和内部规模化负载 |
| S2 | 先进制程、先进封装、HBM 之外，物理数据中心的上电、并网、冷却和网络组织能力也会影响硬件能否转化为真实收入 |
| S3 | 应用层价值捕获从“入口与执行”扩展为“入口、记忆、执行”三个节点 |
| S3 | router 是模型/应用层之间的成本和价值分配器，可用于免费用户变现和 agentic commerce |

### 5. R 层：业绩兑现

更新文件：

- `02-kb/hypotheses/R-业绩兑现/R1-upstream-ai-infrastructure-earnings.md`
- `02-kb/hypotheses/R-业绩兑现/R2-end-user-sustainable-roi.md`

写入内容：

| 文件 | 新增判断 |
|---|---|
| R1 | 上游兑现不能只看芯片出货，还要看数据中心是否完成上电、利用率、租赁价格和现金回收 |
| R1 | 增加“CAPEX 到可售算力”的验证门，防止把采购金额直接当作收入兑现 |
| R2 | 采用者 ROI 要拆成价值创造、价值捕获和扣除全成本后的净收益 |
| R2 | 组织记忆层可能是正向 ROI 路径；倦怠、cognitive rot 和同薪酬更高产出预期是负向约束 |
| R2 | router 和 agentic commerce 是应用变现线索，但需要实际收入、抽佣、留存和毛利验证 |

### 6. Concept 层

更新文件：

- `02-kb/concepts/L3-基础设施层（Infrastructure）/基础设施层触发器.md`
- `02-kb/concepts/L4-模型层（Models）/技术路线/模型架构演进（Transformer、MoE、推理优化、物理AI）.md`
- `02-kb/concepts/L4-模型层（Models）/供需周期与供应链/云厂商算力采购节奏（英伟达、自研ASIC、第三方云）.md`
- `02-kb/concepts/L5-应用层（Applications）/商业模式/AI应用商业模式与赛道（Agent、Copilot、机器人、自动驾驶、应用发展）.md`
- `02-kb/concepts/L5-应用层（Applications）/渗透率与周期/AI应用渗透率观察.md`

写入内容：

| Concept | 新增内容 |
|---|---|
| L3 基础设施触发器 | 新增“数据中心上电与 revenue per GW 分化”触发器 |
| L4 模型架构 | 新增记忆 vs RAG、adapter fine-tuning、router/thinking budget、软硬件协同 |
| L4 云厂商算力采购 | 新增 NVIDIA 系统、自研 ASIC、NeoCloud、海外/区域化算力四条采购路径 |
| L5 应用商业模式 | 新增企业记忆层、router、免费用户变现、agentic commerce |
| L5 AI 渗透率观察 | 新增组织摩擦、倦怠、经理能力、cognitive rot |

### 7. Entity 层

更新文件：

- `02-kb/entities/NVDA-NVIDIA.md`

写入内容：

- 将 NVIDIA 核心逻辑从“待补充”改为系统级护城河：
  - GPU
  - 网络
  - HBM
  - 先进制程
  - 系统软件
  - 供应链谈判
  - 交付节奏
- 增加两条跟踪线：
  1. 系统级护城河是否继续兑现
  2. 自研 ASIC 是否压缩利润池
- 事件日志增加两条 IMA 入库记录：
  - a16z / Dylan Patel: NVIDIA 系统级护城河与自研 ASIC 威胁
  - Sequoia / Dylan Patel: 软硬件协同、NeoCloud 与多极生态

## 五、哪些是来源观点，哪些是我的判断

| 内容 | 类型 | 说明 |
|---|---|---|
| NVIDIA 新进入者需要约 5x 性能优势 | 来源观点 | 来自 a16z/Dylan Patel 访谈，应作为产业观点跟踪 |
| 软硬件协同可能产生 100x 效率提升 | 来源观点 | 来自 Sequoia/Dylan Patel 访谈，应作为方向性判断，不直接当作财务测算 |
| 组织记忆可带来两个数量级 token 节省 | 来源观点 | 来自 Engram 访谈，需真实客户数据验证 |
| 倦怠超过 54%、高效经理约四分之一 | 来源观点 | 来自 Lenny 调查，需要看原调查样本 |
| G1 增加“CAPEX 到可售算力”验证门 | 我的结构化判断 | 基于 Dylan Patel 与 a16z 两篇资料对 G1 的归纳 |
| S3 从“入口与执行”扩展为“入口、记忆、执行” | 我的结构化判断 | 基于腾讯 Agent OS、Engram 和 a16z router 资料整合 |
| R2 拆成价值创造、价值捕获和扣除全成本后的净收益 | 我的结构化判断 | 基于当前 GSR 框架对应用层 ROI 的边界修正 |

## 六、后续需要你确认的问题

1. 是否同意把“企业记忆层 / 持续学习”作为 S3 应用层价值捕获的长期子议题？
2. 是否同意把 “revenue per GW / 数据中心上电 / GPU idle” 纳入 G1 与 R1 的长期指标？
3. 是否需要给 CoreWeave、Crusoe、Oracle、Google TPU、Amazon Trainium、Meta MTIA 建实体档案，还是暂时只放在 concept 和 hypothesis 中？
4. 是否需要把 “AI 工作情绪 / cognitive rot / 倦怠” 放进 R2 长期观察，还是只作为应用渗透率的辅助背景？

## 七、以后固定流程建议

以后每次 IMA / Feishu / ZSXQ / WeRead 入库，先生成本类审阅单，路径建议：

`05-meta/ingest-reviews/YYYY-MM-DD-source-topic-ingest-review.md`

用户确认后，再执行正式写入：

1. 新建或更新 source 摘要。
2. 更新 G/S/R 假设。
3. 更新 concept 或 entity。
4. 跑本地 build。
5. 给出“最终变更清单”。
6. 用户确认是否推送 GitHub。
