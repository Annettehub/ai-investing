# Feishu 自动入库评审：2026-08-31

## 结论

- 本次评审 raw 文件：9 个
- 建议进入 distill：8 个
- 仅保留 raw：1 个
- 新建来源卡片：0 个

本报告按 G/S/R 多维路由规则生成；每个路由至少需要两个主题信号。它只做预筛，不代表事实核验，也不自动更新假设 certainty。

## 建议进入 distill

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 来源卡 | 判断 |
|---|---:|---|---|---|---|---|---|
| `03-raw/feishu/2026-08-31 电商头条 美团AI转型检讨.md` | 2 | G3 | G3, S3 | `02-kb/hypotheses/G-需求与周期/G3-inference-demand-scale.md` | 价格 | `未创建` | 主路由为 G3 推理需求与规模；交叉命中：G3 推理需求与规模, S3 应用层价值捕获，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-31 Baron Capital SpaceX公司分析.md` | 2 | G1 | G1, S3 | `02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md` | 价格 | `未创建` | 主路由为 G1 需求与资本开支；交叉命中：G1 需求与资本开支, S3 应用层价值捕获，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-31 The Diary Of A CEO Ed Zitron反AI泡沫访谈.md` | 4 | G1 | G1, R1, S1 | `02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md` | B200, CAPEX, 价格 | `未创建` | 主路由为 G1 需求与资本开支；交叉命中：G1 需求与资本开支, R1 上游业绩兑现, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-31 我有充足的时间 Moonshots英伟达AI循环经济.md` | 10 | S1 | S1, G2, G3, R2, S3, G1, R1 | `02-kb/hypotheses/S-产业结构与价值捕获/S1.1-chip-accelerator-competition.md` | B200, LTA, TSMC, 产能, 价格, 内存 | `未创建` | 主路由为 S1 芯片与加速器竞争结构；交叉命中：S1 芯片与加速器竞争结构, G2 存储成长与周期, G3 推理需求与规模, R2 下游回报兑现, S3 应用层价值捕获, G1 需求与资本开支, R1 上游业绩兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-31 我有充足的时间 英伟达Q2业绩电话会.md` | 13 | G2 | G2, S1, G1, R1, G3 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | Blackwell, CAPEX, DRAM, LTA, Samsung, 产能, 价格, 内存, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, S1 芯片与加速器竞争结构, G1 需求与资本开支, R1 上游业绩兑现, G3 推理需求与规模，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-31 方伟看十年 腾讯AI战略定位.md` | 3 | R1 | R1, G1, S3, G3 | `02-kb/hypotheses/R-业绩兑现/R1-upstream-ai-infrastructure-earnings.md` | CAPEX, 价格 | `未创建` | 主路由为 R1 上游业绩兑现；交叉命中：R1 上游业绩兑现, G1 需求与资本开支, S3 应用层价值捕获, G3 推理需求与规模，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-31 我有充足的时间 Dylan Patel算力集中化.md` | 15 | G2 | G2, G1, S1, S3, G3, R1, R2, S2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CAPEX, DRAM, HBM, Micron, SK Hynix, Samsung, TSMC, 产能, 价格, 内存, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G1 需求与资本开支, S1 芯片与加速器竞争结构, S3 应用层价值捕获, G3 推理需求与规模, R1 上游业绩兑现, R2 下游回报兑现, S2 先进制造、封装与国产替代，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-31 吴梓豪leslie 盛合晶微先进封装投资机会.md` | 17 | G2 | G2, R1, S2, S1, R2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CoWoS, DRAM, HBM, HBM3E, HBM4, Micron, SK Hynix, Samsung, TSMC, 产能, 存储, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, R1 上游业绩兑现, S2 先进制造、封装与国产替代, S1 芯片与加速器竞争结构, R2 下游回报兑现，建议进入 distill 人工复核。 |

## 仅保留 raw

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 判断 |
|---|---:|---|---|---|---|---|
| `03-raw/feishu/2026-08-31 Lenny's Podcast OpenAI产品负责人Tara访谈.md` | 0 | 无 | 无 | 无 | 无 | 未命中 G/S/R 入库路由，保留在 raw。 |

## 当前入库门槛

- 先判断 G/S/R 主路由，再判断是否存在交叉证据。
- 是否改变主路由对应假设的判断方向或 certainty。
- 是否补强或反驳对应假设、概念框架或公司档案。
- 涉及多个路由时，分别记录证据，不把偶然关键词当作主题归类。
