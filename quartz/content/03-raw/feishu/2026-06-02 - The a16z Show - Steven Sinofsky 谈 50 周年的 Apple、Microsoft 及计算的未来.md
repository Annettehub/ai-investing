# Info

- Podcast: The a16z Show
- Episode: Steven Sinofsky on Apple at 50, Microsoft, and the Future of Computing
- Link: https://app.podwise.ai/dashboard/episodes/8127546
- Publish Time: 2026-06-02
- Save Time: 2026-06-13

# Summary

The transition of AI compute from hyperscale data centers to local devices marks a fundamental shift in personal computing, mirroring historical trends where resource-constrained tasks eventually move to the client. NVIDIA’s recent announcements at Computex, specifically the integration of ARM-based CPUs with advanced parallel processing, highlight this evolution toward AI-native hardware. While current industry efforts focus on maintaining backward compatibility with legacy Windows applications, this approach risks perpetuating existing system vulnerabilities and performance limitations. True progress requires moving beyond legacy constraints to embrace a sealed, optimized architecture that prioritizes local agent execution and privacy. Former Microsoft Windows division president Steven Sinofsky emphasizes that while the industry currently balances enterprise requirements with consumer needs, the future of computing lies in hardware specifically designed for efficient, local AI inference, effectively eliminating the costs associated with cloud-based token consumption.
> AI 计算从超大规模数据中心过渡到本地设备标志着个人计算的根本转变，反映了历史趋势，即资源受限的任务最终移向客户端。NVIDIA 在台北计算机博览会上的最新公告，特别是与先进并行处理相结合的 ARM 架构 CPU 的集成，突显了这一向 AI 本地硬件发展的演变。虽然当前行业努力保持与传统 Windows 应用程序的向后兼容性，但这一做法风险在于延续现有系统漏洞和性能限制。真正的进步需要超越传统限制，拥抱一种封闭的、优化的架构，优先考虑本地代理执行和隐私。前微软 Windows 业务部门总裁史蒂芬·西诺夫斯基强调，尽管行业目前平衡企业需求与消费者需求，但未来计算的发展在于专为高效、本地 AI 推理设计的硬件，从而有效消除与基于云的令牌消费相关的成本。

# Takeaways

* Whenever computing resource constraints become a financial burden, the technology inevitably shifts to the local device, transforming that resource into a free utility.
  > 当计算资源限制成为财务负担时，技术不可避免地转向本地设备，将该资源转化为免费工具。
* The transition to AI-native computing is defined by a fundamental shift in the primary compute burden from the CPU to graphics processors and specialized neural processing units.
  > 向人工智能原生计算的过渡定义为一种根本性的转变，即将主要计算负担从中央处理器转移到图形处理器和专业神经处理单元。
* The current reliance on cloud-based AI is gated by the cost of tokens, creating a strong market incentive to move AI inference to local hardware where compute becomes effectively free.
  > 当前对基于云的人工智能的依赖受到代币成本的限制，从而产生了强烈的市场激励，将人工智能推理转向本地硬件，在那里计算变得实际上是免费的。
* The PC industry's persistent focus on maintaining legacy software compatibility often prevents the adoption of more secure, efficient, and modern computing architectures.
  > 个人电脑行业持续关注维护老旧软件兼容性，往往阻碍了更安全、高效和现代计算架构的采用。
* NVIDIA has transitioned from an external component supplier to a primary architect of the personal computing ecosystem, directly influencing the integration of AI-optimized hardware.
  > NVIDIA 已从一个外部组件供应商转变为个人计算生态系统的主要架构师，直接影响了人工智能优化硬件的集成。
* Rapid advancements in inference pipeline optimization are expected to significantly lower the memory requirements for running sophisticated AI models on consumer-grade hardware.
  > 预计推理管道优化的快速进展将显著降低在消费级硬件上运行复杂人工智能模型的内存需求。
* Future personal computing will be dominated by autonomous agents that require specialized local hardware to perform complex, long-running tasks without the prohibitive costs associated with cloud-based inference.
  > 未来的个人计算将被要求专业本地硬件以执行复杂的、长时间运行的任务的自主代理主导，而不必承担与基于云的推理相关的高昂成本。
* The lack of hardware homogeneity in the PC market creates a significant barrier for consumers trying to identify devices capable of supporting high-performance AI workloads compared to more unified platforms.
  > 个人电脑市场缺乏硬件同质性，为消费者识别能够支持高性能人工智能工作负载的设备创造了显著障碍，相较于更统一的平台。

# Q & A

**Q: Why is the computing industry shifting AI workloads from the cloud to local devices?**
> **Q: 为什么计算行业将人工智能工作负载从云端转移到本地设备？**

A: The primary driver is the cost and availability of tokens. Currently, everyone is gated by the consumption of tokens, which cost money and are often unavailable if you’re trying to use them for free. If you want to run an agent that works for three days to figure out a complex travel itinerary, you don't want to end up with a $10,000 bill. By moving that compute to your local device, you essentially gain access to "infinitely free" tokens. This is a recurring pattern in computing history: whenever there is a resource constraint that you have to pay for, the compute eventually migrates to your local device and becomes free.
> A: 主要驱动因素是令牌的成本和可用性。目前，每个人都受限于令牌的消费，令牌需要花费金钱，并且如果你试图免费使用它们，往往是无法获得的。如果你想运行一个代理工作三天来制定复杂的旅行计划，你不想最终收到一份 10,000 美元的账单。通过将计算移至本地设备，你实际上获得了 “无限免费的” 令牌。这在计算历史上是一种反复出现的模式：每当必须付费的资源受到限制时，计算最终会迁移到本地设备，并变得免费。

---

**Q: What is the significance of the NVIDIA Spark Superchip announcement at Computex?**
> **Q: NVIDIA 在 Computex 上宣布的 Spark 超级芯片有什么意义？**

A: It represents a fundamental shift in how PCs are built. It is an Arm CPU mated with NVIDIA parallel processing graphics into a single system-on-a-chip, utilizing a completely new memory architecture. While the mainstream press viewed this as NVIDIA simply entering the PC business, it is actually an evolution of the compute burden shifting from the CPU to the GPU and neural processors. This is an incredibly important opportunity for the industry to make the PC forward-looking rather than backward-looking, moving away from the traditional ways we’ve built computers for the last 30 years.
> A: 这代表了个人电脑构建方式的根本转变。这是一个与 NVIDIA 平行处理图形相结合的 Arm CPU，采用全新的系统单芯片架构，使用完全新的内存架构。虽然主流媒体将其视为 NVIDIA 只是进入 PC 业务，但实际上这是计算负担从 CPU 转移到 GPU 和神经处理器的演变。这是行业一个极其重要的机会，可以使个人电脑面向未来，而不是面向过去，摆脱我们过去 30 年来构建计算机的传统方式。

---

**Q: Given current memory shortages, what is your outlook on the cost and availability of AI-native hardware?**
> **Q: 在当前内存短缺的背景下，您对人工智能原生硬件的成本和可用性有何展望？**

A: Having lived through about a half-dozen component shortages, my advice is to just wait them out. Whether it’s DRAM, hard drives, or processors, these cycles always correct themselves in short order. I have zero concern about memory constraints because the models themselves are also evolving. Every month, new research papers are published showing how to cleave giant parts off the inference pipeline, meaning we don't need nearly as much memory as people think. The hardware and software will adapt, and the problem will resolve itself.
> A: 经历过大约六次组件短缺后，我的建议是耐心等待。无论是 DRAM、硬盘还是处理器，这些周期总是会在短期内自行修正。我对内存限制毫不担心，因为模型本身也在不断演变。每个月都有新的研究论文发表，展示如何削减推理管道的大部分，这意味着我们并不需要像人们想象的那样多的内存。硬件和软件将适应，问题将得到解决。

---

**Q: Looking back, what was the original vision for the Surface, and why did it become a niche product?**
> **Q: 回顾一下，Surface 的最初愿景是什么，为什么它成为了一款小众产品？**

