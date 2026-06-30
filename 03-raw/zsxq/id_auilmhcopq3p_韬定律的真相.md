# 韬定律的真相

        
            [来自：
                半导体大佬的会议室](https://wx.zsxq.com/group/88888812815442)
        
        
            
                

![](images/39ac34f1b548792d9368.jpg)

                吴梓豪leslie
            
            2026年05月26日 03:27
        
        
            从何庭波论文的 τ scaling、155→238 MTr/mm²、LogicFolding 到“等效 1.4nm”的口径拆解

何庭波论文提出的“韬定律”（τ scaling）在工程方向上抓住了后摩尔时代的真实问题，先进制程之外，封装、互联、存储、供电、散热、系统架构都会限制最终算力。

但论文最值得警惕的地方，是把“时间常数 τ”的系统级优化，与“155→238 MTr/mm²”“2031 年等效 1.4nm”等最容易被公众理解为先进制程节点的指标混在一起。

拆开公式和口径后可以看到，所谓 238 MTr/mm²并不是SMIC N+3 的单层物理逻辑密度，而是华为公式口径叠加 3D 俯视 footprint 后得到的有效密度。

笔者这篇文章的目的不是否定 3D 堆叠、先进封装、光互联、存储融合这些技术方向。恰恰相反，这些方向是全球半导体工业正在共同推进的真实方向。

本文要指出的是，如果华为可以用自定义公式、3D footprint、系统级 τ 优化来宣称“等效 MTr/mm²”和“等效 1.4nm”，那么台积电、英伟达、AMD、Intel、三星、SK hynix 等全球领先者同样可以用相同口径重算，而且海外这些技术大部分早已经在商业产品中量产落地，而不是论文。

### **何庭波论文的要点：从空间缩微转向时间缩微**

**原文摘录：**“This perspective argues for a successor scaling principle — τ scaling — that adopts time itself, rather than transistor area, as the primary metric of progress...”

**问题指出：这句话是论文的理论核心：用时间 τ 替代面积或节点作为进步指标。这个方向本身有工程意义，但它不是一条可直接换算为“几纳米”的物理定律，但他的宣传却全部挂勾了几纳米多少MTr。**

何文首先指出，过去半导体行业靠摩尔定律和 Dennard scaling 前进，晶体管变小、频率提高、单位逻辑门成本下降。

但 2005 年前后 Dennard scaling 失效，电压不再随尺寸等比例下降。7nm 以后，局部互连 RC、EUV 折旧、掩膜成本、设计规则复杂度开始吞噬几何缩微收益。

论文特别强调，对于华为这样前段光刻受限的企业，不能再假设“下一代节点会自然解决问题”。

因此论文提出，半导体进步的主指标不应再只是空间尺寸，而应是跨层时间常数 τ。论文把 τ 分解为晶体管、电路、芯片、系统四层：

τ = f(τ_transistor, τ_circuit, τ_chip, τ_system)

这套框架的普通解释是：晶体管开关要快，电路关键路径要短，芯片内部访问存储要快，系统之间传输数据也要快。

最终用户看到的不是“某根线宽多少纳米”，而是应用响应更快、吞吐更高、功耗更低。

这部分既合情有合理，也是全球半导体行业早在进行的方向。今天 AI 数据中心的瓶颈早已不是单一芯片峰值算力，而是 HBM 带宽、片间互联、机柜互联、供电、散热、封装良率和软件调度的综合结果。

而且全世界整个供应链早都在解决上述问题，英伟达供应链的台积电，海力士，光模块，CPO，PCB，液冷，服务器电源与机柜这些热点题材都炒了多少年了？

而何的论文问题在于，论文后面又用 MTr/mm²和“等效 1.4nm”来对外表述，导致“时间缩微”与“制程缩微”的语义被混在一起。宣传演讲也着重MTr跟等效1.4nm这些博眼球的数据，韬定律得核心『时间』被抛在脑后。

![](images/7e66e4b258f8740da222.png)

**表 1：韬定律按层级拆解后，并不是全新物理路线，而是把全球产业正在做的系统级优化统一包装成 τ scaling。**

### **论文最核心的实证：LogicFolding 与 Kirin 2026（9050) 的 155→238 MTr/mm²**

**原文摘录：**“Transistor density rose step-wise from 155 to 238 MTr/mm² in a single generation (transistor density is calculated using the formula 2/(CPP*cell height); the area utilization of Kirin SoC design is 68%)...”

**问题指出：这是全文最容易被误读的地方。原文直接写 transistor density 和 MTr/mm²，但同时又承认这是固定节点下通过三维拓扑重组得到的提升。它不应被理解为 SMIC N+3 单层平面制程密度变成 238 MTr/mm²。**

**原文摘录：**“These gains were achieved at a fixed device node, obtained not through a new lithography step but through a topological reorganization of the spatial distribution of logic in three dimensions.”

**问题指出：这句话实际已经说明：238 MTr/mm²不是新光刻节点带来的平面物理密度，而是三维重组后的有效密度。**

**原文摘录：**“The LogicFolding implementation shipping in Kirin 2026 is deliberately conservative... folding was applied selectively along key critical paths rather than across the entire design.”

**问题指出：原文自己承认 Kirin 2026(9050) 不是整颗芯片全面折叠，而是选择性应用在关键路径。这进一步说明 155→238 不能被当作整个制程节点的平面密度跃迁。**

按照论文描述，LogicFolding 不是简单把两个完整 CPU 或 GPU 计算 die 上下叠起来，而是把 digital、analog、memory circuits 分配到垂直堆叠的 active tiers 中，尤其把 critical-path gates、NoC data path、SRAM 关键路径、clock network 等放到上下两层之间重新布局。

论文给出的工艺/封装参数包括：hybrid bonding pitch 1.5μm，目标 gear ratio 接近 1；overlay accuracy 小于 0.5μm；TSV CD/KOZ 小于 1.5μm；TSV pitch 小于 6μm；failure rate 小于 100ppm，repair rate 99.9%。这些参数说明它确实是一种先进 3D active-tier 堆叠能力，但不是一条全新的物理路线或者技术。

很多人讨论这组数据的hybrid bonding pitch 1.5μm达到国际最领先水平，目前台积电SoIC-X-W的官方规格是 <3μm。这个数据被国内许多网友引用，超越了台积电。

目前台积电的SoIC技术可支持hybrid bonding solution SoIC capable of 0.9μm pitch，这里会有几个问题，首先是良率，这数字任何厂家都是谜，不论是台积电或者是华为。

再来是台积电虽然可能有更强的sub-μm HB能力，但目前也没听到有哪家客户采用，所以Kirin 2026（9050)有可能是全球混合键合pitch最小的芯片。

也就是说华为LogicFolding技术在某些参数上确实已进入世界领先集团。

华为在混合键合领域是在全球领先集团。我想这部分国内可以买到BESI的100nm accuracy HB system等最先进混合键合设备，自然不会差。

1.5μm跟目前全球领先的2μm以下可能更高一点但也基本大家属于同一水平，未来再混合键合领域的sub-μm HB能力也将是一个重要观察指标。

但最小pitch是可以靠高成本方案去争取的，所以除了pitch以外，我们还得看良率以及througput吞吐量，低良率以及低吞吐量也可以不计代价缩小pitch但不具备经济性。

另外华为公布的overlay accuracy 小于 0.5μm 跟1.5μm的pitch相比比例过大，IMEC的2μm的pitch对应0.35μm套刻精度完全在合理的control window内，华为的0.5μm套刻精度对应1.5μm的pitch确实不太合乎半导体制程比例。

总而言之，华为hybrid bonding pitch 1.5μm绝对是国际领先水平，但这数字可能无法改变太多，毕竟它只是芯片诸多制程中的一个混合键合工艺，再其中的一个重要参数之一。对于改变整个芯片性能无疑是杯水车薪。

全世界都在混合键合，大家的设备相同，研发时间也差不多，所以pitch差距不会太大，但芯片怎堆叠，可不只是pitch这么简单，在先进封装这个领域，我们与全球的差距大约还有两年左右的时间。

![](images/a0b0c7161e24c9fe22b3.png)

**表 2：何文 LogicFolding 参数与本文解读。**

### **155MTr的第一层口径问题：华为的公式天然比Mark Bohr密度公式高约 35.7%**

