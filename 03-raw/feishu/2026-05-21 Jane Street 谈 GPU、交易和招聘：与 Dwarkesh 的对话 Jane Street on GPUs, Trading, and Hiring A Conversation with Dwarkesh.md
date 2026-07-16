2026-05-21 Jane Street 谈 GPU、交易和招聘：与 Dwarkesh 的对话 Jane Street on GPUs, Trading, and Hiring A Conversation with Dwarkesh
Info
Podcast: Jane Street
Episode: Jane Street on GPUs, Trading, and Hiring: A Conversation with Dwarkesh
Link: https://app.podwise.ai/dashboard/episodes/8066837
Publish Time: 2026-05-21
Save Time: 2026-05-30
Summary
Trading firms like Jane Street operate across multiple time horizons, requiring a sophisticated ensemble of strategies ranging from nanosecond-level FPGA-based execution to longer-term model-driven decisions. High-performance trading demands specialized infrastructure, where physical constraints like power, cooling, and network latency dictate the placement of compute resources. While large-scale AI models offer significant potential for innovation, financial data remains inherently noisy, necessitating smaller, specialized models rather than monolithic foundation models. Scaling this compute requires complex logistical planning, including managing long-lead items like generators and optimizing fleet-wide performance. Despite the rise of automation, human judgment remains critical for navigating market phase transitions and managing unforeseen events. Consequently, the firm prioritizes hiring diverse technical talent to solve complex engineering and research challenges, viewing human cognition as a vital component of competitive advantage in an increasingly automated landscape.
交易公司如 Jane Street 在多个时间范围内运作，需要从纳秒级 FPGA 执行到长期模型驱动决策的复杂策略组合。高性能交易需要专业基础设施，在此基础上，电力、冷却和网络延迟等物理限制决定了计算资源的放置。尽管大规模 AI 模型提供了显著的创新潜力，但金融数据本质上仍然是嘈杂的，这使得更小的专业模型成为必需，而非单一的大型基础模型。扩展这些计算需要复杂的后勤规划，包括管理发电机等长期物品，并优化整个车队的性能。尽管自动化的兴起，人类判断在市场阶段转变和管理不可预见事件方面仍然至关重要。因此，公司优先招聘多样化的技术人才，以解决复杂的工程和研究挑战，将人类认知视为在日益自动化的环境中获得竞争优势的关键组成部分。
Takeaways
Trading strategies utilize an ensemble approach that balances speed and complexity, ranging from sub-100 nanosecond FPGA-based execution for simple decisions to longer-horizon model-based processes for complex valuation.
交易策略采用一种集成的方法，平衡速度和复杂性，从低于 100 纳秒的基于 FPGA 的简单决策执行到用于复杂估值的长期模型基础过程。
Financial trading functions as an AGI-complete problem, as it requires synthesizing diverse, noisy, and constantly evolving global data to predict future value, rendering total automation elusive.
金融交易作为一个 AGI 完全问题，因为它需要合成多样、嘈杂且不断演变的全球数据来预测未来价值，使得完全自动化变得难以实现。
Scaling AI compute in trading is increasingly constrained by physical infrastructure limitations, such as power density, cooling requirements, and the long lead times for critical components like generators, rather than just chip availability.
在交易中，AI 计算的扩展越来越受到物理基础设施限制的约束，例如功率密度、冷却要求以及像发电机这样的关键组件的较长交付时间，而不仅仅是芯片的可用性。
Human judgment remains a vital component of trading, particularly during market "phase transitions" or anomalous events where historical data fails to guide automated systems.
人类判断在交易中仍然是一个重要组成部分，特别是在市场 “相变” 或历史数据无法指导自动化系统的异常事件期间。
Financial models require specialized architectures rather than monolithic foundation models because financial data is significantly noisier and requires a higher bytes-to-flop ratio for effective inference.
金融模型需要专门的架构，而不是单体基础模型，因为金融数据显著嘈杂，并且在有效推理时需要更高的字节与浮点运算比。
The primary constraint on organizational growth is the capacity to mentor and integrate new talent into the firm's culture, rather than the ability to procure or deploy hardware.
组织增长的主要约束是指导和整合新人才进入公司文化的能力，而不是获取或部署硬件的能力。
The transition from a centralized, x86-only compute environment to a disaggregated, multi-architecture infrastructure is essential to overcome the physical power and cooling limits of modern data centers.
从集中化、仅限 x86 的计算环境过渡到分散的多架构基础设施对于克服现代数据中心的物理功率和冷却限制是至关重要的。
Q & A
Q: How do you balance the need for extreme speed—down to the nanosecond—with the desire to run complex AI models?
Q: 你如何平衡对极端速度（精确到纳秒）的需求与运行复杂 AI 模型的愿望？
A: We don't rely on a single time horizon; instead, we use an ensemble approach. For trades requiring sub-100 nanosecond turnaround, we use FPGAs directly wired to the network because CPUs are simply too slow. As the time horizon expands to microseconds or milliseconds, we can utilize more complex models on CPUs or GPUs. The key is to match the complexity of the decision-making process to the specific time budget available. You cannot perform heavy computation at the lowest latency levels, so we optimize for different regimes simultaneously.
A: 我们不依赖单一的时间视角；相反，我们采用集成方法。对于需要低于 100 纳秒周转的交易，我们直接使用与网络连接的 FPGA，因为 CPU 实在太慢。当时间视角扩展到微秒或毫秒时，我们可以在 CPU 或 GPU 上利用更复杂的模型。关键是将决策过程的复杂性与可用的特定时间预算相匹配。在最低延迟水平下无法进行重计算，因此我们同时优化不同的模式。

Q: Why is the naive view that AGI will eventually automate away trading firms incorrect?
Q: 为什么认为 AGI 最终会自动化交易公司的天真看法是错误的？
A: I view trading as "AGI-complete" or "NP-complete" because every piece of information in the world can potentially influence a trade. The business is far more diverse than people realize, involving many non-electronic, human-intermediated processes. While we automate many tasks, human judgment remains critical, especially during market anomalies or "phase transitions" where models may struggle. We aren't close to a world where AI is strictly smarter than humans at all cognitive tasks, and even if we were, the competitive edge lies in the hard parts of the business that we don't yet know how to automate.
A: 我将交易视为 “AGI 完全” 或 “NP 完全”，因为世界上每一条信息都可能影响一笔交易。这个行业远比人们意识到的要多样化，涉及许多非电子和人力中介的过程。尽管我们自动化了许多任务，但人类判断仍然至关重要，尤其是在市场异常或 “相变” 期间，此时模型可能会面临困难。我们还远未接近一个 AI 在所有认知任务上严格比人类聪明的世界，即使我们接近这样的世界，竞争优势也在于我们尚不知道如何自动化的行业中那些困难的部分。

Q: What are the current bottlenecks in scaling AI compute, and how do you manage them?
Q: 目前在扩展 AI 计算方面存在哪些瓶颈，你如何管理这些瓶颈？
A: The bottlenecks shift constantly. Currently, we face significant lead times for components like generators, transformers, and liquid cooling equipment. We manage this by warehousing fungible components and working closely with internal procurement teams. We are also adopting a "long power" strategy—securing data center space and power capacity well in advance, even if we delay the purchase of the expensive chips themselves. We are also increasingly turning to modular data centers, where infrastructure is pre-built offsite to allow for near plug-and-play deployment.
A: 瓶颈不断变化。目前，我们面临组件（如发电机、变压器和液体冷却设备）显著的交货时间延迟。我们通过储存可替代组件并与内部采购团队紧密合作来管理这一点。我们还采用了一种 “长电力” 策略——提前确保数据中心空间和电力容量，即使我们延迟购买昂贵的芯片。我们还越来越多地转向模块化数据中心，基础设施在现场外预先构建，以实现近乎即插即用的部署。

Q: Why does Jane Street prioritize a diverse set of specialized models rather than one large, general-purpose foundation model?
Q: 为什么 Jane Street 优先考虑多样化的专用模型而不是一个大型通用基础模型？
A: Our models must be adapted to consume specific data sources with unique data rates. Financial data is extremely noisy, which means our models tend to be smaller but trained on much larger, noisier datasets compared to traditional LLMs. Because our "bytes to flop" ratio differs for every application, we gain significant value by experimenting with diverse model architectures. We need to customize everything from data loading to inference throughput to fit the specific dynamics of different markets.
A: 我们的模型必须适应特定数据源并具备独特的数据传输速率。金融数据非常嘈杂，这意味着我们的模型往往较小，但训练在的更大、更嘈杂的数据集上相比于传统的 LLM。由于我们的 “字节与浮点运算” 的比例因每个应用而异，我们通过实验多样化的模型架构获得显著的价值。我们需要从数据加载到推理吞吐量定制所有内容，以配合不同市场的特定动态。

