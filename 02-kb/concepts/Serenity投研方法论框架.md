---
title: Serenity 投研方法论框架
aliases:
  - Serenity Methodology
  - Serenity 投研框架
  - Serenity AI Supply Chain Framework
tags:
  - serenity
  - 投研方法论
  - AI基础设施
  - supply-chain
  - bottleneck
  - 半导体
created: 2026-06-26
updated: 2026-06-26
source_vault: Serenity_Twitter_Obsidian
source_pdf: aleabitoreddit_tweets(2).pdf
source_pdf_tweets: 4788
source_pdf_range_utc: 2025-07-02 to 2026-05-04
source_pdf_bucket_until_utc: 2026-05-05
---

# Serenity 投研方法论框架

> [!abstract] 一句话
> Serenity 的核心不是传统自下而上的单公司 DCF，而是通过 **信息综合 + 供应链映射 + 架构代际判断 + 证券结构审查**，提前发现尚未被机构充分定价的结构性机会，再选择最合适的公开市场表达方式。

这套方法论可以概括为：

**先看资本流向，再画供应链图；先找瓶颈，再找纯度最高的标的；先判断架构代际和证券结构，再决定是核心长仓、全球纯标的、篮子、事件交易、相对错价还是期权/波动率交易。**

> [!info] 全量推文校准
> 已用 `~/Downloads/aleabitoreddit_tweets(2).pdf` 对本框架做二次校准。该 PDF 导出 4788 条公开可检索 tweet，覆盖 2025-07-02 至 2026-05-04 UTC，桶查询区间到 2026-05-05。高频主题显示，上一版抓住了 AI supply chain 主轴，但低估了 **国际市场纯标的、证券结构、TAM/小市值错配、期权/波动率、相对错价** 在 Serenity 方法论中的权重。

全量推文中的主题频次校准：

| 主题 | 推文数 | 方法论含义 |
|---|---:|---|
| CPO / photonics / laser | 802 | 光互联和硅光是最核心的结构性主线 |
| Neocloud / GPU / datacenter | 761 | AI capex 不只买 GPU，还要看云算力融资和客户质量 |
| Valuation / market cap / TAM | 712 | 小市值和大 TAM 的错配是重估弹性来源 |
| Event / catalyst / ramp | 648 | volume ramp、qualification、listing、订单是主要催化 |
| International / IBKR / global | 514 | 很多最纯标的不在美股，需要全球市场搜索 |
| Financing / dilution / capital structure | 407 | 股东回报经常被债务、稀释、权证、锁定期吞掉 |
| Options / IV / LEAPS | 317 | 一部分收益来自波动率和期限结构错价 |

---

## 0. 与“琳半导体框架”的关系

琳的半导体投研框架偏向 **产业周期、供需、价格、产能、竞争格局、库存、资本开支**，适合判断一个半导体子行业是否进入上行周期，以及龙头公司是否具备周期弹性。

Serenity 的框架更像是在琳的框架上叠加了四层：

1. **AI 基础设施 capex funnel**：从 hyperscaler、neocloud、GPU、网络、光互联、电力、存储、封装逐层传导。
2. **供应链瓶颈地图**：不只看“需求好”，而是追问“哪个环节最卡、谁控制这个卡点、市场是否还没发现”。
3. **架构代际切换**：区分当前受益者、过渡代际受益者、下一代架构受益者，避免用旧周期线性外推。
4. **公开市场表达**：同一个瓶颈可能有美股纯标的、海外更纯标的、ETF、篮子、事件交易、或者只能观察不能买。

> [!tip] 兼容方式
> 琳的框架回答“这个环节有没有周期 beta 和盈利弹性”，Serenity 的框架回答“这个环节是否是未来 6-24 个月市场会重新定价的 alpha 卡点”。

---

## 1. 框架总览：F-A-B-E-S-R-P

Serenity 的投研流程可以压缩成七个字母：