这是何庭波论文中最具争议的部分。但很可惜全球所有中英文专业或不专业的媒体，无一看出。只有笔者在阅读何的论文之后发现这个问题以及后续衍生出的疑点。
何在论文中直接给出 transistor density 计算公式：D_Huawei = 2 × 10^6 / (CPP_nm × CellHeight_nm)
但行业常见的Mark Bohr 逻辑密度公式却是：D_Bohr = 1.474 × 10^6 / (CPP_nm × CellHeight_nm)
这里出现了最大的争议点之一，两者比值为：D_Huawei / D_Bohr = 2 / 1.474 ≈ 1.357倍
也就是说，在同一组 CPP 和 cell height 下，只要换成华为公式，MTr/mm²数字就会天然高约 35.7%。
所以155与238MTr，这不是华为制程突然变先进，而是计算公式的的系数压根不同所致。
假设 SMIC N+3 的某组尺寸可以用 CPP=57nm、cell height=228nm 近似演示，则：
D_Bohr = 1.474 × 10^6 / (57 × 228) ≈ 113.4 MTr/mm²D_Huawei = 2 × 10^6 / (57 × 228) ≈ 153.9 MTr/mm²
上述两组数字，就解释了去年TechInsights 对 Kirin 9030 / SMIC N+3 的拆解报告中计算出7nm的N+3制程 MTr为110~120，如今何庭波的论文没有来由的增加到155。
155这数字一出让整个行业感到莫名其妙，毕竟N+3得明年才能换代，2026年的制程跟2025是一样的。而且明年即便N+4也到不了155。
主要原因就是这155 压根不是TechInsights或行业里采用的Bohr密度公式的口径，而是华为自己的口径（何庭波论文明确计算公式）。
这就是解释了为何，没有任何理由MTr忽然间大增的原因，其实还是去年那个MTr 110～120的N+3。
在N+3的基础上透过自定义公式放大MTr，再加上上述的LogicFolding逻辑折叠技术，何庭波的论文称进一步把MTr提升到238，如此神奇的技术又是怎么回事呢？

![](images/f0259f906ece9e5c5651.png)

**表 3：155 MTr/mm²的第一层放大来自公式口径差异。**

### **238MTr的第二层口径问题：3D footprint effective density，而不是单层制程密度**

MTr/mm²表面上是“每平方毫米百万晶体管”，看似没有等效空间。

但只要进入 3D 堆叠，关键问题就变成，这个平方毫米到底是单层 silicon area，还是封装/芯片俯视 footprint？

传统平面制程密度默认是：D_process = N_transistors / A_single_active_layer

但 3D 堆叠可以写成：D_3D_footprint = (N_bottom + N_top) / A_projected_footprint

如果上下两层 active logic 疊在同一个俯视面积内，分子增加，分母不变，MTr/mm²自然提高。这个数不是假的，但它已经不是传统意义上的单层制程节点密度。

用华为自己的 155→238 来反推：提升比例 = 238 / 155 ≈ 1.535× 。增加量 = 238 − 155 = 83 MTr/mm²

如果上层逻辑密度也按华为口径为 155，则需要覆盖底层 footprint 的比例为：f = 83 / 155 ≈ 53.5%

也就是说，如果上层是同密度逻辑，它大约只覆盖了底层 footprint 的一半多。如果上层覆盖整个 footprint，那么上层平均密度约 83 MTr/mm²。

这都不像“完整高性能计算 die 叠完整高性能计算 die”，而更像局部 critical-path gates、NoC、SRAM 周边、clock、control、I/O 或支援逻辑的选择性 folding。

再把华为公式还原到Mark Bohr口径：

155 / 1.357 ≈ 114.2 MTr/mm²

238 / 1.357 ≈ 175.4 MTr/mm²

所以所谓 238，本质上更像“Bohr 约 175 MTr/mm²的 3D footprint 有效密度”，不是 SMIC N+3 单层物理密度突然变成 238。

**何论文的 3D 堆叠不是新物理路线：产业早已有大量对应案例**

何论文把 LogicFolding 作为韬定律的核心 proof point，但从产业分类看，它属于 active-tier stacking / logic-on-logic / SRAM-on-logic / memory-on-logic / active base die + compute chiplet 的大类。

我不清楚最终kirin 2026芯片上的堆叠式堆了什么，但离不开上述范畴，这些技术与方向全部都不是华为独创。

区别只在于何文宣称它在手机 SoC 的关键路径上做到了更细粒度的 cell/path-level folding，但公开论文没有给出版图、拆解或第三方验证。

![](images/a3f7c6e920979a202bef.png)

表 4：何论文的堆叠方式在全球产业中早以大量落地并非新技术。

### **AMD 3D V-Cache 是最直观的反例：若按何文口径，MTr/mm²也能大幅提高**

以 AMD 3D V-Cache 为例，公开资料显示 Ryzen 7 5800X3D 的 7nm CCD 面积约 80.7mm²、晶体管约 4.15B。

上层 3D V-Cache die 面积约 41mm²、晶体管约 4.7B。正常单层 CCD 口径为：D_CCD = 4.15B / 80.7mm² ≈ 51.4 MTr/mm²

如果按何文式 3D footprint 口径，把上层 V-Cache 晶体管也算入 CCD 俯视 footprint：D_footprint = (4.15B + 4.7B) / 80.7mm² ≈ 109.7 MTr/mm²

提升比例为：109.7 / 51.4 ≈ 2.13× 。这比华为 155→238 的 1.535×还高。

但 AMD 根本不会说“我们的7nm CCD 等效变成 3nm”。因为行业清楚这只是 SRAM cache die 叠在 CPU CCD 上，提升的是缓存容量、局部数据访问、性能和功耗，而不是 CPU 逻辑制程密度。

如果改用 total silicon area，把上下 die 面积都算进成本和晶圆消耗：D_total_silicon = (4.15B + 4.7B) / (80.7 + 41)mm² ≈ 72.7 MTr/mm²

![](images/70b478d5e78b036d3523.png)

**表 5：同一颗 AMD 3D V-Cache 芯片，不同口径下 MTr/mm²差异巨大。**

### **如果同样口径给台积电 N5/N3**

何的论文的问题不在于“用等效密度”本身，而在于只把等效口径用于华为自身，而不用同等口径与其他竞品相比，有明显的断章取义嫌疑。即便何在论文中提供了其计算公式。

如果允许华为把公式放大和 3D footprint 合并进 MTr/mm²，那么台积电 N5/N3 也应当用同样口径重算。

以常见公开估算为例，TSMC N5 的 Bohr 类逻辑密度约 137.6 MTr/mm²，N3B/N3E/N3P 可粗略使用约 197/216/224 MTr/mm²作为示意。仅把公式换成华为口径，即乘以 1.357，就得到：

![](images/0d09ba1f5d4bd73785bf.png)

**表 6：只换公式口径，TSMC N3 的“华为式 MTr/mm²”已明显高于 238。**

**
**

如果再套用何文 155→238 的 LogicFolding 增益，也就是华为做到238的算法对应：

LogicFolding 增益 = 238 / 155 ≈ 1.535

![](images/e9442db89770e65e04a2.png)

表 7：若全球领先节点也用同一等效口径，华为 238 MTr/mm²只有台积电3nm的一半，反推依然是台积电7nm优化版的水平。

**
**

这个表不是说台积电会这样宣传，而是说明：等效口径必须对所有玩家一致。不能只允许华为把 3D 堆叠、封装、系统优化算进 MTr/mm²，却不允许台积电、AMD、NVIDIA、Intel、三星、SK hynix 用相同口径重算。

### **韬定律的真正问题：讲 τ 时合理，讲 MTr/mm²和 1.4nm 时混淆**

**原文摘录：**“τ is a time law, not a joule law. A super-node operating 10× faster but with 10× greater power consumption violates no scaling principle, yet exceeds grid capacity.”

**问题指出：这段原文其实非常重要：τ scaling 只管时间，不自动解决功耗、供电、散热、成本和良率。把 τ 改善直接宣传成等效先进节点，会掩盖这些硬约束。**

**原文摘录：**“Full-scale LogicFolding requires the toolchain to treat multiple stacked dies as a single continuous design entity — partitioning logic at cell granularity rather than block granularity...”

**问题指出：原文承认全规模 LogicFolding 需要全新的 3D-native EDA、跨 die timing closure、inter-wafer variation 处理。这说明它还不是成熟完成品。**

**原文摘录：**“Every hybrid bond and every TSV incurs a finite resistance and capacitance penalty, and TSV KOZ displaces standard cells.”

**问题指出：这是对 3D 堆叠“不是免费午餐”的承认。垂直互联会带来 R/C、KOZ、良率、热和供电问题。**

 这些原文其实足以说明，韬定律不是一个可以把所有系统提升简单相乘、最后换成“等效几纳米”的公式。

