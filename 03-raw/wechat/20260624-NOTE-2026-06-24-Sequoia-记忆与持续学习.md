---
media_id: note_4eb085f96cced54b4d07836d397a65e3_74831342705311107479412815576231
source: IMA Workbuddy同步库
media_type: NOTE
create_time: "2026-06-24"
sync_time: "2026-07-15T23:08:00+08:00"
---

A: 我们利用多种基于适配器的微调技术——例如 LoRAs、前缀和稀疏架构——来持续更新模型权重。核心挑战是确定哪些数据作为有用的训练信号。我们将原始文档、团队互动和反馈循环转化为训练数据，使模型能够随时间改善。这是关于在研究和产品之间创造一个紧密、集成的循环，让模型从现实世界中的实际用户反馈中学习，而不仅仅是成为一项从研究实验室抛出的静态成果。

Q: How do you respond to the "Bitter Lesson" perspective—the idea that simply scaling compute and data on generic models will eventually solve all these problems?


Q: 你如何回应 “苦涩教训” 的观点——即简单地在通用模型上扩展计算和数据最终会解决所有这些问题？

Dan Biderman:(07:09)Yeah, that's one thing. The fact that you don't have to research things and re-read things and the fact that you don't have to write like monstrous system prompts. They're all 80. That can give you, you know, two orders of magnitude reduction in token inference consumption. It's not like, you know, 50% or it can be 100x fewer tokens because many things,  especially things that relate To people and teams and organization and priorities,  these are things that you can't really find in one document unless like you really have it really regimented and document everything. These kinds of things the model can kind of implicitly learn by training on some of the data and answer,  you know, within 100 tokens, what the best frontier models would consume 100,000 tokens.


# 2026-06-24-Sequoia Capital-记忆与持续学习：Engram的Dan Biderman和Jessy Lin


Podcast: Sequoia Capital


Episode: Memory and Continual Learning: Engram's Dan Biderman and Jessy Lin


Link: https://app.podwise.ai/dashboard/episodes/8303329


Publish Time: 2026-06-24


Save Time: 2026-07-15


# Summary


AI models currently rely on RAG and context engineering, which are computationally expensive and fail to capture the deep, intuitive understanding required for complex, evolving knowledge work. Engram addresses this by developing "always training" models that utilize adapter fine-tuning to internalize team-specific data directly into model weights. This approach reduces inference token consumption by orders of magnitude while enabling agents to learn from private, bespoke workflows that generic frontier models cannot master. By treating memory as a fundamental component of model architecture rather than an external database, these systems move toward a future where personalized AI agents evolve alongside their users. This shift from static retrieval to continuous, weight-based learning mimics biological memory, allowing models to synthesize complex associations and operate with the efficiency of an experienced employee who deeply understands company initiatives and internal processes.


# Takeaways


Current reliance on context engineering and RAG is a fundamental bottleneck because it fails to build the deep, instinctual understanding of evolving, private, or bespoke team workflows that only weight-based training can provide.


当前对上下文工程和 RAG 的依赖是一个根本性的瓶颈，因为它未能建立对不断演变的、私密的或定制团队工作流程的深刻、本能理解，而只有基于权重的训练才能提供这种理解。

Baking context directly into model weights via adapter fine-tuning can reduce inference token consumption by up to two orders of magnitude compared to relying on massive, repetitive system prompts.


通过适配器微调将上下文直接融入模型权重，可以将推理令牌消耗减少到依赖于大量、重复系统提示的两级数量级。

The traditional computer science separation between "databases" (facts) and "algorithms" (logic) is a false dichotomy in deep learning, as models must internalize specific facts to compose the complex, abstract thoughts required for high-level reasoning.


在深度学习中，计算机科学传统上将 “数据库”（事实）和 “算法”（逻辑）分开，这是一种错误的二分法，因为模型必须内化特定事实，以组合进行高级推理所需的复杂、抽象思维。

True continual learning requires moving beyond static pre-training and test-time retrieval to a model architecture that treats every user interaction as a potential training signal, allowing the model to improve its performance autonomously over time.


真正的持续学习需要超越静态的预训练和测试时间检索，采用一种将每次用户交互视为潜在训练信号的模型架构，使模型能够随着时间的推移自主提高其性能。

A: 标准 RAG 本质上是 “外部化记忆”——它依赖于在测试时搜索文档并将其塞入上下文窗口。虽然我们并不否定 RAG，但我们认为它有局限性：在令牌消耗上成本高，并且它难以建立一名经验丰富的员工在多年中自然发展出的深层次、直观的联系。通过按团队或工作区训练模型，我们可以将该上下文内化到权重中。这使得模型 “只需知道” 一个公司的运作方式，而无需不断地搜索和重读文件，这可以将令牌推理消耗减少多达两个数量级。

Q: Is it possible to truly disentangle "fact memorization" from "skill learning" in large language models?


Q: 在大型语言模型中，是否可以真正将 “事实记忆” 与 “技能学习” 分开？

A: We believe that separating the two is largely a false dichotomy. To compose complex concepts or engage in deep reasoning, a model needs to have internalized some level of foundational knowledge. If you strip a model of its facts, it becomes unnatural and loses its ability to function effectively. The real challenge is not whether to memorize, but how to distinguish what is important to remember versus what is noise. We are trying to build systems that act more like human memory, which is lossy but highly efficient at compressing what is important and discarding what isn't.


Q: What is the "dreaming" analogy in the context of AI memory, and why is it relevant to your development process?


Q: 在人工智能记忆的背景下，“梦境” 类比是什么？它与您的开发过程有什么相关性？

A: In humans, dreaming is a way to experiment with affordances, social situations, and what we can or can't do in the world. We are exploring the idea of giving models "offline" time to retreat from active interactions and experiment with their own capabilities. By letting the model process its own knowledge and test its limits in a simulated environment, it can better internalize what it knows and how it should behave. It’s about moving beyond just reacting to prompts at test time and toward a model that digests its experiences to become more capable the next day.


A: 在人的认知中，做梦是一种实验，探索潜能、社交情境，以及我们能做或不能做的事情。我们正在探索给模型提供 “离线” 时间，让其从主动交互中撤回并实验自身能力的想法。通过让模型处理自己的知识并在模拟环境中测试自身极限，它可以更好地内化自己所知道的内容及该如何行为。这不仅仅是对测试时提问的反应，而是向着一个能够消化自身经历、使其在下一天变得更有能力的模型迈进。

Q: How do you view the role of Engram in the broader AI ecosystem alongside giants like OpenAI or Microsoft?


Q: 你如何看待 Engram 在更广泛的 AI 生态系统中与 OpenAI 或 Microsoft 等巨头的角色？

A: We see ourselves as building the neural interface to the data plane. While frontier labs are focused on building the most powerful generic "brain," we are focused on the "memory" and the "continual learning" that makes that brain useful for a specific company or individual. We aren't trying to replace the frontier models; we are building the infrastructure that allows those models to be deeply integrated into the bespoke, messy, and evolving reality of actual human work. We are the layer that makes the model feel like a long-term employee who truly understands the company's culture and history.


A: 我们视自己为构建数据平面的神经接口。虽然前沿实验室专注于构建最强大的通用 “脑”，但我们专注于使该脑对特定公司或个人有用的 “记忆” 和 “持续学习”。我们并不是试图取代前沿模型；我们是在构建基础设施，使这些模型能够深度融入实际人类工作的定制、复杂和不断变化的现实中。我们就是那一层，使得模型更像是一名真正了解公司文化和历史的长期员工。

# Keywords


|Keywords|Explanation|
|---|---|

|Engram|A research lab focused on the fundamental problems of memory and continual learning in artificial intelligence. They aim to move beyond static models by creating systems that can "always be training" and adapt to new, evolving contexts within a company.|

|Engram|一个专注于人工智能中记忆和持续学习基本问题的研究实验室。他们的目标是通过创建 “始终在训练” 的系统，超越静态模型，并适应公司内的新、不断发展的环境。|

|RAG (Retrieval-Augmented Generation)|A technique where AI models search through external documents to find relevant information before answering a user's question. In the podcast, it is discussed as a common but sometimes inefficient way to provide context, which the guests hope to complement or improve upon by internalizing knowledge directly into the model.|

|RAG (检索增强生成)|一种技术，其中 AI 模型在回答用户问题之前搜索外部文档以找到相关信息。在播客中，这被讨论作为一种常见但有时效率低下的提供上下文方式，嘉宾们希望通过将知识直接内化到模型中来补充或改善这一点。|

# Transcript


## Moving Beyond Static Pre-training to Continuous Model Learning


超越静态预训练的持续模型学习

Current AI models are limited by their reliance on static pre-training and post-training, failing to adapt to evolving, private, or company-specific contexts. The "always training" approach aims to bake new information directly into model weights, similar to how humans internalize experiences. While context engineering and RAG are current stopgaps, they suffer from high inference costs and an inability to form deep, abstract associations. By utilizing adapter-based fine-tuning, models can learn from team-specific data, reducing the need for massive system prompts and enabling more efficient, high-fidelity performance that improves over time.


当前的人工智能模型受限于对静态预训练和后训练的依赖，无法适应不断变化、私密或特定公司的环境。“不断训练” 的方法旨在将新信息直接嵌入模型权重中，类似于人类如何内化经验。虽然上下文工程和 RAG 是当前的临时解决方案，但它们面临高推理成本和无法形成深层、抽象关联的问题。通过利用基于适配器的微调，模型可以从团队特定数据中学习，减少对大量系统提示的需求，并实现更高效、更高保真度的性能，随着时间的推移不断改进。

A: 我们认为将二者分开在很大程度上是一个错误的二元对立。要构成复杂的概念或进行深入的推理，模型需要内化一定程度的基础知识。如果你剥夺一个模型的事实知识，它会变得不自然并失去有效运作的能力。真正的挑战不是记忆与否，而是如何区分什么是重要的记忆内容与什么是噪声。我们正在尝试构建更像人类记忆的系统，虽然是有损的，但在压缩重要内容和丢弃无关内容方面效率极高。

|GitHub Copilot|一个 AI 驱动的编码助手，为软件开发人员提供实时建议和代码补全。它被认为是 AI 在技术领域提高生产力的实际应用中的一个重要里程碑。|

|HBM (High Bandwidth Memory)|A specialized, high-performance memory type used in graphics processing units (GPUs) to handle the massive data requirements of AI models. The podcast notes that managing the storage of large amounts of data in this memory is a major technical challenge for current AI infrastructure.|

|HBM (高带宽内存)|一种专用的高性能内存类型，用于图形处理单元 (GPU)，以处理 AI 模型的大量数据需求。播客指出，管理这种内存中大量数据的存储是目前 AI 基础设施中的一个重大技术挑战。|


Dan Biderman:(02:39)Yeah. And to me, it's like, as an individual, taking notes and having sticky notes is a very valuable thing. We should never discard this. But whenever we get back to business the next day,  we always have some sort of There's a trace of memory in our brain,  some new intuition about how things should be and where should we look. So these two things should come together. And current solutions are more kind of externalized memory. And this has two issues. One is that the amount of tokens we will all collectively,  individually generate is going to be in the tens of millions of tokens per day soon.


AI 模型目前依赖于 RAG 和上下文工程，这在计算上昂贵，并且无法捕捉到复杂、不断发展的知识工作的深层直观理解。Engram 通过开发 “始终训练” 的模型来解决这个问题，这些模型利用适配器微调将团队特定的数据直接内化到模型权重中。这种方法将推理令牌消耗减少了几个数量级，同时使代理能够从私人、定制的工作流程中学习，而通用前沿模型无法掌握。通过将记忆视为模型架构的基本组件，而不是外部数据库，这些系统朝着个性化 AI 代理与用户共同发展的未来迈进。这种从静态检索到基于权重的持续学习的转变模仿了生物记忆，使模型能够综合复杂的关联并以深刻理解公司计划和内部流程的经验员工的效率运行。

Dan Biderman:(05:31)Yeah. And it's not a bet that tools are not there. Like our models always work under the assumption that some knowledge is externalized, some tools are always there. What you need to do is you need to figure out, and that's the hard task,  is what needs to be internalized and what can be externalized. And even for stuff that's externalized, many individuals and companies have their own bespoke tools and ways of doing things. Not everyone has the same, you know, bash CLI tools that, you know,  the frontier models are training on and how to get the models to better understand your bespoke setup,  I think, is its own interesting thing.