Q: How does the massive increase in compute needs affect your hiring strategy?
Q: 计算需求的大幅增加如何影响你的招聘策略？
A: We don't view compute as a limiting factor that restricts hiring; rather, the high value of our research justifies the investment in more compute. We are scaling from tens of thousands to hundreds of thousands of GPUs. The real bottleneck is finding great people and having the mentorship capacity to integrate them into our culture. We are hiring across the board—from mechanical and electrical engineers for our physical infrastructure to software engineers and ML researchers. We are also specifically looking for people with experience in fleet-wide optimization and formal methods, as our scale now requires a level of engineering rigor similar to the hyperscalers.
A: 我们并不认为计算是限制招聘的因素；相反，我们研究的高价值证明了对更多计算的投资是合理的。我们的 GPU 数量正在从数万扩展到数十万。真正的瓶颈是寻找优秀人才并具备将他们融入我们文化的指导能力。我们正在全面招聘——从机械和电气工程师到软件工程师和机器学习研究员。我们还特别寻找具有整个车队优化和形式方法经验的人，因为我们现在的规模需要与超大规模公司相似的工程严谨性。

Q: How much do humans stay in the loop when most of your trading is automated?
Q: 在你们大部分交易都是自动化的情况下，人类在其中保持多大程度的参与？
A: We always have people watching the systems. Even if individual transactions happen too fast for human intervention, humans provide essential meta-judgment. During market anomalies or "weird" events where the world goes crazy, models can struggle, and human intuition about how today differs from historical data becomes a competitive advantage. We prioritize building tools that increase human understanding, agency, and efficiency rather than just replacing the human element.
A: 我们始终有工作人员监控系统。即使个别交易发生得太快以至于无法进行人工干预，人类也提供了至关重要的元判断。在市场异常或 “奇怪” 事件中，世界变得疯狂时，模型可能会挣扎，人类对今天如何与历史数据不同的直觉成为了一种竞争优势。我们优先构建能够增加人类理解、主动性和效率的工具，而不仅仅是替代人类元素。

Q: How has the shift to high-density compute, such as GPUs, changed your approach to physical data center engineering?
Q: 向高密度计算（如 GPU）的转变如何改变了你对物理数据中心工程的看法？
A: It has forced us to rethink everything from power delivery to cooling. With racks reaching one megawatt, the physical infrastructure—the pipes for cooling and the power distribution—becomes a massive engineering challenge. We are moving away from traditional, slower data center design practices. For example, we might forgo backup generators for non-critical systems if it allows us to get our GPUs online six months faster. It’s about making the best business decision, which often means challenging the status quo of how data centers have been built for the last 20 years.
A: 这迫使我们重新思考从供电到冷却的所有内容。随着机架达到一兆瓦，物理基础设施——冷却管道和电力分配——成为一个巨大的工程挑战。我们正在逐渐远离传统的、较慢的数据中心设计实践。例如，如果能让我们的 GPU 提前六个月上线，我们可能会放弃非关键系统的备用发电机。这关乎做出最佳商业决策，通常意味着挑战过去 20 年来数据中心建设的现状。
Keywords


Keywords

Explanation

FPGA

Stands for Field Programmable Gate Array, a type of hardware that can be configured to perform specific, high-speed tasks. In the context of trading, it is used to process data directly from the network with extremely low latency, often faster than a standard computer processor.

FPGA

代表现场可编程门阵列，是一种可以配置以执行特定高速任务的硬件。在交易的上下文中，它用于以极低的延迟直接处理来自网络的数据，通常快于标准计算机处理器。

OCaml

A functional programming language known for its strong type system and performance. It is used by the firm to build complex, reliable trading systems that require both speed and correctness.

OCaml

一种以其强类型系统和性能而闻名的函数式编程语言。该公司使用它来构建需要速度和正确性的复杂可靠交易系统。

Colocation

The practice of placing servers in the same physical facility as a financial exchange. This minimizes the physical distance data must travel, allowing traders to execute orders with minimal time delay.

Colocation

将服务器放置在与金融交易所相同物理设施中的做法。这最小化了数据必须传输的物理距离，使交易者能够以最小的时间延迟执行订单。

Latency

The time delay between an action, such as a market event, and the response, such as a trade execution. In high-frequency trading, reducing this delay to nanoseconds is a critical competitive advantage.

Latency

市场事件等行为与交易执行等响应之间的时间延迟。在高频交易中，将这种延迟减少到纳秒是一个关键的竞争优势。

Scaling Laws

Mathematical relationships that describe how the performance of an AI model improves as you increase the amount of computing power and data used to train it. These laws help researchers predict the resources needed to build more capable models.

Scaling Laws

描述随着计算能力和用于训练的数据信息量增加，人工智能模型的性能如何改善的数学关系。这些规律帮助研究人员预测构建更强大模型所需的资源。

Adverse Selection

A risk in trading where one party has more information than the other, often leading to unfavorable outcomes for the less-informed party. Managing this risk is a core challenge when providing liquidity in financial markets.

Adverse Selection

交易中的一种风险，其中一方掌握的信息较多，这往往导致对信息较少的一方产生不利结果。管理这种风险是提供金融市场流动性时的核心挑战。

Formal Methods

A rigorous approach to software engineering that uses mathematical proofs to verify that a system will behave exactly as intended. It is used to ensure high reliability in critical software applications.

Formal Methods

一种严格的软件工程方法，使用数学证明来验证系统将按预期行为运行。这用于确保关键软件应用程序的高可靠性。

Liquid Cooling

A method of removing heat from high-density computer servers by circulating liquid rather than air. This is becoming essential as modern hardware, such as powerful GPUs, generates more heat than traditional cooling systems can handle.

Liquid Cooling

一种通过循环液体而非空气从高密度计算机服务器中移除热量的方法。随着现代硬件（如强大的 GPU）产生的热量超过传统冷却系统的承受能力，这变得越来越重要。

ASIC

Stands for Application-Specific Integrated Circuit, a custom-designed chip built to perform a single, specific task very efficiently. These chips are often used in high-performance computing when general-purpose hardware is not fast enough.

ASIC

代表应用特定集成电路，是一种为高效执行单一特定任务而设计的定制芯片。这些芯片通常用于高性能计算，当通用硬件的速度不足时。

LLM

Stands for Large Language Model, a type of artificial intelligence trained on massive amounts of text to understand and generate human-like language. These models are increasingly used for a variety of cognitive tasks beyond simple chatbots.

LLM