它是一套系统工程优化方法。某些场景下，它可以改善延迟、吞吐、能效或 footprint；但如果拿它来替代物理制程差距，就会变成宣传口径。

真正的矛盾在于，理论上，何的论文说不要再看 nm，要看 τ；宣传上，却又把读者最熟悉的 MTr/mm²和 1.4nm 拿出来。

更关键的是，这些 MTr/mm²并非传统制程密度，而是自定义公式 + 3D footprint 的结果。

这就形成了一个非常典型的叙事技巧，当物理节点不占优时，改用系统级口径。当需要传播效果时，又把系统级口径翻译成先进节点听感。巧妙之处就在这里。

### **回到全球产业：每个瓶颈都要突破，但领先者正在全栈推进**

后摩尔时代确实不是只靠先进制程。AI 算力系统至少有五个核心瓶颈：先进制程、先进封装、光互联/电互联、散热/供电、存储/HBM。每一项都必须突破，任何一项短板都会限制最终算力。

![](images/37b5be697816dd378fcb.png)

**表 8：后摩尔时代的竞争是全栈竞争，不是单一“定律”可以抹平。**

**
**

这也是为什么说，韬定律不能被理解为“华为用一条新定律绕过了全球半导体差距”。它更像是华为在先进光刻受限条件下提出的一套补偿性工程路线。

这个路线可以带来局部收益，也可能在某些特定产品上做出漂亮优化。但它并不能改变全球领先者也在用同样甚至更强的工具链、封装平台、HBM 供应链和系统生态快速前进。

英伟达的 GB200/NVL72 本身就是真正系统级 τ 优化：GPU、Grace CPU、NVLink、NVSwitch、HBM、液冷 rack-scale system 共同工作。

AMD MI300 是 compute + active I/O die + HBM 的 3D 异质集成。

台积电 3DFabric/SoIC/CoWoS 正在把先进制程、先进封装、HBM、未来光互联整合成平台。

SK hynix 的 HBM4 则是 AI 记忆体瓶颈的现实突破。

把这些全部放进同一个 τ scaling 口径，全球领先者并不会原地等华为追赶，甚至正在不断拉开差距，华为没办法凭借一个韬定律轻松改变战局。

### **最终结论：韬定律揭示的是系统战，不是差距消失**

韬定律最有价值的一点，是承认后摩尔时代的竞争已经从单一制程节点，转向制程、封装、存储、互联、散热、供电、软件和系统架构的全栈竞争。

何庭波这个判断是对的。今天再只看“几纳米”已经不够，必须看最终系统能把多少算力、带宽、存储和能效组织起来。

但韬定律最大的问题，是把系统级优化的合理性，转化成“等效 MTr/mm²”“等效 1.4nm”的传播口径。

155→238 MTr/mm²经过拆解后，至少被两层放大：

第一，华为公式 2/(CPP×cell height) 相对 Bohr/TechInsights 类公式天然高约 35.7%；

第二，LogicFolding 把上下 active tiers 的晶体管按俯视 footprint 合并计算，使 MTr/mm²从单层制程密度变成 3D footprint effective density。

因此，笔者的判断与结论是：

何庭波论文的 3D 堆叠不是全新的物理路线，而是产业已有的 logic-on-logic、SRAM-on-logic、memory-on-logic、active-base-die stacking、hybrid bonding 等技术方向的华为式整合。

155→238 MTr/mm²不是 SMIC N+3 单层平面制程密度从 155 变成 238，而是华为公式口径下，叠加局部 3D LogicFolding 后的俯视 footprint 有效密度。

如果用同样口径看全球竞争对手，AMD 3D V-Cache、MI300、Intel Foveros、Samsung X-Cube、TSMC SoIC、HBM + GPU package 都可以大幅提高所谓 MTr/mm²。

台积电 N3 若套用华为公式和同等 folding 增益，数字会高达467，远高于论文中kirin 2026的238两倍。这个差距基本也说明kirin 2026的真实物理MTr跟台积电7nm优化版接近，也跟kirin 9030的N+3的110~120接近，脱下面纱之后，一切都还璞归真。

因此，韬定律不能证明华为追平先进制程，也不能证明中西差距缩小。

它真正说明的是，后摩尔时代竞争变成系统战，而在这场系统战中，全球领先供应链仍在制程、封装、HBM、光互联、散热、系统互联等每个环节快速推进。

所以，我们可以承认韬定律作为工程方法论有启发性，也可以承认华为在受限环境下尝试通过 3D 堆叠和系统协同取得增量。

但不能接受把自定义口径包装成“等效先进节点”的宣传。

真正严谨的比较，必须把单层制程密度、3D footprint 有效密度、total silicon area、成本、功耗、散热、良率和系统性能分开。只有这样，才能看清技术进步本身，也才能看清宣传口径背后的“猫腻”。

今天韬定律大火，简短看了几篇文章，全部都是不知所以，晚上看了下论文，一下就看到了最大的问题，那就是何庭波的计算公式，这个基本常识的问题全世界中英文媒体，不论媒体巨擘还是外资投行，没有一个发现，没有一个针对这基本公式去说明，全部胡乱报导一通。

早在上周3nm等效小作文爆炒之后，笔者第一时间就澄清与打假，但是文章几乎发不了，说明这次布局是很精妙且庞大的组织，连续的预热与最终高潮，韬定律是大事件，热度非常高，其实炒一波应该也没问题，不过我是不会去的，还是慢慢等好机会。

回到半导体行业，我一直反覆强调你搞不明白那就是定义与口径出现问题，永远就只有这问题，只要统一口径与定义，半导体还是那个半导体，不会有弯道超车，更不会有莫名其妙的进步，全部都是脚踏实地的一步一脚印，这才叫科学，这才叫产业。

        
        从何庭波论文的 τ scaling、155→238 MTr/mm²、LogicFolding 到“等效 1.4nm”的口径拆解

何庭波论文提出的“韬定律”（τ scaling）在工程方向上抓住了后摩尔时代的真实问题，先进制程之外，封装、互联、存储、供电、散热、系统架构都会限制最终算力。

但论文最值得警惕的地方，是把“时间常数 τ”的系统级优化，与“155→238 MTr/mm²”“2031 年等效 1.4nm”等最容易被公众理解为先进制程节点的指标混在一起。

拆开公式和口径后可以看到，所谓 238 MTr/mm²并不是SMIC N+3 的单层物理逻辑密度，而是华为公式口径叠加 3D 俯视 footprint 后得到的有效密度。

笔者这篇文章的目的不是否定 3D 堆叠、先进封装、光互联、存储融合这些技术方向。恰恰相反，这些方向是全球半导体工业正在共同推进的真实方向。

本文要指出的是，如果华为可以用自定义公式、3D footprint、系统级 τ 优化来宣称“等效 MTr/mm²”和“等效 1.4nm”，那么台积电、英伟达、AMD、Intel、三星、SK hynix 等全球领先者同样可以用相同口径重算，而且海外这些技术大部分早已经在商业产品中量产落地，而不是论文。

### **何庭波论文的要点：从空间缩微转向时间缩微**

**原文摘录：**“This perspective argues for a successor scaling principle — τ scaling — that adopts time itself, rather than transistor area, as the primary metric of progress...”

**问题指出：这句话是论文的理论核心：用时间 τ 替代面积或节点作为进步指标。这个方向本身有工程意义，但它不是一条可直接换算为“几纳米”的物理定律，但他的宣传却全部挂勾了几纳米多少MTr。**

何文首先指出，过去半导体行业靠摩尔定律和 Dennard scaling 前进，晶体管变小、频率提高、单位逻辑门成本下降。

但 2005 年前后 Dennard scaling 失效，电压不再随尺寸等比例下降。7nm 以后，局部互连 RC、EUV 折旧、掩膜成本、设计规则复杂度开始吞噬几何缩微收益。

论文特别强调，对于华为这样前段光刻受限的企业，不能再假设“下一代节点会自然解决问题”。

因此论文提出，半导体进步的主指标不应再只是空间尺寸，而应是跨层时间常数 τ。论文把 τ 分解为晶体管、电路、芯片、系统四层：

τ = f(τ_transistor, τ_circuit, τ_chip, τ_system)

这套框架的普通解释是：晶体管开关要快，电路关键路径要短，芯片内部访问存储要快，系统之间传输数据也要快。

最终用户看到的不是“某根线宽多少纳米”，而是应用响应更快、吞吐更高、功耗更低。

