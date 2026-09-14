# Feishu 自动入库评审：2026-09-14

## 结论

- 本次评审 raw 文件：7 个
- 建议进入 distill：6 个
- 仅保留 raw：1 个
- 新建来源卡片：0 个

本报告按 G/S/R 多维路由规则生成；每个路由至少需要两个主题信号。它只做预筛，不代表事实核验，也不自动更新假设 certainty。

## 建议进入 distill

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 来源卡 | 判断 |
|---|---:|---|---|---|---|---|---|
| `03-raw/feishu/2026-09-14 didier RSI比AI白领更早.md` | 0 | G3 | G3 | `02-kb/hypotheses/G-需求与周期/G3-inference-demand-scale.md` |  | `未创建` | 主路由为 G3 推理需求与规模；交叉命中：G3 推理需求与规模，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-14 didier AI股神杀回来了.md` | 12 | G2 | G2, G1, G3, R2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DRAM, HBM, LTA, SK Hynix, SSD, 价格, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G1 需求与资本开支, G3 推理需求与规模, R2 下游回报兑现，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-14 didier 四家AI巨头谈降速.md` | 3 | G1 | G1, G2, R2, S3 | `02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md` | 价格, 涨价 | `未创建` | 主路由为 G1 需求与资本开支；交叉命中：G1 需求与资本开支, G2 存储成长与周期, R2 下游回报兑现, S3 应用层价值捕获，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-14 didier Anthropic RUM算力交易.md` | 6 | G1 | G1, S1 | `02-kb/hypotheses/G-需求与周期/G1-ai-capex-and-capacity.md` | Blackwell, CAPEX, 产能 | `未创建` | 主路由为 G1 需求与资本开支；交叉命中：G1 需求与资本开支, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-14 didier 存储30%光通信4%.md` | 14 | G2 | G2, G1, S1, G3 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DRAM, HBM, LTA, NAND, SSD, 价格, 内存, 存储, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G1 需求与资本开支, S1 芯片与加速器竞争结构, G3 推理需求与规模，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-14 didier 光通信进入计算核心.md` | 11 | G2 | G2, R1, G1, S1 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | HBM, TSMC, 产能, 内存, 存储, 涨价 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, R1 上游业绩兑现, G1 需求与资本开支, S1 芯片与加速器竞争结构，建议进入 distill 人工复核。 |

## 仅保留 raw

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 判断 |
|---|---:|---|---|---|---|---|
| `03-raw/feishu/untitled.md` | 0 | 无 | 无 | 无 | 无 | 未命中 G/S/R 入库路由，保留在 raw。 |

## 当前入库门槛

- 先判断 G/S/R 主路由，再判断是否存在交叉证据。
- 是否改变主路由对应假设的判断方向或 certainty。
- 是否补强或反驳对应假设、概念框架或公司档案。
- 涉及多个路由时，分别记录证据，不把偶然关键词当作主题归类。
