---
title: "来源摘要：GPU 可租用率与 B200 on-demand 供给"
source_type: "feishu/raw-extraction"
source_path: "03-raw/feishu/2026-07-22 GPU可需用情况 B200可租用率0%.md"
author: "Feishu 同步资料 / 3Fourteen Research 指标解读"
published_at: "2026-07-22"
ingested_at: "2026-07-22"
confidence: "中"
---

# 来源摘要：GPU 可租用率与 B200 on-demand 供给

## 信源信息

| 字段 | 内容 |
|---|---|
| 来源平台 | Feishu / raw-extraction |
| 原始资料 | `03-raw/feishu/2026-07-22 GPU可需用情况 B200可租用率0%.md` |
| 原始日期 | 2026-07-22 |
| 入库日期 | 2026-07-22 |
| 入库方式 | Feishu raw 同步后人工整理为 source card |
| 外部核验 | 未做外部事实核验 |
| 置信度 | 中：指标解释有价值，但原文中 `image.png` 未同步，图表需补原图或原始链接 |

## 一句话结论

GPU availability 指标衡量的是云平台 on-demand GPU 可租用性，不等于 GPU 是否“可用”或总供给是否为零。B200 可租用率 0% 更适合解读为新卡被长期客户、内部训练、预订订单和供给瓶颈锁定，而不是没有 B200 出货。

## 核心观点

1. **availability 是云端现货可租用率**
   - 100% 表示主流 A100/H100/GH200/B200 等实例都能在监测云平台中租到。
   - 0% 表示监测平台里 on-demand 资源售罄，不代表芯片不能运行或没有交付。

2. **B200 可租用率 0% 指向供需紧张**
   - 资料认为 B200 资源可能优先给长期大客户、自用训练、预订订单或新集群建设。
   - 这类信号支持 G1/G3：需求可能强于云端现货供给，但仍要与 CoWoS、HBM、机柜交付和上电节奏交叉验证。

3. **AI 应用公司的成本压力会上升**
   - 如果推理需求增长但现货 GPU 稀缺，应用公司会面对更高的推理成本和更差的弹性调度条件。
   - 这会影响 R2：最终采用者是否能在推理成本上升时仍获得可持续 ROI。

## 可入库信息

| 入库位置 | 信息 | 用途 |
|---|---|---|
| `hypotheses/G1` | on-demand GPU availability 可作为可上线算力紧张度指标 | 补充 CAPEX 到可用算力的验证路径 |
| `hypotheses/G3` | B200 现货紧缺支持推理/训练需求仍强，但需区分长期订单和现货 | 补充推理需求供给约束 |
| `concepts/L4 云厂商算力采购节奏` | 可租用率不等于总供给，要拆分自用、长约、现货、预订 | 优化云厂商采购与租赁框架 |

## 需要跟踪的指标

1. B200/H200/H100 在主要云平台的 on-demand、reserved、spot 价格和可用性。
2. CoreWeave、Crusoe、Lambda 等 NeoCloud 是否披露新卡上电进度。
3. CoWoS/HBM 供给改善后，B200 现货可租用率是否回升。
4. AI 应用公司是否提到推理成本、GPU 稀缺或云资源成本压力。