这部分既合情有合理，也是全球半导体行业早在进行的方向。今天 AI 数据中心的瓶颈早已不是单一芯片峰值算力，而是 HBM 带宽、片间互联、机柜互联、供电、散热、封装良率和软件调度的综合结果。

而且全世界整个供应链早都在解决上述问题，英伟达供应链的台积电，海力士，光模块，CPO，PCB，液冷，服务器电源与机柜这些热点题材都炒了多少年了？

而何的论文问题在于，论文后面又用 MTr/mm²和“等效 1.4nm”来对外表述，导致“时间缩微”与“制程缩微”的语义被混在一起。宣传演讲也着重MTr跟等效1.4nm这些博眼球的数据，韬定律得核心『时间』被抛在脑后。

![](images/7e66e4b258f8740da222.png)

**表 1：韬定律按层级拆解后，并不是全新物理路线，而是把全球产业正在做的系统级优化统一包装成 τ scaling。**

### **论文最核心的实证：LogicFolding 与 Kirin 2026（9050) 的 155→238 MTr/mm²**

**原文摘录：**“Transistor density rose step-wise from 155 to 238 MTr/mm² in a single generation (transistor density is calculated using the formula 2/(CPP*cell height); the area utilization of Kirin SoC design is 68%)...”

**问题指出：这是全文最容易被误读的地方。原文直接写 transistor density 和 MTr/mm²，但同时又承认这是固定节点下通过三维拓扑重组得到的提升。它不应被理解为 SMIC N+3 单层平面制程密度变成 238 MTr/mm²。**

**原文摘录：**“These gains were achieved at a fixed device node, obtained not through a new lithography step but through a topological reorganization of the spatial distribution of logic in three dimensions.”

**问题指出：这句话实际已经说明：238 MTr/mm²不是新光刻节点带来的平面物理密度，而是三维重组后的有效密度。**

**原文摘录：**“The LogicFolding implementation shipping in Kirin 2026 is deliberately conservative... folding was applied selectively along key critical paths rather than across the entire design.”

**问题指出：原文自己承认 Kirin 2026(9050) 不是整颗芯片全面折叠，而是选择性应用在关键路径。这进一步说明 155→238 不能被当作整个制程节点的平面密度跃迁。**

按照论文描述，LogicFolding 不是简单把两个完整 CPU 或 GPU 计算 die 上下叠起来，而是把 digital、analog、memory circuits 分配到垂直堆叠的 active tiers 中，尤其把 critical-path gates、NoC data path、SRAM 关键路径、clock network 等放到上下两层之间重新布局。

论文给出的工艺/封装参数包括：hybrid bonding pitch 1.5μm，目标 gear ratio 接近 1；overlay accuracy 小于 0.5μm；TSV CD/KOZ 小于 1.5μm；TSV pitch 小于 6μm；failure rate 小于 100ppm，repair rate 99.9%。这些参数说明它确实是一种先进 3D active-tier 堆叠能力，但不是一条全新的物理路线或者技术。

很多人讨论这组数据的hybrid bonding pitch 1.5μm达到国际最领先水平，目前台积电SoIC-X-W的官方规格是 <3μm。这个数据被国内许多网友引用，超越了台积电。

目前台积电的SoIC技术可支持hybrid bonding solution SoIC capable of 0.9μm pitch，这里会有几个问题，首先是良率，这数字任何厂家都是谜，不论是台积电或者是华为。

再来是台积电虽然可能有更强的sub-μm HB能力，但目前也没听到有哪家客户采用，所以Kirin 2026（9050)有可能是全球混合键合pitch最小的芯片。

也就是说华为LogicFolding技术在某些参数上确实已进入世界领先集团。

华为在混合键合领域是在全球领先集团。我想这部分国内可以买到BESI的100nm accuracy HB system等最先进混合键合设备，自然不会差。

1.5μm跟目前全球领先的2μm以下可能更高一点但也基本大家属于同一水平，未来再混合键合领域的sub-μm HB能力也将是一个重要观察指标。

但最小pitch是可以靠高成本方案去争取的，所以除了pitch以外，我们还得看良率以及througput吞吐量，低良率以及低吞吐量也可以不计代价缩小pitch但不具备经济性。

另外华为公布的overlay accuracy 小于 0.5μm 跟1.5μm的pitch相比比例过大，IMEC的2μm的pitch对应0.35μm套刻精度完全在合理的control window内，华为的0.5μm套刻精度对应1.5μm的pitch确实不太合乎半导体制程比例。

总而言之，华为hybrid bonding pitch 1.5μm绝对是国际领先水平，但这数字可能无法改变太多，毕竟它只是芯片诸多制程中的一个混合键合工艺，再其中的一个重要参数之一。对于改变整个芯片性能无疑是杯水车薪。

全世界都在混合键合，大家的设备相同，研发时间也差不多，所以pitch差距不会太大，但芯片怎堆叠，可不只是pitch这么简单，在先进封装这个领域，我们与全球的差距大约还有两年左右的时间。

![](images/a0b0c7161e24c9fe22b3.png)

**表 2：何文 LogicFolding 参数与本文解读。**

### **155MTr的第一层口径问题：华为的公式天然比Mark Bohr密度公式高约 35.7%**

这是何庭波论文中最具争议的部分。但很可惜全球所有中英文专业或不专业的媒体，无一看出。只有笔者在阅读何的论文之后发现这个问题以及后续衍生出的疑点。
何在论文中直接给出 transistor density 计算公式：D_Huawei = 2 × 10^6 / (CPP_nm × CellHeight_nm)
但行业常见的Mark Bohr 逻辑密度公式却是：D_Bohr = 1.474 × 10^6 / (CPP_nm × CellHeight_nm)
这里出现了最大的争议点之一，两者比值为：D_Huawei / D_Bohr = 2 / 1.474 ≈ 1.357倍
也就是说，在同一组 CPP 和 cell height 下，只要换成华为公式，MTr/mm²数字就会天然高约 35.7%。
所以155与238MTr，这不是华为制程突然变先进，而是计算公式的的系数压根不同所致。
假设 SMIC N+3 的某组尺寸可以用 CPP=57nm、cell height=228nm 近似演示，则：
D_Bohr = 1.474 × 10^6 / (57 × 228) ≈ 113.4 MTr/mm²D_Huawei = 2 × 10^6 / (57 × 228) ≈ 153.9 MTr/mm²
上述两组数字，就解释了去年TechInsights 对 Kirin 9030 / SMIC N+3 的拆解报告中计算出7nm的N+3制程 MTr为110~120，如今何庭波的论文没有来由的增加到155。
155这数字一出让整个行业感到莫名其妙，毕竟N+3得明年才能换代，2026年的制程跟2025是一样的。而且明年即便N+4也到不了155。
主要原因就是这155 压根不是TechInsights或行业里采用的Bohr密度公式的口径，而是华为自己的口径（何庭波论文明确计算公式）。
这就是解释了为何，没有任何理由MTr忽然间大增的原因，其实还是去年那个MTr 110～120的N+3。
在N+3的基础上透过自定义公式放大MTr，再加上上述的LogicFolding逻辑折叠技术，何庭波的论文称进一步把MTr提升到238，如此神奇的技术又是怎么回事呢？

![](images/f0259f906ece9e5c5651.png)

**表 3：155 MTr/mm²的第一层放大来自公式口径差异。**

### **238MTr的第二层口径问题：3D footprint effective density，而不是单层制程密度**

MTr/mm²表面上是“每平方毫米百万晶体管”，看似没有等效空间。

但只要进入 3D 堆叠，关键问题就变成，这个平方毫米到底是单层 silicon area，还是封装/芯片俯视 footprint？

传统平面制程密度默认是：D_process = N_transistors / A_single_active_layer

但 3D 堆叠可以写成：D_3D_footprint = (N_bottom + N_top) / A_projected_footprint

如果上下两层 active logic 疊在同一个俯视面积内，分子增加，分母不变，MTr/mm²自然提高。这个数不是假的，但它已经不是传统意义上的单层制程节点密度。

用华为自己的 155→238 来反推：提升比例 = 238 / 155 ≈ 1.535× 。增加量 = 238 − 155 = 83 MTr/mm²

如果上层逻辑密度也按华为口径为 155，则需要覆盖底层 footprint 的比例为：f = 83 / 155 ≈ 53.5%

也就是说，如果上层是同密度逻辑，它大约只覆盖了底层 footprint 的一半多。如果上层覆盖整个 footprint，那么上层平均密度约 83 MTr/mm²。