代表大型语言模型， 一种在大量文本上训练的人工智能，用于理解和生成类似人类的语言。这些模型越来越多地用于超越简单聊天机器人的各种认知任务。
Highlights
(10:43) Trading feels to me as AGI-complete, meaning that all of the different problems of the world end up influencing what you're doing in a trading context.
对我来说，交易感觉是 AGI 完整的，这意味着世界上不同的问题最终会影响你在交易环境中的行为。
(13:49) We want to build models that work well through phase transitions, but humans work better than models through phase transitions.
我们希望构建在相位转换中表现良好的模型，但人类在相位转换中比模型表现得更好。
(28:07) Trying to drive tooling in a way that increases human understanding, agency, and efficiency—that's the core thing.
试图以提高人类理解、能力和效率的方式推动工具的发展——这就是核心要义。
Transcript
Trading Time Horizons and Physical Infrastructure Constraints
交易时间范围和物理基础设施限制
Trading strategies operate across multiple time horizons, ranging from sub-100 nanosecond FPGA-based packet turnaround to longer-term decision-making processes. While high-speed trading requires specialized hardware like FPGAs in co-located facilities, larger models allow for more flexibility in physical placement. Operating within co-located data centers introduces strict constraints on power, cooling, and space, necessitating careful engineering to manage compute density and infrastructure requirements.
交易策略在多个时间范围内运作，从亚 100 纳秒的 FPGA 基础数据包周转到更长期的决策过程。虽然高速交易需要专用硬件，如在共同驻地设施中的 FPGA，但更大的模型允许在物理位置上更大的灵活性。在共同驻地数据中心内运营引入了对电力、冷却和空间的严格限制，必须仔细工程设计以管理计算密度和基础设施需求。
Dwarkesh Patel:
(00:00)
Jane Street are partners of my podcast and one of the fun ideas we had is why don't I come visit a This is a data center for training that you guys run. So I just got a tour of this Texas data center from Ron Minsky, who co-heads the technology group, and Dan Pontecorvo, who heads the physical engineering team. So thank you guys for showing me around.
Jane Street 是我播客的合作伙伴，我们的一个有趣想法是，为什么我不来访问一下你们的这个数据中心呢？这是一个用于训练的数据中心。所以我刚刚参观了这个德克萨斯州的数据中心，由罗恩·敏斯基（Ron Minsky）和丹·庞特科沃（Dan Pontecorvo）带领，他们分别负责技术组和物理工程团队。感谢你们的陪同。
Ron Minsky:
(00:22)
For what it's worth, I've never been here before, so I was also getting a tour, which was great.
不管怎样，我以前从未来过这里，所以我也是在参观，这真是太好了。
Dwarkesh Patel:
(00:26)
Previously, I was confused. Well, how can you be doing GPU things if you need to be trading on nanoseconds? And maybe you can talk through what is the actual time horizon Can you afford to be running big models in the middle of making trading decisions?
之前我感到困惑。嗯，如果你们需要在纳秒级别进行交易，那怎么能做 GPU 相关的事情呢？或许你可以聊聊，实际的时间范围是什么？你能否承受在做交易决策的过程中运行大模型？
Ron Minsky:
(00:44)
I think the thing to understand here is there isn't one time horizon. There are many time horizons. There are trading systems we build and trades that we do where in order to be competitive you actually have to turn around a packet in under 100 nanoseconds. That's a very different regime, right? People sometimes talk about like, oh, can you guys write high performance stuff in OCaml? We can, but like for this kind of speed, it's like, it doesn't matter if you write, you know, Camel or Rust or C++, you can't use a CPU. You are going to be on an FPGA that's like direct wire attached to the network.
我想这里需要理解的是，没有一个固定的时间范围。有很多时间范围。我们构建的交易系统和我们进行的交易，需要在不到 100 纳秒的时间内完成数据包的传输，以保持竞争力。这是一种非常不同的情况，对吧？有时候人们会谈论，哦，你们能在 OCaml 中编写高性能的东西吗？我们可以，但对于这种速度来说，无论你是写 Camel、Rust 还是 C++，你都不能使用 CPU。你将使用一种直接连接到网络的 FPGA。
(01:17)
And you're going to be turning around the packets so fast that if you like attach an oscilloscope to the wire on the way in and the wire on the way out, you would see the packet start to leave before it's done being consumed. So it's like a very different, very specialized regime. But like when you're in that time regime, You really can't do very much computation. The decisions you're making are going to be very simple. And in fact, there's this kind of whole curve of trade-offs between how smart is the decision that you're making, be it a model or some other kind of maybe even like handwritten decision-making process, and how fast the turnaround is.
而且你将以非常快速的速度处理数据包，以至于如果你把示波器连接到输入和输出的线路上，你会看到数据包在被消费之前就开始离开。所以这是一个非常不同、非常专业化的情况。但是当你处于那个时间范围时，你实际上不能进行很多计算。你做出的决策将会非常简单。实际上，有一个整体的权衡曲线，关于你所做的决策有多智能，无论是一个模型，还是其他某种手工决策流程，以及处理速度有多快。
(01:50)
And The right way to build an optimal trading strategy is really to have a kind of ensemble approach where for some kinds of decisions, you're making very simple decisions very quickly. For some kinds of decisions, you're operating at the scale of, instead of thinking of 100 nanos, maybe like A handful of mics or tens of microseconds or hundreds of microseconds or milliseconds. And in some cases, there are processes where if you can get that decision turned around, you know, in an hour or that day, that's totally fine. And you're kind of competitive on a time basis at each of these horizons, but you're making very different kinds of decisions at all of them.
合理构建最佳交易策略的正确方法，实际上是采用一种集合的方法，其中对某些类型的决策，你需要非常快速地做出非常简单的决策。对于某些类型的决策，你的操作规模是，从考虑 100 纳秒，转而考虑一小把微秒、十几微秒、几百微秒或毫秒。在某些情况下，如果你能在一个小时或当天内完成这个决策，完全可以。在这些时间范围内你在时间上是竞争的，但你在每个时间范围内做出的决策都是非常不同的。
Dwarkesh Patel:
(02:30)
Maybe you can't say, but what is it exactly these models are predicting? Surely it's just not the next thing in the order book, or maybe it is.
也许你不能说，但这些模型到底在预测什么呢？肯定不只是订单簿中的下一个东西，或者也许就是。
Ron Minsky:
(02:36)
Right. So we're definitely like dancing towards stuff that's hard to talk about, but I think the simplest and most important one that we've been thinking about, like we think about it now, but like also 25 years ago when I started at Jane Street, when I was building like models out of linear regression, you know, and stuff like that, like a very useful kind of thing is to predict a fair value for a thing. Like, what do we think this thing is worth? And that fits in in a very kind of composable way into lots of different trading processes. That's not the only kind of thing that we use as a prediction target, but it's an important one.
对。我们绝对是在跳舞，谈论一些难以言说的事情，但我认为我们一直在思考的最简单和最重要的一个，我们现在在思考这个问题，但在我 25 年前刚开始在 Jane Street 工作时，我也在思考这个，当时我在构建线性回归模型，你知道的，还有其他类似的东西，一个非常有用的事情是预测事物的公平价值。像，我们认为这个东西值多少钱？而这以一种非常可组合的方式融入许多不同的交易过程。这并不是我们用作预测目标的唯一类型，但它很重要。
Dwarkesh Patel:
(03:06)
It seemed like a meme I was getting for a while about like what trading firms do is like, you got to get the colo and where the NASDAQ exchange is. And it's very important that your machines are right there.
我曾经听到一个关于交易公司所做事情的段子，像是，你得拿到 colo 和纳斯达克交易所的位置。而且你的机器必须就在那儿。
Ron Minsky:
(03:15)
Without saying too much about what we put where, like your inference processes might be on CPU, might be on FPGA, might be on GPU. Depending on the kind of constraints of how much compute you need, how big the model is, what kind of latency turnaround do you need? And yeah, like bigger, slower things you can put farther away. It's annoying to have to put all the compute right by the exchange. And for the stuff that's like really, really fast, like being in the colo isn't enough. You care about like how long is the spool of wire that gets you there? Like you're literally like measuring out the length of the fiber runs when you're, again, when you're like at this very, very low nanosecond scale.
不用多说我们把什么放在哪里，像是你的推断过程可能在 CPU 上，可能在 FPGA 上，可能在 GPU 上。这取决于你需要多少计算、模型有多大、你需要什么样的延迟周转？是的，像是更大、更慢的东西可以放得更远。把所有计算都放在交易所附近是件麻烦事。对于那些真的是非常非常快的东西，仅仅在 colo 内是远远不够的。你关心的是到那里的电缆有多长？你实际上是在测量光纤的长度，当你又一次处于这个非常、非常低的纳秒级别时。
(03:53)
In general, the bigger models give you a lot more flexibility in terms of where they physically go.
一般来说，更大的模型在物理部署上提供了更多的灵活性。
Dan Pontecorvo:
(03:59)
If we're putting GPUs in some of these co-located facilities that are next to the exchanges, now you have to work with their rules. Who is that provider? Who is giving you that space? Your power, your cooling, all those constraints now are maybe slightly tighter than if you have a facility that you're designing and operating. You're now having to come up with ways to, hey, maybe I could only get one GPU in a rack because it consumes so much power, so now I have to spread it all out rather than being able to do liquid cooled in one rack. Things we need to keep in mind as our compute, you know, compute needs change.
如果我们在某些与交易所相邻的共置设施中放置 GPU，那么现在你必须按照他们的规则来操作。那个提供商是谁？谁在给你提供那块空间？你的电力和冷却，所有这些限制现在可能比你自己设计和运营的设施要严格一些。你现在必须想办法，嘿，可能在一个机架里只放一个 GPU，因为它消耗了太多电力，所以现在我必须把它们分散，而不能在一个机架里使用液冷。这些是我们需要记住的事情，因为我们的计算需求，你知道，正在改变。