是的。而且这并不是说工具不存在的赌注。就像我们的模型总是在某些知识被外部化、某些工具总是存在的假设下工作。你需要做的是找出，且这是困难的任务，什么需要被内化，什么可以被外化。即使是被外化的东西，许多个人和公司都有自己定制的工具和做事方式。并不是每个人都有相同的，嗯，bash CLI 工具，嗯，前沿模型所训练的，以及如何让模型更好地理解你的定制设置，我认为这是一个很有趣的话题。

A: One major challenge is maintaining the right boundaries. We don't necessarily want a model to remember everything across every context—there needs to be a clear separation between personal, work, and public contexts. If a model tries to mix everything, the "memory" becomes flawed and irrelevant. The product form factor of the future needs to provide users with control over what the model remembers and how it applies that knowledge, ensuring that the AI remains a helpful assistant rather than a confusing or intrusive one.


A: 一个主要挑战是保持正确的边界。我们并不希望一个模型在每个上下文中都记住一切——个人、工作和公共上下文之间需要有明确的分隔。如果模型试图将所有内容混为一谈，“记忆” 就变得有缺陷且毫无意义。未来的产品形态需要为用户提供对模型记忆内容及其应用方式的控制，确保人工智能仍然是一个有用的助手，而不是一个令人困惑或侵扰的存在。

|LoRA (Low-Rank Adaptation)|A method for fine-tuning large AI models by updating only a small, specific set of parameters rather than the entire model. This approach allows for efficient customization of models for specific tasks or private company data without requiring massive computational resources.|

|LoRA (低秩适应)|一种通过仅更新一小组特定参数而不是整个模型来对大型 AI 模型进行微调的方法。这种方法允许模型高效地定制以适应特定任务或私人公司数据，而无需大量计算资源。|

|Frontier Models|The most advanced and powerful AI models currently available, typically developed by major research labs. These models serve as the baseline for high-level reasoning, coding, and math, and are often the starting point for further specialized training.|

|Frontier Models|当前可用的最先进和最强大的 AI 模型，通常由主要研究实验室开发。这些模型作为高级推理、编码和数学的基线，通常是进一步专业化训练的起点。|

Sonya Huang:(06:03)And so is the premise then that my Notion agent will be a custom agent that is LoRa fine-tuned or,  you know, some way with an adapter tuned so that it's constantly learning on new content that's added into my Notion workspace? Is that the premise?


While RAG is an effective tool for externalizing data, internalizing knowledge into weights is necessary for models to make autonomous, abstract associations that go beyond simple keyword-based retrieval.


虽然 RAG 是一种有效的数据外部化工具，但将知识内化为权重是模型进行自主、抽象关联所必需的，这超越了简单的基于关键词的检索。

Q: How does Engram’s approach differ from the standard RAG (Retrieval-Augmented Generation) paradigm?


Q: Engram 的方法与标准的 RAG（检索增强生成）范式有何不同？

A: Standard RAG is essentially "externalized memory"—it relies on searching through documents and stuffing them into a context window at test time. While we don't discard RAG, we believe it has limitations: it is expensive in terms of token consumption, and it struggles to build the deep, intuitive associations that an experienced employee naturally develops over years. By training models per team or workspace, we can internalize that context into the weights. This allows the model to "just know" how a company operates, rather than needing to constantly search and re-read files, which can reduce token inference consumption by up to two orders of magnitude.


Q: What is the "holy grail" for the future of AI-driven knowledge work?


Q: AI 驱动知识工作的未来的 “圣杯” 是什么？

A: The ideal future is one where you go to work, generate immense value, and the model learns your unique way of doing things, your inventions, and your workflows. Crucially, we want to solve the problem of how to carry those skills with you to your next role in a way that is sanitized, ethical, and respects intellectual property. We want to move toward a world where each of us has a personalized model that acts as a neural interface to the data plane—a system that is associative, efficient, and deeply aligned with our personal and professional growth.


A: 理想的未来是您去上班，创造巨大的价值，模型学习您独特的工作方式、您的发明和工作流程。至关重要的是，我们希望解决如何将这些技能携带到下一个角色的问题，以一种无污点、伦理和尊重知识产权的方式。我们希望朝着一个世界发展，在那里我们每个人都有一个个性化的模型，作为数据平面的神经接口——一个联想、有效并与我们的个人和职业成长深度对齐的系统。

|KV Cache (Key-Value Cache)|A data structure used in AI models to store intermediate computation results during the process of generating text. By caching these values, the model avoids re-calculating everything from scratch, which speeds up performance but consumes significant memory on graphics processing units.|

|KV Cache (键值缓存)|一种数据结构，用于在生成文本过程中存储中间计算结果。通过缓存这些值，模型避免了从头开始重新计算所有内容，从而加快了性能，但在图形处理单元上消耗了大量内存。|

|Continual Learning|The ability of an AI system to keep learning and updating its knowledge over time as it encounters new information. This is a core focus of the guests, who argue that models should be able to integrate new experiences into their "weights" rather than relying on external lookups.|

|Continual Learning|AI 系统随着遇到新信息而不断学习和更新知识的能力。这是嘉宾们的核心关注点，他们认为模型应该能够将新经验整合到它们的 “权重” 中，而不是依赖外部查找。|

那么也许可以开始，Engram 网站上说，我们不是通过预训练或后训练的视角看待世界。我们的模型始终在训练中。这是什么意思？

Jessy Lin:(01:09)So I think like models today obviously know a lot of things. They're incredibly smart. But we kind of think the bottleneck for making these models more useful these days is not really raw intelligence,  but understanding like new and evolving context. So whether it's like, you know, a new task that you're doing or a particular context for,  you know, like a job or something like this. How do you bake that into the model weights the same way that, you know,  pre-training and post-training bakes into the model weights very deeply? And this is kind of why we think of ourselves as working on these fundamental problems of memory and continual learning,  which are really two sides of the same coin.


所以我认为如今的模型显然知道很多事情。它们非常智能。但我们认为使这些模型在当今更有用的瓶颈并不是真正的智力，而是理解新出现的上下文。所以无论是您正在进行的新任务，还是某个特定的上下文，比如工作或类似的事情。您如何将这些因素与预训练和后训练一样，深刻地融入模型权重中？这正是我们认为自己致力于解决记忆和持续学习这两个基本问题的原因，这实际上是同一枚硬币的两面。

(01:46)How do you make the models learn new things and bake them deeply into the weights of the model?


您如何让模型学习新知识，并将其深深融入模型的权重中？

Sonya Huang:(01:51)And is your premise then that memory as a separate database or separate You know,  thing that you've shoved into the context window is not true memory and it's not true continual learning.


那么您的前提是，作为单独数据库或您放入上下文窗口的其他内容的记忆不是真正的记忆，也不是持续学习。

Dan Biderman:(06:30)We need white, you know, we need white box access to the weights, right? So, you know, we can partner with companies that have, you know, closed source weights and do this with them. But it's easiest for us to do it with open source models. But any model that's a transformer model, we can do our thing to it.


我们需要白盒访问权对权重，对吧？所以，您知道，我们可以与拥有闭源权重的公司合作，和他们一起做这个。但对我们来说，使用开源模型最简单。但任何变换器模型，我们都可以对其进行处理。

Sonya Huang:(06:49)And what's the trade-off then when people are comparing the before and after using you? Is it that they're no longer sending so much context? And so the trade-off is like you burn more compute upfront to learn your company's way of doing things into the weights and then you're sending less context to the model on every inference pass? Is that the rough trade-off?


Q: Why do you believe the language-centric approach has dominated over vision in the current AI boom?


Q: 为什么你认为以语言为中心的方法在当前 AI 热潮中占主导地位？

Jessy Lin:(00:00)What about pre-training or even post-training makes it possible for the models to generalize in these magical emergent ways and controlling that process so that a company has a set of private data? How do we make the models learn that just as well as the models know like the capital of France or,  you know, like how to write Python? So I think it's a really fun problem to think about.


预训练或后训练中的哪些因素使模型能够以这种神奇的方式进行概括，并控制这一过程，以便公司拥有一组私有数据？我们如何让模型学习得和它们知道法国首都或者如何编写 Python 一样好？所以我认为这是一个非常有趣的问题值得思考。

Unknown Speaker:(00:32)Thank you for watching.


谢谢观看。

Jessy Lin:(02:01)I think all of these tools will kind of come together. So these days, like the way that people are solving these problems is with context engineering. So you take like a huge prompt, maybe you like We keep talking to the model over many,  many turns and hours and reorganize the context to better understand what you're trying to do. And we think these kinds of things like tool use, context engineering will play a part. But I think an underleveraged tool these days is using the same kind of training pipeline or framework or kind of workflow that the Frontier Labs are using to make these models really good at frontier math or code,  but applying that to every kind of domain, every kind of context that you have,


我认为所有这些工具会结合在一起。如今，人们解决这些问题的方式是通过上下文工程。您可以采取大量提示，可能您会与模型进行多次交互，并重新组织上下文，以更好地理解您要做的事情。我们认为这些工具使用和上下文工程将发挥重要作用。但我认为现在一个未被充分利用的工具是使用与前沿实验室相同的训练管道或框架，或者类似的工作流程，使这些模型在前沿数学或代码方面表现出色，但将其应用于您拥有的每种领域和上下文，

(02:38)let's say in a company.


比如在一家公司中。

是的。我的意思是，从高层次看，我们想做的是把任何上下文拿出来，比如说，这些不同的工作空间。所以我们正在与像 Notion、Microsoft 和 Harvey 这样的合作伙伴合作，他们有这些地方，人们在这里进行大量的长期工作。上下文有很多，包括你们团队已经写好的文件，还有人们现在在这些产品中与这些代理进行越来越多的互动、对话并给予反馈。以及找出如何构建一个能够深入理解这些上下文的模型。所以不仅仅是在测试时阅读文件，而是像在你公司工作多年的员工那样真正理解它。

(04:15)So you kind of understand at a high level, oh, these are the initiatives across the company. This is the way that we do things. You've studied like how to run the hiring pipeline or how to, you know,  do this kind of thing within the company and can operate just as well as like any anybody else can in the company. And so what we're doing is training per team models within these workspaces that deeply understand those contexts and can improve with time on the things that people care about.


这样你就能在高层次上理解，哦，这些是公司范围内的倡议。这是我们做事情的方式。你已经研究过如何运行招聘流程，或者如何在公司内部做这种事，能像公司里的其他人一样有效地工作。所以我们正在做的是在这些工作空间中为每个团队训练能够深入理解这些上下文并随着时间推移改进人们关心的事物的模型。

A: 有一种理论认为，在生物学中，视觉具有巨大的比特率优势，通过眼睛处理光学数据的速度远远超过声音。然而，在数字世界中，一切都是电子的。我们基本上通过将一切搬入令牌和嵌入的范畴，平等化了竞争环境。尽管语言是一种人工且高维的构造，但它已被证明是一种极其有效的抽象媒介。尽管视觉和语言最终会统一成一种多模态系统，但语言已提供了更直接和可扩展的途径，通向我们在当前模型中看到的 “智能”。

Q: What is the biggest risk or challenge in creating personalized models for individuals?


Q: 创建个性化模型的最大风险或挑战是什么？

|Transformer|The underlying architecture that powers almost all modern large language models. It uses an "attention" mechanism to process information, allowing the model to understand complex relationships between words in a sequence.|

|Transformer|几乎所有现代大型语言模型的基础架构。它使用 “注意力” 机制来处理信息，使模型能够理解序列中单词之间的复杂关系。|

|Amos Tversky|A renowned cognitive psychologist and mathematician known for his influential work on human decision-making and judgment. He is mentioned in the podcast to highlight the distinction between artificial intelligence and the study of human cognitive processes.|

|Amos Tversky|一位著名的认知心理学家和数学家，以其对人类决策和判断的影响力工作而闻名。他在播客中被提及，以突出人工智能与人类认知过程研究之间的区别。|