这都不像“完整高性能计算 die 叠完整高性能计算 die”，而更像局部 critical-path gates、NoC、SRAM 周边、clock、control、I/O 或支援逻辑的选择性 folding。

再把华为公式还原到Mark Bohr口径：

155 / 1.357 ≈ 114.2 MTr/mm²

238 / 1.357 ≈ 175.4 MTr/mm²

所以所谓 238，本质上更像“Bohr 约 175 MTr/mm²的 3D footprint 有效密度”，不是 SMIC N+3 单层物理密度突然变成 238。

**何论文的 3D 堆叠不是新物理路线：产业早已有大量对应案例**

何论文把 LogicFolding 作为韬定律的核心 proof point，但从产业分类看，它属于 active-tier stacking / logic-on-logic / SRAM-on-logic / memory-on-logic / active base die + compute chiplet 的大类。

我不清楚最终kirin 2026芯片上的堆叠式堆了什么，但离不开上述范畴，这些技术与方向全部都不是华为独创。

区别只在于何文宣称它在手机 SoC 的关键路径上做到了更细粒度的 cell/path-level folding，但公开论文没有给出版图、拆解或第三方验证。

![](images/a3f7c6e920979a202bef.png)

表 4：何论文的堆叠方式在全球产业中早以大量落地并非新技术。

### **AMD 3D V-Cache 是最直观的反例：若按何文口径，MTr/mm²也能大幅提高**

以 AMD 3D V-Cache 为例，公开资料显示 Ryzen 7 5800X3D 的 7nm CCD 面积约 80.7mm²、晶体管约 4.15B。

上层 3D V-Cache die 面积约 41mm²、晶体管约 4.7B。正常单层 CCD 口径为：D_CCD = 4.15B / 80.7mm² ≈ 51.4 MTr/mm²

如果按何文式 3D footprint 口径，把上层 V-Cache 晶体管也算入 CCD 俯视 footprint：D_footprint = (4.15B + 4.7B) / 80.7mm² ≈ 109.7 MTr/mm²

提升比例为：109.7 / 51.4 ≈ 2.13× 。这比华为 155→238 的 1.535×还高。

但 AMD 根本不会说“我们的7nm CCD 等效变成 3nm”。因为行业清楚这只是 SRAM cache die 叠在 CPU CCD 上，提升的是缓存容量、局部数据访问、性能和功耗，而不是 CPU 逻辑制程密度。

如果改用 total silicon area，把上下 die 面积都算进成本和晶圆消耗：D_total_silicon = (4.15B + 4.7B) / (80.7 + 41)mm² ≈ 72.7 MTr/mm²

![](images/70b478d5e78b036d3523.png)

**表 5：同一颗 AMD 3D V-Cache 芯片，不同口径下 MTr/mm²差异巨大。**

### **如果同样口径给台积电 N5/N3**

何的论文的问题不在于“用等效密度”本身，而在于只把等效口径用于华为自身，而不用同等口径与其他竞品相比，有明显的断章取义嫌疑。即便何在论文中提供了其计算公式。

如果允许华为把公式放大和 3D footprint 合并进 MTr/mm²，那么台积电 N5/N3 也应当用同样口径重算。

以常见公开估算为例，TSMC N5 的 Bohr 类逻辑密度约 137.6 MTr/mm²，N3B/N3E/N3P 可粗略使用约 197/216/224 MTr/mm²作为示意。仅把公式换成华为口径，即乘以 1.357，就得到：

![](images/0d09ba1f5d4bd73785bf.png)

**表 6：只换公式口径，TSMC N3 的“华为式 MTr/mm²”已明显高于 238。**

**
**

如果再套用何文 155→238 的 LogicFolding 增益，也就是华为做到238的算法对应：

LogicFolding 增益 = 238 / 155 ≈ 1.535

![](images/e9442db89770e65e04a2.png)

表 7：若全球领先节点也用同一等效口径，华为 238 MTr/mm²只有台积电3nm的一半，反推依然是台积电7nm优化版的水平。

**
**

这个表不是说台积电会这样宣传，而是说明：等效口径必须对所有玩家一致。不能只允许华为把 3D 堆叠、封装、系统优化算进 MTr/mm²，却不允许台积电、AMD、NVIDIA、Intel、三星、SK hynix 用相同口径重算。

### **韬定律的真正问题：讲 τ 时合理，讲 MTr/mm²和 1.4nm 时混淆**

**原文摘录：**“τ is a time law, not a joule law. A super-node operating 10× faster but with 10× greater power consumption violates no scaling principle, yet exceeds grid capacity.”

**问题指出：这段原文其实非常重要：τ scaling 只管时间，不自动解决功耗、供电、散热、成本和良率。把 τ 改善直接宣传成等效先进节点，会掩盖这些硬约束。**

**原文摘录：**“Full-scale LogicFolding requires the toolchain to treat multiple stacked dies as a single continuous design entity — partitioning logic at cell granularity rather than block granularity...”

**问题指出：原文承认全规模 LogicFolding 需要全新的 3D-native EDA、跨 die timing closure、inter-wafer variation 处理。这说明它还不是成熟完成品。**

**原文摘录：**“Every hybrid bond and every TSV incurs a finite resistance and capacitance penalty, and TSV KOZ displaces standard cells.”

**问题指出：这是对 3D 堆叠“不是免费午餐”的承认。垂直互联会带来 R/C、KOZ、良率、热和供电问题。**

 这些原文其实足以说明，韬定律不是一个可以把所有系统提升简单相乘、最后换成“等效几纳米”的公式。

它是一套系统工程优化方法。某些场景下，它可以改善延迟、吞吐、能效或 footprint；但如果拿它来替代物理制程差距，就会变成宣传口径。

真正的矛盾在于，理论上，何的论文说不要再看 nm，要看 τ；宣传上，却又把读者最熟悉的 MTr/mm²和 1.4nm 拿出来。

更关键的是，这些 MTr/mm²并非传统制程密度，而是自定义公式 + 3D footprint 的结果。

这就形成了一个非常典型的叙事技巧，当物理节点不占优时，改用系统级口径。当需要传播效果时，又把系统级口径翻译成先进节点听感。巧妙之处就在这里。

### **回到全球产业：每个瓶颈都要突破，但领先者正在全栈推进**

后摩尔时代确实不是只靠先进制程。AI 算力系统至少有五个核心瓶颈：先进制程、先进封装、光互联/电互联、散热/供电、存储/HBM。每一项都必须突破，任何一项短板都会限制最终算力。

![](images/37b5be697816dd378fcb.png)

**表 8：后摩尔时代的竞争是全栈竞争，不是单一“定律”可以抹平。**

**
**

这也是为什么说，韬定律不能被理解为“华为用一条新定律绕过了全球半导体差距”。它更像是华为在先进光刻受限条件下提出的一套补偿性工程路线。

这个路线可以带来局部收益，也可能在某些特定产品上做出漂亮优化。但它并不能改变全球领先者也在用同样甚至更强的工具链、封装平台、HBM 供应链和系统生态快速前进。

英伟达的 GB200/NVL72 本身就是真正系统级 τ 优化：GPU、Grace CPU、NVLink、NVSwitch、HBM、液冷 rack-scale system 共同工作。

AMD MI300 是 compute + active I/O die + HBM 的 3D 异质集成。

台积电 3DFabric/SoIC/CoWoS 正在把先进制程、先进封装、HBM、未来光互联整合成平台。

SK hynix 的 HBM4 则是 AI 记忆体瓶颈的现实突破。

把这些全部放进同一个 τ scaling 口径，全球领先者并不会原地等华为追赶，甚至正在不断拉开差距，华为没办法凭借一个韬定律轻松改变战局。

### **最终结论：韬定律揭示的是系统战，不是差距消失**

韬定律最有价值的一点，是承认后摩尔时代的竞争已经从单一制程节点，转向制程、封装、存储、互联、散热、供电、软件和系统架构的全栈竞争。

何庭波这个判断是对的。今天再只看“几纳米”已经不够，必须看最终系统能把多少算力、带宽、存储和能效组织起来。

但韬定律最大的问题，是把系统级优化的合理性，转化成“等效 MTr/mm²”“等效 1.4nm”的传播口径。

155→238 MTr/mm²经过拆解后，至少被两层放大：

第一，华为公式 2/(CPP×cell height) 相对 Bohr/TechInsights 类公式天然高约 35.7%；

第二，LogicFolding 把上下 active tiers 的晶体管按俯视 footprint 合并计算，使 MTr/mm²从单层制程密度变成 3D footprint effective density。

