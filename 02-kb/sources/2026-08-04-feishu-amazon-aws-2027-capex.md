---
title: "来源摘要：亚马逊专家 Q&A - 2027 AWS 数据中心与 CAPEX"
source_type: "feishu/raw-extraction"
source_path: "03-raw/feishu/2026-08-04 2030FY观点 亚马逊专家Q&A.md"
author: "2030FY 知识星球 / 亚马逊专家 Q&A"
published_at: "2026-08-04"
ingested_at: "2026-08-08"
confidence: "medium"
tags: ["G1", "G2", "S1", "AWS", "Amazon", "CAPEX", "Trainium", "NVIDIA", "storage", "data-center"]
---

# 来源摘要：亚马逊专家 Q&A - 2027 AWS 数据中心与 CAPEX

## 信源信息

| 字段 | 内容 |
|---|---|
| 来源平台 | Feishu |
| 原始资料 | `03-raw/feishu/2026-08-04 2030FY观点 亚马逊专家Q&A.md` |
| 作者/机构 | 2030FY 知识星球 / 亚马逊专家 Q&A |
| 原始发布日期 | 2026-08-04 |
| 入库日期 | 2026-08-08 |
| 入库方式 | Feishu raw 同步后人工确认入库 |
| 外部核验 | 未做外部事实核验 |
| 置信度 | 中；适合作为 G1/G2/S1 的专家访谈增量证据，具体 GW、GPU 数量和 CAPEX 口径需用 AWS/亚马逊财报或第三方产业数据交叉验证 |

## 一句话结论

这篇资料强化了 G1 的核心判断：2027 年 AI 数据中心上线容量仍大，但 AWS 的 CAPEX 不能简单按 NVIDIA Rubin 单 GW 成本外推；Trainium、自研芯片、长期存储协议、租赁容量和数据中心可用性会改变资金流向和硬件价值分配。

## 核心观点

1. **2027 年 AWS 规划上线容量约 7GW**
   - 自建容量规划从此前超过 6GW 下调至约 5GW。
   - 另有租赁容量约 1.8-2GW。
   - 资料强调该口径是 2027 年能够通电并产生经济效益的容量，而不是单纯开工容量。

2. **Trainium 改变单 GW CAPEX 口径**
   - 如果按 NVIDIA GPU 测算，市场可能高估单 GW 支出。
   - AWS 自研 Trainium 方案的单 GW 硬件支出可能显著低于 Rubin/NVIDIA 方案。
   - 资料给出的简化口径是：单 GW 总硬件投资不超过约 300 亿元人民币，其中约 150 亿元 Trainium 卡，约 150 亿元存储价值。

3. **存储价值量仍是重要变量，但 AWS 通过 LTA 控制价格上限**
   - Rubin 架构下单 GW 存储价值量可能接近 250 亿元人民币。
   - Trainium 方案的单 GW 存储价值量约 150 亿元人民币。
   - AWS 的 DRAM 采购已通过长期协议控制价格上限，价格不是永久固定，但不会超过协议上限。

4. **AWS 2027 采购结构中 Trainium 权重高于 NVIDIA**
   - 资料称 2027 年 AWS 计划采购约 100 万张 NVIDIA GPU，最多一半为 Rubin，另一半仍为 Blackwell。
   - Trainium 采购量接近 300 多万片，和 NVIDIA GPU 数量比例约 3.5:1。
   - 折算功耗后，Rubin 在 7GW 增量容量中的占比约 1-2GW。

5. **AI 算力消耗与收入贡献不完全匹配**
   - AI 工作负载可能消耗超过 60% 的算力资源，但收入贡献尚未达到总收入的 50%。
   - 传统云业务仍贡献超过一半收入。
   - Bedrock 向企业销售模型 API 的抽成模式增长快、利润率更高，资料称抽成接近 50%。

6. **2027 年瓶颈可能从芯片转向数据中心可用性**
   - 2026 年核心瓶颈是芯片供应，尤其 Trainium 供应紧。
   - 2027 年如果芯片供应通过长协和预付款基本锁定，主要瓶颈将变成数据中心、电力、土地和土建可用性。
   - 北美自建数据中心规划仍可能在 2027 年 1 月后继续下修。

## 可入库信息

| 入库位置 | 信息 | 用途 |
|---|---|---|
| `02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md` | 2027 AWS 约 7GW 上线容量、Trainium 降低单 GW 成本、2027 瓶颈从芯片转向数据中心可用性 | 更新 G1 的 CAPEX 拆解与产能验证 |
| `02-kb/hypotheses/S-产业结构与价值捕获/S1.1-chip-accelerator-competition.md` | Trainium 与 NVIDIA GPU 数量比例约 3.5:1，Rubin 在功耗口径中的占比约 1-2GW | 更新 GPU vs ASIC/自研芯片竞争结构 |
| `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | Trainium/Rubin 单 GW 存储价值量差异、DRAM LTA 价格上限 | 更新存储需求与 LTA 价格边界 |
| `02-kb/entities/AMZN-Amazon-AWS.md` | AWS AI CAPEX、Trainium、Bedrock、Anthropic/OpenAI 资源分配 | 新增 AWS/Amazon 实体跟踪 |
| `02-kb/concepts/L4-模型层（Models）/供需周期与供应链/云厂商算力采购节奏（英伟达、自研ASIC、第三方云）.md` | CSP 采购结构从 NVIDIA GPU 拆分到 Trainium、自研芯片、租赁容量和传统云 | 补充云厂商算力采购框架 |

## 需要跟踪的指标

1. AWS 2027 实际上线 GW 与规划 7GW 的差异。
2. Trainium 与 NVIDIA GPU 的真实采购数量、功耗折算和集群利用率。
3. AWS AI 工作负载算力消耗占比与 AI 收入占比是否持续错配。
4. Bedrock 模型 API 平台收入、抽成和毛利变化。
5. DRAM/存储 LTA 的价格上限、重谈机制和客户覆盖范围。

## 置信度说明

- 专家访谈适合给出 AWS 内部规划、采购结构和瓶颈变化的方向性线索。
- 具体 GW、Trainium 数量、NVIDIA GPU 数量和单 GW 成本仍需亚马逊财报、供应链数据、IDC 建设进度和第三方产业数据库交叉验证。