| 层级 | 英文 | 中文 | 核心问题 |
|---|---|---|---|
| F | Funnel | 资本流漏斗 | AI capex 正在流向哪里？ |
| A | Architecture | 架构代际 | 当前技术路线处在哪一代？下一代卡点是什么？ |
| B | Bottleneck | 结构瓶颈 | 哪个环节最供不应求、最难扩产、最容易提价？ |
| E | Exposure | 标的表达 | 哪家公司或工具对这个瓶颈的暴露最纯？ |
| S | Security Structure | 证券结构 | 股东真实回报是否会被债务、稀释、权证、锁定期或低流通盘扭曲？ |
| R | Repricing | 重估催化 | 市场何时会发现？催化来自订单、财报、涨价还是机构建仓？ |
| P | Portfolio | 组合执行 | 用核心仓、篮子、barbell、事件仓还是 swing trade 表达？ |

---

## 1.1 Serenity 的四个策略栈

全量推文显示，Serenity 不是单一的“半导体瓶颈投资者”，而是把四套策略叠在一起使用。

| 策略栈 | 目标 | 典型研究动作 | 仓位表达 |
|---|---|---|---|
| 核心瓶颈长仓 | 找多年结构性供需错配 | AI capex -> 架构代际 -> 上游卡点 -> 纯标的 | Core long、basket |
| 全球纯标的挖掘 | 找美股之外更纯的供应链资产 | 韩国、台湾、日本、欧洲小盘供应商映射到美股需求 | 国际股票、ADR、观察清单 |
| 事件/证券结构交易 | 利用融资、锁定期、权证、稀释、上市、短空结构错价 | 看 cap table、debt、convert、ATM、float、short interest | Event trade、small position |
| 相对错价/波动率交易 | 找跨市场、跨标的、跨期限的反应滞后 | ETF、期权 IV、LEAPS、相关股 catch-up、时间差 | Options、swing、timezone arbitrage |

> [!warning] V1 框架的遗漏
> 上一版把 Serenity 主要抽象成“AI supply chain bottleneck alpha”。这对核心长仓是对的，但不够完整。全量推文里，她还反复使用证券结构、国际市场、期权波动率和相对错价来放大或过滤投资机会。

---

## 2. 第一层：Funnel，先看 AI 资本开支往哪里流

Serenity 的起点不是某个公司便宜，而是 AI 基础设施的资本开支正在形成哪条巨大传导链。

典型传导链：

```text
AI 需求
-> Hyperscaler / Neocloud capex
-> GPU / ASIC / TPU
-> HBM / DRAM / NAND / SSD
-> Networking / Optical transceivers / EML / CPO
-> Advanced packaging / Substrate / Foundry / Equipment
-> Power / Grid / Transformer / Cooling / Data center real estate
```

对应笔记：

| 方向 | 代表笔记 | Serenity 关注点 |
|---|---|---|
| 存储 | [[MU]], [[SNDK]] | AI 训练和推理拉动 HBM、DRAM、NAND、SSD 的结构性上行 |
| 光互联 | [[LITE]], [[COHR]], [[AAOI]], [[MRVL]] | 800G、1.6T、CPO、EML、DSP、硅光升级 |
| 上游材料 | [[AXTI]], [[SOI]] | InP、SOI、外延片、衬底是否成为真正瓶颈 |
| 云算力 | [[NBIS]], [[CRWV]], [[IREN]], [[CIFR]] | backlog、客户质量、融资结构、GPU 折旧和稀释 |
| 电力电网 | [[HPS]] | transformer、substation、conductor、capacitor bank、electrical steel |

> [!important] Serenity 不是只买“AI 主题”
> 她真正寻找的是 AI capex 漏斗里 **下一段会被迫补资本开支的节点**。主题只是入口，瓶颈才是 alpha 来源。

---

## 3. 第二层：Architecture，判断架构代际，而不是只看行业名

同一个行业里，当前 winners 和下一代 winners 可能完全不同。

以光互联为例，Serenity 的笔记反复区分：

| 代际 | 典型方向 | 代表表达 |
|---|---|---|
| 当前代际 | Pluggable optics、EML、800G/1.6T 放量 | [[LITE]], [[COHR]], [[AAOI]], Innolight |
| 过渡代际 | 服务器和交换机集成度提升，线缆、制造和组装受益 | [[AAOI]], [[JBL]], [[FN]] |
| 下一代 | CPO、硅光、co-packaged optics | [[SIVE]], Celestial AI, Ayar Labs, [[POET]] |
| 更远期 | wafer-level optics、foundry photonics、量子点激光等 | VisEra, QD Laser, ALMU |

关键判断：