|GitHub Copilot|An AI-powered coding assistant that provides real-time suggestions and code completion for software developers. It is cited as a significant milestone in the practical application of AI for increasing productivity in technical fields.|

# Highlights


(01:14) The bottleneck for making models more useful is not raw intelligence, but understanding new and evolving context.


使模型更有用的瓶颈不是原始智力，而是理解新的和不断发展的背景。

(09:56) Human memory is lossy, because part of the feature of intelligence is compressing what is important and separating that from what is not.


人类记忆是有损的，因为智力的一个特性是压缩重要信息，并将其与不重要的信息分开。

(11:43) The magic of deep learning is that databases and algorithms are now mushed together, and we need to break them apart to truly understand them.


深度学习的魔力在于数据库和算法现在被紧密结合在一起，我们需要将它们分开以真正理解它们。

(30:52) Gradient descent is a proof of existence that you can pack a massive amount of information into very few numbers.


梯度下降证明了你可以将大量信息压缩成非常少的数字。

是的。在我看来，对我个人来说，记笔记和使用便条纸是非常有价值的事情。我们绝不能忽视这一点。但每当我们第二天回到工作时，总会有一些我们的脑海中留存的记忆痕迹，一些关于事情应该如何以及我们应该关注什么的新直觉。所以这两件事情应该结合在一起。而当前的解决方案更像是外部化的记忆。这有两个问题。一个是我们每个人共同生成的标记数量，未来很快就会达到每天数千万个标记。

(03:13)So just keeping it and searching through it is going to be and rereading it's going to be pretty expensive,  but it's going to also be pretty hard,  pretty confusing for the models unless we have major,  major breakthroughs.


所以仅仅是保留和搜索这些东西，以及重新阅读它们将会是非常昂贵的，也会很困难，对模型来说会非常混乱，除非我们有重大的突破。

那么，前提是我的 Notion 代理将是一个定制代理，这是 LoRa 微调的，或者说，某种方式通过适配器调优，以便它不断学习添加到我的 Notion 工作区的新内容？这是前提吗？

Dan Biderman:(06:19)Yeah,  and they're working with many models and they're the early users of all the Frontier models and they're probably going to keep doing that.


是的，他们正在与许多模型合作，他们是所有前沿模型的早期用户，他们可能会继续这样做。

Sonya Huang:(06:26)Does this approach work on the Frontier Models or the closed Frontier Models?


这种方法在前沿模型或闭源前沿模型上有效吗？

Current KV caching methods are highly inefficient, often requiring gigabytes of HBM memory to represent small amounts of information that could be compressed into a fraction of the space through weight-based training.


当前的 KV 缓存方法效率极低，通常需要数 GB 的 HBM 内存来表示少量信息，而这些信息可以通过基于权重的训练压缩到更小的空间中。

The future of AI will likely shift from a single, monolithic frontier model to a landscape of personalized, team-specific models that retain private, proprietary knowledge while evolving alongside the user's unique workflow.


未来的人工智能可能会从单一的、整体的前沿模型转变为个性化的、团队特定的模型，这些模型在随着用户独特工作流程的演变而保留私密的、专有的知识。

Human memory is inherently lossy and associative, serving as a model for AI development; the ability to compress and prioritize information is a core feature of intelligence rather than a limitation.


人类记忆本质上是有损和关联的，作为人工智能发展的模型；压缩和优先处理信息的能力是智能的核心特征，而非限制。

# Q & A


Q: Why is "raw intelligence" no longer the primary bottleneck for AI, and what is the real challenge Engram is trying to solve?


Q: 为什么 “原始智能” 不再是人工智能的主要瓶颈，而 Engram 试图解决的真正挑战是什么？

A: While current models are incredibly smart, they are essentially static. The real bottleneck for making these models useful in a business or professional context is their inability to understand evolving, private, or bespoke contexts. We don't see the world through the lens of just pre-training or post-training; we believe models should be "always training." The goal is to bake specific company contexts, workflows, and team-level knowledge directly into the model weights, just as deeply as frontier labs bake in general knowledge like Python or geography.


A: 虽然目前的模型非常智能，但它们本质上是静态的。使这些模型在商业或专业环境中有用的真正瓶颈是它们无法理解不断变化的、私密的或定制的情境。我们并不总是通过预训练或后训练的视角来看待世界；我们认为模型应该是 “持续训练” 的。目标是将特定公司的情境、工作流程和团队级知识直接融入模型权重中，就像前沿实验室将通用知识如 Python 或地理知识深度融入其中一样。

Q: How does Engram handle the technical implementation of "continual learning" for specific workspaces?


Q: Engram 如何处理特定工作区的 “持续学习” 的技术实现？

A: We utilize a variety of adapter-based fine-tuning techniques—such as LoRAs, prefixes, and sparse architectures—to update model weights continuously. The core challenge is determining what data serves as a useful training signal. We take raw documents, team interactions, and feedback loops and transform them into training data that allows the model to improve over time. It’s about creating a tight, integrated loop between research and product, where the model learns from actual user feedback in the real world rather than just being a static artifact thrown over a fence from a research lab.


A: We are as "bitterless and pilled" as anyone else. We believe in the power of scaling compute and training on data. However, we think the "bitter lesson" applies to our work as well: we want to burn more compute on new context that the model hasn't seen before. The frontier labs are focused on a single, massive AGI model, but we believe there is a massive opportunity in creating smaller, bespoke models that are highly optimized for specific human or organizational contexts. We aren't betting against the frontier; we are betting that there is a different, highly valuable path for personalized, continually learning models.


A: 我们像其他人一样 “毫无痛苦和烦恼”。我们相信扩展计算和使用数据进行训练的力量。然而，我们认为 “苦涩教训” 也适用于我们的工作：我们希望在模型以前未见过的 * 新 * 上下文上消耗更多计算。前沿实验室专注于一个单一的、庞大的 AGI 模型，但我们相信创建更小的、为特定人类或组织情境高度优化的模型存在巨大的机会。我们并不是在对抗前沿；我们是在下注，认为为个性化、持续学习模型找到不同且高度有价值的道路。

A: There is a theory that in biology, vision has a massive bit-rate advantage, processing optical data through the eye at a scale far beyond sound. However, in the digital world, everything is electronic. We have essentially leveled the playing field by moving everything into the domain of tokens and embeddings. Language, despite being an artificial and high-dimensional construct, has proven to be an incredibly effective medium for abstraction. While vision and language will eventually unify into a multimodal system, language has provided a more direct and scalable path to the "intelligence" we see in current models.


Sonya Huang:(00:41)Welcome to Training Data. We are delighted to have Dan Biderman and Jessy Lin, co-founders of Engram today. Engram is a Neolab focused on memory and continual learning and two of the hottest topics in all of AI research today. And Shaun and I are delighted to dig in on those topics with you today.


欢迎来到训练数据。我们很高兴今天能请到 Engram 的联合创始人 Dan Biderman 和 Jessy Lin。Engram 是一个专注于记忆和持续学习的 Neolab，涉及当前所有人工智能研究中两个最热门的话题。Shaun 和我很高兴今天能和你一起深入探讨这些话题。

Dan Biderman:(00:57)Awesome. Great.


太棒了。很好。

Sonya Huang:(00:59)So maybe to kick off, the Engram website says,  we don't see the world through the lens of pre-training or post-training. Our models are always training. What does that mean?


Sonya Huang:(03:23)Tens of billions of tokens for Shaun.


对于肖恩来说是数百亿个标记。

Dan Biderman:(03:25)That's good.


这很好。

Shaun Maguire:(03:27)Depends on the day.


这要看那天的情况。

Sonya Huang:(03:29)Could you maybe tell us a little bit about the Engram architecture, the Engram product and how it works?


你能不能告诉我们一点有关 Engram 架构、Engram 产品及其工作原理的事情？

Jessy Lin:(03:35)Yeah. I mean, at a high level, I think what we're trying to do is Take any context,  like there's all these different workspaces, let's say. So we're working with partners like Notion and Microsoft and Harvey that have these places where people are doing a lot of work over a long period of time. There's all this context, both in terms of like, you know,  documents that you've already written as a team,  as well as like now people are interacting with these agents more and more in these products or having conversations,  giving them feedback. And figuring out how to have a model that deeply understands that context. So not just reading the files at test time,  but really understanding it the way that an employee that's worked at your company for years has.


(04:43)So the way that we do this at like a technical level maybe is training these into weights so we do a lot of like adapter fine tuning so adapters of many types like I think people have looked into this for decades at this point,  like whether it's Laura's or prefixes or. You know sparse architectures. I think like all of these tools are at our disposal, and then figuring out what the right data is. So,  how do you turn any kind of raw like document or interaction into useful training signal for the model so again we have like a variety of tools now like Supervised fine-tuning,  you know, RL, you know, on-policy distillation, like all of these things that, you know,  the field has kind of developed and trying to fit these pieces together into a model that learns continuously on the things that people care about.


那么当人们比较使用你的前后，权衡是什么？他们是不是不再发送这么多上下文？所以权衡就像你在前端烧更多计算能力来学习你公司的做事方式，然后在每次推理中向模型发送更少的上下文？这是粗略的权衡吗？

所以我们在技术层面上做到这一点的方式可能是将这些训练成权重，我们进行大量的适配器微调，因此许多类型的适配器，比如我认为人们在这一点上研究这个已有几十年了，无论是 Laura 的还是前缀的。你知道稀疏架构。我认为这些工具都在我们手中，接下来需要弄清楚正确的数据是什么。所以，你如何将任何原始的文档或互动转化为对模型有用的训练信号，我们现在有多种工具，比如监督微调，还有强化学习、在线蒸馏，所有这些东西，都是这个领域逐渐发展出来的，并试图将这些部分整合成一个持续学习人们关心的事物的模型。

Dan Biderman:(14:19)Yeah, I have one example. Maybe Jessy can give another one. A hypothetical one, for example, imagine one of the AI labs say OpenAI has to win some math Olympiad in a week time from now. Would they construct a catalog of all the math textbooks and really have People annotate which chapters to get and which graphs to see or will they actually collect this,  synthesize some training data, launch a training job, see where it lands in five,  six days, start evaluating it. And stuff like that. So it's obvious for anyone who's trained models that there's superior way to integrate across the ideas and capabilities and involves this kind of magic of training.


是的，我有一个例子。也许 Jessy 可以再给一个。一个假设的例子，比如想象一下，某个 AI 实验室，比如 OpenAI，必须在一周内赢得某个数学奥林匹克。他们会构建一个所有数学教材的目录，真的让人们标注哪些章节需要获取，哪些图表需要查看，还是会实际收集这些，合成一些训练数据，启动训练任务，看看在五、六天后结果如何，开始评估它。还有其他类似的事情。对于任何训练过模型的人来说，显然有更优的方法来整合各种想法和能力，涉及到这种训练的魔力。

Jessy Lin:(18:50)I think it's obviously one of the grand challenges in AI. I think everybody's talking about it these days because the models are so smart. What else is left? I think learning at the edges, learning the remainders of what makes these models useful. It's not just about raw intelligence anymore. It's about learning new things. And I think it also feels very fundamental because it kind of goes back to really understanding what makes the model so good. So right now the models kind of incidentally know a lot of things from pre-training and we don't really understand why. It's like the internet was just, you know,  this gift granted to us where there's like a diverse set of data that contains like all of these different examples of coding and like writing and all these other things.


Sonya Huang:(20:07)And Dan, you came from the neuroscience world, is that right?


丹，你是来自神经科学界，对吧？

Dan Biderman:(20:10)Yes, yes. I was initially interested in questions around consciousness and the human condition and things like that.


是的，是的。我最初对意识和人类状况等问题感兴趣。

Sonya Huang:(20:17)Are the models conscious?


模型有意识吗？

Dan Biderman:(20:18)I don't have any advanced thoughts on this more than you and Reid. I don't think so, but it's important that smart people are thinking about it. I would say I was interested in how humans think, how humans perceive. And as Amos Tversky, the Israeli psychologist, used to say, he's not interested in artificial intelligence. He's interested in natural stupidity. So I would say I started kind of similarly trying to see how people and animals experience the world. Gradually, you know, my inclinations took me to the stats and AI domains. And there I figured that so many of the same problems of memory and continual learning are really, really urgent.


