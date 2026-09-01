# Feishu 自动入库评审：2026-09-01

## 结论

- 本次评审 raw 文件：27 个
- 建议进入 distill：26 个
- 仅保留 raw：1 个
- 新建来源卡片：0 个

本报告按 G/S/R 多维路由规则生成；每个路由至少需要两个主题信号。它只做预筛，不代表事实核验，也不自动更新假设 certainty。

## 建议进入 distill

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 来源卡 | 判断 |
|---|---:|---|---|---|---|---|---|
| `03-raw/feishu/2026-09-01 Gavin Baker播客 主持人与嘉宾观点推理链条.md` | 9 | G2 | G2, G1, G3, S1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DRAM, NAND, 产能, 价格, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G1 需求与资本开支, G3 推理需求与规模, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 苔藓花园 Gavin Baker AI需求跑赢算力供给.md` | 11 | G2 | G2, S1, G1, G3, S3, R1, R2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DRAM, NAND, TSMC, 产能, 价格, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, S1 芯片与加速器竞争结构, G1 需求与资本开支, G3 推理需求与规模, S3 应用层价值捕获, R1 上游业绩兑现, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 小盖fun 智谱财报电话会技术路线总结.md` | 3 | G3 | G3, G2 | `02-kb/hypotheses/G-需求与周期/G3-inference-demand-scale.md` | 价格, 涨价 | `未创建` | 主路由为 G3 推理需求与规模；交叉命中：G3 推理需求与规模, G2 存储成长与周期，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 The Information SpaceX自建涡轮叶片工厂.md` | 3 | G1 | G1 | `02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md` | 产能 | `未创建` | 主路由为 G1 需求与资本开支；交叉命中：G1 需求与资本开支，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 Alex Heath OpenAI今年可能实现AGI.md` | 3 | G2 | G2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | 价格, 内存 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 JPM_Asia_Tech_Outlook_2026_Analysis.md` | 21 | G2 | G2, G1, G3, S1, R1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CAPEX, CoWoS, DDR5, DRAM, HBM, HBM4, LTA, Micron, NAND, SK Hynix, SSD, Samsung, 产能, 价格, 内存, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G1 需求与资本开支, G3 推理需求与规模, S1 芯片与加速器竞争结构, R1 上游业绩兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 J.P.md` | 6 | G1 | G1, G3, R2, S3 | `02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md` | B200, CAPEX, 产能 | `未创建` | 主路由为 G1 需求与资本开支；交叉命中：G1 需求与资本开支, G3 推理需求与规模, R2 下游回报兑现, S3 应用层价值捕获，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 didier 英伟达35亿认购联发科CB分析.md` | 9 | S1 | S1, G2, R1, G1 | `02-kb/hypotheses/S-产业结构与价值捕获/S1.1-chip-accelerator-competition.md` | HBM, TSMC, 产能, 价格, 内存 | `未创建` | 主路由为 S1 芯片与加速器竞争结构；交叉命中：S1 芯片与加速器竞争结构, G2 存储成长与周期, R1 上游业绩兑现, G1 需求与资本开支，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 服务器调研Rubin产能与液冷CPO.md` | 14 | G2 | G2, R1, S1, G1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | B200, Blackwell, DDR5, HBM, HBM4, SK Hynix, Samsung, 产能, 价格, 内存 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, R1 上游业绩兑现, S1 芯片与加速器竞争结构, G1 需求与资本开支，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 Databricks专家观察开源倾斜.md` | 6 | G2 | G2, G3, R2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | LTA, 价格, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G3 推理需求与规模, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 HBF高带宽闪存讨论会纪要.md` | 13 | G2 | G2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DRAM, HBM, HBM3E, HBM4, NAND, SK Hynix, SSD, 内存 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 存储行业走向HBM降配分析.md` | 17 | G2 | G2, S1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DRAM, HBM, HBM4, NAND, SK Hynix, SSD, Samsung, 产能, 价格, 内存, 存储, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 HotChips网络五大专用架构.md` | 1 | S1 | S1 | `02-kb/hypotheses/S-产业结构与价值捕获/S1.1-chip-accelerator-competition.md` | 内存 | `未创建` | 主路由为 S1 芯片与加速器竞争结构；交叉命中：S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 美光北美专家纪要.md` | 16 | G2 | G2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DDR5, DRAM, HBM, HBM4, LTA, Micron, NAND, SK Hynix, SSD, Samsung, 产能 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 TrendForce 液冷渗透率2026达53%.md` | 0 | S1 | S1 | `02-kb/hypotheses/S-产业结构与价值捕获/S1.1-chip-accelerator-competition.md` |  | `未创建` | 主路由为 S1 芯片与加速器竞争结构；交叉命中：S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 2030FY CXMT High-k材料与DRAM变革.md` | 13 | G2 | G2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DDR5, DRAM, HBM, Micron, SK Hynix, Samsung, 内存, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 中国内存自立与NVHBM变革.md` | 16 | G2 | G2, R1, S1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DDR5, DRAM, HBM, HBM4, NAND, SK Hynix, SSD, Samsung, 产能, 价格, 内存 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, R1 上游业绩兑现, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 UBS 存储芯片需求预测图表.md` | 17 | G2 | G2, S1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | B200, HBM, HBM3E, HBM4, Micron, NAND, SK Hynix, SSD, Samsung, 产能, 价格, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 Meritz Research CCL涨价扩散研报.md` | 3 | G2 | G2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | 价格, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 Marvell业绩后小会纪要.md` | 3 | G2 | G2, R1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | 内存, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, R1 上游业绩兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 高盛 人形机器人半导体BOM.md` | 14 | G2 | G2, S1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DDR5, DRAM, HBM, Micron, NAND, SK Hynix, Samsung, 价格, 内存 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 投行研报 Hot Chips会议芯片总结.md` | 14 | G2 | G2, G3, S1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CoWoS, DDR5, DRAM, HBM, HBM3E, SSD, Samsung, TSMC, 内存 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G3 推理需求与规模, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 高盛 AI项目月度跟踪8月.md` | 8 | R1 | R1, S1, G1, G2, G3 | `02-kb/hypotheses/R-业绩兑现/R1-upstream-ai-infrastructure-earnings.md` | B200, Blackwell, 产能, 存储 | `未创建` | 主路由为 R1 上游业绩兑现；交叉命中：R1 上游业绩兑现, S1 芯片与加速器竞争结构, G1 需求与资本开支, G2 存储成长与周期, G3 推理需求与规模，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 台积电SEMICON中文总结.md` | 11 | G2 | G2, G1, G3 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CoWoS, HBM, HBM4, LTA, TSMC, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G1 需求与资本开支, G3 推理需求与规模，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 台积电SEMICON Taiwan研报.md` | 9 | G3 | G3, G1, G2, R2 | `02-kb/hypotheses/G-需求与周期/G3-inference-demand-scale.md` | CoWoS, HBM, HBM4, LTA, TSMC | `未创建` | 主路由为 G3 推理需求与规模；交叉命中：G3 推理需求与规模, G1 需求与资本开支, G2 存储成长与周期, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-01 FAU_2030 韩国8月芯片出口创新高.md` | 11 | G2 | G2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DRAM, HBM, NAND, 价格, 内存, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期，建议进入 distill 人工复核。 |

## 仅保留 raw

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 判断 |
|---|---:|---|---|---|---|---|
| `03-raw/feishu/2026-09-01 Franklin Templeton 债务格局正在发生变化.md` | 2 | 无 | 无 | 无 | 价格 | 未命中 G/S/R 入库路由，保留在 raw。 |

## 当前入库门槛

- 先判断 G/S/R 主路由，再判断是否存在交叉证据。
- 是否改变主路由对应假设的判断方向或 certainty。
- 是否补强或反驳对应假设、概念框架或公司档案。
- 涉及多个路由时，分别记录证据，不把偶然关键词当作主题归类。