1. 当前业务是否真的吃到本代需求。
2. 公司是否能自然迁移到下一代架构。
3. 市场是否把“当前代际受益”误当成“永久赢家”。
4. 估值是否已经反映下一代，还是只反映旧业务。

> [!warning] Serenity 的反直觉点
> “光模块很强”不是买入理由。真正的问题是：这家公司押中的到底是 800G、1.6T、CPO、硅光、InP，还是只是被主题带起来的低纯度标的？

---

## 4. 第三层：Bottleneck，找结构性瓶颈

Serenity 最重要的动作是把新闻、财报、技术路线和供应链关系拼成瓶颈地图。

### 4.1 什么是好瓶颈

一个高质量瓶颈通常同时满足：

| 维度 | 判断标准 |
|---|---|
| 需求确定 | 下游订单、capex、backlog、合同或客户口径明确 |
| 扩产困难 | 产线、良率、设备、材料、认证、工程能力存在真实约束 |
| 集中度高 | 由少数公司控制，或者上游只有 2-3 家关键供应商 |
| 替代困难 | 短期不能轻易换材料、换架构、换供应商 |
| 持续时间长 | 不是一个季度缺货，而是 1-3 年甚至更长的供需错配 |
| 市场低估 | 公开信息存在，但机构尚未完整映射到相关标的 |

### 4.2 Serenity 常见瓶颈类型

| 瓶颈 | 逻辑 | 代表笔记 |
|---|---|---|
| Memory / HBM / NAND | AI workload 对容量、带宽、SSD 需求上升 | [[MU]], [[SNDK]] |
| InP substrate | EML、DFB、laser、photodetector 依赖 InP 衬底 | [[AXTI]], [[LITE]] |
| EML / optical engine | 800G、1.6T、CPO 前夜，光互联成为 GPU 集群瓶颈 | [[LITE]], [[COHR]], [[AAOI]] |
| DSP / switching / interconnect | AI 集群从单机算力转向网络瓶颈 | [[MRVL]], [[AVGO]] |
| Power grid | 数据中心电力接入、变压器、输电、无功补偿、导体材料 | [[HPS]] |
| Neocloud financing | 买 GPU 容易，便宜融资、客户质量、现金流更难 | [[NBIS]], [[CRWV]], [[IREN]] |
| Advanced packaging | HBM、CoWoS、substrate、testing、foundry capacity | [[TSM]], [[AMKR]], [[FORM]], [[AEHR]] |

> [!quote] Serenity 式问题
> “如果这个 AI 资本开支计划必须落地，下一步最可能卡在哪里？谁拥有那个卡点？”

---

## 5. 第四层：Exposure，选择最合适的公开市场表达

找到瓶颈以后，下一步不是立刻买最出名的公司，而是比较不同表达方式的纯度和风险。

### 5.1 暴露纯度排序

| 类型 | 优点 | 风险 |
|---|---|---|
| 纯瓶颈公司 | 弹性最大，市场重估最直接 | 流动性、估值、单点执行风险高 |
| 大公司里的瓶颈业务 | 财务更稳，客户关系强 | 主题被其他业务稀释 |
| 上游材料/设备 | 更早反映供需缺口 | 财报传导慢，市场理解成本高 |
| 下游集成商 | 订单可见度高 | 毛利率和资本开支压力大 |
| 海外更纯标的 | 产业链位置更准 | 美股投资者不一定方便买 |
| ETF / basket | 容错更高 | alpha 被摊薄 |

### 5.2 例子

| 主题 | 可能表达 |
|---|---|
| 存储 supercycle | [[MU]], [[SNDK]], DRAM ETF, SK Hynix, Samsung, Kioxia, [[WDC]] |
| InP/光子上游 | [[AXTI]], [[IQE]], Sumitomo, JX Nippon, [[LITE]], [[COHR]] |
| CPO/硅光 | [[SIVE]], [[MRVL]], [[AVGO]], [[TSEM]], [[SOI]], Celestial AI, Ayar Labs, [[POET]] |
| Glass core / advanced substrate | [[LPK]], Nittobo, Unimicron, Shin-Etsu |
| HBM4 / hybrid bonding metrology | Auros, Towa, [[FORM]], [[AEHR]], [[KLAC]] |
| Neocloud | [[NBIS]], [[CRWV]], [[IREN]], [[CIFR]], [[WULF]] |
| 电力瓶颈 | [[HPS]], POWL, AMSC, PLPC, VICR, ATKR, CLF |

