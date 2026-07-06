# 韬定律与 Kirin 9050 最終修正

        
            [来自：
                半导体大佬的会议室](https://wx.zsxq.com/group/88888812815442)
        
        
            
                

![](images/39ac34f1b548792d9368.jpg)

                吴梓豪leslie
            
            2026年05月28日 18:38
        
        
            本文在前文基础上，修改logic + SRAM hybrid 上层 die並加入 3.1GHz 峰值频率条件，并重新审视 logic + SRAM hybrid 上层 die 在手机 AP 热约束下是否成立。

结论是可以成立，但必须非常保守。

上层 die 不能变成高活性 compute layer，也不应做 40–60mm² 大面积高带宽 SRAM。更合理的是 30–34mm² 的 active hybrid die，其中 SRAM/buffer 约 16–22mm²，低切换率 logic 约 8–12mm²。

**
**

昨天的文章『华为韬定律解读-2』笔者给了一个9050设计思路，主要是思考，性能提升幅度，发热与相关功能布局，大概得出下层die维持之前120~130mm2的面积，上层die需要40mm2的面积来放SRAM，经过许多同学提醒，我重新再看一下韬定律，确实何庭波的韬定律论文针对logicfloding的阐述並非单纯SRAM on logic也包含了logic。

何的论文描述：digital、analog、memory circuits 被分配到上下 active tiers；critical-path gates 可跨上下层分布；NoC data path、clock network、SRAM path 都可做 folding。这说明它不是单纯 AMD 式 SRAM-on-logic。

不过logic on logic或者SRAM on logic的工艺本质没有不同，核心都是3D工艺这套东西，减薄、CMP、HB、铜铜连接、介电层键合、TSV、KGD测试跟热与机械可靠性。

从hybrid bonding的互联来看，并不会因为上面接的是SRAM cell或者standard cell logic就变得不一样。 

不过设计难度确实会有不同，纯SRAM上层是一块规则的记忆体阵列，结构一致，可分bank，可冗余修复，重点是热均匀，所以设计上难度较低，而但纯logic的话又不现实，因为热的问题，可放在上层的logic很有限，大概只有10mm2即可，这样一来面积提升太小了，又无法达成华为官方的性能提升幅度。

所以吹上层全 logic、全球唯一新物理，制程新突破，这也没有道理，对于热来说更不现实。

在细读何论文这部分的阐述，同时提到 SRAM bit-line / word-line critical path、SRAM operating frequency 提升，且明确说 Kirin 2026 是 conservative implementation，只在 key critical paths selective folding，不是整颗 SoC 任意拆分。

所以最准确表述是，Kirin 9050 更可能是 mixed active-tier folding，上层包含低热 logic + SRAM / memory path / NoC / clock buffer，而非纯 SRAM，也非完整高热 logic die。

所以笔者针对更为收敛的定义，重新调整设计思路，下层保留 CPU/GPU/NPU 主运算，上层缩小到约 30–34mm²，放 16–22mm² SRAM/buffer 和 8–12mm² 低热 logic。

这既符合 LogicFolding 官方语义，也更符合手机 AP 对散热的严苛限制。

**3.1GHz 条件支持保守 logic + SRAM hybrid**

目前关于 Kirin 2026 / 9050 的 3.1GHz 说法，我在和的論文以及華為官方資料中沒找到，而是来自外部对华为 LogicFolding 路线图与媒体报道的整理。

我认为比较可信的口径是：Kirin 2026 / 9050 的最大频率提升约 12.7%，对应上一代 Kirin 9030 Pro 约 2.75GHz 的大核频率，计算结果接近 3.1GHz。

![](images/552be145abca16bb3eda.png)

这个 3.1GHz 条件很关键。

昨天的纯 SRAM 上层 die佈局主要改善 cache miss、外存访问与 sustained performance，对 CPU 峰值频率的直接帮助有限。

CPU 从 2.75GHz 到 3.1GHz，更需要 clock tree、critical path、local interconnect、skew tuning、PDN 和电压频率曲线改善。

因此，若 3.1GHz 口径成立，它反而支持上层存在少量低热 logic，而不是纯 SRAM die。

但这也不意味着上层可以放高功耗逻辑。手机 AP 的热条件极其严苛，上层 logic 只能是 clock / NoC / cache controller / QoS / DFT / thermal control 这类低切换率模块。

CPU core、GPU shader、NPU MAC、GPU L1、NPU L0 这类高热单元還是必须留在下层。

**
**

**重新审视散热：同面积下 hybrid 比纯 SRAM 更容易产生热点**

此前我们从“纯 3D SRAM”推到“logic + SRAM hybrid”。现在必须更严格地审视手机散热。

结论是：同面积、同工作强度下，logic + SRAM hybrid 的局部热风险高于纯 SRAM。

SRAM 虽然也有读写动态功耗和漏电，但它结构规则、bank 化容易、power gating 容易；logic 的切换率不均匀，某些 router、clock buffer、DMA 控制或 compression 逻辑可能形成局部热斑。

![](images/c2010e9a87c92ee1ab59.png)

 

因此，hybrid 方案不是因为“logic 更冷”，而是因为它可以把上层 active die 面积压小，避免 40–60mm² 的大 SRAM die 覆盖下层热区。

真正可行的逻辑是：少量低热 logic + 中等容量 SRAM/buffer，而不是更大容量SRAM。

**
**

**最终保守设计：下层扩大， 上层缩小；下层算，上层修路径和暂存**

在 3.1GHz 和手机散热约束加入后，Kirin 9050 的最合理设计应从此前 36–40mm² 上层 die 收缩到30-34mm2。

新的设计如下：

![](images/86ac0941577b53f6db28.png)

这套设计的核心不是上层加了logic代表它也在算，而是上层修关键路径、缩短部分互连、改善 clock skew、管理中等容量 SRAM/buffer。下层才是 CPU/GPU/NPU/ISP 的主运算层。

**
**

**上层 SRAM 容量重算：不再追求 40–50MB，而是 18–25MB 可用**

沿用此前的密度口径：上层 83 MTr/mm² 为未换算口径，若除以 1.357，则约为 61.16 MTr/mm²。若按 6T SRAM 换算，约为 1.27MB/mm² raw SRAM。

公式：83 ÷ 1.357 ≈ 61.16 MTr/mm²；61.16 ÷ 6 ÷ 8 ≈ 1.27MB/mm²。

![](images/0313f89a0774ba94d762.png)

 

这个结果意味着，新版 Kirin 9050 不是我们昨天规划的手机版 3D V-Cache 大 cache，而更像是“中等容量 3D staging memory + 低热 logic folding”。

它不追求用 40–50MB 上层 SRAM 解决所有问题，而是选择关键路径和关键场景做补偿。

### **3.1GHz 如何实现：更像 critical path 与 clock 优化**

若 Kirin 9030 Pro 的 P 核峰值约 2.75GHz，Kirin 9050 提高到 3.1GHz，本质是约 12.7% 的峰值频率提升。这没有跨代的飞跃，中规中矩的提升，但对同样是SMIC N+3制程而言已经不容易。

![](images/d0fb63ca4eb8e9e75fbe.png)

 

这也解释为什么纯 SRAM 上层不够。纯 SRAM 有助于减少 DRAM 访问、提升 GPU/NPU/ISP sustained efficiency，但不能充分解释 P 核峰值频率 +12.7%。因此，保守的 logic + SRAM hybrid 更符合 3.1GHz 条件。

**
**

**GPU/NPU 官方提升如何对应新版设计**

华为图示的 GPU +38%、GPU 能效 +40%、NPU +140%、NPU 能效 +81%，不能由 30–34mm² 上层 hybrid die 单独实现。上层只是降低数据搬移与关键路径成本，真正主增量仍应来自下层 GPU/NPU 扩大、低精度计算、压缩和软件协同。

![](images/7f4974bc6ce3ee9c95fd.png)

 

新版设计与官方提升能对上，但必须强调，上层不是全部性能来源。

尤其 NPU +140% 绝不可能单靠上层 SRAM 或少量 logic 实现，它一定需要下层 NPU 本体、低精度、稀疏和 runtime 同时提升。

**logic + SRAM hybrid 上层 die的设计能满足手机AP的高散热要求吗？**

笔者认为整体设计方向基本上是适合的，但仅限于非常保守上die较小面积的形态。

不过最终上层hybrid die的面积到底是多大，这就取决于海思的设计能力了，总而言之本质上都是面积的问题，面积大小涉及了性能与热管理的平衡，目前坊间夸大的独一无二的设计思路肯定是有帮助但这只是优化改变不了物理本质。

根据所有条件的不断收敛，笔者认为最合理的kirin 9050，它不是 3D compute stacking，也不是大面积 cache stacking，而是“有限面积、低热 logic、中等 SRAM、场景化启用”的折中方案。

下面表格就是华为想要在手机AP实现它宣称的性能提升所有满足或者说克服的条件，这些条件的达成代表华为下了很大的工夫与成本去不断打磨kirin芯片。

9050百分百是一款好产品，也有一些唯一性的技术应用落地，但这个唯一性不是因为技术别人达不到，而是别人有更低成本的方案。

所以这里面并没有看到什么突破性的技术出现，大家还是得客观看待。

对于9050的出现与落地必然是要给华为一个大大的肯定，这真的是花了大代价获得的，但不应该把这些设计上或制程上的不同说成世界唯一的突破，这样说并不科学也夸大了。

![](images/ccf4b2db78a9f0563cbc.png)

 

**理性看待所谓全球唯一，这仍然是高成本补课，不是新物理**

坊间一个常见说法是，LogicFolding 需要重新开发 EDA，所以它是全球唯一、前所未有的新技术。这个说法并非小作文但真的需要降温。

因为这类把应该做的事，上纲上线，寻找一些非核心的不同，利用一大堆技术术语不断地引导不懂的普通群众并不妥当，大家回想一下这几天韬定律发表后，从一开始铺天盖地的神话般吹捧，重新定义半导体，然后被不断科普后一直在降低规格，不断都缩限可宣传的点，大家从这两天我发表韬定律文章以来，每天同学们发小作文来让我澄清点的越来越细枝末节可以看出。

这还没算上，上周那个N+3堆叠N+2达到等效3nm的铺天盖地预热小作文，一切看得出来都是有计划的。

就EDA这事来说，半导体行业任何新的制程、新的封装、新的设计规则、新的 PDK、新的互连模型、新的可靠性要求，都需要 EDA 工具链配合。

EDA 本身不是神秘魔法。开发某一类新设计流程所需的工具、规则、脚本、模型、验证方法，并不等于在全球半导体体系之外开辟了一个新宇宙。

真正难的不是“写一个 EDA 工具”本身，而是经过长期产品迭代、硅验证、客户项目、foundry PDK、signoff 经验，不断优化出可靠、可复用、可量产的设计流程。这才是全球三大 EDA 和先进 foundry 生态的壁垒。

AMD 3D V-Cache 是一个很好的类比。AMD 官方介绍 3D V-Cache 时强调的是 64MB L3 cache die、TSV、direct copper-to-copper bonding、互连能效等技术结果，而不会把“我们为此开发了一套全球独一无二的 EDA”作为主要宣传卖点。

原因很简单，做 3D V-Cache 当然需要 TSMC SoIC / 3DFabric 开发全新的设计流程、封装规则、热模型、测试流程、版图约束，但这是先进封装项目必须具备的工程配套，不是产品价值本身。

任何全新技术都需要有全新的EDA，不然芯片怎出来，而全球三大跟三星，台积电，英特尔一起开发的全新制程每年数不胜数，但他们并没有脱离现在制程的本质，有谁会去宣传呢？

华为做 LogicFolding 当然需要新的 EDA flow、3D floorplan、cross-tier timing、thermal-aware placement、post-bond test、DFT、PDN 和 signoff，他要做这些事自然会有产业链上的投入，而且是很大的投入。

但这只能说明华为跟全球主流集团一样进入了 3D IC 设计领域，而且处于全球领先地位，笔者认为这一点值得肯定甚至当成宣传重点大书特书，但非要挂勾它发明了一种全球从未有过的底层技术，你叫我如此去写他？

正常宣传正常表达，没有任何人会有意见的，我也一定会夸他，但夸得没边我去澄清就变成了贬他了。

如果你是我这样认知，你会继续认为它独一无二还是认为他夸大呢？

澄清了几天后，目前坊间基本就剩下一整说法，那就是华为这不是 AMD 的 SRAM-on-logic，也不是台积电 SoIC，也不是普通 3D cache，而是全球唯一华为特有的logicfolding。

这个说法也需要拆开看。

从工程本质看，SRAM-on-logic、logic-on-logic、logic + SRAM hybrid，底层工具箱是一样的hybrid bonding、TSV 或垂直互连、known-good-die、3D floorplan、cross-tier timing、PDN、thermal design、post-bond test、DFT、repair。

差别只是上层放的模块不同、跨层连接颗粒度不同、热与时序难度不同。本质上就是模块布局的不同。

Logic-on-logic 不神秘，英特尔早有大量产品采用这技术，它本质上就是把原本在 2D 平面中的部分功能模块拆到上下两层，缩短部分互连，降低 RC，改善关键路径和数据流。

昨天的文章已经说明，Kinrin 9050给是全球第一颗3D堆叠技术的手机SoC，这里面必须要有一个定语那就是手机SoC，因为不论SRAM on logic 或者 logic on logic都早有相关技术与产品的落地，但加上手机SoC这个定语他就能成为唯一，但我们也不能把它神化为半导体规则被改写。

确实logic on logic更难，但那是设计上要费更多工夫的难，要达到各条件完美平衡，要花大量的人力与财力，全世界真心没有多少企业做得到，但这并非底层技术突破。

Kirin 9050 更合理定位是，在先进制程受限下，华为用更高成本、更复杂的 3D active-on-active / hybrid bonding / logic + SRAM 协同，补偿 SMIC N+3的7nm制程与国际领先制程之间的差距。

全球主流手机 SoC 没有大规模采用类似方案，不是因为不知道，更不是因为做不到，而是因为在可以使用 TSMC N3/N2 的前提下，传统平面 SoC + 常规大 cache + 成熟先进封装更加经济。

半导体行业永远倾向于同等性能下成本最低、同等成本下效率最高的方案。华为采用这种方案，更多是被限制后的高成本补课，而不是天然最优解。

### **最终结论**

今天这一篇基本上已经把所有华为公布的已知条件都收链完成，很感谢星球上得同学不断的给我发各种资料，让我也能不断地去完善。

最终我们加入 3.1GHz 跟logic + SRAM hybrid 上层 die等条件后。

Kirin 9050 的上层 die 确实不宜设计成纯 SRAM，必然也不能设计成高活性 logic-on-logic。

最现实的版本是比我昨天的更保守的logic + SRAM hybrid，下层 123–128mm² compute die，上层缩小到30–34mm² active hybrid die，其中 16–22mm² SRAM / buffer，8–12mm² low-power logic，可用 SRAM 约 18–25MB。

这个方案可以解释 P 核从 2.75GHz 到 3.1GHz 的约 12.7% 峰值频率提升，因为上层低热 logic 可以服务 critical path、clock skew、NoC 和 cache controller。

也能部分解释 GPU/NPU 的能效提升，因为中等容量 SRAM 可以减少 LPDDR 访问。但它不能单独解释 NPU +140%，后者必须来自下层 NPU 本体扩张、低精度、稀疏和 runtime 优化。

因此，最终判断是，混合上层 die 适合手机 AP，但必须更为保守，一切还是得看海思的设计优化功力，这一点我一直是非常佩服华为的。

但这一切是中国在先进制程受限下的高成本工程补课方案，而不是颠覆半导体的新物理，也不是全球其他厂商做不到的神秘技术。

华为的努力必须给予肯定，9050这颗芯片的综合技术能力非常高，这一点是明确的，但成本同样也高，但不能因为没人做而宣称全球只有我们可以做到，这里有很大的本质差异。

中国半导体与全球的差距，因为有华为与中芯国际的不懈努力，差距不断扩大的局面必然会有收敛。

不过别人也在进步，且全球AI带来的新技术才是真正突破性的技术，比如 High-NA EUV、背供电、CFET、CoWoS、CoPoS、CPO、IMC-SI、3D堆叠，HBM、HBF等等因为AI爆发且众多的新技术。

我们还是在别人路线中寻找自己的道路，整个系统级技术的每一个环节我们都是跟随者，这一点是明确的事实。

华为这条高成本3D堆叠方案确实是未来中国特色半导体之路，但是这也仅仅是众多系统级技术之一，我们没办法靠一种技术实现反超，而且这技术别人一样先进。

以上是单纯的事实陈述，这些事实完全不影响中国半导体不断在努力发展。

笔者一直强调，中国半导体做自己即可，先满足自己国内需求，不需要整天盲目对标世界，对标世界就是我上面说的事实，如果你不信那只能靠遥遥领先沸腾文走进信息茧房来麻痺自己，这一点用都没有。

我抨击的只是那些不切实际的对标世界，我们中国半导体该怎么做笔者之前文章也说过不少，快速推进或弯道超车是缺乏科学跟产业逻辑的，目前我们现在连满足本国需求还做不到，所以普通民众先把期望放在国产满足可完全自力更生上，而不是拳打台积电，脚踏英伟达。

中国成千上万的半导体企业有足够的资金，也有足够的人力，更有举国之力的支持，现在需要的只是时间，先做好自己，一步一脚印即可，追不上世界半导体天也不会塌下来，只要我们可以做到自力更生，就算落后那也是全球两个体系各自发展，中国半导体能一直进步，这一点才是关键。

kirin 9050的真正意义是这个靠先进封装的中国特色半导体之路，由kirin 9050的真正落地开启，这一条高成本方案正常来说没有竞争力应该会被淘汰，但是国内半导体产业没有其他方法，只能死磕。

最后再加上国家的分摊与补贴，或许未来在先进封装上，我们靠着更多的应用，会越做越好，成本越来越低，最终在先进封装上反而有高度竞争力，这一点是华为9050真正落地的最大意义。

        
        本文在前文基础上，修改logic + SRAM hybrid 上层 die並加入 3.1GHz 峰值频率条件，并重新审视 logic + SRAM hybrid 上层 die 在手机 AP 热约束下是否成立。

结论是可以成立，但必须非常保守。

上层 die 不能变成高活性 compute layer，也不应做 40–60mm² 大面积高带宽 SRAM。更合理的是 30–34mm² 的 active hybrid die，其中 SRAM/buffer 约 16–22mm²，低切换率 logic 约 8–12mm²。

**
**

昨天的文章『华为韬定律解读-2』笔者给了一个9050设计思路，主要是思考，性能提升幅度，发热与相关功能布局，大概得出下层die维持之前120~130mm2的面积，上层die需要40mm2的面积来放SRAM，经过许多同学提醒，我重新再看一下韬定律，确实何庭波的韬定律论文针对logicfloding的阐述並非单纯SRAM on logic也包含了logic。

何的论文描述：digital、analog、memory circuits 被分配到上下 active tiers；critical-path gates 可跨上下层分布；NoC data path、clock network、SRAM path 都可做 folding。这说明它不是单纯 AMD 式 SRAM-on-logic。

不过logic on logic或者SRAM on logic的工艺本质没有不同，核心都是3D工艺这套东西，减薄、CMP、HB、铜铜连接、介电层键合、TSV、KGD测试跟热与机械可靠性。

从hybrid bonding的互联来看，并不会因为上面接的是SRAM cell或者standard cell logic就变得不一样。 

不过设计难度确实会有不同，纯SRAM上层是一块规则的记忆体阵列，结构一致，可分bank，可冗余修复，重点是热均匀，所以设计上难度较低，而但纯logic的话又不现实，因为热的问题，可放在上层的logic很有限，大概只有10mm2即可，这样一来面积提升太小了，又无法达成华为官方的性能提升幅度。

所以吹上层全 logic、全球唯一新物理，制程新突破，这也没有道理，对于热来说更不现实。

在细读何论文这部分的阐述，同时提到 SRAM bit-line / word-line critical path、SRAM operating frequency 提升，且明确说 Kirin 2026 是 conservative implementation，只在 key critical paths selective folding，不是整颗 SoC 任意拆分。

所以最准确表述是，Kirin 9050 更可能是 mixed active-tier folding，上层包含低热 logic + SRAM / memory path / NoC / clock buffer，而非纯 SRAM，也非完整高热 logic die。

所以笔者针对更为收敛的定义，重新调整设计思路，下层保留 CPU/GPU/NPU 主运算，上层缩小到约 30–34mm²，放 16–22mm² SRAM/buffer 和 8–12mm² 低热 logic。

这既符合 LogicFolding 官方语义，也更符合手机 AP 对散热的严苛限制。

**3.1GHz 条件支持保守 logic + SRAM hybrid**

目前关于 Kirin 2026 / 9050 的 3.1GHz 说法，我在和的論文以及華為官方資料中沒找到，而是来自外部对华为 LogicFolding 路线图与媒体报道的整理。

我认为比较可信的口径是：Kirin 2026 / 9050 的最大频率提升约 12.7%，对应上一代 Kirin 9030 Pro 约 2.75GHz 的大核频率，计算结果接近 3.1GHz。

![](images/552be145abca16bb3eda.png)

这个 3.1GHz 条件很关键。

昨天的纯 SRAM 上层 die佈局主要改善 cache miss、外存访问与 sustained performance，对 CPU 峰值频率的直接帮助有限。

CPU 从 2.75GHz 到 3.1GHz，更需要 clock tree、critical path、local interconnect、skew tuning、PDN 和电压频率曲线改善。

因此，若 3.1GHz 口径成立，它反而支持上层存在少量低热 logic，而不是纯 SRAM die。

但这也不意味着上层可以放高功耗逻辑。手机 AP 的热条件极其严苛，上层 logic 只能是 clock / NoC / cache controller / QoS / DFT / thermal control 这类低切换率模块。

CPU core、GPU shader、NPU MAC、GPU L1、NPU L0 这类高热单元還是必须留在下层。

**
**

**重新审视散热：同面积下 hybrid 比纯 SRAM 更容易产生热点**

此前我们从“纯 3D SRAM”推到“logic + SRAM hybrid”。现在必须更严格地审视手机散热。

结论是：同面积、同工作强度下，logic + SRAM hybrid 的局部热风险高于纯 SRAM。

SRAM 虽然也有读写动态功耗和漏电，但它结构规则、bank 化容易、power gating 容易；logic 的切换率不均匀，某些 router、clock buffer、DMA 控制或 compression 逻辑可能形成局部热斑。

![](images/c2010e9a87c92ee1ab59.png)

 

因此，hybrid 方案不是因为“logic 更冷”，而是因为它可以把上层 active die 面积压小，避免 40–60mm² 的大 SRAM die 覆盖下层热区。

真正可行的逻辑是：少量低热 logic + 中等容量 SRAM/buffer，而不是更大容量SRAM。

**
**

**最终保守设计：下层扩大， 上层缩小；下层算，上层修路径和暂存**

在 3.1GHz 和手机散热约束加入后，Kirin 9050 的最合理设计应从此前 36–40mm² 上层 die 收缩到30-34mm2。

新的设计如下：

![](images/86ac0941577b53f6db28.png)

这套设计的核心不是上层加了logic代表它也在算，而是上层修关键路径、缩短部分互连、改善 clock skew、管理中等容量 SRAM/buffer。下层才是 CPU/GPU/NPU/ISP 的主运算层。

**
**

**上层 SRAM 容量重算：不再追求 40–50MB，而是 18–25MB 可用**

沿用此前的密度口径：上层 83 MTr/mm² 为未换算口径，若除以 1.357，则约为 61.16 MTr/mm²。若按 6T SRAM 换算，约为 1.27MB/mm² raw SRAM。

公式：83 ÷ 1.357 ≈ 61.16 MTr/mm²；61.16 ÷ 6 ÷ 8 ≈ 1.27MB/mm²。

![](images/0313f89a0774ba94d762.png)

 

这个结果意味着，新版 Kirin 9050 不是我们昨天规划的手机版 3D V-Cache 大 cache，而更像是“中等容量 3D staging memory + 低热 logic folding”。

它不追求用 40–50MB 上层 SRAM 解决所有问题，而是选择关键路径和关键场景做补偿。

### **3.1GHz 如何实现：更像 critical path 与 clock 优化**

若 Kirin 9030 Pro 的 P 核峰值约 2.75GHz，Kirin 9050 提高到 3.1GHz，本质是约 12.7% 的峰值频率提升。这没有跨代的飞跃，中规中矩的提升，但对同样是SMIC N+3制程而言已经不容易。

![](images/d0fb63ca4eb8e9e75fbe.png)

 

这也解释为什么纯 SRAM 上层不够。纯 SRAM 有助于减少 DRAM 访问、提升 GPU/NPU/ISP sustained efficiency，但不能充分解释 P 核峰值频率 +12.7%。因此，保守的 logic + SRAM hybrid 更符合 3.1GHz 条件。

**
**

**GPU/NPU 官方提升如何对应新版设计**

华为图示的 GPU +38%、GPU 能效 +40%、NPU +140%、NPU 能效 +81%，不能由 30–34mm² 上层 hybrid die 单独实现。上层只是降低数据搬移与关键路径成本，真正主增量仍应来自下层 GPU/NPU 扩大、低精度计算、压缩和软件协同。

![](images/7f4974bc6ce3ee9c95fd.png)

 

新版设计与官方提升能对上，但必须强调，上层不是全部性能来源。

尤其 NPU +140% 绝不可能单靠上层 SRAM 或少量 logic 实现，它一定需要下层 NPU 本体、低精度、稀疏和 runtime 同时提升。

**logic + SRAM hybrid 上层 die的设计能满足手机AP的高散热要求吗？**

笔者认为整体设计方向基本上是适合的，但仅限于非常保守上die较小面积的形态。

不过最终上层hybrid die的面积到底是多大，这就取决于海思的设计能力了，总而言之本质上都是面积的问题，面积大小涉及了性能与热管理的平衡，目前坊间夸大的独一无二的设计思路肯定是有帮助但这只是优化改变不了物理本质。

根据所有条件的不断收敛，笔者认为最合理的kirin 9050，它不是 3D compute stacking，也不是大面积 cache stacking，而是“有限面积、低热 logic、中等 SRAM、场景化启用”的折中方案。

下面表格就是华为想要在手机AP实现它宣称的性能提升所有满足或者说克服的条件，这些条件的达成代表华为下了很大的工夫与成本去不断打磨kirin芯片。

9050百分百是一款好产品，也有一些唯一性的技术应用落地，但这个唯一性不是因为技术别人达不到，而是别人有更低成本的方案。

所以这里面并没有看到什么突破性的技术出现，大家还是得客观看待。

对于9050的出现与落地必然是要给华为一个大大的肯定，这真的是花了大代价获得的，但不应该把这些设计上或制程上的不同说成世界唯一的突破，这样说并不科学也夸大了。

![](images/ccf4b2db78a9f0563cbc.png)

 

**理性看待所谓全球唯一，这仍然是高成本补课，不是新物理**

坊间一个常见说法是，LogicFolding 需要重新开发 EDA，所以它是全球唯一、前所未有的新技术。这个说法并非小作文但真的需要降温。

因为这类把应该做的事，上纲上线，寻找一些非核心的不同，利用一大堆技术术语不断地引导不懂的普通群众并不妥当，大家回想一下这几天韬定律发表后，从一开始铺天盖地的神话般吹捧，重新定义半导体，然后被不断科普后一直在降低规格，不断都缩限可宣传的点，大家从这两天我发表韬定律文章以来，每天同学们发小作文来让我澄清点的越来越细枝末节可以看出。

这还没算上，上周那个N+3堆叠N+2达到等效3nm的铺天盖地预热小作文，一切看得出来都是有计划的。

就EDA这事来说，半导体行业任何新的制程、新的封装、新的设计规则、新的 PDK、新的互连模型、新的可靠性要求，都需要 EDA 工具链配合。

EDA 本身不是神秘魔法。开发某一类新设计流程所需的工具、规则、脚本、模型、验证方法，并不等于在全球半导体体系之外开辟了一个新宇宙。

真正难的不是“写一个 EDA 工具”本身，而是经过长期产品迭代、硅验证、客户项目、foundry PDK、signoff 经验，不断优化出可靠、可复用、可量产的设计流程。这才是全球三大 EDA 和先进 foundry 生态的壁垒。

AMD 3D V-Cache 是一个很好的类比。AMD 官方介绍 3D V-Cache 时强调的是 64MB L3 cache die、TSV、direct copper-to-copper bonding、互连能效等技术结果，而不会把“我们为此开发了一套全球独一无二的 EDA”作为主要宣传卖点。

原因很简单，做 3D V-Cache 当然需要 TSMC SoIC / 3DFabric 开发全新的设计流程、封装规则、热模型、测试流程、版图约束，但这是先进封装项目必须具备的工程配套，不是产品价值本身。

任何全新技术都需要有全新的EDA，不然芯片怎出来，而全球三大跟三星，台积电，英特尔一起开发的全新制程每年数不胜数，但他们并没有脱离现在制程的本质，有谁会去宣传呢？

华为做 LogicFolding 当然需要新的 EDA flow、3D floorplan、cross-tier timing、thermal-aware placement、post-bond test、DFT、PDN 和 signoff，他要做这些事自然会有产业链上的投入，而且是很大的投入。

但这只能说明华为跟全球主流集团一样进入了 3D IC 设计领域，而且处于全球领先地位，笔者认为这一点值得肯定甚至当成宣传重点大书特书，但非要挂勾它发明了一种全球从未有过的底层技术，你叫我如此去写他？

正常宣传正常表达，没有任何人会有意见的，我也一定会夸他，但夸得没边我去澄清就变成了贬他了。

如果你是我这样认知，你会继续认为它独一无二还是认为他夸大呢？

澄清了几天后，目前坊间基本就剩下一整说法，那就是华为这不是 AMD 的 SRAM-on-logic，也不是台积电 SoIC，也不是普通 3D cache，而是全球唯一华为特有的logicfolding。

这个说法也需要拆开看。

从工程本质看，SRAM-on-logic、logic-on-logic、logic + SRAM hybrid，底层工具箱是一样的hybrid bonding、TSV 或垂直互连、known-good-die、3D floorplan、cross-tier timing、PDN、thermal design、post-bond test、DFT、repair。

差别只是上层放的模块不同、跨层连接颗粒度不同、热与时序难度不同。本质上就是模块布局的不同。

Logic-on-logic 不神秘，英特尔早有大量产品采用这技术，它本质上就是把原本在 2D 平面中的部分功能模块拆到上下两层，缩短部分互连，降低 RC，改善关键路径和数据流。

昨天的文章已经说明，Kinrin 9050给是全球第一颗3D堆叠技术的手机SoC，这里面必须要有一个定语那就是手机SoC，因为不论SRAM on logic 或者 logic on logic都早有相关技术与产品的落地，但加上手机SoC这个定语他就能成为唯一，但我们也不能把它神化为半导体规则被改写。

确实logic on logic更难，但那是设计上要费更多工夫的难，要达到各条件完美平衡，要花大量的人力与财力，全世界真心没有多少企业做得到，但这并非底层技术突破。

Kirin 9050 更合理定位是，在先进制程受限下，华为用更高成本、更复杂的 3D active-on-active / hybrid bonding / logic + SRAM 协同，补偿 SMIC N+3的7nm制程与国际领先制程之间的差距。

全球主流手机 SoC 没有大规模采用类似方案，不是因为不知道，更不是因为做不到，而是因为在可以使用 TSMC N3/N2 的前提下，传统平面 SoC + 常规大 cache + 成熟先进封装更加经济。

半导体行业永远倾向于同等性能下成本最低、同等成本下效率最高的方案。华为采用这种方案，更多是被限制后的高成本补课，而不是天然最优解。

### **最终结论**

今天这一篇基本上已经把所有华为公布的已知条件都收链完成，很感谢星球上得同学不断的给我发各种资料，让我也能不断地去完善。

最终我们加入 3.1GHz 跟logic + SRAM hybrid 上层 die等条件后。

Kirin 9050 的上层 die 确实不宜设计成纯 SRAM，必然也不能设计成高活性 logic-on-logic。

最现实的版本是比我昨天的更保守的logic + SRAM hybrid，下层 123–128mm² compute die，上层缩小到30–34mm² active hybrid die，其中 16–22mm² SRAM / buffer，8–12mm² low-power logic，可用 SRAM 约 18–25MB。

这个方案可以解释 P 核从 2.75GHz 到 3.1GHz 的约 12.7% 峰值频率提升，因为上层低热 logic 可以服务 critical path、clock skew、NoC 和 cache controller。

也能部分解释 GPU/NPU 的能效提升，因为中等容量 SRAM 可以减少 LPDDR 访问。但它不能单独解释 NPU +140%，后者必须来自下层 NPU 本体扩张、低精度、稀疏和 runtime 优化。

因此，最终判断是，混合上层 die 适合手机 AP，但必须更为保守，一切还是得看海思的设计优化功力，这一点我一直是非常佩服华为的。

但这一切是中国在先进制程受限下的高成本工程补课方案，而不是颠覆半导体的新物理，也不是全球其他厂商做不到的神秘技术。

华为的努力必须给予肯定，9050这颗芯片的综合技术能力非常高，这一点是明确的，但成本同样也高，但不能因为没人做而宣称全球只有我们可以做到，这里有很大的本质差异。

中国半导体与全球的差距，因为有华为与中芯国际的不懈努力，差距不断扩大的局面必然会有收敛。

不过别人也在进步，且全球AI带来的新技术才是真正突破性的技术，比如 High-NA EUV、背供电、CFET、CoWoS、CoPoS、CPO、IMC-SI、3D堆叠，HBM、HBF等等因为AI爆发且众多的新技术。

我们还是在别人路线中寻找自己的道路，整个系统级技术的每一个环节我们都是跟随者，这一点是明确的事实。

华为这条高成本3D堆叠方案确实是未来中国特色半导体之路，但是这也仅仅是众多系统级技术之一，我们没办法靠一种技术实现反超，而且这技术别人一样先进。

以上是单纯的事实陈述，这些事实完全不影响中国半导体不断在努力发展。

笔者一直强调，中国半导体做自己即可，先满足自己国内需求，不需要整天盲目对标世界，对标世界就是我上面说的事实，如果你不信那只能靠遥遥领先沸腾文走进信息茧房来麻痺自己，这一点用都没有。

我抨击的只是那些不切实际的对标世界，我们中国半导体该怎么做笔者之前文章也说过不少，快速推进或弯道超车是缺乏科学跟产业逻辑的，目前我们现在连满足本国需求还做不到，所以普通民众先把期望放在国产满足可完全自力更生上，而不是拳打台积电，脚踏英伟达。

中国成千上万的半导体企业有足够的资金，也有足够的人力，更有举国之力的支持，现在需要的只是时间，先做好自己，一步一脚印即可，追不上世界半导体天也不会塌下来，只要我们可以做到自力更生，就算落后那也是全球两个体系各自发展，中国半导体能一直进步，这一点才是关键。

kirin 9050的真正意义是这个靠先进封装的中国特色半导体之路，由kirin 9050的真正落地开启，这一条高成本方案正常来说没有竞争力应该会被淘汰，但是国内半导体产业没有其他方法，只能死磕。

最后再加上国家的分摊与补贴，或许未来在先进封装上，我们靠着更多的应用，会越做越好，成本越来越低，最终在先进封装上反而有高度竞争力，这一点是华为9050真正落地的最大意义。

        本文在前文基础上，修改logic + SRAM hybrid 上层 die並加入 3.1GHz 峰值频率条件，并重新审视 logic + SRAM hybrid 上层 die 在手机 AP 热约束下是否成立。

结论是可以成立，但必须非常保守。

上层 die 不能变成高活性 compute layer，也不应做 40–60mm² 大面积高带宽 SRAM。更合理的是 30–34mm² 的 active hybrid die，其中 SRAM/buffer 约 16–22mm²，低切换率 logic 约 8–12mm²。

**
**

昨天的文章『华为韬定律解读-2』笔者给了一个9050设计思路，主要是思考，性能提升幅度，发热与相关功能布局，大概得出下层die维持之前120~130mm2的面积，上层die需要40mm2的面积来放SRAM，经过许多同学提醒，我重新再看一下韬定律，确实何庭波的韬定律论文针对logicfloding的阐述並非单纯SRAM on logic也包含了logic。

何的论文描述：digital、analog、memory circuits 被分配到上下 active tiers；critical-path gates 可跨上下层分布；NoC data path、clock network、SRAM path 都可做 folding。这说明它不是单纯 AMD 式 SRAM-on-logic。

不过logic on logic或者SRAM on logic的工艺本质没有不同，核心都是3D工艺这套东西，减薄、CMP、HB、铜铜连接、介电层键合、TSV、KGD测试跟热与机械可靠性。

从hybrid bonding的互联来看，并不会因为上面接的是SRAM cell或者standard cell logic就变得不一样。 

不过设计难度确实会有不同，纯SRAM上层是一块规则的记忆体阵列，结构一致，可分bank，可冗余修复，重点是热均匀，所以设计上难度较低，而但纯logic的话又不现实，因为热的问题，可放在上层的logic很有限，大概只有10mm2即可，这样一来面积提升太小了，又无法达成华为官方的性能提升幅度。

所以吹上层全 logic、全球唯一新物理，制程新突破，这也没有道理，对于热来说更不现实。

在细读何论文这部分的阐述，同时提到 SRAM bit-line / word-line critical path、SRAM operating frequency 提升，且明确说 Kirin 2026 是 conservative implementation，只在 key critical paths selective folding，不是整颗 SoC 任意拆分。

所以最准确表述是，Kirin 9050 更可能是 mixed active-tier folding，上层包含低热 logic + SRAM / memory path / NoC / clock buffer，而非纯 SRAM，也非完整高热 logic die。

所以笔者针对更为收敛的定义，重新调整设计思路，下层保留 CPU/GPU/NPU 主运算，上层缩小到约 30–34mm²，放 16–22mm² SRAM/buffer 和 8–12mm² 低热 logic。

这既符合 LogicFolding 官方语义，也更符合手机 AP 对散热的严苛限制。

**3.1GHz 条件支持保守 logic + SRAM hybrid**

目前关于 Kirin 2026 / 9050 的 3.1GHz 说法，我在和的論文以及華為官方資料中沒找到，而是来自外部对华为 LogicFolding 路线图与媒体报道的整理。

我认为比较可信的口径是：Kirin 2026 / 9050 的最大频率提升约 12.7%，对应上一代 Kirin 9030 Pro 约 2.75GHz 的大核频率，计算结果接近 3.1GHz。

![](images/552be145abca16bb3eda.png)

这个 3.1GHz 条件很关键。

昨天的纯 SRAM 上层 die佈局主要改善 cache miss、外存访问与 sustained performance，对 CPU 峰值频率的直接帮助有限。

CPU 从 2.75GHz 到 3.1GHz，更需要 clock tree、critical path、local interconnect、skew tuning、PDN 和电压频率曲线改善。

因此，若 3.1GHz 口径成立，它反而支持上层存在少量低热 logic，而不是纯 SRAM die。

但这也不意味着上层可以放高功耗逻辑。手机 AP 的热条件极其严苛，上层 logic 只能是 clock / NoC / cache controller / QoS / DFT / thermal control 这类低切换率模块。

CPU core、GPU shader、NPU MAC、GPU L1、NPU L0 这类高热单元還是必须留在下层。

**
**

**重新审视散热：同面积下 hybrid 比纯 SRAM 更容易产生热点**

此前我们从“纯 3D SRAM”推到“logic + SRAM hybrid”。现在必须更严格地审视手机散热。

结论是：同面积、同工作强度下，logic + SRAM hybrid 的局部热风险高于纯 SRAM。

SRAM 虽然也有读写动态功耗和漏电，但它结构规则、bank 化容易、power gating 容易；logic 的切换率不均匀，某些 router、clock buffer、DMA 控制或 compression 逻辑可能形成局部热斑。

![](images/c2010e9a87c92ee1ab59.png)

 

因此，hybrid 方案不是因为“logic 更冷”，而是因为它可以把上层 active die 面积压小，避免 40–60mm² 的大 SRAM die 覆盖下层热区。

真正可行的逻辑是：少量低热 logic + 中等容量 SRAM/buffer，而不是更大容量SRAM。

**
**

**最终保守设计：下层扩大， 上层缩小；下层算，上层修路径和暂存**

在 3.1GHz 和手机散热约束加入后，Kirin 9050 的最合理设计应从此前 36–40mm² 上层 die 收缩到30-34mm2。

新的设计如下：

![](images/86ac0941577b53f6db28.png)

这套设计的核心不是上层加了logic代表它也在算，而是上层修关键路径、缩短部分互连、改善 clock skew、管理中等容量 SRAM/buffer。下层才是 CPU/GPU/NPU/ISP 的主运算层。

**
**

**上层 SRAM 容量重算：不再追求 40–50MB，而是 18–25MB 可用**

沿用此前的密度口径：上层 83 MTr/mm² 为未换算口径，若除以 1.357，则约为 61.16 MTr/mm²。若按 6T SRAM 换算，约为 1.27MB/mm² raw SRAM。

公式：83 ÷ 1.357 ≈ 61.16 MTr/mm²；61.16 ÷ 6 ÷ 8 ≈ 1.27MB/mm²。

![](images/0313f89a0774ba94d762.png)

 

这个结果意味着，新版 Kirin 9050 不是我们昨天规划的手机版 3D V-Cache 大 cache，而更像是“中等容量 3D staging memory + 低热 logic folding”。

它不追求用 40–50MB 上层 SRAM 解决所有问题，而是选择关键路径和关键场景做补偿。

### **3.1GHz 如何实现：更像 critical path 与 clock 优化**

若 Kirin 9030 Pro 的 P 核峰值约 2.75GHz，Kirin 9050 提高到 3.1GHz，本质是约 12.7% 的峰值频率提升。这没有跨代的飞跃，中规中矩的提升，但对同样是SMIC N+3制程而言已经不容易。

![](images/d0fb63ca4eb8e9e75fbe.png)

 

这也解释为什么纯 SRAM 上层不够。纯 SRAM 有助于减少 DRAM 访问、提升 GPU/NPU/ISP sustained efficiency，但不能充分解释 P 核峰值频率 +12.7%。因此，保守的 logic + SRAM hybrid 更符合 3.1GHz 条件。

**
**

**GPU/NPU 官方提升如何对应新版设计**

华为图示的 GPU +38%、GPU 能效 +40%、NPU +140%、NPU 能效 +81%，不能由 30–34mm² 上层 hybrid die 单独实现。上层只是降低数据搬移与关键路径成本，真正主增量仍应来自下层 GPU/NPU 扩大、低精度计算、压缩和软件协同。

![](images/7f4974bc6ce3ee9c95fd.png)

 

新版设计与官方提升能对上，但必须强调，上层不是全部性能来源。

尤其 NPU +140% 绝不可能单靠上层 SRAM 或少量 logic 实现，它一定需要下层 NPU 本体、低精度、稀疏和 runtime 同时提升。

**logic + SRAM hybrid 上层 die的设计能满足手机AP的高散热要求吗？**

笔者认为整体设计方向基本上是适合的，但仅限于非常保守上die较小面积的形态。

不过最终上层hybrid die的面积到底是多大，这就取决于海思的设计能力了，总而言之本质上都是面积的问题，面积大小涉及了性能与热管理的平衡，目前坊间夸大的独一无二的设计思路肯定是有帮助但这只是优化改变不了物理本质。

根据所有条件的不断收敛，笔者认为最合理的kirin 9050，它不是 3D compute stacking，也不是大面积 cache stacking，而是“有限面积、低热 logic、中等 SRAM、场景化启用”的折中方案。

下面表格就是华为想要在手机AP实现它宣称的性能提升所有满足或者说克服的条件，这些条件的达成代表华为下了很大的工夫与成本去不断打磨kirin芯片。

9050百分百是一款好产品，也有一些唯一性的技术应用落地，但这个唯一性不是因为技术别人达不到，而是别人有更低成本的方案。

所以这里面并没有看到什么突破性的技术出现，大家还是得客观看待。

对于9050的出现与落地必然是要给华为一个大大的肯定，这真的是花了大代价获得的，但不应该把这些设计上或制程上的不同说成世界唯一的突破，这样说并不科学也夸大了。

![](images/ccf4b2db78a9f0563cbc.png)

 

**理性看待所谓全球唯一，这仍然是高成本补课，不是新物理**

坊间一个常见说法是，LogicFolding 需要重新开发 EDA，所以它是全球唯一、前所未有的新技术。这个说法并非小作文但真的需要降温。

因为这类把应该做的事，上纲上线，寻找一些非核心的不同，利用一大堆技术术语不断地引导不懂的普通群众并不妥当，大家回想一下这几天韬定律发表后，从一开始铺天盖地的神话般吹捧，重新定义半导体，然后被不断科普后一直在降低规格，不断都缩限可宣传的点，大家从这两天我发表韬定律文章以来，每天同学们发小作文来让我澄清点的越来越细枝末节可以看出。

这还没算上，上周那个N+3堆叠N+2达到等效3nm的铺天盖地预热小作文，一切看得出来都是有计划的。

就EDA这事来说，半导体行业任何新的制程、新的封装、新的设计规则、新的 PDK、新的互连模型、新的可靠性要求，都需要 EDA 工具链配合。

EDA 本身不是神秘魔法。开发某一类新设计流程所需的工具、规则、脚本、模型、验证方法，并不等于在全球半导体体系之外开辟了一个新宇宙。

真正难的不是“写一个 EDA 工具”本身，而是经过长期产品迭代、硅验证、客户项目、foundry PDK、signoff 经验，不断优化出可靠、可复用、可量产的设计流程。这才是全球三大 EDA 和先进 foundry 生态的壁垒。

AMD 3D V-Cache 是一个很好的类比。AMD 官方介绍 3D V-Cache 时强调的是 64MB L3 cache die、TSV、direct copper-to-copper bonding、互连能效等技术结果，而不会把“我们为此开发了一套全球独一无二的 EDA”作为主要宣传卖点。

原因很简单，做 3D V-Cache 当然需要 TSMC SoIC / 3DFabric 开发全新的设计流程、封装规则、热模型、测试流程、版图约束，但这是先进封装项目必须具备的工程配套，不是产品价值本身。

任何全新技术都需要有全新的EDA，不然芯片怎出来，而全球三大跟三星，台积电，英特尔一起开发的全新制程每年数不胜数，但他们并没有脱离现在制程的本质，有谁会去宣传呢？

华为做 LogicFolding 当然需要新的 EDA flow、3D floorplan、cross-tier timing、thermal-aware placement、post-bond test、DFT、PDN 和 signoff，他要做这些事自然会有产业链上的投入，而且是很大的投入。

但这只能说明华为跟全球主流集团一样进入了 3D IC 设计领域，而且处于全球领先地位，笔者认为这一点值得肯定甚至当成宣传重点大书特书，但非要挂勾它发明了一种全球从未有过的底层技术，你叫我如此去写他？

正常宣传正常表达，没有任何人会有意见的，我也一定会夸他，但夸得没边我去澄清就变成了贬他了。

如果你是我这样认知，你会继续认为它独一无二还是认为他夸大呢？

澄清了几天后，目前坊间基本就剩下一整说法，那就是华为这不是 AMD 的 SRAM-on-logic，也不是台积电 SoIC，也不是普通 3D cache，而是全球唯一华为特有的logicfolding。

这个说法也需要拆开看。

从工程本质看，SRAM-on-logic、logic-on-logic、logic + SRAM hybrid，底层工具箱是一样的hybrid bonding、TSV 或垂直互连、known-good-die、3D floorplan、cross-tier timing、PDN、thermal design、post-bond test、DFT、repair。

差别只是上层放的模块不同、跨层连接颗粒度不同、热与时序难度不同。本质上就是模块布局的不同。

Logic-on-logic 不神秘，英特尔早有大量产品采用这技术，它本质上就是把原本在 2D 平面中的部分功能模块拆到上下两层，缩短部分互连，降低 RC，改善关键路径和数据流。

昨天的文章已经说明，Kinrin 9050给是全球第一颗3D堆叠技术的手机SoC，这里面必须要有一个定语那就是手机SoC，因为不论SRAM on logic 或者 logic on logic都早有相关技术与产品的落地，但加上手机SoC这个定语他就能成为唯一，但我们也不能把它神化为半导体规则被改写。

确实logic on logic更难，但那是设计上要费更多工夫的难，要达到各条件完美平衡，要花大量的人力与财力，全世界真心没有多少企业做得到，但这并非底层技术突破。

Kirin 9050 更合理定位是，在先进制程受限下，华为用更高成本、更复杂的 3D active-on-active / hybrid bonding / logic + SRAM 协同，补偿 SMIC N+3的7nm制程与国际领先制程之间的差距。

全球主流手机 SoC 没有大规模采用类似方案，不是因为不知道，更不是因为做不到，而是因为在可以使用 TSMC N3/N2 的前提下，传统平面 SoC + 常规大 cache + 成熟先进封装更加经济。

半导体行业永远倾向于同等性能下成本最低、同等成本下效率最高的方案。华为采用这种方案，更多是被限制后的高成本补课，而不是天然最优解。

### **最终结论**

今天这一篇基本上已经把所有华为公布的已知条件都收链完成，很感谢星球上得同学不断的给我发各种资料，让我也能不断地去完善。

最终我们加入 3.1GHz 跟logic + SRAM hybrid 上层 die等条件后。

Kirin 9050 的上层 die 确实不宜设计成纯 SRAM，必然也不能设计成高活性 logic-on-logic。

最现实的版本是比我昨天的更保守的logic + SRAM hybrid，下层 123–128mm² compute die，上层缩小到30–34mm² active hybrid die，其中 16–22mm² SRAM / buffer，8–12mm² low-power logic，可用 SRAM 约 18–25MB。

这个方案可以解释 P 核从 2.75GHz 到 3.1GHz 的约 12.7% 峰值频率提升，因为上层低热 logic 可以服务 critical path、clock skew、NoC 和 cache controller。

也能部分解释 GPU/NPU 的能效提升，因为中等容量 SRAM 可以减少 LPDDR 访问。但它不能单独解释 NPU +140%，后者必须来自下层 NPU 本体扩张、低精度、稀疏和 runtime 优化。

因此，最终判断是，混合上层 die 适合手机 AP，但必须更为保守，一切还是得看海思的设计优化功力，这一点我一直是非常佩服华为的。

但这一切是中国在先进制程受限下的高成本工程补课方案，而不是颠覆半导体的新物理，也不是全球其他厂商做不到的神秘技术。

华为的努力必须给予肯定，9050这颗芯片的综合技术能力非常高，这一点是明确的，但成本同样也高，但不能因为没人做而宣称全球只有我们可以做到，这里有很大的本质差异。

中国半导体与全球的差距，因为有华为与中芯国际的不懈努力，差距不断扩大的局面必然会有收敛。

不过别人也在进步，且全球AI带来的新技术才是真正突破性的技术，比如 High-NA EUV、背供电、CFET、CoWoS、CoPoS、CPO、IMC-SI、3D堆叠，HBM、HBF等等因为AI爆发且众多的新技术。

我们还是在别人路线中寻找自己的道路，整个系统级技术的每一个环节我们都是跟随者，这一点是明确的事实。

华为这条高成本3D堆叠方案确实是未来中国特色半导体之路，但是这也仅仅是众多系统级技术之一，我们没办法靠一种技术实现反超，而且这技术别人一样先进。

以上是单纯的事实陈述，这些事实完全不影响中国半导体不断在努力发展。

笔者一直强调，中国半导体做自己即可，先满足自己国内需求，不需要整天盲目对标世界，对标世界就是我上面说的事实，如果你不信那只能靠遥遥领先沸腾文走进信息茧房来麻痺自己，这一点用都没有。

我抨击的只是那些不切实际的对标世界，我们中国半导体该怎么做笔者之前文章也说过不少，快速推进或弯道超车是缺乏科学跟产业逻辑的，目前我们现在连满足本国需求还做不到，所以普通民众先把期望放在国产满足可完全自力更生上，而不是拳打台积电，脚踏英伟达。

中国成千上万的半导体企业有足够的资金，也有足够的人力，更有举国之力的支持，现在需要的只是时间，先做好自己，一步一脚印即可，追不上世界半导体天也不会塌下来，只要我们可以做到自力更生，就算落后那也是全球两个体系各自发展，中国半导体能一直进步，这一点才是关键。

kirin 9050的真正意义是这个靠先进封装的中国特色半导体之路，由kirin 9050的真正落地开启，这一条高成本方案正常来说没有竞争力应该会被淘汰，但是国内半导体产业没有其他方法，只能死磕。

最后再加上国家的分摊与补贴，或许未来在先进封装上，我们靠着更多的应用，会越做越好，成本越来越低，最终在先进封装上反而有高度竞争力，这一点是华为9050真正落地的最大意义。

        
                
                

![](/assets_dweb/logo@1x.png)

                知识星球
                
        
        
            
            扫码加入星球
            查看更多优质内容
        
        https://wx.zsxq.com/mweb/views/joingroup/join_group.html?group_id=88888812815442

---

Source: https://articles.zsxq.com/id_qdgmrfkoxnol.html

Linked from topic_id: 55522521125222484