因此，笔者的判断与结论是：

何庭波论文的 3D 堆叠不是全新的物理路线，而是产业已有的 logic-on-logic、SRAM-on-logic、memory-on-logic、active-base-die stacking、hybrid bonding 等技术方向的华为式整合。

155→238 MTr/mm²不是 SMIC N+3 单层平面制程密度从 155 变成 238，而是华为公式口径下，叠加局部 3D LogicFolding 后的俯视 footprint 有效密度。

如果用同样口径看全球竞争对手，AMD 3D V-Cache、MI300、Intel Foveros、Samsung X-Cube、TSMC SoIC、HBM + GPU package 都可以大幅提高所谓 MTr/mm²。

台积电 N3 若套用华为公式和同等 folding 增益，数字会高达467，远高于论文中kirin 2026的238两倍。这个差距基本也说明kirin 2026的真实物理MTr跟台积电7nm优化版接近，也跟kirin 9030的N+3的110~120接近，脱下面纱之后，一切都还璞归真。

因此，韬定律不能证明华为追平先进制程，也不能证明中西差距缩小。

它真正说明的是，后摩尔时代竞争变成系统战，而在这场系统战中，全球领先供应链仍在制程、封装、HBM、光互联、散热、系统互联等每个环节快速推进。

所以，我们可以承认韬定律作为工程方法论有启发性，也可以承认华为在受限环境下尝试通过 3D 堆叠和系统协同取得增量。

但不能接受把自定义口径包装成“等效先进节点”的宣传。

真正严谨的比较，必须把单层制程密度、3D footprint 有效密度、total silicon area、成本、功耗、散热、良率和系统性能分开。只有这样，才能看清技术进步本身，也才能看清宣传口径背后的“猫腻”。

今天韬定律大火，简短看了几篇文章，全部都是不知所以，晚上看了下论文，一下就看到了最大的问题，那就是何庭波的计算公式，这个基本常识的问题全世界中英文媒体，不论媒体巨擘还是外资投行，没有一个发现，没有一个针对这基本公式去说明，全部胡乱报导一通。

早在上周3nm等效小作文爆炒之后，笔者第一时间就澄清与打假，但是文章几乎发不了，说明这次布局是很精妙且庞大的组织，连续的预热与最终高潮，韬定律是大事件，热度非常高，其实炒一波应该也没问题，不过我是不会去的，还是慢慢等好机会。

回到半导体行业，我一直反覆强调你搞不明白那就是定义与口径出现问题，永远就只有这问题，只要统一口径与定义，半导体还是那个半导体，不会有弯道超车，更不会有莫名其妙的进步，全部都是脚踏实地的一步一脚印，这才叫科学，这才叫产业。

        从何庭波论文的 τ scaling、155→238 MTr/mm²、LogicFolding 到“等效 1.4nm”的口径拆解

何庭波论文提出的“韬定律”（τ scaling）在工程方向上抓住了后摩尔时代的真实问题，先进制程之外，封装、互联、存储、供电、散热、系统架构都会限制最终算力。

但论文最值得警惕的地方，是把“时间常数 τ”的系统级优化，与“155→238 MTr/mm²”“2031 年等效 1.4nm”等最容易被公众理解为先进制程节点的指标混在一起。

拆开公式和口径后可以看到，所谓 238 MTr/mm²并不是SMIC N+3 的单层物理逻辑密度，而是华为公式口径叠加 3D 俯视 footprint 后得到的有效密度。

笔者这篇文章的目的不是否定 3D 堆叠、先进封装、光互联、存储融合这些技术方向。恰恰相反，这些方向是全球半导体工业正在共同推进的真实方向。

本文要指出的是，如果华为可以用自定义公式、3D footprint、系统级 τ 优化来宣称“等效 MTr/mm²”和“等效 1.4nm”，那么台积电、英伟达、AMD、Intel、三星、SK hynix 等全球领先者同样可以用相同口径重算，而且海外这些技术大部分早已经在商业产品中量产落地，而不是论文。

### **何庭波论文的要点：从空间缩微转向时间缩微**

**原文摘录：**“This perspective argues for a successor scaling principle — τ scaling — that adopts time itself, rather than transistor area, as the primary metric of progress...”

**问题指出：这句话是论文的理论核心：用时间 τ 替代面积或节点作为进步指标。这个方向本身有工程意义，但它不是一条可直接换算为“几纳米”的物理定律，但他的宣传却全部挂勾了几纳米多少MTr。**

何文首先指出，过去半导体行业靠摩尔定律和 Dennard scaling 前进，晶体管变小、频率提高、单位逻辑门成本下降。

但 2005 年前后 Dennard scaling 失效，电压不再随尺寸等比例下降。7nm 以后，局部互连 RC、EUV 折旧、掩膜成本、设计规则复杂度开始吞噬几何缩微收益。

论文特别强调，对于华为这样前段光刻受限的企业，不能再假设“下一代节点会自然解决问题”。

因此论文提出，半导体进步的主指标不应再只是空间尺寸，而应是跨层时间常数 τ。论文把 τ 分解为晶体管、电路、芯片、系统四层：

τ = f(τ_transistor, τ_circuit, τ_chip, τ_system)

这套框架的普通解释是：晶体管开关要快，电路关键路径要短，芯片内部访问存储要快，系统之间传输数据也要快。

最终用户看到的不是“某根线宽多少纳米”，而是应用响应更快、吞吐更高、功耗更低。

这部分既合情有合理，也是全球半导体行业早在进行的方向。今天 AI 数据中心的瓶颈早已不是单一芯片峰值算力，而是 HBM 带宽、片间互联、机柜互联、供电、散热、封装良率和软件调度的综合结果。

而且全世界整个供应链早都在解决上述问题，英伟达供应链的台积电，海力士，光模块，CPO，PCB，液冷，服务器电源与机柜这些热点题材都炒了多少年了？

而何的论文问题在于，论文后面又用 MTr/mm²和“等效 1.4nm”来对外表述，导致“时间缩微”与“制程缩微”的语义被混在一起。宣传演讲也着重MTr跟等效1.4nm这些博眼球的数据，韬定律得核心『时间』被抛在脑后。

![](images/7e66e4b258f8740da222.png)

**表 1：韬定律按层级拆解后，并不是全新物理路线，而是把全球产业正在做的系统级优化统一包装成 τ scaling。**

### **论文最核心的实证：LogicFolding 与 Kirin 2026（9050) 的 155→238 MTr/mm²**

**原文摘录：**“Transistor density rose step-wise from 155 to 238 MTr/mm² in a single generation (transistor density is calculated using the formula 2/(CPP*cell height); the area utilization of Kirin SoC design is 68%)...”

**问题指出：这是全文最容易被误读的地方。原文直接写 transistor density 和 MTr/mm²，但同时又承认这是固定节点下通过三维拓扑重组得到的提升。它不应被理解为 SMIC N+3 单层平面制程密度变成 238 MTr/mm²。**

**原文摘录：**“These gains were achieved at a fixed device node, obtained not through a new lithography step but through a topological reorganization of the spatial distribution of logic in three dimensions.”

**问题指出：这句话实际已经说明：238 MTr/mm²不是新光刻节点带来的平面物理密度，而是三维重组后的有效密度。**

**原文摘录：**“The LogicFolding implementation shipping in Kirin 2026 is deliberately conservative... folding was applied selectively along key critical paths rather than across the entire design.”

**问题指出：原文自己承认 Kirin 2026(9050) 不是整颗芯片全面折叠，而是选择性应用在关键路径。这进一步说明 155→238 不能被当作整个制程节点的平面密度跃迁。**

按照论文描述，LogicFolding 不是简单把两个完整 CPU 或 GPU 计算 die 上下叠起来，而是把 digital、analog、memory circuits 分配到垂直堆叠的 active tiers 中，尤其把 critical-path gates、NoC data path、SRAM 关键路径、clock network 等放到上下两层之间重新布局。

论文给出的工艺/封装参数包括：hybrid bonding pitch 1.5μm，目标 gear ratio 接近 1；overlay accuracy 小于 0.5μm；TSV CD/KOZ 小于 1.5μm；TSV pitch 小于 6μm；failure rate 小于 100ppm，repair rate 99.9%。这些参数说明它确实是一种先进 3D active-tier 堆叠能力，但不是一条全新的物理路线或者技术。

很多人讨论这组数据的hybrid bonding pitch 1.5μm达到国际最领先水平，目前台积电SoIC-X-W的官方规格是 <3μm。这个数据被国内许多网友引用，超越了台积电。