A: The original vision was to create a platform discontinuity—a move to mobile chips (Arm) and mobile form factors. We shipped it as a convertible tablet, but we also created an Intel x86-based version as an "objection handler" to address concerns about the lack of legacy software compatibility. Unfortunately, Microsoft eventually abandoned the Arm strategy for about eight years to focus on those x86 objection handlers. In my mind, that turned the subsequent Surface products into niche devices—they were just different Intel PCs that didn't fundamentally push the industry forward or change the paradigm.
> A: 最初的愿景是创造一个平台的不连续性——转向移动芯片（Arm）和移动形式因素。我们将其作为可转换平板电脑发布，但我们也创建了基于 Intel x86 的版本，作为应对缺乏传统软件兼容性担忧的 “异议处理程序”。不幸的是，微软最终放弃了 Arm 战略，专注于这些 x86 异议处理程序，持续了约八年。在我看来，这使得后来的 Surface 产品变成了小众设备——它们只不过是不同的 Intel 个人电脑，并未从根本上推动行业向前发展或改变范式。

---

**Q: Why is the industry's obsession with backward compatibility potentially holding back the PC?**
> **Q: 为什么行业对向后兼容性的痴迷可能会阻碍个人电脑的发展？**

A: We keep trying to make new PCs run every single app from the last 30 years, but users don't actually need that. By forcing backward compatibility, we retain the same old problems—fans, malware, and the ability for users to break the system by editing the registry or deleting system files. A truly forward-looking device should be a "sealed case" like a Mac or a phone, where you can't accidentally destroy the OS. We don't need to run legacy applications from 2003 on our local agent machines; we can just remote into them or run them in a VM. We should be focusing on the future, not clinging to the past.
> A: 我们一直在尝试让新 PC 运行过去 30 年的每一个应用，但用户实际上并不需要那样。通过强制向后兼容性，我们保留了旧问题——风扇、恶意软件以及用户通过编辑注册表或删除系统文件来破坏系统的能力。一款真正面向未来的设备应该像 Mac 或手机那样是一个 “密封外壳”，用户无法随意破坏操作系统。我们不需要在本地代理机器上运行 2003 年的遗留应用程序；我们完全可以远程使用它们或在虚拟机中运行。我们应该关注未来，而不是固守过去。

---

**Q: If you were recommending a PC today, what specifications should a user look for?**
> **Q: 如果今天要推荐一款电脑，用户应该关注什么规格？**

A: I would recommend a 16-gigabyte machine. While some devices try to get by with 8 gigabytes, it usually takes "techie work"—like uninstalling bloatware, managing background tasks, and tweaking system settings—to make that experience feel reasonable. That is not something you should ever ask a typical user to do. If you want a machine that works well without constant maintenance, 16 gigabytes is the baseline you should aim for.
> A: 我会推荐一台 16GB 的机器。虽然一些设备试图使用 8GB，但通常需要进行 “技术性工作”——比如卸载臃肿的软件、管理后台任务和调整系统设置——才能让使用体验变得合理。这绝不是你应该要求普通用户去做的事情。如果你希望一台机器能够正常运行而无需持续维护，16GB 是你应该追求的基本配置。

---

**Q: How will the integration of NVIDIA's CUDA APIs into the Windows ecosystem change the landscape?**
> **Q: NVIDIA 的 CUDA API 集成到 Windows 生态系统中将如何改变格局？**

A: NVIDIA has an enormous investment in open-source models and tuning them through their hardware. The big question is how these APIs will be implemented. Whether they become a native part of the OS, a standard download, or a thunking layer will determine how effective they are. For the PC, Microsoft is clearly embracing this, but for Apple, the question is whether they will allow these APIs to run natively at WWDC or force developers into their own proprietary stack. We are at a fork in the road, and the details of that implementation will define the next generation of AI-native computing.
> A: NVIDIA 在开源模型及其通过硬件调整中的巨额投资值得注意。大问题是这些 API 将如何实施。它们是成为操作系统的原生部分、标准下载，还是一个中间层，将决定它们的有效性。就个人电脑而言，微软显然对此表示拥抱，但对苹果而言，问题是他们是否允许这些 API 在 WWDC 上原生运行，或强迫开发者进入自己的专有堆栈。我们正处于一个重要的分水岭，那些实现细节将定义下一代人工智能原生计算。

# Keywords

|Keywords|Explanation|
|---|---|
|Computex|A major international trade show held in Taiwan, focusing on the computing and technology hardware ecosystem. It serves as a critical hub for companies to showcase components, chipsets, and manufacturing advancements within the global supply chain.|
|计算展|在台湾举行的主要国际贸易展会，专注于计算和技术硬件生态系统。它作为公司展示组件、芯片组和全球供应链制造进展的重要中心。|
|CUDA|A parallel computing platform and programming model created by NVIDIA. It allows software developers to use the power of graphics processing units for general-purpose computing tasks, which is essential for high-performance AI operations.|
|CUDA|由 NVIDIA 创建的并行计算平台和编程模型。它允许软件开发人员利用图形处理单元的强大功能进行通用计算任务，这对高性能 AI 操作至关重要。|
|Tokens|In the context of AI, tokens are the basic units of text or data that models process. Because AI services are often "gated" by the number of tokens consumed, there is a growing industry shift toward moving AI processing to local devices to avoid ongoing usage costs.|
|令牌|在 AI 的上下文中，令牌是模型处理的文本或数据的基本单元。由于 AI 服务通常受到消耗令牌数量的「限制」，因此有一个行业趋势，向将 AI 处理移至本地设备，以避免持续的使用成本。|
|Surface|A line of personal computing devices developed by Microsoft, ranging from tablets to laptops. The program was originally envisioned as a way to transition the PC industry toward mobile hardware and new, more portable usage scenarios.|
|Surface|微软开发的一系列个人计算设备，从平板电脑到笔记本电脑。该程序最初设想为将 PC 行业过渡到移动硬件和新的、更便携的使用场景的一种方式。|
|ARM|A type of processor architecture known for being highly power-efficient and ideal for mobile devices. It is increasingly being adopted in laptops and desktops as an alternative to traditional processors to improve battery life and thermal performance.|
|ARM|一种以高能效和适合移动设备而闻名的处理器架构。它越来越多地被笔记本电脑和台式计算机采用，作为传统处理器的替代方案，以提高电池续航和热性能。|
|DirectX|A collection of application programming interfaces (APIs) developed by Microsoft for handling tasks related to multimedia, especially graphics and game programming. It has been a foundational part of the Windows operating system for decades, ensuring software can communicate effectively with hardware.|
|DirectX|由微软开发的一组应用程序编程接口（API），用于处理与多媒体相关的任务，特别是图形和游戏编程。它几十年来一直是 Windows 操作系统的基础部分，确保软件能够有效地与硬件通信。|
|WWDC|An annual event hosted by Apple for software developers to learn about new technologies and updates for Apple platforms. It is a significant industry event where the company often announces major shifts in its operating systems and developer tools.|
|WWDC|苹果公司为软件开发人员举办的年度活动，了解苹果平台的新技术和更新。这是一个重要的行业活动，公司通常会在此宣布其操作系统和开发工具的重大变化。|
|Inference|The process of using a trained AI model to make predictions or generate content based on new input data. Moving this process from large, expensive data centers to a local device is a key trend in the evolution of personal computing.|
|推理|使用训练好的 AI 模型根据新输入数据进行预测或生成内容的过程。将这一过程从大型昂贵的数据中心移至本地设备是个人计算演进的一个关键趋势。|
|Registry|A hierarchical database in the Windows operating system that stores configuration settings and options for the operating system and installed applications. It is a powerful but sensitive component that, if modified incorrectly, can cause system instability.|
|注册表|Windows 操作系统中的一种层次数据库，用于存储操作系统和已安装应用程序的配置设置和选项。它是一个强大但敏感的组件，如果修改不当，可能会导致系统不稳定。|
|Hardcore Software|A blog and project by Steven Sinofsky that documents the history of software development at Microsoft. It provides detailed, firsthand insights into the creation and strategic management of major products like Windows and Office.|
|Hardcore Software|Steven Sinofsky 的一项博客和项目，记录了微软软件开发的历史。它提供了对 Windows 和 Office 等主要产品的创建和战略管理的详细第一手见解。|

# Highlights