这是一个更哲学性的问题。你提到在大脑中，有许多不同的房地产是不同的，共处理单元，等等，现代计算机架构中有 CPU、GPU，你知道，还有内存，不同的协处理器。在《苦涩教训》中，你认为发生的事情是，像 LLMs 这样的东西， converged 为一个完全主导的协处理器。就是所有计算都将在你知道的 GPU 等效的语言模型中发生。还是你认为这些模型在模型内部以某种方式构建了一堆协处理器？

(22:31)And take with memory, do you think that The models themselves will just build,  you know,  whatever part of the brain equivalent would be that's good at memory or do you think there needs to be like another standalone architecture?


而提到记忆，你认为模型本身会构建出，任何与记忆相关的脑部等效区域，还是你认为需要另一个独立的架构？

是的，这是一方面。你不必研究事情和重读事情，以及你不必写像怪物般的系统提示的事实。它们都是 80。这可以让你，嗯，减少两个数量级的令牌推理消耗。这不是说，嗯，50% 或者可以少 100 倍的令牌，因为许多事情，尤其是与人和团队、组织及优先事项相关的事情，这些东西你真的很难在一个文档里找到，除非你真的将它们系统化并记录所有内容。这些模型通过在一些数据上训练，能够隐性地学习到这些事情，并在 100 个令牌内回答，什么是最佳前沿模型所消耗的 100,000 个令牌。

(07:51)So these kinds of examples are interesting. And also the quality, you know, there are tasks that are,  you know, not supernatural for the current generation of the models and we kind of think there's going to be consistently this gap of like Three to six months ahead where there's certain things that are bespoke that people are just exploring. The models are not fully great for them. The models will at some point be great for them. But if you can autonomously learn in a very lightweight way,  it will give value in that time in terms of capabilities.


所以这些例子很有趣。而且质量，你知道，目前一代模型有些任务并不是超自然的，我们认为将会持续存在三到六个月的差距，某些定制的事情人们还在探索中。这些模型对他们来说并不是完全优秀。这些模型在某个时候会对他们很棒。但是如果你可以以非常轻量的方式自主学习，它在能力方面会在那个时候带来价值。

Sonya Huang:(08:19)Why train on the workspace level versus the individual level, for example?


为什么要在工作区级别进行训练，而不是个人级别，例如？

但是，记忆是有损的，因为智能的一个特征是压缩重要的内容，并将其与不重要的内容分开。所以我认为你不能真的将事实学习与非事实学习或技能学习分开，正如一些人所希望的那样。比如，如果你拿一个模型，有些人在模型中做过这种事情，将所有的事实剔除，只保留纯粹的核心或类似的东西。这作为模型很不自然。它不知道基本的东西。你需要这些。但是我认为……。

Sonya Huang:(10:33)Why do you need that? Like, why can't you look up facts and then just have...


你为什么需要这些？比如，为什么不能查找事实，然后再……。

(17:08)And definitely all of them are thinking about memory and all of them are thinking about continual learning. It's just more of a product kind of effort right now. We think it deserves its own attention. We think breakthroughs need to happen there and Demis and the Sequoia event about a month ago said pretty clearly that we need new breakthroughs around these topics and obviously they're thinking about them. We're just focusing exclusively on this. And we think certain things around incentives of where the data is and who owns the model are pretty interesting. So if you could learn from many humans or organizations at scale without necessarily sending someone to work with them shoulder to shoulder,  that would be a pretty big unlock.


他们肯定都在考虑内存问题，所有人都在考虑持续学习。现在这更多的是一种产品努力。我们认为它值得独立关注。我们认为在这些领域需要取得突破，Demis 和大约一个月前的 Sequoia 事件明确表示，我们需要在这些主题上进行新的突破，显然他们正在考虑这些问题。我们只是专注于这个。我们认为关于数据位置和谁拥有模型的某些激励因素非常有趣。所以如果你可以在不必派人去与他们肩并肩工作情况下从许多人或组织中进行规模学习，那将是一个巨大的解锁。

我认为如果你看看模型的思维方式，如果你需要回忆基本事实以便继续思考，那你根本走不了多远。也许这是一种高层次的直觉，但这也是我们认为训练非常重要的原因之一。为了能够对事物进行更复杂、更深入的思考，你需要内化一些东西，以便将它们组合成更抽象的概念。

Dan Biderman:(11:00)And there have been efforts before that were hard to scale to try and,  you know, disentangle the two and pre train the models in a way that's,  you know, allows it to retrieve and search for things and not internalize them. It's just the recipe we know to hill climb on collectively right now, is this,  you know, fact pre training step. And I think the magic of The mystery of this approach is that, you know,  traditionally in CS we would have, you know,  databases as its own curriculum and we would have algorithms and the databases is like facts about the world and capitals of whatever,  store them, query them.


之前也有努力想要尝试分离这两者，并以某种方式预训练模型，这样可以检索和搜索内容，而不需要内化它们。我们现在所知道的集体的高峰攀登的食谱是，这个事实预训练步骤。我认为这一方法的神秘之处在于，传统上在计算机科学中，我们会有，数据库作为它自己的课程，我们会有算法，数据库就像是关于世界的事实和首都，存储它们，查询它们。

还有如何高效地操作信息和获取某些答案的算法。以样本高效的方式。我认为深度学习的魅力在于这两件事情现在被揉在了一起，我们需要所有这些聪明的人和人类可解释性来尝试将它们分开。我认为我们现在在人工智能纳入经济中的许多现象表明，这些东西正在逐渐再次分离，即公司拥有自己的上下文，并且确实小心处理它们并精心设计它们。而一个与这些上下文完全陌生的通用模型正在对它们进行操作。但对我们来说，很明显。

(12:12)There needs to be a certain convergence, at least with some cadence,  where the facts and the stories and the details are getting mixed into the model. It has disadvantages as well, because if you have to, you know, capitals of countries are,  you know, they can change, but it's not very frequent. But there's many other facts that are changing all the time. And just imprinting them into weights is a challenging thing to do.


至少需要有一定程度的融合，以某种节奏，将事实、故事和细节混合到模型中。这也有缺点，因为如果你必须知道，国家的首都是，你知道，它们可能会改变，但并不是很频繁。但是还有很多其他的事实是不断变化的。而将它们直接印刷到权重中是一个具有挑战性的事情。

Sonya Huang:(12:35)I see. So you're saying it's a false dichotomy that's trying to separate Algorithms from databases here. What really matters is like how to distinguish what's important to remember versus what's not important.


我对这个问题没有比你和瑞德更深的见解。我不这么认为，但聪明的人在思考这个问题很重要。我会说我对人类如何思考、如何感知感兴趣。正如以色列心理学家阿莫斯·特沃斯基曾经说的，他对人工智能不感兴趣。他对自然的愚蠢感兴趣。所以我会说，我开始时类似于想看看人类和动物如何体验世界。逐渐地，你知道，我的倾向带我进入了统计和人工智能领域。在那里我发现，许多记忆和持续学习的问题都是非常迫切的。

(20:54)And the kind of solutions we have in the current systems are pretty far from what we have in biology. And I'm not one of these people who would say that the machine should be like,  you know, like the animal or the human brain. I don't think so. There's many things computers can do better than us. But human memory has these, like, very different things in it. It's, you know, if you want to store a whole code base or you can use a computer,  you don't even need AI on the computer to store everything losslessly and just get it. The human brain evolved to work in these constraints of, you know,  information capacity and to have these fuzzy representations that can then,


(21:30)you know, be abstracted and form connections and form the next day. Current systems don't really have that beyond the generic pre-training step. And I was really interested in, you know, what are ways to build that in? What are ways to learn from that?


Sonya Huang:(22:46)Yeah, like is memory an emergent property?


是的，记忆是一种涌现属性吗？

Shaun Maguire:(22:49)Exactly. And almost everything. Like is everything that we need in intelligence will just be emergent with Better training data and more scaled compute.


正是如此。以及几乎所有的东西。就是我们在智能中所需的一切都会随着更好的训练数据和更大的计算能力而涌现出来。

我们只是认为有更多的计算可以扩展。如果我真的想理解肖恩和肖恩在肖恩的上下文中的工作，就像重新阅读文件一样，这一点并不够，尤其是对于像你这样特别的人。

Sonya Huang:(24:39)What are you finding that people care most about their models learning? Like, is it memorizing facts about the organization? Is it remembering like, ah, no, we do CI this way? Is it like, what are people actually hoping to? And then maybe this feeds into how you do the ranking of memory slots and all that.


## Disentangling Fact Memorization and Skill Acquisition


理清事实记忆与技能获取

Separating fact memorization from skill learning is a false dichotomy, as models require internalized knowledge to compose complex, abstract concepts. Current AI development often treats facts as external databases, but true intelligence requires compressing important information into weights to facilitate deeper reasoning. The "dreaming" phase—where models retreat from active interaction to experiment with affordances—is a missing component in current pipelines. By focusing on team-level models rather than generic AGI, it is possible to create systems that learn from ambiguous, private, or conflicting data, bridging the gap between research and real-world product deployment.


Dan Biderman:(13:21)Yeah. And what are dreams? Dreams are pretty crazy things to say we want to build an AI. That's like our dreams sounds a little bit like a nut thing to do. There's not a lot of coherence there. But what's interesting there is like What happens in our dreams, we see things,  we talk to ourselves,  and we experiment with the affordances of what can we do and can't we do in the world and social situations and,  you know, any, any, it's heavily biased towards social stuff, right? So for us to with things we're building is, you know,  you We give the models the time to then go back,  retreat from the actual interaction and experiment with its affordances. What can it do in an environment? What does it know?


是的。那么什么是梦想？梦想是相当疯狂的事情，我们想要构建一个人工智能。这就像我们的梦想听起来有点疯狂。这里面没有太多的连贯性。但有趣的是，在我们的梦中，我们看到事物，与自己交谈，并且我们尝试体验我们在世界和社交场合中可以做和不能做的事情，你知道的，这些内容在社交方面非常偏向，对吧？对我们来说，正在构建的事情是，我们给模型足够的时间，然后再回去，退回到实际互动中，探索它的能力。它在环境中可以做些什么？它知道些什么？

(14:56)And we are clear that this has to happen in those high stake domains of math and coding and cyber and stuff. We just think much of this magic can actually end up in the hands of many more people in interesting ways.


我们很清楚，这必须发生在高风险的数学、编码和网络等领域。我们认为这许多魔法实际上可以以有趣的方式交到更多人的手中。

(15:46)And I think a lot of these things we're already seeing are hard to train into the models with the same tools that we have used for like decades in machine learning,  which is like, you have really clean supervision, you have like ground truth reward signals,  and you like create a nice environment and you like train the model to like use the tools to better accomplish this like coding task. And instead, a lot of the things that actually happen out in the world are very ambiguous,  or like, It's hard to say like what makes something good.


我认为我们已经看到的许多问题，用我们在机器学习中几十年来使用的相同工具来训练模型是很困难的，那就是，你有非常干净的监督，你有真实的奖励信号，你创建一个良好的环境，然后训练模型使用这些工具更好地完成这个编码任务。而相反，实际上在世界上发生的很多事情都是非常模糊的，或者说，很难说什么才算是好的事物。

(16:18)And so I think a lot of these things are very specific to individuals and I think very kind of misaligned or not very aligned with how the Frontier Labs think about the whole training pipeline and what kind of models will exist in the longer term.


所以我认为很多这些事情都是非常特定于个人的，我认为与 Frontier Labs 对整个训练流程的看法不太对齐，或者说不太一致。

Dan Biderman:(16:32)Yeah, and to add to it, I think, you know, what is the P0 for the Frontier Labs? And some of you here are pretty close with them. It's getting to AGI,  getting this one generic model that's extremely capable in coding and math and then using it to automate the economy or to solve really hard,  you know, long-term problems in cryptography and defense or whatever. And it's pretty clear what needs to happen. To push this, you know, more pre-training, bigger models, more data, more RL, more inference time compute,  that kind of stuff. That's P0. That's where the majority of expenditure and talent goes.


