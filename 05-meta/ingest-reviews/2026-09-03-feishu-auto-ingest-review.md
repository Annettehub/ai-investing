# Feishu 自动入库评审：2026-09-03

## 结论

- 本次评审 raw 文件：5 个
- 建议进入 distill：4 个
- 仅保留 raw：1 个
- 新建来源卡片：0 个

本报告按 G/S/R 多维路由规则生成；每个路由至少需要两个主题信号。它只做预筛，不代表事实核验，也不自动更新假设 certainty。

## 建议进入 distill

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 来源卡 | 判断 |
|---|---:|---|---|---|---|---|---|
| `03-raw/feishu/2026-09-03 UBS研报 ASML中国业务与光刻追赶分析.md` | 2 | S2 | S2 | `02-kb/hypotheses/S-产业结构与价值捕获/S2.1-advanced-manufacturing-packaging-localization.md`<br>`02-kb/concepts/L2-芯片层（Chips）/技术路线/国产光刻机突围路线.md`<br>`02-kb/concepts/L2-芯片层（Chips）/供需周期与供应链/先进封装生态（CoWoS、2.5D、3D封装）.md` | 存储 | `未创建` | 主路由为 S2 先进制造、封装与国产替代；交叉命中：S2 先进制造、封装与国产替代，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-03 didier AI内存架构战争已经开始.md` | 19 | G2 | G2, G3, S1, S2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DDR5, DRAM, HBM, HBM4, Micron, NAND, QLC, SK Hynix, SSD, Samsung, 产能, 价格, 内存, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G3 推理需求与规模, S1 芯片与加速器竞争结构, S2 先进制造、封装与国产替代，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-03 didier 台湾Semicon内存发言Takeaway.md` | 16 | G2 | G2, G3, S1, S2 | `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md` | DRAM, HBM, Micron, NAND, SK Hynix, SSD, Samsung, 产能, 价格, 内存, 存储 | `未创建` | 主路由为 G2 存储成长与周期；交叉命中：G2 存储成长与周期, G3 推理需求与规模, S1 芯片与加速器竞争结构, S2 先进制造、封装与国产替代，建议进入 distill 人工复核。 |
| `03-raw/feishu/2026-09-03 吴梓豪 德邦科技华为散热投资分析.md` | 3 | R1 | R1 | `02-kb/hypotheses/R-业绩兑现/R1-upstream-ai-infrastructure-earnings.md` | 产能 | `未创建` | 主路由为 R1 上游业绩兑现；交叉命中：R1 上游业绩兑现，建议进入 distill 人工复核。 |

## 仅保留 raw

| raw 文件 | 分数 | 主路由 | 交叉路由 | 建议目标 | 命中项 | 判断 |
|---|---:|---|---|---|---|---|
| `03-raw/feishu/2026-09-03 简洁价值派 红杉Alfred Lin伟大就是微小优势.md` | 0 | 无 | 无 | 无 | 无 | 未命中 G/S/R 入库路由，保留在 raw。 |

## 当前入库门槛

- 先判断 G/S/R 主路由，再判断是否存在交叉证据。
- 是否改变主路由对应假设的判断方向或 certainty。
- 是否补强或反驳对应假设、概念框架或公司档案。
- 涉及多个路由时，分别记录证据，不把偶然关键词当作主题归类。