- [(00:13)](https://app.podwise.ai/dashboard/episodes/8127546?locate=13) The world where you are gated on dollars per token is going to move to your own device, which is exactly what happened with all of computing.
  > 你所限制在每个代币上付费的世界将移至你自己的设备，这正是所有计算机所发生的事情。
- [(00:22)](https://app.podwise.ai/dashboard/episodes/8127546?locate=22) Anytime there is a resource constraint that you have to pay for, it moves to your device and becomes free.
  > 每当你必须支付的资源有限时，它就会移至你的设备并变得免费。
- [(26:23)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1583) What users really want is to not have backward compatibility; they just don't know it yet.
  > 用户真正想要的是不具备向后兼容性；他们只是还不知道而已。

# Transcript

## NVIDIA's RTX Spark Superchip and the Computex Ecosystem
> NVIDIA 的 RTX Spark 超级芯片与电脑展生态系统

Computex serves as the critical supply chain hub for the global computing industry. NVIDIA's recent announcement of the RTX Spark Superchip, a system-on-a-chip integrating ARM CPUs with parallel processing graphics, signals a major shift in PC architecture. This development mirrors historical industry milestones, moving beyond traditional x86 constraints to prioritize AI-native capabilities. The event highlights the growing importance of specialized hardware in the AI era, positioning NVIDIA as a central player in the personal computing supply chain.
> 电脑展是全球计算产业重要的供应链中心。NVIDIA 最近宣布的 RTX Spark 超级芯片是一款集成 ARM CPU 与并行处理图形的系统级芯片，标志着 PC 架构的重大转变。此项发展反映了行业历史里程碑的演变，超越了传统 x86 的限制，优先考虑 AI 原生能力。此次活动突显了专用硬件在 AI 时代日益重要的地位，使 NVIDIA 成为个人计算供应链的核心参与者。

**Steven Sinofsky:**
[(00:00)](https://app.podwise.ai/dashboard/episodes/8127546?locate=0)
Having lived through like a half dozen component shortage things,  you just sort of wait them out and you just let some local Macs or local men determine the future. This will all correct itself in short order. This world where you're all gated on dollars per token is a thing that's going to move to your own device,  which is exactly what happened with all of computing. Anytime there's a resource constraint that you have to pay for, it moves to your device and becomes free. AI introduces yet another opportunity to change that dynamic for the PC to have it be forward-looking, not backward-looking. And I think this is an incredibly important opportunity for Microsoft and for the industry as a whole.
> 经历过半打组件短缺事件后，你只能等待，任由一些当地的 Mac 或当地的人决定未来。这些很快就会自行调整。这个世界完全依赖每个代币的美元这一点，将会转移到你自己的设备上，这正是计算机发展的过程。每当有资源限制需要付费时，它就会转移到你的设备上并变得免费的。人工智能为个人电脑的动态变化提供了另一个机会，让其面向未来，而不是回顾过去。我认为这是微软以及整个行业一个极为重要的机会。

**Unknown Speaker:**
[(00:47)](https://app.podwise.ai/dashboard/episodes/8127546?locate=47)
Few people have had a front-row seat to the personal computing revolution quite like Steven Sinofsky. Over nearly three decades at Microsoft, he helped shape products that defined the PC era, including Windows, Office, and Surface. Along the way, he also witnessed one of the technology industry's longest-running rivalries, Microsoft and Apple. As Apple celebrates its 50th anniversary, questions about product design, platforms, hardware, software,  and the future of computing remain as relevant as ever. Theo Jaffee speaks with Steven Sinofsky about Apple, Microsoft, and the evolution of personal computing.
> 很少有人像史蒂文·西诺夫斯基那样直接经历个人计算革命。在微软近三十年的时间里，他帮助塑造了定义 PC 时代的产品，包括 Windows、Office 和 Surface。在这期间，他还见证了科技行业持续时间最长的竞争之一，微软与苹果。随着苹果庆祝其 50 周年纪念，关于产品设计、平台、硬件、软件以及未来计算的问题仍然显得尤为重要。西奥·贾菲与史蒂文·西诺夫斯基谈论苹果、微软及个人计算的演变。

**Steven Glinert:**
[(01:27)](https://app.podwise.ai/dashboard/episodes/8127546?locate=87)
I'm in the Situation Room with Steven Sinofsky,  who might have been like the first ever guest on MTS back when we were still doing test streams,  I think. He was the first person I interviewed on a test stream. He was the president of the Windows division at Microsoft. He created the Surface program at Microsoft, which we have some very interesting news about today. We're thrilled to have you on, Steven. Welcome to MTS. Welcome back.
> 我在情况室里，和史蒂文·西诺夫斯基在一起，他可能是我们还在做测试直播时 MTS 的第一个嘉宾，我想。他是我在测试直播中采访的第一人。他是微软 Windows 部门的总裁。他创建了微软的 Surface 项目，我们今天有一些非常有趣的消息。我们很高兴你能来，史蒂文。欢迎来到 MTS。欢迎回来。

**Steven Sinofsky:**
[(01:55)](https://app.podwise.ai/dashboard/episodes/8127546?locate=115)
Well, thanks so much. Good to see you.
> 嗯，非常感谢。很高兴见到你。

**Steven Glinert:**
[(01:58)](https://app.podwise.ai/dashboard/episodes/8127546?locate=118)
Hi, everyone. Yeah. First question would be NVIDIA and Microsoft and Arm and a few other companies just announced something very interesting at Computex. What exactly did they announce and what does it matter? Sure.
> 大家好。是的。第一个问题是 NVIDIA、微软、Arm 和其他几家公司刚刚在 Computex 上宣布了一些非常有趣的事情。他们到底宣布了什么，为什么这很重要？当然。

**Steven Sinofsky:**
[(02:16)](https://app.podwise.ai/dashboard/episodes/8127546?locate=136)
Well, just so folks know, because it doesn't get in the news much,  but Computex is this big giant trade show in Taiwan. And it's the weirdest show because it's like this total inside baseball You know, Silicon Supply Chain Show. And normally you never hear about it. Like, in fact, I never went to it even. I wanted to, but it actually turns out it was always right around the same time as a big Microsoft sales meeting. So I never went. But you can think of it as the ecosystem show for everything it takes to build a computing device of any kind. Totally well,  but Jensen in his keynote last night did this incredible slide where he walked up and down the whole length of the stage pointing to partners that he was very excited to be there.
> 好吧，大家知道一下，因为它新闻不多，但 Computex 是台湾一个大型的贸易展。这是最奇怪的展会，因为它就像是完全内行的，你知道，硅谷供给链展。而且通常你根本听不到它的消息。其实，我甚至从没去过这个展会。我想去，但实际上它总是在一个大型微软销售会议的时间段内。所以我从没去过。但你可以把它想象成构建任何计算设备所需的一切生态系统展。完全没问题，但詹森在昨晚的主旨演讲中展示了这个令人难以置信的幻灯片，他走上舞台的整个长度，指着他非常高兴的合作伙伴。

[(03:07)](https://app.podwise.ai/dashboard/episodes/8127546?locate=187)
And I would bet anyone that Anyone watching would have no idea who the companies he was pointing at. Half of the ones he pointed to as kind of being entertaining were just names of companies in traditional Chinese. You don't even know what they are. It's an incredible show. It's just wild because it's such inside baseball about components and peripherals and chipsets and assembly lines and deals and deals and stuff. And every 10 years or so, it jumps into the mainstream, but never like the past 24 hours. You never see that and actually it was a lot like I think it was two years ago Jensen keynoted CES and I I've been to 40 CES and I'd never seen one with such a broad media reach.
> 我敢打赌，所有观看的人根本不知道他指着的那些公司。他指向的一半公司名字用的是繁体中文。你甚至不知道它们是什么。这是一个令人难以置信的展会。这简直太疯狂了，因为这是关于组件、外设、芯片组和生产线、交易的内幕信息。而每过十年左右，它就会跳进主流，但从来没有像过去 24 小时那样。你从没见过那样，实际上我觉得就像两年前詹森在 CES 上做主旨演讲一样，我去过 40 届 CES，从未见过如此广泛的媒体覆盖。

**Steven Glinert:**
[(04:01)](https://app.podwise.ai/dashboard/episodes/8127546?locate=241)
Taylor Swift of the tech industry.
> 就像科技行业的泰勒·斯威夫特。

**Steven Sinofsky:**
[(04:05)](https://app.podwise.ai/dashboard/episodes/8127546?locate=245)
It's an incredible level of. It just speaks to the awareness of tech and then the awareness of AI and what NVIDIA has done. Because I mean, it was bigger than, like, CES Xbox was like a sideshow compared to this.
> 这是一个惊人的水平。这正是对科技的认知，以及对人工智能和 NVIDIA 所做的事情的认知。因为我认为，这比 CES 还要大，Xbox 在这次展会面前简直是个小场面。

**Steven Glinert:**
[(04:24)](https://app.podwise.ai/dashboard/episodes/8127546?locate=264)
Wow. And he's huge in China, too.
> 哇。他在中国也非常受欢迎。

**Steven Sinofsky:**
[(04:27)](https://app.podwise.ai/dashboard/episodes/8127546?locate=267)
Well, the show is always huge in Asia, broadly, because most of the companies are there,  whether they're in mainland or in Taiwan or in Vietnam or Singapore,  and that's sort of the origin of the show. Go there and speak in Asian language forever. So fascinating. So the big announce, though, I mean, look, there's a zillion things going on. But the one that rose to the top was Nvidia announcing what they called the RTX Spark Superchip,  which is a mouthful. Before the show, it was broadly called N1X. And that's sort of what it is. It's an arm. CPU mated with NVIDIA parallel processing graphics,  basically into one system on a chip that has a whole new memory architecture relative to the historic way that PCs had been built.
> 嗯，这个展会在亚洲一直都很大，因为大多数公司都在那里，无论是在大陆、台湾、越南还是新加坡，这就是这个展会的起源。去那里用亚洲语言讲个不停。真是令人着迷。不过大新闻是，我的意思是，发生了无数事情。但突出的事情是 NVIDIA 宣布了他们所称的 RTX Spark 超级芯片，真的是个绕口令。在展会之前，它通常被称为 N1X。这就是它的本质。它是一个处理器。CPU 与 NVIDIA 的并行处理图形基本合并成一个系统芯片，具有相对于传统 PC 构建的全新内存架构。

[(05:28)](https://app.podwise.ai/dashboard/episodes/8127546?locate=328)
And the target for it are the PC makers. And so it's very, very exciting. And if you, the mainstream press, the stock market press, the CNBC going on behind me,  like they all looked at this as like NVIDIA entering the PC business,  which is what's called the mainstream chip business. But which is so weird because, you know, long before in the Stone Ages,  which is now we're talking about 2011, we actually announced I'm involved in milking PCs and making the Surface computer,  the very first one. And it was a Computex big announcement, and it was a CES announcement, and it was,  you know,
> 目标人群是 PC 制造商。所以这非常令人兴奋。而且如果你看看主流媒体、股市媒体，CNBC 在我身后直播，他们都把这看成是 NVIDIA 进军 PC 业务，这被称为主流芯片业务。但这很奇怪，因为你知道，在石器时代，谈到的正是 2011 年，我们实际上宣布过我参与制作 PC 和 Surface 计算机，就是第一个。那是一个 Computex 的大新闻，也是 CES 的宣布，你知道，

[(06:13)](https://app.podwise.ai/dashboard/episodes/8127546?locate=373)
 I remember very vividly the partner slide had NVIDIA and Qualcomm and Texas Instruments and all the chip makers and PC makers. So it has a ring of familiarity at, I would imagine, like 1-100th the scale. I sent you the tech meme roll from that day when we announced the stuff and it was a pretty significant roll. So you'll be able to throw it up at some later date.
> 我还记得很清楚，合作伙伴幻灯片上有 NVIDIA、高通、德州仪器和所有芯片制造商和 PC 制造商。所以我想这带有熟悉感，可能就像 1/100 的规模。我给你发了那天我们宣布那些东西时的科技新闻快照，那个确实很重要。所以你可以在稍后的某个时间放上去。


---

## Transitioning AI Compute from Cloud to Local Devices
> 将 AI 计算从云端转移到本地设备

The compute burden is shifting from CPUs to GPUs and neural processors to enable local AI execution. Relying on cloud-based models creates a "token" bottleneck, where usage is gated by costs and availability. Moving AI tasks to local devices provides "infinitely free" tokens and enhances privacy. While current industry trends involve running agents on local hardware like Mac minis, the future of computing lies in optimizing AI stacks directly for local hardware, necessitating new operating system support and API standards for both Windows and macOS.
> 计算负担正在从 CPU 转移到 GPU 和神经处理器，以便实现本地 AI 执行。依赖基于云的模型会造成 “令牌” 瓶颈，其中使用受到成本和可用性的限制。将 AI 任务移到本地设备可提供 “无尽免费” 的令牌，并增强隐私。虽然当前行业趋势是让代理运行在本地硬件上，如 Mac mini，但未来计算的关键在于针对本地硬件优化 AI 堆栈，因此需要新的操作系统支持和 Windows 与 macOS 的 API 标准。

**Speaker 2:**
[(06:42)](https://app.podwise.ai/dashboard/episodes/8127546?locate=402)
Yeah. So in what way is this laptop more like AI native?
> 是的。那么这个笔记本在什么方面更像是 AI 本土？

**Steven Sinofsky:**
[(06:48)](https://app.podwise.ai/dashboard/episodes/8127546?locate=408)
So the big thing that's really changed is that the compute burden has shifted from the CPU to the graphics processor and then the associated neural processors,  TPUs and those chips. And that's the thing that really changed. It's not unlike Fifteen years ago,  what had changed was the bulk of the interesting processing had moved from the CPU to the GPU just for rendering. And where we are today is just an extension of all of that. And the difference, it's just insanely important because now that's the compute that we think everybody wants to do. Now, a lot of people will look at this and go, well, I use ChatGPT. I do it on my MacBook Air, my Chromebook, my phone. I don't really need another thing.
> 主要变化的地方在于计算负担已经从 CPU 转移到了图形处理器，以及相关的神经处理器、TPU 和那些芯片。这就是改变的地方。这和十五年前的变化类似，当时大部分有趣的处理工作已经从 CPU 转移到 GPU，仅仅是为了渲染。而我们今天所处的阶段只是所有这些的扩展。而且这个区别极其重要，因为现在我们认为人人都想要进行这种计算。现在，很多人看到这一点会说，哦，我用 ChatGPT。我在我的 MacBook Air、我的 Chromebook、我的手机上使用。我真的不需要别的东西。

[(07:39)](https://app.podwise.ai/dashboard/episodes/8127546?locate=459)
The problem is, and this might be a word you guys have used or heard before,  but the problem is tokens. And so the problem is that everybody is gated by the consumption of tokens,  which cost money, where you can't get them if you're trying to use them for free. And so the interesting thing about this device is how much of compute can it move to your local device,  where you basically have infinitely free tokens. And that is incredibly interesting and super important. Now, of course, you've all seen this run up to where we are today with the stacks of Mac minis. And everybody running their agents on minis. So why did they do that?
> 问题是，这可能是你们以前使用过或听说过的一个词，问题是代币。因此问题在于，每个人都受限于消耗代币，而代币是要花钱的，如果你试图免费使用是无法获得的。所以这个设备的有趣之处在于，它能将多少计算转移到你的本地设备上，在那里你基本上有无限免费的代币。这非常有趣且非常重要。当然，你们都看到了我们现在与 Mac Mini 堆叠的进展。所有人都在使用迷你设备运行他们的代理。那他们为什么要这么做呢？

[(08:24)](https://app.podwise.ai/dashboard/episodes/8127546?locate=504)
Well, there's a whole bunch of stuff about privacy and sandboxing them,  but the primary thing was if you just want to let something roll for three days while it figures out your best travel itinerary,  you really don't want to end up with a $10,000 bill. So instead you buy three minis and let it crank away with each mini putting something in isolation or whatever. But if you just fast forward, You know, six or nine months, it's abundantly clear. And I say that as a predictor of the future, not like as a,  it's obviously intellectually clear, but like,  it just seems to me that this world where you're all gated on dollars per token is the thing that's going to move to your own device.
> 好吧，有很多关于隐私和沙盒化的内容，但主要的原因是如果你只是想让某个东西运行三天，以便找到最佳旅行行程，你真的不想最后收到一张 $10,000 的账单。所以你买三个迷你设备，让每个设备各自进行隔离操作。但是如果你快进到六个月或九个月后，一切就变得非常清楚。我这么说是作为未来的预测，而不是以一种显而易见的智力清晰度，而是，在我看来，这个世界在 Token 的每美元都有门槛，这实际上是将转向你自己的设备。

**Speaker 2:**
[(09:06)](https://app.podwise.ai/dashboard/episodes/8127546?locate=546)
Yeah.
> 是的。

**Steven Sinofsky:**
[(09:07)](https://app.podwise.ai/dashboard/episodes/8127546?locate=547)
Which is exactly what happened with all of computing. Anytime there's a resource constraint that you have to pay for, it moves to your device and becomes free. And I just don't imagine, I don't know how it can happen.
> 这正是计算机技术发展过程中发生的事情。每当有需要付费的资源限制时，它就转移到你的设备上并变得免费。我想象不到，我不知道这怎么能发生。

**Steven Glinert:**
[(09:24)](https://app.podwise.ai/dashboard/episodes/8127546?locate=564)
Sure. So for someone who wants a more AI native device in like a year when all of these products have shipped,  do you think they're going to want like an NVIDIA Spark laptop or do you think they're going to want to stick with like MacBook Pro or the rumored MacBook Ultra,  which is supposed to come out later this year, early next year?
> 当然。那么对于那些希望在一年内拥有更具 AI 原生设备的人来说，当这些产品都发布时，你认为他们会想要像 NVIDIA Spark 笔记本电脑，还是更倾向于继续使用 MacBook Pro 或者传闻中的 MacBook Ultra，这款产品预期将在今年晚些时候或明年年初推出？

**Steven Sinofsky:**
[(09:42)](https://app.podwise.ai/dashboard/episodes/8127546?locate=582)
Well, this is just, I mean, this is the huge thing. And the way that I think this can play out is, well, of course,  you can play it out in, like, essentially status quo, which is, you know,  the Fortune 500, you know, 80, 20, 70, 30 rule will be able to just fad to Windows devices running Intel or maybe Spark devices running ARM,  but running with a Windows operating system. And then, you know, the cool people, the bosses, the elites or whatever you call it,  running their MacBook Pros with Chrome or Safari, just connecting things and phones. But there's another path where it becomes incredibly important to run highly optimized AI stack of software on your device.
> 好吧，这只是，我的意思是，这非常重要。我认为这一切的发展方式可以是，当然，你可以在基本的现状中进行，也就是，财富 500 强，80、20，70、30 的规则将只是逐渐被运行英特尔的 Windows 设备或许是运行 ARM 的 Spark 设备所取代，但运行的是 Windows 操作系统。然后，你知道，酷的人、老板、精英或者你称之为什么，正在用他们的 MacBook Pro 运行 Chrome 或 Safari，只是在连接各种设备和手机。但还有另一条路径，在这种情况下，运行高度优化的 AI 软件栈在你的设备上变得极其重要。

[(10:32)](https://app.podwise.ai/dashboard/episodes/8127546?locate=632)
And whatever that stack is, is going to get optimized for a particular hardware base. And that's the thing we've seen over and over again. Now,  where we are right now is just so interesting because we don't have enough information to know where things are heading. At the announcement last night and the press releases and the commentary, Microsoft made it clear,  much to my surprise, which we can go into,  that the NVIDIA stack of CUDA will be available and supported and part of this Spark. Now, there are a lot of ways for that to become true. It could be a download that just runs. It could be a thing that's installed, pre-installed on a Spark device.
> 无论那个栈是什么，都将针对特定的硬件基础进行优化。这正是我们一再看到的事情。现在，我们所处的这个时刻非常有趣，因为我们没有足够的信息来了解事情的走向。在昨晚的公告、新闻稿和评论中，微软明确表示，令我感到惊讶的是，我们可以深入探讨，NVIDIA 的 CUDA 栈将会在这个 Spark 上可用，并受到支持。现在，有很多方法可以实现这一点。这可能是一个可以直接运行的下载。这可能是一个安装在 Spark 设备上的预装程序。

[(11:13)](https://app.podwise.ai/dashboard/episodes/8127546?locate=673)
It could be A thing that's part of the OS and updated with Windows Update and administrative permissions and all of this other stuff. It could be a whole range of things that I still nobody knows yet in terms of public announcing how they're going to do that. The same thing holds for Apple. Today, on a Mac, you can run all the models locally and stuff like that. You can't really do that on a phone. An interesting question is going to be, what is Apple going to do at WWDC with respect to the CUDA APIs? Like, are they going to be native? Are they going to be a thunking layer? Lots of stuff could happen there. Are they distributed? Is it an app store app? Is it an OS component? Nobody has any idea.
> 这可能是操作系统的一部分，并随着 Windows 更新和管理权限等内容一起更新。这可能是一系列事情，目前还没有人知道具体会如何公开宣布实现。苹果也是如此。今天，在 Mac 上，你可以本地运行所有模型等东西。你在手机上真的无法做到这一点。一个有趣的问题是，苹果将在 WWDC 上对 CUDA API 采取什么措施？他们会是原生的吗？他们会是一个 thunking 层吗？很多事情都可能发生。他们是分布式的吗？是一个应用商店应用吗？是操作系统组件吗？没有人知道。

[(12:04)](https://app.podwise.ai/dashboard/episodes/8127546?locate=724)
Now, for both companies, the past is very interesting, and most people didn't live through this,  but NVIDIA has always been an outsider to the personal computer industry. It's always been an add-on. So on the PC, if you ever wanted to use an NVIDIA graphics card,  you bought the card and you downloaded drivers from NVIDIA. Or before that, they came on a CD or a floppy disk that came with your graphics card. And so for 30 years, this whole thing was like, do you have the latest NVIDIA drivers? Where do you get them? And we went from, you know, getting a new CD, to getting a new DVD,  to FTP, to downloading them from the web. It was a whole cycle,  but it was never a first-class part of Windows until we fixed that in Windows 7 and got them on Windows Update and all this other stuff.
> 对于这两家公司来说，过去非常有趣，而大多数人并没有经历过这一切，但 NVIDIA 一直是个人电脑行业的外来者。它一直都是一个附加组件。因此，在 PC 上，如果你想使用 NVIDIA 显卡，你需要购买显卡并从 NVIDIA 下载驱动程序。或者在此之前，它们会随显卡附带的 CD 或软盘中提供。所以在过去的 30 年里，整个过程就是：你有最新的 NVIDIA 驱动程序吗？你从哪里获得它们？我们经历了从获取新 CD，转向新 DVD，再到 FTP，最后下载到网页的过程。这是一个完整的周期，但在我们在 Windows 7 中修复之前，它从来不是 Windows 的一部分。

[(12:54)](https://app.podwise.ai/dashboard/episodes/8127546?locate=774)
And the APIs on a PC to do graphics, you could always just download the NVIDIA library and call them. But the official Windows APIs were DirectX. And they just did the same kind of thing, just completely differently. That the X is Xbox. And so Microsoft was all in on the DirectX APIs. They were a huge part of Windows release called Windows Vista. And when they first got integrated and then Windows 7 forward. Then there were the NVIDIA APIs, which at first were just the NVIDIA APIs. Then they became CUDA. Then for graphics, NVIDIA embraced this open thing called OpenGL. And then Apple went through the same exact thing. On the Mac, you could download drivers. You could install an NVIDIA card.
> 在 PC 上进行图形操作的 API，你始终可以下载 NVIDIA 库并调用它们。但官方的 Windows API 是 DirectX。它们做的事情相同，但方式完全不同。那个 X 就是 Xbox。所以微软全力以赴于 DirectX API。它们是 Windows 发布的一个重要部分，称为 Windows Vista。当它们首次整合进来，之后就是 Windows 7。然后是 NVIDIA API，最初只有 NVIDIA API。然后它们变成了 CUDA。然后对于图形，NVIDIA 拥抱了一个开放的东西，叫做 OpenGL。然后苹果经历了完全相同的事情。在 Mac 上，你可以下载驱动程序。你可以安装 NVIDIA 显卡。

[(13:45)](https://app.podwise.ai/dashboard/episodes/8127546?locate=825)
But the APIs, and then they supported OpenGL for a while. But they always wanted you to use their own stuff. And the phone did away with all of that. And Merrill did away with all that. And it was all in on Apple. Now, the good news for Apple was that native graphics were just outstanding. And they've always been great. On the PC side,  Intel was so far behind that it just kept pulling both NVIDIA and ATI slash AMD to be what you used if you used Photoshop or made movies or were just graphic intensive. And so in the next few weeks, we'll know what Apple is going to do for these APIs. And more importantly, the models themselves in the runtime.
> 但 API，然后它们一段时间支持 OpenGL。但他们始终希望你使用他们自己的东西。而手机则消除了所有这些。而 Merrill 则消除了所有这些。一切都在苹果之上。现在，对苹果来说，好消息是原生图形表现出色。而且他们一直表现得很棒。在 PC 方面，英特尔远远落后，这使得 NVIDIA 和 ATI slash AMD 成为你在使用 Photoshop、制作电影或需要大量图形处理时所使用的产品。因此在接下来的几周内，我们将知道苹果将对这些 API 做什么。更重要的是，运行时中的模型本身。

[(14:31)](https://app.podwise.ai/dashboard/episodes/8127546?locate=871)
I mean, NVIDIA has an enormous investment in the open source models and tuning them through their hardware. And the ecosystem has done a great job, as evidenced by the Mac minis,  of tuning those APIs for the Mac. But that has nothing to do with the phones. And so that's an operating system difference. And the number of phone people is large. And as we know, the hardware was the same. Now, it's not quite the same and blah, blah, blah, amount of memory, all that stuff. But it's very interesting to see the details of Microsoft and then what Apple chooses to do.
> 我是说，NVIDIA 对开源模型进行了巨大的投资，并通过他们的硬件进行了调优。整个生态系统做得很好，正如 Mac mini 上所证明的那样，为 Mac 调整这些 API。但这与手机无关。因此，这是操作系统的区别。手机用户的数量庞大。而我们知道，硬件是相同的。现在，它并不完全相同，以及 blah blah blah 的内存量，所有这些东西。但看到微软的细节，然后观察苹果的选择是非常有趣的。


---

## Balancing Backward Compatibility and Modern PC Architecture
> 平衡向后兼容性与现代 PC 架构

Component shortages, such as memory constraints, are temporary hurdles that will resolve as models become more efficient. While devices like the Dell XPS 13 offer high-end specs, the industry remains divided on the necessity of legacy support. The Surface program originally aimed to introduce a platform discontinuity by moving to ARM and mobile form factors, but the market continues to struggle with the tension between maintaining backward compatibility for enterprise software and adopting modern, secure, fanless architectures. Future PC success depends on prioritizing forward-looking, AI-native designs over legacy Windows dependencies.
> 组件短缺，如内存限制，是暂时的障碍，随着模型变得更加高效将得到解决。虽然像戴尔 XPS 13 这样的设备提供高端规格，但行业在旧版支持的必要性上仍存在分歧。Surface 计划最初旨在通过转向 ARM 和移动形态建立平台的不连续性，但市场在维护企业软件的向后兼容性和采用现代、安全、无风扇架构之间仍然存在紧张关系。未来 PC 的成功取决于优先考虑前瞻性、AI 原生设计，而非遗留的 Windows 依赖关系。

**Steven Glinert:**
[(15:10)](https://app.podwise.ai/dashboard/episodes/8127546?locate=910)
Right.
> 对。

**Speaker 2:**
[(15:12)](https://app.podwise.ai/dashboard/episodes/8127546?locate=912)
Like obviously we are seeing like a memory shortage, right? And like, so what do you expect the cost to a consumer of this kind of like,  you know, very AI native computing device to cost?
> 很明显，我们正面临内存短缺，对吧？所以你期望这类非常以 AI 为核心的计算设备对消费者的成本是多少？

**Steven Sinofsky:**
[(15:27)](https://app.podwise.ai/dashboard/episodes/8127546?locate=927)
Well, certainly for the, having lived through like a half dozen component shortage things,  you just sort of wait them out and you don't let some local max or local min determine the future. This will all correct itself in short order. The history of it, whether it's been DRAM or hard drives or processor shortage,  all of these things, we've had them come and go, or even smaller components. So I'm not worried about it at all. I mean, obviously, you know, if you're thinking that you need, you know,  96 or 128 gig for a standard consumer device versus say the eight on a MacBook Neo,  There's a huge difference. But also that will change in the models too.
> 好吧，当然，对于经历过数次组件短缺的人来说，你只是等着，看不让一些局部最大值或局部最小值决定未来。这一切都将很快自行纠正。不管是 DRAM、硬盘还是处理器短缺的历史，我们经历过这些问题，然后又消失，甚至更小的组件。所以我对此并不担心。我的意思是，显然，如果你认为你需要 96 或 128 GB 来配合标准消费者设备，而不是 MacBook Neo 上的 8 GB，这是个巨大的差异。但在模型中这也会有所变化。

[(16:12)](https://app.podwise.ai/dashboard/episodes/8127546?locate=972)
Like right now, the models themselves are all tuned to run in hyperscale data centers. And every month it seems like there's a new paper that says, oh,  we cleaved this giant thing off of the inference pipeline. So now we don't need nearly as much memory. So that all will get fixed. Not even an inkling of concern I have for that problem.
> 现在，模型本身都经过调优以在超大规模数据中心中运行。每个月似乎都有一篇新论文说，哦，我们从推断管道中剔除了这个庞然大物。所以现在我们不再需要这么多内存。所以这一切都会修复。对这一问题，我没有丝毫担忧。

**Steven Glinert:**
[(16:35)](https://app.podwise.ai/dashboard/episodes/8127546?locate=995)
So another thing that was just announced yesterday was last time we talked, you were very,  very excited about the MacBook Neo for Apple as like a category defining product. Dell just came out with a new XPS 13 that is, they say,  slightly better specs on Slightly better specs than the MacBook Neo,  and it's like $100 more expensive. So the Neo is like, what is it? It's $400 for students, $500 for everyone else.
> 所以昨天刚刚宣布的另一件事是，上次我们聊天时，你对苹果的 MacBook Neo 作为一个定义类别的产品非常兴奋。戴尔刚刚推出了一款新的 XPS 13，他们说规格稍微比 MacBook Neo 更好，而且价格比 MacBook Neo 贵了 100 美元。那么 Neo 是多少钱？学生的价格是 400 美元，其他人的价格是 500 美元。

**Steven Sinofsky:**
[(17:05)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1025)
It's $599, $699. $599, $699. Yeah. And then $499, $599, I think.
> 它的价格是 599 美元，699 美元。599 美元，699 美元。是的。然后是 499 美元，599 美元，我认为。

**Steven Glinert:**
[(17:13)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1033)
Yeah, the XPS 18 is $599, $699. MacBook Neo is $499, $599. Yeah. So what are your takes on this?
> 是的，XPS 18 售价 $599 和 $699。MacBook Neo 售价 $499 和 $599。是的。你对此有什么看法？

**Steven Sinofsky:**
[(17:25)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1045)
Well, first, kudos to Dell. Dell is just on an incredible roll. And Michael Dell is just a legendary CEO. And read his book, his second book that came out during the pandemic, I think,  or right after or right before. It's fantastic. The XPS 13 for a very long time was sort of my go-to laptop when friends and family and whatever would ask for one. It is like the best laptop and then it took a little bit of a dip and went in a funky way on design and it is actually back with a vengeance now. It is the laptop to get. Now this latest one is an attempt to build on that same chassis using Intel. You know, 30 years I can't keep track of the names. Panther Lake, Python Lake, Crystal Lake.
> 好吧，首先，祝贺戴尔。戴尔正处于一个令人难以置信的滚动状态。而迈克尔·戴尔则是一位传奇的首席执行官。推荐他在疫情期间出的一本书，我想，或者是前后刚发行的第二本书。非常棒。XPS 13 很长一段时间是我朋友和家人需要时的首选笔记本电脑。它是最好的笔记本电脑，后来设计上稍微有些变化，现在又重新回归了。现在它是必买的笔记本电脑。这一最新型号是在使用英特尔的同一机壳上进行的尝试。你知道的，三十年了，我都记不住名字。Panther Lake，Python Lake，Crystal Lake。

[(18:21)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1101)
I don't know what it is.
> 我不知道这是什么。

**Steven Glinert:**
[(18:22)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1102)
It's some lake.
> 这是某个湖。

**Steven Sinofsky:**
[(18:24)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1104)
Intel names are always places I've never been. Panther Lake. It's the Intel Rails. There's a lot of excitement about it. It does integrate some of the AI compute stuff into it. But it's not going to be the target machine that the PC ecosystem wants to sell. And its capabilities are going to be different from the ones that they do want to sell,  which is different than the Neo, which has the capabilities that We need to be targeted. So the Apple hardware line has a lot of homogeneity in it, in terms of capability. But PCs can become really hit or miss. And that's always been the difficulty in the PC ecosystem, is even when there's a winning machine,  it's not the one that when you walk into Best Buy and say, I need to buy a computer,
> 英特尔的名字总是一些我从未去过的地方。Panther Lake。这是英特尔的 Rails。对此有很多兴奋。它确实将一些人工智能计算的东西整合了进去。但这不会是 PC 生态系统想要销售的目标机器。它的能力和他们想要销售的那些机器会有所不同，而 Neo 具有我们需要的目标能力。所以苹果的硬件系列在能力方面有很多同质性。但 PC 可以真的很不稳定。这一直是 PC 生态系统中的难点，即使有一台获胜的机器，当你走进百思买说，我需要买台电脑时，

[(19:17)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1157)
 help me, Mr. or Mrs. Salesman, and then they just direct you to something based on Spiff Current ads or whatever. So we'll see. I'm sure it's a quality machine. You have the tech people on X talking about, you know, taking sides. It's either the Neo killer because it has an HDMI port or whatever,  or it's like embarrassing to the PC ecosystem because regardless it still runs Windows. Those extremes are stupid. Both the Neo and this machine are targeted at just people who need a computer. I think in five years, people who need a computer will also need a computer that runs agents. But the hardware software world will be unimaginably different in five years.
> 销售员会根据 Spiff 当前的广告或其他信息来推荐给你。所以我们拭目以待。我相信这是一台优秀的机器。X 上的技术人员在谈论，你知道，站队的问题。它要么是 Neo 杀手，因为它有 HDMI 端口，或者说它对 PC 生态系统很尴尬，因为无论如何它仍然运行 Windows。这些极端的说法很愚蠢。Neo 和这台机器都是针对那些需要电脑的人。我觉得五年之后，需要电脑的人也会需要能运行代理的电脑。但是五年后的硬件和软件世界将会有天壤之别。

[(20:09)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1209)
So this conversation has no relevance to the product lines that will be available in five years.
> 所以这个谈话与五年后将会有的产品线没有任何相关性。

**Steven Glinert:**
[(20:14)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1214)
So wow, it goes up to 32 gigs of RAM and a terabyte of storage. It starts at 8 gigs of RAM, which is like not great, I guess. That's not a good.
> 哇，它的内存最高可以达到 32GB，存储空间达到一 TB。它的起始内存是 8GB，这个我想不是很好。这个不太好。

**Steven Sinofsky:**
[(20:28)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1228)
That's not a good number for a PC. Yeah, the Mac will do 8. The PC is I, you know,  like I hate saying it because and I truly had a bunch of these over the past month,  six months or so. But I spent a lot of energy with our team on getting the memory down to two and four gigs at the time. But A is going to be hard. Now, Windows is doing a lot of work right now on that, so we'll see where that goes. But right now, if you ask me about what PC to buy, I would send you to a 16-gig PC. It takes work. It takes like techie work to get it down to be eight gig reasonable,  like uninstalling a bunch of stuff, banging around, stuff that you wouldn't, you shouldn't tell anyone to do.
> 这个对于 PC 来说不是一个好数字。是的，Mac 会配置 8GB。PC 是我，你知道，我不想这么说，但我过去一个月，过去六个月左右。但我花了很多精力和我们的团队一起将内存降到两 GB 和四 GB。但这会很困难。现在，Windows 正在为此做很多工作，所以我们拭目以待。但现在如果你问我该买什么 PC，我会推荐你买一台 16GB 的 PC。这需要工作。这需要一些技术性工作才能让它降到八 GB，像是卸载一大堆东西，搞一些你不应该让任何人做的事情。

**Steven Glinert:**
[(21:16)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1276)
Like which PC would you recommend? Like a specific laptop?
> 你推荐哪个 PC？像特定的笔记本电脑？

**Steven Sinofsky:**
[(21:20)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1280)
I would get a Dell XPS 13. What do you think about the Surface lineup? I'm obviously not objective about the Surface lineup. When we designed Surface, and I wrote like 80 million words on this, which everybody can go see on Hardcore Software. I'm not going to replay them here about what we did wrong and right,  but originally Surface was envisioned to be this platform discontinuity in PCs. It was going to be the move to mobile chips, ARM, and mobile form factors, like a tablet. We shipped it as a convertible tablet, but as a tablet. We actually did an Intel x86-based Surface, and at the time we called it an objection handler.
> 我会选择戴尔 XPS 13。你对 Surface 系列怎么看？我显然对 Surface 系列不是客观的。当我们设计 Surface 时，我写了大约 8000 万字，大家可以在 Hardcore Software 上看到。我不会在这里重述我们做错和对的东西，但最初 Surface 被设想成为 PC 的这种平台断裂。它将是移动芯片、ARM 和移动形态的转变，比如平板电脑。我们作为可转换平板电脑发布了它，但作为平板电脑。我们实际上做了一个基于 Intel x86 的 Surface，当时我们称之为反对意见处理器。

[(22:17)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1337)
And it was to handle the objection of things you didn't like about the ARM-based Surface. It didn't run existing software. It wasn't compatible with old software or whatever. And so my heart and the strategy for Arm was always to introduce this discontinuity where,  look, the world is different now. The hardware world is different now. The usage scenarios are different now. And portability is different. People want better battery life. They don't want fans. They don't want viruses and all that other stuff. Didn't work. I moved down to San Francisco area to chat to founders and stuff. And what Microsoft did was sort of basically abandon ARM for the next eight years or so.
> 这用于处理你对 ARM 架构 Surface 的不满。它不能运行现有软件。它与旧软件不兼容或者其他。所以我心中的 Arm 战略一直是要引入这种断裂，让大家看到，世界现在不同了。现在硬件世界不同了。使用场景现在不同了。便携性不同了。人们想要更好的电池续航。他们不想要风扇。他们不想要病毒和其他麻烦。这行不通。我搬到旧金山地区，与创始人们聊聊天。微软所做的基本上是抛弃了 ARM 大约八年左右。

[(23:08)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1388)
And focus on the objection handler side of things. So all the services that followed were, in my mind,  a niche product because they were just like different Intel PCs that weren't super important to me. I mean, I had brought each one of them, but they weren't important to me. AI introduces yet another opportunity to change that dynamic for the PC, to have it be forward-looking, not backward-looking. And I think this is an incredibly important opportunity for Microsoft and for the industry as a whole. But the wire, it's different like it was in 2011,  in that it's mobile chips and the scenarios are different,  even more so.
> 并专注于反对意见处理器的事情。在我看来，所有后续的服务都是小众产品，因为它们就像是其他不太重要的 Intel PC。意思是，我曾经买过每一款，但它们对我来说并不重要。AI 又提供了一个改变 PC 动态的机会，使其具有前瞻性，而不是回顾性。我认为这是微软以及整个行业一个非常重要的机会。但是与 2011 年相比，现在是不同的，因为它是移动芯片和不同的场景，更加不同。

[(23:52)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1432)
80% of the typical PC buyers are just running browser-based compute and they just want the keyboard,  the form factor, and they like Macs because they don't wear down over time. They have all their battery life for real. They have the viruses and malware, a whole different game. It's sort of this sealed case that we used to call it. PCs that did move to ARM also thwarted all of the Windows APIs,  which was the thing we chose not to do. So now, the new PCs running ARM are just the old PCs with the same viruses,  the same problems with fans, the same, you know, lack of quality over time. Like, you know, the classic Windows thing is, oh, you can just go edit the registry.
> 80% 的典型 PC 购买者仅仅是在运行基于浏览器的计算，他们只需要键盘、形态，并且他们喜欢 Mac，因其不会随时间而下降。它们的电池续航非常棒。它们有病毒和恶意软件，也完全是另一回事。这就像我们以前称之为密封的外壳。迁移到 ARM 的 PC 也阻止了所有 Windows API，这是我们选择不做的事情。所以现在，运行 ARM 的新 PC 只是旧 PC，带着相同的病毒、相同的风扇问题，以及，知道的，随着时间推移的质量缺失。比如，经典的 Windows 说法是哦，你可以去编辑注册表。

[(24:44)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1484)
Well, if you have an ARM PC, you can still go edit the registry,  and you can still hork your PC totally, and then you're screwed. And so I just don't think that backward looking is the thing,  which brings us to last night and all the X comments on the Spark laptops. And everybody immediately jumping to two things. First, NVIDIA announced that they're all going to run all existing Windows programs,  which of course just follows from Microsoft's strategy of porting Win32 to ARM,  which wasn't hard. We'd already done it. It was just opening up the dev tools and the ability to load the apps and things,  which we disabled for ARM because we wanted to move the ecosystem forward to a new OS API.
> 嗯，如果你有一台 ARM PC，你仍然可以去编辑注册表，你仍然可以完全搞砸你的 PC，那样的话你就完了。所以我只是不认为回头看是正确的，这把我们带到了昨晚所有关于 Spark 笔记本的 X 评论。每个人立刻跳回到两个问题上。首先，NVIDIA 宣布他们所有的产品将运行所有现有的 Windows 程序，这当然是微软移植 Win32 到 ARM 策略的延续，这并不困难。我们已经做到过了。这只是打开开发工具和加载应用的能力，我们禁用了 ARM 的这一功能，因为我们想让生态系统向新的操作系统 API 前进。

[(25:31)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1531)
But then the other part of this is just how you spin the whole thing in terms of backward compatibility. And then they said, oh, it runs every single app of all time. It's like, yeah, but you don't want to do that. And more importantly, the second thing is you don't need it anymore. But all of the enthusiasts are going nuts because they see it as Intel being replaced by Nvidia,  which is conceptually true, except not really. It's just an alternative. And what you're going to see in the marketplace is just sort of this Price comparison and Intel and NVIDIA are just going to drive the prices to each other and only one of them can really afford to battle.
> 但这件事情的另一部分就是如何将整个事情运转为向后兼容。然后他们说，哦，它支持所有历史应用。是的，但你不想那样做。更重要的是，第二件事情是你不再需要它了。但所有的爱好者们都在疯狂，因为他们看到 Intel 被 Nvidia 取代，虽然在概念上是对的，但并不完全如此。它只是个替代品。你将在市场上看到的只是价格对比，Intel 和 NVIDIA 只会把价格互相压低，只有一个他们能真正负担得起这场战斗。

[(26:20)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1580)
But that doesn't change the value proposition for consumers,  which is what they really want is to not have that backward compatibility. They just don't know it. They got a PC without a fan that you couldn't edit the registry, you couldn't break it,  you couldn't just go into the system folder and delete stuff. All of these things that you don't even think about on a Mac anymore and you don't even think about,  you can't even think about on a phone. You don't want them on the PC. And so it's tough for me to see Microsoft sort of embracing this because I mean,  I understand like if you want to sell the enterprise,  you have to run that VB app from 2003,  but that's not, you don't need to do that.
> 但这并没有改变消费者的价值主张，消费者真正想要的是没有向后兼容性。他们只是不知道这一点。他们得到了一台没有风扇的 PC，你无法编辑注册表，无法破坏它，不能随便进系统文件删除东西。所有这些你在 Mac 上不再考虑的事情，而在手机上甚至都无法想象。你不希望这些出现在 PC 上。所以我很难看着微软接受这一点，因为我明白如果你想进入企业市场，你必须运行 2003 年的 VB 应用，但那并不是，你不需要这样做。

[(27:03)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1623)
You could just put it on a server and remote into it. You could put it in a VM on an x86 machine. There's a million ways to do that. You just don't need to run it on the machine that you want to run your agents on. And in the short term, everybody is going to be running terminal anyway. And these agents and today's agents are all headless anyway. That will change too. But right now, We hit this fork in the road and Microsoft has already said the direction they want to take it,  which is they just want NVIDIA chips to do all the things that Windows has always done,  which always tests well with customers until you say the customer's like, yeah,  but those registry editors and admin scripts and stuff really screwed us up.
> 你可以把它放在服务器上，并远程连接。你可以把它放在 x86 机器的虚拟机中。有很多种方法可以做到这一点。你只需不在你想要运行代理的机器上运行它即可。而且在短期内，每个人都将使用终端。而这些代理，以及今天的代理，都是无头的。这也会改变。但现在，我们到了一个分岔路口，微软已经表示他们想要的方向，就是希望 NVIDIA 芯片执行 Windows 一直以来的所有功能，这在客户中测试效果很好，直到客户说，没错，但那些注册表编辑器和管理脚本之类的东西真的让我们陷入了麻烦。

[(27:49)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1669)
And like, we know, we know this. So it's tough for me to see.
> 我们知道，我们知道这一点。所以我很难看清楚。

**Steven Glinert:**
[(27:53)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1673)
Yep. Well, we're really excited for the NVIDIA Spark laptops to come out later this year. We'll see if it can replace my MacBook.
> 是的。好吧，我们非常期待今年晚些时候 NVIDIA Spark 笔记本的发布。我们看看它是否能取代我的 MacBook。

**Speaker 2:**
[(28:01)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1681)
Yeah.
> 是的。

**Steven Glinert:**
[(28:01)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1681)
I'm not sure. We'll see. Yeah, we'll do a tech review on stream.
> 我不太确定。我们拭目以待。是的，我们会在直播中做一个技术评测。

**Steven Sinofsky:**
[(28:05)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1685)
I mean,  you could see what it's going to be like if you just have the Spark that you could get from Dell today. That's the mini device. I have one of those and it's incredible. I mean, it's just it's my end of the tower as well.
> 我的意思是，如果你今天从戴尔获得 Spark，你可以看到它是什么样的。那是迷你设备。我有一个，真是不可思议。我的意思是，它也是我塔的终端。

**Steven Glinert:**
[(28:22)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1702)
Alright, well, we'll take a look at that. Steven, thank you so much for joining us.
> 好的，我们会看看这个。斯蒂文，非常感谢你加入我们。

**Steven Sinofsky:**
[(28:26)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1706)
Sure, thank you guys.
> 当然，谢谢你们。

**Unknown Speaker:**
[(28:30)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1710)
Thanks for listening to this episode of The a16z Podcast. If you liked this episode, be sure to like, comment, subscribe, leave us a rating or review,  and share it with your friends and family. For more episodes, go to YouTube, Apple Podcasts, and Spotify. Follow us on X at a16z and subscribe to our substack at a16z.substack.com. Thanks again for listening and I'll see you in the next episode. This information is for educational purposes only and is not a recommendation to buy,  hold, or sell any investment or financial product. This podcast has been produced by a third party and may include paid promotional advertisements,  other company references, and individuals unaffiliated with a16z.
> 感谢您收听这集的 The a16z Podcast。如果您喜欢这一集，请确保点赞、评论、订阅、留下评分或评论，并与您的朋友和家人分享。更多集数请前往 YouTube、Apple Podcasts 和 Spotify。在 X 上关注我们 @a16z，并在 substack 上订阅我们的内容 a16z.substack.com。再次感谢您的收听，我们下集再见。本信息仅用于教育目的，并不构成购买、持有或出售任何投资或金融产品的推荐。本播客由第三方制作，可能包含付费宣传广告、其他公司参考以及与 a16z 无关的个人。

[(29:10)](https://app.podwise.ai/dashboard/episodes/8127546?locate=1750)
Such advertisements, companies, and individuals are not endorsed by AH Capital Management LLC, a16z, or any of its affiliates. Information is from sources deemed reliable on the date of publication, but a16z does not guarantee its accuracy.
> 此类广告、公司和个人并未得到 AH Capital Management LLC、a16z 或其任何附属机构的认可。信息来源于发布时被认为可靠的来源，但 a16z 不保证其准确性。