你知道，被抽象、形成连接并构成下一天。当前的系统在通用预训练步骤之外没有这种特征。我对如何将其构建进去非常感兴趣。有哪些方法可以从中学习？

Shaun Maguire:(21:44)This is more of a philosophical question. You know, you mentioned in the brain, there's a bunch of different Real estate is different,  coprocessing units, whatever, modern computer architecture, there's CPUs, GPUs, you know, memory, there's different coprocessors. With The Bitter Lesson, do you think that what's happening is that, like, LLMs are,  you know, converged to say like one coprocessor that's just totally dominant. It's like everything, all compute is going to happen in, you know, the GPU equivalent of like a language model. Or do you think that these models are kind of building a bunch of coprocessors,  like, you know, emergently inside the model?


是的，我会说就当前人工智能的部署来看，它远不止于 GPU，我们看到了所有这些，沙盒爆炸和模型在其他计算机上尝试的情景。

Shaun Maguire:(23:11)I'm learning on the model architecture level rather than on the...


我在模型架构层面上学习，而不是...

Dan Biderman:(23:15)So other experiments, there have been many previous experiments on different architectures that we contributed to,  like the state space family and others to try and handle Very, very long context more efficiently. The thing with all these methods, it ends up being a trade-off, usually a trade-off between memory and accuracy. And memory not in the behavioral cognitive sense, memory in the computer sense, right? Instead of having, you know, the memory footprint of the transformer attention, which is quadratic in the sequence length.


所以其他实验，之前对不同架构的许多实验我们都有参与，例如状态空间家族等，旨在更有效地处理非常非常长的上下文。所有这些方法的关键在于，最终都是取舍，通常是在记忆和准确性之间的取舍。记忆并不是指行为认知意义上的记忆，而是计算机意义上的记忆，对吧？而不是有你知道的变压器注意力的内存占用，这是与序列长度的平方成正比的。

Shaun Maguire:(23:44)Some are claiming, you know, they have sub-quadratic.


有些人声称他们的占用是亚平方的。

Dan Biderman:(23:47)Yeah, some do have it, right? And some of the best Chinese model have layers that are, you know,  inspired by those state space architectures and are,  you know, not quadratic in cost. Thing is, is that in our hands, we find that, you know, you always compromise accuracy for this memory. There's no free lunch. And what we're saying is like, look, if you're really bitterless and pilled,  what do you want to do is you want to think,  how can I burn more compute? And how can I burn it on, you know, new context that I have not seen before. So we're as bitterless and pilled as anyone else. And we are not betting that the overall direction of AGI is going to, you know, end anywhere soon.


你发现人们最关心他们的模型学习什么？是记住有关组织的事实吗？是记得：哦，我们以这种方式进行 CI 吗？是这样的，实际上人们希望得到的是什么？然后这可能影响到你如何对记忆槽进行排序之类的。

Jessy Lin:(25:02)Yeah, well, I think if you look at what people are spending their time in the app layer doing these days,  it's a lot of just trying to make the model work well for your use case. Like, oh, I want the model to like, Let's say, design my website with my brand style. That's a very common example these days. But there's many kinds of different tasks that people do with agents,  like learning how to run a workflow or your particular way of writing,  let's say. So there's many, many kinds of things. And honestly, I think when we think about these methods,  Kind of going back to this distinction between like facts and skills,  there really is none. I think the methods are kind of agnostic to that.


Shaun Maguire:(15:09)Like why isn't it Just the foundation model labs that own the end product here. How do you go between giants?


为什么这里只是基础模型实验室拥有最终产品呢？如何在巨头之间转换？

Jessy Lin:(15:18)Yeah, so I think the worldview that we have is a bit different from the Frontier Lab worldview,  where it's like, we want one model that's bigger and bigger,  that's more and more intelligent across a variety of domains. Instead, how we see it, we kind of imagine this world where everybody has their own model. A lot of the things that people want to learn are either private,  like things that will never see the light of day in a post-training dataset,  or even conflicting, like, oh, the way that I want to do the task is different from how another company or another individual wants to.


是的，我认为我们的世界观与前沿实验室的世界观有些不同，他们想要一个越来越大的模型，一个在各种领域中越来越智能的模型。相反，我们的看法是，我们想象一个每个人都有自己的模型的世界。很多人想学习的东西要么是私密的，比如在训练后的数据集中永远不会被公开的内容，要么是相互冲突的，比如，我想做某个任务的方式与另一家公司或个人的方式不同。

也许另一个观点是，我认为很多事情在世界上需要看起来不同。首先需要有新的研究突破。其次是新的训练基础设施，比如说，为每个人提供小型模型而不是只有一个大型模型，一个大型运行。然后第三，我认为是将研究与产品结合的不同方式。因此现在，我认为，在这些前沿实验室中，研究人员会对模型进行训练，他们会把模型 “扔” 到产品团队那一边，然后，产品团队会根据核心模型进行提示或联系工程师，开发出新的产品。但在这个模型始终在训练的世界里，我认为用户提供的输入与模型从中学习的内容是非常紧密相连的，

(18:29)like what the training signal is. And so there needs to be a lot more of a kind of integrated loop between research and product. And so while we're focused on tackling a lot of the core research challenges,  and that's our background,  I think we're also very focused on how to deploy this as quickly as possible to learn from actual feedback in the real world.


就像训练信号是什么一样。因此，研究与产品之间需要有更多的整合循环。所以虽然我们专注于解决很多核心研究挑战，而这正是我们的背景，我们也非常关注如何尽快部署这一点，以便从现实世界的实际反馈中学习。

Sonya Huang:(18:47)What motivated you to work on this problem?


什么促使你来解决这个问题？

是的，有些确实如此，对吧？一些最佳的中文模型具有受这些状态空间架构启发的层，并且，你知道，成本不是平方的。问题是，在我们手中，我们发现，始终是在牺牲准确性以换取这种记忆。没有免费的午餐。我们所说的是：如果你真的苦涩并且一致，你想做的就是思考，我如何能消耗更多的计算？我如何能在我以前未见过的新上下文上消耗它？所以我们和其他任何人一样坚信。我们并不认为 AGI 的整体方向会很快结束。

Jessy Lin:(10:37)I think if you look at like how the models think,  if you need to recall basic facts in order to like take the next step in your thinking,  you can't get very far. Maybe that's like a high level intuition, but it's part of like the reason why we think training is really important. In order to like, think more and more complex and deep thoughts about things,  you kind of need to internalize some things so that you can compose them into more abstract concepts.


我认为这显然是人工智能领域的重大挑战之一。我认为如今每个人都在谈论它，因为这些模型非常聪明。还有什么其他的挑战？我认为在边界处学习，学习那些使得这些模型有用的剩余部分。这不再单单是关于原始智慧了。这关系到学习新的事物。我认为这也是非常基础的问题，因为它回到真正理解是什么使得模型如此优秀。现在模型在预训练中偶然了解了很多东西，但我们并不真的理解为什么。就像互联网，只是，您知道，这是赐予我们的礼物，其中包含一系列多样的数据，包含所有这些不同的编码、写作及其他各种示例。

将事实记忆与技能学习分开是一种错误的二分法，因为模型需要内化知识以组成复杂、抽象的概念。当前的人工智能发展往往将事实视为外部数据库，但真正的智能需要将重要信息压缩为权重，以促进更深层次的推理。“梦游” 阶段——模型从主动互动中撤退以实验潜能——是目前流程中缺失的组成部分。通过关注团队级模型而不是通用的 AGI，有可能创建能够从模糊、私密或冲突数据中学习的系统，弥合研究与现实产品部署之间的差距。

Dan Biderman:(08:22)Either is fine for us. It's just easier to start with You know, teams of people have, you know,  are more, you know, disciplined in how they collect context and in the amount of context they have over years. And it's easy for us to start there. But every person's computer and every person's phone one day is a useful, you know, target for our technologies. And in fact, it will be very interesting to go there. We just think, you know, the big deposits of information are now in teams of people collaborating in knowledge work.


对我们来说，两者都可以。只是开始时比较简单，你知道，团队的人，他们在收集上下文和多年来拥有的上下文量方面更有纪律。对我们来说，从这里开始很简单。但每个人的电脑和每个人的手机，有一天都是我们技术的一个有用目标。实际上，去那里会非常有趣。我们只是认为，广泛的信息存储现在在团队之间共同协作的知识工作中。

大量的事实记忆基本上内置于大型语言模型中，这是一个特征还是一个缺陷？有一种观点你知道。模型只是死记硬背 "法国的首都巴黎"的事实，这实际上是一件坏事。我们希望模型能做的，是抽象地学习国家和首都的概念，而不是在权重中记住所有这些事实。所以我想知道你对分离记忆与学习的看法，以及今天模型是如何做到这一点的，以及你打算如何处理它。

(09:57)but like, it's lossy, because Part of the feature of intelligence is compressing what's important and separating that from what's not important. And so I think like,  you can't really separate fact learning from like non fact learning or skill learning as some people would like to think. Like if you take a model and like some people have done this with models where you like strip out,  you know, like all the facts and just have it like the pure core or something like this. It's very unnatural as a model. It doesn't know basic things. And you kind of need need that. But I think...


我明白了。所以你是说，这是一种错误的二分法，试图在这里将算法与数据库分开。重要的是如何区分什么是重要的记忆与什么不是重要的记忆。

Jessy Lin:(12:46)Exactly.


正是如此。

(14:01)How fast can it handle these kind of tail extreme things, the same ones that we dream about at night?


它能多快处理这些极端情况，正是我们晚上梦见的那些？

Shaun Maguire:(14:08)You guys come from academic backgrounds. What's a canonical example that motivates this problem or that's a win so far?


你们来自学术背景。有什么经典的例子能激励这个问题，或者到目前为止有什么成功的案例？

(24:24)We just think there's more compute to scale. And if I truly want to understand Shaun and Shaun's work in Shaun's context,  Just like re-reading files is not going to make it, especially for a special person like you.


## Optimizing Model Efficiency Through Weight-Based Memory


通过基于权重的记忆优化模型效率

The reliance on RAG and KV caching creates significant inference bottlenecks, as models repeatedly process the same documents. Internalizing knowledge into weights offers a "RAG killer" alternative, potentially reducing token consumption by two orders of magnitude. While RAG remains useful for certain tasks, weight-based learning allows models to develop intuition about where to look for information and how to handle bespoke workflows. By spending compute offline to compress data into model weights, systems can achieve higher fidelity and faster performance, moving away from the "monstrosity" of current KV cache requirements.


依赖 RAG 和 KV 缓存会造成显著的推理瓶颈，因为模型不断处理相同的文档。将知识内化为权重提供了 “一种 RAG 替代品”，有可能将令牌消耗减少两个数量级。虽然 RAG 在某些任务中仍然有用，但基于权重的学习使模型能够发展出对信息查找位置和如何处理定制工作流的直觉。通过在离线计算中压缩数据到模型权重，系统可以实现更高的保真度和更快的性能，摆脱对当前 KV 缓存要求的 “怪物” 依赖。

(19:36)It just happened that way. And now to figure out how to crack this problem of continual learning,  it's about figuring out what about pre-training or even post-training makes it possible for the models to generalize in these magical emergent ways and controlling that process so that,  you know, a company has a set of private data. How do we make the models learn that just as well as the models know like the capital of France or,  you know, like how to write Python? So I think it's a really fun problem to think about.


就是这样发生的。现在要弄清楚如何解决持续学习这个问题，关键在于弄明白预训练或后训练的哪些因素使得模型能够以这些神秘的渐现方式进行归纳，并控制这个过程，以便，你知道，一家公司拥有一组私有数据。我们如何让模型学习，就像它们知道法国的首都，或者，嗯，如何编写 Python 一样？所以我认为这是一个非常有趣的问题可以思考。

Sonya Huang:(08:51)Is it a feature or a bug that there is so much Fact memorization basically built into the large language models and there's a school of thoughts that you know. The models just wrote memorizing the fact that the capital of France is Paris is actually a bad thing. And what we would prefer for the models to do is, you know,  abstractly learn the concepts of countries and capital cities,  but not to memorize all these facts in the weights. And so I'm curious what you think about disentangling memorization versus learning, how it's done in the models today,  and then how you're thinking of approaching it.