目前台积电的SoIC技术可支持hybrid bonding solution SoIC capable of 0.9μm pitch，这里会有几个问题，首先是良率，这数字任何厂家都是谜，不论是台积电或者是华为。

再来是台积电虽然可能有更强的sub-μm HB能力，但目前也没听到有哪家客户采用，所以Kirin 2026（9050)有可能是全球混合键合pitch最小的芯片。

也就是说华为LogicFolding技术在某些参数上确实已进入世界领先集团。

华为在混合键合领域是在全球领先集团。我想这部分国内可以买到BESI的100nm accuracy HB system等最先进混合键合设备，自然不会差。

1.5μm跟目前全球领先的2μm以下可能更高一点但也基本大家属于同一水平，未来再混合键合领域的sub-μm HB能力也将是一个重要观察指标。

但最小pitch是可以靠高成本方案去争取的，所以除了pitch以外，我们还得看良率以及througput吞吐量，低良率以及低吞吐量也可以不计代价缩小pitch但不具备经济性。

另外华为公布的overlay accuracy 小于 0.5μm 跟1.5μm的pitch相比比例过大，IMEC的2μm的pitch对应0.35μm套刻精度完全在合理的control window内，华为的0.5μm套刻精度对应1.5μm的pitch确实不太合乎半导体制程比例。

总而言之，华为hybrid bonding pitch 1.5μm绝对是国际领先水平，但这数字可能无法改变太多，毕竟它只是芯片诸多制程中的一个混合键合工艺，再其中的一个重要参数之一。对于改变整个芯片性能无疑是杯水车薪。

全世界都在混合键合，大家的设备相同，研发时间也差不多，所以pitch差距不会太大，但芯片怎堆叠，可不只是pitch这么简单，在先进封装这个领域，我们与全球的差距大约还有两年左右的时间。

![](images/a0b0c7161e24c9fe22b3.png)

**表 2：何文 LogicFolding 参数与本文解读。**

### **155MTr的第一层口径问题：华为的公式天然比Mark Bohr密度公式高约 35.7%**

这是何庭波论文中最具争议的部分。但很可惜全球所有中英文专业或不专业的媒体，无一看出。只有笔者在阅读何的论文之后发现这个问题以及后续衍生出的疑点。
何在论文中直接给出 transistor density 计算公式：D_Huawei = 2 × 10^6 / (CPP_nm × CellHeight_nm)
但行业常见的Mark Bohr 逻辑密度公式却是：D_Bohr = 1.474 × 10^6 / (CPP_nm × CellHeight_nm)
这里出现了最大的争议点之一，两者比值为：D_Huawei / D_Bohr = 2 / 1.474 ≈ 1.357倍
也就是说，在同一组 CPP 和 cell height 下，只要换成华为公式，MTr/mm²数字就会天然高约 35.7%。
所以155与238MTr，这不是华为制程突然变先进，而是计算公式的的系数压根不同所致。
假设 SMIC N+3 的某组尺寸可以用 CPP=57nm、cell height=228nm 近似演示，则：
D_Bohr = 1.474 × 10^6 / (57 × 228) ≈ 113.4 MTr/mm²D_Huawei = 2 × 10^6 / (57 × 228) ≈ 153.9 MTr/mm²
上述两组数字，就解释了去年TechInsights 对 Kirin 9030 / SMIC N+3 的拆解报告中计算出7nm的N+3制程 MTr为110~120，如今何庭波的论文没有来由的增加到155。
155这数字一出让整个行业感到莫名其妙，毕竟N+3得明年才能换代，2026年的制程跟2025是一样的。而且明年即便N+4也到不了155。
主要原因就是这155 压根不是TechInsights或行业里采用的Bohr密度公式的口径，而是华为自己的口径（何庭波论文明确计算公式）。
这就是解释了为何，没有任何理由MTr忽然间大增的原因，其实还是去年那个MTr 110～120的N+3。
在N+3的基础上透过自定义公式放大MTr，再加上上述的LogicFolding逻辑折叠技术，何庭波的论文称进一步把MTr提升到238，如此神奇的技术又是怎么回事呢？

![](images/f0259f906ece9e5c5651.png)

**表 3：155 MTr/mm²的第一层放大来自公式口径差异。**

### **238MTr的第二层口径问题：3D footprint effective density，而不是单层制程密度**

MTr/mm²表面上是“每平方毫米百万晶体管”，看似没有等效空间。

但只要进入 3D 堆叠，关键问题就变成，这个平方毫米到底是单层 silicon area，还是封装/芯片俯视 footprint？

传统平面制程密度默认是：D_process = N_transistors / A_single_active_layer

但 3D 堆叠可以写成：D_3D_footprint = (N_bottom + N_top) / A_projected_footprint

如果上下两层 active logic 疊在同一个俯视面积内，分子增加，分母不变，MTr/mm²自然提高。这个数不是假的，但它已经不是传统意义上的单层制程节点密度。

用华为自己的 155→238 来反推：提升比例 = 238 / 155 ≈ 1.535× 。增加量 = 238 − 155 = 83 MTr/mm²

如果上层逻辑密度也按华为口径为 155，则需要覆盖底层 footprint 的比例为：f = 83 / 155 ≈ 53.5%

也就是说，如果上层是同密度逻辑，它大约只覆盖了底层 footprint 的一半多。如果上层覆盖整个 footprint，那么上层平均密度约 83 MTr/mm²。

这都不像“完整高性能计算 die 叠完整高性能计算 die”，而更像局部 critical-path gates、NoC、SRAM 周边、clock、control、I/O 或支援逻辑的选择性 folding。

再把华为公式还原到Mark Bohr口径：

155 / 1.357 ≈ 114.2 MTr/mm²

238 / 1.357 ≈ 175.4 MTr/mm²

所以所谓 238，本质上更像“Bohr 约 175 MTr/mm²的 3D footprint 有效密度”，不是 SMIC N+3 单层物理密度突然变成 238。

**何论文的 3D 堆叠不是新物理路线：产业早已有大量对应案例**

何论文把 LogicFolding 作为韬定律的核心 proof point，但从产业分类看，它属于 active-tier stacking / logic-on-logic / SRAM-on-logic / memory-on-logic / active base die + compute chiplet 的大类。

我不清楚最终kirin 2026芯片上的堆叠式堆了什么，但离不开上述范畴，这些技术与方向全部都不是华为独创。

区别只在于何文宣称它在手机 SoC 的关键路径上做到了更细粒度的 cell/path-level folding，但公开论文没有给出版图、拆解或第三方验证。

![](images/a3f7c6e920979a202bef.png)

表 4：何论文的堆叠方式在全球产业中早以大量落地并非新技术。

### **AMD 3D V-Cache 是最直观的反例：若按何文口径，MTr/mm²也能大幅提高**

以 AMD 3D V-Cache 为例，公开资料显示 Ryzen 7 5800X3D 的 7nm CCD 面积约 80.7mm²、晶体管约 4.15B。

上层 3D V-Cache die 面积约 41mm²、晶体管约 4.7B。正常单层 CCD 口径为：D_CCD = 4.15B / 80.7mm² ≈ 51.4 MTr/mm²

如果按何文式 3D footprint 口径，把上层 V-Cache 晶体管也算入 CCD 俯视 footprint：D_footprint = (4.15B + 4.7B) / 80.7mm² ≈ 109.7 MTr/mm²

提升比例为：109.7 / 51.4 ≈ 2.13× 。这比华为 155→238 的 1.535×还高。

但 AMD 根本不会说“我们的7nm CCD 等效变成 3nm”。因为行业清楚这只是 SRAM cache die 叠在 CPU CCD 上，提升的是缓存容量、局部数据访问、性能和功耗，而不是 CPU 逻辑制程密度。

如果改用 total silicon area，把上下 die 面积都算进成本和晶圆消耗：D_total_silicon = (4.15B + 4.7B) / (80.7 + 41)mm² ≈ 72.7 MTr/mm²

![](images/70b478d5e78b036d3523.png)

**表 5：同一颗 AMD 3D V-Cache 芯片，不同口径下 MTr/mm²差异巨大。**

### **如果同样口径给台积电 N5/N3**

何的论文的问题不在于“用等效密度”本身，而在于只把等效口径用于华为自身，而不用同等口径与其他竞品相比，有明显的断章取义嫌疑。即便何在论文中提供了其计算公式。

