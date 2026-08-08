# AMZN / AWS — Amazon 云与 AI 基础设施实体档案

> 创建日期: 2026-08-08 | 状态: 📗 待跟踪
> 首次入库来源: `02-kb/sources/2026-08-04-feishu-amazon-aws-2027-capex.md`

---

## 基本信息

| 项目 | 内容 |
|---|---|
| 全称 | Amazon.com, Inc. / Amazon Web Services |
| 股票代码 | AMZN |
| 业务位置 | 全球 CSP、AI 云、Trainium 自研芯片、Bedrock 模型 API 平台 |
| AI 角色 | AI CAPEX 需求方、自研 ASIC 使用方、模型公司算力承接方 |

## 当前核心判断

AWS 不是单纯的 NVIDIA GPU 采购方，而是一个同时使用自研 Trainium、NVIDIA GPU、租赁容量、传统云 capacity 和 Bedrock 模型平台的复合型 AI 基础设施运营商。

本实体的跟踪重点是：AWS headline CAPEX 到底流向 NVIDIA、Trainium、存储、数据中心土建、电力、租赁容量和 Bedrock 平台收入的哪一部分。

## 2026-08-08 更新 #1

- **触发**: 2030FY 亚马逊专家 Q&A 入库。
- **核心观点**:
  - 2027 年 AWS 规划可通电并产生经济效益的新增容量约 7GW，其中自建约 5GW，租赁约 1.8-2GW。
  - Trainium 会显著改变单 GW CAPEX 口径，不能用 NVIDIA Rubin 单 GW 成本机械外推 AWS CAPEX。
  - 资料称 AWS 2027 年计划采购约 100 万张 NVIDIA GPU，同时 Trainium 采购接近 300 多万片，数量比例约 3.5:1。
  - AI 可能消耗超过 60% 的算力资源，但收入贡献尚未达到总收入 50%，传统云仍贡献超过一半收入。
  - 2027 年瓶颈可能从芯片供应转向数据中心、电力、土地和土建可用性。
- **影响维度**: G1 / G2 / S1 / R2。
- **来源标签**: `02-kb/sources/2026-08-04-feishu-amazon-aws-2027-capex.md`
- **置信度**: 中；专家口径，需财报和供应链数据验证。

## GSR 映射

| 层级 | 卡片编号 | 相关命题 | 本实体角色 | 关键跟踪项 |
|---|---|---|---|---|
| G | G1 | AI CAPEX 与算力供给周期 | 全球 AI CAPEX 需求方 | 自建/租赁 GW、CAPEX、上线容量 |
| G | G2 | 存储成长与周期分层 | 大型存储采购方 | DRAM LTA、Trainium/Rubin 单 GW 存储价值 |
| S | S1 | 芯片与加速器竞争结构 | 自研 Trainium 对 NVIDIA 的替代样本 | Trainium 与 NVIDIA GPU 采购比例、利用率 |
| R | R2 | 下游兑现 | Bedrock/AI 云平台商业化样本 | AI 算力消耗占比、AI 收入占比、Bedrock 抽成 |

## 待验证项

- [ ] 2027 年 7GW 上线容量是否实现。
- [ ] Trainium 与 NVIDIA GPU 实际采购数量、功耗折算和利用率。
- [ ] Bedrock 收入、抽成、毛利和客户增长。
- [ ] AI 工作负载算力消耗占比与收入贡献是否继续错配。
- [ ] 北美数据中心规划是否继续下修，是否通过海外、租赁或 power share 补足。