Jessy Lin:(09:24)Yeah, I think it's a really interesting question. To some extent you kind of need to remember stuff in order to like compose them into more complex concepts. I think the thing that's kind of missing is figuring out what's important to remember. And I think even now, when you think about like learning new knowledge,  if you look at a lot of these academic benchmarks,  it's like, how can we learn very specific facts, like, you know,  the length of a bridge in this like African country. And that's not something that you really want the models to devote capacity for. And it's not something that we devote capacity to. So I think if you look at human memory, I mean,  you can say a lot more about this,


是的，我觉得这是一个非常有趣的问题。在某种程度上，你确实需要记住一些内容，以便将它们组合成更复杂的概念。我认为缺失的部分是弄清楚什么是重要的记住的内容。我认为即使在现在，当你考虑学习新知识时，如果你看看很多这些学术基准，就像，如何学习非常具体的事实，比如这个非洲国家一个桥的长度。这并不是你真正希望模型为之投入能力的事情。这也不是我们投入能力的事情。所以我认为，如果你看看人类记忆，我的意思是，你可以说更多的内容，

(11:36)There's also algorithms of how do you efficiently manipulate information and get some answers. In a sample efficient way. And I think the magic of deep learning is that these two things are now mushed together and we need all these smart people and anthropic interpretability to try and break them apart. And I think a lot of what we're seeing now in the adoption of AI into the economy is that these things are gradually separating again where companies have their own context and they really Handle them with care and engineer them with care. And there's a generic model that's completely a stranger to these contexts and the model is operating on them. But for us, it's clear that.


Jessy Lin:(17:49)And maybe another point on that is like,  I think a lot of things need to look different in the world. So one is there needs to be new research breakthroughs. Two is new infrastructure for training like You know,  small models for everybody rather than like one big model,  one big run. And then the third, I think, is a different way of kind of combining research and product. So right now, I think, like, there's like researchers in these frontier labs, they kind of train the model,  they throw it over the fence to the product team,  who then like prompts or contacts engineers like new products surfaces on top of the core models. But in this world where the models are always training,  I think the inputs that users provide are very intricately tied to what the models learn from,


Dan Biderman:(12:47)And it's an open question.


这是一个开放的问题。

Sonya Huang:(12:48)I guess it's part of how we dream. And are you guys taking any inspiration from that in terms of ranking?


我想这是我们梦想的一部分。你们是否在排名方面受到过这样的启发？

Jessy Lin:(12:52)Very, very loosely, I think. Just the idea that that's kind of a phase that's missing maybe where you take a context and you deeply internalize it. Right now, it's like everything happens at test time. You look at the context that the user gives you and you do some like thinking on the fly. But again, like you can't get very far or you can get so far maybe. And like you make mistakes along the way,  like how do you digest that back into the model so that next time you do it,  you do it the right way and make even more progress.


非常，非常宽泛，我想。只是这个想法，可能是这样一个缺失的阶段，你需要深入内化一个上下文。现在，就像所有事情都发生在测试时。你查看用户给你的上下文，然后你进行一些即时思考。但再次强调，你不能走得太远，或者你可能会走得很远。而且在这个过程中你会犯错误，如何将这些反馈回到模型中，以便下次做到时，以正确的方式进行，并取得更大的进展。

是的，补充一下，我认为，Frontier Labs 的 P0 是什么？你们中有些人与他们关系挺近。这是朝着 AGI 前进，获得这个能够在编码和数学方面非常有能力的通用模型，然后利用它来自动化经济，或者解决非常困难的，你知道的，长期加密和防御问题，或者其他任何事情。而且很清楚需要达到什么目的。推进这个，需要更多的预训练，更大的模型，更多的数据，更强的强化学习，更多的推理时间计算，这类东西。这就是 P0。大部分的开支和人才都投入在这里。

我们当前系统中的解决方案与生物学中的解决方案相去甚远。我并不是那种认为机器应该像动物或人类大脑一样的人。我不这么认为。有很多事情计算机能做得比我们更好。但人类记忆中有这些非常不同的东西。如果你想存储整个代码库，或者你可以使用计算机，你甚至不需要计算机上的人工智能就可以无损地存储一切并得到它。人类大脑是在信息容量的限制下进化出来的，并拥有这些模糊的表征，之后可以，

Dan Biderman:(22:58)Yeah, I would say just on a more like superficial perspective on the current deployment of AI,  it's way more than just GPUs and we're seeing all these, you know,  sandboxes exploding and models operating on other computers trying things.


是的，我认为如果你看看人们在应用层上现在花费的时间，很多都在努力让模型在他们的用例中发挥良好。像是，我希望模型可以，假设，设计我的网站，符合我的品牌风格。这是一个非常常见的例子。但人们用代理做的任务有很多种，比如学习如何运行工作流或你特定的写作方式，比如说。所以有许多许多种事情。老实说，当我们考虑这些方法时，有点回到事实和技能之间的区别，其实并没有。我认为这些方法在这方面是无差别的。

Dan Biderman:(29:46)And this involves some sort of intuition that sometimes the models don't have. Interestingly enough, they don't know where to look. And especially if you're, you know, limited to the current way of doing things,  which is keyword search, that is just easier to scale in RL and least involved in terms of like infra for embeddings and stuff. So yeah, knowing what to search is something that's intuitive and can happen in the weights and also about caching and inference. Much of this company started with us taking it like a deep dive into like KV caches and caching. And this is a fascinating thing, right? KV cache is a monstrosity of the current way of doing things that, you know,  think about it, a KV cache for a single like Wikipedia article for some,


而这涉及某种直觉，有时候模型并没有。有趣的是，他们不知道该去哪里找。尤其是如果你知道，局限于目前的做法，即关键字搜索，这在强化学习中更容易扩展，而且在嵌入和其他方面涉及的基础设施较少。所以，是的，知道该搜索什么是直观的，并且可以在权重中发生，也与缓存和推理有关。许多事情是我们通过深入研究 KV 缓存和缓存开始的。这是一个引人入胜的事情，对吧？KV 缓存是当前做事方式的一个庞然大物，想想看，一个 KV 缓存为某个像维基百科的单一文章，

对我来说，我从来没有对语言感兴趣。在我看来，这是一种如此先进的能力，整个动物王国在表达和语言方面有着与我们非常不同的形式，还有我们如何与自己和书写沟通。我一直觉得，像许多其他 AI 领域的领袖一样，自然的事物就是必须体验世界，去行动，想象一个将是关键的行动。但是后来，我和其他人一样，看到 ChatGPT 的时刻，去 Mosaic 等地方做了一些工作，以了解 NLP 方面的运作。

(38:02)And the thing that's striking is that like the Language should be pretty hard. Like each word has this one hot embedding vector that's as dissimilar to any other word than it is,  you know, it's a completely high dimensional space and it's really artificial in a sense. And we learn it with models that are order of magnitude bigger than the best vision models. And still, you know, things work pretty well. I do think there's a lot of juice to be squeezed in an image and video. And I think you guys are doing good investments in this space. But I think the two would keep being interesting in different ways.


Dan Biderman:(42:11)Anyways, yeah, and vision is dominating. When people are training vision language models, they end up Language ends up dominating the vision content there. But yeah, it's hard to say that because a certain brain is more, you know,  biased towards a certain modality doesn't mean necessarily that we're going to more efficiently do it. I do think that efforts on like brain computer interfaces should take this into account. How do you then relay it back to the brain? That's where I think it's really important to think like, what real estate do we have there right now? But for knowledge work, it's equally fine if it's text, I think.


不管怎样，是的，视觉占主导地位。当人们训练视觉语言模型时，语言最终会主导那里的视觉内容。不过，说某个大脑更偏向于某种模态，并不一定意味着我们能够更有效地做到这一点。我确实认为在脑机接口的努力中应该考虑到这一点。那你如何将其传回大脑？我觉得思考一下我们现在在那里有多少空间真的是很重要。但对于知识工作来说，我认为如果是文本也同样可以。

Sonya Huang:(42:45)Last question. If everything goes right, what does the world look like in 5-10 years and then what is Engram's role in it?


Dan Biderman:(25:46)Yeah, to me, it's like the natural thing. Almost all the app layers are basically, you know,  a frontier model wrapped in a loop with search tools and stuff. And what they're all interested in doing with us is finding ways to kind of interface with their data in a way that's,  you know, Faster, more efficient and also is more contextual. So almost all of them, it's like we want to have our, you know,  our firm knowledge, you know, be encoded in something that's more efficient that I don't have to research. We want to have the model know in a targeted way who's the person I should triage a thing to.


Jessy Lin:(34:59)Like, it's like, oh, you know, you might like these sheets because you trained a model on a GPU last week. It's like, that's totally irrelevant. And to some extent, it's like because the memory is flawed. But also, I think you do want memory in your, I guess,  tools and the products that you use to be separated to have control over that. So I personally think like there needs to be some separation there. But I guess to be determined what that might look like.


就像是，哦，你可能会喜欢这些表格，因为你上周在 GPU 上训练了模型。这完全无关紧要。在某种程度上，这是因为记忆是有缺陷的。但我也觉得你确实想要在你的工具和产品中有记忆，并且将其分开，以便控制。所以我个人认为，要在那里有一定的分离。但我想这还有待确定它可能会是什么样子。

(39:36)This is just kind of my dumb assessment. It seems many orders of magnitude greater. And there's a lot of like optical processing that happens, like even before you reach, you know, like electrons. And so it's just like the total bit rate that is of training data that's kind of Being processed and then making it to your brain seems many orders of magnitude greater than the audio data where,  you know, it's sound waves where sound waves are fundamentally like It's a much slower bitrate than light. And then there's almost like an upscaling from the acoustics to electronics, which make it into your brain,  where it's like a downscaling from photons to electrons with vision.


这只是我愚蠢的评估。它似乎大了好几个数量级。而且有很多光学处理发生在你到达，像电子之前。所以，训练数据的总比特率在被处理后传输到你的大脑中，似乎比音频数据要高很多个数量级，你知道的，音波的比特率本质上远低于光的比特率。然后几乎可以说是从声学到电子的升级，使其进入你的大脑，就像从光子到电子的视觉缩减。

Jessy Lin:(29:46)Yeah.


是的。

Shaun Maguire:(31:38)What are some of the things that could happen in the next year or two that would be like the ChatGPT moment of memory? Or do you think that that's not how things will play out?


在接下来的一年或两年里，可能发生的事情中，有哪些会像 ChatGPT 的记忆时刻？还是你认为事情不会这样发展？

Jessy Lin:(31:49)It's a good question. I don't know, I think like the first proof of concept of the thing that people keep talking about with continual learning,  which is you have an intern that you can teach things over time, and it actually gets better. I think everybody's waiting to see that, you know,  and no matter how sophisticated the context engineering approaches are these days,  they're not getting there. So I think you need, you know, all these tools at your disposal to make that happen. But I think it will be something like that where it's like the model's actually getting smarter. Like, whoa, it's different from yesterday.


Shaun Maguire:(33:18)This is just for fun, like rapid fire questions going off just memory. When's the last time you reached surprised about something in AI, in any area?


这只是为了好玩，就像快速提问，用记忆来回答。你上一次对 AI 的某件事感到惊讶是什么时候，在任何领域？

Dan Biderman:(33:28)When reading about fundraising, a lot of surprises every day. I would say all of us felt, you know,  a little bit of a change around the capabilities of the coding agents.


在阅读有关筹款的内容时，每天都有很多惊喜。我可以说我们所有人都感受到了一些关于编码代理能力的变化。

Jessy Lin:(33:38)That's true.


是的。我认为一个圣杯是，你去工作，然后你快速消耗所有这些代币，创造所有的价值，但不知为何，所有的知识产权和其他东西都留在公司，但你所学到的技能，你发明的东西，你的做事方式，其中一些你可以以某种方式带到你的下一份工作中，确保不会对其他公司的知识产权造成伤害。所以我确实认为掌握一套技能会很有趣。我们现在在生物学中这样做，我们就签署保密协议并遵循一些伦理规则。

