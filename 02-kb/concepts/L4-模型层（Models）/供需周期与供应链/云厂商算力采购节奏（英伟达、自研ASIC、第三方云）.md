# 云厂商算力采购节奏（英伟达、自研ASIC、第三方云）

> （待补充，内容后续增加）

## 2026-07-15 IMA 补充：GPU、自研 ASIC 与第三方云

| 采购路径 | 逻辑 | 观察指标 |
|---|---|---|
| NVIDIA 系统 | 仍受益于 GPU 通用性、网络、HBM、先进制程、供应链和软件生态 | 数据中心收入、NVL/Rubin 出货、毛利率、CoWoS/HBM 份额 |
| 自研 ASIC | Google/Amazon/Meta 等有 captive customer，可在稳定内部负载中压缩 NVIDIA 利润率 | TPU/Trainium/MTIA 内部份额、外部化销售、软件生态成熟度 |
| NeoCloud / 第三方云 | CoreWeave、Crusoe 等以 GPU 集群交付速度、长期合同和激励机制切入 | 租赁价格/MW、上电速度、客户集中度、融资成本 |
| 海外/区域化算力 | 电力、并网、合规和数据中心容量影响云厂商真实可用算力 | 海外数据中心合同、并网、利用率、监管变化 |

**核心判断**：云厂商采购节奏不能只看 CAPEX 金额。要区分芯片订单、机柜交付、数据中心上电、算力出租/自用、收入确认五个阶段。

**来源**：
- `02-kb/sources/2026-07-15-ima-sequoia-dylanpatel-codesign.md`
- `02-kb/sources/2026-07-15-ima-a16z-nvidia-infra-future.md`

## 2026-07-22 Feishu 补充：CAPEX 上修的三条拆解线

云厂商算力采购节奏不能只看“预算是否上修”，还要拆成：

| 拆解线 | 观察问题 | 对应信号 |
|---|---|---|
| 价格线 | HBM/DRAM、GPU、光模块、液冷、电源、PCB 等组件是否涨价 | CAPEX 上修但 GPU 数量不一定同比例增加 |
| 数量线 | 训练、推理、视频生成、Agent 等真实 token / workload 是否增长 | GPU、HBM、eSSD、网络和机柜需求同步增加 |
| 架构线 | 是否从普通 8 卡服务器升级到 NVL72、supernode、高密度液冷机柜 | 单机柜价格上升，系统集成和基础设施占比提高 |
| 可用线 | 新卡是否能在云端现货租到，还是被长约、自用和预订锁定 | on-demand GPU availability 低，说明现货紧缺但不等于总供给为零 |

**新增判断**：B200 可租用率 0% 应被理解为云端 on-demand 现货紧缺信号，而不是“B200 没有出货”。后续分析云厂商采购时，需要区分自用训练、长期客户、reserved/spot/on-demand、预订集群和第三方云租赁五种路径。

**来源**：
- `02-kb/sources/2026-07-22-feishu-bytedance-capex-revision.md`
- `02-kb/sources/2026-07-22-feishu-gpu-availability-b200.md`

## 2026-08-08 Feishu 补充：AWS/Microsoft 的采购节奏拆分

本批资料把云厂商算力采购进一步拆成“自建容量、租赁容量、自研芯片、NVIDIA GPU、传统云释放、AI token 使用和收入确认”几条线：

| 云厂商 | 新增观察 | 对框架的修正 |
|---|---|---|
| AWS | 2027 年上线容量口径约 7GW，其中自建约 5GW、租赁约 1.8-2GW；Trainium 采购量可能显著高于 NVIDIA GPU | 不能用 NVIDIA Rubin 单 GW 成本直接外推 AWS headline CAPEX，必须区分 Trainium、自研芯片、NVIDIA GPU 与存储价值量 |
| Microsoft | MaaS 收入高度依赖 OpenAI GPT API；传统云 DC capacity 释放、租赁会计和 Nebius 合作会影响 headline CAPEX 与真实算力供给 | CAPEX、RPO、token revenue、Copilot revenue 和云毛利率要分开看，不能用“买了 seat”替代“实际使用和收入确认” |

**新增判断**：云厂商 AI CAPEX 进入产业链的路径不止 GPU 一条。自研 ASIC 可能降低单位 GW 芯片成本，但不一定降低存储、网络、电力、数据中心和软件生态成本；因此 G1/S1/R1 需要联动验证。

**来源**：
- `02-kb/sources/2026-08-04-feishu-amazon-aws-2027-capex.md`
- `02-kb/sources/2026-08-06-feishu-microsoft-cloud-copilot.md`