> [!note] Serenity 的表达纪律
> 如果美股没有足够纯的表达，她会用 basket、ETF、海外映射或观察清单，而不是硬把低纯度公司当成高纯度瓶颈标的。

### 5.3 全球纯标的搜索

全量推文里，Serenity 多次把 alpha 来源指向美股之外的韩国、台湾、日本、欧洲小盘供应链公司。这个模块在上一版里写得太轻。

全球搜索的顺序：

1. **先从美国需求反推全球供应商**：例如 Mag7、[[NVDA]]、[[TSM]]、[[MRVL]]、[[JBL]]、[[AAPL]] 的下一代架构需要哪些材料、设备或光源。
2. **再找最纯收入暴露**：美股大公司可能只是低纯度 proxy，真正纯标的可能在韩国、台湾、日本、欧洲。
3. **确认可交易性**：是否能通过 IBKR、ADR、粉单、海外市场、ETF 或本地券商表达。
4. **比较本地市场认知差**：本地投资者可能把它当传统小盘，海外机构可能还没覆盖。
5. **等待全球资金接力**：美股上市、纳入机构覆盖、英文研究扩散、sell-side 主题报告，都可能触发重估。

| 类型 | Serenity 式观察 |
|---|---|
| 韩国小盘供应商 | Samsung / SK Hynix 供应链、HBM4、hybrid bonding、metrology |
| 台湾/日本材料设备 | glass core substrate、advanced packaging、硅光、特殊化学品 |
| 欧洲光子小盘 | DFB laser、MBE、InP reactor、quantum / photonics assets |
| 美股可替代 proxy | 当海外纯标的不可买时，用 [[IQE]], [[TSEM]], [[SOI]], [[LITE]], [[COHR]] 等间接表达 |

> [!tip] IBKR 不是工具细节，而是方法论的一部分
> 如果研究结论指向海外纯标的，但交易工具只允许美股，alpha 会被迫退化成低纯度 proxy。Serenity 全量推文里反复出现国际市场，是因为“能买到更纯的东西”本身就是优势。

---

## 6. 第五层：Repricing，寻找市场重估催化

Serenity 的很多 alpha 来自“公开信息已经出现，但市场还没完全连起来”的时间差。

常见催化：

| 催化 | 观察信号 |
|---|---|
| 订单和 backlog | 长协、预付款、客户锁产能、sold out into 2027/2028 |
| 财报和电话会 | 管理层首次明确提到 AI 需求、涨价、扩产、客户认证 |
| 供应链新闻 | 上游材料短缺、设备 lead time 延长、关键客户新增订单 |
| 机构建仓 | Point72、Apollo 等机构开始买入此前冷门标的 |
| 价格信号 | DRAM/NAND/SSD/光模块/变压器价格持续上修 |
| 政策和政府项目 | CHIPS Act、DOE、国防、能源、电网升级 |
| 税损卖压后修复 | 年末 tax-loss selling 后，基本面没坏但价格被压低 |
| 横向映射 | A 股、台股、日股、韩股先涨，美股 proxy 滞后 |

> [!important] 时间差是 alpha
> Serenity 的强项不是拥有别人没有的信息，而是更快地把公开信息拼成可交易的结构。

---

### 6.1 Volume ramp 比当前 earnings 更重要

Serenity 对早期供应链公司的判断经常不是看当前 EPS，而是看 **qualification -> allocation -> HVM / volume ramp -> revenue recognition** 这条线是否成立。

关键问题：

```text
产品是否已被目标客户认证？
客户是否已经给 RFQ、allocation、design win、volume ramp timeline？
量产在 H2 2026、2027、2028 的哪一个窗口？
当前财报差，是因为需求不存在，还是因为收入还没进入 ramp？
管理层电话会有没有给出 ramp signal？
```

这解释了为什么 Serenity 会说某些 pre-ramp 公司的“earnings 不重要”，真正重要的是管理层对激光、CPO、HBM4、glass core、hybrid bonding 等项目的量产指引。

### 6.2 TAM / 小市值错配