(35:56)But I think doing it in a digital world would be pretty interesting and pretty rewarding because it will force each of us to push the frontier and implement AI more deeply in our companies,  in our individual life, and then be rewarded for it.


但我认为在数字世界中这样做会非常有趣也非常有回报，因为这将迫使我们每个人推进边界，更深入地在我们的公司和个人生活中实施人工智能，并因此获得回报。

Dan Biderman:(37:23)Yeah, to me, like I've never been interested in language. It seemed to me Such an advanced capability that, you know,  the entire animal kingdom has very different forms of Of speech and language than what we,  you know, and how we communicate with ourselves and writing. And I was always, as many other leaders in AI, had this thought that,  you know, the natural thing is you have to experience the world, act in it,  envision an action that will be the key. But then I've, you know, like anyone else,  seen the ChatGPT moment and went to do some work at Mosaic and stuff like that to learn how the sausage is made on the NLP side.


Dan Biderman:(35:24)Yeah. And like, I think a holy grail is like,  you go to work and you just burn through all these tokens and you create all this value and somehow,  you know, all the IP and stuff stays with the company, but somehow the skills you learned,  the things you invented, your ways of doing things,  some of them you can take with you as well to your next job in a way that's,  you know, sanitized and not, you know, harmful to any other company's IP. So I do think like carrying a set of skills will be interesting. We do it in our biology right now and we just, you know,  sign NDAs and have like ethical rules around it.


不，伙计，我正在外部化。我在个人生活方式中是个非常相信外部化的人。

Shaun Maguire:(42:03)In the limit, it's all rag.


在极限情况下，全都是外部化。

Dan Biderman:(42:05)I internalize just, you know, important things like My emotions to you. No, just kidding.


我仅仅内化一些，比如对你的情感。不，开玩笑的。

Jessy Lin:(42:11)Sorry.


抱歉。

是的。对我而言，这确实是一个变种故事，比如，在神经科学中，我们知道记忆和导航是密切相关的。在大脑中，相同的电路负责空间中的地标，同时也涉及一些，记忆情节的元素以及类似的事情。对我来说，我认为公司可以是每个人与数据平面的实际 LLM 接口。与我们所熟知的优秀公司如 Databricks 和 Oracle 等有一些相似之处，我们形成的这些记忆恰好是神经记忆，模型也正好是个性化的，并且数量达到数亿，

(44:00)but they're basically a neural interface to the data plane in a way that's very different from what we know. And it's more efficient. It's more associative. It's not representing the file system as it is. It's representing a brain state. So that's for me a vision.


但它们基本上是以一种与我们所知道的截然不同的方式，作为数据平面的神经接口。而且它更高效。它更具关联性。它并不是在表示文件系统的真实状态。它是在表示一种大脑状态。所以这对我来说是一种愿景。

Sonya Huang:(44:14)Beautiful vision to end on. Thank you guys so much for coming by to share what you're building.


美丽的愿景，让我们结束在这里。非常感谢你们来分享你们正在构建的东西。

Dan Biderman:(44:19)Awesome.


太棒了。

Shaun Maguire:(44:19)Love it. Thank you guys.


爱它。谢谢你们。

我认为这是一个未解决的问题。我认为没有人回答过这个问题。我们都在努力解决它。这也是生物记忆的基本问题。什么应该内化，什么不应该？我认为那些像是，你知道的，你是否需要内化一年前你住过的酒店的房间号？可能不需要，毕竟它不在你的神经组织中。可能把它写下来是好的，但你是否需要现在内化你家的密码？可能在未来几年里，将其印刻在某处是有用的。所以，没错。这如何转化为知识、工作和产品？

(27:44)This is still something we figure out and we try to take the approach that we try to use as few heuristics as possible. It's easier on filters on the data and say, like, I'm going to keep this,  discard that, train on this, train on that. But as humans, you know, we watch TikTok and we, you know,  get exposed to a lot of garbage and still the brain is able to learn and not completely go off the rails. And we think models should be the same as well.


这仍然是我们在探索的事情，我们尝试采取尽可能少的启发式方法。对数据过滤更容易，也就是说，我将保留这个，丢弃那个，基于这个进行训练，基于那个进行训练。但作为人类，你知道，我们观看 TikTok，接触到很多垃圾，但大脑仍然能够学习，而不会完全失控。我们认为模型也应该是这样的。

我在 2007 年于斯坦福大学的 SAS 公司开始了博士学位，那时人工智能无聊得不能再无聊了。一切都是统计学习。基本上有两个领域：计算机视觉和自然语言处理。所以视觉和语言算是这两个领域。我认为这仍然是真的。到 2012 年，所有这些都发生了，视觉在六年或更久的时间里占据了主导地位。你们对语言似乎在进展中主导于视觉感到惊讶吗？第二个问题，你认为视觉有可能回归吗？你对此怎么看？

Jessy Lin:(36:48)Yeah, I think it is pretty surprising to me. I mean, some people maybe saw it coming,  but I think I've always kind of been interested in language as like I don't know,  I guess like a medium for communication and like so many kind of complex abstract things can be done in language. I do think like, you know, I imagine like in the longer term,  language and vision will kind of like combine in this more like unified system where,  you know,  we kind of like take in inputs from all of these different modalities and like understand them in this abstract way. But yeah.


是的，这对我来说确实很惊讶。我是说，有些人可能预见到了，但我一直对语言感兴趣，就好像，我不知道，我想就像是沟通的媒介，许多复杂的抽象事物可以用语言来表达。我确实认为，从长远来看，语言和视觉将会结合成一个更统一的系统，在这个系统中，我们将从所有这些不同的模态中接受输入，并以抽象的方式理解它们。不过，对。

(41:52)I'll have to check with ChatGPT, but I think that's the situation.


我得和 ChatGPT 确认一下，但我想情况就是这样的。

Shaun Maguire:(41:56)You don't know from memory?


你不知道吗？不靠记忆？

Dan Biderman:(41:57)No, man, I'm externalizing. I'm a big rag believer in my personal lifestyle.


对我来说，这就像是自然的事情。几乎所有的应用层基本上都是，你知道，裹着循环的前沿模型，带着搜索工具等。他们都希望和我们一起找到与他们的数据接口的更快、更高效、更具上下文感的方法。几乎所有人都想，我们希望我们的知识能够以更高效的方式编码，以便我无需研究。我们希望模型以针对性的方式知道应将事情交给谁。

是的。我想再深入讨论一下这个 RAG 杀手的事情。对不起，我再重复一下同样的事情。我还没有完全理解它。

Dan Biderman:(26:52)Yeah.


Sonya Huang:(26:54)Is the premise that there's some trade-off between doing RAG versus updating your model weights? Is the idea that you should be doing both? What types of things should be done in the weights versus what types of things should be externalized to RAG?


这个前提是，在做 RAG 和更新模型权重之间有某种权衡吗？这个想法是你应该同时做这两件事吗？在权重中应该做哪些事情，与应该外部化到 RAG 的事情相比？

Jessy Lin:(28:05)Yeah, maybe concretely in the short term,  I think a lot of what people are worried about these days is the huge inference costs of running these agents like for days on end.


是的，可能短期内，我认为人们现在最担心的一点是运行这些代理的巨大推理成本，一直持续几天。

Sonya Huang:(28:15)High inference costs a good thing.


高推理成本是好事。

Jessy Lin:(28:18)I mean, consuming tokens for what?


我是说，消耗令牌是为了什么？

Shaun Maguire:(28:20)Sonya works at Fireworks. She really loves that.


Sonya 在 Fireworks 工作。她非常喜欢这个工作。

像泰勒·斯威夫特之类的，将会在 GPU 上占用 80 GB 的 HBM 内存，还需要整个 llama。这是，比如，一个 70B 的 llama 模型。整个模型的权重大约是 100 GB。而且，即使有些失真，它们也能记住整个互联网。那么这个东西为什么会如此……一个东西是如此高效呢。我们有一个存在证明，即梯度下降可以在很少的数字中打包大量信息。而这个 KVCache 的东西，你取几十 KB 的文章，它就变成那 80 GB 的大脑状态。所以当然，你可以缓存这个，你可以加载这个。你会遇到磁盘和 HBM 之间的问题。人们正在为之努力。

(31:14)It's pretty interesting. But what if we can take those 80 gigabytes, spend some compute offline, maybe also in Fireworks,  but then compress it and make it really,  really small so that the thing we load in cache is like,  A thousand X smaller. That would have tremendous implications for how we load things, how fast we can do things,  and what the fidelity of their representation is.


这非常有趣。但是如果我们可以把这 80 GB 花一些计算时间离线，可能也在 Fireworks 中，但随后压缩它并使其真正，真正小，以便我们加载到缓存中的东西像是，1000 倍更小。这将对我们加载东西、我们多快能完成事情以及它们代表的保真度产生巨大影响。

Sonya Huang:(31:37)Super interesting.


非常有趣。

Dan Biderman:(31:38)Yeah.


Shaun Maguire:(36:07)I started a PhD in the SAS firm in 2007 at Stanford and AI was boring as hell at the time. It was all statistical learning. And there's basically two areas like computer vision and NLP. So like vision and language were kind of the two areas. And I think that's still true. In 2012, all that happened, like vision was dominating for six years or whatever. Are you guys surprised that language seems to be like the language approach seems to be like dominating over vision in progress? Question two, do you think vision has any chance of coming back? How do you think about this?


最后一个问题。如果一切顺利，五到十年后的世界是什么样的，恩格拉姆的角色又是什么？

Jessy Lin:(42:52)I think I'm imagining like a world where everyone has their own model that is really different from the other person's model and from the frontier model. And all of these kind of serve different purposes. And to have a model that really, you know, I think people often talk about like,  knowing, knowing you, but also like, kind of like helping you in the ways that make sense to you,  personally, whether it's like an individual or a team,  I think There's an element of like having different kinds of intelligence everywhere.


我想象的是一个世界，每个人都有自己独特的模型，与其他人的模型和前沿模型截然不同。而且所有这些模型都有不同的目的。要有一个真正的模型，我认为人们常常会谈到了解你，但也要以对你有意义的方式来帮助你，不管是个人还是团队，我认为无处不在都有不同类型的智慧。

Dan Biderman:(43:24)Yeah. And to me, actually, it's a variant of the story where like, you know,  in neuroscience, we know that memory and navigation are pretty closely related. Same circuits in the brain that, you know,  represent landmarks in space are in charge of some,  you know, elements of episodic memory and things like this. And for me, I think the company can be, you know,  the actual LLM interface to the data plane for everyone. Sharing some similarities to great companies like, you know, Databricks and Oracle, where, you know,  we form these memories that happen to be neural memories with models that happen to be personalized and happens to be there's hundreds of millions of them,


Jessy Lin:(28:28)Yeah. So I think it's like in the short term, I think that's the immediate pain point. Like, why are you reading the same files over and over again, you know,  even in the same query, but like definitely, you know, across people in the same company,  they're running the same queries on the same documents over and over again. And that should be something the model just knows. Like in the same way you ask an employee, they don't, you know, type into the search box,  like, what was I working on yesterday? They just know.


是的。所以我认为，短期内，这就是当下的痛点。比如，为什么你反复读取相同的文件，即使在同一个查询中，但确实，你知道，同一公司的不同人，他们在同样的文件上反复运行相同的查询。这应该是模型自然知道的事情。就像你问一个员工时，他们不会在搜索框里输入，像 “我昨天在做什么？”。他们直接知道。

Sonya Huang:(28:51)But doesn't caching kind of solve that?


但是缓存不是可以解决这个问题吗？

Jessy Lin:(28:53)I think to some extent, yeah. But I think going back to this, like,  question of What should be internalized versus what's,  like, something you retrieve at test time? I think, again, like a lot of it is about building on your knowledge. So if you are always doing RAG, you can't make associations like, oh, you know,  I see somebody, you know, on the team is doing this kind of research. And I kind of, like recall, at an abstract level, oh,  there's this like related thing that you might want to know about. You didn't even ask about it. Right. But I think like, These kinds of associations can only happen in weights because they're not really about,  you know, you asked me to search for this.


(34:24)That's interesting.


这很有趣。