Scaling Laws and the Role of Human Judgment in Trading
规模法则与人类判断在交易中的作用
Financial firms leverage scaling laws through diverse model architectures and high-frequency experimentation, prioritizing faster iteration times to drive innovation. Unlike general-purpose LLMs, financial models must handle noisy, high-volume data streams with specific latency requirements. Despite advancements in automation, trading remains an "AGI-complete" task where human judgment is critical, particularly during market phase transitions or volatile events where models may struggle to adapt to unprecedented conditions.
金融公司通过多样化的模型架构和高频实验利用规模法则，优先考虑更快的迭代时间以推动创新。与通用的 LLM 不同，金融模型必须处理具有特定延迟要求的嘈杂、高容量数据流。尽管自动化有所进展，交易仍然是一个 “AGI 完全” 任务，人类判断至关重要，特别是在市场阶段转换或波动事件期间，模型可能难以适应前所未有的条件。
Dwarkesh Patel:
(04:31)
You guys recently signed a $6 billion compute deal with CoreEV. What are you going to use that for?
你们最近与 CoreEV 签订了 60 亿美元的计算协议。你打算用它来做什么？
Ron Minsky:
(04:37)
The rest of the AI world has scaling laws. We have scaling laws too and there are lots of models that we want to train. I think the thing that's interesting and maybe different between us and the kind of more traditional AI labs is the amount of Diversity in model architecture and the amount of experimentation that we're doing. So a lot of the value you get from all of this is just people are like trying lots of very different new things in the model designs and giving researchers just like faster iteration time so they can discover more ideas and drive more innovation. It just turns out to be incredibly important.
剩下的 AI 世界有扩展法则。我们也有扩展法则，还有很多模型我们想训练。我认为有趣并且可能与我们以及更传统的 AI 实验室之间的不同之处在于模型架构的多样性和我们所做实验的量。所以，从这一切中获得的大部分价值只是在于人们尝试许多非常不同的新模型设计，为研究人员提供更快的迭代时间，以便他们可以发现更多的想法并推动更多的创新。这被证明是非常重要的。
Dwarkesh Patel:
(05:11)
In the case of these foundation labs, there's some gain from training just one model that does everything that is fully general rather than building a bunch of Custom Different Models. Can you give me a sense of why there's a different trade-off at Jane Street?
在这些基础实验室的情况下，从训练一个可以做一切的通用模型中获得的收益要比构建一堆定制的不同模型要好。你能告诉我为什么在 Jane Street 这种权衡不同吗？
Ron Minsky:
(05:24)
For us, some of the specialization is about Being adapted to consume the right kind of data, right? And there's like many possible data sources that we might be feeding in. There are like a bunch of just differences in the data rates that we need to achieve. Like just like another thing that like just makes us need to kind of specialize in what we're doing is just like the overall kind of both inference and trading dynamics are made different by just like the bytes to flop ratio being different. We have like way more data That we are using to train the models, but the data is kind of bite for bite less informative just because financial data is very noisy.
对我们而言，一些专门化是为了适应正确类型数据的消费，对吧？我们可能会输入许多可能的数据源。在我们需要达到的数据速率上有很多不同之处。就像另一件使我们需要在所做的事情上进行专业化的事情，就是整体推断和交易的动态因为字节与浮点运算的比率不同而有所不同。我们用于训练模型的数据要多得多，但这些数据在字节对字节上信息含量较低，仅仅因为金融数据非常嘈杂。
(06:00)
And so the models tend to be smaller and the data tends to be noisier and there tends to be a lot more of it. And it's also different between different models that we build for different applications, right? As we try and figure out like, how can we leverage more of the information that we get? It's like, oh, now there's like all of the kind of Decisions from like, how do we store and load data efficiently, to how do we shape the model, to how do we make the inference process, you know, have both the throughput and latency that it needs. There's going to be a whole different set of trade-offs there.
所以模型往往比较小，而数据往往更嘈杂，且数量也往往更多。而且我们为不同应用构建的不同模型之间也有区别，对吧？当我们试图弄清楚如何利用我们获得的更多信息时，哦，现在的所有决策都涉及从如何有效存储和加载数据，到如何调整模型，再到如何使推断过程具备所需的吞吐量和延迟。这将涉及到一整套不同的权衡。
(06:30)
And so there's just like a lot of value in kind of working that out and picking the best thing that you can do for different applications.
所以在理清这一点并为不同应用选择你能做到的最佳方案方面有很多价值。
Dwarkesh Patel:
(06:39)
What is the inference workload actually? How does it compare to what your traditional big chatbot LLM company is doing?
推断工作负载实际上是什么？它与你传统的大型聊天机器人 LLM 公司所做的比较如何？
Ron Minsky:
(06:48)
In broad strokes, latency matters more, as you might expect. Batching is still an issue. Depending on the model you're doing, you might have models or part of models that are disaggregated for different symbols that you're looking at. The same kind of pulling in data from multiple sources and batching them together makes a difference. I think another thing that's interesting is just the data rates are really high. The aggregate data rate that you get in a large LLM lab from all of the different users is also very high, but the amount of sequential data that you're going to get from any one user is not that high.
从广义上讲，延迟比你想象的更重要。批处理仍然是一个问题。根据你所使用的模型，你可能有模型或模型的一部分是针对你正在关注的不同符号进行解耦。从多个来源提取数据并将其批处理在一起是有区别的。我认为另一个有趣的事情是数据速率真的很高。从所有不同用户那里在大型 LLM 实验室中获得的总数据速率也非常高，但每个用户所获得的顺序数据量并不高。
(07:22)
Whereas the data that you're pulling is the bytes that are coming out of the NASDAQ feed. It's like, oh man, the data rate that you want, the kind of sequentially consumed in one domain, kind of causally one after the other is really high. And so again, the dynamics change. But I think a lot of the same Kind of basic engineering questions are not so dissimilar, but like all the constants are twiddled to different places until you end up making different choices. There's more emphasis on the performance of the data loading than you might otherwise see. I think we're doing a lot of work to build out our own large-scale data storage system, our own internal object store, where we've used various vendor products.
而你提取的数据则是来自纳斯达克馈送的字节。就像，哦，天哪，你想要的数据速率，在某个领域中顺序消耗的字节，在因果关系上是一个接一个的速度真的很高。所以再一次，动态发生变化。但我觉得许多基础工程问题并不那么不同，只是所有常数都被稍微调整到不同的地方，直到你最终做出不同的选择。对数据加载性能的重视程度可能比你否则看到的更多。我认为我们正在努力构建我们自己的大规模数据存储系统，以及我们的内部对象存储，其中我们使用了各种供应商产品。
(08:12)
Over time, I just think for some of these research-focused use cases, we need to operate at a much larger scale and need also to deal with the diversity of data centers. This is less an inference time and more of a training time question of we just can't get all the compute we want all in the same place. I feel like in general, an important trick in effectively running a technical organization is figuring out what shortcuts you can take. One shortcut that we were privileged to be able to take for many years is we got to pretend like there was only one CPU architecture on the planet. Everything was for x86-64. We pretended like none of these other things existed.
随着时间的推移，我认为对于一些以研究为导向的使用案例，我们需要在更大规模上运行，也需要应对数据中心的多样性。这更像是推断时间的问题，而不是训练时间的问题，我们无法将所有需要的计算都集中在同一个地方。我觉得一般来说，成功运行一家技术组织的重要窍门是弄清楚你可以采取哪些捷径。我们多年来能够采取的一个捷径是，我们得以假装地球上只有一种 CPU 架构。一切都是为 x86-64 服务。我们假装这些其他东西都不存在。
(08:52)
And that simplified a bunch of things. And we also had one big research data center and one big storage cluster. And that also simplified a ton of things. And actually, both of those have now been unwound. You just can't get the amount of power. You cannot wire in enough thunderbolts into the same data center to power all the things you need. You need to get the data centers built all over the place. So there's a big disaggregation problem. And that gives you a problem like, oh, now you have to think about Your compute scheduling and your storage scheduling being intertwined one with the other and there's a ton of data. So moving around is like non-trivial.
这简化了许多事情。我们还拥有一个大型的研究数据中心和一个大型的存储集群。这也简化了大量事情。事实上，这两者现在都已经被解构。你根本无法获取足够的电力。你无法在同一个数据中心布线足够的电力线路来为你需要的所有设备供电。你需要让数据中心在各地建设。所以这是一个重大的去中心化问题。这让你面临一个问题，比如，现在你必须考虑你的计算调度和存储调度必须相互交织，还有大量数据。所以在这里移动是相当复杂的。
(09:25)
And also we had to give up on this x86 only thing because Nvidia has a bunch of cool new products that mean that you need to support ARM now.
而且我们也不得不放弃这种仅限于 x86 的做法，因为 Nvidia 有一堆很酷的新产品，这意味着你现在需要支持 ARM。
Dwarkesh Patel:
(09:33)
Zooming out, I want to ask a very naive question. There's maybe a naive view that, you know, if you have AGI, It can like immediately do what Jane Street does. Give me a sense of like why that naive view is naive.
拉远视角，我想问一个非常幼稚的问题。也许一种幼稚的看法是，你知道，如果你有 AGI，它可以立刻做 Jane Street 所做的事情。给我一种感觉，为什么这个幼稚的看法是幼稚的。
Ron Minsky:
(09:49)
Yeah. And I don't want to totally discount it. Like, you know, there's a world that we should take seriously where like, you know, we're going to build large language models or some other AI systems that are like strictly smarter than all humans on the planet and more capable at all cognitive tasks. And like, Yeah, that's going to be weird. And that's a different state of things. And in that case, yeah, maybe large amounts of things that Jane Street does will be automated away. And maybe we'll all just sit back and drink more margaritas or something. I don't know what that world looks like. But it doesn't feel like we're particularly close to that now.
是的。我并不想完全否定它。就像，你知道，有一个我们应该认真对待的世界，就像，我们将建立大型语言模型或其他一些严格比地球上所有人都更聪明、在所有认知任务上更有能力的 AI 系统。而且，嗯，这会很奇怪。这将是一个不同的状态。在那种情况下，嗯，也许 Jane Street 做的大量工作将会被自动化。也许我们都只会坐下来喝更多的玛格丽塔酒之类的。我不知道那个世界是什么样子的。但现在感觉我们并没有特别接近那个目标。
(10:29)
In general, I think it's easy to underestimate the richness and complexity of the work, both at a company like Jane Street does, but really that is done in any really ambitious, high-difficulty company-scale task. I think trading in particular feels to me as AGI-complete, NP-complete, meaning that all of the different problems of the world end up influencing what you're doing in a trading context, because at the end of the day, Trading involves figuring out what things are worth, which means making predictions about the future, and lots of different things flow into that, and as various pieces of that get automated, You know, you have the usual thing of like the other hard parts that we don't yet know how to automate.
总的来说，我认为很容易低估这项工作的丰富性和复杂性，无论是在像 Jane Street 这样的公司所做的工作，但实际上，这也是任何真正雄心勃勃、高难度的公司规模任务中所进行的工作。我认为交易特别让我感觉像是 AGI 完整和 NP 完整，这意味着世界上的各种问题最终都会影响你在交易中的决策，因为归根结底，交易涉及到评估事物的价值，这意味着对未来进行预测，而很多不同的因素都会影响这一点，而随着这些环节的自动化，你知道，常见的情况是其他我们还不知道如何自动化的困难部分。
(11:14)
Well, that ends up being where the competitive edge lies. I feel like humans and like human cognition are like more valuable than ever. Like I have never been more desperate to hire more engineers and more traders than I am today because everything people are doing is more valuable than it was. I mean, some of this is just me being Somewhat skeptical that we are quite as close to the models that are like smarter than humans and all the things as some people seem to think.
好吧，这就是竞争优势所在。我觉得人类和人类的认知比以往更有价值。我从未像今天这样迫切需要招聘更多的工程师和交易员，因为人们所做的一切比以往更有价值。我的意思是，这其中有些只是我对我们距离那些比人类更聪明的模型和各种事物的怀疑。
Dwarkesh Patel:
(11:40)
Maybe it's like physical infrastructure, like actually getting the colo. Maybe it's actually like a software infrastructure that you built. Like, give me a sense of what it is that would, you know.
也许这就像物理基础设施，实际上是获得数据中心。也许这实际上是你建立的软件基础设施。给我一个关于它是什么的感觉，你知道的。
Ron Minsky:
(11:47)
Yeah, we build like a huge variety of complicated pieces of software, have people thinking about lots of different trading problems, some of which are not very electronic at all. Like the business is just like way more diverse than I think people give it credit for. And there's an idea of like, oh yeah, it's like, it must be that like simple thing where you just like, you just have smart people who like make smart decisions and write good software. And like, if we could just automate the smartness part, That would be the whole thing and I think it's just way more complicated than that.
是的，我们构建了各种复杂的软件，拥有思考许多不同交易问题的人，其中一些根本没有电子化。这个行业的多样性远超过我认为人们给它的评价。而且有一种想法，哦，是的，肯定是那种简单的事情，你只是，你只是有聪明的人，他们做出聪明的决策并编写优秀的软件。如果我们能自动化聪明的部分，那就完美了，但我认为事情远比这复杂得多。
Dwarkesh Patel:
(12:15)
What do you mean by the non-electronic parts of trading?
你所说的交易中的非电子部分是什么意思？
Ron Minsky:
(12:18)
I mean, there's still trading that happens via chat between people talking to each other and making decisions and like someone like sizing up how much adverse selection they think the person on the other side of the phone represents. That's like still a real part of the business. There's just different kinds of securities that have taken longer to get more automated. The bonds business, for example, is just not nearly at the level of automation that you see in equities. Indeed, I think we were kind of confused about this. I think those of us who have been in the business for a while, we kind of I mean, I started a little too late to really see the kind of transition of equities becoming electronic,
我的意思是，仍然有通过聊天发生的交易，人们互相交谈并做出决策，就像有人在评估对方在电话另一端所代表的逆向选择程度。这仍然是业务的一个真实部分。只是有些不同类型的证券需要更长的时间才能实现更多自动化。例如，债券业务的自动化水平远不如股票。确实，我认为我们在这方面有点困惑。我认为我们这些在这个行业待了一段时间的人，我是说，我开始得有点晚，没能真正看到股票变成电子化的过程，
(12:59)
but I think people who were, you know, paying attention a little earlier than me were like, yeah, and I guess everything else comes next. And like, you know what? It's been like, you know, 25, 30 years and like not everything has gone that way. The systems are still, you know, we don't have a lot of people like standing on the floor of exchanges anymore, but there's still lots of trading that is deeply intermediated by humans and human judgment.
不过我觉得那些比我稍早关注的人则是，是的，我想其他一切都接踵而至。你知道吗？过去大约 25、30 年，情况并不是所有事情都朝那个方向发展。系统仍然是，我们没有很多人在交易所的交易大厅，但仍有很多交易是由人类和人类判断深度中介的。
Dwarkesh Patel:
(13:18)
How much are humans in the loop between the model and the trading decision?
在模型与交易决策之间，人的参与程度有多高？
Ron Minsky:
(13:23)
Many of your most profitable days They happen when like weird stuff happens and there are events and the world kind of goes crazy and like nobody knows what's going on. And like that's when it's like very hard to provide liquidity in those contexts. And so you get paid more for doing it. And there's often a lot of volume on days like that. And doing that well often involves human judgment of like thinking about like, how is today different from all of the other days? And you know, to the degree that we can, we want to build models that work well through phase transitions.
你最赚钱的很多日子往往都是在奇怪的事情发生时，那些事件让世界有点疯狂，没人知道发生了什么。而且在这种情况下，提供流动性非常困难。所以你获得的报酬会更多。这样的日子通常会有很多交易量。而且做得好通常涉及人类的判断，思考今天与其他日子的不同之处。而且，尽可能地，我们希望构建在相变时表现良好的模型。
(13:55)
But also we think humans work better than models do through phase transitions and sometimes you need this kind of meta judgment to decide. What to do. And so there's a, even for the systems that are largely automated, there are decisions to be made by the people who are watching. And we always have people who are watching, right? I think an important part of trading is paying attention to and thinking about what's happening during the trading day. Even if the individual transactions are going by far too fast for a human to kind of weigh in on that kind of transaction by transaction basis.
但我们也认为人类在相变时的表现优于模型，有时需要这种元判断来决定。应该怎么办。因此，即使是大部分自动化的系统，依然有需要由观察者做出的决策。我们总是有观察者，对吧？我认为交易的重要部分是关注和思考在交易日发生的事情。即使个别交易进行得太快，以至于人类无法在行为上逐一权衡。

