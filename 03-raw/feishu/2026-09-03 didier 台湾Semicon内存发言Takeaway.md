2026-09-03 didier 台湾Semicon内存发言Takeaway

部分内容由豆包生成
作者：didier
发布：2026-09-02 18:58
来源：知识星球

豆包要点总结
1. AI对内存需求很强但不会雨露均沾：未来两年最赚钱的仍是HBM和先进封装；NAND有机会但不能吹得太早；普通DRAM到2028年仍有明显过剩风险
2. HBM逻辑继续成立：训练/推理热权重、active KV和activation短期仍离不开HBM；HBF、CXL、SSD主要走温数据和冷数据，暂时替代不了HBM核心位置；Sandisk讲HBF、Samsung讲zNAND-O不构成SK hynix近期利空
3. HBM不会永远赢：Google正在压缩KV、提高服务器利用率、回收旧内存；GQA、MLA、量化和prefix cache都在减少每Token的HBM需求；2027年景气判断增强，但2028年周期风险未消除
4. NAND有故事但先别把期权当利润：当前真正赚钱的AI NAND需求是训练数据、数据湖、checkpoint、模型加载、RAG数据库和高容量企业SSD；KV cache下沉、persistent context和HBF属于下一阶段；Sandisk 2027年才推出首批HBF推理设备样品
5. 最确定的卖铲子机会在封装和工艺设备：无论HBM、3D DRAM、HBF还是zNAND-O，都需要混合键合、晶圆键合、TSV、薄化、overlay检测、缺陷检测、先进封装和散热；2028年普通DRAM过剩、HBM供需接近平衡甚至局部仍紧、AI企业SSD开始增长
开头总结

AI对内存需求很强，但不会雨露均沾
AI对内存的需求确实很强，但不会雨露均沾。未来两年最赚钱的仍是HBM和先进封装；NAND有机会，但不能吹得太早；普通DRAM到了2028年仍有明显过剩风险。
具体拆开看
一、对HBM：逻辑继续成立

训练推理热数据短期仍离不开HBM
训练、推理中的热权重、active KV和activation，短期仍离不开HBM。HBF、CXL、SSD主要走温数据和冷数据，暂时替代不了HBM的核心位置。
所以，Sandisk讲HBF、Samsung讲zNAND-O，并不构成SK hynix的近期利空。它们更像给GPU增加一个容量层，让昂贵HBM只保存最热的数据。

SK hynix 2026-2027核心逻辑得到加强
对SK hynix而言，2026—2027年的核心逻辑得到加强：HBM需求、单芯片容量、堆叠层数和定制化程度都在上升。ASIC扩大HBM采用，也在降低对英伟达单一平台的依赖。
二、但HBM不会永远赢

软件效率正在减少每Token的HBM需求
Google正在压缩KV、提高服务器利用率、回收旧内存；GQA、MLA、量化和prefix cache都在减少每Token的HBM需求。
因此要同时看两个数字：
总Token需求增长多少；
每Token所需内存下降多少。

2027年景气增强，但2028年周期风险未消除
只要Token、Agent和并发增长更快，HBM总需求继续上升。到了2028年，如果软件效率提高、HBM产能释放，同时AI需求第二曲线没有出现，HBM价格和利润率仍可能明显回落。
这批材料增强了2027年的景气判断，没有消除2028年的周期风险。
三、对NAND：有故事，但先别把期权当利润

当前真正赚钱的AI NAND需求
当前真正赚钱的AI NAND需求主要是：
训练数据、数据湖、checkpoint、模型加载、RAG数据库和高容量企业SSD。
KV cache下沉、persistent context和HBF属于下一阶段。只有上下文能够反复复用，且SSD读取速度快于重新计算，NAND才真正创造价值。
每个Token都要更新的output KV、activation，现阶段仍不适合NAND。Sandisk计划2027年才推出首批HBF推理设备样品，Samsung的zNAND-O目标更晚。

更值得关注高端eSSD、控制器、固件和缓存调度能力
所以不能因为AI数据爆炸就直接重仓所有NAND厂。更值得关注的是高端eSSD、控制器、固件和缓存调度能力。
Sandisk、Phison的AI故事可以给估值期权，但暂时不应进入核心盈利预测。
四、最确定的卖铲子机会在封装和工艺设备

无论哪种内存胜出，都需要封装和工艺设备
无论最后赢家是HBM、3D DRAM、HBF还是zNAND-O，都需要：
混合键合、晶圆键合、TSV、薄化、overlay检测、缺陷检测、先进封装和散热。
这些环节不需要提前猜中哪种新型内存最终胜出。只要内存继续向3D堆叠发展，工艺难度、设备价值量和检测强度都会上升。

先进封装、键合、量测检测和热管理比押注新型存储更稳
因此，从产业确定性看，先进封装、键合、量测检测和热管理，可能比押注某一种尚未量产的新型存储更稳。
五、对2028年：会出现结构性分化

CXMT扩产首先打击普通DDR和部分LPDDR
CXMT扩产首先打击普通DDR和部分LPDDR。普通DRAM价格可能下跌，三星、SK hynix、美光的传统DRAM利润都会受压。
但HBM仍受堆叠、封装、散热、良率和客户认证限制，供给不会随着DRAM晶圆同步增加。

2028年可能出现的结构性分化
所以2028年可能出现：
普通DRAM过剩；
HBM供需接近平衡甚至局部仍紧；
AI企业SSD开始增长；
HBF仍处于客户验证和初期放量。
不能再用一个全球DRAM产能判断三家公司的利润，要分别计算传统DRAM、HBM和NAND的收入占比及毛利。
一句话落到投资上

2026-2027继续围绕SK hynix/HBM、先进封装和高端eSSD布局
2026-2027年继续围绕SK hynix/HBM、先进封装和高端eSSD布局；HBF与AI NAND只给期权价值；普通DRAM和CXMT扩产风险留到2028年重点防守。真正需要警惕的拐点，是HBM有效供给增速超过Token需求增长减去软件效率提升之后的净需求增速。
