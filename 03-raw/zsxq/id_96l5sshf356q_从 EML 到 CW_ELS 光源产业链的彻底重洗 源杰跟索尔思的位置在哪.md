# 从 EML 到 CW/ELS 光源产业链的彻底重洗  源杰跟索尔思的位置在哪

        
            [来自：
                半导体大佬的会议室](https://wx.zsxq.com/group/88888812815442)
        
        
            
                

![](images/39ac34f1b548792d9368.jpg)

                吴梓豪leslie
            
            2026年04月28日 20:35
        
        
            

### **导读：本文的核心判断**

AI 数据中心的光通信升级，表面上看是从 800G 到 1.6T、3.2T、6.4T、12.8T 的速率迭代，实际上是一次更深层的架构迁移：光互连正在从前面板可插拔模块，逐步走向 LPO、NPO、CPO，最后进入 OIO。

速率只是结果，真正改变产业权力格局的是光源位置、调制器位置、制造平台与系统维修模式的变化。

在 800G/1.6T 时代，光源仍在光模块里，EML 是核心。在 3.2T 时代，NPO 很可能成为 scale-up 与 scale-out 的主战场。到 6.4T 时代，CPO 的必要性明显提升，光源开始外置化。到 12.8T/OIO 时代，光源不再是模块内器件，而是系统级供光资源。

这条路线决定了光源行业的权力转移，EML 时代是 InP IDM 的天下；CW/ELS 时代，纯 CW 激光器 IDM、Fabless、III-V Foundry、衬底、隔离器、TEC、透镜与外置激光模块供应链都被重新打开。

CPO 不会消灭光源，反而会把光源从一颗器件升级为 AI 计算系统的基础设施。

LightCounting 在 2026 年 3 月 Ethernet Optics 报告中提出，在多个条件同时配合的情况下，AI cluster optical interconnect 年销售额到 2030 年有合理机会达到 1000 亿美元级别；这是把 AI cluster optics 作为一个大口径市场来看。

Yole 早期对狭义 CPO 的预测更保守，估算 CPO 市场从 2022 年约 3800 万美元增长到 2033 年约 26 亿美元，CAGR 约 46%。两者差异说明：只看 CPO module，市场不算夸张；若把 LPO、NPO、CPO、OIO、ELS、AI cluster optics 合并看，产业锚会大幅上移。

Lumentum、Coherent 对 2030 年 optical interconnect / datacom 可服务市场的表述均大幅上移，反映激光器、光源模块与光互连系统已经从传统光模块配套件，变成 AI 基础设施的关键瓶颈。

### **先看代际：100G、200G、400G 单通道如何推动架构迁移**

光通信产业每一代升级，最关键的不是总带宽，而是单通道速率。

总带宽可以靠增加路数堆出来，但单通道速率一旦翻倍，整个链路的压力会同时落到SerDes、DSP、Driver、TIA、光源、调制器、封装、散热、PCB/基板走线、前面板密度和可维修性上。

也就是说，100G/lane、200G/lane、400G/lane 不是单纯的数字，而是三个不同工程时代。

400G 是 4×100G，800G 是 8×100G，1.6T 进入 8×200G、约 106.25GBaud，3.2T 则进入 8×400G、约 224GBaud。

当单通道从 100G 到 200G，传统可插拔还能靠更先进 DSP、LPO、优化热设计继续撑住。当单通道进入 400G，传统前面板可插拔的功耗、散热、信号完整性与封装密度会同步逼近极限。

因此，要先搞明白EML、CW、VCSEL、MicroLED等光源技术演变，就必须先把 Pluggable、LPO、NPO、CPO、OIO 这条架构演化路线讲清楚。

光源技术不是孤立演进，而是被架构迁移推动。

## **800G：100G/lane，可插拔仍然舒适**

800G 的主流形态是 8×100G/lane。这一代光模块仍然以 OSFP、QSFP-DD 等可插拔形态为主，EML、硅光、VCSEL 都有应用，但在 AI 数据中心单模短距与中距场景里，EML 是最成熟的主流光源。

这一阶段的核心特征是：光源在模块内，调制器也在模块内，光模块厂采购EML、DSP、Driver/TIA、透镜、FAU、PCB、外壳，完成模块组装与测试。

光源产业链的核心价值在 EML IDM 手中，因为 EML 不是单一 DFB，而是 DFB + EAM 的 InP 单片集成器件。

800G 时代的可插拔逻辑仍然成立：模块热插拔、供应商可替换、维修半径小、数据中心集采模式成熟。光源位于模块内部并不构成系统性问题，因为单模块功耗与散热尚能在 OSFP/QSFP-DD 的热设计内被消化。

## **1.6T：200G/lane，可插拔仍是主流， LPO 开始延寿**

1.6T 主流是 8×200G/lane。1.6T 还没有让 CPO 成为主流，因为可插拔模块仍有维修性、部署弹性、供应链成熟度与标准化优势。

但压力开始明显增加，1.6T 可插拔模块功耗约 20–28W，其中 DSP/SerDes 占 10–14W，接近 50%。LPO 移除模块内完整 DSP 后，可把功耗压到约 12–15W。

所以1.6T 的本质不是 CPO 立刻取代可插拔，而是 Full DSP Pluggable → LPO Pluggable → NPO/CPO 预备导入。

LPO 的核心是把模块内 DSP/retimer 拿掉，只保留线性 Driver、TIA，让主机 ASIC/SerDes 承担更多均衡与补偿。这样做的好处是功耗与延迟降低，坏处是互通、校准、training、主机 SerDes 能力要求都更高。

在 1.6T 时代，EML 仍然是主流光源。Lumentum 在 OFC 2025 展示 448Gbps、224GBaud PAM4 EML，说明 EML 在单通道速率上仍有上探能力。同时 450G PAM4 DFB-MZI 的展示也说明 InP 平台并没有在 200G/lane 后失去价值。

真正的问题不是 EML 不能做，而是当系统走向 3.2T/6.4T，模块内分散发光与分散调制的架构是否仍是最经济的选择。

## **3.2T：NPO 的黄金窗口，而不是 CPO 一统天下**

3.2T 可能是争议最多的一代。很多文章会直接把 3.2T 说成 CPO 的开始，但更合理的判断是，3.2T 很可能是 NPO 的黄金窗口，市场会分化，而不是 CPO 一统天下甚至还不一定成为主流。

3.2T 对应 400G/lane。从物理压力看，CPO 的吸引力确实上升，因为前面板可插拔的走线、功耗、散热、面板密度都开始受压。

448G SerDes 下，3.2T 可插拔模块功耗可能进入 40–60W 区间，这已经高于 OSFP-XD 40W 上限，意味着单纯用传统前面板可插拔形态硬撑会越来越困难。

但从产业现实看，CPO 的封装、测试、良率、维修、标准化、供应链责任界面都还没有完全成熟。CPO 一旦把光引擎拉进 package 或 substrate，失效维修半径变大，供应链界面变复杂，客户集采模式也会被重构。这就给 NPO 留下非常重要的过渡窗口。

3.2T 可能形成两条大路线：第一条是 scale-up，用 VCSEL NPO 替代部分铜互连；第二条是 scale-out，用 CW/ELS + NPO。

前者利用 VCSEL 的低功耗、低成本、短距优势，面向 GPU 丛集内部；后者保留外置 CW 光源与硅光调制方向，但不一定立刻把光引擎完全推进 CPO 封装。

所以3.2T 不是「CPO 必然取代 NPO」，笔者认为更大的概率是「英伟达推 CPO，博通 + CSP 推 NPO」。英伟达有能力推 CPO，因为它掌握 GPU、NVLink、InfiniBand/Ethernet switch、系统设计与客户生态。

博通和 CSP 则更可能用 VCSEL NPO、CW NPO、高密度可插拔/XPO 等方式保留供应链弹性。

## **6.4T：CPO 开始变成主线**

到了 6.4T，问题已经不只是光源能不能做到 400G/lane，而是整个系统是否还值得维持 NPO 形态。

6.4T 如果用 16×400G 或更高密度通道，NPO 仍然可以工程化实现，但它的代价会明显上升，更多光引擎、更高电逃逸压力、更复杂的基板走线、更高散热负担、更难的校准和维修。

这时CPO 的系统级收益开始明显增加。

光引擎更靠近 ASIC，电走线更短，SerDes 功耗和信号损失更低，封装密度更高。

台积电 COUPE 路线也指向这一点：1.6T OE on substrate 是起点，6.4T OE on substrate 导入 CPO with switch，再往后进入 12.8T OE on interposer pathfinding。

从台积电的技术路线，我们可判断出6.4T是CPO 开始成为高端 scale-out、spine、switch fabric 的主线，但 NPO 仍会在部分 scale-up、可维修和成本敏感场景共存。

## **12.8T/OIO：光源成为系统级供光资源**

12.8T 以后，产业不应再把问题理解成更大号的光模块。它进入的是 CPO 到 OIO 的过渡，光 I/O 更靠近 ASIC、XPU，完全进入了interposer 或 CoWoS 类封装结构。

TSMC 的 3D optical interconnect 设计逻辑把光互连系统拆成 laser、fiber、waveguide、grating coupler、edge coupler、MRR、MRM、PD、MRM driver、TIA、thermal controller，再用 WDM 作为扩展轴。

这说明未来不是单一模块形态升级，而是光源、波导、调制、探测、驱动、热控全部进入系统级协同。

此时光源不再是模块内 EML，而是外置、集中、可替换、可监控、可冗余的 CW laser array / laser pool / ELS。光源从一个模块里的一颗器件变成整个计算系统的供光基础设施。

![](images/1c5a3ddb501fd2a93187.png)

## **EML、CW/ELS、VCSEL、MicroLED 的本质区别**
**
**
### ***EML：模块时代的最强光源***

EML 是 electro-absorption modulated laser，即电吸收调制激光器。它的本质是把 DFB 激光器和 EAM 电吸收调制器做在同一颗 InP 芯片上。

DFB 负责产生单模光，EAM 负责高速调制。这种结构的优点是高速、成熟、单模性能好、适合 FR/DR/LR 等单模链路，也适合 800G/1.6T 可插拔光模块。

DFB 的核心在于分布式布拉格光栅。普通 Fabry-Perot 激光器靠端面反射形成腔模，模式较多。DFB 透过周期性光栅在有源区附近提供波长选择，使激光器在指定波长单模工作。

对数据中心 1310nm O-band 或 1550nm C-band 场景，DFB 的波长稳定性、SMSR、线宽、RIN、温漂都会影响链路裕量。

EAM 的核心是 Franz-Keldysh 或量子限制 Stark 效应带来的吸收系数变化。当外加电场改变材料吸收边，EAM 对通过的光进行强度调制。

EAM 的优势是器件尺寸小、驱动电压低、调制速度高，适合与 DFB 在 InP 上单片集成。相比外置 MZM，EAM 可以把发光与调制做得更紧凑，但其 chirp、插入损耗、热稳定和高速眼图质量需要精细工程控制。

所以，EML 是 800G/1.6T 可插拔时代的最强光源，但它并不是 CPO/OIO 终局适合的方案。

EML最擅长的是模块级分布式发光与调制，而 CPO/OIO 要解决的是系统级集中供光与靠近 ASIC 的调制。

### ***CW/ELS：CPO/OIO 时代的系统级光源***

CW laser 是连续波激光器。它不负责高速调制，只输出稳定连续光。

ELS 是 external laser source，即外置光源模块，通常由多颗 CW DFB laser、laser array、隔离器、透镜、TEC、监控 PD、控制电路与光纤耦合结构组成。

CW/ELS 的产业意义是把 EML 中的 DFB 和 EAM 拆开，DFB/CW laser 留在光源端；EAM/MRM/MZM 调制功能搬到硅光 PIC 里。这不是简单的器件替代，而是光源与调制器位置的重新分工。

外置光源的最大工程价值是把温度敏感的激光器从高功率ASIC、GPU、switch package 周边移开。

激光器对温度非常敏感，温度会影响波长、输出功率、RIN、老化速度和模式稳定性。若把激光器放在 package 热源附近，波长控制与可靠性会很难。若用 ELS 外置供光，则可以用更独立的热管理、冗余、现场可替换 laser module 来提升整机可维修性。

Sivers、O-Net、Enablence 的 ELS 合作很有代表性，最近被频繁提及，Sivers 提供 DFB laser arrays，O-Net 作为 ODM 集成，Enablence 提供 NxN Star Coupler。

这说明 ELS 不再是一颗激光芯片，而是激光阵列、分光器、封装、热控和系统接口共同构成的小型供光系统。

### ***VCSEL：3.2T scale-up 替铜的最现实光源***

VCSEL 是垂直腔面发射激光器。它一般使用 GaAs 平台，而不是EML跟CW的InP。

光从晶圆表面垂直出射，而不是像边发射激光器那样从芯片侧面出光。这带来几个重要优势，晶圆级测试方便、阵列化容易、耦合到多模光纤成本低、阈值电流低、短距能效好。

从Broadcom 200G VCSEL展示的850nm VCSEL 在 106Gbd PAM4 下实现 200Gbps/lane 的路线，-3dB bandwidth 超过 35GHz，RIN 低于 -152dB/Hz，并在 50m OM4 光纤上展示无不可校正错误。

这些参数说明 VCSEL 不再只是 25G/50G SR 时代的低速方案，而可以在 200G/lane scale-up 中扮演重要角色。

VCSEL 的限制也很明确，它适合 <50m 的 scale-up，不适合 100m–2km 的 scale-out 主干。它适合多模短距，不适合长距单模。它可以打 3.2T 的黄金窗口，但 6.4T 再靠增加通道数硬堆会越来越痛苦。

因此，VCSEL 也不是 CPO/OIO 终局，但它很可能在 2026–2029 年左右成为 AI scale-up 从铜到光的部分过渡。

### ***MicroLED：短距激进方案，但不是主线***

MicroLED 方向是低速多通道、高并行、低功耗，理论上可以在短距 chip-to-chip 或 board-to-board 互连中提供低延迟方案。

它的逻辑与 400G/lane PAM4 不同：不是把每条 lane 推到极高速，而是用大量低速光通道并行传输，降低 DSP、FEC 和高速类比前端压力。

但 MicroLED 面临量产、耦合、生态、标准、可靠性等问题。MicroLED 制程涉及 III-V dry etching、侧壁损伤修复、ALD/CVD passivation、bonding、test & repair 等难点。

相比 VCSEL NPO 和 CW/ELS 硅光方案，MicroLED 更像短距光互连的一条激进分支，而不是 AI 数据中心光源主线。

![](images/16af550418a3dc0adeff.png)

 

## **EML是IDM 统治的时代**

进入光源产业链分析，第一个结论必须非常清楚，EML 时代不是所有光源公司都有机会，而是 InP IDM 统治。

原因很简单，EML 不是一颗 DFB 激光器，而是 DFB + EAM 的单片集成。DFB 和 EAM 都在 InP 平台上完成。

这要求企业同时具备 InP 外延、grating、DFB、EAM、芯片制程、端面处理、镀膜、测试、封装与可靠性能力。

纯 DFB 厂商没有 EAM，Fabless 没有 InP fab，III-V Foundry 没有客户侧完整可靠性数据，都很难在 EML 时代正面挑战 Lumentum、Coherent、Broadcom、Mitsubishi、Sumitomo、Source Photonics 这类 IDM。

EML器件与加工

EML器件与加工

![](images/225b80a6e262e91c5359.png)

# 

全球EML主导企业

![](images/378903e3cc80c4436301.png)

## 

## **EML 时代谁被排除，谁稳定受益**

EML 时代真正能吃到核心价值的是能够自己做 InP 外延、DFB、EAM、封装、可靠性测试的 IDM。这使得很多看起来与光源相关的公司，在 EML 时代反而不容易受益。

第一，纯 CW/DFB 厂商被压制。因为客户买的是 EML，不是裸 DFB。

纯 DFB 能力不足以满足 800G/1.6T 主流 EML 模块需求。这也是为什么很多只有 CW/DFB 能力的公司，在 EML 时代很难和 Lumentum、Coherent 正面竞争。

第二，Fabless 被压制。Fabless 可以设计激光器，但 EML 的量产可靠性高度依赖 InP fab、外延与制程。对大型 CSP 和模块厂而言，一旦出现失效，责任界面非常复杂。因此 EML 时代客户更愿意选成熟 IDM。

第三，III-V Foundry 被压制。全新、联亚、IQE、Smart Photonics、III-V Lab 这类公司有价值，但在 EML 时代，真正高端 AI EML 主供应链仍集中在 IDM。

Foundry 更容易在 CW/ELS 时代放量，因为 CW laser 的功能边界更清楚，不需要把 EAM 一起做到极致。

第四，稳定受益的是衬底与前段设备。InP 衬底、MOCVD、刻蚀、沉积设备在 EML 时代仍受益。因为不管谁做 EML，都需要 InP wafer、外延、加工与制程控制。

## **CW/ELS 时代供应链被重新打开**

CPO/NPO/OIO 不是不需要光源，而是不再需要每个模块内自带 EML。

在 EML 时代，光源公司要同时提供 DFB + EAM；在 CW/ELS 时代，调制器进入硅光 PIC，光源端只需要提供稳定 CW 光。

这一变化非常大。它意味着没有EAM 能力的纯 CW/DFB 厂商开始有机会。Fabless + III-V Foundry 模式开始有空间。InP 衬底、外延、MOCVD、刻蚀、沉积需求外溢。光隔离器、透镜、TEC、FAU、外置光源模块成为新价值环节。Lumentum、Coherent 仍然强，但不再是唯一能做光源的人。

在 CW/ELS 时代，光源端的核心指标会转向：输出功率、RIN、线宽、波长稳定性、SMSR、热漂移、寿命、冗余能力、可替换性、与硅光 PIC WDM 的匹配。这和 EML 时代强调 DFB+EAM 高速调制不同。

![](images/fcc22ee05e28903b19d4.png)

 

## **CW/ELS 时代的产业链分层：IDM、Fabless、Foundry、衬底、设备**
**
**
### **原 EML IDM仍然最强，但竞争不再完全封闭**

Lumentum、Coherent、Broadcom、Mitsubishi、Sumitomo、Source Photonics 在 CW/ELS 时代仍然非常强。原因是 CW laser 仍是 InP 激光器，仍然需要外延、DFB、封装、可靠性和客户认证。

原有 EML IDM 不会因为 EAM 被搬走而失去价值，只是价值形态从 EML chip 变成 CW laser / laser array / ELS module。

但竞争不再像 EML 时代那么封闭。因为 EAM 不在光源内，纯 CW/DFB 能力的公司也有机会。过去不能做完整 EML 的厂商，若能做出高功率、低 RIN、波长稳定、长寿命 CW laser，就可以进入 ELS 供应链。

![](images/c6c3d1049a09894d4536.png)

### **新 CW laser IDM：源杰、Sivers、台湾华星光通，长光华芯等的新窗口**

新 CW laser IDM 的机会来自一个核心变化：产业不再要求光源端必须提供 DFB+EAM 一体化 EML。只要能提供高可靠 CW laser，就能进入 CPO/NPO/OIO 的供光链。

源杰科技代表中国DFB/CW/EML 光芯片能力。Sivers Photonics 代表欧洲/英国 DFB laser array 与 ELS 生态。长光华芯代表高功率半导体激光器平台向通信光源延伸的可能性。华星光、QD Laser、Quintessent 等则代表台日美不同光源路线的潜在切入。

![](images/95191b3d1d0f0175a2b6.png)

### **Fabless设计型公司 CW/ELS 时代最需要补强的一层**

EML 时代，Fabless 最大的问题是没有 InP fab，无法对 DFB+EAM 的完整可靠性负责。

但 CW/ELS 时代，调制器搬到硅光平台，光源端只要输出稳定 CW 光，Fabless 可以设计 laser array、外置光源架构、controller、photonic interposer 或光 I/O 系统，再找 III-V Foundry 或 IDM 代工。

这里要区分「纯光源Fabless」和「光 I/O 系统 Fabless」。

前者直接设计激光器、DFB array、外置光源模块；后者更偏向 photonic interposer、optical I/O、chip-to-chip 光互连，需要外置激光器作为系统供光来源。CW/ELS 时代，两类公司都会推高外部光源需求。

![](images/d7ee107ebd34f3e9da96.png)

### **中国光源三小金刚与平台型公司**

中国光源相关企业不能一概而论。源杰科技、仕佳光子、长光华芯常被市场放在「三小金刚」框架中讨论，但三者能力完全不同，源杰更接近DFB/CW/EML 光芯片；仕佳更偏 PLC/AWG/DFB/光器件；长光华芯是高功率半导体激光器平台，向通信 CW 光源延伸仍需产品、客户和可靠性验证。

此外，光迅科技、华工科技/华工正源、中际旭创、新易盛、天孚通信、太辰光、博创科技等公司也会在不同环节受益，但不能全部归为「光源核心」。

有些是模块厂，有些是光器件，有些是连接/FAU，有些是平台型公司。文章需要把它们放回正确位置，避免把所有 CPO 概念公司都写成光源核心受益者。

再加上A推票断章取义风气盛行，目前把通信级别的光源技术或者相关器件，包装成未来CPO高端光源或器件的几乎在每一家公司的宣传上都出现，辨别材料跟器件，传统光通讯与目前EML或者未来CPO在不同器件上的技术区别，是投资A股光题材标的的重中之重。。

![](images/97cec85cdbc93dac4d3c.png)

## **
**

### **III-V Foundry / Epi：CW/ELS 时代的外溢受益者**

III-V Foundry / Epi 在 EML 时代不是最核心，因为高端 EML 多由 IDM 自己做。

但 CW/ELS 时代，Fabless、外置光源模块公司、硅光平台公司都可能需要外部 InP/GaAs 外延与代工能力，这会让全新、联亚、IQE、Smart Photonics、III-V Lab 等公司的重要性上升。

这里也要注意区分：GaAs foundry、InP foundry、Epi wafer supplier、完整 laser IDM 不是一回事。

稳懋、宏捷科更偏 GaAs/RF foundry，这块与硅光热点有区别，早期做RF的近两年市场低迷，都不约而同往光互联的题材上蹭或者说转型，卓胜微当初自建工厂正是为了射频业务，如今也在往光互联市场发展。

全新、联亚更接近外延与III-V供应；Smart Photonics、III-V Lab 更像 InP PIC foundry 生态。

![](images/6bc8c3523ae0cedf7cba.png)

 

### **衬底：InP/GaAs 的上游底座**

无论是EML、CW DFB、InP PIC，还是 VCSEL，都离不开三五族衬底。InP 主要对应 1310nm/1550nm 通信光源，GaAs 主要对应 VCSEL、部分 850nm/940nm/1060nm 应用以及射频/功率半导体。

衬底的核心指标包括晶圆尺寸、缺陷密度、掺杂均匀性、翘曲、表面粗糙度、热稳定性与批次一致性。高端通信激光器对缺陷和一致性要求高，因为微小材料缺陷可能导致外延缺陷、模式不稳定、可靠性下降。

![](images/b8a8debe8bce0bc3e3e5.png)

 

### **设备：三五族光源前段制程**

这文不讨论ficonTEC、光耦合设备、ATE、探针卡、封测设备，因为本文中心是光源本体，尤其是 InP/GaAs 的激光器制造。

设备部分只保留三五族前段制程：MOCVD、刻蚀、沉积、金属化、清洗/去损伤。

三五族光源前段制程的核心是材料和表面。其中： 

MOCVD 决定量子阱、波导、有源区质量；

刻蚀决定 DFB 光栅、脊波导、mesa、隔离槽的形貌和损伤；

沉积与 passivation 决定表面复合、漏电、可靠性；

金属化决定接触电阻、热阻与高速电性能。

这里要避免一个A 股常见误区，CPO 热度不等于所有后段自动化耦合设备都成为最核心环节。对光源本体而言，最底层的是三五族材料与前段制程，尤其是 MOCVD 外延、DFB 光栅与波导刻蚀、表面 passivation、电极金属化与可靠性控制。

其中MOCVD是三五族特有关键设备。这也是前两年我在推荐国产设备股的时候一直是把中微放在首位的加分項，前两年就能看到未来三五族MOCVD因为光互联的繁荣，不过中微的重点是放在LED，需要有所侧重转向。

![](images/76177ae9f07a3c305f2f.png)

 

## **ELS 不是一颗激光器，而是一个完整光源系统**

很多分析把 CW/ELS 简化成只要 DFB，这不完整。真正的 ELS 是一个小型光源系统。

它至少包括 InP substrate、epitaxy、DFB laser die、laser array、wavelength locker、monitor PD、isolator、Faraday rotator、lens/collimator、TEC、thermistor、hermetic package、fiber pigtail、FAU、control board/driver。

ELS的难点不是单颗 DFB 亮起来，而是多颗激光器功率一致、波长稳定、RIN 低、热漂小、反射可控、寿命长、可替换、可监控，并能与硅光 PIC 的 WDM/调制器精准匹配。

在 CPO/OIO 架构下，激光器通常不应放在最热的 ASIC/package 周边，因为温度会影响波长与可靠性。

ELS 将 laser source 外置，可透过独立散热和冗余设计提升 serviceability，也让 laser module 成为可以现场替换的系统部件。ELS大大地改善了CPO的可维护性，可维护性一直是CPO被行业诟病的核心。

CW/ELS供应链全景

![](images/e5141efcf52c7974302e.png)

 

### **不能把 TGG/TSAG 和通信级隔离器混为一谈**

光隔离器在 ELS 中非常关键。外置激光器最怕反射光回灌，反射会造成模式跳变、RIN 上升、波长漂移、相位噪声甚至激光器失效。光隔离器的功能就是让光单向通过，阻止反射光回到激光腔。

典型隔离器由 input polarizer、Faraday rotator、output polarizer、magnet、lens/collimator、封装结构组成。

Faraday rotator 在磁场下旋转偏振方向，配合偏振器实现单向通光。

这里要特别科普，TGG/TSAG 不等于通信级高端隔离器。TGG、TSAG 常见于高功率工业激光与部分近红外应用，但通信级 1310/1550nm 小型化隔离器更重视插损、隔离度、回损、温漂、偏振一致性、小尺寸、薄片加工与封装匹配。

GRANOPT、Sumitomo 这类日系磁光材料与隔离器供应商的优势，不只是有晶体，而是它们在通信波段、小型化薄片、低插损、高隔离与长期可靠性上的制程积累。

福晶科技有磁光晶体能力，但不能简单等同于 Coherent、Sumitomo、GRANOPT 的通信级隔离器供应地位。

若要进入 CPO/ELS 供应链，核心不是能做或有TGG/TSAG产品线，而是能否做到通信级小型化、低插损、高隔离、高一致性与长期可靠性。

简单说传统的工业脉冲激光、科研、高功率固态激光（1064nm 为主）的法拉第炫光片与EML/CW/ELS的1310nm与1550nm波长的光隔离器材料相同但制作工艺上是两码事。做材料跟做成品元器件是两码事。

![](images/f4ccb950be73fde88073.png)

 

### 

### **EML 时代 vs CW/ELS 时代：产业链重构表**

![](images/942297a53877be3d259b.png)

 

**让我们再复习一下未来光互联形式的方案演变****
**
### **3.2T 为什么是 NPO 的黄金窗口**

3.2T 时代，光模块厂不会愿意立刻把主导权交给 Foundry 和 CPO 封装平台。因为 NPO 还保留了模块厂的制造角色，也保留了 CSP 喜欢的可维修性、多供应商和部署弹性。

Scale-up 方向，VCSEL NPO 的优势是低功耗、低成本、短距足够、可靠性好。200G/lane VCSEL 可支撑 3.2T scale-up，能效可接近 1pJ/bit，对比铜缆在更长距离、更大机柜域中的损耗与布线压力，VCSEL NPO 是非常务实的替铜方案。

Scale-out 方向，CW/ELS NPO 则可以把光源外置，把调制放在硅光光引擎，但不一定立刻做完整 CPO。这样既能降低一部分功耗，又保留一定可维修性和供应链开放度。对博通与 CSP 而言，这比高度封闭的 CPO 更符合多供应商采购与白盒生态逻辑。

因此，3.2T 不会是一条路线吃掉所有市场，而是分化：英伟达偏 CPO，博通偏 NPO+CPO 双轨，CSP 更偏 NPO/XPO/CPX，模块厂强推 NPO/XPO，Foundry 则更希望 CPO/OIO 把价值推向 PIC/EIC/封装平台。

![](images/796472b619784cd6d418.png)

### **6.4T CPO 的主场**

到了 6.4T，NPO 的优势开始下降。原因不是 VCSEL、CW 或 EML 不能继续进步，而是系统层面的代价变高。通道数增加，光引擎数量增加，电逃逸距离与损耗难以控制，基板与连接器设计更复杂，热管理压力上升，校准与测试成本上升，维修半径变大。

所以6.4T 的光源形态大概率是外置 ELS + 硅光 PIC + CPO 光引擎。这里光源行业不是被消灭，而是变成外置供光模块。模块厂如果仍停留在传统可插拔装配，就会被削弱；但如果能切入 ELS、FAU、光纤连接、激光器封装、测试，仍然有位置。

CPO 的真正价值不是「把模块塞进封装」，而是把高功耗、高损耗、高延迟的电逃逸缩短，把光调制放在更接近 ASIC 的位置。此时光源端最好的工程选择不是把激光器也放在热源旁，而是外置化、冗余化和可维修化。

### **12.8T/OIO：光源的终局是 laser pool**

12.8T 和 OIO 时代，光源会进一步系统化。这时不应再说某颗 EML 多少 G，而要说整个系统如何分配光功率、波长、冗余、热控与维修。

未来的光源可能是多通道ELS、laser pool、remote laser source、可替换 laser cartridge，并与 CPO/OIO 光引擎标准化接口连接。

OIO 的核心不是把激光器放到 interposer 上，而是把调制与探测更靠近计算芯片，光源可以外置，避免热源与可靠性问题。

这个阶段的竞争不只是器件公司之间的竞争，而是系统厂、Foundry、InP 激光 IDM、Fabless 光 I/O 公司、外置光源模块厂之间的架构竞争。

谁能把稳定、低噪声、高功率、可维护的光送到最靠近计算芯片的地方，谁就掌握未来光互连的入口。

### **全球光源相关企业总表**

![](images/4b5800ebf558a852901b.png)

## **2025–2030+ 光互连与光源技术时间轴**

这张表是整篇文章的总结性图谱。它不是精准预测每家公司产品节奏，而是把 PO 形态、光源形式、单通道速率、路数、调制器材料与产业主线放在同一张时间轴里。

核心要点是：2025–2027 年是 EML IDM 收获期；2028 年前后是 NPO 黄金窗口；2029–2030 年后 CPO/OIO 把光源从模块内器件重构为系统级供光资源。

![](images/326fff36d1a6dc6e8a52.png)

## **结论 CPO 不消灭光源，而是重分配光源价值**

这篇文章最后要落在一个清楚的判断：2025–2027 年，是 EML IDM 的收获期；2028 年前后，是 NPO 的黄金窗口；2029–2030 年后，CPO/OIO 把光源从模块内器件重构为系统级供光资源。

所以，光源产业不是被 CPO 消灭，而是被 CPO 和 OIO 重构。EML 时代，价值在 DFB + EAM 一体化，只有 InP IDM 能吃大头。CW/ELS 时代，EAM 被搬到硅光平台，光源端回到 CW DFB laser，纯 CW laser IDM、Fabless、III-V Foundry、衬底、隔离器、TEC、透镜、FAU 全部被重新放进产业链。

3.2T 是这场变局的分水岭，但它不是 CPO 一统天下的时刻。更大概率是：英伟达推 CPO，博通与 CSP 推 VCSEL/CW NPO，模块厂用 XPO、NPO 延长自己的生命周期。真正到 6.4T、12.8T/OIO，光源才会从模块内分布式 EML，全面转向外置、集中、可维护、可监控的 CW/ELS。

一句话总结：800G/1.6T 看 EML IDM；3.2T 看 NPO 分化；6.4T 看 CPO 成熟；12.8T/OIO 看 laser pool。光源不是消失，而是从一颗器件，变成 AI 计算系统的基础设施。

### 本文感想：

最近一直在学习光互联产业，了解越深越觉得自己知识的渺小，本文早在十天之前就写好初稿，但与许多光通信专家与做了十多年硅光的老朋友讨论之后，发现目前光互联技术路线处于战国时期。

各种技术路线都认为自己的方向正确，欧美台的产业链跟国内的观点不太一样，国内依托光模块产业链大家都是奋力的阻挡CPO的产业链迁移，问到CPO总是有一千个理由，CPO有总总困难没那么快。

可与欧美或台系的产业内朋友聊却是另一番光景，整个行业都在摩拳擦掌迎接CPO的到来。

最终经过与许多业内朋友的讨论，汇整这一份资料，内容并非完全依照专家的意见，因为有的观点完全不同，甚至是对立的，我只能自己根据自己的产业经验与主流企业的技术方向自行延伸并做出判断。

笔者综合下来，6.4T也就是2029/2030年左右会是一个真正的分水岭，NPO即便延寿再成功也阻挡不了CPO成为主流，光模块厂失去新增量，但这是好几年以后的叙事，在二级市场上不用过份放大影响。

3.2T的VCSEL NPO增加了scale up这个全新增量，让我在现阶段看好光模块厂，因为2029/2030年的6.4T还早，明年跟后年的3.2T还是光模块主导的NPO，且还增加了以前没有的scale up，我认为2026年只要光模块厂有下跌都是可以入手的好机会，因为未来两年的业绩都是大好。

本文因为是写给普通网友与投资者看的，文章的论点并非很严谨，更多是本人自己衡量后依照经验做出的推演与判断。可能会有不同立场的专家有不同意见。

其实咱们星球内的有lumentun，cohernet以及三五族fab的许多从业者与朋友，这些老朋友有自己看法的也欢迎能提出，不吝赐教，大家可以试着讨论出未来最可能的方向，感谢各位。

        
        

### **导读：本文的核心判断**

AI 数据中心的光通信升级，表面上看是从 800G 到 1.6T、3.2T、6.4T、12.8T 的速率迭代，实际上是一次更深层的架构迁移：光互连正在从前面板可插拔模块，逐步走向 LPO、NPO、CPO，最后进入 OIO。

速率只是结果，真正改变产业权力格局的是光源位置、调制器位置、制造平台与系统维修模式的变化。

在 800G/1.6T 时代，光源仍在光模块里，EML 是核心。在 3.2T 时代，NPO 很可能成为 scale-up 与 scale-out 的主战场。到 6.4T 时代，CPO 的必要性明显提升，光源开始外置化。到 12.8T/OIO 时代，光源不再是模块内器件，而是系统级供光资源。

这条路线决定了光源行业的权力转移，EML 时代是 InP IDM 的天下；CW/ELS 时代，纯 CW 激光器 IDM、Fabless、III-V Foundry、衬底、隔离器、TEC、透镜与外置激光模块供应链都被重新打开。

CPO 不会消灭光源，反而会把光源从一颗器件升级为 AI 计算系统的基础设施。

LightCounting 在 2026 年 3 月 Ethernet Optics 报告中提出，在多个条件同时配合的情况下，AI cluster optical interconnect 年销售额到 2030 年有合理机会达到 1000 亿美元级别；这是把 AI cluster optics 作为一个大口径市场来看。

Yole 早期对狭义 CPO 的预测更保守，估算 CPO 市场从 2022 年约 3800 万美元增长到 2033 年约 26 亿美元，CAGR 约 46%。两者差异说明：只看 CPO module，市场不算夸张；若把 LPO、NPO、CPO、OIO、ELS、AI cluster optics 合并看，产业锚会大幅上移。

Lumentum、Coherent 对 2030 年 optical interconnect / datacom 可服务市场的表述均大幅上移，反映激光器、光源模块与光互连系统已经从传统光模块配套件，变成 AI 基础设施的关键瓶颈。

### **先看代际：100G、200G、400G 单通道如何推动架构迁移**

光通信产业每一代升级，最关键的不是总带宽，而是单通道速率。

总带宽可以靠增加路数堆出来，但单通道速率一旦翻倍，整个链路的压力会同时落到SerDes、DSP、Driver、TIA、光源、调制器、封装、散热、PCB/基板走线、前面板密度和可维修性上。

也就是说，100G/lane、200G/lane、400G/lane 不是单纯的数字，而是三个不同工程时代。

400G 是 4×100G，800G 是 8×100G，1.6T 进入 8×200G、约 106.25GBaud，3.2T 则进入 8×400G、约 224GBaud。

当单通道从 100G 到 200G，传统可插拔还能靠更先进 DSP、LPO、优化热设计继续撑住。当单通道进入 400G，传统前面板可插拔的功耗、散热、信号完整性与封装密度会同步逼近极限。

因此，要先搞明白EML、CW、VCSEL、MicroLED等光源技术演变，就必须先把 Pluggable、LPO、NPO、CPO、OIO 这条架构演化路线讲清楚。

光源技术不是孤立演进，而是被架构迁移推动。

## **800G：100G/lane，可插拔仍然舒适**

800G 的主流形态是 8×100G/lane。这一代光模块仍然以 OSFP、QSFP-DD 等可插拔形态为主，EML、硅光、VCSEL 都有应用，但在 AI 数据中心单模短距与中距场景里，EML 是最成熟的主流光源。

这一阶段的核心特征是：光源在模块内，调制器也在模块内，光模块厂采购EML、DSP、Driver/TIA、透镜、FAU、PCB、外壳，完成模块组装与测试。

光源产业链的核心价值在 EML IDM 手中，因为 EML 不是单一 DFB，而是 DFB + EAM 的 InP 单片集成器件。

800G 时代的可插拔逻辑仍然成立：模块热插拔、供应商可替换、维修半径小、数据中心集采模式成熟。光源位于模块内部并不构成系统性问题，因为单模块功耗与散热尚能在 OSFP/QSFP-DD 的热设计内被消化。

## **1.6T：200G/lane，可插拔仍是主流， LPO 开始延寿**

1.6T 主流是 8×200G/lane。1.6T 还没有让 CPO 成为主流，因为可插拔模块仍有维修性、部署弹性、供应链成熟度与标准化优势。

但压力开始明显增加，1.6T 可插拔模块功耗约 20–28W，其中 DSP/SerDes 占 10–14W，接近 50%。LPO 移除模块内完整 DSP 后，可把功耗压到约 12–15W。

所以1.6T 的本质不是 CPO 立刻取代可插拔，而是 Full DSP Pluggable → LPO Pluggable → NPO/CPO 预备导入。

LPO 的核心是把模块内 DSP/retimer 拿掉，只保留线性 Driver、TIA，让主机 ASIC/SerDes 承担更多均衡与补偿。这样做的好处是功耗与延迟降低，坏处是互通、校准、training、主机 SerDes 能力要求都更高。

在 1.6T 时代，EML 仍然是主流光源。Lumentum 在 OFC 2025 展示 448Gbps、224GBaud PAM4 EML，说明 EML 在单通道速率上仍有上探能力。同时 450G PAM4 DFB-MZI 的展示也说明 InP 平台并没有在 200G/lane 后失去价值。

真正的问题不是 EML 不能做，而是当系统走向 3.2T/6.4T，模块内分散发光与分散调制的架构是否仍是最经济的选择。

## **3.2T：NPO 的黄金窗口，而不是 CPO 一统天下**

3.2T 可能是争议最多的一代。很多文章会直接把 3.2T 说成 CPO 的开始，但更合理的判断是，3.2T 很可能是 NPO 的黄金窗口，市场会分化，而不是 CPO 一统天下甚至还不一定成为主流。

3.2T 对应 400G/lane。从物理压力看，CPO 的吸引力确实上升，因为前面板可插拔的走线、功耗、散热、面板密度都开始受压。

448G SerDes 下，3.2T 可插拔模块功耗可能进入 40–60W 区间，这已经高于 OSFP-XD 40W 上限，意味着单纯用传统前面板可插拔形态硬撑会越来越困难。

但从产业现实看，CPO 的封装、测试、良率、维修、标准化、供应链责任界面都还没有完全成熟。CPO 一旦把光引擎拉进 package 或 substrate，失效维修半径变大，供应链界面变复杂，客户集采模式也会被重构。这就给 NPO 留下非常重要的过渡窗口。

3.2T 可能形成两条大路线：第一条是 scale-up，用 VCSEL NPO 替代部分铜互连；第二条是 scale-out，用 CW/ELS + NPO。

前者利用 VCSEL 的低功耗、低成本、短距优势，面向 GPU 丛集内部；后者保留外置 CW 光源与硅光调制方向，但不一定立刻把光引擎完全推进 CPO 封装。

所以3.2T 不是「CPO 必然取代 NPO」，笔者认为更大的概率是「英伟达推 CPO，博通 + CSP 推 NPO」。英伟达有能力推 CPO，因为它掌握 GPU、NVLink、InfiniBand/Ethernet switch、系统设计与客户生态。

博通和 CSP 则更可能用 VCSEL NPO、CW NPO、高密度可插拔/XPO 等方式保留供应链弹性。

## **6.4T：CPO 开始变成主线**

到了 6.4T，问题已经不只是光源能不能做到 400G/lane，而是整个系统是否还值得维持 NPO 形态。

6.4T 如果用 16×400G 或更高密度通道，NPO 仍然可以工程化实现，但它的代价会明显上升，更多光引擎、更高电逃逸压力、更复杂的基板走线、更高散热负担、更难的校准和维修。

这时CPO 的系统级收益开始明显增加。

光引擎更靠近 ASIC，电走线更短，SerDes 功耗和信号损失更低，封装密度更高。

台积电 COUPE 路线也指向这一点：1.6T OE on substrate 是起点，6.4T OE on substrate 导入 CPO with switch，再往后进入 12.8T OE on interposer pathfinding。

从台积电的技术路线，我们可判断出6.4T是CPO 开始成为高端 scale-out、spine、switch fabric 的主线，但 NPO 仍会在部分 scale-up、可维修和成本敏感场景共存。

## **12.8T/OIO：光源成为系统级供光资源**

12.8T 以后，产业不应再把问题理解成更大号的光模块。它进入的是 CPO 到 OIO 的过渡，光 I/O 更靠近 ASIC、XPU，完全进入了interposer 或 CoWoS 类封装结构。

TSMC 的 3D optical interconnect 设计逻辑把光互连系统拆成 laser、fiber、waveguide、grating coupler、edge coupler、MRR、MRM、PD、MRM driver、TIA、thermal controller，再用 WDM 作为扩展轴。

这说明未来不是单一模块形态升级，而是光源、波导、调制、探测、驱动、热控全部进入系统级协同。

此时光源不再是模块内 EML，而是外置、集中、可替换、可监控、可冗余的 CW laser array / laser pool / ELS。光源从一个模块里的一颗器件变成整个计算系统的供光基础设施。

![](images/1c5a3ddb501fd2a93187.png)

## **EML、CW/ELS、VCSEL、MicroLED 的本质区别**
**
**
### ***EML：模块时代的最强光源***

EML 是 electro-absorption modulated laser，即电吸收调制激光器。它的本质是把 DFB 激光器和 EAM 电吸收调制器做在同一颗 InP 芯片上。

DFB 负责产生单模光，EAM 负责高速调制。这种结构的优点是高速、成熟、单模性能好、适合 FR/DR/LR 等单模链路，也适合 800G/1.6T 可插拔光模块。

DFB 的核心在于分布式布拉格光栅。普通 Fabry-Perot 激光器靠端面反射形成腔模，模式较多。DFB 透过周期性光栅在有源区附近提供波长选择，使激光器在指定波长单模工作。

对数据中心 1310nm O-band 或 1550nm C-band 场景，DFB 的波长稳定性、SMSR、线宽、RIN、温漂都会影响链路裕量。

EAM 的核心是 Franz-Keldysh 或量子限制 Stark 效应带来的吸收系数变化。当外加电场改变材料吸收边，EAM 对通过的光进行强度调制。

EAM 的优势是器件尺寸小、驱动电压低、调制速度高，适合与 DFB 在 InP 上单片集成。相比外置 MZM，EAM 可以把发光与调制做得更紧凑，但其 chirp、插入损耗、热稳定和高速眼图质量需要精细工程控制。

所以，EML 是 800G/1.6T 可插拔时代的最强光源，但它并不是 CPO/OIO 终局适合的方案。

EML最擅长的是模块级分布式发光与调制，而 CPO/OIO 要解决的是系统级集中供光与靠近 ASIC 的调制。

### ***CW/ELS：CPO/OIO 时代的系统级光源***

CW laser 是连续波激光器。它不负责高速调制，只输出稳定连续光。

ELS 是 external laser source，即外置光源模块，通常由多颗 CW DFB laser、laser array、隔离器、透镜、TEC、监控 PD、控制电路与光纤耦合结构组成。

CW/ELS 的产业意义是把 EML 中的 DFB 和 EAM 拆开，DFB/CW laser 留在光源端；EAM/MRM/MZM 调制功能搬到硅光 PIC 里。这不是简单的器件替代，而是光源与调制器位置的重新分工。

外置光源的最大工程价值是把温度敏感的激光器从高功率ASIC、GPU、switch package 周边移开。

激光器对温度非常敏感，温度会影响波长、输出功率、RIN、老化速度和模式稳定性。若把激光器放在 package 热源附近，波长控制与可靠性会很难。若用 ELS 外置供光，则可以用更独立的热管理、冗余、现场可替换 laser module 来提升整机可维修性。

Sivers、O-Net、Enablence 的 ELS 合作很有代表性，最近被频繁提及，Sivers 提供 DFB laser arrays，O-Net 作为 ODM 集成，Enablence 提供 NxN Star Coupler。

这说明 ELS 不再是一颗激光芯片，而是激光阵列、分光器、封装、热控和系统接口共同构成的小型供光系统。

### ***VCSEL：3.2T scale-up 替铜的最现实光源***

VCSEL 是垂直腔面发射激光器。它一般使用 GaAs 平台，而不是EML跟CW的InP。

光从晶圆表面垂直出射，而不是像边发射激光器那样从芯片侧面出光。这带来几个重要优势，晶圆级测试方便、阵列化容易、耦合到多模光纤成本低、阈值电流低、短距能效好。

从Broadcom 200G VCSEL展示的850nm VCSEL 在 106Gbd PAM4 下实现 200Gbps/lane 的路线，-3dB bandwidth 超过 35GHz，RIN 低于 -152dB/Hz，并在 50m OM4 光纤上展示无不可校正错误。

这些参数说明 VCSEL 不再只是 25G/50G SR 时代的低速方案，而可以在 200G/lane scale-up 中扮演重要角色。

VCSEL 的限制也很明确，它适合 <50m 的 scale-up，不适合 100m–2km 的 scale-out 主干。它适合多模短距，不适合长距单模。它可以打 3.2T 的黄金窗口，但 6.4T 再靠增加通道数硬堆会越来越痛苦。

因此，VCSEL 也不是 CPO/OIO 终局，但它很可能在 2026–2029 年左右成为 AI scale-up 从铜到光的部分过渡。

### ***MicroLED：短距激进方案，但不是主线***

MicroLED 方向是低速多通道、高并行、低功耗，理论上可以在短距 chip-to-chip 或 board-to-board 互连中提供低延迟方案。

它的逻辑与 400G/lane PAM4 不同：不是把每条 lane 推到极高速，而是用大量低速光通道并行传输，降低 DSP、FEC 和高速类比前端压力。

但 MicroLED 面临量产、耦合、生态、标准、可靠性等问题。MicroLED 制程涉及 III-V dry etching、侧壁损伤修复、ALD/CVD passivation、bonding、test & repair 等难点。

相比 VCSEL NPO 和 CW/ELS 硅光方案，MicroLED 更像短距光互连的一条激进分支，而不是 AI 数据中心光源主线。

![](images/16af550418a3dc0adeff.png)

 

## **EML是IDM 统治的时代**

进入光源产业链分析，第一个结论必须非常清楚，EML 时代不是所有光源公司都有机会，而是 InP IDM 统治。

原因很简单，EML 不是一颗 DFB 激光器，而是 DFB + EAM 的单片集成。DFB 和 EAM 都在 InP 平台上完成。

这要求企业同时具备 InP 外延、grating、DFB、EAM、芯片制程、端面处理、镀膜、测试、封装与可靠性能力。

纯 DFB 厂商没有 EAM，Fabless 没有 InP fab，III-V Foundry 没有客户侧完整可靠性数据，都很难在 EML 时代正面挑战 Lumentum、Coherent、Broadcom、Mitsubishi、Sumitomo、Source Photonics 这类 IDM。

EML器件与加工

EML器件与加工

![](images/225b80a6e262e91c5359.png)

# 

全球EML主导企业

![](images/378903e3cc80c4436301.png)

## 

## **EML 时代谁被排除，谁稳定受益**

EML 时代真正能吃到核心价值的是能够自己做 InP 外延、DFB、EAM、封装、可靠性测试的 IDM。这使得很多看起来与光源相关的公司，在 EML 时代反而不容易受益。

第一，纯 CW/DFB 厂商被压制。因为客户买的是 EML，不是裸 DFB。

纯 DFB 能力不足以满足 800G/1.6T 主流 EML 模块需求。这也是为什么很多只有 CW/DFB 能力的公司，在 EML 时代很难和 Lumentum、Coherent 正面竞争。

第二，Fabless 被压制。Fabless 可以设计激光器，但 EML 的量产可靠性高度依赖 InP fab、外延与制程。对大型 CSP 和模块厂而言，一旦出现失效，责任界面非常复杂。因此 EML 时代客户更愿意选成熟 IDM。

第三，III-V Foundry 被压制。全新、联亚、IQE、Smart Photonics、III-V Lab 这类公司有价值，但在 EML 时代，真正高端 AI EML 主供应链仍集中在 IDM。

Foundry 更容易在 CW/ELS 时代放量，因为 CW laser 的功能边界更清楚，不需要把 EAM 一起做到极致。

第四，稳定受益的是衬底与前段设备。InP 衬底、MOCVD、刻蚀、沉积设备在 EML 时代仍受益。因为不管谁做 EML，都需要 InP wafer、外延、加工与制程控制。

## **CW/ELS 时代供应链被重新打开**

CPO/NPO/OIO 不是不需要光源，而是不再需要每个模块内自带 EML。

在 EML 时代，光源公司要同时提供 DFB + EAM；在 CW/ELS 时代，调制器进入硅光 PIC，光源端只需要提供稳定 CW 光。

这一变化非常大。它意味着没有EAM 能力的纯 CW/DFB 厂商开始有机会。Fabless + III-V Foundry 模式开始有空间。InP 衬底、外延、MOCVD、刻蚀、沉积需求外溢。光隔离器、透镜、TEC、FAU、外置光源模块成为新价值环节。Lumentum、Coherent 仍然强，但不再是唯一能做光源的人。

在 CW/ELS 时代，光源端的核心指标会转向：输出功率、RIN、线宽、波长稳定性、SMSR、热漂移、寿命、冗余能力、可替换性、与硅光 PIC WDM 的匹配。这和 EML 时代强调 DFB+EAM 高速调制不同。

![](images/fcc22ee05e28903b19d4.png)

 

## **CW/ELS 时代的产业链分层：IDM、Fabless、Foundry、衬底、设备**
**
**
### **原 EML IDM仍然最强，但竞争不再完全封闭**

Lumentum、Coherent、Broadcom、Mitsubishi、Sumitomo、Source Photonics 在 CW/ELS 时代仍然非常强。原因是 CW laser 仍是 InP 激光器，仍然需要外延、DFB、封装、可靠性和客户认证。

原有 EML IDM 不会因为 EAM 被搬走而失去价值，只是价值形态从 EML chip 变成 CW laser / laser array / ELS module。

但竞争不再像 EML 时代那么封闭。因为 EAM 不在光源内，纯 CW/DFB 能力的公司也有机会。过去不能做完整 EML 的厂商，若能做出高功率、低 RIN、波长稳定、长寿命 CW laser，就可以进入 ELS 供应链。

![](images/c6c3d1049a09894d4536.png)

### **新 CW laser IDM：源杰、Sivers、台湾华星光通，长光华芯等的新窗口**

新 CW laser IDM 的机会来自一个核心变化：产业不再要求光源端必须提供 DFB+EAM 一体化 EML。只要能提供高可靠 CW laser，就能进入 CPO/NPO/OIO 的供光链。

源杰科技代表中国DFB/CW/EML 光芯片能力。Sivers Photonics 代表欧洲/英国 DFB laser array 与 ELS 生态。长光华芯代表高功率半导体激光器平台向通信光源延伸的可能性。华星光、QD Laser、Quintessent 等则代表台日美不同光源路线的潜在切入。

![](images/95191b3d1d0f0175a2b6.png)

### **Fabless设计型公司 CW/ELS 时代最需要补强的一层**

EML 时代，Fabless 最大的问题是没有 InP fab，无法对 DFB+EAM 的完整可靠性负责。

但 CW/ELS 时代，调制器搬到硅光平台，光源端只要输出稳定 CW 光，Fabless 可以设计 laser array、外置光源架构、controller、photonic interposer 或光 I/O 系统，再找 III-V Foundry 或 IDM 代工。

这里要区分「纯光源Fabless」和「光 I/O 系统 Fabless」。

前者直接设计激光器、DFB array、外置光源模块；后者更偏向 photonic interposer、optical I/O、chip-to-chip 光互连，需要外置激光器作为系统供光来源。CW/ELS 时代，两类公司都会推高外部光源需求。

![](images/d7ee107ebd34f3e9da96.png)

### **中国光源三小金刚与平台型公司**

中国光源相关企业不能一概而论。源杰科技、仕佳光子、长光华芯常被市场放在「三小金刚」框架中讨论，但三者能力完全不同，源杰更接近DFB/CW/EML 光芯片；仕佳更偏 PLC/AWG/DFB/光器件；长光华芯是高功率半导体激光器平台，向通信 CW 光源延伸仍需产品、客户和可靠性验证。

此外，光迅科技、华工科技/华工正源、中际旭创、新易盛、天孚通信、太辰光、博创科技等公司也会在不同环节受益，但不能全部归为「光源核心」。

有些是模块厂，有些是光器件，有些是连接/FAU，有些是平台型公司。文章需要把它们放回正确位置，避免把所有 CPO 概念公司都写成光源核心受益者。

再加上A推票断章取义风气盛行，目前把通信级别的光源技术或者相关器件，包装成未来CPO高端光源或器件的几乎在每一家公司的宣传上都出现，辨别材料跟器件，传统光通讯与目前EML或者未来CPO在不同器件上的技术区别，是投资A股光题材标的的重中之重。。

![](images/97cec85cdbc93dac4d3c.png)

## **
**

### **III-V Foundry / Epi：CW/ELS 时代的外溢受益者**

III-V Foundry / Epi 在 EML 时代不是最核心，因为高端 EML 多由 IDM 自己做。

但 CW/ELS 时代，Fabless、外置光源模块公司、硅光平台公司都可能需要外部 InP/GaAs 外延与代工能力，这会让全新、联亚、IQE、Smart Photonics、III-V Lab 等公司的重要性上升。

这里也要注意区分：GaAs foundry、InP foundry、Epi wafer supplier、完整 laser IDM 不是一回事。

稳懋、宏捷科更偏 GaAs/RF foundry，这块与硅光热点有区别，早期做RF的近两年市场低迷，都不约而同往光互联的题材上蹭或者说转型，卓胜微当初自建工厂正是为了射频业务，如今也在往光互联市场发展。

全新、联亚更接近外延与III-V供应；Smart Photonics、III-V Lab 更像 InP PIC foundry 生态。

![](images/6bc8c3523ae0cedf7cba.png)

 

### **衬底：InP/GaAs 的上游底座**

无论是EML、CW DFB、InP PIC，还是 VCSEL，都离不开三五族衬底。InP 主要对应 1310nm/1550nm 通信光源，GaAs 主要对应 VCSEL、部分 850nm/940nm/1060nm 应用以及射频/功率半导体。

衬底的核心指标包括晶圆尺寸、缺陷密度、掺杂均匀性、翘曲、表面粗糙度、热稳定性与批次一致性。高端通信激光器对缺陷和一致性要求高，因为微小材料缺陷可能导致外延缺陷、模式不稳定、可靠性下降。

![](images/b8a8debe8bce0bc3e3e5.png)

 

### **设备：三五族光源前段制程**

这文不讨论ficonTEC、光耦合设备、ATE、探针卡、封测设备，因为本文中心是光源本体，尤其是 InP/GaAs 的激光器制造。

设备部分只保留三五族前段制程：MOCVD、刻蚀、沉积、金属化、清洗/去损伤。

三五族光源前段制程的核心是材料和表面。其中： 

MOCVD 决定量子阱、波导、有源区质量；

刻蚀决定 DFB 光栅、脊波导、mesa、隔离槽的形貌和损伤；

沉积与 passivation 决定表面复合、漏电、可靠性；

金属化决定接触电阻、热阻与高速电性能。

这里要避免一个A 股常见误区，CPO 热度不等于所有后段自动化耦合设备都成为最核心环节。对光源本体而言，最底层的是三五族材料与前段制程，尤其是 MOCVD 外延、DFB 光栅与波导刻蚀、表面 passivation、电极金属化与可靠性控制。

其中MOCVD是三五族特有关键设备。这也是前两年我在推荐国产设备股的时候一直是把中微放在首位的加分項，前两年就能看到未来三五族MOCVD因为光互联的繁荣，不过中微的重点是放在LED，需要有所侧重转向。

![](images/76177ae9f07a3c305f2f.png)

 

## **ELS 不是一颗激光器，而是一个完整光源系统**

很多分析把 CW/ELS 简化成只要 DFB，这不完整。真正的 ELS 是一个小型光源系统。

它至少包括 InP substrate、epitaxy、DFB laser die、laser array、wavelength locker、monitor PD、isolator、Faraday rotator、lens/collimator、TEC、thermistor、hermetic package、fiber pigtail、FAU、control board/driver。

ELS的难点不是单颗 DFB 亮起来，而是多颗激光器功率一致、波长稳定、RIN 低、热漂小、反射可控、寿命长、可替换、可监控，并能与硅光 PIC 的 WDM/调制器精准匹配。

在 CPO/OIO 架构下，激光器通常不应放在最热的 ASIC/package 周边，因为温度会影响波长与可靠性。

ELS 将 laser source 外置，可透过独立散热和冗余设计提升 serviceability，也让 laser module 成为可以现场替换的系统部件。ELS大大地改善了CPO的可维护性，可维护性一直是CPO被行业诟病的核心。

CW/ELS供应链全景

![](images/e5141efcf52c7974302e.png)

 

### **不能把 TGG/TSAG 和通信级隔离器混为一谈**

光隔离器在 ELS 中非常关键。外置激光器最怕反射光回灌，反射会造成模式跳变、RIN 上升、波长漂移、相位噪声甚至激光器失效。光隔离器的功能就是让光单向通过，阻止反射光回到激光腔。

典型隔离器由 input polarizer、Faraday rotator、output polarizer、magnet、lens/collimator、封装结构组成。

Faraday rotator 在磁场下旋转偏振方向，配合偏振器实现单向通光。

这里要特别科普，TGG/TSAG 不等于通信级高端隔离器。TGG、TSAG 常见于高功率工业激光与部分近红外应用，但通信级 1310/1550nm 小型化隔离器更重视插损、隔离度、回损、温漂、偏振一致性、小尺寸、薄片加工与封装匹配。

GRANOPT、Sumitomo 这类日系磁光材料与隔离器供应商的优势，不只是有晶体，而是它们在通信波段、小型化薄片、低插损、高隔离与长期可靠性上的制程积累。

福晶科技有磁光晶体能力，但不能简单等同于 Coherent、Sumitomo、GRANOPT 的通信级隔离器供应地位。

若要进入 CPO/ELS 供应链，核心不是能做或有TGG/TSAG产品线，而是能否做到通信级小型化、低插损、高隔离、高一致性与长期可靠性。

简单说传统的工业脉冲激光、科研、高功率固态激光（1064nm 为主）的法拉第炫光片与EML/CW/ELS的1310nm与1550nm波长的光隔离器材料相同但制作工艺上是两码事。做材料跟做成品元器件是两码事。

![](images/f4ccb950be73fde88073.png)

 

### 

### **EML 时代 vs CW/ELS 时代：产业链重构表**

![](images/942297a53877be3d259b.png)

 

**让我们再复习一下未来光互联形式的方案演变****
**
### **3.2T 为什么是 NPO 的黄金窗口**

3.2T 时代，光模块厂不会愿意立刻把主导权交给 Foundry 和 CPO 封装平台。因为 NPO 还保留了模块厂的制造角色，也保留了 CSP 喜欢的可维修性、多供应商和部署弹性。

Scale-up 方向，VCSEL NPO 的优势是低功耗、低成本、短距足够、可靠性好。200G/lane VCSEL 可支撑 3.2T scale-up，能效可接近 1pJ/bit，对比铜缆在更长距离、更大机柜域中的损耗与布线压力，VCSEL NPO 是非常务实的替铜方案。

Scale-out 方向，CW/ELS NPO 则可以把光源外置，把调制放在硅光光引擎，但不一定立刻做完整 CPO。这样既能降低一部分功耗，又保留一定可维修性和供应链开放度。对博通与 CSP 而言，这比高度封闭的 CPO 更符合多供应商采购与白盒生态逻辑。

因此，3.2T 不会是一条路线吃掉所有市场，而是分化：英伟达偏 CPO，博通偏 NPO+CPO 双轨，CSP 更偏 NPO/XPO/CPX，模块厂强推 NPO/XPO，Foundry 则更希望 CPO/OIO 把价值推向 PIC/EIC/封装平台。

![](images/796472b619784cd6d418.png)

### **6.4T CPO 的主场**

到了 6.4T，NPO 的优势开始下降。原因不是 VCSEL、CW 或 EML 不能继续进步，而是系统层面的代价变高。通道数增加，光引擎数量增加，电逃逸距离与损耗难以控制，基板与连接器设计更复杂，热管理压力上升，校准与测试成本上升，维修半径变大。

所以6.4T 的光源形态大概率是外置 ELS + 硅光 PIC + CPO 光引擎。这里光源行业不是被消灭，而是变成外置供光模块。模块厂如果仍停留在传统可插拔装配，就会被削弱；但如果能切入 ELS、FAU、光纤连接、激光器封装、测试，仍然有位置。

CPO 的真正价值不是「把模块塞进封装」，而是把高功耗、高损耗、高延迟的电逃逸缩短，把光调制放在更接近 ASIC 的位置。此时光源端最好的工程选择不是把激光器也放在热源旁，而是外置化、冗余化和可维修化。

### **12.8T/OIO：光源的终局是 laser pool**

12.8T 和 OIO 时代，光源会进一步系统化。这时不应再说某颗 EML 多少 G，而要说整个系统如何分配光功率、波长、冗余、热控与维修。

未来的光源可能是多通道ELS、laser pool、remote laser source、可替换 laser cartridge，并与 CPO/OIO 光引擎标准化接口连接。

OIO 的核心不是把激光器放到 interposer 上，而是把调制与探测更靠近计算芯片，光源可以外置，避免热源与可靠性问题。

这个阶段的竞争不只是器件公司之间的竞争，而是系统厂、Foundry、InP 激光 IDM、Fabless 光 I/O 公司、外置光源模块厂之间的架构竞争。

谁能把稳定、低噪声、高功率、可维护的光送到最靠近计算芯片的地方，谁就掌握未来光互连的入口。

### **全球光源相关企业总表**

![](images/4b5800ebf558a852901b.png)

## **2025–2030+ 光互连与光源技术时间轴**

这张表是整篇文章的总结性图谱。它不是精准预测每家公司产品节奏，而是把 PO 形态、光源形式、单通道速率、路数、调制器材料与产业主线放在同一张时间轴里。

核心要点是：2025–2027 年是 EML IDM 收获期；2028 年前后是 NPO 黄金窗口；2029–2030 年后 CPO/OIO 把光源从模块内器件重构为系统级供光资源。

![](images/326fff36d1a6dc6e8a52.png)

## **结论 CPO 不消灭光源，而是重分配光源价值**

这篇文章最后要落在一个清楚的判断：2025–2027 年，是 EML IDM 的收获期；2028 年前后，是 NPO 的黄金窗口；2029–2030 年后，CPO/OIO 把光源从模块内器件重构为系统级供光资源。

所以，光源产业不是被 CPO 消灭，而是被 CPO 和 OIO 重构。EML 时代，价值在 DFB + EAM 一体化，只有 InP IDM 能吃大头。CW/ELS 时代，EAM 被搬到硅光平台，光源端回到 CW DFB laser，纯 CW laser IDM、Fabless、III-V Foundry、衬底、隔离器、TEC、透镜、FAU 全部被重新放进产业链。

3.2T 是这场变局的分水岭，但它不是 CPO 一统天下的时刻。更大概率是：英伟达推 CPO，博通与 CSP 推 VCSEL/CW NPO，模块厂用 XPO、NPO 延长自己的生命周期。真正到 6.4T、12.8T/OIO，光源才会从模块内分布式 EML，全面转向外置、集中、可维护、可监控的 CW/ELS。

一句话总结：800G/1.6T 看 EML IDM；3.2T 看 NPO 分化；6.4T 看 CPO 成熟；12.8T/OIO 看 laser pool。光源不是消失，而是从一颗器件，变成 AI 计算系统的基础设施。

### 本文感想：

最近一直在学习光互联产业，了解越深越觉得自己知识的渺小，本文早在十天之前就写好初稿，但与许多光通信专家与做了十多年硅光的老朋友讨论之后，发现目前光互联技术路线处于战国时期。

各种技术路线都认为自己的方向正确，欧美台的产业链跟国内的观点不太一样，国内依托光模块产业链大家都是奋力的阻挡CPO的产业链迁移，问到CPO总是有一千个理由，CPO有总总困难没那么快。

可与欧美或台系的产业内朋友聊却是另一番光景，整个行业都在摩拳擦掌迎接CPO的到来。

最终经过与许多业内朋友的讨论，汇整这一份资料，内容并非完全依照专家的意见，因为有的观点完全不同，甚至是对立的，我只能自己根据自己的产业经验与主流企业的技术方向自行延伸并做出判断。

笔者综合下来，6.4T也就是2029/2030年左右会是一个真正的分水岭，NPO即便延寿再成功也阻挡不了CPO成为主流，光模块厂失去新增量，但这是好几年以后的叙事，在二级市场上不用过份放大影响。

3.2T的VCSEL NPO增加了scale up这个全新增量，让我在现阶段看好光模块厂，因为2029/2030年的6.4T还早，明年跟后年的3.2T还是光模块主导的NPO，且还增加了以前没有的scale up，我认为2026年只要光模块厂有下跌都是可以入手的好机会，因为未来两年的业绩都是大好。

本文因为是写给普通网友与投资者看的，文章的论点并非很严谨，更多是本人自己衡量后依照经验做出的推演与判断。可能会有不同立场的专家有不同意见。

其实咱们星球内的有lumentun，cohernet以及三五族fab的许多从业者与朋友，这些老朋友有自己看法的也欢迎能提出，不吝赐教，大家可以试着讨论出未来最可能的方向，感谢各位。

        

### **导读：本文的核心判断**

AI 数据中心的光通信升级，表面上看是从 800G 到 1.6T、3.2T、6.4T、12.8T 的速率迭代，实际上是一次更深层的架构迁移：光互连正在从前面板可插拔模块，逐步走向 LPO、NPO、CPO，最后进入 OIO。

速率只是结果，真正改变产业权力格局的是光源位置、调制器位置、制造平台与系统维修模式的变化。

在 800G/1.6T 时代，光源仍在光模块里，EML 是核心。在 3.2T 时代，NPO 很可能成为 scale-up 与 scale-out 的主战场。到 6.4T 时代，CPO 的必要性明显提升，光源开始外置化。到 12.8T/OIO 时代，光源不再是模块内器件，而是系统级供光资源。

这条路线决定了光源行业的权力转移，EML 时代是 InP IDM 的天下；CW/ELS 时代，纯 CW 激光器 IDM、Fabless、III-V Foundry、衬底、隔离器、TEC、透镜与外置激光模块供应链都被重新打开。

CPO 不会消灭光源，反而会把光源从一颗器件升级为 AI 计算系统的基础设施。

LightCounting 在 2026 年 3 月 Ethernet Optics 报告中提出，在多个条件同时配合的情况下，AI cluster optical interconnect 年销售额到 2030 年有合理机会达到 1000 亿美元级别；这是把 AI cluster optics 作为一个大口径市场来看。

Yole 早期对狭义 CPO 的预测更保守，估算 CPO 市场从 2022 年约 3800 万美元增长到 2033 年约 26 亿美元，CAGR 约 46%。两者差异说明：只看 CPO module，市场不算夸张；若把 LPO、NPO、CPO、OIO、ELS、AI cluster optics 合并看，产业锚会大幅上移。

Lumentum、Coherent 对 2030 年 optical interconnect / datacom 可服务市场的表述均大幅上移，反映激光器、光源模块与光互连系统已经从传统光模块配套件，变成 AI 基础设施的关键瓶颈。

### **先看代际：100G、200G、400G 单通道如何推动架构迁移**

光通信产业每一代升级，最关键的不是总带宽，而是单通道速率。

总带宽可以靠增加路数堆出来，但单通道速率一旦翻倍，整个链路的压力会同时落到SerDes、DSP、Driver、TIA、光源、调制器、封装、散热、PCB/基板走线、前面板密度和可维修性上。

也就是说，100G/lane、200G/lane、400G/lane 不是单纯的数字，而是三个不同工程时代。

400G 是 4×100G，800G 是 8×100G，1.6T 进入 8×200G、约 106.25GBaud，3.2T 则进入 8×400G、约 224GBaud。

当单通道从 100G 到 200G，传统可插拔还能靠更先进 DSP、LPO、优化热设计继续撑住。当单通道进入 400G，传统前面板可插拔的功耗、散热、信号完整性与封装密度会同步逼近极限。

因此，要先搞明白EML、CW、VCSEL、MicroLED等光源技术演变，就必须先把 Pluggable、LPO、NPO、CPO、OIO 这条架构演化路线讲清楚。

光源技术不是孤立演进，而是被架构迁移推动。

## **800G：100G/lane，可插拔仍然舒适**

800G 的主流形态是 8×100G/lane。这一代光模块仍然以 OSFP、QSFP-DD 等可插拔形态为主，EML、硅光、VCSEL 都有应用，但在 AI 数据中心单模短距与中距场景里，EML 是最成熟的主流光源。

这一阶段的核心特征是：光源在模块内，调制器也在模块内，光模块厂采购EML、DSP、Driver/TIA、透镜、FAU、PCB、外壳，完成模块组装与测试。

光源产业链的核心价值在 EML IDM 手中，因为 EML 不是单一 DFB，而是 DFB + EAM 的 InP 单片集成器件。

800G 时代的可插拔逻辑仍然成立：模块热插拔、供应商可替换、维修半径小、数据中心集采模式成熟。光源位于模块内部并不构成系统性问题，因为单模块功耗与散热尚能在 OSFP/QSFP-DD 的热设计内被消化。

## **1.6T：200G/lane，可插拔仍是主流， LPO 开始延寿**

1.6T 主流是 8×200G/lane。1.6T 还没有让 CPO 成为主流，因为可插拔模块仍有维修性、部署弹性、供应链成熟度与标准化优势。

但压力开始明显增加，1.6T 可插拔模块功耗约 20–28W，其中 DSP/SerDes 占 10–14W，接近 50%。LPO 移除模块内完整 DSP 后，可把功耗压到约 12–15W。

所以1.6T 的本质不是 CPO 立刻取代可插拔，而是 Full DSP Pluggable → LPO Pluggable → NPO/CPO 预备导入。

LPO 的核心是把模块内 DSP/retimer 拿掉，只保留线性 Driver、TIA，让主机 ASIC/SerDes 承担更多均衡与补偿。这样做的好处是功耗与延迟降低，坏处是互通、校准、training、主机 SerDes 能力要求都更高。

在 1.6T 时代，EML 仍然是主流光源。Lumentum 在 OFC 2025 展示 448Gbps、224GBaud PAM4 EML，说明 EML 在单通道速率上仍有上探能力。同时 450G PAM4 DFB-MZI 的展示也说明 InP 平台并没有在 200G/lane 后失去价值。

真正的问题不是 EML 不能做，而是当系统走向 3.2T/6.4T，模块内分散发光与分散调制的架构是否仍是最经济的选择。

## **3.2T：NPO 的黄金窗口，而不是 CPO 一统天下**

3.2T 可能是争议最多的一代。很多文章会直接把 3.2T 说成 CPO 的开始，但更合理的判断是，3.2T 很可能是 NPO 的黄金窗口，市场会分化，而不是 CPO 一统天下甚至还不一定成为主流。

3.2T 对应 400G/lane。从物理压力看，CPO 的吸引力确实上升，因为前面板可插拔的走线、功耗、散热、面板密度都开始受压。

448G SerDes 下，3.2T 可插拔模块功耗可能进入 40–60W 区间，这已经高于 OSFP-XD 40W 上限，意味着单纯用传统前面板可插拔形态硬撑会越来越困难。

但从产业现实看，CPO 的封装、测试、良率、维修、标准化、供应链责任界面都还没有完全成熟。CPO 一旦把光引擎拉进 package 或 substrate，失效维修半径变大，供应链界面变复杂，客户集采模式也会被重构。这就给 NPO 留下非常重要的过渡窗口。

3.2T 可能形成两条大路线：第一条是 scale-up，用 VCSEL NPO 替代部分铜互连；第二条是 scale-out，用 CW/ELS + NPO。

前者利用 VCSEL 的低功耗、低成本、短距优势，面向 GPU 丛集内部；后者保留外置 CW 光源与硅光调制方向，但不一定立刻把光引擎完全推进 CPO 封装。

所以3.2T 不是「CPO 必然取代 NPO」，笔者认为更大的概率是「英伟达推 CPO，博通 + CSP 推 NPO」。英伟达有能力推 CPO，因为它掌握 GPU、NVLink、InfiniBand/Ethernet switch、系统设计与客户生态。

博通和 CSP 则更可能用 VCSEL NPO、CW NPO、高密度可插拔/XPO 等方式保留供应链弹性。

## **6.4T：CPO 开始变成主线**

到了 6.4T，问题已经不只是光源能不能做到 400G/lane，而是整个系统是否还值得维持 NPO 形态。

6.4T 如果用 16×400G 或更高密度通道，NPO 仍然可以工程化实现，但它的代价会明显上升，更多光引擎、更高电逃逸压力、更复杂的基板走线、更高散热负担、更难的校准和维修。

这时CPO 的系统级收益开始明显增加。

光引擎更靠近 ASIC，电走线更短，SerDes 功耗和信号损失更低，封装密度更高。

台积电 COUPE 路线也指向这一点：1.6T OE on substrate 是起点，6.4T OE on substrate 导入 CPO with switch，再往后进入 12.8T OE on interposer pathfinding。

从台积电的技术路线，我们可判断出6.4T是CPO 开始成为高端 scale-out、spine、switch fabric 的主线，但 NPO 仍会在部分 scale-up、可维修和成本敏感场景共存。

## **12.8T/OIO：光源成为系统级供光资源**

12.8T 以后，产业不应再把问题理解成更大号的光模块。它进入的是 CPO 到 OIO 的过渡，光 I/O 更靠近 ASIC、XPU，完全进入了interposer 或 CoWoS 类封装结构。

TSMC 的 3D optical interconnect 设计逻辑把光互连系统拆成 laser、fiber、waveguide、grating coupler、edge coupler、MRR、MRM、PD、MRM driver、TIA、thermal controller，再用 WDM 作为扩展轴。

这说明未来不是单一模块形态升级，而是光源、波导、调制、探测、驱动、热控全部进入系统级协同。

此时光源不再是模块内 EML，而是外置、集中、可替换、可监控、可冗余的 CW laser array / laser pool / ELS。光源从一个模块里的一颗器件变成整个计算系统的供光基础设施。

![](images/1c5a3ddb501fd2a93187.png)

## **EML、CW/ELS、VCSEL、MicroLED 的本质区别**
**
**
### ***EML：模块时代的最强光源***

EML 是 electro-absorption modulated laser，即电吸收调制激光器。它的本质是把 DFB 激光器和 EAM 电吸收调制器做在同一颗 InP 芯片上。

DFB 负责产生单模光，EAM 负责高速调制。这种结构的优点是高速、成熟、单模性能好、适合 FR/DR/LR 等单模链路，也适合 800G/1.6T 可插拔光模块。

DFB 的核心在于分布式布拉格光栅。普通 Fabry-Perot 激光器靠端面反射形成腔模，模式较多。DFB 透过周期性光栅在有源区附近提供波长选择，使激光器在指定波长单模工作。

对数据中心 1310nm O-band 或 1550nm C-band 场景，DFB 的波长稳定性、SMSR、线宽、RIN、温漂都会影响链路裕量。

EAM 的核心是 Franz-Keldysh 或量子限制 Stark 效应带来的吸收系数变化。当外加电场改变材料吸收边，EAM 对通过的光进行强度调制。

EAM 的优势是器件尺寸小、驱动电压低、调制速度高，适合与 DFB 在 InP 上单片集成。相比外置 MZM，EAM 可以把发光与调制做得更紧凑，但其 chirp、插入损耗、热稳定和高速眼图质量需要精细工程控制。

所以，EML 是 800G/1.6T 可插拔时代的最强光源，但它并不是 CPO/OIO 终局适合的方案。

EML最擅长的是模块级分布式发光与调制，而 CPO/OIO 要解决的是系统级集中供光与靠近 ASIC 的调制。

### ***CW/ELS：CPO/OIO 时代的系统级光源***

CW laser 是连续波激光器。它不负责高速调制，只输出稳定连续光。

ELS 是 external laser source，即外置光源模块，通常由多颗 CW DFB laser、laser array、隔离器、透镜、TEC、监控 PD、控制电路与光纤耦合结构组成。

CW/ELS 的产业意义是把 EML 中的 DFB 和 EAM 拆开，DFB/CW laser 留在光源端；EAM/MRM/MZM 调制功能搬到硅光 PIC 里。这不是简单的器件替代，而是光源与调制器位置的重新分工。

外置光源的最大工程价值是把温度敏感的激光器从高功率ASIC、GPU、switch package 周边移开。

激光器对温度非常敏感，温度会影响波长、输出功率、RIN、老化速度和模式稳定性。若把激光器放在 package 热源附近，波长控制与可靠性会很难。若用 ELS 外置供光，则可以用更独立的热管理、冗余、现场可替换 laser module 来提升整机可维修性。

Sivers、O-Net、Enablence 的 ELS 合作很有代表性，最近被频繁提及，Sivers 提供 DFB laser arrays，O-Net 作为 ODM 集成，Enablence 提供 NxN Star Coupler。

这说明 ELS 不再是一颗激光芯片，而是激光阵列、分光器、封装、热控和系统接口共同构成的小型供光系统。

### ***VCSEL：3.2T scale-up 替铜的最现实光源***

VCSEL 是垂直腔面发射激光器。它一般使用 GaAs 平台，而不是EML跟CW的InP。

光从晶圆表面垂直出射，而不是像边发射激光器那样从芯片侧面出光。这带来几个重要优势，晶圆级测试方便、阵列化容易、耦合到多模光纤成本低、阈值电流低、短距能效好。

从Broadcom 200G VCSEL展示的850nm VCSEL 在 106Gbd PAM4 下实现 200Gbps/lane 的路线，-3dB bandwidth 超过 35GHz，RIN 低于 -152dB/Hz，并在 50m OM4 光纤上展示无不可校正错误。

这些参数说明 VCSEL 不再只是 25G/50G SR 时代的低速方案，而可以在 200G/lane scale-up 中扮演重要角色。

VCSEL 的限制也很明确，它适合 <50m 的 scale-up，不适合 100m–2km 的 scale-out 主干。它适合多模短距，不适合长距单模。它可以打 3.2T 的黄金窗口，但 6.4T 再靠增加通道数硬堆会越来越痛苦。

因此，VCSEL 也不是 CPO/OIO 终局，但它很可能在 2026–2029 年左右成为 AI scale-up 从铜到光的部分过渡。

### ***MicroLED：短距激进方案，但不是主线***

MicroLED 方向是低速多通道、高并行、低功耗，理论上可以在短距 chip-to-chip 或 board-to-board 互连中提供低延迟方案。

它的逻辑与 400G/lane PAM4 不同：不是把每条 lane 推到极高速，而是用大量低速光通道并行传输，降低 DSP、FEC 和高速类比前端压力。

但 MicroLED 面临量产、耦合、生态、标准、可靠性等问题。MicroLED 制程涉及 III-V dry etching、侧壁损伤修复、ALD/CVD passivation、bonding、test & repair 等难点。

相比 VCSEL NPO 和 CW/ELS 硅光方案，MicroLED 更像短距光互连的一条激进分支，而不是 AI 数据中心光源主线。

![](images/16af550418a3dc0adeff.png)

 

## **EML是IDM 统治的时代**

进入光源产业链分析，第一个结论必须非常清楚，EML 时代不是所有光源公司都有机会，而是 InP IDM 统治。

原因很简单，EML 不是一颗 DFB 激光器，而是 DFB + EAM 的单片集成。DFB 和 EAM 都在 InP 平台上完成。

这要求企业同时具备 InP 外延、grating、DFB、EAM、芯片制程、端面处理、镀膜、测试、封装与可靠性能力。

纯 DFB 厂商没有 EAM，Fabless 没有 InP fab，III-V Foundry 没有客户侧完整可靠性数据，都很难在 EML 时代正面挑战 Lumentum、Coherent、Broadcom、Mitsubishi、Sumitomo、Source Photonics 这类 IDM。

EML器件与加工

EML器件与加工

![](images/225b80a6e262e91c5359.png)

# 

全球EML主导企业

![](images/378903e3cc80c4436301.png)

## 

## **EML 时代谁被排除，谁稳定受益**

EML 时代真正能吃到核心价值的是能够自己做 InP 外延、DFB、EAM、封装、可靠性测试的 IDM。这使得很多看起来与光源相关的公司，在 EML 时代反而不容易受益。

第一，纯 CW/DFB 厂商被压制。因为客户买的是 EML，不是裸 DFB。

纯 DFB 能力不足以满足 800G/1.6T 主流 EML 模块需求。这也是为什么很多只有 CW/DFB 能力的公司，在 EML 时代很难和 Lumentum、Coherent 正面竞争。

第二，Fabless 被压制。Fabless 可以设计激光器，但 EML 的量产可靠性高度依赖 InP fab、外延与制程。对大型 CSP 和模块厂而言，一旦出现失效，责任界面非常复杂。因此 EML 时代客户更愿意选成熟 IDM。

第三，III-V Foundry 被压制。全新、联亚、IQE、Smart Photonics、III-V Lab 这类公司有价值，但在 EML 时代，真正高端 AI EML 主供应链仍集中在 IDM。

Foundry 更容易在 CW/ELS 时代放量，因为 CW laser 的功能边界更清楚，不需要把 EAM 一起做到极致。

第四，稳定受益的是衬底与前段设备。InP 衬底、MOCVD、刻蚀、沉积设备在 EML 时代仍受益。因为不管谁做 EML，都需要 InP wafer、外延、加工与制程控制。

## **CW/ELS 时代供应链被重新打开**

CPO/NPO/OIO 不是不需要光源，而是不再需要每个模块内自带 EML。

在 EML 时代，光源公司要同时提供 DFB + EAM；在 CW/ELS 时代，调制器进入硅光 PIC，光源端只需要提供稳定 CW 光。

这一变化非常大。它意味着没有EAM 能力的纯 CW/DFB 厂商开始有机会。Fabless + III-V Foundry 模式开始有空间。InP 衬底、外延、MOCVD、刻蚀、沉积需求外溢。光隔离器、透镜、TEC、FAU、外置光源模块成为新价值环节。Lumentum、Coherent 仍然强，但不再是唯一能做光源的人。

在 CW/ELS 时代，光源端的核心指标会转向：输出功率、RIN、线宽、波长稳定性、SMSR、热漂移、寿命、冗余能力、可替换性、与硅光 PIC WDM 的匹配。这和 EML 时代强调 DFB+EAM 高速调制不同。

![](images/fcc22ee05e28903b19d4.png)

 

## **CW/ELS 时代的产业链分层：IDM、Fabless、Foundry、衬底、设备**
**
**
### **原 EML IDM仍然最强，但竞争不再完全封闭**

Lumentum、Coherent、Broadcom、Mitsubishi、Sumitomo、Source Photonics 在 CW/ELS 时代仍然非常强。原因是 CW laser 仍是 InP 激光器，仍然需要外延、DFB、封装、可靠性和客户认证。

原有 EML IDM 不会因为 EAM 被搬走而失去价值，只是价值形态从 EML chip 变成 CW laser / laser array / ELS module。

但竞争不再像 EML 时代那么封闭。因为 EAM 不在光源内，纯 CW/DFB 能力的公司也有机会。过去不能做完整 EML 的厂商，若能做出高功率、低 RIN、波长稳定、长寿命 CW laser，就可以进入 ELS 供应链。

![](images/c6c3d1049a09894d4536.png)

### **新 CW laser IDM：源杰、Sivers、台湾华星光通，长光华芯等的新窗口**

新 CW laser IDM 的机会来自一个核心变化：产业不再要求光源端必须提供 DFB+EAM 一体化 EML。只要能提供高可靠 CW laser，就能进入 CPO/NPO/OIO 的供光链。

源杰科技代表中国DFB/CW/EML 光芯片能力。Sivers Photonics 代表欧洲/英国 DFB laser array 与 ELS 生态。长光华芯代表高功率半导体激光器平台向通信光源延伸的可能性。华星光、QD Laser、Quintessent 等则代表台日美不同光源路线的潜在切入。

![](images/95191b3d1d0f0175a2b6.png)

### **Fabless设计型公司 CW/ELS 时代最需要补强的一层**

EML 时代，Fabless 最大的问题是没有 InP fab，无法对 DFB+EAM 的完整可靠性负责。

但 CW/ELS 时代，调制器搬到硅光平台，光源端只要输出稳定 CW 光，Fabless 可以设计 laser array、外置光源架构、controller、photonic interposer 或光 I/O 系统，再找 III-V Foundry 或 IDM 代工。

这里要区分「纯光源Fabless」和「光 I/O 系统 Fabless」。

前者直接设计激光器、DFB array、外置光源模块；后者更偏向 photonic interposer、optical I/O、chip-to-chip 光互连，需要外置激光器作为系统供光来源。CW/ELS 时代，两类公司都会推高外部光源需求。

![](images/d7ee107ebd34f3e9da96.png)

### **中国光源三小金刚与平台型公司**

中国光源相关企业不能一概而论。源杰科技、仕佳光子、长光华芯常被市场放在「三小金刚」框架中讨论，但三者能力完全不同，源杰更接近DFB/CW/EML 光芯片；仕佳更偏 PLC/AWG/DFB/光器件；长光华芯是高功率半导体激光器平台，向通信 CW 光源延伸仍需产品、客户和可靠性验证。

此外，光迅科技、华工科技/华工正源、中际旭创、新易盛、天孚通信、太辰光、博创科技等公司也会在不同环节受益，但不能全部归为「光源核心」。

有些是模块厂，有些是光器件，有些是连接/FAU，有些是平台型公司。文章需要把它们放回正确位置，避免把所有 CPO 概念公司都写成光源核心受益者。

再加上A推票断章取义风气盛行，目前把通信级别的光源技术或者相关器件，包装成未来CPO高端光源或器件的几乎在每一家公司的宣传上都出现，辨别材料跟器件，传统光通讯与目前EML或者未来CPO在不同器件上的技术区别，是投资A股光题材标的的重中之重。。

![](images/97cec85cdbc93dac4d3c.png)

## **
**

### **III-V Foundry / Epi：CW/ELS 时代的外溢受益者**

III-V Foundry / Epi 在 EML 时代不是最核心，因为高端 EML 多由 IDM 自己做。

但 CW/ELS 时代，Fabless、外置光源模块公司、硅光平台公司都可能需要外部 InP/GaAs 外延与代工能力，这会让全新、联亚、IQE、Smart Photonics、III-V Lab 等公司的重要性上升。

这里也要注意区分：GaAs foundry、InP foundry、Epi wafer supplier、完整 laser IDM 不是一回事。

稳懋、宏捷科更偏 GaAs/RF foundry，这块与硅光热点有区别，早期做RF的近两年市场低迷，都不约而同往光互联的题材上蹭或者说转型，卓胜微当初自建工厂正是为了射频业务，如今也在往光互联市场发展。

全新、联亚更接近外延与III-V供应；Smart Photonics、III-V Lab 更像 InP PIC foundry 生态。

![](images/6bc8c3523ae0cedf7cba.png)

 

### **衬底：InP/GaAs 的上游底座**

无论是EML、CW DFB、InP PIC，还是 VCSEL，都离不开三五族衬底。InP 主要对应 1310nm/1550nm 通信光源，GaAs 主要对应 VCSEL、部分 850nm/940nm/1060nm 应用以及射频/功率半导体。

衬底的核心指标包括晶圆尺寸、缺陷密度、掺杂均匀性、翘曲、表面粗糙度、热稳定性与批次一致性。高端通信激光器对缺陷和一致性要求高，因为微小材料缺陷可能导致外延缺陷、模式不稳定、可靠性下降。

![](images/b8a8debe8bce0bc3e3e5.png)

 

### **设备：三五族光源前段制程**

这文不讨论ficonTEC、光耦合设备、ATE、探针卡、封测设备，因为本文中心是光源本体，尤其是 InP/GaAs 的激光器制造。

设备部分只保留三五族前段制程：MOCVD、刻蚀、沉积、金属化、清洗/去损伤。

三五族光源前段制程的核心是材料和表面。其中： 

MOCVD 决定量子阱、波导、有源区质量；

刻蚀决定 DFB 光栅、脊波导、mesa、隔离槽的形貌和损伤；

沉积与 passivation 决定表面复合、漏电、可靠性；

金属化决定接触电阻、热阻与高速电性能。

这里要避免一个A 股常见误区，CPO 热度不等于所有后段自动化耦合设备都成为最核心环节。对光源本体而言，最底层的是三五族材料与前段制程，尤其是 MOCVD 外延、DFB 光栅与波导刻蚀、表面 passivation、电极金属化与可靠性控制。

其中MOCVD是三五族特有关键设备。这也是前两年我在推荐国产设备股的时候一直是把中微放在首位的加分項，前两年就能看到未来三五族MOCVD因为光互联的繁荣，不过中微的重点是放在LED，需要有所侧重转向。

![](images/76177ae9f07a3c305f2f.png)

 

## **ELS 不是一颗激光器，而是一个完整光源系统**

很多分析把 CW/ELS 简化成只要 DFB，这不完整。真正的 ELS 是一个小型光源系统。

它至少包括 InP substrate、epitaxy、DFB laser die、laser array、wavelength locker、monitor PD、isolator、Faraday rotator、lens/collimator、TEC、thermistor、hermetic package、fiber pigtail、FAU、control board/driver。

ELS的难点不是单颗 DFB 亮起来，而是多颗激光器功率一致、波长稳定、RIN 低、热漂小、反射可控、寿命长、可替换、可监控，并能与硅光 PIC 的 WDM/调制器精准匹配。

在 CPO/OIO 架构下，激光器通常不应放在最热的 ASIC/package 周边，因为温度会影响波长与可靠性。

ELS 将 laser source 外置，可透过独立散热和冗余设计提升 serviceability，也让 laser module 成为可以现场替换的系统部件。ELS大大地改善了CPO的可维护性，可维护性一直是CPO被行业诟病的核心。

CW/ELS供应链全景

![](images/e5141efcf52c7974302e.png)

 

### **不能把 TGG/TSAG 和通信级隔离器混为一谈**

光隔离器在 ELS 中非常关键。外置激光器最怕反射光回灌，反射会造成模式跳变、RIN 上升、波长漂移、相位噪声甚至激光器失效。光隔离器的功能就是让光单向通过，阻止反射光回到激光腔。

典型隔离器由 input polarizer、Faraday rotator、output polarizer、magnet、lens/collimator、封装结构组成。

Faraday rotator 在磁场下旋转偏振方向，配合偏振器实现单向通光。

这里要特别科普，TGG/TSAG 不等于通信级高端隔离器。TGG、TSAG 常见于高功率工业激光与部分近红外应用，但通信级 1310/1550nm 小型化隔离器更重视插损、隔离度、回损、温漂、偏振一致性、小尺寸、薄片加工与封装匹配。

GRANOPT、Sumitomo 这类日系磁光材料与隔离器供应商的优势，不只是有晶体，而是它们在通信波段、小型化薄片、低插损、高隔离与长期可靠性上的制程积累。

福晶科技有磁光晶体能力，但不能简单等同于 Coherent、Sumitomo、GRANOPT 的通信级隔离器供应地位。

若要进入 CPO/ELS 供应链，核心不是能做或有TGG/TSAG产品线，而是能否做到通信级小型化、低插损、高隔离、高一致性与长期可靠性。

简单说传统的工业脉冲激光、科研、高功率固态激光（1064nm 为主）的法拉第炫光片与EML/CW/ELS的1310nm与1550nm波长的光隔离器材料相同但制作工艺上是两码事。做材料跟做成品元器件是两码事。

![](images/f4ccb950be73fde88073.png)

 

### 

### **EML 时代 vs CW/ELS 时代：产业链重构表**

![](images/942297a53877be3d259b.png)

 

**让我们再复习一下未来光互联形式的方案演变****
**
### **3.2T 为什么是 NPO 的黄金窗口**

3.2T 时代，光模块厂不会愿意立刻把主导权交给 Foundry 和 CPO 封装平台。因为 NPO 还保留了模块厂的制造角色，也保留了 CSP 喜欢的可维修性、多供应商和部署弹性。

Scale-up 方向，VCSEL NPO 的优势是低功耗、低成本、短距足够、可靠性好。200G/lane VCSEL 可支撑 3.2T scale-up，能效可接近 1pJ/bit，对比铜缆在更长距离、更大机柜域中的损耗与布线压力，VCSEL NPO 是非常务实的替铜方案。

Scale-out 方向，CW/ELS NPO 则可以把光源外置，把调制放在硅光光引擎，但不一定立刻做完整 CPO。这样既能降低一部分功耗，又保留一定可维修性和供应链开放度。对博通与 CSP 而言，这比高度封闭的 CPO 更符合多供应商采购与白盒生态逻辑。

因此，3.2T 不会是一条路线吃掉所有市场，而是分化：英伟达偏 CPO，博通偏 NPO+CPO 双轨，CSP 更偏 NPO/XPO/CPX，模块厂强推 NPO/XPO，Foundry 则更希望 CPO/OIO 把价值推向 PIC/EIC/封装平台。

![](images/796472b619784cd6d418.png)

### **6.4T CPO 的主场**

到了 6.4T，NPO 的优势开始下降。原因不是 VCSEL、CW 或 EML 不能继续进步，而是系统层面的代价变高。通道数增加，光引擎数量增加，电逃逸距离与损耗难以控制，基板与连接器设计更复杂，热管理压力上升，校准与测试成本上升，维修半径变大。

所以6.4T 的光源形态大概率是外置 ELS + 硅光 PIC + CPO 光引擎。这里光源行业不是被消灭，而是变成外置供光模块。模块厂如果仍停留在传统可插拔装配，就会被削弱；但如果能切入 ELS、FAU、光纤连接、激光器封装、测试，仍然有位置。

CPO 的真正价值不是「把模块塞进封装」，而是把高功耗、高损耗、高延迟的电逃逸缩短，把光调制放在更接近 ASIC 的位置。此时光源端最好的工程选择不是把激光器也放在热源旁，而是外置化、冗余化和可维修化。

### **12.8T/OIO：光源的终局是 laser pool**

12.8T 和 OIO 时代，光源会进一步系统化。这时不应再说某颗 EML 多少 G，而要说整个系统如何分配光功率、波长、冗余、热控与维修。

未来的光源可能是多通道ELS、laser pool、remote laser source、可替换 laser cartridge，并与 CPO/OIO 光引擎标准化接口连接。

OIO 的核心不是把激光器放到 interposer 上，而是把调制与探测更靠近计算芯片，光源可以外置，避免热源与可靠性问题。

这个阶段的竞争不只是器件公司之间的竞争，而是系统厂、Foundry、InP 激光 IDM、Fabless 光 I/O 公司、外置光源模块厂之间的架构竞争。

谁能把稳定、低噪声、高功率、可维护的光送到最靠近计算芯片的地方，谁就掌握未来光互连的入口。

### **全球光源相关企业总表**

![](images/4b5800ebf558a852901b.png)

## **2025–2030+ 光互连与光源技术时间轴**

这张表是整篇文章的总结性图谱。它不是精准预测每家公司产品节奏，而是把 PO 形态、光源形式、单通道速率、路数、调制器材料与产业主线放在同一张时间轴里。

核心要点是：2025–2027 年是 EML IDM 收获期；2028 年前后是 NPO 黄金窗口；2029–2030 年后 CPO/OIO 把光源从模块内器件重构为系统级供光资源。

![](images/326fff36d1a6dc6e8a52.png)

## **结论 CPO 不消灭光源，而是重分配光源价值**

这篇文章最后要落在一个清楚的判断：2025–2027 年，是 EML IDM 的收获期；2028 年前后，是 NPO 的黄金窗口；2029–2030 年后，CPO/OIO 把光源从模块内器件重构为系统级供光资源。

所以，光源产业不是被 CPO 消灭，而是被 CPO 和 OIO 重构。EML 时代，价值在 DFB + EAM 一体化，只有 InP IDM 能吃大头。CW/ELS 时代，EAM 被搬到硅光平台，光源端回到 CW DFB laser，纯 CW laser IDM、Fabless、III-V Foundry、衬底、隔离器、TEC、透镜、FAU 全部被重新放进产业链。

3.2T 是这场变局的分水岭，但它不是 CPO 一统天下的时刻。更大概率是：英伟达推 CPO，博通与 CSP 推 VCSEL/CW NPO，模块厂用 XPO、NPO 延长自己的生命周期。真正到 6.4T、12.8T/OIO，光源才会从模块内分布式 EML，全面转向外置、集中、可维护、可监控的 CW/ELS。

一句话总结：800G/1.6T 看 EML IDM；3.2T 看 NPO 分化；6.4T 看 CPO 成熟；12.8T/OIO 看 laser pool。光源不是消失，而是从一颗器件，变成 AI 计算系统的基础设施。

### 本文感想：

最近一直在学习光互联产业，了解越深越觉得自己知识的渺小，本文早在十天之前就写好初稿，但与许多光通信专家与做了十多年硅光的老朋友讨论之后，发现目前光互联技术路线处于战国时期。

各种技术路线都认为自己的方向正确，欧美台的产业链跟国内的观点不太一样，国内依托光模块产业链大家都是奋力的阻挡CPO的产业链迁移，问到CPO总是有一千个理由，CPO有总总困难没那么快。

可与欧美或台系的产业内朋友聊却是另一番光景，整个行业都在摩拳擦掌迎接CPO的到来。

最终经过与许多业内朋友的讨论，汇整这一份资料，内容并非完全依照专家的意见，因为有的观点完全不同，甚至是对立的，我只能自己根据自己的产业经验与主流企业的技术方向自行延伸并做出判断。

笔者综合下来，6.4T也就是2029/2030年左右会是一个真正的分水岭，NPO即便延寿再成功也阻挡不了CPO成为主流，光模块厂失去新增量，但这是好几年以后的叙事，在二级市场上不用过份放大影响。

3.2T的VCSEL NPO增加了scale up这个全新增量，让我在现阶段看好光模块厂，因为2029/2030年的6.4T还早，明年跟后年的3.2T还是光模块主导的NPO，且还增加了以前没有的scale up，我认为2026年只要光模块厂有下跌都是可以入手的好机会，因为未来两年的业绩都是大好。

本文因为是写给普通网友与投资者看的，文章的论点并非很严谨，更多是本人自己衡量后依照经验做出的推演与判断。可能会有不同立场的专家有不同意见。

其实咱们星球内的有lumentun，cohernet以及三五族fab的许多从业者与朋友，这些老朋友有自己看法的也欢迎能提出，不吝赐教，大家可以试着讨论出未来最可能的方向，感谢各位。

        
                
                

![](/assets_dweb/logo@1x.png)

                知识星球
                
        
        
            
            扫码加入星球
            查看更多优质内容
        
        https://wx.zsxq.com/mweb/views/joingroup/join_group.html?group_id=88888812815442

---

Source: https://articles.zsxq.com/id_96l5sshf356q.html

Linked from topic_id: 55522114522281444