Data Center Evolution and Compute Resource Management
数据中心演变与计算资源管理
Data center operations have shifted toward modular infrastructure and off-site pre-fabrication to overcome long lead times for critical components like generators and cooling equipment. As compute density increases, infrastructure design must be finalized well before chip procurement. Firms manage compute constraints by prioritizing high-value research and experimentation, treating excess capacity as a buffer for bulk inference tasks rather than relying on a single, monolithic reserve use case.
数据中心运营已经转向模块化基础设施和离站预制，以克服关键组件如发电机和冷却设备的长交货期。随着计算密度的增加，基础设施设计必须在芯片采购之前最终确定。公司通过优先研究和实验的高价值来管理计算约束，将多余的容量视为大量推理任务的缓冲，而不是依赖单一的、统一的储备用例。
Dwarkesh Patel:
(14:25)
Dan, what have been the more notable changes over the last 20 years that you've been And today, we're going to be talking about what we're doing in buildings like these.
丹，你在过去 20 年中看到的更显著的变化是什么？今天我们将讨论我们在像这样的建筑中所做的事情。
Dan Pontecorvo:
(14:33)
Yeah, people actually care about data centers and want to talk about it. You're working on cooling for a while and now all of a sudden people talk about it and think it's interesting. So that's fun and exciting. And for folks on my team, I think they feel that way as well. There's people who have been in the data center industry for 20 years that kind of still want to do it the way they used to. And I think that's kind of falling by the wayside now. Challenging previous thoughts. Hey, my entire data center is backed up by generators. But generators are some of the longest lead time items you can buy.
是的，人们其实关心数据中心，并想谈论它。你工作于冷却领域一段时间后，突然人们开始谈论它，并觉得它很有趣。所以这很有趣和令人兴奋。对我团队的成员而言，他们也有这样的感觉。数据中心行业中一些工作了 20 年的人仍然希望以旧方式进行。我认为现在这种情况正在被淘汰。挑战以往的想法。嘿，我整个数据中心都是由发电机备份的。但发电机是你可以购买的时间周期最长的项目之一。
(15:05)
So maybe we take those away and only put it for a core part of the system that needs that resiliency. That gets our GPUs on six months faster. Let's do it. So those are things that, you know, maybe it's not the best engineering decision, but it's really the best business decision. And I think it's stuff like that that has been coming up more and more often.
所以也许我们将它们去掉，仅用于核心系统中需要这种韧性的部分。这能让我们的 GPU 提前六个月到达。那就这样吧。所以这些事情，可能不是最好的工程决策，但确实是最好的商业决策。我认为越来越多这样的事情正浮出水面。
Dwarkesh Patel:
(15:24)
It feels like every year people change the What is bottlenecking scaling AI compute? Right now, as you're doing more negotiations and trying to acquire more compute, what is the current bottleneck and what do you expect it to be for next year?
感觉每年人们都在改变，什么在制约 AI 计算的规模？现在，当你进行更多的谈判并尝试获取更多计算资源时，目前的瓶颈是什么？你预计明年的瓶颈是什么？
Dan Pontecorvo:
(15:36)
Putting aside compute and memory and all that fun stuff, so generators, transformers, Some of the cooling equipment that's used now for the liquid cooling is in a lot of demand, and it changes rapidly. What I tell you today is definitely going to be different two weeks from now. We do this thing, we work very closely with internal teams on the procurement side to stock up on some of this stuff. Stuff that we know is fungible across all our data centers, we will warehouse and have it ready to go. There's components like generators where you're not going to put a giant generator in a warehouse or For instance, if you're doing something behind the meter like a turbine,
暂且不谈计算和内存以及其他有趣的东西，所以发电机、变压器、现在用于液冷的某些冷却设备需求很大，并且迅速变化。我今天告诉你的事情，在两周后肯定会有所不同。我们做这项工作，与内部团队在采购方面非常紧密合作，以备足够的库存。我们知道在所有数据中心都可以通用的东西，我们将其入库并准备就绪。像发电机那样的组件，你不会将一个巨型发电机放在仓库中；例如，如果你在做某个突出的项目，例如涡轮机，
(16:12)
you're going to have to think about those markets a little bit more, where you're getting them, where you're staging them. You can't just leave them off to the side. I think the components definitely change. Those are some of the big ones. As we get to more and more density, I think One hope is that the buildings get a little bit smaller and maybe, and we're able to like, you know, build the buildings faster, get all that compute kind of in a nice tight bundle. And then all the infrastructure around it's gotta be maybe pre-built and delivered to site, right? Modular data centers or modular infrastructure is becoming more and more of a thing where these components, especially the long lead components are being designed and built offsite and shipped to site.
你得更加考虑这些市场，考虑你从哪里获得它们，如何储存它们。你不能就把它们放在一旁。我认为组件确实在变化。这些都是大问题。随着密度越来越高，我认为一种希望是建筑变得小一点，也许，我们能够更快地建造这些建筑，将所有计算资源很好地打包在一起。然后所有周围的基础设施也必须预先建造并送到现场，对吧？模块化数据中心或模块化基础设施正变得越来越普遍，这些组件，尤其是时间周期长的组件正在现场外设计和建造，并运送到现场。
(16:54)
So almost as close to plug and play as you can get.
所以几乎可以达到即插即用的状态。
Dwarkesh Patel:
(16:57)
One of the points you made earlier is that As the racks themselves get more dense, you know, more and more of the data center is like the infra around the actual racks, which is actually kind of similar to like a package on like a chip, right? Or like a chip on a package. It's like the compute is a very small part of the total area of the package.
你之前提到的一个观点是，随着机架本身变得更密集，数据中心越来越多的是关于实际机架周围的基础设施，这实际上有点类似于芯片上的封装，对吧？或者像封装上的芯片。计算实际上是整个封装面积中非常小的一部分。
Dan Pontecorvo:
(17:23)
It's interesting. I mean, I don't, you know, It doesn't solve any problems per se. It creates others, sure. You get to a one megawatt rack. People are like, what does that even mean, one megawatt in a rack? The cooling, the pipe is just going to get larger that you're bringing there. The amount of power, whether it's the AC power that we're using now or 800 volt DC where it's going in the future, you still have to bring all those components to a slot. The thing that's interesting from our point of view is, You know, we could design these engineering things, but at the end of the day, whether it's NVIDIA or an ASIC or whoever, they have to sell a component that can work in a data center.
这很有趣。我的意思是，我不会， 这并不能解决任何问题。它确实会产生其他问题，当然。你进入一兆瓦机架时。人们就会问，机架里的 1 兆瓦到底意味着什么？你的冷却管会变得更大。不论是我们现在使用的交流电，还是未来的 800 伏直流电，仍旧必须将所有这些组件带到插槽。从我们的角度来看，值得注意的是，我们可以设计这些工程方案，但无论是 NVIDIA、ASIC 还是其他公司，它们必须出售可以在数据中心中使用的组件。
(18:02)
And they're thinking very hard about what they sell because you need people to use it, right? If you build a one-megawatt data center, one-megawatt rack, but there's no way to power and cool it, it's kind of useless. So, you know, we're working very closely with kind of almost everyone in that space to think about what are the components you need to be able to support these next generations. Because the lead times you're talking about, you know, over a year sometimes, and you're just, you're deciding on the infrastructure before you're placing an order for the chips. So, you know, you're trying, for instance, the, you know, TPUs, they use lower temperature water and they're half as dense as,
他们在认真考虑他们所销售的东西，因为你需要人们使用它，对吧？如果你建立一个一兆瓦的数据中心，一个一兆瓦的机架，但没有办法为其提供电力和冷却，那就没有什么用处。所以，我们与几乎所有人紧密合作，思考你需要哪些组件来支持下一代产品。因为你提到的交货时间，有时会超过一年，而在下订单芯片之前，你就已经在决定基础设施。所以，你知道，举个例子，TPU 使用低温水且其密度是一半，
(18:39)
you know, an NBL72 GP300, right? That requires a different strategy and you want to make sure you can handle those in the future.
相较于 NBL72 GP300，对吧？这需要不同的策略，且你希望确保自己未来可以处理这些。
Dwarkesh Patel:
(18:47)
One of the things that allows hyperscalers to commit to large amounts of compute is that they have some reserve use for Excess compute that they're not using for training or inference of LLMs at a particular time, for example, like meta, if they're not using some of the GPUs they've bought, they can just say, we'll just make our Insta ad serving model slightly better for today. What is the equivalent sort of reserve use of compute for Jane Street that's just a lower bound on how much it's worth for you?
让超大规模供应商能够承诺大量计算资源的原因之一是，他们在某个特定时间有一些备用的计算能力未用于 LLM 的训练或推理。例如，像 Meta，如果他们没有使用某些购买的 GPU，他们可以只说，今天我们就让我们的 Insta 广告投放模型稍微好一些。Jane Street 的计算资源利用相当于什么，也就是你认为它值多少钱的下限？
Ron Minsky:
(19:16)
Part of what's going on is like, in many ways, we're just like very compute constrained. There's lots of Innovation and experimentation and new ideas that people have that is bounded by the amount of compute that we have. And so in some ways, like if we just think about like, like we do, we try and do a kind of moderately rigorous job of thinking about the value of the new different runs that we can do and the value of the runs that we're turning away is really quite high. We're doing what we think are the most valuable things, but if it turns out we have more compute than we need for those, there's just a ton of other research and experimentation that we can do in that space.
发生的部分情况是，在许多方面，我们实际上是非常受限于计算资源的。人们拥有许多创新和实验的新想法，但这些都受到我们拥有的计算资源的限制。所以在某种程度上，如果我们只是考虑一下，我们会努力以一种适度严谨的方式来思考我们可以进行的新不同运行的价值，以及我们拒绝的运行的价值真的相当高。我们正在做我们认为最有价值的事情，但如果结果是我们所需的计算能力超出了这些，还有很多其他的研究和实验可以在这个领域进行。
(19:55)
We're nowhere near to being like, oh, too much compute. We have the opposite problem. I think there's also really low-hanging fruit in that direction. It's valuable to retrain the models more often. There's some decay in the quality of models over time and being able to rerun them, that has immediate and clear value to the firm. There's also some amount of bulk inference tasks that we can do that can fill in the gaps in the systems where there's nothing else to schedule. So we don't quite have the thing that looks like the analog of the Instagram ad serving thing, but there is just a ton of other Kind of dark space of like things that we're not doing, but we would if we had more compute.
我们远未达到 “哦，计算太多了” 的程度。我们的问题正好相反。我认为在那个方向上还有一些低垂的果实可以摘。更频繁地重新训练模型是有价值的。模型的质量会随时间而下降，能够重新运行它们对公司具有直接和明显的价值。还有一些批量推理任务可以填补系统中没有其他安排的空白。所以我们并没有完全拥有类似于 Instagram 广告投放的功能，但还有很多我们未进行的其他类似的 “暗区” 事情，但是如果我们有更多的计算能力，我们会去做。
(20:40)
So we're like pretty unconcerned about getting value out of these. Everything there is like there is a bunch of embedded bets. Like we are like investing a lot of money in this stuff and You could imagine that things won't get better at the rate that we are thinking they will in terms of the value of the individual models and trades that we're doing. It's a competitive environment. Maybe other people will out-compete us. I think one part of remaining good is always being nervous about other ways that competitors can figure out doing similar things to what you're doing and reduce the value of that. There are ways that it might not work out, but Certainly with anything like the current mix of compute jobs that we have,
所以我们对此并不太担心获取这些的价值。那里的一切就像是有很多潜在的投资。就像我们在这些事情上投入大量资金，你可以想象，个别模型和我们进行的交易的价值可能不会以我们预期的速度提升。这是一个竞争环境。也许其他人会超越我们。我认为保持优秀的一部分是始终对竞争对手可能找到类似方法并降低其价值感到紧张。可能会有失败的方式，但对我们当前计算工作的组合而言，
(21:22)
we're just very far from having this problem.
我们离这个问题还很远。
Dan Pontecorvo:
(21:25)
It's interesting to hear this isn't exactly answered, but like, you know, you can disconnect the powering the data center from the chips and say, okay, well, you know, I might need to use this compute later. Let me commit to the data center and the power now, but like delay the decision on the chips, which are very expensive, right? And just be slightly long power data center for that point of time where you might need that compute. And then we'll build in situations where, hey, maybe we can kind of offload some of that capacity to somebody else. It's much easier for us, I guess, to offload power and data center capacity than it is the chips themselves for obvious reasons.
听到这些很有趣，虽然这并没有完全解答，但你知道，你可以把数据中心的电源与芯片断开，并说，好吧，你知道，我可能需要稍后使用这部分计算能力。让我现在先承诺电源和数据中心，但将芯片的决策延后，这些是非常昂贵的，对吧？只需稍微延迟一下数据中心的电源，直到你可能需要那部分计算能力的时间。然后我们会建立这样的情况，嘿，也许我们可以将部分能力转移给其他人。对我们来说，将电力和数据中心的能力转移比转移芯片本身要容易得多，原因显而易见。
(21:59)
But you can really bifurcate those two.
但你确实可以将这两者区分开来。

