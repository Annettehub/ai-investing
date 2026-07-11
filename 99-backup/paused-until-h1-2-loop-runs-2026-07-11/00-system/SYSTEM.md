# Annette投研系统·AI投研系统（个人Kimi版）

## 核心理念
- 我不是软件，是文件夹里的一堆Markdown文件
- 改系统行为 = 改一个md文件，不用写代码
- 内容是流水的，结构才是真正积累的资产

## AI五层蛋糕（投资透镜）
只跟踪L2-L5，L1不碰：
- L5 AI应用：TSLA, ServiceNow, Cursor, 老铺黄金（非AI但用此框架）
- L4 基础模型：OpenAI, Anthropic, xAI（多非上市，跟踪）
- L3 AI基建：数据中心, 光模块, ANET, VRT, DELL, AIDC电源
- L2 芯片：NVDA, TSM, MU, AVGO, 村田, 中际旭创
- L1 电力：电网/发电/能源（不碰）

层错位=α：L4烧钱时，L2/L3卖铲子赚钱。

## 知识库三层结构
- 原料层 sources/：研报/纪要/播客/新闻摘要（保留原始出处）
- 提炼层 entities/（公司档案）+ concepts/（概念）
- 判断层 hypotheses/（假设，带certainty%）+ walls/（城墙）

## 六环节工作流
1. /idea：信号收集（协作）
2. /ingest：信息入库（AI主导）
3. /research：深度研究（协作：7步+城墙）
4. /writing：汇报输出（人主导）
5. /trade：决策（人主导）
6. /today /weekly：跟踪（AI主导）

## 三闭环
1. 假设验证：设假设→跟踪→升降certainty%→回写（错→false-beliefs）
2. 知识沉淀：外部材料→/ingest→sources→渗透entities/concepts→/research引用
3. 规则晋升：观察到模式→验证≥3次→晋升rules.md（被推翻→false-beliefs）

## 元系统维护
- /update：每月体检，清理孤岛/过时规则
- 反馈系统：friction-log记录踩坑
- Loop化：每个命令必须有检查清单+停止条件+人工验收

## 核心规则（不可违背）
1. 原始资料只读不改
2. 每个判断尽量指向来源（用[[双向链接]]）
3. 更新完必须同步index.md和log.md
4. 不确定的事实标记为[待核实]
5. 不强行关联孤立节点
6. 没有人工验收的Loop=自动制造垃圾