全量推文里，“TAM、market cap、3x/10x、small cap vs massive market”出现频率很高。Serenity 不只找瓶颈，还找 **瓶颈重要性与公司市值之间的非线性错配**。

判断句式：

```text
如果这个公司控制的卡点进入量产，它的收入/利润弹性是否足以让当前市值显得荒谬？
当前市值是在给旧业务估值，还是已经给下一代架构估值？
TAM 扩张来自单一产品涨价，还是来自下游应用扩展到 AI、consumer hardware、robotics、space、defense？
```

TAM 错配要和风险一起看：

| 高质量错配 | 低质量错配 |
|---|---|
| 小市值 + 真实卡点 + 客户认证 + 量产时间表 | 小市值 + 宏大故事 + 无客户验证 |
| TAM 扩张能映射到公司产品 | TAM 很大但公司收入暴露很低 |
| 本地市场还没理解全球需求 | 所有人都知道故事，只是执行风险太高 |

---

## 7. 第六层：Security Structure，证券结构和交易结构

这是上一版最重要的遗漏。全量推文中，Serenity 对融资、稀释、权证、锁定期、低流通盘、短空比例、期权 IV 的关注非常高。

> [!danger] 核心原则
> 好公司、好主题、好 backlog 不等于好股票。股东能不能赚钱，要经过证券结构过滤。

### 7.1 资本结构过滤

| 检查项 | 为什么重要 |
|---|---|
| Debt / interest | 债务利息可能吃掉经营现金流，尤其是 neocloud 和高 capex 公司 |
| Convertible notes | 可转债可能带来套利盘压制和未来稀释 |
| ATM / share offering | 公司可能持续卖股，把增长转移给新股东或债权人 |
| Warrants | 权证行权会改变真实股本和股价上限 |
| Lockup | IPO、SPAC、低流通盘标的解禁后可能出现供给冲击 |
| Float / short interest | 低流通盘和高空头能制造 squeeze，也能制造假 alpha |
| Holding company discount | 控股公司折价不一定能套利，除非有明确释放机制 |

### 7.2 事件结构交易

Serenity 的事件交易不只是“等财报”，还包括：

| 事件 | 交易含义 |
|---|---|
| IPO / recent listing | 低 float、lockup、warrants、市场认知不足都会放大波动 |
| Nasdaq listing / uplisting | 本地小盘转向美国机构投资者，可能改变估值体系 |
| Lawsuit dropped / regulatory overhang removed | 反身性修复，尤其是高 short interest 标的 |
| Financing terms disclosed | 同样是融资，低成本长期资金和 toxic financing 对股东完全不同 |
| Customer contract disclosed | backlog 质量从猜测变为可验证 |
| Index / ETF exposure | 指数权重、国家 ETF、行业 ETF 可以提供放大器 |

### 7.3 期权和波动率错价

全量推文里，Serenity 不少收益来自 LEAPS、OTM calls、covered calls、IV mispricing 和跨市场波动率滞后。

使用前提：

```text
方向判断有基本面或事件支持；
期限覆盖 thesis 兑现窗口；
IV 没有把潜在波动完全定价；
最大亏损能承受；
这不是用杠杆替代研究。
```

典型场景：

| 场景 | 可能工具 |
|---|---|
| 长周期主题但短期 IV 低 | LEAPS |
| 高波动持仓想降低成本 | Covered calls |
| ETF 成分高度集中但 IV 没反映底层波动 | ETF options |
| 相关标的已动，滞后标的未动 | catch-up trade |
| 同一主题不同市场反应错位 | timezone arbitrage |

---

## 8. 第七层：Portfolio，把方法论落到仓位

Serenity 的组合并不是所有 idea 同权，也不是所有推文都代表同等 conviction。

### 8.1 四类仓位

| 仓位类型 | 适用场景 | 例子 |
|---|---|---|
| Core long | 多年结构瓶颈，需求和供给都清楚，标的纯度高 | photonics、memory、InP、部分 neocloud |
| Basket / mini ETF | 供应链受益面广，单一赢家不确定 | power grid、advanced packaging、CPO chain |
| Event trade | 财报、订单、政策、融资、税损修复等短期催化 | beaten-down recovery names |
| Swing / tactical | 波动率、情绪、跨市场滞后、短线错价 | earnings setup、IV trade、timezone arbitrage |

### 8.2 仓位原则