Organizational Scaling and Talent Strategy in AI-Driven Trading
组织规模与人才战略在 AI 驱动的交易中
Growth is primarily limited by the ability to find and mentor exceptional talent rather than hardware availability. The organization is expanding its focus to include fleet-wide optimization, custom ASIC development, and the application of formal methods to software engineering. Despite the rise of AI, the human element remains central, with a focus on building tools that enhance human understanding, agency, and efficiency within a complex, diverse trading environment.
增长主要受限于寻找和培养优秀人才的能力，而不是硬件的可用性。组织扩大了其关注范围，包括全舰队优化、自定义 ASIC 开发和将形式化方法应用于软件工程。尽管人工智能的兴起，人类元素仍然是中心，重点是构建增强人类理解、能动性和效率的工具，以应对复杂多样的交易环境。
Dwarkesh Patel:
(22:02)
This also changes the considerations around hiring. I mean, you already have like the highest bar for hiring, but it just increases even more. If you hire one more person, that is one person who will need compute to do their experiments. And that compute It's going to be traded off against somebody else who's excellent on your team who could be doing experiments themselves.
这也改变了招聘的考量。我的意思是，你们已经有了招聘的最高标准，但这只会让标准更高。如果你再雇一个人，那就意味着这个人需要计算能力来进行他们的实验。而这部分计算能力将与你团队中的其他优秀成员进行权衡，他们也可以自己做实验。
Ron Minsky:
(22:24)
I hear what you're saying, but we don't think, oh, it'd be weird to hire more researchers because then we'd have to give them more compute. It's more like the research is incredibly valuable. The researchers are incredibly valuable. This is a good argument for buying more compute. We're very axed to grow the amount of compute. These days, we are in something like the range of tens of thousands of GPUs, and we will in not too long be in the range of hundreds of thousands of GPUs. We think it's well justified by the business. It's not like It's not like, you know, we're worried about like, oh, you know, can we justify it based on like the P&Ls of the trading strategy? It's like, no, no, no.
我明白你的意思，但我们并不认为，哦，雇更多的研究人员会很奇怪，因为那样我们就得给他们更多的计算能力。更像是，研究是极其有价值的。研究人员是极其有价值的。这是购买更多计算能力的有力论据。我们非常期待增加计算能力的数量。目前，我们的计算能力在数万台 GPU 的范围内，不久后我们将进入数十万台 GPU 的范围。我们认为这是商业上合理的。这不是说，我们担心能否基于交易策略的损益表来为此辩护。不是的，不是的。
(23:04)
It's like, these are clearly good investments. So it doesn't feel like it's slowing us down on the hiring front. In some ways, the biggest impediment to growth is that it takes time to really train people and absorb them into the culture and build them up and build the place up. We want Jane Street to continue to be a great place to work. I just don't think of the hardware thing as at all being the thing that slows us down. I think the real limiting factors are finding great people and having the mentorship capacity for them.
这是显然是很好的投资。所以这让我们在招聘上不会觉得受到拖累。从某种意义上说，增长的最大障碍是需要时间来真正培训人员，让他们融入文化，培养他们并提升团队。我们希望 Jane Street 能继续成为一个优秀的工作场所。我只是不认为硬件问题会减缓我们的速度。我认为真正的限制因素是寻找优秀的人才和提供对他们的指导能力。
Dwarkesh Patel:
(23:33)
I guess this might be a good opportunity for you guys to mention what kinds of roles you're currently hiring for.
我想这可能是你们提及目前招聘哪些角色的好机会。
Ron Minsky:
(23:39)
Oh, man. Why don't you start in the engineering space?
哦，天哪。你为什么不从工程领域开始呢？
Dan Pontecorvo:
(23:41)
Yeah, I'll start. So we're generally just looking for really smart people that are interested in doing this stuff. And that's mechanical engineers, electrical engineers, I'm a project manager, architects, people that help design and build some of these spaces. Our remit in my team is really to find the spaces, to design them, to construct them, and then to operate them. It's a full life cycle. In each one of those, you need people, lots of engineers, What we call physical engineering, which is a made up term that we came up with, but mechanical engineers and structural engineers, maybe electrical engineers, those types of folks.
是的，我可以开始。我们总的来说是寻找真正聪明并对这些事情感兴趣的人。包括机械工程师、电气工程师、项目经理、建筑师，帮助设计和建造这些场所的人。我们团队的职责是寻找这些空间，设计它们，建造它们，然后操作它们。这是一个完整的生命周期。在每一个环节，你都需要人，很多工程师，我们所称的物理工程，虽然这是个我们创造的术语，但包括机械工程师和结构工程师，还有电气工程师，这类人才。
Ron Minsky:
(24:20)
And machine learning and trading in general is really like a whole team sport. And so we want to hire people from lots of different backgrounds and with lots of different capabilities. We're certainly very excited to hire people with We have specific machine learning backgrounds of designing architectures and building models in various cases. I mentioned that we have a bunch of custom architectures and stuff for our own bespoke kinds of data that we need, like the data characteristic of the markets. We also build LLMs and people who experience in all sorts of parts of the lifecycle of LLM training. We're interested in hiring and have been growing that area.
机器学习和交易整体上其实就像是一项团队运动。所以我们想从不同背景和不同能力的人中招聘。我们当然非常期待招聘在设计架构和构建模型方面有特定机器学习背景的人。我提到过，我们有很多为我们定制的架构和样式，满足我们所需的某种数据，比如市场的数据特征。我们还构建 LLMs，并且在 LLM 训练生命周期的各个阶段都有经验。我们有兴趣招聘，并且一直在扩大这一领域。
(25:02)
We hire lots of people with generally good scientific and technical backgrounds from math and CS and physics and engineering and stuff to be traders. There's a kind of mix of skills there, but that's an area we continue to be very excited to hire in. On the software engineering side, there's a general software engineering role, which we're always eager to get great people for that It feels a little silly to say, but just like Dan was saying, smart, curious people with really good CS backgrounds fit into that generalist role and there's lots of different kinds of things they can end up doing. There's also a bunch of interesting specialized areas where we really are excited.
我们吸引了大量具有良好的科学和技术背景的人员，来自数学、计算机科学、物理和工程等领域，成为交易员。这是一种技能的结合，但我们仍然非常期待在这个领域招聘。在软件工程方面，有一个通用的软件工程角色，我们总是渴望找到优秀的人来填补这个角色。说这话有点傻，但就像丹所说的，聪明、好奇并且具有良好计算机科学背景的人非常适合这个通才角色，他们可以做很多不同类型的工作。还有很多有趣的专业领域，我们真的很兴奋。
(25:47)
Here's the thing that's kind of new. With all of this scale, we are much more interested in fleet-wide optimization than we were in the past. Our old view about performance optimization was that it was much more about making the things that were most speed critical as fast as possible. More generally, yeah, compute's kind of cheap and people are expensive and we're not spending that much time optimizing our general compute. Man, we're doing a lot of general compute now. You start investing billions of dollars in this stuff and it just becomes more valuable there. And there are people who have experience in doing this at some of the hyperscalers.
这是一件有点新的事情。随着这一切的规模扩大，我们对整个车队的优化比过去更感兴趣。我们以前对性能优化的看法是，更注重让那些速度至关重要的东西尽可能快。更普遍来说，是的，计算成本有点低，而人力成本高，我们在优化一般计算上花的时间并不多。伙计，我们现在正在进行大量的通用计算。你开始在这些东西上投资数十亿美元，它的价值也会随之增加。而且有些人在一些超大规模公司中有相关的经验。
(26:20)
And we'd love to hire more people with that kind of background to think about the optimization problems that we're hitting, which are like We're related in important ways, different, but like, you know, so it's like both a related challenge and a new one. We're like, we do a lot of fun, like hardware engineering stuff. We're like working on our own ASICs. People with that kind of experience is super exciting. One thing that we mentioned a little earlier at lunch was like, we're starting to think about building out a formal methods team, using basically mathematical proof to make software engineering more effective. That's like a new, very speculative area.
我们希望雇佣更多拥有这种背景的人来思考我们面临的优化问题，这些问题在某种重要的方面是相关的，虽然不同，但你知道的，所以这既是一个相关的挑战，也是一个新挑战。我们做了很多有趣的硬件工程相关的事情。我们正在开展自己的 ASIC 项目。拥有这种经验的人真是令人兴奋。我们在午餐时提到的一件事情是，我们开始考虑建立一个正式方法团队，基本上使用数学证明来提高软件工程的效率。这像是一个新的，非常有前景的领域。
(26:56)
And we're like very excited to find people that we feel like that's a kind of a set of a whole community of people who in the past, I feel like I've always had to disappoint by like, yeah, we're not interested in formal methods. But like, I think the whole AI revolution makes formal methods suddenly a much more interesting field. And so it's a place we're excited to invest in. So I don't know. And like, I don't know, project managers, people who do front end dev actually like, From most of Jane Street's experience, we pretended like this whole web thing had never happened and like almost all of our tools were just like in the terminal.
我们非常期待找到那些我们认为是一个社区全体成员的人，以前他们总是让我失望，因为我们没兴趣正式方法。但我认为整个 AI 革新使得正式方法突然变得更加有趣。所以这是我们期待投资的地方。我不知道。而且，我不知道，项目经理、做前端开发的人实际上像是，从大多数 Jane Street 的经验来看，我们假装这个整个网络的事情从未发生过，而且我们几乎所有的工具都只是终端里的。
(27:26)
But, you know, it turns out it's useful to be able to like draw a straight line and, you know, have a tool tip and things like that. So we've actually invested a lot in building really good tools for doing front-end development and building tools for people and having great front-end engineers who are both really good software engineers and have a good sense of what it means to make an application that's good for a person is really important. I think as a general meta point about all of this, I think that in all of the legitimate and real excitement around AI tooling, I think people sometimes miss out on the importance of the human element of all of this.
但是，你知道，事实证明能够画一条直线、拥有工具提示之类的东西是有用的。所以我们实际上在构建非常好的前端开发工具和为人们提供工具方面投入了很多，拥有优秀的前端工程师，他们不仅是很好的软件工程师，而且对为用户打造优秀应用意味着什么有很好的理解，这非常重要。我认为关于这一切的一个总体元观点是，在所有关于人工智能工具的合法和真实的兴奋中，我觉得人们有时会忽略其中人类因素的重要性。
(27:59)
I think that we really care a ton about building tools that are good for people. And that includes the AI tooling itself. I think trying to drive tooling in a way that increases human understanding and agency and efficiency, that's the core thing. We are limited more than anything else. By the amazing people who work there and like being able to find more of the right people and grow the organization so that we can get more done And so we have a very kind of human oriented way that we think about the systems that we build It's been really cool to have you guys.
我们真的非常关心构建对人们有益的工具。这包括人工智能工具本身。我认为推动工具以增加人类理解、代理能力和效率，这才是核心。我们的限制主要来自于其他方面。通过在那工作的了不起的人，能够找到更多合适的人并壮大组织，以便我们能做更多事情。我们对所构建的系统有一种非常以人为本的思考方式，很高兴你们能在这里。
Dwarkesh Patel:
(28:32)
We're here to help you make these fun puzzles and challenges. I think in general you do that, but also you guys have made a couple for the listeners of the podcast in particular, and I think people who are listening to this might find it interesting to check those out, including one, by the way, which Not only was nobody who submitted to the competition able to solve, but Jane Street itself cannot solve, which involves finding backdoors to various LLMs that have a trigger phrase baked into them. Anyways, I mention this because to the extent people are interested in learning more, I think these are the kinds of fun puzzles that might give some indication of what work is like and why it seems like a fun place.
我们在这里帮助你制作这些有趣的谜题和挑战。我认为一般来说你们会这样做，但你们也为播客的听众准备了几个，我觉得正在收听的人可能会觉得查看这些很有趣，包括一个顺便提一下，没有任何提交比赛的人能够解决，而且 Jane Street 自身也无法解决，它涉及到找到各种 LLM 的后门，这些后门中嵌入了触发词。不过，我提到这一点是因为如果人们有兴趣了解更多，我认为这些有趣的谜题可能能给出一些工作是什么样的指示，以及为什么它似乎是一个有趣的地方。
Ron Minsky:
(29:12)
Yeah, puzzles are a deeply embedded part of the culture, so it's kind of great to use them as a way to reach out to people as well.
是的，谜题是文化中深深根植的一部分，所以用它们来吸引人们也很不错。
Dwarkesh Patel:
(29:17)
I guess the plug here in this case is JaneStreet.com slash Dwarkesh so that people can learn more about the open roles and about all these puzzles.
我想在这种情况下的推广是 JaneStreet.com slash Dwarkesh，以便人们可以了解更多关于开放职位和所有这些谜题的信息。
Ron Minsky:
(29:27)
Awesome.
太棒了。
Dwarkesh Patel:
(29:28)
Cool. Thank you for doing this, guys.
很酷。谢谢你们这么做，大家。
Dan Pontecorvo:
(29:30)
Thank you very much.
非常感谢。
Ron Minsky:
(29:31)
Our pleasure.
我们很乐意。
