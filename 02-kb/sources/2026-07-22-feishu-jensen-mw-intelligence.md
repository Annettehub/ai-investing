---
title: "来源摘要：黄仁勋一兆瓦电生产多少智能"
source_type: "feishu/raw-extraction"
source_path: "03-raw/feishu/2026-07-22 黄仁勋观点：一兆瓦电，能生产多少智能.md"
author: "Feishu 同步资料 / Jensen Huang 观点解读"
published_at: "2026-07-22"
ingested_at: "2026-07-22"
confidence: "中高"
---

# 来源摘要：黄仁勋一兆瓦电生产多少智能

## 信源信息

| 字段 | 内容 |
|---|---|
| 来源平台 | Feishu / raw-extraction |
| 原始资料 | `03-raw/feishu/2026-07-22 黄仁勋观点：一兆瓦电，能生产多少智能.md` |
| 原始日期 | 2026-07-22 |
| 入库日期 | 2026-07-22 |
| 入库方式 | Feishu raw 同步后人工整理为 source card |
| 外部核验 | 未做外部事实核验 |
| 置信度 | 中高：作为 NVIDIA 叙事和效率指标框架有价值；具体 10x 数值需限定模型、吞吐和优化条件 |

## 一句话结论

这篇资料把 AI 基础设施的评价指标从“买了多少 GPU”推进到“每兆瓦能产出多少有效 token / 智能”。这对 L1 能源、L3 基础设施和 G3 推理需求都有价值，因为未来瓶颈可能从芯片单点性能转向系统级能源效率。

## 核心观点

1. **AI 工厂的单位产出指标可以写成 tokens per MW**
   - 资料以 DeepSeek R1 推理场景为例，比较 GB200 NVL72 与 Vera Rubin NVL72 的每兆瓦 token 产出。
   - 来源称在特定吞吐假设下，Rubin NVL72 的 TPS/MW 可能较 GB200 NVL72 提升约 10 倍。

2. **能源效率会影响 CAPEX 兑现质量**
   - 如果同样一兆瓦电能产生更多推理 token，云厂商的 revenue per MW、推理毛利和数据中心选址价值都会变化。
   - 这让 G1 的 CAPEX 验证必须加入“上电后产出效率”，而不是只看机柜交付。

3. **不能把 10x 泛化为所有工作负载**
   - 这个数字依赖具体模型、吞吐、batch、软件优化和硬件代际。
   - 更稳妥的入库方式是把它作为“每 MW 智能产出”指标框架，而不是单一确定性结论。

## 可入库信息

| 入库位置 | 信息 | 用途 |
|---|---|---|
| `concepts/L1 能源层触发器` | 增加 tokens per MW / intelligence per MW 作为能源效率触发器 | 判断电力瓶颈是否被系统效率改善缓解 |
| `concepts/L3 基础设施层触发器` | 增加 revenue per MW / tokens per MW 作为数据中心效率指标 | 连接上电、推理效率和收入兑现 |
| `hypotheses/G3` | 推理需求要同时看 token 总量和单位电力 token 产出 | 优化推理需求规模验证 |

## 需要跟踪的指标

1. NVIDIA、AMD、ASIC 厂商是否持续披露 tokens/MW、tokens/$ 或 inference throughput/watt。
2. 云厂商是否披露 revenue per MW、GPU utilization、推理毛利或单位推理成本。
3. 模型架构优化是否使推理 token 增长不再线性推高电力和机柜需求。
4. 电力受限地区是否优先采购高 tokens/MW 的新一代系统。
