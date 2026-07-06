# 从 CoWoS 到 SoW-X 不只是拼大，台积电全面重构系统

        
            [来自：
                半导体大佬的会议室](https://wx.zsxq.com/group/88888812815442)
        
        
            
                

![](images/39ac34f1b548792d9368.jpg)

                吴梓豪leslie
            
            2026年04月26日 18:48
        
        
            过去几年，AI 芯片的叙事一直围绕算力展开：GPU die 越来越大，HBM 越堆越多，CoWoS 产能越来越紧，先进封装从幕后工艺变成了整个 AI 产业链最核心的瓶颈之一。

但如果我们只把这条线理解成“interposer 越做越大”“HBM 从 8 颗变 12 颗、再变 20 颗”，其实会错过台积电路线图背后真正发生的变化。

台积电展示的先进封装路线，从 2024 年的 3.3 倍 reticle，到 2026 年 5.5 倍 reticle，再到 2027 年 9.5 倍、2028 年 14 倍，最后到 2029 年 SoW-X 的 40 倍 reticle、64 颗 HBM，表面上看是一条“封装面积持续放大”的曲线，但本质上不是简单把 CoWoS-S 或 CoWoS-L 不断拼大，而是 AI 系统边界正在被重新定义。

过去，一个 AI 加速器系统的层级大致是，die 在封装里，封装在载板上，载板接到 PCB，PCB 再组成服务器，服务器再进入 rack，rack 之间再靠 NVLink、以太网、光模块和交换芯片连接。

每跨一层，互连距离变长，延迟变大，功耗上升，带宽密度下降。AI 时代的真正问题，已经不是单颗芯片算力不够，而是算力、显存、带宽、I/O、供电、散热、rack 内互连全部同时撞墙。

所以台积电的封装路线，不只是“把芯片封得更大”，而是试图把原本属于 board、rack 甚至系统级的互连，逐步压缩进 package、panel、wafer-system 里面。也就是说，先进封装正在从芯片制造的后段工艺，变成系统架构本身。

## **
**

![](images/b589f2e913d0417cd7ee.jpg)

## **
**

## **3.3× 到 5.5× 不只是 HBM 增加，而是封装内部开始系统化**

台积电路线图里最容易被忽略的地方，是 2024 年 3.3× reticle 与 2026 年 5.5× reticle 的差别。

表面看，2024 年是 8 颗 HBM，2026 年变成 12 颗 HBM，好像只是显存堆栈数量增加。

但图中真正值得注意的是，2026 年开始，在 GPU/SoC 上下方出现了红色区域。这个红色区域必定不是 GPU compute die，更合理的判断是 I/O die、SerDes die、NVLink PHY、die-to-die 互连、封装边缘连接芯片，或者其他 active interconnect chiplet。

这意味着 5.5× reticle 不是简单的大 GPU + 更多 HBM，而是从传统的计算芯片封装，开始走向系统级封装。

  

这一步非常关键。过去 GPU die 自己承担大量计算、I/O、互连控制功能。但随着 HBM 数量增加、NVLink 带宽提升、CPO/光互连逐渐靠近封装边缘，compute die 不可能无限承担所有外部 I/O。

把 I/O、PHY、SerDes 或互连功能拆出来，放在封装边缘或 GPU 上下方，是非常自然的演进。

所以 2026 Rubin 时代的 5.5× reticle，不应该只看作12 HBM 的 CoWoS，而应该看作 AI 封装从计算芯片 + 存储向计算、存储、I/O、互连分工的系统封装过渡。

这也解释了为什么 2024 年 3.3× 的图里没有这些红色区域，而 2026、2027、2028 年的 roadmap 里逐渐出现。封装面积放大以后，真正变化的不只是 HBM 数量，而是封装内部的功能分区开始接近一个小系统。

**Rubin 仍然是 2.5D 主线，SoIC 还无法大规模上车**

从产品对应看，2026 年 Rubin 最确定的技术主线仍然是 CoWoS-L + HBM4。它会比 Blackwell 更大，HBM 数量更多，I/O 更复杂，但它未必需要把 3D SoIC 作为核心叙事。

原因很简单，英伟达过去的 GPU 路线一直偏向超大 die。Blackwell、Hopper 这一类产品，本质上还是 800mm² 级别大 die 或大 chiplet加 HBM，通过 CoWoS-S 或 CoWoS-L 平铺整合。

只要超大 die 还能制造，只要 CoWoS-L 还能继续放大，英伟达就没有必要太早承担大规模 logic-on-logic 3D 堆叠的热和良率风险。

AMD MI300 是台积电 SoIC + CoWoS 结合的早期样板，但它不能被简单理解成GPU compute die 叠 GPU compute die。

它更准确的意义是，SoIC 先在 compute chiplet、base die/active interposer、I/O/互连功能之间建立高密度垂直连接，再通过 CoWoS 把 HBM 纳入同一个 2.5D 系统。

因此，MI300 证明的不是大 GPU die 必须上下堆叠，而是 SoIC 可以作为 CoWoS 体系内的 3D 集成模块，先从 base die、I/O、cache、SRAM 或小 chiplet 这些更适合的功能块切入。

MI300不是简单把 CPU、GPU、HBM 全部平铺在 interposer 上，而是先把 compute chiplet 叠在 base die / active interposer 上，再通过 2.5D CoWoS 把这个 compute complex 与 HBM 横向整合。

MI300 证明了一件事：3D SoIC 可以先局部进入 CoWoS，而不是一开始就把所有东西垂直堆叠。也就是说，3D 并不是取代 2.5D，而是嵌入 2.5D 体系之中，先在局部功能块上使用。

但 NVIDIA 的 Rubin 不一定要走同样节奏。Rubin 更可能仍然以大 die / chiplet + HBM4 + CoWoS-L 为主。即便有 SoIC，也更可能是局部或辅助功能，而不是 GPU 主体大规模 3D 堆叠。

这一点很重要。我们不能看到台积电大幅度扩产 SoIC，就直接推导出 Rubin GPU 大 die 要立刻上下堆叠。更合理的解释是，SoIC 的第一批大规模需求，很可能来自 SRAM/cache、小 chiplet 或局部 I/O，有这方面情却需求的正是26 GTC的 Groq 3 LPU。

## **3D SoIC 的真正入口  SRAM、cache、I/O 与小 die**

3D SoIC 到底会用在哪里？这是整条路线能不能成立的关键。

由于散热问题无法解决，直接把两个高功耗大 GPU die 叠起来是不现实的。GPU 本身功耗已经进入数百瓦甚至千瓦级封装时代，大 die 热流密度极高，如果再叠一层高功耗 logic，散热会非常困难，良率和测试也会变得极其复杂。

更合理的顺序是：

![](images/9225e771199c9a183036.png)

其中最确定的是 SRAM。

6T SRAM 结构已经很难继续按逻辑制程同步微缩。先进逻辑节点里，逻辑晶体管密度还能继续提升，但 SRAM 面积缩放越来越慢，片上 cache 越来越贵。AI 推理，尤其是低延迟推理、LPU 或 SRAM-heavy 架构，对大容量、低延迟、高带宽 SRAM 的需求很强。

把 SRAM 单独做成 die，然后通过 hybrid bonding / SoIC 堆在 logic die 上，比继续在大逻辑 die 里平面铺 SRAM 更合理。其实这正是2nmm以下世代SRAM无法有效同步微缩的必要方法。

而且 SRAM die 功耗密度低于 GPU compute die，热问题相对更可控。因此，SRAM-on-logic 很可能是 3D SoIC 在 AI 领域最先真正放量的方向。

这也解释了台积电扩 SoIC 的一个重要逻辑。当前 LPU 3 仍在三星代工，而下一代 LPU 4 已经开始在台积电流片，那么 SoIC 扩产最直接的用途之一，可能就是 LPU 的 logic die + SRAM die 堆叠。相比把 Rubin GPU 主 die 直接 3D 化，LPU/SRAM 的需求更符合 SoIC 的工程现实。

I/O die、PHY、SerDes、NVLink、未来 CPO 的电接口，也可能成为 SoIC 的候选，但短期未必最急。因为台积电 roadmap 图中红色区域已经给了 I/O 或互连 PHY 平铺空间，它们可以先放在封装边缘，通过 CoWoS-L 的 RDL 或 local silicon bridge 连接，不一定马上需要垂直堆叠。

所以更准确的判断是：Rubin 这一代，SoIC 未必是 GPU 主体；Rubin Ultra 到 Feynman 之间，SoIC 的真正主角更可能是 SRAM/cache、LPU、小 chiplet 和局部 I/O。等到散热、HBM 定制化、CoPoS 与 IMC-Si 进一步成熟后，memory-on-logic 才会进入更主线的位置。

## **HBM 与 GPU 立体集成必须靠冷却打开**

即便海力士在2024年就公布HBM4e与GPU立体堆叠的技术路线，但一直以来笔者会比较保守地看待 HBM-on-GPU。原因很直接，GPU 是最高热流密度区域，HBM 又对温度敏感，把 HBM 直接压在 GPU 上方，这非常不现实。

但如果把 SK hynix 的 HBM roadmap、HBM4E 的 custom 趋势、台积电 IMC-Si 冷却技术放在一起看，这个判断可以更乐观地收敛。

未来 HBM 与 GPU/ASIC 的立体集成，已经不是会不会发生，而是从哪一代、以什么形式、先在什么区域发生。

HBM4 开始，base die 已经越来越像逻辑组件，而不是传统意义上的纯存储底座。

HBM4E 之后，custom HBM、logic base die、GPU/ASIC 深度定制会更加明显。也就是说，HBM 正在从标准存储器，变成 AI 系统立体封装中的一部分。

之前HBM之父金正浩表示AI时代主导权正从GPU转向内存,被似懂非懂的网友误解。

未来AI的存储绝对价值会远高于逻辑GPU,但作为标准品,即便未来custom客制化也是依附于逻辑制程,并融入整个平台中,所以金正浩的表态只能是其站在存储角度的发言,只能说价值量存储绝对是遥遥领先,重要度最高,但主导权并不会因为金正浩的立场性发言而改变分毫,只要你明白这个体系如何运行,就能清楚的明白。

未来HBM与HBF成为AI系统立体封装的一部分时,IMC-Si 的意义就凸显出来。如今我们随便挑出一个系统级环节,就能明白这一切并非存储厂家能主导,系统级层面要解决的问题太多了。

![](images/5d52f4352fa71193533c.png)

目前台积电公开展示的 IMC-Si 技術仍然是服务于 2.5D CoWoS 封装的顶部散热增强方案。也就是说，GPU 与 HBM 仍然横向平铺在 CoWoS/RDL/interposer 上，冷却结构从传统的 TIM、lid、cold plate 进一步靠近 silicon die，以减少中间热阻，而不是已经在 GPU 与 HBM 之间插入液冷层。

当前更接近的结构是：

![](images/00af2167a6846169f8c4.png)

台积电在 ECTC 2025 展示的 direct-to-silicon liquid cooling，是把液冷结构整合到 CoWoS 平台上，重点是应对 AI/HPC 芯片功耗密度继续上升后的热墙。

台积电的 IMC-Si 正在 CoWoS-R 有机 interposer 测试载具上验证，测试载具模拟 4 SoC + 8 HBM 的封装，并展示了在 40°C 水、10 L/min 流量下带走超过 3000W 均匀功耗的能力。 

这说明 IMC-Si 的第一步价值非常明确，让 2.5D 大封装继续放大，让 GPU/SoC 顶部散热路径更短、更直接。 但它还不是完整的 GPU-HBM 立体堆叠散热方案。

在 IMC-Si 之外，台积电也在探索更高导热材料来替代或增强传统 lid/顶盖结构。

台积电正在评估 SiC/diamond 等材料，用它们的高导热性和机械强度来改善先进封装的散热与可靠性。  

这里可以理解成另一条并行路线：IMC-Si 负责把液冷推近 silicon，金刚石或碳化硅 lid 负责提高顶部热扩散与热传导效率。

因此，当前可验证的散热技术组合更像是：

![](images/696ef82d5d96e1b541d2.png)

真正的 HBM-on-GPU，不能只靠顶部有 IMC-Si。因为一旦 HBM 放在 GPU 上方，热流路径会变得完全不同，GPU 的热会向上进入 HBM，HBM 自身也会发热，而中间层如果没有冷却或热隔离，HBM 就会被夹在高热区域中。这个结构和当前 HBM 横向平铺完全不同。

所以，未来若要实现 GPU 与 HBM 的立体堆叠，比较合理的路径不是一步到位，而是分阶段演进。

第一阶段，是当前的 2.5D 平铺 + 顶部 direct-to-silicon cooling。GPU 与 HBM 仍然平铺，IMC-Si 主要覆盖高热 GPU/SoC 区域，金刚石或 SiC lid 帮助提升顶部热扩散能力。这一阶段解决的是大封装继续扩功耗的问题。

这里有个值得注意的问题，目前大肆炒作的SiC interposer必然是错的，先不说interposer早就不承担散热功能这种基本常识，目前台积电在测试的是SiC作为Carrier，更重点是主要是多晶SiC根本不是二级市场炒作的单晶SiC。

第二阶段，是 GPU 与 HBM 分区冷却。也就是说，GPU 上方有更强的 direct-to-silicon cooling，HBM 上方也有独立热路径或局部冷却结构，但 HBM 仍不一定直接压在 GPU 正上方。这个阶段会让 HBM 更靠近 GPU，但仍然保留一定横向分布，以降低热耦合风险。

第三阶段，才是真正的 HBM-on-GPU 立体堆叠。这个阶段至少需要三条热路径同时成立：HBM 上方要有高效散热路径，GPU/logic 上方或背面要有高效散热路径，GPU 与 HBM 中间还需要 interlayer cooling、microfluidic channel、热隔离层或极高导热中介层。否则 HBM 堆在 GPU 上方会被 GPU 热源持续烘烤，很难稳定量产。

真正的未来结构可以理解成：

![](images/39fa7632c8b7d6b29ec6.png)

也就是说，金刚石或 SiC lid 可以改善顶部热扩散，IMC-Si 可以把冷却推近 die，但如果要做 HBM-on-GPU，GPU 与 HBM 中间仍然需要一层真正有效的热管理结构。 没有中间层冷却，立体堆叠仍然难以成立。

针对 3D stacked dies，microfluidic interlayer cooling 被认为是解决中间层热堆积的重要路径，微軟的研究也提到，微流道可以用于 3D stacked dies 的 interlayer cooling，并可针对 GPU server 里的 SoC 与 HBM 做 targeted cooling。  

此外，关于 diamond inter-tier cooling 的研究也显示，高导热材料可以作为 3D IC 冷却策略的一部分，用来替代部分介质层或热通孔，改善垂直堆叠中的热传导。 

因此，對於未來3D SoIC 的HBM-on-GPU 立体堆叠，我們的判斷可以收敛為：

IMC-Si 是 HBM-on-GPU 的必要条件，但不是充分条件，金刚石/SiC lid 是顶部热扩散的重要补充，但也不能单独解决中间层热堆积。

真正让 GPU 与 HBM 立体堆叠成立的，是 IMC-Si、interlayer cooling、高导热 lid、CoPoS/CoWoS 底座、电源完整性与封装良率共同成熟。

这也是为什么 2026 Rubin 仍然大概率是 HBM 平铺，2027 Rubin Ultra 可能只是更紧密的 2.5D/准 3D 探索，而 2028 Feynman 才更像是 HBM4E/custom HBM、IMC-Si 与更复杂立体集成同时成熟的关键节点。但这一切都是建立在无数的新技术之上，Delay的风险并不低。

## **
**

![](images/b589f2e913d0417cd7ee.jpg)

## **
**

## **Rubin Ultra 的 4 die 争议：平台能力与产品量产不是一回事**

台积电 roadmap 里 2027 年展示 9.5× reticle，看起来可以支持 4 个 compute die、12 颗 HBM4E 以及上下 I/O 区域。这说明台积电平台能力已经准备向更大封装推进。

但这并不等于 NVIDIA Rubin Ultra 一定会采用最满配的 4 die 单封装方案。

最近市场传出 Rubin Ultra 从 4 die 改成 2 die，本质不是“技术不会做”，而是量产取舍。4 die + 12/16 HBM 的单封装方案，理论上很激进，但现实中会遇到一连串问题。虽然这些问题并非不是无解，但综合成本可量，或许更保守方案更为安全。

![](images/6fec5a9817c296c6618f.png)

所以 2027 年可能出现一个非常典型的分化：台积电平台能力已经可以展示 9.5× reticle，但 NVIDIA 的实际产品出于良率、成本、交付和供应链节奏考虑，选择更保守的 2×AB1 方案。

这里的 AB1 可以理解成一种中间集成单元。不是把 4 个 die 全部一次性压到一个超大封装里，而是先把 2 个 die 做成一个较小单元，再通过封装或系统互连组合成更大的产品。

这会牺牲部分带宽和延迟，但换来更好的量产稳定性。这并不否定台积电 roadmap，反而说明先进封装正在进入一个新阶段，平台能力和客户实际产品选择不再完全同步。

台积电需要先把能力往前推，客户则会根据产品良率、成本和交付节奏选择吃多少。

因此，Rubin Ultra 的 4 die 争议不是路线错误，而是 2027 年正好处在 CoWoS-L 极限扩大、SoIC 局部导入、CoPoS 尚未完全成熟之前的过渡期。

## **CoWoS-L、CoPoS、SoIC、SoW-X 不是替代关系，而是技术栈融合**

很多讨论容易把台积电技术路线说成线性替代：CoWoS-L 之后是 CoPoS，CoPoS 之后是 SoW-X。或者简单分成 CoWoS-L 是高端，CoPoS 是顶级，SoW-X 是极端方案。这种说法不准确。

更正确的理解应该是：

![](images/ff72831f0846e208be74.png)

它们不是谁取代谁，而是会在不同层级最终汇集台积电平台里，未来台积电CoWoS/CoPoS会把各种五花八门的技术全部集成再一起。

CoWoS-L 的意义，是用 RDL base + local silicon bridge，减少对大面积 65nm silicon interposer 的依赖，解决 CoWoS-S 大硅 interposer 产能和面积扩展问题。它不是整片 65nm interposer 的无限放大，而是通过局部硅和 RDL，把封装面积继续做大。

CoPoS 的意义，是把底座从 wafer-based 扩展到 panel-based。随着封装面积越来越大，圆形 wafer 的面积利用率越来越不适合超大矩形封装，panel 更适合大尺寸封装的生产效率。CoPoS 不是简单“比 CoWoS-L 更高级”，而是大面积封装制造方式的变化。

SoIC 的意义，是提供垂直互连能力。它可以嵌入 CoWoS-L，也可以嵌入 CoPoS。未来在 CoPoS 上使用 SoIC，在 SoIC 上整合 SRAM、I/O、HBM 或小 compute die，是非常自然的方向。

SoW-X 则不是取代 CoPoS，而是在更大系统尺度上使用类似思想。它不是单纯一个封装，而是把系统边界推进到 wafer-scale / system-scale。

所以未来真正的顶级形态，不是“选择 CoPoS 或 SoIC 或 SoW-X”，而是 CoPoS 做大面积底座，SoIC 做局部垂直堆叠，IMC-Si 解决热墙，CPO/COUPE 解决高速光电 I/O，SoW-X 把系统边界进一步放大。

## **玻璃基板与 CoPoS：不是玻璃带来翘曲，而是大尺寸要求更好的翘曲控制**

CoPoS 讨论中还有一个容易混淆的点：玻璃基板。

玻璃基板的优势之一，正是低 CTE、更好尺寸稳定性、更低翘曲、更适合高密度互连和大尺寸封装。

所以不能说换 CoPoS 后翘曲更严重，是因为玻璃。更准确的说法是，当封装从 wafer/package 尺寸走向更大 panel 尺寸后，整体应力、翘曲、热膨胀匹配、贴装平整度都会更难控制，而玻璃基板正是解决这些问题的重要材料方案之一。

![](images/9b6f4ba17f8dad88c165.png)

因此，2028 Feynman 时代，更可能是 CoWoS-L 继续承担主力，CoPoS 在顶级 SKU 或特定系统中开始导入。到了 2029 Feynman Ultra，CoPoS + SoIC + IMC-Si + optical I/O 的融合才会更明显。

## **SoW-X 不是 Cerebras，也不是整张 65nm interposer**

SoW-X 是另一个容易被误解的技术。

第一种误解，是把 SoW-X 说成 Cerebras。

Cerebras WSE 是整片 wafer 做成一个 monolithic AI chip，依靠片上 SRAM 和特殊 mesh 架构。这种路线已经存在多年，也证明了 wafer-scale 能做，但它并没有成为通用 AI 加速器主流。

原因很简单：它的架构特殊，生态特殊，没有 HBM，适合特定工作负载，但不是 GPU/HBM 主流训练架构。

SoW-X 不一样。它更像是整片 wafer / system-scale 平台，加多个 known-good logic die、多个 HBM、多个 I/O die、connector/conductor 与系统级互连。

也就是说，Cerebras 是wafer 是一个芯片，SoW-X 是wafer 是一个系统。Cerebras 是改芯片架构，SoW-X 是改系统封装架构。

第二种误解，是把 SoW-X 理解成整张 65nm silicon interposer。

如果 SoW-X 真是整张 65nm interposer，那它马上就会遇到致命问题，65nm 产能不够，整片硅 interposer 成本太高，TSV/BEOL 良率风险太大，整片 wafer 级被动 interposer 几乎无法经济量产。

所以 SoW-X 不可能是 CoWoS-S 的简单放大版。它是 CoWoS-L / CoPoS 思想在系统尺度上的延伸，使用 RDL、局部 silicon bridge、hybrid bonding、panel/wafer-level base、edge connector/conductor，把多个 logic、HBM、I/O 组织成 wafer-scale system。

这也解释了台積電roadmap图中右上角 SoW-X 里的 connector。越往后走，封装边缘的系统连接、I/O、供电、信号分发会变得越来越重要。红色 die 更合理地理解为 I/O/互连功能块，而 connector是更高层的系统连接结构。

SoW-X 的战略意义在于，台积电把 wafer-scale 从 Cerebras 式特殊芯片架构，转成先进封装与系统集成平台。

## **2025–2029 产品与技术如何对应**

如果把整个路线收敛成产品时间线，可以这样理解。

2025 年 Blackwell 仍然是 CoWoS-L 主导。封装很大，HBM 很多，液冷重要性提升，但本质仍然是大 GPU + HBM 的 2.5D 系统。

2026 年 Rubin 进入 5.5× reticle。主线是 CoWoS-L + HBM4 + 更复杂 I/O。

roadmaop的红色区域代表 I/O/PHY/互连功能开始进入封装内部，系统分工更明确。但 Rubin 不會是SoIC 大规模上车，它仍然主要是 2.5D 放大。

2027 年 Rubin Ultra 对应 9.5× reticle 平台能力。台积电理论上可以支持更大封装、更复杂 chiplet、更高 HBM 数量。但 NVIDIA 产品端可能因为良率、成本、交付选择更保守的 2 die 或 2×AB1 方案。

与此同时，笔者把台积电北美论坛 roadmap上没有提及的技术加进来，同学们才能更好的去理解未来AI芯片的变化，3D SoIC 产能开始被 LPU、SRAM/cache、小 ASIC、局部 I/O 消耗，而IMC-Si 初步进入量产准备。

2028 年 Feynman 是真正关键节点。

CoWoS-L 达到 14× reticle 级别，CoPoS 开始导入或进入早期量产，HBM4E/custom HBM 与 logic 的关系更紧密，IMC-Si 逐渐成熟，SRAM/I/O/HBM 的局部 3D 集成开始进入主线。

Feynman 这一代很可能是从 2.5D 平铺向 3D memory-on-logic 转折的关键阶段。

2029 年 Feynman Ultra 则可能进入 CoPoS + SoIC + IMC-Si + SoW-X 的系统级融合。主流高端产品仍可能是 CoPoS/CoWoS-L + SoIC 的组合，SoW-X 则作为极少数 wafer-scale system 方案出现。

![](images/932fd498ad11a61cee52.png)

## **最终主线：横向更大、纵向更密、散热更近、互连更光、系统更大**

如果把所有技术拆开看，会觉得非常复杂：

CoWoS-L、CoPoS、SoIC、IMC-Si、SoW-X、CPO、COUPE、HBM4E、custom HBM、SRAM stack、I/O die、红色 PHY 区域，每一个都是一条线。

但把它们放在一起，主线其实很清楚。

![](images/265ee56416a150e58875.png)

台积电不是在单纯追求更大的 interposer，而是在用先进封装重构 AI 系统。过去属于 PCB 和 rack 的互连，正在被推进到封装内部。

过去属于封装外部的冷却，正在靠近 silicon；过去平铺在旁边的存储，正在向 logic 上方或更近距离靠拢；过去分散在系统里的 I/O，正在变成封装内的独立 die 或 PHY 区域。

因此，AI 封装未来不是简单从 CoWoS-L 走向 CoPoS，也不是简单从 2.5D 走向 3D，而是多条技术线同时融合。

2026 Rubin 是 2.5D CoWoS-L 的系统化；2027 Rubin Ultra 是平台能力与产品量产之间的过渡；2028 Feynman 是 HBM4E、IMC-Si、SoIC、CoPoS 同时成熟的转折点；2029 Feynman Ultra 则可能进入 CoPoS + SoIC + SoW-X 的系统级封装时代。

这条路线的终点，不是单颗 GPU 更大，而是整个 AI 系统被重新封装。

另外从 roadmap 带来的硅面积需求增长将会是一个非常恐怖的数字，这是笔者早有预期但现实比我预期增长更大许多，上面的所有要点加起來，正是我不论从短中长期，一直选择重压台积电的原因。

        
        过去几年，AI 芯片的叙事一直围绕算力展开：GPU die 越来越大，HBM 越堆越多，CoWoS 产能越来越紧，先进封装从幕后工艺变成了整个 AI 产业链最核心的瓶颈之一。

但如果我们只把这条线理解成“interposer 越做越大”“HBM 从 8 颗变 12 颗、再变 20 颗”，其实会错过台积电路线图背后真正发生的变化。

台积电展示的先进封装路线，从 2024 年的 3.3 倍 reticle，到 2026 年 5.5 倍 reticle，再到 2027 年 9.5 倍、2028 年 14 倍，最后到 2029 年 SoW-X 的 40 倍 reticle、64 颗 HBM，表面上看是一条“封装面积持续放大”的曲线，但本质上不是简单把 CoWoS-S 或 CoWoS-L 不断拼大，而是 AI 系统边界正在被重新定义。

过去，一个 AI 加速器系统的层级大致是，die 在封装里，封装在载板上，载板接到 PCB，PCB 再组成服务器，服务器再进入 rack，rack 之间再靠 NVLink、以太网、光模块和交换芯片连接。

每跨一层，互连距离变长，延迟变大，功耗上升，带宽密度下降。AI 时代的真正问题，已经不是单颗芯片算力不够，而是算力、显存、带宽、I/O、供电、散热、rack 内互连全部同时撞墙。

所以台积电的封装路线，不只是“把芯片封得更大”，而是试图把原本属于 board、rack 甚至系统级的互连，逐步压缩进 package、panel、wafer-system 里面。也就是说，先进封装正在从芯片制造的后段工艺，变成系统架构本身。

## **
**

![](images/b589f2e913d0417cd7ee.jpg)

## **
**

## **3.3× 到 5.5× 不只是 HBM 增加，而是封装内部开始系统化**

台积电路线图里最容易被忽略的地方，是 2024 年 3.3× reticle 与 2026 年 5.5× reticle 的差别。

表面看，2024 年是 8 颗 HBM，2026 年变成 12 颗 HBM，好像只是显存堆栈数量增加。

但图中真正值得注意的是，2026 年开始，在 GPU/SoC 上下方出现了红色区域。这个红色区域必定不是 GPU compute die，更合理的判断是 I/O die、SerDes die、NVLink PHY、die-to-die 互连、封装边缘连接芯片，或者其他 active interconnect chiplet。

这意味着 5.5× reticle 不是简单的大 GPU + 更多 HBM，而是从传统的计算芯片封装，开始走向系统级封装。

  

这一步非常关键。过去 GPU die 自己承担大量计算、I/O、互连控制功能。但随着 HBM 数量增加、NVLink 带宽提升、CPO/光互连逐渐靠近封装边缘，compute die 不可能无限承担所有外部 I/O。

把 I/O、PHY、SerDes 或互连功能拆出来，放在封装边缘或 GPU 上下方，是非常自然的演进。

所以 2026 Rubin 时代的 5.5× reticle，不应该只看作12 HBM 的 CoWoS，而应该看作 AI 封装从计算芯片 + 存储向计算、存储、I/O、互连分工的系统封装过渡。

这也解释了为什么 2024 年 3.3× 的图里没有这些红色区域，而 2026、2027、2028 年的 roadmap 里逐渐出现。封装面积放大以后，真正变化的不只是 HBM 数量，而是封装内部的功能分区开始接近一个小系统。

**Rubin 仍然是 2.5D 主线，SoIC 还无法大规模上车**

从产品对应看，2026 年 Rubin 最确定的技术主线仍然是 CoWoS-L + HBM4。它会比 Blackwell 更大，HBM 数量更多，I/O 更复杂，但它未必需要把 3D SoIC 作为核心叙事。

原因很简单，英伟达过去的 GPU 路线一直偏向超大 die。Blackwell、Hopper 这一类产品，本质上还是 800mm² 级别大 die 或大 chiplet加 HBM，通过 CoWoS-S 或 CoWoS-L 平铺整合。

只要超大 die 还能制造，只要 CoWoS-L 还能继续放大，英伟达就没有必要太早承担大规模 logic-on-logic 3D 堆叠的热和良率风险。

AMD MI300 是台积电 SoIC + CoWoS 结合的早期样板，但它不能被简单理解成GPU compute die 叠 GPU compute die。

它更准确的意义是，SoIC 先在 compute chiplet、base die/active interposer、I/O/互连功能之间建立高密度垂直连接，再通过 CoWoS 把 HBM 纳入同一个 2.5D 系统。

因此，MI300 证明的不是大 GPU die 必须上下堆叠，而是 SoIC 可以作为 CoWoS 体系内的 3D 集成模块，先从 base die、I/O、cache、SRAM 或小 chiplet 这些更适合的功能块切入。

MI300不是简单把 CPU、GPU、HBM 全部平铺在 interposer 上，而是先把 compute chiplet 叠在 base die / active interposer 上，再通过 2.5D CoWoS 把这个 compute complex 与 HBM 横向整合。

MI300 证明了一件事：3D SoIC 可以先局部进入 CoWoS，而不是一开始就把所有东西垂直堆叠。也就是说，3D 并不是取代 2.5D，而是嵌入 2.5D 体系之中，先在局部功能块上使用。

但 NVIDIA 的 Rubin 不一定要走同样节奏。Rubin 更可能仍然以大 die / chiplet + HBM4 + CoWoS-L 为主。即便有 SoIC，也更可能是局部或辅助功能，而不是 GPU 主体大规模 3D 堆叠。

这一点很重要。我们不能看到台积电大幅度扩产 SoIC，就直接推导出 Rubin GPU 大 die 要立刻上下堆叠。更合理的解释是，SoIC 的第一批大规模需求，很可能来自 SRAM/cache、小 chiplet 或局部 I/O，有这方面情却需求的正是26 GTC的 Groq 3 LPU。

## **3D SoIC 的真正入口  SRAM、cache、I/O 与小 die**

3D SoIC 到底会用在哪里？这是整条路线能不能成立的关键。

由于散热问题无法解决，直接把两个高功耗大 GPU die 叠起来是不现实的。GPU 本身功耗已经进入数百瓦甚至千瓦级封装时代，大 die 热流密度极高，如果再叠一层高功耗 logic，散热会非常困难，良率和测试也会变得极其复杂。

更合理的顺序是：

![](images/9225e771199c9a183036.png)

其中最确定的是 SRAM。

6T SRAM 结构已经很难继续按逻辑制程同步微缩。先进逻辑节点里，逻辑晶体管密度还能继续提升，但 SRAM 面积缩放越来越慢，片上 cache 越来越贵。AI 推理，尤其是低延迟推理、LPU 或 SRAM-heavy 架构，对大容量、低延迟、高带宽 SRAM 的需求很强。

把 SRAM 单独做成 die，然后通过 hybrid bonding / SoIC 堆在 logic die 上，比继续在大逻辑 die 里平面铺 SRAM 更合理。其实这正是2nmm以下世代SRAM无法有效同步微缩的必要方法。

而且 SRAM die 功耗密度低于 GPU compute die，热问题相对更可控。因此，SRAM-on-logic 很可能是 3D SoIC 在 AI 领域最先真正放量的方向。

这也解释了台积电扩 SoIC 的一个重要逻辑。当前 LPU 3 仍在三星代工，而下一代 LPU 4 已经开始在台积电流片，那么 SoIC 扩产最直接的用途之一，可能就是 LPU 的 logic die + SRAM die 堆叠。相比把 Rubin GPU 主 die 直接 3D 化，LPU/SRAM 的需求更符合 SoIC 的工程现实。

I/O die、PHY、SerDes、NVLink、未来 CPO 的电接口，也可能成为 SoIC 的候选，但短期未必最急。因为台积电 roadmap 图中红色区域已经给了 I/O 或互连 PHY 平铺空间，它们可以先放在封装边缘，通过 CoWoS-L 的 RDL 或 local silicon bridge 连接，不一定马上需要垂直堆叠。

所以更准确的判断是：Rubin 这一代，SoIC 未必是 GPU 主体；Rubin Ultra 到 Feynman 之间，SoIC 的真正主角更可能是 SRAM/cache、LPU、小 chiplet 和局部 I/O。等到散热、HBM 定制化、CoPoS 与 IMC-Si 进一步成熟后，memory-on-logic 才会进入更主线的位置。

## **HBM 与 GPU 立体集成必须靠冷却打开**

即便海力士在2024年就公布HBM4e与GPU立体堆叠的技术路线，但一直以来笔者会比较保守地看待 HBM-on-GPU。原因很直接，GPU 是最高热流密度区域，HBM 又对温度敏感，把 HBM 直接压在 GPU 上方，这非常不现实。

但如果把 SK hynix 的 HBM roadmap、HBM4E 的 custom 趋势、台积电 IMC-Si 冷却技术放在一起看，这个判断可以更乐观地收敛。

未来 HBM 与 GPU/ASIC 的立体集成，已经不是会不会发生，而是从哪一代、以什么形式、先在什么区域发生。

HBM4 开始，base die 已经越来越像逻辑组件，而不是传统意义上的纯存储底座。

HBM4E 之后，custom HBM、logic base die、GPU/ASIC 深度定制会更加明显。也就是说，HBM 正在从标准存储器，变成 AI 系统立体封装中的一部分。

之前HBM之父金正浩表示AI时代主导权正从GPU转向内存,被似懂非懂的网友误解。

未来AI的存储绝对价值会远高于逻辑GPU,但作为标准品,即便未来custom客制化也是依附于逻辑制程,并融入整个平台中,所以金正浩的表态只能是其站在存储角度的发言,只能说价值量存储绝对是遥遥领先,重要度最高,但主导权并不会因为金正浩的立场性发言而改变分毫,只要你明白这个体系如何运行,就能清楚的明白。

未来HBM与HBF成为AI系统立体封装的一部分时,IMC-Si 的意义就凸显出来。如今我们随便挑出一个系统级环节,就能明白这一切并非存储厂家能主导,系统级层面要解决的问题太多了。

![](images/5d52f4352fa71193533c.png)

目前台积电公开展示的 IMC-Si 技術仍然是服务于 2.5D CoWoS 封装的顶部散热增强方案。也就是说，GPU 与 HBM 仍然横向平铺在 CoWoS/RDL/interposer 上，冷却结构从传统的 TIM、lid、cold plate 进一步靠近 silicon die，以减少中间热阻，而不是已经在 GPU 与 HBM 之间插入液冷层。

当前更接近的结构是：

![](images/00af2167a6846169f8c4.png)

台积电在 ECTC 2025 展示的 direct-to-silicon liquid cooling，是把液冷结构整合到 CoWoS 平台上，重点是应对 AI/HPC 芯片功耗密度继续上升后的热墙。

台积电的 IMC-Si 正在 CoWoS-R 有机 interposer 测试载具上验证，测试载具模拟 4 SoC + 8 HBM 的封装，并展示了在 40°C 水、10 L/min 流量下带走超过 3000W 均匀功耗的能力。 

这说明 IMC-Si 的第一步价值非常明确，让 2.5D 大封装继续放大，让 GPU/SoC 顶部散热路径更短、更直接。 但它还不是完整的 GPU-HBM 立体堆叠散热方案。

在 IMC-Si 之外，台积电也在探索更高导热材料来替代或增强传统 lid/顶盖结构。

台积电正在评估 SiC/diamond 等材料，用它们的高导热性和机械强度来改善先进封装的散热与可靠性。  

这里可以理解成另一条并行路线：IMC-Si 负责把液冷推近 silicon，金刚石或碳化硅 lid 负责提高顶部热扩散与热传导效率。

因此，当前可验证的散热技术组合更像是：

![](images/696ef82d5d96e1b541d2.png)

真正的 HBM-on-GPU，不能只靠顶部有 IMC-Si。因为一旦 HBM 放在 GPU 上方，热流路径会变得完全不同，GPU 的热会向上进入 HBM，HBM 自身也会发热，而中间层如果没有冷却或热隔离，HBM 就会被夹在高热区域中。这个结构和当前 HBM 横向平铺完全不同。

所以，未来若要实现 GPU 与 HBM 的立体堆叠，比较合理的路径不是一步到位，而是分阶段演进。

第一阶段，是当前的 2.5D 平铺 + 顶部 direct-to-silicon cooling。GPU 与 HBM 仍然平铺，IMC-Si 主要覆盖高热 GPU/SoC 区域，金刚石或 SiC lid 帮助提升顶部热扩散能力。这一阶段解决的是大封装继续扩功耗的问题。

这里有个值得注意的问题，目前大肆炒作的SiC interposer必然是错的，先不说interposer早就不承担散热功能这种基本常识，目前台积电在测试的是SiC作为Carrier，更重点是主要是多晶SiC根本不是二级市场炒作的单晶SiC。

第二阶段，是 GPU 与 HBM 分区冷却。也就是说，GPU 上方有更强的 direct-to-silicon cooling，HBM 上方也有独立热路径或局部冷却结构，但 HBM 仍不一定直接压在 GPU 正上方。这个阶段会让 HBM 更靠近 GPU，但仍然保留一定横向分布，以降低热耦合风险。

第三阶段，才是真正的 HBM-on-GPU 立体堆叠。这个阶段至少需要三条热路径同时成立：HBM 上方要有高效散热路径，GPU/logic 上方或背面要有高效散热路径，GPU 与 HBM 中间还需要 interlayer cooling、microfluidic channel、热隔离层或极高导热中介层。否则 HBM 堆在 GPU 上方会被 GPU 热源持续烘烤，很难稳定量产。

真正的未来结构可以理解成：

![](images/39fa7632c8b7d6b29ec6.png)

也就是说，金刚石或 SiC lid 可以改善顶部热扩散，IMC-Si 可以把冷却推近 die，但如果要做 HBM-on-GPU，GPU 与 HBM 中间仍然需要一层真正有效的热管理结构。 没有中间层冷却，立体堆叠仍然难以成立。

针对 3D stacked dies，microfluidic interlayer cooling 被认为是解决中间层热堆积的重要路径，微軟的研究也提到，微流道可以用于 3D stacked dies 的 interlayer cooling，并可针对 GPU server 里的 SoC 与 HBM 做 targeted cooling。  

此外，关于 diamond inter-tier cooling 的研究也显示，高导热材料可以作为 3D IC 冷却策略的一部分，用来替代部分介质层或热通孔，改善垂直堆叠中的热传导。 

因此，對於未來3D SoIC 的HBM-on-GPU 立体堆叠，我們的判斷可以收敛為：

IMC-Si 是 HBM-on-GPU 的必要条件，但不是充分条件，金刚石/SiC lid 是顶部热扩散的重要补充，但也不能单独解决中间层热堆积。

真正让 GPU 与 HBM 立体堆叠成立的，是 IMC-Si、interlayer cooling、高导热 lid、CoPoS/CoWoS 底座、电源完整性与封装良率共同成熟。

这也是为什么 2026 Rubin 仍然大概率是 HBM 平铺，2027 Rubin Ultra 可能只是更紧密的 2.5D/准 3D 探索，而 2028 Feynman 才更像是 HBM4E/custom HBM、IMC-Si 与更复杂立体集成同时成熟的关键节点。但这一切都是建立在无数的新技术之上，Delay的风险并不低。

## **
**

![](images/b589f2e913d0417cd7ee.jpg)

## **
**

## **Rubin Ultra 的 4 die 争议：平台能力与产品量产不是一回事**

台积电 roadmap 里 2027 年展示 9.5× reticle，看起来可以支持 4 个 compute die、12 颗 HBM4E 以及上下 I/O 区域。这说明台积电平台能力已经准备向更大封装推进。

但这并不等于 NVIDIA Rubin Ultra 一定会采用最满配的 4 die 单封装方案。

最近市场传出 Rubin Ultra 从 4 die 改成 2 die，本质不是“技术不会做”，而是量产取舍。4 die + 12/16 HBM 的单封装方案，理论上很激进，但现实中会遇到一连串问题。虽然这些问题并非不是无解，但综合成本可量，或许更保守方案更为安全。

![](images/6fec5a9817c296c6618f.png)

所以 2027 年可能出现一个非常典型的分化：台积电平台能力已经可以展示 9.5× reticle，但 NVIDIA 的实际产品出于良率、成本、交付和供应链节奏考虑，选择更保守的 2×AB1 方案。

这里的 AB1 可以理解成一种中间集成单元。不是把 4 个 die 全部一次性压到一个超大封装里，而是先把 2 个 die 做成一个较小单元，再通过封装或系统互连组合成更大的产品。

这会牺牲部分带宽和延迟，但换来更好的量产稳定性。这并不否定台积电 roadmap，反而说明先进封装正在进入一个新阶段，平台能力和客户实际产品选择不再完全同步。

台积电需要先把能力往前推，客户则会根据产品良率、成本和交付节奏选择吃多少。

因此，Rubin Ultra 的 4 die 争议不是路线错误，而是 2027 年正好处在 CoWoS-L 极限扩大、SoIC 局部导入、CoPoS 尚未完全成熟之前的过渡期。

## **CoWoS-L、CoPoS、SoIC、SoW-X 不是替代关系，而是技术栈融合**

很多讨论容易把台积电技术路线说成线性替代：CoWoS-L 之后是 CoPoS，CoPoS 之后是 SoW-X。或者简单分成 CoWoS-L 是高端，CoPoS 是顶级，SoW-X 是极端方案。这种说法不准确。

更正确的理解应该是：

![](images/ff72831f0846e208be74.png)

它们不是谁取代谁，而是会在不同层级最终汇集台积电平台里，未来台积电CoWoS/CoPoS会把各种五花八门的技术全部集成再一起。

CoWoS-L 的意义，是用 RDL base + local silicon bridge，减少对大面积 65nm silicon interposer 的依赖，解决 CoWoS-S 大硅 interposer 产能和面积扩展问题。它不是整片 65nm interposer 的无限放大，而是通过局部硅和 RDL，把封装面积继续做大。

CoPoS 的意义，是把底座从 wafer-based 扩展到 panel-based。随着封装面积越来越大，圆形 wafer 的面积利用率越来越不适合超大矩形封装，panel 更适合大尺寸封装的生产效率。CoPoS 不是简单“比 CoWoS-L 更高级”，而是大面积封装制造方式的变化。

SoIC 的意义，是提供垂直互连能力。它可以嵌入 CoWoS-L，也可以嵌入 CoPoS。未来在 CoPoS 上使用 SoIC，在 SoIC 上整合 SRAM、I/O、HBM 或小 compute die，是非常自然的方向。

SoW-X 则不是取代 CoPoS，而是在更大系统尺度上使用类似思想。它不是单纯一个封装，而是把系统边界推进到 wafer-scale / system-scale。

所以未来真正的顶级形态，不是“选择 CoPoS 或 SoIC 或 SoW-X”，而是 CoPoS 做大面积底座，SoIC 做局部垂直堆叠，IMC-Si 解决热墙，CPO/COUPE 解决高速光电 I/O，SoW-X 把系统边界进一步放大。

## **玻璃基板与 CoPoS：不是玻璃带来翘曲，而是大尺寸要求更好的翘曲控制**

CoPoS 讨论中还有一个容易混淆的点：玻璃基板。

玻璃基板的优势之一，正是低 CTE、更好尺寸稳定性、更低翘曲、更适合高密度互连和大尺寸封装。

所以不能说换 CoPoS 后翘曲更严重，是因为玻璃。更准确的说法是，当封装从 wafer/package 尺寸走向更大 panel 尺寸后，整体应力、翘曲、热膨胀匹配、贴装平整度都会更难控制，而玻璃基板正是解决这些问题的重要材料方案之一。

![](images/9b6f4ba17f8dad88c165.png)

因此，2028 Feynman 时代，更可能是 CoWoS-L 继续承担主力，CoPoS 在顶级 SKU 或特定系统中开始导入。到了 2029 Feynman Ultra，CoPoS + SoIC + IMC-Si + optical I/O 的融合才会更明显。

## **SoW-X 不是 Cerebras，也不是整张 65nm interposer**

SoW-X 是另一个容易被误解的技术。

第一种误解，是把 SoW-X 说成 Cerebras。

Cerebras WSE 是整片 wafer 做成一个 monolithic AI chip，依靠片上 SRAM 和特殊 mesh 架构。这种路线已经存在多年，也证明了 wafer-scale 能做，但它并没有成为通用 AI 加速器主流。

原因很简单：它的架构特殊，生态特殊，没有 HBM，适合特定工作负载，但不是 GPU/HBM 主流训练架构。

SoW-X 不一样。它更像是整片 wafer / system-scale 平台，加多个 known-good logic die、多个 HBM、多个 I/O die、connector/conductor 与系统级互连。

也就是说，Cerebras 是wafer 是一个芯片，SoW-X 是wafer 是一个系统。Cerebras 是改芯片架构，SoW-X 是改系统封装架构。

第二种误解，是把 SoW-X 理解成整张 65nm silicon interposer。

如果 SoW-X 真是整张 65nm interposer，那它马上就会遇到致命问题，65nm 产能不够，整片硅 interposer 成本太高，TSV/BEOL 良率风险太大，整片 wafer 级被动 interposer 几乎无法经济量产。

所以 SoW-X 不可能是 CoWoS-S 的简单放大版。它是 CoWoS-L / CoPoS 思想在系统尺度上的延伸，使用 RDL、局部 silicon bridge、hybrid bonding、panel/wafer-level base、edge connector/conductor，把多个 logic、HBM、I/O 组织成 wafer-scale system。

这也解释了台積電roadmap图中右上角 SoW-X 里的 connector。越往后走，封装边缘的系统连接、I/O、供电、信号分发会变得越来越重要。红色 die 更合理地理解为 I/O/互连功能块，而 connector是更高层的系统连接结构。

SoW-X 的战略意义在于，台积电把 wafer-scale 从 Cerebras 式特殊芯片架构，转成先进封装与系统集成平台。

## **2025–2029 产品与技术如何对应**

如果把整个路线收敛成产品时间线，可以这样理解。

2025 年 Blackwell 仍然是 CoWoS-L 主导。封装很大，HBM 很多，液冷重要性提升，但本质仍然是大 GPU + HBM 的 2.5D 系统。

2026 年 Rubin 进入 5.5× reticle。主线是 CoWoS-L + HBM4 + 更复杂 I/O。

roadmaop的红色区域代表 I/O/PHY/互连功能开始进入封装内部，系统分工更明确。但 Rubin 不會是SoIC 大规模上车，它仍然主要是 2.5D 放大。

2027 年 Rubin Ultra 对应 9.5× reticle 平台能力。台积电理论上可以支持更大封装、更复杂 chiplet、更高 HBM 数量。但 NVIDIA 产品端可能因为良率、成本、交付选择更保守的 2 die 或 2×AB1 方案。

与此同时，笔者把台积电北美论坛 roadmap上没有提及的技术加进来，同学们才能更好的去理解未来AI芯片的变化，3D SoIC 产能开始被 LPU、SRAM/cache、小 ASIC、局部 I/O 消耗，而IMC-Si 初步进入量产准备。

2028 年 Feynman 是真正关键节点。

CoWoS-L 达到 14× reticle 级别，CoPoS 开始导入或进入早期量产，HBM4E/custom HBM 与 logic 的关系更紧密，IMC-Si 逐渐成熟，SRAM/I/O/HBM 的局部 3D 集成开始进入主线。

Feynman 这一代很可能是从 2.5D 平铺向 3D memory-on-logic 转折的关键阶段。

2029 年 Feynman Ultra 则可能进入 CoPoS + SoIC + IMC-Si + SoW-X 的系统级融合。主流高端产品仍可能是 CoPoS/CoWoS-L + SoIC 的组合，SoW-X 则作为极少数 wafer-scale system 方案出现。

![](images/932fd498ad11a61cee52.png)

## **最终主线：横向更大、纵向更密、散热更近、互连更光、系统更大**

如果把所有技术拆开看，会觉得非常复杂：

CoWoS-L、CoPoS、SoIC、IMC-Si、SoW-X、CPO、COUPE、HBM4E、custom HBM、SRAM stack、I/O die、红色 PHY 区域，每一个都是一条线。

但把它们放在一起，主线其实很清楚。

![](images/265ee56416a150e58875.png)

台积电不是在单纯追求更大的 interposer，而是在用先进封装重构 AI 系统。过去属于 PCB 和 rack 的互连，正在被推进到封装内部。

过去属于封装外部的冷却，正在靠近 silicon；过去平铺在旁边的存储，正在向 logic 上方或更近距离靠拢；过去分散在系统里的 I/O，正在变成封装内的独立 die 或 PHY 区域。

因此，AI 封装未来不是简单从 CoWoS-L 走向 CoPoS，也不是简单从 2.5D 走向 3D，而是多条技术线同时融合。

2026 Rubin 是 2.5D CoWoS-L 的系统化；2027 Rubin Ultra 是平台能力与产品量产之间的过渡；2028 Feynman 是 HBM4E、IMC-Si、SoIC、CoPoS 同时成熟的转折点；2029 Feynman Ultra 则可能进入 CoPoS + SoIC + SoW-X 的系统级封装时代。

这条路线的终点，不是单颗 GPU 更大，而是整个 AI 系统被重新封装。

另外从 roadmap 带来的硅面积需求增长将会是一个非常恐怖的数字，这是笔者早有预期但现实比我预期增长更大许多，上面的所有要点加起來，正是我不论从短中长期，一直选择重压台积电的原因。

        过去几年，AI 芯片的叙事一直围绕算力展开：GPU die 越来越大，HBM 越堆越多，CoWoS 产能越来越紧，先进封装从幕后工艺变成了整个 AI 产业链最核心的瓶颈之一。

但如果我们只把这条线理解成“interposer 越做越大”“HBM 从 8 颗变 12 颗、再变 20 颗”，其实会错过台积电路线图背后真正发生的变化。

台积电展示的先进封装路线，从 2024 年的 3.3 倍 reticle，到 2026 年 5.5 倍 reticle，再到 2027 年 9.5 倍、2028 年 14 倍，最后到 2029 年 SoW-X 的 40 倍 reticle、64 颗 HBM，表面上看是一条“封装面积持续放大”的曲线，但本质上不是简单把 CoWoS-S 或 CoWoS-L 不断拼大，而是 AI 系统边界正在被重新定义。

过去，一个 AI 加速器系统的层级大致是，die 在封装里，封装在载板上，载板接到 PCB，PCB 再组成服务器，服务器再进入 rack，rack 之间再靠 NVLink、以太网、光模块和交换芯片连接。

每跨一层，互连距离变长，延迟变大，功耗上升，带宽密度下降。AI 时代的真正问题，已经不是单颗芯片算力不够，而是算力、显存、带宽、I/O、供电、散热、rack 内互连全部同时撞墙。

所以台积电的封装路线，不只是“把芯片封得更大”，而是试图把原本属于 board、rack 甚至系统级的互连，逐步压缩进 package、panel、wafer-system 里面。也就是说，先进封装正在从芯片制造的后段工艺，变成系统架构本身。

## **
**

![](images/b589f2e913d0417cd7ee.jpg)

## **
**

## **3.3× 到 5.5× 不只是 HBM 增加，而是封装内部开始系统化**

台积电路线图里最容易被忽略的地方，是 2024 年 3.3× reticle 与 2026 年 5.5× reticle 的差别。

表面看，2024 年是 8 颗 HBM，2026 年变成 12 颗 HBM，好像只是显存堆栈数量增加。

但图中真正值得注意的是，2026 年开始，在 GPU/SoC 上下方出现了红色区域。这个红色区域必定不是 GPU compute die，更合理的判断是 I/O die、SerDes die、NVLink PHY、die-to-die 互连、封装边缘连接芯片，或者其他 active interconnect chiplet。

这意味着 5.5× reticle 不是简单的大 GPU + 更多 HBM，而是从传统的计算芯片封装，开始走向系统级封装。

  

这一步非常关键。过去 GPU die 自己承担大量计算、I/O、互连控制功能。但随着 HBM 数量增加、NVLink 带宽提升、CPO/光互连逐渐靠近封装边缘，compute die 不可能无限承担所有外部 I/O。

把 I/O、PHY、SerDes 或互连功能拆出来，放在封装边缘或 GPU 上下方，是非常自然的演进。

所以 2026 Rubin 时代的 5.5× reticle，不应该只看作12 HBM 的 CoWoS，而应该看作 AI 封装从计算芯片 + 存储向计算、存储、I/O、互连分工的系统封装过渡。

这也解释了为什么 2024 年 3.3× 的图里没有这些红色区域，而 2026、2027、2028 年的 roadmap 里逐渐出现。封装面积放大以后，真正变化的不只是 HBM 数量，而是封装内部的功能分区开始接近一个小系统。

**Rubin 仍然是 2.5D 主线，SoIC 还无法大规模上车**

从产品对应看，2026 年 Rubin 最确定的技术主线仍然是 CoWoS-L + HBM4。它会比 Blackwell 更大，HBM 数量更多，I/O 更复杂，但它未必需要把 3D SoIC 作为核心叙事。

原因很简单，英伟达过去的 GPU 路线一直偏向超大 die。Blackwell、Hopper 这一类产品，本质上还是 800mm² 级别大 die 或大 chiplet加 HBM，通过 CoWoS-S 或 CoWoS-L 平铺整合。

只要超大 die 还能制造，只要 CoWoS-L 还能继续放大，英伟达就没有必要太早承担大规模 logic-on-logic 3D 堆叠的热和良率风险。

AMD MI300 是台积电 SoIC + CoWoS 结合的早期样板，但它不能被简单理解成GPU compute die 叠 GPU compute die。

它更准确的意义是，SoIC 先在 compute chiplet、base die/active interposer、I/O/互连功能之间建立高密度垂直连接，再通过 CoWoS 把 HBM 纳入同一个 2.5D 系统。

因此，MI300 证明的不是大 GPU die 必须上下堆叠，而是 SoIC 可以作为 CoWoS 体系内的 3D 集成模块，先从 base die、I/O、cache、SRAM 或小 chiplet 这些更适合的功能块切入。

MI300不是简单把 CPU、GPU、HBM 全部平铺在 interposer 上，而是先把 compute chiplet 叠在 base die / active interposer 上，再通过 2.5D CoWoS 把这个 compute complex 与 HBM 横向整合。

MI300 证明了一件事：3D SoIC 可以先局部进入 CoWoS，而不是一开始就把所有东西垂直堆叠。也就是说，3D 并不是取代 2.5D，而是嵌入 2.5D 体系之中，先在局部功能块上使用。

但 NVIDIA 的 Rubin 不一定要走同样节奏。Rubin 更可能仍然以大 die / chiplet + HBM4 + CoWoS-L 为主。即便有 SoIC，也更可能是局部或辅助功能，而不是 GPU 主体大规模 3D 堆叠。

这一点很重要。我们不能看到台积电大幅度扩产 SoIC，就直接推导出 Rubin GPU 大 die 要立刻上下堆叠。更合理的解释是，SoIC 的第一批大规模需求，很可能来自 SRAM/cache、小 chiplet 或局部 I/O，有这方面情却需求的正是26 GTC的 Groq 3 LPU。

## **3D SoIC 的真正入口  SRAM、cache、I/O 与小 die**

3D SoIC 到底会用在哪里？这是整条路线能不能成立的关键。

由于散热问题无法解决，直接把两个高功耗大 GPU die 叠起来是不现实的。GPU 本身功耗已经进入数百瓦甚至千瓦级封装时代，大 die 热流密度极高，如果再叠一层高功耗 logic，散热会非常困难，良率和测试也会变得极其复杂。

更合理的顺序是：

![](images/9225e771199c9a183036.png)

其中最确定的是 SRAM。

6T SRAM 结构已经很难继续按逻辑制程同步微缩。先进逻辑节点里，逻辑晶体管密度还能继续提升，但 SRAM 面积缩放越来越慢，片上 cache 越来越贵。AI 推理，尤其是低延迟推理、LPU 或 SRAM-heavy 架构，对大容量、低延迟、高带宽 SRAM 的需求很强。

把 SRAM 单独做成 die，然后通过 hybrid bonding / SoIC 堆在 logic die 上，比继续在大逻辑 die 里平面铺 SRAM 更合理。其实这正是2nmm以下世代SRAM无法有效同步微缩的必要方法。

而且 SRAM die 功耗密度低于 GPU compute die，热问题相对更可控。因此，SRAM-on-logic 很可能是 3D SoIC 在 AI 领域最先真正放量的方向。

这也解释了台积电扩 SoIC 的一个重要逻辑。当前 LPU 3 仍在三星代工，而下一代 LPU 4 已经开始在台积电流片，那么 SoIC 扩产最直接的用途之一，可能就是 LPU 的 logic die + SRAM die 堆叠。相比把 Rubin GPU 主 die 直接 3D 化，LPU/SRAM 的需求更符合 SoIC 的工程现实。

I/O die、PHY、SerDes、NVLink、未来 CPO 的电接口，也可能成为 SoIC 的候选，但短期未必最急。因为台积电 roadmap 图中红色区域已经给了 I/O 或互连 PHY 平铺空间，它们可以先放在封装边缘，通过 CoWoS-L 的 RDL 或 local silicon bridge 连接，不一定马上需要垂直堆叠。

所以更准确的判断是：Rubin 这一代，SoIC 未必是 GPU 主体；Rubin Ultra 到 Feynman 之间，SoIC 的真正主角更可能是 SRAM/cache、LPU、小 chiplet 和局部 I/O。等到散热、HBM 定制化、CoPoS 与 IMC-Si 进一步成熟后，memory-on-logic 才会进入更主线的位置。

## **HBM 与 GPU 立体集成必须靠冷却打开**

即便海力士在2024年就公布HBM4e与GPU立体堆叠的技术路线，但一直以来笔者会比较保守地看待 HBM-on-GPU。原因很直接，GPU 是最高热流密度区域，HBM 又对温度敏感，把 HBM 直接压在 GPU 上方，这非常不现实。

但如果把 SK hynix 的 HBM roadmap、HBM4E 的 custom 趋势、台积电 IMC-Si 冷却技术放在一起看，这个判断可以更乐观地收敛。

未来 HBM 与 GPU/ASIC 的立体集成，已经不是会不会发生，而是从哪一代、以什么形式、先在什么区域发生。

HBM4 开始，base die 已经越来越像逻辑组件，而不是传统意义上的纯存储底座。

HBM4E 之后，custom HBM、logic base die、GPU/ASIC 深度定制会更加明显。也就是说，HBM 正在从标准存储器，变成 AI 系统立体封装中的一部分。

之前HBM之父金正浩表示AI时代主导权正从GPU转向内存,被似懂非懂的网友误解。

未来AI的存储绝对价值会远高于逻辑GPU,但作为标准品,即便未来custom客制化也是依附于逻辑制程,并融入整个平台中,所以金正浩的表态只能是其站在存储角度的发言,只能说价值量存储绝对是遥遥领先,重要度最高,但主导权并不会因为金正浩的立场性发言而改变分毫,只要你明白这个体系如何运行,就能清楚的明白。

未来HBM与HBF成为AI系统立体封装的一部分时,IMC-Si 的意义就凸显出来。如今我们随便挑出一个系统级环节,就能明白这一切并非存储厂家能主导,系统级层面要解决的问题太多了。

![](images/5d52f4352fa71193533c.png)

目前台积电公开展示的 IMC-Si 技術仍然是服务于 2.5D CoWoS 封装的顶部散热增强方案。也就是说，GPU 与 HBM 仍然横向平铺在 CoWoS/RDL/interposer 上，冷却结构从传统的 TIM、lid、cold plate 进一步靠近 silicon die，以减少中间热阻，而不是已经在 GPU 与 HBM 之间插入液冷层。

当前更接近的结构是：

![](images/00af2167a6846169f8c4.png)

台积电在 ECTC 2025 展示的 direct-to-silicon liquid cooling，是把液冷结构整合到 CoWoS 平台上，重点是应对 AI/HPC 芯片功耗密度继续上升后的热墙。

台积电的 IMC-Si 正在 CoWoS-R 有机 interposer 测试载具上验证，测试载具模拟 4 SoC + 8 HBM 的封装，并展示了在 40°C 水、10 L/min 流量下带走超过 3000W 均匀功耗的能力。 

这说明 IMC-Si 的第一步价值非常明确，让 2.5D 大封装继续放大，让 GPU/SoC 顶部散热路径更短、更直接。 但它还不是完整的 GPU-HBM 立体堆叠散热方案。

在 IMC-Si 之外，台积电也在探索更高导热材料来替代或增强传统 lid/顶盖结构。

台积电正在评估 SiC/diamond 等材料，用它们的高导热性和机械强度来改善先进封装的散热与可靠性。  

这里可以理解成另一条并行路线：IMC-Si 负责把液冷推近 silicon，金刚石或碳化硅 lid 负责提高顶部热扩散与热传导效率。

因此，当前可验证的散热技术组合更像是：

![](images/696ef82d5d96e1b541d2.png)

真正的 HBM-on-GPU，不能只靠顶部有 IMC-Si。因为一旦 HBM 放在 GPU 上方，热流路径会变得完全不同，GPU 的热会向上进入 HBM，HBM 自身也会发热，而中间层如果没有冷却或热隔离，HBM 就会被夹在高热区域中。这个结构和当前 HBM 横向平铺完全不同。

所以，未来若要实现 GPU 与 HBM 的立体堆叠，比较合理的路径不是一步到位，而是分阶段演进。

第一阶段，是当前的 2.5D 平铺 + 顶部 direct-to-silicon cooling。GPU 与 HBM 仍然平铺，IMC-Si 主要覆盖高热 GPU/SoC 区域，金刚石或 SiC lid 帮助提升顶部热扩散能力。这一阶段解决的是大封装继续扩功耗的问题。

这里有个值得注意的问题，目前大肆炒作的SiC interposer必然是错的，先不说interposer早就不承担散热功能这种基本常识，目前台积电在测试的是SiC作为Carrier，更重点是主要是多晶SiC根本不是二级市场炒作的单晶SiC。

第二阶段，是 GPU 与 HBM 分区冷却。也就是说，GPU 上方有更强的 direct-to-silicon cooling，HBM 上方也有独立热路径或局部冷却结构，但 HBM 仍不一定直接压在 GPU 正上方。这个阶段会让 HBM 更靠近 GPU，但仍然保留一定横向分布，以降低热耦合风险。

第三阶段，才是真正的 HBM-on-GPU 立体堆叠。这个阶段至少需要三条热路径同时成立：HBM 上方要有高效散热路径，GPU/logic 上方或背面要有高效散热路径，GPU 与 HBM 中间还需要 interlayer cooling、microfluidic channel、热隔离层或极高导热中介层。否则 HBM 堆在 GPU 上方会被 GPU 热源持续烘烤，很难稳定量产。

真正的未来结构可以理解成：

![](images/39fa7632c8b7d6b29ec6.png)

也就是说，金刚石或 SiC lid 可以改善顶部热扩散，IMC-Si 可以把冷却推近 die，但如果要做 HBM-on-GPU，GPU 与 HBM 中间仍然需要一层真正有效的热管理结构。 没有中间层冷却，立体堆叠仍然难以成立。

针对 3D stacked dies，microfluidic interlayer cooling 被认为是解决中间层热堆积的重要路径，微軟的研究也提到，微流道可以用于 3D stacked dies 的 interlayer cooling，并可针对 GPU server 里的 SoC 与 HBM 做 targeted cooling。  

此外，关于 diamond inter-tier cooling 的研究也显示，高导热材料可以作为 3D IC 冷却策略的一部分，用来替代部分介质层或热通孔，改善垂直堆叠中的热传导。 

因此，對於未來3D SoIC 的HBM-on-GPU 立体堆叠，我們的判斷可以收敛為：

IMC-Si 是 HBM-on-GPU 的必要条件，但不是充分条件，金刚石/SiC lid 是顶部热扩散的重要补充，但也不能单独解决中间层热堆积。

真正让 GPU 与 HBM 立体堆叠成立的，是 IMC-Si、interlayer cooling、高导热 lid、CoPoS/CoWoS 底座、电源完整性与封装良率共同成熟。

这也是为什么 2026 Rubin 仍然大概率是 HBM 平铺，2027 Rubin Ultra 可能只是更紧密的 2.5D/准 3D 探索，而 2028 Feynman 才更像是 HBM4E/custom HBM、IMC-Si 与更复杂立体集成同时成熟的关键节点。但这一切都是建立在无数的新技术之上，Delay的风险并不低。

## **
**

![](images/b589f2e913d0417cd7ee.jpg)

## **
**

## **Rubin Ultra 的 4 die 争议：平台能力与产品量产不是一回事**

台积电 roadmap 里 2027 年展示 9.5× reticle，看起来可以支持 4 个 compute die、12 颗 HBM4E 以及上下 I/O 区域。这说明台积电平台能力已经准备向更大封装推进。

但这并不等于 NVIDIA Rubin Ultra 一定会采用最满配的 4 die 单封装方案。

最近市场传出 Rubin Ultra 从 4 die 改成 2 die，本质不是“技术不会做”，而是量产取舍。4 die + 12/16 HBM 的单封装方案，理论上很激进，但现实中会遇到一连串问题。虽然这些问题并非不是无解，但综合成本可量，或许更保守方案更为安全。

![](images/6fec5a9817c296c6618f.png)

所以 2027 年可能出现一个非常典型的分化：台积电平台能力已经可以展示 9.5× reticle，但 NVIDIA 的实际产品出于良率、成本、交付和供应链节奏考虑，选择更保守的 2×AB1 方案。

这里的 AB1 可以理解成一种中间集成单元。不是把 4 个 die 全部一次性压到一个超大封装里，而是先把 2 个 die 做成一个较小单元，再通过封装或系统互连组合成更大的产品。

这会牺牲部分带宽和延迟，但换来更好的量产稳定性。这并不否定台积电 roadmap，反而说明先进封装正在进入一个新阶段，平台能力和客户实际产品选择不再完全同步。

台积电需要先把能力往前推，客户则会根据产品良率、成本和交付节奏选择吃多少。

因此，Rubin Ultra 的 4 die 争议不是路线错误，而是 2027 年正好处在 CoWoS-L 极限扩大、SoIC 局部导入、CoPoS 尚未完全成熟之前的过渡期。

## **CoWoS-L、CoPoS、SoIC、SoW-X 不是替代关系，而是技术栈融合**

很多讨论容易把台积电技术路线说成线性替代：CoWoS-L 之后是 CoPoS，CoPoS 之后是 SoW-X。或者简单分成 CoWoS-L 是高端，CoPoS 是顶级，SoW-X 是极端方案。这种说法不准确。

更正确的理解应该是：

![](images/ff72831f0846e208be74.png)

它们不是谁取代谁，而是会在不同层级最终汇集台积电平台里，未来台积电CoWoS/CoPoS会把各种五花八门的技术全部集成再一起。

CoWoS-L 的意义，是用 RDL base + local silicon bridge，减少对大面积 65nm silicon interposer 的依赖，解决 CoWoS-S 大硅 interposer 产能和面积扩展问题。它不是整片 65nm interposer 的无限放大，而是通过局部硅和 RDL，把封装面积继续做大。

CoPoS 的意义，是把底座从 wafer-based 扩展到 panel-based。随着封装面积越来越大，圆形 wafer 的面积利用率越来越不适合超大矩形封装，panel 更适合大尺寸封装的生产效率。CoPoS 不是简单“比 CoWoS-L 更高级”，而是大面积封装制造方式的变化。

SoIC 的意义，是提供垂直互连能力。它可以嵌入 CoWoS-L，也可以嵌入 CoPoS。未来在 CoPoS 上使用 SoIC，在 SoIC 上整合 SRAM、I/O、HBM 或小 compute die，是非常自然的方向。

SoW-X 则不是取代 CoPoS，而是在更大系统尺度上使用类似思想。它不是单纯一个封装，而是把系统边界推进到 wafer-scale / system-scale。

所以未来真正的顶级形态，不是“选择 CoPoS 或 SoIC 或 SoW-X”，而是 CoPoS 做大面积底座，SoIC 做局部垂直堆叠，IMC-Si 解决热墙，CPO/COUPE 解决高速光电 I/O，SoW-X 把系统边界进一步放大。

## **玻璃基板与 CoPoS：不是玻璃带来翘曲，而是大尺寸要求更好的翘曲控制**

CoPoS 讨论中还有一个容易混淆的点：玻璃基板。

玻璃基板的优势之一，正是低 CTE、更好尺寸稳定性、更低翘曲、更适合高密度互连和大尺寸封装。

所以不能说换 CoPoS 后翘曲更严重，是因为玻璃。更准确的说法是，当封装从 wafer/package 尺寸走向更大 panel 尺寸后，整体应力、翘曲、热膨胀匹配、贴装平整度都会更难控制，而玻璃基板正是解决这些问题的重要材料方案之一。

![](images/9b6f4ba17f8dad88c165.png)

因此，2028 Feynman 时代，更可能是 CoWoS-L 继续承担主力，CoPoS 在顶级 SKU 或特定系统中开始导入。到了 2029 Feynman Ultra，CoPoS + SoIC + IMC-Si + optical I/O 的融合才会更明显。

## **SoW-X 不是 Cerebras，也不是整张 65nm interposer**

SoW-X 是另一个容易被误解的技术。

第一种误解，是把 SoW-X 说成 Cerebras。

Cerebras WSE 是整片 wafer 做成一个 monolithic AI chip，依靠片上 SRAM 和特殊 mesh 架构。这种路线已经存在多年，也证明了 wafer-scale 能做，但它并没有成为通用 AI 加速器主流。

原因很简单：它的架构特殊，生态特殊，没有 HBM，适合特定工作负载，但不是 GPU/HBM 主流训练架构。

SoW-X 不一样。它更像是整片 wafer / system-scale 平台，加多个 known-good logic die、多个 HBM、多个 I/O die、connector/conductor 与系统级互连。

也就是说，Cerebras 是wafer 是一个芯片，SoW-X 是wafer 是一个系统。Cerebras 是改芯片架构，SoW-X 是改系统封装架构。

第二种误解，是把 SoW-X 理解成整张 65nm silicon interposer。

如果 SoW-X 真是整张 65nm interposer，那它马上就会遇到致命问题，65nm 产能不够，整片硅 interposer 成本太高，TSV/BEOL 良率风险太大，整片 wafer 级被动 interposer 几乎无法经济量产。

所以 SoW-X 不可能是 CoWoS-S 的简单放大版。它是 CoWoS-L / CoPoS 思想在系统尺度上的延伸，使用 RDL、局部 silicon bridge、hybrid bonding、panel/wafer-level base、edge connector/conductor，把多个 logic、HBM、I/O 组织成 wafer-scale system。

这也解释了台積電roadmap图中右上角 SoW-X 里的 connector。越往后走，封装边缘的系统连接、I/O、供电、信号分发会变得越来越重要。红色 die 更合理地理解为 I/O/互连功能块，而 connector是更高层的系统连接结构。

SoW-X 的战略意义在于，台积电把 wafer-scale 从 Cerebras 式特殊芯片架构，转成先进封装与系统集成平台。

## **2025–2029 产品与技术如何对应**

如果把整个路线收敛成产品时间线，可以这样理解。

2025 年 Blackwell 仍然是 CoWoS-L 主导。封装很大，HBM 很多，液冷重要性提升，但本质仍然是大 GPU + HBM 的 2.5D 系统。

2026 年 Rubin 进入 5.5× reticle。主线是 CoWoS-L + HBM4 + 更复杂 I/O。

roadmaop的红色区域代表 I/O/PHY/互连功能开始进入封装内部，系统分工更明确。但 Rubin 不會是SoIC 大规模上车，它仍然主要是 2.5D 放大。

2027 年 Rubin Ultra 对应 9.5× reticle 平台能力。台积电理论上可以支持更大封装、更复杂 chiplet、更高 HBM 数量。但 NVIDIA 产品端可能因为良率、成本、交付选择更保守的 2 die 或 2×AB1 方案。

与此同时，笔者把台积电北美论坛 roadmap上没有提及的技术加进来，同学们才能更好的去理解未来AI芯片的变化，3D SoIC 产能开始被 LPU、SRAM/cache、小 ASIC、局部 I/O 消耗，而IMC-Si 初步进入量产准备。

2028 年 Feynman 是真正关键节点。

CoWoS-L 达到 14× reticle 级别，CoPoS 开始导入或进入早期量产，HBM4E/custom HBM 与 logic 的关系更紧密，IMC-Si 逐渐成熟，SRAM/I/O/HBM 的局部 3D 集成开始进入主线。

Feynman 这一代很可能是从 2.5D 平铺向 3D memory-on-logic 转折的关键阶段。

2029 年 Feynman Ultra 则可能进入 CoPoS + SoIC + IMC-Si + SoW-X 的系统级融合。主流高端产品仍可能是 CoPoS/CoWoS-L + SoIC 的组合，SoW-X 则作为极少数 wafer-scale system 方案出现。

![](images/932fd498ad11a61cee52.png)

## **最终主线：横向更大、纵向更密、散热更近、互连更光、系统更大**

如果把所有技术拆开看，会觉得非常复杂：

CoWoS-L、CoPoS、SoIC、IMC-Si、SoW-X、CPO、COUPE、HBM4E、custom HBM、SRAM stack、I/O die、红色 PHY 区域，每一个都是一条线。

但把它们放在一起，主线其实很清楚。

![](images/265ee56416a150e58875.png)

台积电不是在单纯追求更大的 interposer，而是在用先进封装重构 AI 系统。过去属于 PCB 和 rack 的互连，正在被推进到封装内部。

过去属于封装外部的冷却，正在靠近 silicon；过去平铺在旁边的存储，正在向 logic 上方或更近距离靠拢；过去分散在系统里的 I/O，正在变成封装内的独立 die 或 PHY 区域。

因此，AI 封装未来不是简单从 CoWoS-L 走向 CoPoS，也不是简单从 2.5D 走向 3D，而是多条技术线同时融合。

2026 Rubin 是 2.5D CoWoS-L 的系统化；2027 Rubin Ultra 是平台能力与产品量产之间的过渡；2028 Feynman 是 HBM4E、IMC-Si、SoIC、CoPoS 同时成熟的转折点；2029 Feynman Ultra 则可能进入 CoPoS + SoIC + SoW-X 的系统级封装时代。

这条路线的终点，不是单颗 GPU 更大，而是整个 AI 系统被重新封装。

另外从 roadmap 带来的硅面积需求增长将会是一个非常恐怖的数字，这是笔者早有预期但现实比我预期增长更大许多，上面的所有要点加起來，正是我不论从短中长期，一直选择重压台积电的原因。

        
                
                

![](/assets_dweb/logo@1x.png)

                知识星球
                
        
        
            
            扫码加入星球
            查看更多优质内容
        
        https://wx.zsxq.com/mweb/views/joingroup/join_group.html?group_id=88888812815442

---

Source: https://articles.zsxq.com/id_0nw0z2czqga1.html

Linked from topic_id: 22255882815285151