1. **高 conviction 才集中**：绿色仓位可以集中，红色或未验证 idea 不应强行重仓。
2. **不要因为新瓶颈就卖掉旧瓶颈**：如果原瓶颈仍 sold out into 2028，换主题可能是 FOMO。
3. **篮子解决不确定性**：当知道“电力链会受益”但不知道谁最强时，用 mini ETF 表达。
4. **核心仓和事件仓分开**：核心仓看多年瓶颈，事件仓看催化兑现。
5. **纯度和估值要匹配**：低纯度公司不能给高纯度瓶颈估值。

---

## 9. Serenity 评分表

可以用 100 分制快速判断一个 idea 是否值得进入核心研究。

| 模块 | 分值 | 问题 |
|---|---:|---|
| 资本流确定性 | 12 | 下游 capex 是否已经明确？客户是否真实花钱？ |
| 瓶颈强度 | 18 | 供给是否真的卡？是否难扩产？是否有提价权？ |
| 架构位置 | 12 | 它是当前代际、过渡代际还是下一代核心？ |
| 暴露纯度 | 13 | 公司收入、利润、估值是否能明显吃到这个瓶颈？ |
| 证券结构 | 15 | 债务、可转债、ATM、权证、锁定期、低 float 是否会改变股东回报？ |
| 重估催化 | 12 | 未来 3-12 个月是否有订单、财报、机构、价格或政策催化？ |
| 风险可控 | 10 | 是否存在融资、稀释、客户集中、替代、执行或估值风险？ |
| 仓位适配 | 8 | 适合 core、basket、event、options 还是 swing？是否与现有组合相关性过高？ |

解释：

| 总分 | 动作 |
|---:|---|
| 80-100 | 核心候选，继续深挖财务和仓位 |
| 65-79 | 篮子或中等仓位，等待催化确认 |
| 50-64 | 观察清单，只做事件或小仓位 |
| 0-49 | 暂不交易，除非出现明显新信息 |

---

## 10. 反面检查：Serenity 框架最容易踩的坑

| 坑 | 检查问题 |
|---|---|
| 主题正确但股票错误 | 公司到底有没有这个瓶颈收入？还是只是被贴了 AI 标签？ |
| 当前代际高点 | 估值是否已经透支本代际，下一代架构是否会绕开它？ |
| 供给瓶颈被高估 | 扩产、替代、双供、客户自研是否会削弱瓶颈？ |
| 融资结构太差 | backlog 很大，但债务利息、GPU 折旧、ATM 稀释是否吞掉股东回报？ |
| 客户质量不够 | 客户是否是真正有支付能力的 Mag7、hyperscaler、政府或工业客户？ |
| 高波动误判为 alpha | 股价上涨是否由 squeeze、流动性、社媒情绪驱动，而非基本面重估？ |
| 把所有推文等同于观点 | 提及、调侃、观察、swing trade、core long 必须分层 |

---

## 11. 标准研究流程

### Step 1：确定 AI capex 漏斗中的位置

写清楚：

```text
需求来自谁？
资本开支来自谁？
它在 AI 基础设施链条的哪一层？
下游不买它会发生什么？
```

### Step 2：画供应链地图

至少画出：

```text
客户
-> 系统/模组/设备
-> 关键组件
-> 材料/衬底/设备
-> 产能/良率/认证/扩产限制
```

### Step 3：验证瓶颈是否真实

需要找证据：

```text
订单 / backlog / sold-out timeline
价格上涨
lead time 拉长
客户认证周期
新增 capex
竞争对手也承认短缺
机构或产业方开始行动
```

### Step 4：比较标的表达

至少比较三类：

```text
最纯美股标的
海外更纯标的
低纯度但流动性更好的大公司
```

### Step 5：检查证券结构

至少写清楚：

```text
债务和利息成本：
可转债 / ATM / 权证 / 锁定期：
真实 fully diluted share count：
float 和 short interest：
是否存在 toxic financing 或未来供给冲击：
```

### Step 6：识别催化和退出条件

必须同时写：

```text
为什么未来 3-12 个月市场会重新定价？
什么事实出现后说明 thesis 错了？
什么事实出现后说明只是估值太贵、不是逻辑错？
```

---

## 12. 单票研究模板

