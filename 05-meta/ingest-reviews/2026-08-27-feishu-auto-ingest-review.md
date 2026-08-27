# Feishu 自动入库评审：2026-08-27

## 结论

- 本次评审 raw 文件：15 个
- 建议进入 distill：14 个
- 仅保留 raw：1 个
- 新建来源卡片：0 个

本报告按 G/S/R 多维路由规则生成；每个路由至少需要两个主题信号。它只做预筛，不代表事实核验，也不自动更新假设 certainty。

## 建议进入 distill

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 来源卡 | 判断 |
|---|---:|---|---|---|---|---|---|
| `03-raw/feishu/Dylan Patel 观点推理链条.md` | 11 | G2 | G2, G1, G3, R2, S2, S3 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CAPEX, HBM, TSMC, 产能, 价格, 内存, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G1 需求与资本开支, G3 推理需求与规模, R2 下游回报兑现, S2 先进制造、封装与国产替代, S3 应用层价值捕获，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-27 didier 英伟达把2027年悬崖推走（卡片版）.md` | 18 | G2 | G2, S1, G1, G3, R1, R2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | Blackwell, CAPEX, DRAM, HBM, HBM4, LTA, Micron, SK Hynix, Samsung, TSMC, 产能, 价格, 内存, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, S1 芯片与加速器竞争结构, G1 需求与资本开支, G3 推理需求与规模, R1 上游业绩兑现, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-27 国泰海通海外科技团队 英伟达FY27Q2业绩会.md` | 12 | S1 | S1, G2, R1, G3, G1 | `02-kb/hypotheses/S-产业结构与价值捕获/S1.1-chip-accelerator-competition.md` | Blackwell, DRAM, LTA, Samsung, 产能, 价格, 存储 | `未创建` | 主路由为 S1 芯片与加速器竞争结构；交叉命中：S1 芯片与加速器竞争结构, G2 存储成长与周期, R1 上游业绩兑现, G3 推理需求与规模, G1 需求与资本开支，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-27 价值实验笔记 老铺黄金反面观点 好公司vs好投资.md` | 2 | R1 | R1 | `02-kb/hypotheses/R-业绩兑现/R1-upstream-ai-infrastructure-earnings.md` | 价格 | `未创建` | 主路由为 R1 上游业绩兑现；交叉命中：R1 上游业绩兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-25 Ben Thompson访谈 九大科技公司正反观点知识卡片.md` | 2 | S1 | S1, S3, G1, G3, R1, R2 | `02-kb/hypotheses/S-产业结构与价值捕获/S1.1-chip-accelerator-competition.md` | 价格 | `未创建` | 主路由为 S1 芯片与加速器竞争结构；交叉命中：S1 芯片与加速器竞争结构, S3 应用层价值捕获, G1 需求与资本开支, G3 推理需求与规模, R1 上游业绩兑现, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-27 Dario Amodei 技术的青春期.md` | 4 | G2 | G2, G3 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | LTA, 价格 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G3 推理需求与规模，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-27 Waterzzz 老铺黄金26H1分析师纪要.md` | 2 | R1 | R1, S3 | `02-kb/hypotheses/R-业绩兑现/R1-upstream-ai-infrastructure-earnings.md` | 价格 | `未创建` | 主路由为 R1 上游业绩兑现；交叉命中：R1 上游业绩兑现, S3 应用层价值捕获，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-27 老铺黄金中期业绩说明会纪要.md` | 2 | R1 | R1 | `02-kb/hypotheses/R-业绩兑现/R1-upstream-ai-infrastructure-earnings.md` | 价格 | `未创建` | 主路由为 R1 上游业绩兑现；交叉命中：R1 上游业绩兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-27 FAU_2030 Databricks专家观察与开源趋势.md` | 6 | G3 | G3, G2, R2 | `02-kb/hypotheses/G-需求与周期/G3-inference-demand-scale.md` | LTA, 价格, 存储 | `未创建` | 主路由为 G3 推理需求与规模；交叉命中：G3 推理需求与规模, G2 存储成长与周期, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-26 ZeroHedge 黄金期货创纪录与后市展望.md` | 4 | G2 | G2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | LTA, 价格 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-26 半导体大佬 小米玄戒芯片深度分析.md` | 18 | G2 | G2, S1, G3, G1, R2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CoWoS, DDR5, DRAM, HBM, HBM3E, HBM4, SK Hynix, Samsung, TSMC, 产能, 价格, 内存, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, S1 芯片与加速器竞争结构, G3 推理需求与规模, G1 需求与资本开支, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-26 J.P.md` | 15 | G2 | G2, G3, S1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CAPEX, CoWoS, DRAM, HBM, LTA, NAND, SK Hynix, SSD, Samsung, 内存 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G3 推理需求与规模, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-26 投资笔记 老铺黄金投资逻辑.md` | 3 | G2 | G2, R1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | 价格, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, R1 上游业绩兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-26 2030FY Hot Chips核心要点.md` | 12 | G2 | G2, S1, G3 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DDR5, DRAM, HBM, HBM3E, Samsung, 内存, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, S1 芯片与加速器竞争结构, G3 推理需求与规模，建议进入 distill 人工复核。 |

## 仅保留 raw

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 判断 |
|---|---:|---|---|---|---|---|
| `03-raw/feishu/2026-08-27 PatrickBoyle Leopold基金崩盘复盘.md` | 4 | 无 | 无 | 无 | SK Hynix, Samsung | 未命中 G/S/R 入库路由，保留在 raw。 |

## 当前入库门槛

- 先判断 G/S/R 主路由，再判断是否存在交叉证据。
- 是否改变主路由对应假设的判断方向或 certainty。
- 是否补强或反驳对应假设、概念框架或公司档案。
- 涉及多个路由时，分别记录证据，不把偶然关键词当作主题归类。