如果允许华为把公式放大和 3D footprint 合并进 MTr/mm²，那么台积电 N5/N3 也应当用同样口径重算。

以常见公开估算为例，TSMC N5 的 Bohr 类逻辑密度约 137.6 MTr/mm²，N3B/N3E/N3P 可粗略使用约 197/216/224 MTr/mm²作为示意。仅把公式换成华为口径，即乘以 1.357，就得到：

![](images/0d09ba1f5d4bd73785bf.png)

**表 6：只换公式口径，TSMC N3 的“华为式 MTr/mm²”已明显高于 238。**

**
**

如果再套用何文 155→238 的 LogicFolding 增益，也就是华为做到238的算法对应：

LogicFolding 增益 = 238 / 155 ≈ 1.535

![](images/e9442db89770e65e04a2.png)

表 7：若全球领先节点也用同一等效口径，华为 238 MTr/mm²只有台积电3nm的一半，反推依然是台积电7nm优化版的水平。

**
**

这个表不是说台积电会这样宣传，而是说明：等效口径必须对所有玩家一致。不能只允许华为把 3D 堆叠、封装、系统优化算进 MTr/mm²，却不允许台积电、AMD、NVIDIA、Intel、三星、SK hynix 用相同口径重算。

### **韬定律的真正问题：讲 τ 时合理，讲 MTr/mm²和 1.4nm 时混淆**

**原文摘录：**“τ is a time law, not a joule law. A super-node operating 10× faster but with 10× greater power consumption violates no scaling principle, yet exceeds grid capacity.”

**问题指出：这段原文其实非常重要：τ scaling 只管时间，不自动解决功耗、供电、散热、成本和良率。把 τ 改善直接宣传成等效先进节点，会掩盖这些硬约束。**

**原文摘录：**“Full-scale LogicFolding requires the toolchain to treat multiple stacked dies as a single continuous design entity — partitioning logic at cell granularity rather than block granularity...”

**问题指出：原文承认全规模 LogicFolding 需要全新的 3D-native EDA、跨 die timing closure、inter-wafer variation 处理。这说明它还不是成熟完成品。**

**原文摘录：**“Every hybrid bond and every TSV incurs a finite resistance and capacitance penalty, and TSV KOZ displaces standard cells.”

**问题指出：这是对 3D 堆叠“不是免费午餐”的承认。垂直互联会带来 R/C、KOZ、良率、热和供电问题。**

 这些原文其实足以说明，韬定律不是一个可以把所有系统提升简单相乘、最后换成“等效几纳米”的公式。

它是一套系统工程优化方法。某些场景下，它可以改善延迟、吞吐、能效或 footprint；但如果拿它来替代物理制程差距，就会变成宣传口径。

真正的矛盾在于，理论上，何的论文说不要再看 nm，要看 τ；宣传上，却又把读者最熟悉的 MTr/mm²和 1.4nm 拿出来。

更关键的是，这些 MTr/mm²并非传统制程密度，而是自定义公式 + 3D footprint 的结果。

这就形成了一个非常典型的叙事技巧，当物理节点不占优时，改用系统级口径。当需要传播效果时，又把系统级口径翻译成先进节点听感。巧妙之处就在这里。

### **回到全球产业：每个瓶颈都要突破，但领先者正在全栈推进**

后摩尔时代确实不是只靠先进制程。AI 算力系统至少有五个核心瓶颈：先进制程、先进封装、光互联/电互联、散热/供电、存储/HBM。每一项都必须突破，任何一项短板都会限制最终算力。

![](images/37b5be697816dd378fcb.png)

**表 8：后摩尔时代的竞争是全栈竞争，不是单一“定律”可以抹平。**

**
**

这也是为什么说，韬定律不能被理解为“华为用一条新定律绕过了全球半导体差距”。它更像是华为在先进光刻受限条件下提出的一套补偿性工程路线。

这个路线可以带来局部收益，也可能在某些特定产品上做出漂亮优化。但它并不能改变全球领先者也在用同样甚至更强的工具链、封装平台、HBM 供应链和系统生态快速前进。

英伟达的 GB200/NVL72 本身就是真正系统级 τ 优化：GPU、Grace CPU、NVLink、NVSwitch、HBM、液冷 rack-scale system 共同工作。

AMD MI300 是 compute + active I/O die + HBM 的 3D 异质集成。

台积电 3DFabric/SoIC/CoWoS 正在把先进制程、先进封装、HBM、未来光互联整合成平台。

SK hynix 的 HBM4 则是 AI 记忆体瓶颈的现实突破。

把这些全部放进同一个 τ scaling 口径，全球领先者并不会原地等华为追赶，甚至正在不断拉开差距，华为没办法凭借一个韬定律轻松改变战局。

### **最终结论：韬定律揭示的是系统战，不是差距消失**

韬定律最有价值的一点，是承认后摩尔时代的竞争已经从单一制程节点，转向制程、封装、存储、互联、散热、供电、软件和系统架构的全栈竞争。

何庭波这个判断是对的。今天再只看“几纳米”已经不够，必须看最终系统能把多少算力、带宽、存储和能效组织起来。

但韬定律最大的问题，是把系统级优化的合理性，转化成“等效 MTr/mm²”“等效 1.4nm”的传播口径。

155→238 MTr/mm²经过拆解后，至少被两层放大：

第一，华为公式 2/(CPP×cell height) 相对 Bohr/TechInsights 类公式天然高约 35.7%；

第二，LogicFolding 把上下 active tiers 的晶体管按俯视 footprint 合并计算，使 MTr/mm²从单层制程密度变成 3D footprint effective density。

因此，笔者的判断与结论是：

何庭波论文的 3D 堆叠不是全新的物理路线，而是产业已有的 logic-on-logic、SRAM-on-logic、memory-on-logic、active-base-die stacking、hybrid bonding 等技术方向的华为式整合。

155→238 MTr/mm²不是 SMIC N+3 单层平面制程密度从 155 变成 238，而是华为公式口径下，叠加局部 3D LogicFolding 后的俯视 footprint 有效密度。

如果用同样口径看全球竞争对手，AMD 3D V-Cache、MI300、Intel Foveros、Samsung X-Cube、TSMC SoIC、HBM + GPU package 都可以大幅提高所谓 MTr/mm²。

台积电 N3 若套用华为公式和同等 folding 增益，数字会高达467，远高于论文中kirin 2026的238两倍。这个差距基本也说明kirin 2026的真实物理MTr跟台积电7nm优化版接近，也跟kirin 9030的N+3的110~120接近，脱下面纱之后，一切都还璞归真。

因此，韬定律不能证明华为追平先进制程，也不能证明中西差距缩小。

它真正说明的是，后摩尔时代竞争变成系统战，而在这场系统战中，全球领先供应链仍在制程、封装、HBM、光互联、散热、系统互联等每个环节快速推进。

所以，我们可以承认韬定律作为工程方法论有启发性，也可以承认华为在受限环境下尝试通过 3D 堆叠和系统协同取得增量。

但不能接受把自定义口径包装成“等效先进节点”的宣传。

真正严谨的比较，必须把单层制程密度、3D footprint 有效密度、total silicon area、成本、功耗、散热、良率和系统性能分开。只有这样，才能看清技术进步本身，也才能看清宣传口径背后的“猫腻”。

今天韬定律大火，简短看了几篇文章，全部都是不知所以，晚上看了下论文，一下就看到了最大的问题，那就是何庭波的计算公式，这个基本常识的问题全世界中英文媒体，不论媒体巨擘还是外资投行，没有一个发现，没有一个针对这基本公式去说明，全部胡乱报导一通。

早在上周3nm等效小作文爆炒之后，笔者第一时间就澄清与打假，但是文章几乎发不了，说明这次布局是很精妙且庞大的组织，连续的预热与最终高潮，韬定律是大事件，热度非常高，其实炒一波应该也没问题，不过我是不会去的，还是慢慢等好机会。

回到半导体行业，我一直反覆强调你搞不明白那就是定义与口径出现问题，永远就只有这问题，只要统一口径与定义，半导体还是那个半导体，不会有弯道超车，更不会有莫名其妙的进步，全部都是脚踏实地的一步一脚印，这才叫科学，这才叫产业。

        
                
                

![](/assets_dweb/logo@1x.png)

                知识星球
                
        
        
            
            扫码加入星球
            查看更多优质内容
        
        https://wx.zsxq.com/mweb/views/joingroup/join_group.html?group_id=88888812815442

---

Source: https://articles.zsxq.com/id_auilmhcopq3p.html

Linked from topic_id: 14422422222852122
