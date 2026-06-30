# CoPoS 与玻璃基板 ，从「圆变方」的技术路线与投资逻辑

        
            [来自：
                半导体大佬的会议室](https://wx.zsxq.com/group/88888812815442)
        
        
            
                

![](images/39ac34f1b548792d9368.jpg)

                吴梓豪leslie
            
            2026年06月23日 04:39
        
        
            **本文最重要的七个结论**

1. CoPoS 的本质不是「玻璃基板革命」，而是把 CoWoS-L 类似的 LSI/RDL 中介层制造，从圆形 wafer 平台转到方形 panel 平台。

2. 初期 CoPoS 即使使用玻璃，也主要是临时基板 glass carrier / temporary carrier 的制程应用，做完后会去除，不是最终封装 BOM 里的永久玻璃基板。

Fan-out 封装多年来就大量使用临时玻璃 carrier，因此我们不能把 2028台积电的CoPoS 量产等同于玻璃基板爆发。

3. 真正有价值量、也真正需要 TGV、玻璃金属化、电镀填铜与上下 ABF build-up 的，是后期 oS 段的玻璃心载版 glass core substrate。它是 2030 的第二代CoPoS技术，而不是 2028 年初代 CoPoS 量产的故事。

4. 玻璃芯载板Glass core substrate 不是拿一片平玻璃垫在下面，而是把传统 package substrate 中间的 organic core 换成 glass core，上下仍然保留 ABF 或类 ABF build-up。玻璃没有干掉 ABF，也没有干掉 PCB。

5. 玻璃中介层 Glass interposer 似乎在短期没有用武之地，但它仍有长期研究价值，尤其在低损耗、高频、CPO、RF、光电封装场景，但在台积电 AI GPU 主线中，应该会有很长一段时间不需要把玻璃上移到 interposer，因为目前的技术路线中 LSI/RDL + glass core substrate 已能覆盖相当长一段路线。

6. 2026–2028 年是 CoWoS 与 CoPoS 第一代并行爬坡期，2028H2 若没有重大 delay，初代CoPoS 有机会先在 Feynman 或同级高端 SKU 上落地。2030 前后玻璃芯载版 glass core substrate 才可能在 AI/HPC 中明显放量。

7. 投资上要拆成两波：第一波看圆变方的 panel-level 制程设备与面板工程能力第二波看 glass core、TGV、电镀、ABF build-up、载板与检测。

把两波逻辑混成同一波，是大多数 A 股推票小作文的核心误导。

**CoPoS 到底是什么**

先用一个盖楼的比喻讲清楚。AI GPU 封装像是在一块地上建一座超大工厂，上面有 GPU、HBM、I/O die，彼此要靠非常密的道路相连。下面还要有地基，把电源、讯号和机械支撑一路接到主板。

CoWoS-L 就像是在一个圆形工地上先铺好局部高速道路 LSI、再用 RDL 把城市道路铺开，最后把整个方形的街区切出来接到底部地基。

CoPoS 做的不是把道路材料从矽变成玻璃，而是把工地从圆形变成方形。为什么有意义？

因为 AI 封装是方形，圆形 wafer 上切方形，边角浪费会越来越严重。当一个封装越做越大，方形 panel 基板更像一块方形土地，排方形楼盘土地利用面积可以更紧密。这就是所谓「圆变方」。

很多人听到 panel 面板就以为最终封装里留下了一大块玻璃板，这是误会。Panel 在这里首先是制造幅面、制程平台、临时工地。

最后留下的不是那块临时载板 glass carrier，而是在上面制作出来的 RDL、LSI、铜线、介电层、模封胶固化后的重构 interposer。临时载板像施工脚手架，楼盖好后脚手架拆掉，不能把脚手架算作房子的主材料。

这也解释了为什么「玻璃基板」题材容易被炒错。

玻璃临时载板 carrier 在早期的先进封装就有大量应用 Fan-out、wafer thinning、2.5D/3D 先进封装里本来就用了很多年，玻璃基板龙头康宁Corning 也明确把 advanced packaging glass carrier 定义为 temporary bonding 用于 fan-out 和先进封装的玻璃载具 。

玻璃临时载板这个市场是存在的，但它不是大家所期待大约 2030 年才会爆发的 glass core substrate，那是妥妥的两码事，很可惜A股的卖方们，对相关技术的区别几乎不得而知。

### **JPCA 2026：****台积电到底验证了什么**

JPCA Show 2026 之后，市场最关注的是郭明錤流出的一张台积电PPT，标题为 Glass Substrate Development for CoWoS。

它的价值不在于首次提到玻璃，而在于把 台积电未来的玻璃载板与日本ABF载板龙头揖斐电以及台湾面板厂群创放在同一个玻璃芯载板验证框架里。

郭明錤对该投影片的解读指出，这是玻璃芯载板，结构是 glass core 上下黏合 ABF，该技术对应 CoPoS 的 oS。同时他也提醒图中的 COP 是 coplanarity，不是 Chip-on-Package 。

图 1：使用者提供的 JPCA 2026 台积电 Glass Substrate Development for CoWoS 投影片截图。重点是 Glass-SBT vs Organic-SBT，属于 substrate 层验证。

![](images/3dbf6017b1184bed6f6e.jpg)

PPT的关键规格

1. 测试载具：0.8mm 玻璃核心、5 倍光罩（5x reticle）CoW 作为 test vehicle、整体封装尺寸 85 × 110 mm（已是大型 AI GPU 等级）。

2. 玻璃核心由 250 × 250 mm 母板切割而来，上下各黏合 ABF 增层，形成「ABF / 玻璃核心 / ABF」三层结构。

3. ABF 增层采用味之素（Ajinomoto）GL107 混搭 ABF-GCP，测试层数 24–28 层，正是 2027–2028 主流 AI 晶片规格。

4. 结果：未出现严重翘曲、未发生分层剥离（delamination）；封装共面度（Coplanarity）改善约 16%，并同步降低回路电感（L）与导通电阻（R），带来电源完整性（PI）改善。

这张图不是在证明 CoPoS 初代就用了玻璃 interposer。它是在说：台积电先拿 CoW/CoWoS 测试车去验证 glass core substrate 能不能改善超大封装的共面度、翘曲、CTE、刚性、R/L 与电源完整性。

也就是说，图里的玻璃在 package substrate 这一层，而不是 CoP 的 panel/RDL/LSI 这一层。

因此我们可以采用台积电的固定口径：CoP 段是 panel-level RDL/LSI interposer；oS 段是 package substrate。

2028 年初代CoPoS 跟CoWoS-L一样还是采用临时玻璃载板，但临时玻璃载板从圆形改成方形，仅此而已，oS段

还是会先用传统 organic-core ABF substrate。到了2030年的二代 CoPoS 才会把 substrate 中间的 organic core 换成 glass core玻璃芯载板。

市场上针对CoPoS可能delay以及2028如期推出众说纷纭，我们把事情拆开后，市场上很多看似矛盾的说法就能统一，CoPoS 还是会在 2028H2的Feyman导入，因为改动不大，on schedule是大概率，真正难点也就是玻璃芯载板 glass core substrate 得 2030 后才能真正放量。

**从 CoWoS-S/R/L 到 CoPoS**

CoWoS-S 是最经典的硅中介层方案，互连密度高、成熟度高，但大面积矽中介层成本高，尺寸越大越受 reticle stitching、良率和 wafer 利用率限制。

台积电官方 3DFabric 明确表示，CoWoS-S 可容纳约 3.3 倍 reticle、约 2700 mm² 的 interposer，更大尺寸推荐使用 CoWoS-L 或 CoWoS-R 。

CoWoS-R 是 RDL interposer 路线。它用聚合物介电层与铜线实现扇出与互连，成本和尺寸弹性比完整硅中介层好，但互连密度低于硅中介层。台积电给出的 CoWoS-R 最小 pitch 约 4 μm、线宽线距约 2/2 μm 。

CoWoS-L 则是我们理解未来 CoPoS 的关键。

 

CoWoS-L 不是完整硅中介层，而是 RDL-based interposer 重新布线中介层加 embedded LSI 预埋硅桥。

LSI 是局部硅桥，负责 GPU、HBM、chiplet 之间最需要高密度互连的区域。RDL 负责大面积供电、讯号扇出和较粗互连。这是一种务实折中，最需要高密度的地方用硅，其他区域用 RDL 和有机/聚合物结构。

CoPoS 初期可以理解为 CoWoS-L 的 panel 面板方形化。

它不是推翻 LSI/RDL，而是把这套 RDL + LSI + molding的重构 interposer 制造平台，从圆形 wafer 放大到方形 panel。

![](images/96b12b69150564cc00a1.png)

**CoPoS 的初代变化：不是玻璃基板，而是面板级制造工艺**

CoPoS 的 P 不是一块永久的「玻璃基板」。P 对应的是 panel-level process面板级制程，是中介层/RDL 的方形制造幅面。

根据TrendForce的最新报告，台积电 CoPoS 的标准化 310×310mm panel玻璃基板，2026 年是设备与材料验证期，2027 年 pilot中试，2028H2 量产。

很多人会把这个310×310mm的玻璃基板当成玻璃在先进封装的跨越式应用，事实上这只是原本的12寸圆形玻璃临时载板变成310×310mm的方形临时载板。

临时载板一直都是用玻璃，临时载板本身也没啥价值量，临时载板圆变方的价值增量几乎没有，更大的增量是在能加工方形基板的制程设备上。

所以TrendForce的最新报告，同时又把玻璃芯载板 glass core substrate 放到 CoPoS 之后，商业规模化更可能在 2030 后。TrendForce的这个拆分很重要也足够清晰，跟笔者聊的台积电的CoPoS技术演变相吻合。

如果有人说「CoPoS 量产，所以玻璃基板 2028 大爆发」，这就是把 panel carrier临时玻璃载板、panel process面板制程、glass core substrate 玻璃芯载板混为一谈。

 

再重复一遍，310×310 mm 玻璃基板是 CoP 段的方形临时载版，它是 glass carrier，在 panel 上形成 RDL/LSI/molding interposer 后，最终封装里不会留下了 310×310 mm 的玻璃基板，因为它只是最终要被去除的临时载板，上面不需要有任何加工，金额很低。

制程由圆形改成方形，也不是普通 LCD 面板制程设备原封不动搬来做 CoPoS。

高阶 FPD 光刻机已能做到 1.5–2 μm 级线宽，例如 Canon Gen 8 FPD 光刻机公布过 1.5 μm resolution 与 ±0.35 μm overlay，后续机型也公布 ±0.30 μm overlay 。但 CoPoS 难点不只是线宽，还包括半导体级颗粒、PVD/seed、铜电镀、RDL 应力、翘曲、KGD 对位、全检与可靠性。

 

所以，面板厂的优势不是「直接把 LCD 产线拿来做 AI 封装」，而是它们有大面积玻璃搬运、清洗、贴合、曝光、自动化、平整度与面板级工程经验。

真正 AI CoPoS 需要的是面板级尺寸加半导体级精度。这是群创、友达、京东方、TCL 华星等面板厂能参与但不能单独主导的原因。

**fan-out先进封装早就有临时玻璃载板glass carrier**

Fan-out 封装的基本逻辑是把已知良品 die 放到临时 carrier 上，用 molding compound 固化成重构 wafer 或 panel，再做 RDL、植球、切割。

ASE日月光对 Panel FO 的说法是，传统 fan-out 用圆形 wafer 作为 reconstituted carrier 支撑 chip、RDL 和 molding，而panel-level fan-out 改用矩形 panel 作为 reconstituted carrier，以提高面积利用率 。

上述的FOPLP和我们讨论 CoPoS 的「圆变方」非常相似。

玻璃基板龙头Corning 也明确提供 advanced packaging glass carriers，用于 wafer thinning、fan-out packaging 和 2.5D/3D advanced packaging 的 temporary bonding。

也就是说，玻璃临时载板 carrier 不是 2028 年才出现的新物种，而是先进封装里由来已久的制程载具。

 

临时载板也有价值，但他以前的CoWoS-L就存在所以没有太大增量，而且临时载板更像周转治具或半耗材，附加价值低，不像玻璃芯载板 glass core substrate 那样每颗高端封装都永久消耗一片核心玻璃。

临时 carrier 能否重复使用，要看污染、刮伤、热循环、残胶、TTV、边缘崩裂与规格漂移。高精度 carrier 不是无限次使用，也不是每颗封装一次性消耗。

产线需要 carrier 库存、备品和更换，但不能把它按每颗 AI GPU 线性放大。

因此，初期 CoPoS 主要是 carrier 端和制程端，而不是永久 BOM 端，初期CoPoS不会有任何玻璃基板存在最终的封装成品。

它会带来玻璃 carrier临时载板、release film剥离膜、temporary bonding/debonding临时键合解键合、清洗、搬运和检测的增量，但这些价值量远小于未来 oS 段 glass core substrate玻璃芯载板，这才是市场炒作且期待的真正主餐。

**2030 年才是玻璃芯载板 Glass Core Substrate 的主战场**

Glass core substrate 位于 oS，也就是 on substrate 这一层。传统高阶封装 substrate 可以简化成 organic core + 上下 ABF build-up。

Glass core substrate 则是 glass core + 上下 ABF build-up。它不是把 ABF 干掉，而是把核心骨架换成玻璃，让地基更平、更硬、更稳，再在上下继续用 ABF build-up 做多层铜线、via、pad 和 BGA 扇出。

为何需要ABF+玻璃芯载板的三明治结构，因为玻璃芯载板透过TGV可以实现垂直互联，但没办法做横向拓展互联，航向就得靠ABF。

台积电先在 oS 段导入玻璃核心glass core又是什么考量？

因为substrate这一层对互连密度的要求低于 interposer 层，但对机械稳定性、翘曲、共面度、CTE、供电完整性和尺寸稳定性非常敏感。

超大 AI 封装越做越大，最怕地基不平、热膨胀不一致、回流焊后翘曲、BGA 接点失效、电源回路变差。玻璃 core 的刚性、平整度、低翘曲和尺寸稳定性刚好对症。

但 glass core substrate 绝不是只靠平整度。它必须做 TGV、孔壁处理、阻障层/种子层、铜填孔或电镀、上下 ABF build-up、电测、可靠性与全检。

全球TGV龙头德国LPKF 把 TGV 称为 glass substrates 的 backbone，因为它连接 substrate 两侧的 redistribution layers，支撑多 die 封装 。

基板大厂旭硝子 AGC 也把 TGV glass substrate 用于 semiconductor packaging 和 glass interposer，并列出 wafer 与 panel 形态、通孔、孔径与 pitch 等规格 。

所以，真正高价值的玻璃基板不是一片平玻璃，而是一套玻璃 core + TGV + 金属化 + 电镀 + ABF build-up + 可靠性验证的系统工程。它比 CoPoS 初代难很多，也正因如此，TrendForce 把 glass core substrate 的商业规模化放到 2030 后 。

![](images/21b53428457fe683a094.png)

# **
**
**Glass Interposer 是长期选项之一，但不是台积电主线**

 行业一直以来研究玻璃中介层 glass interposer，这并非没有意义。

玻璃具有低介电损耗、高电阻率、尺寸稳定、大面积和低成本潜力，对 RF、毫米波、CPO、光电封装、低损耗高速互连有吸引力。IMAPS 等资料也长期提到 TGV interposer 的优势，包括低损耗、低介电常数、高电阻等 。

但把玻璃从 substrate core 上移到 interposer 层，难度也上了一个台阶。

Interposer 要直接连 GPU、HBM、chiplet，要求线宽、线距、TGV/RDL 密度、对位、热管理和良率都高很多。玻璃热导率差、脆性高、大面积 TGV 和细 RDL 良率难，这些都比 substrate core 难得多。

台积电目前已有一条非常合理的工程折中，上面用 CoP 的 LSI/RDL 保住高速互连，下面用 glass core substrate 改善地基。

这条路并不需要把 glass 立刻上移到 interposer，也能支撑 40 倍 reticle 甚至更大的 SoW-X/CoPoS 系统整合想像。换句话说，glass interposer 不是没价值，但不是台积电 AI GPU 主线的必经路。

长期来看，glass interposer 更可能先在 CPO、光电、RF、低损耗大面积互连或特定 chiplet 场景落地。

如果未来 TGV 密度、玻璃金属化、热管理和 panel RDL 良率大幅成熟，它有机会替代一部分硅 interposer 或补充 LSI/RDL。但至少在 2030甚至到2035年的台积电 AI/HPC 主线中，最务实的路线仍是 CoP panel-level LSI/RDL + oS glass core substrate。

**台积电路线时间表：2026–2028 CoPoS，2030 Glass Core**

台积电资深副总张晓强 2026 技术论坛说，5.5-reticle CoWoS 已在生产，14-reticle CoWoS 预计 2028 年量产，可整合约 10 颗大型 compute die 和 20 颗 HBM，2029 年还会 beyond-14 reticle；SoW-X 约 40 reticle，定位是系统级 wafer 整合 。

对 Feynman 或同级产品而言，若封装要容纳更多 compute tile、更多 HBM、更多 I/O 和更大系统互连，panel-level RDL/LSI 的经济性与面积扩张能力会越来越重要。

所以依照台积电官方公布的roadmap，2026–2027 的CoPoS将以设备材料验证和 pilot 中试为主。2028H2 若没重大 delay，CoPoS 在 NVIDIA 高端 SKU 优先导入；2030 前后，ASIC 阵营才开始更普遍跟进。

真正对玻璃基板行业有大帮助的玻璃芯载板则要往后推。2028 年可以有 CoPoS，但不等于 glass core substrate 大量放量。

2030 年左右，当 TGV、电镀、ABF 贴合、良率、供应链与客户验证成熟后，玻璃芯载板glass core substrate 才更可能成为高端 AI/HPC 的明显增量。

 

![](images/5a9dcdaf7b5911c3e7c5.png)

# **
**
**设备与材料：第一波看圆变方，第二波看 TGV**

 CoPoS 第一波受益链不应该是「玻璃基板链」。更正确是 panel-level RDL/interposer 制程链。

这包括大型 panel 搬运、自动化、清洗、涂布显影 Track、曝光、PVD seed、电镀、蚀刻、RDL 检测、翘曲量测、临时 bonding/debonding、release film、carrier 清洗与回收。

这些环节可能吸收一部分面板产业经验，也需要半导体级升级，主要还是由原有的半导体及面板设备商来主导。

第二波才是目前炒作的玻璃基板 glass core substrate 链。它包括低碱/无碱玻璃 core、TGV 成孔、LIDE 或雷射改质、湿蚀刻、孔壁金属化、seed/barrier、铜填孔、电镀、CMP/平坦化、ABF lamination、低 Dk/Df 介电材料、电测、X-ray、AOI、SAM、热循环可靠性、切割与边缘裂纹控制。

因此，材料端在 2028 前后没有想像中剧烈。polymer dielectric、molding compound、ABF、铜、电镀液、光阻、release film、glass carrier 都是既有CoWoS-L体系延伸。

真正材料变化在 2030 前后：substrate core 从有机材料变玻璃后，ABF 与玻璃的界面黏着、热应力匹配、TGV 金属化、填孔可靠性都会变成新战场。

**群创为何涨，利多在哪里**

群创这波被市场重估，不是因为它马上成为台积电 CoPoS 主导或主力厂商，也不是因为它立刻有 AI GPU玻璃心载板 glass core substrate 的巨额收入，而是因为 JPCA 投影片把群创放入 TSMC + Ibiden 的 glass substrate 验证框架。从5月起涨至今已有接近3倍的涨幅。

市场把群创从面板景气循环股重新估值为 AI 先进封装潜在供应链。

群创在CoPoS链条上的真实价值在大尺寸玻璃、面板级制程、搬运、清洗、平整度控制、贴合、自动化和可能的 TGV/玻璃加工中试能力。

这些能力可以参与第一波 CoPoS panel 化，也可以参与第二波 glass core substrate 验证。但它不是替代台积电，更不是替代 Ibiden 或 ABF 载板厂。

 

台湾其他可能受益环节包括：先进封装设备、湿制程、贴合/解键合、检测、自动化、热处理、翘曲量测、ABF 载板、IC substrate、光阻/介电/封装材料。投资上要看真实认证、设备验收、量产良率和收入确认，而不是只看公司是否有玻璃、面板或 TGV 概念。

近期弘塑，万润，印能表现非常不错，辛耘，均豪，志圣也可以，载板的欣兴则一直火热，今年以来股价也早已翻倍。

**中国路线：先做中国版「圆变方」，再谈 Glass Core**

 咱们国内不能一上来就把目标写成「2028 对标台积电 CoPoS + glass core」。

台积电的优势不是某一台 TGV 设备，而是客户、前道、封装、HBM 整合、EDA/DFM、良率、材料、测试与供应链协同。

国内AI芯片由于前道面积做不大，所以圆型interposer的放大空间还很多，转换成方形的急迫性没有海外那么高。但国产AI芯片前段做不大，所以依靠后段去放大interposer不断去拼接die，是增加国产AI芯片算力的最有效方法。

所以对于国产玻璃基板在先进封装的技术推进也应该走现实道路跟台积电一样分两步走。

第一步是中国版 CoPoS，先把 RDL/LSI 或类 LSI/bridge 的制造从圆形 wafer / reconstituted wafer 推向方形 panel，解决 panel-level fan-out、RDL、molding、搬运、对位、检测与翘曲。这一步不一定需要永久 glass core，也不需要一开始就做高难度 TGV substrate。

 

第二步才是玻璃芯载板 glass core substrate，当本土 AI ASIC、交换机 ASIC、CPO/NPO 光引擎或高端推理晶片需要更大 package、更高供电完整性和更低翘曲时，再导入 glass core + TGV + ABF build-up。

整体来说中国供应链可能会慢台积电1-2年落地。所以国产玻璃基板的概念基板上是 2030 以后的事了。

中国可形成「需求牵引 + 封装整合 + 面板/玻璃工程」三角。

需求端可能是华为升腾、寒武纪、海光、沐曦及本土交换芯片。

封装整合端可能是盛合晶微、渠梁或中芯这样的晶圆平台；面板/玻璃端可能是京东方、TCL 华星、沃格、凯盛、彩虹、厦门云天等。载板/PCB 端则需要深南、兴森、珠海越亚等 IC substrate / 高阶 PCB 能力配合。

 

设备端，国产化不能自动胜出。因为先进封装很多设备和材料目前仍可进口，中国封装厂会优先选择能保证良率的国际设备，比如 LPKF、EVG、Besi、ASMPT、KLA、Onto、Camtek、DISCO、TEL、MKS/Atotech 等。

国产设备要进入主线，必须在清洗、电镀、湿法、激光、AOI、量测、贴合/解键合、PVD、CMP、Track 等环节证明良率，而不是只靠国产替代叙事。

 

**京东方/TCL 能否复制群创行情**

京东方和 TCL 华星理论上能复制群创的一部分逻辑，但不能完全复制。

群创被拉动的核心，是被放在 TSMC + Ibiden 的验证图里，这相当于台积电背书。

京东方/TCL 的面板级玻璃能力很强，但中国缺少一个台积电型全球主导者，把客户需求、封装设计、材料设备、良率和量产订单全部拉在一起。

京东方/TCL 能做的不是「中国版台积电」，而是成为本土 panel-level packaging 和 glass engineering 的重要参与者。

它们可以先做临时 glass carrier、成熟制程 FOPLP、Micro LED、CPO/NPO 光学玻璃、RF/IPD、低 I/O glass interposer、面板级搬运和中试线。

 

若要进入 AI/HPC glass core substrate，必须与封装厂、载板厂、晶圆厂和终端客户共同验证。

因此，A 股若直接把「京东方/TCL = 群创 = 台积电 CoPoS 供应链」写成确定逻辑，那就是断章取义。

更合理的投资口径是：京东方/TCL 具备面板工程基础，可参与中国第一代圆变方与第二代 glass core 中试；但其收入节奏取决于本土客户、封装整合平台和进口/国产设备共同爬坡。

**两波投资节奏  不要把 carrier 当 substrate**

第一波是 2026–2028 年 CoPoS/Panel 化。这波的核心不是玻璃基板，而是圆变方。

受益者是面板级光刻、Track、PVD、电镀、蚀刻、检测、搬运、自动化、临时 bonding/debonding、release 材料、RDL 和封装整合供应链。玻璃在这一阶段主要是 carrier/制程端，增量有，但不多。

第二波是 2030 年前后玻璃心载板Glass Core Substrate。这波才是真正的玻璃基板价值量。它需要 glass core、TGV、孔壁金属化、电镀填孔、ABF build-up、低 Dk/Df 材料、翘曲控制、可靠性测试和 IC substrate 产能。这一波会带动 ABF 材料、载板结构、TGV 设备、检测与 PCB/主板协同变化。

 

第三个长期选项还是 glass interposer。但它不是台积电 AI 主线短期必经。若未来 CPO、光电互连、低损耗大面积互连或特定 chiplet 场景需要，它可能在更长期出现。对 2026–2030 的投资来说，不应把 glass interposer 当作主线收入假设。

最终定论：

CoPoS 不是玻璃基板革命，而是 CoWoS-L 的 panel 面板化；真正的玻璃基板革命是CoPoS后期 oS 段 glass core substrate玻璃心载板。

 

从真正的产业逻辑来看，2028 可以炒 CoPoS，但不应把它直接理解成 glass core substrate 大爆发，2030 前后才是 TGV、玻璃 core、ABF 变革与永久玻璃基板供应链真正需要严肃建模的时间点。

但是A股谁去炒真正的产业逻辑？

只要对标海外且逻辑说的大致能通，那A股对应的标的就有空间，所以5月以来群创暴涨了2.5倍，A股的京东方从4.2到目前的6.9，只涨了65%，这是否意味着还有空间？我还真不知道。

我自己也买了京东方，但很清楚就是短期炒个题材，本周打算找高点出了。

台股群创可能涨势逐渐回落，在加上本文的分析，短期实在别想玻璃基板在先进封装有很快的业绩落地，目前玻璃基板最快的应用就是CoPoS，但从技术细节来看，2028年的初代CoPoS并不会有什么玻璃基板会落地，最快也得等到2030年的二代CoPoS，而国内可能还得慢1-2年。

所以玻璃基板就跟着台股群创纯题材炒作，至于炒作啥时候上车啥时候下车，还是得先看一下市场热度，或者保守起见有赚就跑，我想没人能说得准，就看个人的理解与操作风格了。

        
        **本文最重要的七个结论**

1. CoPoS 的本质不是「玻璃基板革命」，而是把 CoWoS-L 类似的 LSI/RDL 中介层制造，从圆形 wafer 平台转到方形 panel 平台。

2. 初期 CoPoS 即使使用玻璃，也主要是临时基板 glass carrier / temporary carrier 的制程应用，做完后会去除，不是最终封装 BOM 里的永久玻璃基板。

Fan-out 封装多年来就大量使用临时玻璃 carrier，因此我们不能把 2028台积电的CoPoS 量产等同于玻璃基板爆发。

3. 真正有价值量、也真正需要 TGV、玻璃金属化、电镀填铜与上下 ABF build-up 的，是后期 oS 段的玻璃心载版 glass core substrate。它是 2030 的第二代CoPoS技术，而不是 2028 年初代 CoPoS 量产的故事。

4. 玻璃芯载板Glass core substrate 不是拿一片平玻璃垫在下面，而是把传统 package substrate 中间的 organic core 换成 glass core，上下仍然保留 ABF 或类 ABF build-up。玻璃没有干掉 ABF，也没有干掉 PCB。

5. 玻璃中介层 Glass interposer 似乎在短期没有用武之地，但它仍有长期研究价值，尤其在低损耗、高频、CPO、RF、光电封装场景，但在台积电 AI GPU 主线中，应该会有很长一段时间不需要把玻璃上移到 interposer，因为目前的技术路线中 LSI/RDL + glass core substrate 已能覆盖相当长一段路线。

6. 2026–2028 年是 CoWoS 与 CoPoS 第一代并行爬坡期，2028H2 若没有重大 delay，初代CoPoS 有机会先在 Feynman 或同级高端 SKU 上落地。2030 前后玻璃芯载版 glass core substrate 才可能在 AI/HPC 中明显放量。

7. 投资上要拆成两波：第一波看圆变方的 panel-level 制程设备与面板工程能力第二波看 glass core、TGV、电镀、ABF build-up、载板与检测。

把两波逻辑混成同一波，是大多数 A 股推票小作文的核心误导。

**CoPoS 到底是什么**

先用一个盖楼的比喻讲清楚。AI GPU 封装像是在一块地上建一座超大工厂，上面有 GPU、HBM、I/O die，彼此要靠非常密的道路相连。下面还要有地基，把电源、讯号和机械支撑一路接到主板。

CoWoS-L 就像是在一个圆形工地上先铺好局部高速道路 LSI、再用 RDL 把城市道路铺开，最后把整个方形的街区切出来接到底部地基。

CoPoS 做的不是把道路材料从矽变成玻璃，而是把工地从圆形变成方形。为什么有意义？

因为 AI 封装是方形，圆形 wafer 上切方形，边角浪费会越来越严重。当一个封装越做越大，方形 panel 基板更像一块方形土地，排方形楼盘土地利用面积可以更紧密。这就是所谓「圆变方」。

很多人听到 panel 面板就以为最终封装里留下了一大块玻璃板，这是误会。Panel 在这里首先是制造幅面、制程平台、临时工地。

最后留下的不是那块临时载板 glass carrier，而是在上面制作出来的 RDL、LSI、铜线、介电层、模封胶固化后的重构 interposer。临时载板像施工脚手架，楼盖好后脚手架拆掉，不能把脚手架算作房子的主材料。

这也解释了为什么「玻璃基板」题材容易被炒错。

玻璃临时载板 carrier 在早期的先进封装就有大量应用 Fan-out、wafer thinning、2.5D/3D 先进封装里本来就用了很多年，玻璃基板龙头康宁Corning 也明确把 advanced packaging glass carrier 定义为 temporary bonding 用于 fan-out 和先进封装的玻璃载具 。

玻璃临时载板这个市场是存在的，但它不是大家所期待大约 2030 年才会爆发的 glass core substrate，那是妥妥的两码事，很可惜A股的卖方们，对相关技术的区别几乎不得而知。

### **JPCA 2026：****台积电到底验证了什么**

JPCA Show 2026 之后，市场最关注的是郭明錤流出的一张台积电PPT，标题为 Glass Substrate Development for CoWoS。

它的价值不在于首次提到玻璃，而在于把 台积电未来的玻璃载板与日本ABF载板龙头揖斐电以及台湾面板厂群创放在同一个玻璃芯载板验证框架里。

郭明錤对该投影片的解读指出，这是玻璃芯载板，结构是 glass core 上下黏合 ABF，该技术对应 CoPoS 的 oS。同时他也提醒图中的 COP 是 coplanarity，不是 Chip-on-Package 。

图 1：使用者提供的 JPCA 2026 台积电 Glass Substrate Development for CoWoS 投影片截图。重点是 Glass-SBT vs Organic-SBT，属于 substrate 层验证。

![](images/3dbf6017b1184bed6f6e.jpg)

PPT的关键规格

1. 测试载具：0.8mm 玻璃核心、5 倍光罩（5x reticle）CoW 作为 test vehicle、整体封装尺寸 85 × 110 mm（已是大型 AI GPU 等级）。

2. 玻璃核心由 250 × 250 mm 母板切割而来，上下各黏合 ABF 增层，形成「ABF / 玻璃核心 / ABF」三层结构。

3. ABF 增层采用味之素（Ajinomoto）GL107 混搭 ABF-GCP，测试层数 24–28 层，正是 2027–2028 主流 AI 晶片规格。

4. 结果：未出现严重翘曲、未发生分层剥离（delamination）；封装共面度（Coplanarity）改善约 16%，并同步降低回路电感（L）与导通电阻（R），带来电源完整性（PI）改善。

这张图不是在证明 CoPoS 初代就用了玻璃 interposer。它是在说：台积电先拿 CoW/CoWoS 测试车去验证 glass core substrate 能不能改善超大封装的共面度、翘曲、CTE、刚性、R/L 与电源完整性。

也就是说，图里的玻璃在 package substrate 这一层，而不是 CoP 的 panel/RDL/LSI 这一层。

因此我们可以采用台积电的固定口径：CoP 段是 panel-level RDL/LSI interposer；oS 段是 package substrate。

2028 年初代CoPoS 跟CoWoS-L一样还是采用临时玻璃载板，但临时玻璃载板从圆形改成方形，仅此而已，oS段

还是会先用传统 organic-core ABF substrate。到了2030年的二代 CoPoS 才会把 substrate 中间的 organic core 换成 glass core玻璃芯载板。

市场上针对CoPoS可能delay以及2028如期推出众说纷纭，我们把事情拆开后，市场上很多看似矛盾的说法就能统一，CoPoS 还是会在 2028H2的Feyman导入，因为改动不大，on schedule是大概率，真正难点也就是玻璃芯载板 glass core substrate 得 2030 后才能真正放量。

**从 CoWoS-S/R/L 到 CoPoS**

CoWoS-S 是最经典的硅中介层方案，互连密度高、成熟度高，但大面积矽中介层成本高，尺寸越大越受 reticle stitching、良率和 wafer 利用率限制。

台积电官方 3DFabric 明确表示，CoWoS-S 可容纳约 3.3 倍 reticle、约 2700 mm² 的 interposer，更大尺寸推荐使用 CoWoS-L 或 CoWoS-R 。

CoWoS-R 是 RDL interposer 路线。它用聚合物介电层与铜线实现扇出与互连，成本和尺寸弹性比完整硅中介层好，但互连密度低于硅中介层。台积电给出的 CoWoS-R 最小 pitch 约 4 μm、线宽线距约 2/2 μm 。

CoWoS-L 则是我们理解未来 CoPoS 的关键。

 

CoWoS-L 不是完整硅中介层，而是 RDL-based interposer 重新布线中介层加 embedded LSI 预埋硅桥。

LSI 是局部硅桥，负责 GPU、HBM、chiplet 之间最需要高密度互连的区域。RDL 负责大面积供电、讯号扇出和较粗互连。这是一种务实折中，最需要高密度的地方用硅，其他区域用 RDL 和有机/聚合物结构。

CoPoS 初期可以理解为 CoWoS-L 的 panel 面板方形化。

它不是推翻 LSI/RDL，而是把这套 RDL + LSI + molding的重构 interposer 制造平台，从圆形 wafer 放大到方形 panel。

![](images/96b12b69150564cc00a1.png)

**CoPoS 的初代变化：不是玻璃基板，而是面板级制造工艺**

CoPoS 的 P 不是一块永久的「玻璃基板」。P 对应的是 panel-level process面板级制程，是中介层/RDL 的方形制造幅面。

根据TrendForce的最新报告，台积电 CoPoS 的标准化 310×310mm panel玻璃基板，2026 年是设备与材料验证期，2027 年 pilot中试，2028H2 量产。

很多人会把这个310×310mm的玻璃基板当成玻璃在先进封装的跨越式应用，事实上这只是原本的12寸圆形玻璃临时载板变成310×310mm的方形临时载板。

临时载板一直都是用玻璃，临时载板本身也没啥价值量，临时载板圆变方的价值增量几乎没有，更大的增量是在能加工方形基板的制程设备上。

所以TrendForce的最新报告，同时又把玻璃芯载板 glass core substrate 放到 CoPoS 之后，商业规模化更可能在 2030 后。TrendForce的这个拆分很重要也足够清晰，跟笔者聊的台积电的CoPoS技术演变相吻合。

如果有人说「CoPoS 量产，所以玻璃基板 2028 大爆发」，这就是把 panel carrier临时玻璃载板、panel process面板制程、glass core substrate 玻璃芯载板混为一谈。

 

再重复一遍，310×310 mm 玻璃基板是 CoP 段的方形临时载版，它是 glass carrier，在 panel 上形成 RDL/LSI/molding interposer 后，最终封装里不会留下了 310×310 mm 的玻璃基板，因为它只是最终要被去除的临时载板，上面不需要有任何加工，金额很低。

制程由圆形改成方形，也不是普通 LCD 面板制程设备原封不动搬来做 CoPoS。

高阶 FPD 光刻机已能做到 1.5–2 μm 级线宽，例如 Canon Gen 8 FPD 光刻机公布过 1.5 μm resolution 与 ±0.35 μm overlay，后续机型也公布 ±0.30 μm overlay 。但 CoPoS 难点不只是线宽，还包括半导体级颗粒、PVD/seed、铜电镀、RDL 应力、翘曲、KGD 对位、全检与可靠性。

 

所以，面板厂的优势不是「直接把 LCD 产线拿来做 AI 封装」，而是它们有大面积玻璃搬运、清洗、贴合、曝光、自动化、平整度与面板级工程经验。

真正 AI CoPoS 需要的是面板级尺寸加半导体级精度。这是群创、友达、京东方、TCL 华星等面板厂能参与但不能单独主导的原因。

**fan-out先进封装早就有临时玻璃载板glass carrier**

Fan-out 封装的基本逻辑是把已知良品 die 放到临时 carrier 上，用 molding compound 固化成重构 wafer 或 panel，再做 RDL、植球、切割。

ASE日月光对 Panel FO 的说法是，传统 fan-out 用圆形 wafer 作为 reconstituted carrier 支撑 chip、RDL 和 molding，而panel-level fan-out 改用矩形 panel 作为 reconstituted carrier，以提高面积利用率 。

上述的FOPLP和我们讨论 CoPoS 的「圆变方」非常相似。

玻璃基板龙头Corning 也明确提供 advanced packaging glass carriers，用于 wafer thinning、fan-out packaging 和 2.5D/3D advanced packaging 的 temporary bonding。

也就是说，玻璃临时载板 carrier 不是 2028 年才出现的新物种，而是先进封装里由来已久的制程载具。

 

临时载板也有价值，但他以前的CoWoS-L就存在所以没有太大增量，而且临时载板更像周转治具或半耗材，附加价值低，不像玻璃芯载板 glass core substrate 那样每颗高端封装都永久消耗一片核心玻璃。

临时 carrier 能否重复使用，要看污染、刮伤、热循环、残胶、TTV、边缘崩裂与规格漂移。高精度 carrier 不是无限次使用，也不是每颗封装一次性消耗。

产线需要 carrier 库存、备品和更换，但不能把它按每颗 AI GPU 线性放大。

因此，初期 CoPoS 主要是 carrier 端和制程端，而不是永久 BOM 端，初期CoPoS不会有任何玻璃基板存在最终的封装成品。

它会带来玻璃 carrier临时载板、release film剥离膜、temporary bonding/debonding临时键合解键合、清洗、搬运和检测的增量，但这些价值量远小于未来 oS 段 glass core substrate玻璃芯载板，这才是市场炒作且期待的真正主餐。

**2030 年才是玻璃芯载板 Glass Core Substrate 的主战场**

Glass core substrate 位于 oS，也就是 on substrate 这一层。传统高阶封装 substrate 可以简化成 organic core + 上下 ABF build-up。

Glass core substrate 则是 glass core + 上下 ABF build-up。它不是把 ABF 干掉，而是把核心骨架换成玻璃，让地基更平、更硬、更稳，再在上下继续用 ABF build-up 做多层铜线、via、pad 和 BGA 扇出。

为何需要ABF+玻璃芯载板的三明治结构，因为玻璃芯载板透过TGV可以实现垂直互联，但没办法做横向拓展互联，航向就得靠ABF。

台积电先在 oS 段导入玻璃核心glass core又是什么考量？

因为substrate这一层对互连密度的要求低于 interposer 层，但对机械稳定性、翘曲、共面度、CTE、供电完整性和尺寸稳定性非常敏感。

超大 AI 封装越做越大，最怕地基不平、热膨胀不一致、回流焊后翘曲、BGA 接点失效、电源回路变差。玻璃 core 的刚性、平整度、低翘曲和尺寸稳定性刚好对症。

但 glass core substrate 绝不是只靠平整度。它必须做 TGV、孔壁处理、阻障层/种子层、铜填孔或电镀、上下 ABF build-up、电测、可靠性与全检。

全球TGV龙头德国LPKF 把 TGV 称为 glass substrates 的 backbone，因为它连接 substrate 两侧的 redistribution layers，支撑多 die 封装 。

基板大厂旭硝子 AGC 也把 TGV glass substrate 用于 semiconductor packaging 和 glass interposer，并列出 wafer 与 panel 形态、通孔、孔径与 pitch 等规格 。

所以，真正高价值的玻璃基板不是一片平玻璃，而是一套玻璃 core + TGV + 金属化 + 电镀 + ABF build-up + 可靠性验证的系统工程。它比 CoPoS 初代难很多，也正因如此，TrendForce 把 glass core substrate 的商业规模化放到 2030 后 。

![](images/21b53428457fe683a094.png)

# **
**
**Glass Interposer 是长期选项之一，但不是台积电主线**

 行业一直以来研究玻璃中介层 glass interposer，这并非没有意义。

玻璃具有低介电损耗、高电阻率、尺寸稳定、大面积和低成本潜力，对 RF、毫米波、CPO、光电封装、低损耗高速互连有吸引力。IMAPS 等资料也长期提到 TGV interposer 的优势，包括低损耗、低介电常数、高电阻等 。

但把玻璃从 substrate core 上移到 interposer 层，难度也上了一个台阶。

Interposer 要直接连 GPU、HBM、chiplet，要求线宽、线距、TGV/RDL 密度、对位、热管理和良率都高很多。玻璃热导率差、脆性高、大面积 TGV 和细 RDL 良率难，这些都比 substrate core 难得多。

台积电目前已有一条非常合理的工程折中，上面用 CoP 的 LSI/RDL 保住高速互连，下面用 glass core substrate 改善地基。

这条路并不需要把 glass 立刻上移到 interposer，也能支撑 40 倍 reticle 甚至更大的 SoW-X/CoPoS 系统整合想像。换句话说，glass interposer 不是没价值，但不是台积电 AI GPU 主线的必经路。

长期来看，glass interposer 更可能先在 CPO、光电、RF、低损耗大面积互连或特定 chiplet 场景落地。

如果未来 TGV 密度、玻璃金属化、热管理和 panel RDL 良率大幅成熟，它有机会替代一部分硅 interposer 或补充 LSI/RDL。但至少在 2030甚至到2035年的台积电 AI/HPC 主线中，最务实的路线仍是 CoP panel-level LSI/RDL + oS glass core substrate。

**台积电路线时间表：2026–2028 CoPoS，2030 Glass Core**

台积电资深副总张晓强 2026 技术论坛说，5.5-reticle CoWoS 已在生产，14-reticle CoWoS 预计 2028 年量产，可整合约 10 颗大型 compute die 和 20 颗 HBM，2029 年还会 beyond-14 reticle；SoW-X 约 40 reticle，定位是系统级 wafer 整合 。

对 Feynman 或同级产品而言，若封装要容纳更多 compute tile、更多 HBM、更多 I/O 和更大系统互连，panel-level RDL/LSI 的经济性与面积扩张能力会越来越重要。

所以依照台积电官方公布的roadmap，2026–2027 的CoPoS将以设备材料验证和 pilot 中试为主。2028H2 若没重大 delay，CoPoS 在 NVIDIA 高端 SKU 优先导入；2030 前后，ASIC 阵营才开始更普遍跟进。

真正对玻璃基板行业有大帮助的玻璃芯载板则要往后推。2028 年可以有 CoPoS，但不等于 glass core substrate 大量放量。

2030 年左右，当 TGV、电镀、ABF 贴合、良率、供应链与客户验证成熟后，玻璃芯载板glass core substrate 才更可能成为高端 AI/HPC 的明显增量。

 

![](images/5a9dcdaf7b5911c3e7c5.png)

# **
**
**设备与材料：第一波看圆变方，第二波看 TGV**

 CoPoS 第一波受益链不应该是「玻璃基板链」。更正确是 panel-level RDL/interposer 制程链。

这包括大型 panel 搬运、自动化、清洗、涂布显影 Track、曝光、PVD seed、电镀、蚀刻、RDL 检测、翘曲量测、临时 bonding/debonding、release film、carrier 清洗与回收。

这些环节可能吸收一部分面板产业经验，也需要半导体级升级，主要还是由原有的半导体及面板设备商来主导。

第二波才是目前炒作的玻璃基板 glass core substrate 链。它包括低碱/无碱玻璃 core、TGV 成孔、LIDE 或雷射改质、湿蚀刻、孔壁金属化、seed/barrier、铜填孔、电镀、CMP/平坦化、ABF lamination、低 Dk/Df 介电材料、电测、X-ray、AOI、SAM、热循环可靠性、切割与边缘裂纹控制。

因此，材料端在 2028 前后没有想像中剧烈。polymer dielectric、molding compound、ABF、铜、电镀液、光阻、release film、glass carrier 都是既有CoWoS-L体系延伸。

真正材料变化在 2030 前后：substrate core 从有机材料变玻璃后，ABF 与玻璃的界面黏着、热应力匹配、TGV 金属化、填孔可靠性都会变成新战场。

**群创为何涨，利多在哪里**

群创这波被市场重估，不是因为它马上成为台积电 CoPoS 主导或主力厂商，也不是因为它立刻有 AI GPU玻璃心载板 glass core substrate 的巨额收入，而是因为 JPCA 投影片把群创放入 TSMC + Ibiden 的 glass substrate 验证框架。从5月起涨至今已有接近3倍的涨幅。

市场把群创从面板景气循环股重新估值为 AI 先进封装潜在供应链。

群创在CoPoS链条上的真实价值在大尺寸玻璃、面板级制程、搬运、清洗、平整度控制、贴合、自动化和可能的 TGV/玻璃加工中试能力。

这些能力可以参与第一波 CoPoS panel 化，也可以参与第二波 glass core substrate 验证。但它不是替代台积电，更不是替代 Ibiden 或 ABF 载板厂。

 

台湾其他可能受益环节包括：先进封装设备、湿制程、贴合/解键合、检测、自动化、热处理、翘曲量测、ABF 载板、IC substrate、光阻/介电/封装材料。投资上要看真实认证、设备验收、量产良率和收入确认，而不是只看公司是否有玻璃、面板或 TGV 概念。

近期弘塑，万润，印能表现非常不错，辛耘，均豪，志圣也可以，载板的欣兴则一直火热，今年以来股价也早已翻倍。

**中国路线：先做中国版「圆变方」，再谈 Glass Core**

 咱们国内不能一上来就把目标写成「2028 对标台积电 CoPoS + glass core」。

台积电的优势不是某一台 TGV 设备，而是客户、前道、封装、HBM 整合、EDA/DFM、良率、材料、测试与供应链协同。

国内AI芯片由于前道面积做不大，所以圆型interposer的放大空间还很多，转换成方形的急迫性没有海外那么高。但国产AI芯片前段做不大，所以依靠后段去放大interposer不断去拼接die，是增加国产AI芯片算力的最有效方法。

所以对于国产玻璃基板在先进封装的技术推进也应该走现实道路跟台积电一样分两步走。

第一步是中国版 CoPoS，先把 RDL/LSI 或类 LSI/bridge 的制造从圆形 wafer / reconstituted wafer 推向方形 panel，解决 panel-level fan-out、RDL、molding、搬运、对位、检测与翘曲。这一步不一定需要永久 glass core，也不需要一开始就做高难度 TGV substrate。

 

第二步才是玻璃芯载板 glass core substrate，当本土 AI ASIC、交换机 ASIC、CPO/NPO 光引擎或高端推理晶片需要更大 package、更高供电完整性和更低翘曲时，再导入 glass core + TGV + ABF build-up。

整体来说中国供应链可能会慢台积电1-2年落地。所以国产玻璃基板的概念基板上是 2030 以后的事了。

中国可形成「需求牵引 + 封装整合 + 面板/玻璃工程」三角。

需求端可能是华为升腾、寒武纪、海光、沐曦及本土交换芯片。

封装整合端可能是盛合晶微、渠梁或中芯这样的晶圆平台；面板/玻璃端可能是京东方、TCL 华星、沃格、凯盛、彩虹、厦门云天等。载板/PCB 端则需要深南、兴森、珠海越亚等 IC substrate / 高阶 PCB 能力配合。

 

设备端，国产化不能自动胜出。因为先进封装很多设备和材料目前仍可进口，中国封装厂会优先选择能保证良率的国际设备，比如 LPKF、EVG、Besi、ASMPT、KLA、Onto、Camtek、DISCO、TEL、MKS/Atotech 等。

国产设备要进入主线，必须在清洗、电镀、湿法、激光、AOI、量测、贴合/解键合、PVD、CMP、Track 等环节证明良率，而不是只靠国产替代叙事。

 

**京东方/TCL 能否复制群创行情**

京东方和 TCL 华星理论上能复制群创的一部分逻辑，但不能完全复制。

群创被拉动的核心，是被放在 TSMC + Ibiden 的验证图里，这相当于台积电背书。

京东方/TCL 的面板级玻璃能力很强，但中国缺少一个台积电型全球主导者，把客户需求、封装设计、材料设备、良率和量产订单全部拉在一起。

京东方/TCL 能做的不是「中国版台积电」，而是成为本土 panel-level packaging 和 glass engineering 的重要参与者。

它们可以先做临时 glass carrier、成熟制程 FOPLP、Micro LED、CPO/NPO 光学玻璃、RF/IPD、低 I/O glass interposer、面板级搬运和中试线。

 

若要进入 AI/HPC glass core substrate，必须与封装厂、载板厂、晶圆厂和终端客户共同验证。

因此，A 股若直接把「京东方/TCL = 群创 = 台积电 CoPoS 供应链」写成确定逻辑，那就是断章取义。

更合理的投资口径是：京东方/TCL 具备面板工程基础，可参与中国第一代圆变方与第二代 glass core 中试；但其收入节奏取决于本土客户、封装整合平台和进口/国产设备共同爬坡。

**两波投资节奏  不要把 carrier 当 substrate**

第一波是 2026–2028 年 CoPoS/Panel 化。这波的核心不是玻璃基板，而是圆变方。

受益者是面板级光刻、Track、PVD、电镀、蚀刻、检测、搬运、自动化、临时 bonding/debonding、release 材料、RDL 和封装整合供应链。玻璃在这一阶段主要是 carrier/制程端，增量有，但不多。

第二波是 2030 年前后玻璃心载板Glass Core Substrate。这波才是真正的玻璃基板价值量。它需要 glass core、TGV、孔壁金属化、电镀填孔、ABF build-up、低 Dk/Df 材料、翘曲控制、可靠性测试和 IC substrate 产能。这一波会带动 ABF 材料、载板结构、TGV 设备、检测与 PCB/主板协同变化。

 

第三个长期选项还是 glass interposer。但它不是台积电 AI 主线短期必经。若未来 CPO、光电互连、低损耗大面积互连或特定 chiplet 场景需要，它可能在更长期出现。对 2026–2030 的投资来说，不应把 glass interposer 当作主线收入假设。

最终定论：

CoPoS 不是玻璃基板革命，而是 CoWoS-L 的 panel 面板化；真正的玻璃基板革命是CoPoS后期 oS 段 glass core substrate玻璃心载板。

 

从真正的产业逻辑来看，2028 可以炒 CoPoS，但不应把它直接理解成 glass core substrate 大爆发，2030 前后才是 TGV、玻璃 core、ABF 变革与永久玻璃基板供应链真正需要严肃建模的时间点。

但是A股谁去炒真正的产业逻辑？

只要对标海外且逻辑说的大致能通，那A股对应的标的就有空间，所以5月以来群创暴涨了2.5倍，A股的京东方从4.2到目前的6.9，只涨了65%，这是否意味着还有空间？我还真不知道。

我自己也买了京东方，但很清楚就是短期炒个题材，本周打算找高点出了。

台股群创可能涨势逐渐回落，在加上本文的分析，短期实在别想玻璃基板在先进封装有很快的业绩落地，目前玻璃基板最快的应用就是CoPoS，但从技术细节来看，2028年的初代CoPoS并不会有什么玻璃基板会落地，最快也得等到2030年的二代CoPoS，而国内可能还得慢1-2年。

所以玻璃基板就跟着台股群创纯题材炒作，至于炒作啥时候上车啥时候下车，还是得先看一下市场热度，或者保守起见有赚就跑，我想没人能说得准，就看个人的理解与操作风格了。

        **本文最重要的七个结论**

1. CoPoS 的本质不是「玻璃基板革命」，而是把 CoWoS-L 类似的 LSI/RDL 中介层制造，从圆形 wafer 平台转到方形 panel 平台。

2. 初期 CoPoS 即使使用玻璃，也主要是临时基板 glass carrier / temporary carrier 的制程应用，做完后会去除，不是最终封装 BOM 里的永久玻璃基板。

Fan-out 封装多年来就大量使用临时玻璃 carrier，因此我们不能把 2028台积电的CoPoS 量产等同于玻璃基板爆发。

3. 真正有价值量、也真正需要 TGV、玻璃金属化、电镀填铜与上下 ABF build-up 的，是后期 oS 段的玻璃心载版 glass core substrate。它是 2030 的第二代CoPoS技术，而不是 2028 年初代 CoPoS 量产的故事。

4. 玻璃芯载板Glass core substrate 不是拿一片平玻璃垫在下面，而是把传统 package substrate 中间的 organic core 换成 glass core，上下仍然保留 ABF 或类 ABF build-up。玻璃没有干掉 ABF，也没有干掉 PCB。

5. 玻璃中介层 Glass interposer 似乎在短期没有用武之地，但它仍有长期研究价值，尤其在低损耗、高频、CPO、RF、光电封装场景，但在台积电 AI GPU 主线中，应该会有很长一段时间不需要把玻璃上移到 interposer，因为目前的技术路线中 LSI/RDL + glass core substrate 已能覆盖相当长一段路线。

6. 2026–2028 年是 CoWoS 与 CoPoS 第一代并行爬坡期，2028H2 若没有重大 delay，初代CoPoS 有机会先在 Feynman 或同级高端 SKU 上落地。2030 前后玻璃芯载版 glass core substrate 才可能在 AI/HPC 中明显放量。

7. 投资上要拆成两波：第一波看圆变方的 panel-level 制程设备与面板工程能力第二波看 glass core、TGV、电镀、ABF build-up、载板与检测。

把两波逻辑混成同一波，是大多数 A 股推票小作文的核心误导。

**CoPoS 到底是什么**

先用一个盖楼的比喻讲清楚。AI GPU 封装像是在一块地上建一座超大工厂，上面有 GPU、HBM、I/O die，彼此要靠非常密的道路相连。下面还要有地基，把电源、讯号和机械支撑一路接到主板。

CoWoS-L 就像是在一个圆形工地上先铺好局部高速道路 LSI、再用 RDL 把城市道路铺开，最后把整个方形的街区切出来接到底部地基。

CoPoS 做的不是把道路材料从矽变成玻璃，而是把工地从圆形变成方形。为什么有意义？

因为 AI 封装是方形，圆形 wafer 上切方形，边角浪费会越来越严重。当一个封装越做越大，方形 panel 基板更像一块方形土地，排方形楼盘土地利用面积可以更紧密。这就是所谓「圆变方」。

很多人听到 panel 面板就以为最终封装里留下了一大块玻璃板，这是误会。Panel 在这里首先是制造幅面、制程平台、临时工地。

最后留下的不是那块临时载板 glass carrier，而是在上面制作出来的 RDL、LSI、铜线、介电层、模封胶固化后的重构 interposer。临时载板像施工脚手架，楼盖好后脚手架拆掉，不能把脚手架算作房子的主材料。

这也解释了为什么「玻璃基板」题材容易被炒错。

玻璃临时载板 carrier 在早期的先进封装就有大量应用 Fan-out、wafer thinning、2.5D/3D 先进封装里本来就用了很多年，玻璃基板龙头康宁Corning 也明确把 advanced packaging glass carrier 定义为 temporary bonding 用于 fan-out 和先进封装的玻璃载具 。

玻璃临时载板这个市场是存在的，但它不是大家所期待大约 2030 年才会爆发的 glass core substrate，那是妥妥的两码事，很可惜A股的卖方们，对相关技术的区别几乎不得而知。

### **JPCA 2026：****台积电到底验证了什么**

JPCA Show 2026 之后，市场最关注的是郭明錤流出的一张台积电PPT，标题为 Glass Substrate Development for CoWoS。

它的价值不在于首次提到玻璃，而在于把 台积电未来的玻璃载板与日本ABF载板龙头揖斐电以及台湾面板厂群创放在同一个玻璃芯载板验证框架里。

郭明錤对该投影片的解读指出，这是玻璃芯载板，结构是 glass core 上下黏合 ABF，该技术对应 CoPoS 的 oS。同时他也提醒图中的 COP 是 coplanarity，不是 Chip-on-Package 。

图 1：使用者提供的 JPCA 2026 台积电 Glass Substrate Development for CoWoS 投影片截图。重点是 Glass-SBT vs Organic-SBT，属于 substrate 层验证。

![](images/3dbf6017b1184bed6f6e.jpg)

PPT的关键规格

1. 测试载具：0.8mm 玻璃核心、5 倍光罩（5x reticle）CoW 作为 test vehicle、整体封装尺寸 85 × 110 mm（已是大型 AI GPU 等级）。

2. 玻璃核心由 250 × 250 mm 母板切割而来，上下各黏合 ABF 增层，形成「ABF / 玻璃核心 / ABF」三层结构。

3. ABF 增层采用味之素（Ajinomoto）GL107 混搭 ABF-GCP，测试层数 24–28 层，正是 2027–2028 主流 AI 晶片规格。

4. 结果：未出现严重翘曲、未发生分层剥离（delamination）；封装共面度（Coplanarity）改善约 16%，并同步降低回路电感（L）与导通电阻（R），带来电源完整性（PI）改善。

这张图不是在证明 CoPoS 初代就用了玻璃 interposer。它是在说：台积电先拿 CoW/CoWoS 测试车去验证 glass core substrate 能不能改善超大封装的共面度、翘曲、CTE、刚性、R/L 与电源完整性。

也就是说，图里的玻璃在 package substrate 这一层，而不是 CoP 的 panel/RDL/LSI 这一层。

因此我们可以采用台积电的固定口径：CoP 段是 panel-level RDL/LSI interposer；oS 段是 package substrate。

2028 年初代CoPoS 跟CoWoS-L一样还是采用临时玻璃载板，但临时玻璃载板从圆形改成方形，仅此而已，oS段

还是会先用传统 organic-core ABF substrate。到了2030年的二代 CoPoS 才会把 substrate 中间的 organic core 换成 glass core玻璃芯载板。

市场上针对CoPoS可能delay以及2028如期推出众说纷纭，我们把事情拆开后，市场上很多看似矛盾的说法就能统一，CoPoS 还是会在 2028H2的Feyman导入，因为改动不大，on schedule是大概率，真正难点也就是玻璃芯载板 glass core substrate 得 2030 后才能真正放量。

**从 CoWoS-S/R/L 到 CoPoS**

CoWoS-S 是最经典的硅中介层方案，互连密度高、成熟度高，但大面积矽中介层成本高，尺寸越大越受 reticle stitching、良率和 wafer 利用率限制。

台积电官方 3DFabric 明确表示，CoWoS-S 可容纳约 3.3 倍 reticle、约 2700 mm² 的 interposer，更大尺寸推荐使用 CoWoS-L 或 CoWoS-R 。

CoWoS-R 是 RDL interposer 路线。它用聚合物介电层与铜线实现扇出与互连，成本和尺寸弹性比完整硅中介层好，但互连密度低于硅中介层。台积电给出的 CoWoS-R 最小 pitch 约 4 μm、线宽线距约 2/2 μm 。

CoWoS-L 则是我们理解未来 CoPoS 的关键。

 

CoWoS-L 不是完整硅中介层，而是 RDL-based interposer 重新布线中介层加 embedded LSI 预埋硅桥。

LSI 是局部硅桥，负责 GPU、HBM、chiplet 之间最需要高密度互连的区域。RDL 负责大面积供电、讯号扇出和较粗互连。这是一种务实折中，最需要高密度的地方用硅，其他区域用 RDL 和有机/聚合物结构。

CoPoS 初期可以理解为 CoWoS-L 的 panel 面板方形化。

它不是推翻 LSI/RDL，而是把这套 RDL + LSI + molding的重构 interposer 制造平台，从圆形 wafer 放大到方形 panel。

![](images/96b12b69150564cc00a1.png)

**CoPoS 的初代变化：不是玻璃基板，而是面板级制造工艺**

CoPoS 的 P 不是一块永久的「玻璃基板」。P 对应的是 panel-level process面板级制程，是中介层/RDL 的方形制造幅面。

根据TrendForce的最新报告，台积电 CoPoS 的标准化 310×310mm panel玻璃基板，2026 年是设备与材料验证期，2027 年 pilot中试，2028H2 量产。

很多人会把这个310×310mm的玻璃基板当成玻璃在先进封装的跨越式应用，事实上这只是原本的12寸圆形玻璃临时载板变成310×310mm的方形临时载板。

临时载板一直都是用玻璃，临时载板本身也没啥价值量，临时载板圆变方的价值增量几乎没有，更大的增量是在能加工方形基板的制程设备上。

所以TrendForce的最新报告，同时又把玻璃芯载板 glass core substrate 放到 CoPoS 之后，商业规模化更可能在 2030 后。TrendForce的这个拆分很重要也足够清晰，跟笔者聊的台积电的CoPoS技术演变相吻合。

如果有人说「CoPoS 量产，所以玻璃基板 2028 大爆发」，这就是把 panel carrier临时玻璃载板、panel process面板制程、glass core substrate 玻璃芯载板混为一谈。

 

再重复一遍，310×310 mm 玻璃基板是 CoP 段的方形临时载版，它是 glass carrier，在 panel 上形成 RDL/LSI/molding interposer 后，最终封装里不会留下了 310×310 mm 的玻璃基板，因为它只是最终要被去除的临时载板，上面不需要有任何加工，金额很低。

制程由圆形改成方形，也不是普通 LCD 面板制程设备原封不动搬来做 CoPoS。

高阶 FPD 光刻机已能做到 1.5–2 μm 级线宽，例如 Canon Gen 8 FPD 光刻机公布过 1.5 μm resolution 与 ±0.35 μm overlay，后续机型也公布 ±0.30 μm overlay 。但 CoPoS 难点不只是线宽，还包括半导体级颗粒、PVD/seed、铜电镀、RDL 应力、翘曲、KGD 对位、全检与可靠性。

 

所以，面板厂的优势不是「直接把 LCD 产线拿来做 AI 封装」，而是它们有大面积玻璃搬运、清洗、贴合、曝光、自动化、平整度与面板级工程经验。

真正 AI CoPoS 需要的是面板级尺寸加半导体级精度。这是群创、友达、京东方、TCL 华星等面板厂能参与但不能单独主导的原因。

**fan-out先进封装早就有临时玻璃载板glass carrier**

Fan-out 封装的基本逻辑是把已知良品 die 放到临时 carrier 上，用 molding compound 固化成重构 wafer 或 panel，再做 RDL、植球、切割。

ASE日月光对 Panel FO 的说法是，传统 fan-out 用圆形 wafer 作为 reconstituted carrier 支撑 chip、RDL 和 molding，而panel-level fan-out 改用矩形 panel 作为 reconstituted carrier，以提高面积利用率 。

上述的FOPLP和我们讨论 CoPoS 的「圆变方」非常相似。

玻璃基板龙头Corning 也明确提供 advanced packaging glass carriers，用于 wafer thinning、fan-out packaging 和 2.5D/3D advanced packaging 的 temporary bonding。

也就是说，玻璃临时载板 carrier 不是 2028 年才出现的新物种，而是先进封装里由来已久的制程载具。

 

临时载板也有价值，但他以前的CoWoS-L就存在所以没有太大增量，而且临时载板更像周转治具或半耗材，附加价值低，不像玻璃芯载板 glass core substrate 那样每颗高端封装都永久消耗一片核心玻璃。

临时 carrier 能否重复使用，要看污染、刮伤、热循环、残胶、TTV、边缘崩裂与规格漂移。高精度 carrier 不是无限次使用，也不是每颗封装一次性消耗。

产线需要 carrier 库存、备品和更换，但不能把它按每颗 AI GPU 线性放大。

因此，初期 CoPoS 主要是 carrier 端和制程端，而不是永久 BOM 端，初期CoPoS不会有任何玻璃基板存在最终的封装成品。

它会带来玻璃 carrier临时载板、release film剥离膜、temporary bonding/debonding临时键合解键合、清洗、搬运和检测的增量，但这些价值量远小于未来 oS 段 glass core substrate玻璃芯载板，这才是市场炒作且期待的真正主餐。

**2030 年才是玻璃芯载板 Glass Core Substrate 的主战场**

Glass core substrate 位于 oS，也就是 on substrate 这一层。传统高阶封装 substrate 可以简化成 organic core + 上下 ABF build-up。

Glass core substrate 则是 glass core + 上下 ABF build-up。它不是把 ABF 干掉，而是把核心骨架换成玻璃，让地基更平、更硬、更稳，再在上下继续用 ABF build-up 做多层铜线、via、pad 和 BGA 扇出。

为何需要ABF+玻璃芯载板的三明治结构，因为玻璃芯载板透过TGV可以实现垂直互联，但没办法做横向拓展互联，航向就得靠ABF。

台积电先在 oS 段导入玻璃核心glass core又是什么考量？

因为substrate这一层对互连密度的要求低于 interposer 层，但对机械稳定性、翘曲、共面度、CTE、供电完整性和尺寸稳定性非常敏感。

超大 AI 封装越做越大，最怕地基不平、热膨胀不一致、回流焊后翘曲、BGA 接点失效、电源回路变差。玻璃 core 的刚性、平整度、低翘曲和尺寸稳定性刚好对症。

但 glass core substrate 绝不是只靠平整度。它必须做 TGV、孔壁处理、阻障层/种子层、铜填孔或电镀、上下 ABF build-up、电测、可靠性与全检。

全球TGV龙头德国LPKF 把 TGV 称为 glass substrates 的 backbone，因为它连接 substrate 两侧的 redistribution layers，支撑多 die 封装 。

基板大厂旭硝子 AGC 也把 TGV glass substrate 用于 semiconductor packaging 和 glass interposer，并列出 wafer 与 panel 形态、通孔、孔径与 pitch 等规格 。

所以，真正高价值的玻璃基板不是一片平玻璃，而是一套玻璃 core + TGV + 金属化 + 电镀 + ABF build-up + 可靠性验证的系统工程。它比 CoPoS 初代难很多，也正因如此，TrendForce 把 glass core substrate 的商业规模化放到 2030 后 。

![](images/21b53428457fe683a094.png)

# **
**
**Glass Interposer 是长期选项之一，但不是台积电主线**

 行业一直以来研究玻璃中介层 glass interposer，这并非没有意义。

玻璃具有低介电损耗、高电阻率、尺寸稳定、大面积和低成本潜力，对 RF、毫米波、CPO、光电封装、低损耗高速互连有吸引力。IMAPS 等资料也长期提到 TGV interposer 的优势，包括低损耗、低介电常数、高电阻等 。

但把玻璃从 substrate core 上移到 interposer 层，难度也上了一个台阶。

Interposer 要直接连 GPU、HBM、chiplet，要求线宽、线距、TGV/RDL 密度、对位、热管理和良率都高很多。玻璃热导率差、脆性高、大面积 TGV 和细 RDL 良率难，这些都比 substrate core 难得多。

台积电目前已有一条非常合理的工程折中，上面用 CoP 的 LSI/RDL 保住高速互连，下面用 glass core substrate 改善地基。

这条路并不需要把 glass 立刻上移到 interposer，也能支撑 40 倍 reticle 甚至更大的 SoW-X/CoPoS 系统整合想像。换句话说，glass interposer 不是没价值，但不是台积电 AI GPU 主线的必经路。

长期来看，glass interposer 更可能先在 CPO、光电、RF、低损耗大面积互连或特定 chiplet 场景落地。

如果未来 TGV 密度、玻璃金属化、热管理和 panel RDL 良率大幅成熟，它有机会替代一部分硅 interposer 或补充 LSI/RDL。但至少在 2030甚至到2035年的台积电 AI/HPC 主线中，最务实的路线仍是 CoP panel-level LSI/RDL + oS glass core substrate。

**台积电路线时间表：2026–2028 CoPoS，2030 Glass Core**

台积电资深副总张晓强 2026 技术论坛说，5.5-reticle CoWoS 已在生产，14-reticle CoWoS 预计 2028 年量产，可整合约 10 颗大型 compute die 和 20 颗 HBM，2029 年还会 beyond-14 reticle；SoW-X 约 40 reticle，定位是系统级 wafer 整合 。

对 Feynman 或同级产品而言，若封装要容纳更多 compute tile、更多 HBM、更多 I/O 和更大系统互连，panel-level RDL/LSI 的经济性与面积扩张能力会越来越重要。

所以依照台积电官方公布的roadmap，2026–2027 的CoPoS将以设备材料验证和 pilot 中试为主。2028H2 若没重大 delay，CoPoS 在 NVIDIA 高端 SKU 优先导入；2030 前后，ASIC 阵营才开始更普遍跟进。

真正对玻璃基板行业有大帮助的玻璃芯载板则要往后推。2028 年可以有 CoPoS，但不等于 glass core substrate 大量放量。

2030 年左右，当 TGV、电镀、ABF 贴合、良率、供应链与客户验证成熟后，玻璃芯载板glass core substrate 才更可能成为高端 AI/HPC 的明显增量。

 

![](images/5a9dcdaf7b5911c3e7c5.png)

# **
**
**设备与材料：第一波看圆变方，第二波看 TGV**

 CoPoS 第一波受益链不应该是「玻璃基板链」。更正确是 panel-level RDL/interposer 制程链。

这包括大型 panel 搬运、自动化、清洗、涂布显影 Track、曝光、PVD seed、电镀、蚀刻、RDL 检测、翘曲量测、临时 bonding/debonding、release film、carrier 清洗与回收。

这些环节可能吸收一部分面板产业经验，也需要半导体级升级，主要还是由原有的半导体及面板设备商来主导。

第二波才是目前炒作的玻璃基板 glass core substrate 链。它包括低碱/无碱玻璃 core、TGV 成孔、LIDE 或雷射改质、湿蚀刻、孔壁金属化、seed/barrier、铜填孔、电镀、CMP/平坦化、ABF lamination、低 Dk/Df 介电材料、电测、X-ray、AOI、SAM、热循环可靠性、切割与边缘裂纹控制。

因此，材料端在 2028 前后没有想像中剧烈。polymer dielectric、molding compound、ABF、铜、电镀液、光阻、release film、glass carrier 都是既有CoWoS-L体系延伸。

真正材料变化在 2030 前后：substrate core 从有机材料变玻璃后，ABF 与玻璃的界面黏着、热应力匹配、TGV 金属化、填孔可靠性都会变成新战场。

**群创为何涨，利多在哪里**

群创这波被市场重估，不是因为它马上成为台积电 CoPoS 主导或主力厂商，也不是因为它立刻有 AI GPU玻璃心载板 glass core substrate 的巨额收入，而是因为 JPCA 投影片把群创放入 TSMC + Ibiden 的 glass substrate 验证框架。从5月起涨至今已有接近3倍的涨幅。

市场把群创从面板景气循环股重新估值为 AI 先进封装潜在供应链。

群创在CoPoS链条上的真实价值在大尺寸玻璃、面板级制程、搬运、清洗、平整度控制、贴合、自动化和可能的 TGV/玻璃加工中试能力。

这些能力可以参与第一波 CoPoS panel 化，也可以参与第二波 glass core substrate 验证。但它不是替代台积电，更不是替代 Ibiden 或 ABF 载板厂。

 

台湾其他可能受益环节包括：先进封装设备、湿制程、贴合/解键合、检测、自动化、热处理、翘曲量测、ABF 载板、IC substrate、光阻/介电/封装材料。投资上要看真实认证、设备验收、量产良率和收入确认，而不是只看公司是否有玻璃、面板或 TGV 概念。

近期弘塑，万润，印能表现非常不错，辛耘，均豪，志圣也可以，载板的欣兴则一直火热，今年以来股价也早已翻倍。

**中国路线：先做中国版「圆变方」，再谈 Glass Core**

 咱们国内不能一上来就把目标写成「2028 对标台积电 CoPoS + glass core」。

台积电的优势不是某一台 TGV 设备，而是客户、前道、封装、HBM 整合、EDA/DFM、良率、材料、测试与供应链协同。

国内AI芯片由于前道面积做不大，所以圆型interposer的放大空间还很多，转换成方形的急迫性没有海外那么高。但国产AI芯片前段做不大，所以依靠后段去放大interposer不断去拼接die，是增加国产AI芯片算力的最有效方法。

所以对于国产玻璃基板在先进封装的技术推进也应该走现实道路跟台积电一样分两步走。

第一步是中国版 CoPoS，先把 RDL/LSI 或类 LSI/bridge 的制造从圆形 wafer / reconstituted wafer 推向方形 panel，解决 panel-level fan-out、RDL、molding、搬运、对位、检测与翘曲。这一步不一定需要永久 glass core，也不需要一开始就做高难度 TGV substrate。

 

第二步才是玻璃芯载板 glass core substrate，当本土 AI ASIC、交换机 ASIC、CPO/NPO 光引擎或高端推理晶片需要更大 package、更高供电完整性和更低翘曲时，再导入 glass core + TGV + ABF build-up。

整体来说中国供应链可能会慢台积电1-2年落地。所以国产玻璃基板的概念基板上是 2030 以后的事了。

中国可形成「需求牵引 + 封装整合 + 面板/玻璃工程」三角。

需求端可能是华为升腾、寒武纪、海光、沐曦及本土交换芯片。

封装整合端可能是盛合晶微、渠梁或中芯这样的晶圆平台；面板/玻璃端可能是京东方、TCL 华星、沃格、凯盛、彩虹、厦门云天等。载板/PCB 端则需要深南、兴森、珠海越亚等 IC substrate / 高阶 PCB 能力配合。

 

设备端，国产化不能自动胜出。因为先进封装很多设备和材料目前仍可进口，中国封装厂会优先选择能保证良率的国际设备，比如 LPKF、EVG、Besi、ASMPT、KLA、Onto、Camtek、DISCO、TEL、MKS/Atotech 等。

国产设备要进入主线，必须在清洗、电镀、湿法、激光、AOI、量测、贴合/解键合、PVD、CMP、Track 等环节证明良率，而不是只靠国产替代叙事。

 

**京东方/TCL 能否复制群创行情**

京东方和 TCL 华星理论上能复制群创的一部分逻辑，但不能完全复制。

群创被拉动的核心，是被放在 TSMC + Ibiden 的验证图里，这相当于台积电背书。

京东方/TCL 的面板级玻璃能力很强，但中国缺少一个台积电型全球主导者，把客户需求、封装设计、材料设备、良率和量产订单全部拉在一起。

京东方/TCL 能做的不是「中国版台积电」，而是成为本土 panel-level packaging 和 glass engineering 的重要参与者。

它们可以先做临时 glass carrier、成熟制程 FOPLP、Micro LED、CPO/NPO 光学玻璃、RF/IPD、低 I/O glass interposer、面板级搬运和中试线。

 

若要进入 AI/HPC glass core substrate，必须与封装厂、载板厂、晶圆厂和终端客户共同验证。

因此，A 股若直接把「京东方/TCL = 群创 = 台积电 CoPoS 供应链」写成确定逻辑，那就是断章取义。

更合理的投资口径是：京东方/TCL 具备面板工程基础，可参与中国第一代圆变方与第二代 glass core 中试；但其收入节奏取决于本土客户、封装整合平台和进口/国产设备共同爬坡。

**两波投资节奏  不要把 carrier 当 substrate**

第一波是 2026–2028 年 CoPoS/Panel 化。这波的核心不是玻璃基板，而是圆变方。

受益者是面板级光刻、Track、PVD、电镀、蚀刻、检测、搬运、自动化、临时 bonding/debonding、release 材料、RDL 和封装整合供应链。玻璃在这一阶段主要是 carrier/制程端，增量有，但不多。

第二波是 2030 年前后玻璃心载板Glass Core Substrate。这波才是真正的玻璃基板价值量。它需要 glass core、TGV、孔壁金属化、电镀填孔、ABF build-up、低 Dk/Df 材料、翘曲控制、可靠性测试和 IC substrate 产能。这一波会带动 ABF 材料、载板结构、TGV 设备、检测与 PCB/主板协同变化。

 

第三个长期选项还是 glass interposer。但它不是台积电 AI 主线短期必经。若未来 CPO、光电互连、低损耗大面积互连或特定 chiplet 场景需要，它可能在更长期出现。对 2026–2030 的投资来说，不应把 glass interposer 当作主线收入假设。

最终定论：

CoPoS 不是玻璃基板革命，而是 CoWoS-L 的 panel 面板化；真正的玻璃基板革命是CoPoS后期 oS 段 glass core substrate玻璃心载板。

 

从真正的产业逻辑来看，2028 可以炒 CoPoS，但不应把它直接理解成 glass core substrate 大爆发，2030 前后才是 TGV、玻璃 core、ABF 变革与永久玻璃基板供应链真正需要严肃建模的时间点。

但是A股谁去炒真正的产业逻辑？

只要对标海外且逻辑说的大致能通，那A股对应的标的就有空间，所以5月以来群创暴涨了2.5倍，A股的京东方从4.2到目前的6.9，只涨了65%，这是否意味着还有空间？我还真不知道。

我自己也买了京东方，但很清楚就是短期炒个题材，本周打算找高点出了。

台股群创可能涨势逐渐回落，在加上本文的分析，短期实在别想玻璃基板在先进封装有很快的业绩落地，目前玻璃基板最快的应用就是CoPoS，但从技术细节来看，2028年的初代CoPoS并不会有什么玻璃基板会落地，最快也得等到2030年的二代CoPoS，而国内可能还得慢1-2年。

所以玻璃基板就跟着台股群创纯题材炒作，至于炒作啥时候上车啥时候下车，还是得先看一下市场热度，或者保守起见有赚就跑，我想没人能说得准，就看个人的理解与操作风格了。

        
                
                

![](/assets_dweb/logo@1x.png)

                知识星球
                
        
        
            
            扫码加入星球
            查看更多优质内容
        
        https://wx.zsxq.com/mweb/views/joingroup/join_group.html?group_id=88888812815442

---

Source: https://articles.zsxq.com/id_mxb3bqwqdd5x.html

Linked from topic_id: 45544525245211428