Sonya Huang:(34:25)Right now there's this idea of we're each going to have a token wallet that we're going to bring around to companies,  or to different apps, different workspaces. Do you think that we're going to end up with a memory bank,  a memory wallet that we're going to move around across the digital world as we go?


令人惊讶的是，语言应该相当困难。每个词都有一个独特的嵌入向量，与其他任何词相比都极为不同，实际上，这是一个完全高维的空间，从某种意义上讲，确实是人为的。我们用的模型的规模比最好的视觉模型大几个数量级。但仍然，情况运作得相当不错。我确实认为图像和视频还有很多可以挖掘的潜力。我觉得你们在这个领域的投资做得很好。但是我认为这两者在不同的方面都会持续有趣。

(40:23)Whereas in computers today, everything is electronic. So it's kind of like you nerfed vision and you like promoted language where the It's like all processing is on the same playing field. It's all electronic. And I just, I think this might, this is like my crazy ass, dumb,  non-technical crackpot theory,  but I think this might be part of why Just like from an information theory perspective that like maybe language and vision are on a similar playing field,  by the time you get to like LLMs, and then LLMs are, we're just a really,  really smart architecture that's better suited for language than for vision. How dumb does this sound? Especially to you, Dan, the neuroscientist.


而在今天的计算机中，一切都是电子的。所以这有点像你削弱了视觉，促进了语言，所有的处理都在同一个水平上。一切都是电子的。我只是觉得，这可能是我疯狂、幼稚、非技术性的冷门理论，但我认为这可能是为什么从信息论的角度来看，语言和视觉可能处于类似的水平，直到你接触到像大型语言模型（LLMs），然后大型语言模型就是，我们只是一种，非常聪明的架构，更适合语言而非视觉。这听起来有多傻？尤其是对你，丹，神经科学家。

杰西也有一些认知计算科学的背景，对吧？所以我想说我的观点是，看，我们在知识工作中所做的很多事情，我们还没有进化到可以做这些，对吧？我们坐在这些电脑前，阅读这些东西，写这些备忘录，随便什么。我们并不是为此而进化的。这对我们来说是新的。我们的大脑并不是为了这个而设计的。不过，尽管如此，拥有大语言模型为我们做这些事情仍然是有用的。而且，你知道，作为人类，我们对视觉有很强的偏见。你知道，其他啮齿动物更偏向嗅觉。我在这些方面也有过个人的研究。那么大脑中分配给视觉的空间是什么，像视觉和，呃，枕叶与像语言区域、颞叶相比，可能是更偏向视觉的。

(26:20)And we're just showing them that with pretty lightweight training, these things can be instinctual to the models. They don't have to And we have these very involved long REPL loops to solve them. So it's, in a sense, it's like, you know, it's a rag killer kind of thing. Again, we can always do rag and we can always retrieve,  but that's the thing that people are interested in interfacing with very large data planes and automating very repetitive things this way.


我们只是向他们展示，通过相当轻量的训练，这些事情可以成为模型的本能。它们不必。而且我们有这些非常复杂的长 REPL 循环来解决它们。从某种意义上说，这就像是，你知道，这是一种拉格杀手的感觉。再次，我们总是可以做拉格，我们总是可以检索，但这是人们希望能够与非常大数据平面接口并以这种方式自动化非常重复的事情。

Sonya Huang:(26:46)Yeah. And I want to double click on this rag killer thing. And I'm sorry to beat a dead horse. I just don't fully grok it yet.


我认为在某种程度上是的。但我认为回到这个问题上，什么应该内化，什么是，如同在测试时检索的东西？我认为，再说一次，很多事情都是关于建立你的知识。所以如果你总是在进行 RAG，你就无法做出关联，比如，你知道，我看到团队中的某个人在做这种研究。而且我有点像在抽象层面上回忆，哦，有这个相关的事情你可能想了解。你甚至没有问过。对的。但我认为，这些类型的关联只能发生在权重中，因为它们并不是真正关于你让我搜索这个。

(29:30)I'm going to search for this.


我将搜索这个。

Dan Biderman:(29:31)And also,  I think the main limitation with retrieval systems in general and in AI specifically is like the problem is not so much what to store and where to put it. It's the problem is like how to address it, like how to query the thing. Do you know what to look for even?


而且，我认为一般来说，检索系统和 AI 的主要限制在于，问题不在于存储什么和放在哪儿。问题在于如何访问它，如何查询那个东西。你知道该寻找什么吗？

(30:29)you know, Taylor Swift or something like this,  it will be like 80 gigabytes of HBM memory on the GPU and an entire llama. It's for, say, a 70B llama model. And the entire weights of the model would be about 100 gigabytes. And, you know, with some distortion, they remember the entire Internet. And how come this thing is so... One thing is so bit efficient. And we have this proof of existence that gradient descent can pack a lot of information in very few numbers. Whereas this KVCache thing, you take a few tens of kilobytes of article and it becomes those 80 gigabytes of brain state. So sure, you can cache this, you can load this. You'll have issues with disk to HBM stuff. People are working on it.


是的。重要的是要说，ChatGPT 模型是没有预料到的。我们只是阅读了某些人在 ChatGPT 之前的不同产品方向。我觉得这个例子就像是，如果你今天辞职，你唯一的任务就是创建一个更适合你的模型，而你会使用 OpenAI、ThoughtPic 和所有这些前沿模型，你会全天候工程化正确的技能，作为个体，你推动改变的方式是非常有限的。你最好等下一版本的模型，然后再进行下一步。

(32:54)And we would like to see a future where actually the more time you spend on the thing actually translates to the quality of performance,  at least in the things and domains you care about. And this is pretty hard to achieve. And the only reason we think it could be achieved is if you start scaling compute and training on these data without destroying them all,  importantly, which is pretty hard.


我们希望看到一个未来，花在某件事情上的时间实际上可以转化为性能质量，至少在你关心的领域和事情上。这很难实现。我们认为这可能实现的唯一原因是，如果你开始对这些数据进行计算和训练，而又不破坏它们，这一点很重要，这实在是很难。

Shaun Maguire:(38:41)That was my lead up. Now I'm going to tell you the crackpot theory. And this podcast is not for me to pontificate. It's for you guys. But this is something I've been thinking a lot about, and you're the right people to share this with. I was pretty shocked that language kind of surpassed vision and I underestimated what was happening with LLMs in like 2018,  2019, 2020 because I just had this bias towards vision. And when I look back on it now,  I think what's basically happening is that in biology,  Like vision has a massive fundamental advantage over language in biology. And maybe I'm wrong, but basically like the bit rate that your brain can process Optical data through the eye is,  and this is my, I'm not a biologist.


那是我之前的铺垫。现在我要给你们讲讲这个疯狂的理论。这个播客并不是让我讲教条。这是给你们的。但这是我一直在思考的事情，而你们是分享这些的合适人选。我对语言超越视觉感到相当震惊，我低估了 2018、2019、2020 年 LLMs 正在发生的事情，因为我有一种对视觉的偏见。当我现在回头看时，我认为基本上发生的事情是，在生物学中，视觉在生物学上对语言有着巨大的基本优势。也许我错了，但基本上，你的脑子可以处理通过眼睛获取的光学数据的比特率是，我不是生物学家。

Dan Biderman:(41:11)Jessy also has some background in cognitive computational science, right? So I would say my point here is like, look,  much of what we're doing in knowledge work,  we haven't evolved to do, right? We're sitting on these computers, reading these things, writing these memos, whatever. We are not evolved to do this. It's new to us. Our brains are not wired for this. Still, nevertheless, it's useful to have LLMs to do this for us. And, you know, as humans, we're heavily vision biased. You know, other rodents are more olfactory biased. And I've worked on these things myself before. So what's the real estate in the brain that's allocated to vision and, you know,  occipital lobes versus like language areas, temporal lobe, probably more vision.


Dan Biderman:(27:07)I think it's an unsolved problem. I don't think anyone has answered to it. We're all working on it. It's also the fundamental question of biological memory. What should be internalized versus what not? I do think that things that are like, you know,  do you need to internalize the room number in a hotel that you were in like a year ago? Probably no, not in your neural tissue. Probably that's good to write down, but do you need to internalize maybe the password to your home right now? Probably it's useful for the next few years to have that imprinted somewhere. So yeah. How does this translate into like knowledge, work and products?


Sonya Huang:(28:24)I love inference.


我喜欢推理。

Dan Biderman:(28:26)We love inference too.


我们也喜欢推理。

## The Evolution of Personalized AI and Neural Data Interfaces


个性化人工智能与神经数据接口的演变

The future of AI lies in personalized models that act as neural interfaces to an organization's data plane, rather than generic, one-size-fits-all systems. While language models currently dominate, the integration of multimodal inputs will eventually create more unified, abstract systems. The concept of a "memory wallet" suggests a future where individuals carry sanitized, learned skills across different workspaces. Ultimately, the goal is to build systems that function like a brain state, providing an associative, efficient, and deeply contextual interface that evolves with the user, fundamentally changing how knowledge work is performed.


人工智能的未来在于个性化模型，它们作为组织数据平面的神经接口，而非通用的、一刀切的系统。尽管当前语言模型占主导地位，但多模态输入的整合最终将创造出更统一、抽象的系统。“记忆钱包” 的概念暗示着未来个人在不同工作空间中携带经过清洗、学到的技能。最终目标是构建像大脑状态一样运行的系统，提供关联性、效率和深度上下文的接口，随着用户一起演变，根本改变知识工作的执行方式。

这是个好问题。我不知道，我觉得像是人们一直在谈论持续学习的概念验证，实际上是你有一个实习生，你可以随着时间教它东西，而且它确实变得更好。我认为每个人都在等待看到那个，你知道，无论如今的上下文工程方法有多么复杂，它们都没有实现。所以我认为你需要这些工具来让这一切发生。但我想它会像那样，模型确实在变得更聪明。就像，哇，今天与昨天不同。

Dan Biderman:(32:19)Yeah. And it's important to say that the ChatGPT model was not anticipated. We just read about all the different product directions that certain people had before ChatGPT was different. I feel like to me, the example is like, look, if you, you know,  resign from your job today and your sole mission was to make a model that's better for you,  and you would use OpenAI and ThoughtPic and all these frontier models,  and you just 24-7 engineer the context right skills,  Your way to move the needle is very limited as an individual. You'll just be better off waiting for the next version of the model and you'll take it from there.


这是真的。

Dan Biderman:(33:38)But we've been, you know, dabbling with these things and trying to make them work in more effortful ways before,  so it didn't come as a complete surprise. But yeah, I think, to me, the main events were GitHub Copilot. That, for me, was just the main event and ChatGPT. And then seeing the agentic stuff, we all anticipated, I think,  and different people had different expectations on how far it can go and how long the horizon it can go. But I feel, yeah, we're yet to see something fundamentally different. And people are working on completely new ways of doing things now. Well, yeah, to me, it's models actually changing in a way that's not harmful and learning new things on the fly that are,  you know, personally and economically viable.


不过我们之前一直在尝试这些东西，并努力让它们以更有效的方式工作，所以这并没有完全让人感到惊讶。不过，我认为对我来说，主要的事件是 GitHub Copilot。对我来说，那就是主要事件，还有 ChatGPT。然后看到我们都预期的代理性东西，我想每个人对它能走多远、需要多长时间有着不同的期待。但我感觉，我们还没有看到什么根本不同的东西。现在人们正在研究完全新的做事方式。嗯，对我来说，是模型以一种不有害的方式变化，并且能够灵活学习新的东西，这些东西在个人和经济上都是可行的。

现在有这样一个想法，我们每个人都会有一个通证钱包，带着它去公司、不同的应用程序和工作空间。你认为我们最终会有一个记忆库、记忆钱包，在数字世界中移动吗？

Jessy Lin:(34:43)I think it's an interesting question. I don't know if we've fully figured out what the right product form factor is in this sense. In a way, even with like ChatGPT memory, let's say,  I kind of don't want it to remember across my like personal and work context.


我认为这是一个有趣的问题。我不知道我们是否已经完全弄清楚在这方面什么是合适的产品形态。在某种程度上，即使像 ChatGPT 记忆，我想说，我不想它在我的个人和工作环境之间记忆。

Sonya Huang:(34:58)Oh, yeah.


哦，没错。