```markdown
# Ticker / Company

## 一句话 thesis

这家公司是 [AI capex 漏斗] 中 [具体瓶颈] 的 [公开市场表达]。

## 供应链位置

- 下游客户：
- 直接产品：
- 上游约束：
- 替代方案：

## 瓶颈证据

- 订单 / backlog：
- 价格 / lead time：
- 产能 / 良率：
- 客户认证：
- 同业验证：

## 架构代际

- 当前代际：
- 过渡代际：
- 下一代风险或机会：

## 标的纯度

- 收入暴露：
- 毛利弹性：
- 估值对应业务：
- 其他业务稀释：

## 证券结构

- 市值 / TAM 错配：
- cash / debt / interest：
- fully diluted share count：
- ATM / warrants / convertibles：
- lockup / insider selling：
- float / short interest：
- option liquidity / IV：
- 是否有 toxic financing：

## 催化

- 3 个月：
- 6-12 个月：
- 机构或产业验证：

## 风险

- 客户集中：
- 融资 / 稀释：
- 多供 / 替代：
- 执行：
- 估值：

## 仓位分类

Core / Global pure-play / Basket / Event / Options / Swing / Watchlist

## 退出条件

- thesis broken：
- valuation stretched：
- better expression found：
```

---

## 13. 与 Serenity 笔记和全量 PDF 的对应证据

| 来源 | 方法论含义 |
|---|---|
| `aleabitoreddit_tweets(2).pdf` | 4788 条全量推文显示，国际市场、证券结构、TAM/市值错配、ramp 催化、期权/IV 是 V1 框架遗漏的高权重模块 |
| [[NBIS]] | 信息综合和 mapping 是核心 edge；neocloud 需要比较 backlog、客户、融资和 GPU 折旧 |
| [[CRWV]] | 同样是 AI 云，融资成本和债务结构可以决定股东回报 |
| [[MU]] | 存储是多年结构瓶颈，但不要因为新瓶颈频繁 FOMO 换仓 |
| [[SNDK]] | 结构性瓶颈要在市场发现前识别，memory cycle 可以通过多种标的表达 |
| [[LITE]] | 光互联需要分清 EML、800G、1.6T、CPO 等代际 |
| [[AXTI]] | 上游 InP 衬底可能比下游热门公司更接近真实卡点 |
| [[AAOI]] | 当前 pluggable bottleneck、客户订单和架构过渡需要分层看 |
| [[HPS]] | 电力链条适合用 mini ETF 思维覆盖多个瓶颈 |
| [[MRVL]] | 网络、DSP、custom silicon 和 AI interconnect 是 GPU 后的关键传导方向 |
| [[SIVE]] | 下一代 CPO / silicon photonics 可能是当前光模块之后的再定价方向 |
| [[IQE]], [[TSEM]], [[SOI]], [[LPK]] | 全球纯标的和上游材料/设备可能比美股大盘 proxy 更接近真实卡点 |
| [[EWY]] | 国家 ETF 和集中成分权重可以形成波动率错价或跨市场表达 |
| [[HIMS]], [[CRCL]], [[HOOD]], [[RDDT]] | Serenity 也做高 short interest、监管/诉讼、平台修复、用户变现等非半导体事件交易 |
| [[RKLB]], [[LPTH]], [[OSS]], [[AIRO]] | 国防、空间、关键材料和国家安全主题是 AI supply chain 之外的另一类结构机会 |

---

## 14. 最终判断句式

一个成熟的 Serenity 风格结论应该长这样：

> [!example] 标准结论
> 我看多这家公司，不是因为它是 AI 概念股，而是因为资本开支正在从 [下游需求] 传导到 [具体环节]；这个环节的供给被 [材料/产能/认证/设备/工程能力] 限制；公开市场中 [公司] 是 [纯度/流动性/估值] 最合适的表达；证券结构没有明显吞噬普通股回报；未来 [catalyst / ramp / listing / financing / price signal] 可能让市场重新定价；如果 [反证] 出现，则 thesis 失效。

反过来，如果一个 idea 只能写成“它也受益 AI”，但写不清楚：

```text
谁花钱？
卡在哪里？
谁控制卡点？
为什么现在没被定价？
什么时候会被定价？
股东结构有没有坑？
错了怎么知道？
```

那它还不是 Serenity 框架下的合格核心仓。
