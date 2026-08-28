# Feishu 自动入库评审：2026-08-28

## 结论

- 本次评审 raw 文件：4 个
- 建议进入 distill：4 个
- 仅保留 raw：0 个
- 新建来源卡片：0 个

本报告按 G/S/R 多维路由规则生成；每个路由至少需要两个主题信号。它只做预筛，不代表事实核验，也不自动更新假设 certainty。

## 建议进入 distill

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 来源卡 | 判断 |
|---|---:|---|---|---|---|---|---|
| `03-raw/feishu/2026-08-28 洛克菲勒家族办公室 AI就业与资本开支周期.md` | 5 | G1 | G1, R1, G2, S1, S3 | `02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md` | 产能, 价格 | `未创建` | 主路由为 G1 需求与资本开支；交叉命中：G1 需求与资本开支, R1 上游业绩兑现, G2 存储成长与周期, S1 芯片与加速器竞争结构, S3 应用层价值捕获，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-28 吴梓豪leslie 国内先进封装扩产高估.md` | 17 | G2 | G2, R1, S2, S1, R2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CoWoS, DRAM, HBM, HBM3E, HBM4, Micron, SK Hynix, Samsung, TSMC, 产能, 存储, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, R1 上游业绩兑现, S2 先进制造、封装与国产替代, S1 芯片与加速器竞争结构, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-28 didier 推理现金流喂大下一代模型.md` | 18 | G2 | G2, S1, G1, G3, R1, R2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DRAM, HBM, HBM4, Micron, NAND, SK Hynix, SSD, Samsung, 产能, 价格, 内存, 存储, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, S1 芯片与加速器竞争结构, G1 需求与资本开支, G3 推理需求与规模, R1 上游业绩兑现, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-08-27 Dylan Patel 观点推理链条.md` | 11 | G2 | G2, G1, G3, R2, S2, S3 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | CAPEX, HBM, TSMC, 产能, 价格, 内存, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G1 需求与资本开支, G3 推理需求与规模, R2 下游回报兑现, S2 先进制造、封装与国产替代, S3 应用层价值捕获，建议进入 distill 人工复核。 |

## 仅保留 raw

无。

## 当前入库门槛

- 先判断 G/S/R 主路由，再判断是否存在交叉证据。
- 是否改变主路由对应假设的判断方向或 certainty。
- 是否补强或反驳对应假设、概念框架或公司档案。
- 涉及多个路由时，分别记录证据，不把偶然关键词当作主题归类。
