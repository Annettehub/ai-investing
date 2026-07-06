# Info

- Podcast: Fragmented - AI Developer Podcast
- Episode: 307 - Harness Engineering - the hard part of AI coding
- Link: https://app.podwise.ai/dashboard/episodes/7532722
- Publish Time: 2026-03-17
- Save Time: 2026-07-05

# Summary

The podcast explores "harness engineering," which involves shaping the environment around AI agents to ensure reliable performance in software development. It emphasizes that the role of engineers is shifting towards steering AI agents rather than writing code directly. Key aspects of shaping the harness include agent legibility, making code repositories more navigable for agents by creating structured documentation; closing feedback loops by providing agents with actionable test results, linters, and access to logs; and establishing persistent memory to prevent recurring errors. Further topics involve entropy control, which is maintaining code order and preventing documentation from becoming stale, and blast radius control, which is setting permissions to limit potential damage from agent errors. The discussion also touches on building custom harnesses tailored to specific enterprise needs, balancing the benefits of customization with the maintenance burden.
> 该播客探讨了 “线束工程”，它涉及塑造 AI 代理周围的环境，以确保其在软件开发中实现可靠的性能。 它强调工程师的角色正在转变为引导 AI 代理，而不是直接编写代码。 线束塑造的关键方面包括代理可读性，通过创建结构化文档使代码存储库对代理更易于导航； 通过向代理提供可操作的测试结果、linters 和对日志的访问来关闭反馈回路； 以及建立持久内存以防止再次发生错误。 进一步的主题包括熵控制，即维护代码顺序并防止文档变得陈旧，以及爆炸半径控制，即设置权限以限制代理错误可能造成的损害。 讨论还涉及构建针对特定企业需求量身定制的定制线束，从而在定制的益处与维护负担之间取得平衡。

# Takeaways

* Harness engineering focuses on shaping the environment around AI agents to ensure reliable performance, shifting the emphasis from model intelligence to the tools and feedback mechanisms available to the agent.
  > Harness 工程侧重于塑造 AI 代理周围的环境，以确保可靠的性能，从而将重点从模型智能转移到代理可用的工具和反馈机制。
* The role of the engineer is evolving from writing code to steering AI agents, requiring a focus on preventing code drift and breakage in agent-generated code.
  > 工程师的角色正在从编写代码演变为引导 AI 代理，需要专注于防止代理生成的代码中出现代码漂移和损坏。
* Agent legibility involves structuring code repositories to be easily navigable and understandable by AI agents, including comprehensive documentation and clear pathways for knowledge discovery.
  > 代理可读性涉及构建代码存储库，使其易于 AI 代理导航和理解，包括全面的文档和清晰的知识发现途径。
* Closing the feedback loop for AI agents requires actionable test outputs, clear error reporting, and integration with standard development tools like linters and static analysis to facilitate self-correction.
  > 闭环 AI 代理的反馈需要可操作的测试输出、清晰的错误报告以及与标准开发工具（如 linters 和静态分析）的集成，以方便自我纠正。
* Persistent memory systems are crucial for AI agents to avoid repeating past mistakes and to efficiently resume tasks, necessitating the creation of systems that record and recall design decisions and failure patterns.
  > 持久内存系统对于 AI 代理避免重复过去的错误并有效恢复任务至关重要，因此需要创建记录和回忆设计决策和失败模式的系统。
* Entropy control is essential in agent-generated code to prevent disorder and maintain code quality, requiring proactive measures to manage documentation drift and code proliferation.
  > 熵控制在代理生成的代码中至关重要，以防止混乱并保持代码质量，需要采取积极措施来管理文档漂移和代码扩散。
* Blast radius control involves implementing strict scope permissions and risk-aware checks to limit the potential damage AI agents can cause, particularly in sensitive areas of the codebase.
  > 爆炸半径控制涉及实施严格的范围权限和风险意识检查，以限制 AI 代理可能造成的潜在损害，尤其是在代码库的敏感区域。
* Building custom harnesses becomes necessary when generic AI tools are insufficient for specific enterprise needs, allowing for tailored workflows and greater confidence in agent behavior.
  > 当通用 AI 工具不足以满足特定企业需求时，构建自定义 Harness 变得必要，从而可以实现定制的工作流程并提高对代理行为的信心。
* As AI-generated code increases, the bottleneck shifts from code creation to code review, necessitating the development of AI-assisted review processes to ensure quality and prevent the introduction of errors.
  > 随着 AI 生成的代码的增加，瓶颈从代码创建转移到代码审查，因此需要开发 AI 辅助的审查流程，以确保质量并防止引入错误。
* The evolution from prompt engineering to context engineering to harness engineering reflects a progression towards managing the broader environment in which AI agents operate, rather than just individual interactions.
  > 从提示工程到上下文工程再到 Harness 工程的演变，反映了一种管理 AI 代理运行的更广泛环境的进展，而不仅仅是管理单个交互。

# Q & A

**Q: What is "harness engineering" in the context of AI development, and why is it becoming increasingly important?**
> **Q: 在人工智能开发中，什么是 “驾驭工程”？为什么它变得越来越重要？**

A: Harness engineering is essentially shaping the environment around an AI agent to ensure it acts reliably. It's important because, as AI models generate more code, the focus shifts from writing code to steering and controlling the agents to prevent code from drifting or breaking. The role of the engineer is evolving into more of a "steering" function, guiding the agents.
> A: 驾驭工程本质上是塑造 AI 代理周围的环境，以确保其行为可靠。这一点很重要，因为随着 AI 模型生成越来越多的代码，重点将从编写代码转移到引导和控制代理，以防止代码漂移或损坏。工程师的角色正在演变成更多的 “引导” 功能，引导代理。

---

**Q: How does harness engineering differ from previous approaches like prompt engineering and context engineering?**
> **Q: 驾驭工程与之前的提示工程和上下文工程等方法有何不同？**

A: Prompt engineering focused on crafting effective prompts, while context engineering dealt with managing and surfacing relevant context to the AI. Harness engineering takes a broader view, focusing on the entire environment in which the agent operates. It's about creating a reliable and controlled environment for the agent to function effectively, rather than just optimizing inputs or context.
> A: 提示工程侧重于制作有效的提示，而上下文工程则侧重于管理和呈现与 AI 相关的上下文。驾驭工程采取更广泛的视角，侧重于代理运行的整个环境。它旨在为代理创建一个可靠且受控的环境以有效运行，而不仅仅是优化输入或上下文。

---

**Q: What are the key components of "shaping the harness" in harness engineering, as discussed in the podcast?**
> **Q: 正如播客中所讨论的，在驾驭工程中，“塑造驾驭” 的关键组成部分是什么？**

A: There are five key areas: agent legibility (making the code base navigable for agents), closing the feedback loops (ensuring agents receive clear feedback on their actions, like test results), persistent memory (allowing agents to remember past decisions and failure patterns), entropy control (managing code disorder), and blast radius control (limiting the scope and permissions of agents to prevent catastrophic actions).
> A: 有五个关键领域：代理可读性（使代码库对代理可导航），闭环反馈（确保代理收到对其操作的明确反馈，例如测试结果），持久内存（允许代理记住过去的决策和失败模式），熵控制（管理代码混乱）和爆炸半径控制（限制代理的范围和权限，以防止灾难性操作）。

---

**Q: What is "agent legibility," and how can developers improve it within their code repositories?**
> **Q: 什么是 “代理可读性”，开发人员如何在其代码存储库中改进它？**

A: Agent legibility refers to making a code repository easily understandable and navigable for AI agents, not just humans. To improve it, create a well-organized documentation structure (like a "docs" folder) with overviews, design rules, and coding practices that agents can easily discover and understand. The agents.md file should act as a map for the agent to understand the repo.
> A: 代理可读性是指使代码存储库对于 AI 代理（而不仅仅是人类）来说易于理解和导航。为了改进它，创建组织良好的文档结构（例如 “docs” 文件夹），其中包含代理可以轻松发现和理解的概述、设计规则和编码实践。agents.md 文件应充当代理理解存储库的地图。

---

**Q: What does it mean to "close the feedback loop" for AI agents, and why is it crucial for reliable performance?**
> **Q: 为 AI 代理 “闭环反馈” 意味着什么？为什么它对于可靠的性能至关重要？**

A: Closing the feedback loop means ensuring an agent receives clear and actionable feedback when it makes a mistake. Tests are the baseline for feedback. The output from the tests needs to be clear enough for the agents to act on it. This allows the agent to learn from its errors and improve over time, rather than requiring constant human intervention. It's also important to provide access to logs and other debugging information.
> A: 闭环反馈意味着确保代理在犯错时收到清晰且可操作的反馈。测试是反馈的基准。测试的输出需要足够清晰，以便代理可以对其采取行动。这使代理能够从错误中学习并随着时间的推移进行改进，而无需持续的人工干预。提供对日志和其他调试信息的访问权限也很重要。

---

**Q: How can developers implement "entropy control" to manage the increasing disorder in codebases generated by AI agents?**
> **Q: 开发人员如何实施 “熵控制” 来管理由 AI 代理生成的代码库中不断增加的混乱？**

A: Entropy control involves actively managing the increasing disorder that can occur in codebases with AI-generated code. This can be done manually, through automation, or by using AI agents to maintain documentation, refactor code, and enforce coding standards. The key is to proactively address the drift and prevent the codebase from becoming a mess.
> A: 熵控制涉及主动管理 AI 生成代码的代码库中可能发生的不断增加的混乱。这可以通过手动、通过自动化或通过使用 AI 代理来维护文档、重构代码和执行编码标准来完成。关键是主动解决漂移，并防止代码库变得混乱。

---

**Q: What is "blast radius control," and how can developers prevent AI agents from causing catastrophic damage to their systems?**
> **Q: 什么是 “爆炸半径控制”，开发人员如何防止 AI 代理对其系统造成灾难性损害？**

A: Blast radius control is about limiting the scope and permissions of AI agents to prevent them from causing catastrophic damage. This involves setting up appropriate permissions, implementing risk-aware checks, and using approval gates to control what agents can do, especially in sensitive areas of the codebase. The goal is to prevent agents from accidentally deleting databases or making other irreversible changes.
> A: 爆炸半径控制是关于限制 AI 代理的范围和权限，以防止它们造成灾难性损害。这包括设置适当的权限、实施风险意识检查以及使用审批门来控制代理可以做什么，尤其是在代码库的敏感区域中。目标是防止代理意外删除数据库或进行其他不可逆转的更改。

---

**Q: What are some practical examples of how developers can engineer their systems to provide better feedback loops for AI agents?**
> **Q: 开发人员如何设计他们的系统以为 AI 代理提供更好的反馈循环的一些实际例子是什么？**

A: One example is ensuring that test outputs are clear and actionable for agents. Another is providing agents with access to logs, potentially through APIs or specialized tools like LogSQL. Additionally, integrating linters and static analysis tools into the development process can provide agents with immediate feedback on code quality.
> A: 一个例子是确保测试输出对于代理来说是清晰且可操作的。另一个是为代理提供对日志的访问权限，可能通过 API 或 LogSQL 等专用工具。此外，将 linters 和静态分析工具集成到开发过程中可以为代理提供关于代码质量的即时反馈。

---

**Q: Why is persistent memory important for AI agents, and what are some approaches to implementing it?**
> **Q: 为什么持久内存对于 AI 代理很重要？实施它的一些方法是什么？**

A: Persistent memory allows agents to remember past decisions, failure patterns, and design decisions, preventing both humans and agents from repeating the same mistakes. Approaches range from simple markdown files (like Claude's memory.md) to more sophisticated systems using vector databases and indexing processes. The goal is to hasten the process of getting the right answers quickly and more efficiently.
> A: 持久内存允许代理记住过去的决策、失败模式和设计决策，从而防止人类和代理重复同样的错误。方法范围从简单的 markdown 文件（如 Claude 的 memory.md）到使用向量数据库和索引过程的更复杂的系统。目标是加快快速有效地获得正确答案的过程。

---

**Q: What is the difference between simply adding information to an agents.md file and implementing a persistent memory system?**
> **Q: 简单地将信息添加到 agents.md 文件和实施持久内存系统之间有什么区别？**

A: While agents.md can provide initial instructions and context, a persistent memory system allows agents to learn and retain information over time. It's not just about starting net new. It is also about encoding past memory. This enables agents to make more informed decisions based on past experiences, rather than relying solely on the information provided in the agents.md file.
> A: 虽然 agents.md 可以提供初始指令和上下文，但持久内存系统允许代理随着时间的推移学习和保留信息。它不仅仅是关于启动新的网络。它还与编码过去的记忆有关。这使代理能够根据过去的经验做出更明智的决策，而不是仅仅依赖于 agents.md 文件中提供的信息。

---

**Q: What is the concept of "building the harness all together," and why might a company choose to do this instead of using generic AI tools?**
> **Q: 什么是 “整体构建安全网” 的概念？公司为什么选择这样做，而不是使用通用 AI 工具？**

A: "Building the harness all together" refers to creating a custom AI development environment tailored to a company's specific needs and processes. Companies might choose this approach when generic AI tools no longer suffice due to custom requirements, security concerns, or the desire to encode specific software engineering practices into the agent's workflow.
> A: “整体构建安全网” 指的是创建定制的 AI 开发环境，以满足公司特定需求和流程。当通用 AI 工具由于定制需求、安全问题或希望将特定软件工程实践编码到代理的工作流程中而不再足够时，公司可能会选择这种方法。

---

**Q: What are some examples of companies that have built their own harnesses, and what were their motivations?**
> **Q: 有哪些公司构建了自己的安全网的例子？他们的动机是什么？**

A: Stripe, for example, created "Stripe Minions," a fork of the Goose coding agent, to address their unique payment security requirements and internal tooling. They wanted to have greater confidence in the agent's behavior and customize the context surfacing and development environment to their specific needs.
> A: 例如，Stripe 创建了 “Stripe Minions”，这是 Goose 编码代理的一个分支，旨在解决他们独特的支付安全需求和内部工具问题。他们希望对代理的行为更有信心，并根据他们的特定需求定制上下文呈现和开发环境。

---

**Q: What are the potential benefits of building a custom AI development harness, such as the "superpowers" approach, for a company's software engineering process?**
> **Q: 构建定制的 AI 开发安全网（例如 “超能力” 方法）对公司的软件工程流程有哪些潜在好处？**

A: A custom harness can encode specific software engineering processes, ensuring that anyone using the agent at work naturally gravitates towards those practices. This can lead to increased trust in the agent's output, improved code quality, and greater consistency in the development process.
> A: 定制的安全网可以编码特定的软件工程流程，确保任何在工作中使用代理的人都会自然而然地倾向于这些实践。这可以提高对代理输出的信任度，提高代码质量，并提高开发过程的一致性。

---

**Q: What are the potential drawbacks or challenges of building a custom AI development harness?**
> **Q: 构建定制 AI 开发安全网有哪些潜在的缺点或挑战？**

A: The main challenge is the burden of maintaining the custom harness. The onus of maintaining that is also on you. Unlike using generic tools, the company is responsible for keeping the harness up-to-date and addressing any issues that arise. This requires dedicating a team to the task, making it more feasible for larger companies.
> A: 主要的挑战是维护定制安全网的负担。维护的责任也在于你。与使用通用工具不同，公司负责保持安全网的更新并解决出现的任何问题。这需要专门的团队来完成这项任务，对于较大的公司来说更可行。

---

**Q: How has the focus in AI-assisted development shifted over time, from prompt engineering to context engineering to harness engineering?**
> **Q: 随着时间的推移，在 AI 辅助开发中，焦点是如何从提示工程转移到上下文工程再到安全网工程的？**

A: The focus has shifted from optimizing prompts to managing context and now to shaping the entire environment in which the agent operates. Each step represents a different leverage point, moving from individual interactions to the overall system that supports the agent's work.
> A: 焦点已经从优化提示转移到管理上下文，现在转移到塑造代理运行的整个环境。每个步骤代表一个不同的杠杆点，从个人互动到支持代理工作的整个系统。

---

**Q: What is the potential evolution of the next step in AI-assisted development, and how can developers prepare for it?**
> **Q: AI 辅助开发的下一步潜在演变是什么？开发人员如何为此做好准备？**

A: The next step may involve building custom versions of open-source tools like Open Code, layering in company-specific processes and best practices. Developers can prepare by exploring these tools, experimenting with custom integrations, and understanding the unique needs of their organizations.
> A: 下一步可能涉及构建开源工具（如 Open Code）的自定义版本，并融入公司特定的流程和最佳实践。开发人员可以通过探索这些工具、试验自定义集成以及了解其组织的独特需求来做好准备。

---

**Q: What are the trade-offs between using generic AI tools and building a custom harness for software development?**
> **Q: 使用通用 AI 工具和构建自定义安全网进行软件开发之间有哪些权衡？**

A: Generic tools offer convenience and ease of use, but may not fully address specific company needs. Custom harnesses provide greater control and customization but require significant investment in development and maintenance. The choice depends on the company's resources, requirements, and long-term goals.
> A: 通用工具提供便利性和易用性，但可能无法完全满足特定公司的需求。自定义安全网提供更大的控制和定制，但需要在开发和维护方面进行大量投资。选择取决于公司的资源、需求和长期目标。

---

**Q: What are some specific examples of "closing the loop" that may not be immediately obvious?**
> **Q: 有哪些 “闭环” 的具体例子可能不容易立即显现出来？**

A: The output from the test needs to be clear enough for the agents to act on it. If you're depending on some tests that are not immediately actionable, or you need to inspect the results somewhere, maybe dumps the results into a file that the agent doesn't know where it is, these tests are not useful actually for the feedback loop.
> A: 测试的输出需要足够清晰，以便代理可以对其采取行动。如果你依赖于一些不能立即采取行动的测试，或者你需要检查某个地方的结果，也许将结果转储到一个代理不知道的文件中，那么这些测试实际上对于反馈循环没有用。

---

**Q: What is an example of blast radius control that Iury experienced?**
> **Q: Iury 经历过的爆破半径控制的例子是什么？**

A: Iury was trying this Gmail MCP the other day, like some time ago actually, and that's automated email drafting. It really had this draft feature. I said, okay, let me use the draft feature. But I think the thing just went on for some time. And then at some point I said, OK, let's just do this change and I think we're good. And then it did the change and he sent the email.
> A: Iury 前几天，大概是之前一段时间，尝试了这个 Gmail MCP，也就是自动电子邮件草稿。它确实有这个草稿功能。我说，好吧，让我使用草稿功能。但我认为事情持续了一段时间。然后在某个时候我说，好的，让我们做这个改变，我想我们很好。然后它做了改变，他发送了电子邮件。

---

**Q: How did Iury learn from his blast radius control experience?**
> **Q: Iury 是如何从他的爆破半径控制经验中学习的？**

A: I learned, OK, though, I have to actually not let it send the email like, you know, like in the permissions part. You would then do in this specific example is go and maybe either add an instruction or basically limit the permission so that you never. Allow the agent to send something. It can only make draft. You would only give it access to the draft permission. You would not give it access to the send permission, so to speak.
> A: 我了解到，好吧，我实际上不应该让它发送电子邮件，就像，你知道，在权限部分。在这种特定情况下，你会做的就是去，也许添加一个指令，或者基本上限制权限，这样你就永远不会。允许代理发送任何东西。它只能制作草稿。你只会授予它访问草稿权限的权限。你不会授予它发送权限，可以这么说。

# Keywords

|Keywords|Explanation|
|---|---|
|Harness Engineering|An approach to software development that focuses on shaping the environment around AI agents to ensure they act reliably. It involves providing agents with the right tools, feedback mechanisms, and human oversight to guide their actions effectively.|
|Harness 工程|一种软件开发方法，专注于塑造 AI 代理周围的环境，以确保它们可靠地行动。它包括为代理提供正确的工具、反馈机制和人工监督，以有效地指导它们的行为。|
|Agents.md|A file used to provide instructions, context, and guidance to AI agents working on a codebase. It acts as a central repository for information that helps agents understand the project's structure, coding practices, and specific tasks.|
|Agents.md|一个用于向处理代码库的 AI 代理提供指令、上下文和指导的文件。它充当信息的中央存储库，帮助代理理解项目的结构、编码实践和特定任务。|
|PR (Pull Request)|A request to merge new code changes into a main project repository. In the context of the podcast, AI agents are generating PRs, which engineers then review and refine.|
|PR（拉取请求）|将新代码更改合并到主项目存储库的请求。在播客的上下文中，AI 代理正在生成 PR，然后工程师会审查和改进这些 PR。|
|LogSQL|A tool mentioned in the podcast that is used to query and analyze logs. It helps developers extract relevant information from large log files, which can then be used to provide feedback to AI agents.|
|LogSQL|播客中提到的一种用于查询和分析日志的工具。它帮助开发人员从大型日志文件中提取相关信息，然后可以将其用于向 AI 代理提供反馈。|
|Agent Legibility|The concept of making a codebase and its associated documentation easily understandable and navigable for AI agents. This involves organizing information in a structured way, providing clear instructions, and ensuring that agents have access to all relevant knowledge.|
|代理可读性|使代码库及其相关文档易于 AI 代理理解和导航的概念。这包括以结构化方式组织信息、提供明确的指令，并确保代理可以访问所有相关知识。|
|Feedback Loops|The process of providing AI agents with information about their performance, allowing them to learn from their mistakes and improve over time. This can involve using tests, linters, static analysis tools, and access to logs.|
|反馈循环|向 AI 代理提供有关其性能的信息的过程，使它们能够从错误中学习并随着时间的推移而改进。这可能涉及使用测试、linter、静态分析工具以及访问日志。|
|Entropy Control|The practice of managing and mitigating the increasing disorder and complexity that can arise in a codebase, especially when AI agents are generating code. It involves implementing processes and tools to maintain code quality, prevent documentation from becoming stale, and avoid the proliferation of unnecessary functions.|
|熵控制|管理和减轻代码库中可能出现的日益增长的混乱和复杂性的实践，尤其是在 AI 代理生成代码时。它包括实施流程和工具来维护代码质量、防止文档变得过时以及避免不必要的功能的扩散。|
|Blast Radius Control|Implementing measures to limit the potential damage that an AI agent can cause if it makes a mistake or acts in an unintended way. This involves setting appropriate permissions, implementing risk-aware checks, and establishing approval gates to control what the agent can do, especially in sensitive areas of the codebase.|
|爆炸半径控制|实施措施以限制 AI 代理在犯错或以非预期方式行动时可能造成的潜在损害。这包括设置适当的权限、实施风险意识检查以及建立审批关口来控制代理可以做什么，尤其是在代码库的敏感区域中。|
|RAG (Retrieval-Augmented Generation)|A technique used in natural language processing where a model retrieves relevant information from an external knowledge source and uses it to generate more accurate and contextually appropriate responses.|
|RAG（检索增强生成）|自然语言处理中使用的一种技术，其中模型从外部知识源检索相关信息，并使用它来生成更准确和上下文相关的响应。|
|Stripe Minions|A custom coding agent developed by Stripe, forked from Goose, to address their specific payment security requirements and internal tooling needs. It represents an example of building a harness tailored to the unique challenges of a large enterprise.|
|Stripe Minions|Stripe 开发的自定义编码代理，从 Goose 分叉而来，旨在满足其特定的支付安全要求和内部工具需求。它代表了构建针对大型企业独特挑战量身定制的 harness 的一个例子。|
|Goose|An open-source coding agent from Block (formerly Square), serving as a base for custom solutions like Stripe Minions. It offers an alternative to commercial coding agents and allows for greater control and customization.|
|Goose|Block（前身为 Square）的一个开源编码代理，可作为 Stripe Minions 等定制解决方案的基础。它提供了商业编码代理的替代方案，并允许更大的控制和自定义。|
|Open Code|An open-source coding tool that can be customized and extended.|
|Open Code|一种可以自定义和扩展的开源编码工具。|
|Superpowers|A set of skills designed to enforce good software engineering practices. It prompts users to brainstorm, create execution plans, write tests, and use work trees.|
|Superpowers|一套旨在加强良好软件工程实践的技能。它提示用户集思广益、创建执行计划、编写测试和使用工作树。|

# Highlights

- [(02:51)](https://app.podwise.ai/dashboard/episodes/7532722?locate=171) It's like the role of the engineer is changing or that we don't, now that we don't really write the code as much, we're more working on this steering part. So we're steering the agents where it's moving.
  > 工程师的角色好像在改变，或者说我们现在不怎么写代码了，更多的是在做引导工作。所以我们在引导代理往哪里走。
- [(03:18)](https://app.podwise.ai/dashboard/episodes/7532722?locate=198) The bottleneck now is not if you can write the code, but it's like, how can you stop the code from drifting or breaking, because there's a lot more code going in.
  > 现在的瓶颈不是你会不会写代码，而是你如何阻止代码漂移或崩溃，因为有更多的代码进来了。
- [(06:04)](https://app.podwise.ai/dashboard/episodes/7532722?locate=364) You're riding this thing and you need to have the tools around it so you can point it to the right direction, so you can ride it in the right place, right?
  > 你在驾驭着它，你需要周围的工具，这样你才能把它指向正确的方向，这样你才能在正确的地方驾驭它，对吧？
- [(16:46)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1006) If you don't have a system of record or design decisions and some failure patterns, both humans and agents will keep paying for the same confusion over and over.
  > 如果你没有记录系统或设计决策以及一些失败模式，那么人类和代理都会一遍又一遍地为同样的困惑付出代价。
- [(22:51)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1371) It's not the junior's developer fault, it's like the person that gave him access to the database.
  > 这不是初级开发人员的错，而是给他访问数据库权限的人的错。
- [(23:03)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1383) If your agent is doing something catastrophic, it's not the agent's fault, actually. So you have to do something about that.
  > 如果你的代理做了一些灾难性的事情，实际上不是代理的错。所以你必须对此采取一些措施。

# Transcript

## Introduction to Harness Engineering: Enhancing Developer Productivity with AI
> Harness 工程简介：利用 AI 提高开发者生产力

Kaushik and Iury introduce the concept of harness engineering, focusing on leveraging AI to improve developer workflows. They highlight the shift towards using AI agents for code generation and the importance of creating a reliable environment for these agents. The discussion sets the stage for exploring the key aspects of harness engineering and its significance in modern software development.
> Kaushik 和 Iury 介绍了 Harness 工程的概念，重点在于利用 AI 来改善开发者的工作流程。他们强调了使用 AI 代理生成代码的转变，以及为这些代理创建可靠环境的重要性。讨论为探索 Harness 工程的关键方面及其在现代软件开发中的意义奠定了基础。

**Kaushik Gopal:**
[(00:04)](https://app.podwise.ai/dashboard/episodes/7532722?locate=4)
Welcome to Fragmented, an AI developer podcast that helps vibe coders become software engineers, one episode at a time. I'm your host, Kaushik.
> 欢迎来到 Fragmented，这是一个 AI 开发者播客，旨在帮助有想法的程序员成为软件工程师，每次一集。我是你们的主持人，Kaushik。

**Iury Souza:**
[(00:14)](https://app.podwise.ai/dashboard/episodes/7532722?locate=14)
And I'm Iury, the other host of Fragmented,  where I'd love to talk about using AI to make you a better developer.
> 我是 Iury，Fragmented 的另一位主持人，我很乐意讨论如何利用 AI 让你成为更好的开发者。


---

## The Rise of Harness Engineering: Steering AI Agents in Software Development
> Harness 工程的兴起：在软件开发中引导 AI 代理

The hosts discuss harness engineering, referencing an OpenAI post that emphasizes building an environment for reliable AI agents. They note that the core challenge is not code creation but ensuring agent reliability. The role of engineers is evolving towards steering agents, addressing code drift and breakage. The discussion highlights the shift from manual coding to managing AI-driven code generation.
> 主持人讨论了 Harness 工程，提到了 OpenAI 的一篇文章，该文章强调为可靠的 AI 代理构建环境。他们指出，核心挑战不是代码创建，而是确保代理的可靠性。工程师的角色正在演变为引导代理，解决代码漂移和损坏。讨论强调了从手动编码到管理 AI 驱动的代码生成的转变。

**Kaushik Gopal:**
[(00:21)](https://app.podwise.ai/dashboard/episodes/7532722?locate=21)
In the last episode, we talked a lot about the agents.md files specifically,  but in the grand scheme of things, that's just one piece of the puzzle. You threw this umbrella term called harness engineering. At least that's what the kids are calling it these days. I know you did a lot of research and you have a bunch of articles that you pulled from and there's some interesting things to talk about,  but maybe let's start by giving our listeners a sort of overview of what are the topics we're going to talk about specifically around harness engineering today.
> 在上一集中，我们主要讨论了 agents.md 文件，但从大局来看，这只是难题的一小部分。你提出了一个总称，叫做 harness engineering。至少现在孩子们是这么称呼它的。我知道你做了很多研究，也引用了很多文章，有很多有趣的东西可以讨论，但也许我们可以先给听众们一个关于今天我们要讨论的关于线束工程的具体话题的概述。

**Iury Souza:**
[(00:51)](https://app.podwise.ai/dashboard/episodes/7532722?locate=51)
So in this episode, we're going to cover what's harness engineering and why is this even important? So why are people talking about this at all and how to shape the harness and how to build it? Does that sound good?
> 所以在这一集中，我们将讨论什么是线束工程，以及为什么它如此重要？那么，为什么人们都在谈论这个，以及如何塑造线束和如何构建它？听起来不错吗？

**Kaushik Gopal:**
[(01:06)](https://app.podwise.ai/dashboard/episodes/7532722?locate=66)
Yeah, that sounds good.
> 嗯，听起来不错。

**Iury Souza:**
[(01:07)](https://app.podwise.ai/dashboard/episodes/7532722?locate=67)
I think the first one is very important, right? Why does this matter, right?
> 我认为第一个问题非常重要，对吧？为什么这件事很重要，对吧？

**Kaushik Gopal:**
[(01:11)](https://app.podwise.ai/dashboard/episodes/7532722?locate=71)
Yeah. Why even talk about this?
> 是的。为什么还要谈论这个？

**Iury Souza:**
[(01:13)](https://app.podwise.ai/dashboard/episodes/7532722?locate=73)
So there was this open AI post with this very name, right, called harness engineering. That actually helps explain this really well. I think it's also interesting because they're showcasing something that they did with a real product. It's their code base for codecs that they use as reference for this article. So they have like over one million lines of code and they claim that's zero manually written, like 1,500 PRs merged. So apparently this is the real deal for them. And what it turns out that the hard part was not actually creating the code,  but it's basically building the environment that makes the agents reliable.
> 所以 OpenAI 发布了一篇帖子，用的就是这个名字，叫做线束工程。这篇文章实际上很好地解释了这个问题。我认为这很有趣，因为他们展示了他们用真实产品做的一些事情。这是他们用于编解码器的代码库，他们用作本文的参考。所以他们有超过一百万行的代码，他们声称这些代码都是零手动编写的，合并了大约 1500 个 PR。所以显然这对他们来说是真实存在的。结果发现，困难的部分实际上不是创建代码，而是构建一个使 agent 可靠的环境。

**Kaushik Gopal:**
[(01:58)](https://app.podwise.ai/dashboard/episodes/7532722?locate=118)
An intentional effort on their end, right? If we were to move in this direction where the agent basically builds the entire product,  what are the problems we run into and how do we alleviate and remove those problems for the agent as we go along?
> 这是他们有意的努力，对吧？如果我们要朝着 agent 构建整个产品的方向发展，我们会遇到什么问题，以及如何减轻和消除 agent 在开发过程中遇到的这些问题？

**Iury Souza:**
[(02:12)](https://app.podwise.ai/dashboard/episodes/7532722?locate=132)
It's a very big shift in the way you do things, right? You actually have to attempt to not manually touch it.
> 这是一种做事方式上的巨大转变，对吧？你实际上必须尝试不手动去修改它。

**Kaushik Gopal:**
[(02:19)](https://app.podwise.ai/dashboard/episodes/7532722?locate=139)
Right.
> 对。

**Iury Souza:**
[(02:20)](https://app.podwise.ai/dashboard/episodes/7532722?locate=140)
And then the problems start showing up and then you have to kind of figure how to solve them. So that's a very interesting case study.
> 然后问题开始显现，然后你必须想办法解决它们。所以这是一个非常有趣的案例研究。

**Kaushik Gopal:**
[(02:28)](https://app.podwise.ai/dashboard/episodes/7532722?locate=148)
One point that stood out in that post that I thought was interesting was they said explicitly throughout the week,  they would basically use agents to generate the PRs,  but then they would spend about a good 20% trying to clean up and make sure that they course correct and then add those corrections into the system.
> 我觉得那篇文章中有一个亮点很有趣，他们明确表示，在一周内，他们基本上会使用代理来生成 PR，但他们会花大约 20% 的时间来清理，确保他们纠正方向，然后将这些更正添加到系统中。

**Iury Souza:**
[(02:45)](https://app.podwise.ai/dashboard/episodes/7532722?locate=165)
Right. And that's basically what We gave birth to this harness engineering thing, right?
> 对。这基本上就是我们创造 harness engineering 的原因，对吧？

**Kaushik Gopal:**
[(02:50)](https://app.podwise.ai/dashboard/episodes/7532722?locate=170)
Exactly, exactly.
> 完全正确。


---

## Code Review Challenges in the Age of AI: Focusing on Agent Improvement
> AI 时代的代码审查挑战：关注代理改进

The conversation shifts to the challenges of reviewing code generated by AI agents, especially with a high volume of pull requests. The hosts suggest focusing on improving agents' ability to review code, rather than relying solely on human review. This approach aims to ensure code quality and prevent errors in an environment where AI generates a significant portion of the codebase.
> 对话转向了审查由 AI 代理生成的代码的挑战，尤其是在有大量 Pull Request 的情况下。主持人建议关注于提高代理审查代码的能力，而不是仅仅依靠人工审查。这种方法旨在确保代码质量，并在 AI 生成大部分代码库的环境中防止错误。

**Iury Souza:**
[(02:51)](https://app.podwise.ai/dashboard/episodes/7532722?locate=171)
It's like the role of the engineer is changing or that we don't,  now that we don't really write the code as much,  we're more working on this steering part. So we're steering the agents where it's moving.
> 这就像工程师的角色正在改变，或者说我们，既然我们不怎么写代码了，我们更多的是在做这个引导部分。所以我们在引导 agent 的走向。

**Kaushik Gopal:**
[(03:05)](https://app.podwise.ai/dashboard/episodes/7532722?locate=185)
That's like a mic drop moment, by the way. Just casually.
> 顺便说一句，这就像一个精彩的时刻。只是随意地说说。

**Iury Souza:**
[(03:09)](https://app.podwise.ai/dashboard/episodes/7532722?locate=189)
Just casually.
> 只是随意地说说。

**Kaushik Gopal:**
[(03:10)](https://app.podwise.ai/dashboard/episodes/7532722?locate=190)
Yeah, you know, humans don't write code anymore. The agents are, so.
> 是的，你知道，人类不再编写代码了。agent 正在编写，所以。

**Iury Souza:**
[(03:16)](https://app.podwise.ai/dashboard/episodes/7532722?locate=196)
No, Inshallah. But yeah, that's pretty much it. The bottleneck now is not if you can write the code, right? But it's like, how can you stop the code from drifting or breaking, you know,  because there's a lot more code going in.
> 不，Inshallah。但是，是的，差不多就是这样。现在瓶颈不在于你是否能编写代码，对吧？而是，你如何阻止代码漂移或崩溃，你知道，因为有更多的代码进入。

**Kaushik Gopal:**
[(03:29)](https://app.podwise.ai/dashboard/episodes/7532722?locate=209)
Man, this is something we should talk about in a future episode too. How do we even approach the review of all of that code, right?
> 伙计，这是我们将来也应该在节目中讨论的事情。我们该如何审查所有这些代码呢，对吧？

**Iury Souza:**
[(03:36)](https://app.podwise.ai/dashboard/episodes/7532722?locate=216)
Oh, that's a big one.
> 哦，这可是个大问题。

**Kaushik Gopal:**
[(03:37)](https://app.podwise.ai/dashboard/episodes/7532722?locate=217)
Generating the code is so easy, but how do you actually review it? There's a general theme where everyone is like, yes,  at least the human should review the code and make sure slop doesn't go in. But, you know, when you have a thousand PRs coming your way,  no chance you're going to be even doing a good job of reviewing. At that point, it's better to think about how can we get agents to focus? How do we make the agents better at reviewing the code?
> 生成代码很容易，但你如何真正审查它呢？有一个普遍的主题，每个人都认为，至少人类应该审查代码，并确保不会出现低级错误。但是，你知道，当有成千上万个 PR 向你涌来时，你根本不可能做好审查工作。在这一点上，最好考虑如何让 agent 集中注意力？我们如何使 agent 更好地审查代码？


---

## Defining Harness Engineering: Shaping the Environment for Reliable AI Agent Action
> 定义 Harness 工程：塑造可靠的 AI 代理行动的环境

Iury defines harness engineering as shaping the environment around an AI agent to ensure reliable action. This involves leveraging tools, commands, sub-agents, context, and instructions. The focus shifts from model intelligence to the tools available and feedback mechanisms. The "harness" metaphor is explained, likening it to straps used to steer a horse, emphasizing control and direction.
> Iury 将 Harness 工程定义为塑造 AI 代理周围的环境，以确保可靠的行动。这涉及到利用工具、命令、子代理、上下文和指令。重点从模型智能转移到可用的工具和反馈机制。“Harness” 的比喻被解释为类似于用来引导马的缰绳，强调控制和方向。

**Iury Souza:**
[(03:59)](https://app.podwise.ai/dashboard/episodes/7532722?locate=239)
Yeah, that's a Let's go now into the what is hardness engineering. I don't know exactly where I got this from,  but it's basically this idea of shaping the environment around the agent so that it can act reliably.
> 是的，让我们现在进入什么是 hardness engineering。我不太清楚我从哪里得到这个概念的，但它基本上是指塑造 agent 周围的环境，使其能够可靠地行动。

**Kaushik Gopal:**
[(04:17)](https://app.podwise.ai/dashboard/episodes/7532722?locate=257)
Shaping the environment around the agent.
> 塑造 agent 周围的环境。

**Iury Souza:**
[(04:19)](https://app.podwise.ai/dashboard/episodes/7532722?locate=259)
Yeah. If you think about it, you know, like with all the tools and the knobs that they give us,  so for example,  skills and commands and sub-agents and context and All the instructions around the agent and the tools that the agent have available. Yeah, so this shifts the focus away from how smart is the model towards like,  what tools does he have and how does he get feedback? And when does the human step in?
> 是的。如果你考虑一下，你知道，就像他们给我们的所有工具和旋钮一样，例如，技能和命令以及子 agent 和上下文以及围绕 agent 的所有指令以及 agent 可用的工具。是的，所以这会将重点从模型的智能程度转移到它拥有哪些工具以及它如何获得反馈？以及人类何时介入？

**Kaushik Gopal:**
[(04:48)](https://app.podwise.ai/dashboard/episodes/7532722?locate=288)
And this is interesting because there's a different school of thought where, you know,  you can think that the models will keep getting better. So you don't need to focus as much. You know, the models will just know how to do it. That's one school of thought. You know, as is the case with most things in AI, right? We don't know where we're going to land into this year. We might come up with some super GPT-6 or, you know, I don't know,  Opus 5, and suddenly the models have become so good and you no longer need to bother about these things. But we never know, at least as it stands today. If you want to get good results, it makes a lot of sense to focus on shaping this environment,  like you put it.
> 这很有趣，因为有一种不同的思路，你知道，你可以认为模型会不断变得更好。所以你不需要太关注。你知道，模型会知道如何做。这是一种思路。你知道，就像人工智能中的大多数事情一样，对吧？我们不知道今年我们会走到哪一步。我们可能会推出一些超级 GPT-6，或者，你知道，我不知道，Opus 5，突然模型变得非常好，你不再需要为这些事情烦恼。但我们永远不知道，至少就目前而言。如果你想获得好的结果，那么专注于塑造这个环境是很有意义的，就像你所说的那样。

**Iury Souza:**
[(05:21)](https://app.podwise.ai/dashboard/episodes/7532722?locate=321)
It's I think that's what we try to do in this pod, right? We're trying to be very pragmatic about these tools and the current state of because no one actually knows where we're going. So, yeah. So this is the whole idea of harness engineering. But I also like I'm not a native speaker. Right. So. When I first heard the word harness, I was kind of confused. I think I probably first heard it on the context of AI. So I was like, what the hell is a harness? So for the non-native speakers out there, but one of the interesting meanings I found It's the one that it's talking about,  you know, the straps you put around a horse, for example, when you want to steer it,  to control it.
> 我认为这就是我们在这个播客中尝试做的事情，对吧？我们正在尝试对这些工具和当前的状态采取非常务实的态度，因为实际上没有人知道我们将走向何方。所以，是的。这就是 harness engineering 的全部理念。但我也喜欢，我不是母语人士。对。所以。当我第一次听到 harness 这个词时，我有点困惑。我想我可能第一次是在人工智能的语境中听到它的。所以我在想，harness 到底是什么？所以对于那些非母语人士来说，我发现的一个有趣的含义是，它指的是你放在马身上的带子，例如，当你想要控制它时，控制它。

**Kaushik Gopal:**
[(06:03)](https://app.podwise.ai/dashboard/episodes/7532722?locate=363)
So the model is the horse here, basically.
> 所以这里模型基本上就是马。

**Iury Souza:**
[(06:04)](https://app.podwise.ai/dashboard/episodes/7532722?locate=364)
You're riding this thing and you need to have the tools around it so you can point it to the right direction,  so you can ride it in the right place, right?
> 你正在骑着这个东西，你需要有它周围的工具，这样你才能把它指向正确的方向，这样你才能把它骑到正确的地方，对吧？

**Kaushik Gopal:**
[(06:13)](https://app.podwise.ai/dashboard/episodes/7532722?locate=373)
Let go of that harness and, you know, you'll fall off that horse, basically.
> 放开那个 harness，你知道，你基本上会从那匹马上掉下来。

**Iury Souza:**
[(06:17)](https://app.podwise.ai/dashboard/episodes/7532722?locate=377)
Exactly. Oh, that's a good one. Cool.
> 完全正确。哦，这说得很好。酷。


---

## Shaping vs. Building the Harness: Two Approaches to Harness Engineering
> 塑造 vs. 构建 Harness：Harness 工程的两种方法

The hosts divide harness engineering into two main approaches: shaping the harness and building the harness. Shaping involves optimizing the environment around the model, while building involves creating custom tools. The episode will focus on shaping the harness, as it is currently more practical and effective, while also touching on the concept of building the harness.
> 主持人将 Harness 工程分为两种主要方法：塑造 Harness 和构建 Harness。塑造涉及到优化模型周围的环境，而构建涉及到创建自定义工具。本集将侧重于塑造 Harness，因为它目前更实用和有效，同时也涉及构建 Harness 的概念。

**Kaushik Gopal:**
[(06:19)](https://app.podwise.ai/dashboard/episodes/7532722?locate=379)
We mentioned this briefly at the start, Iury,  but I think it's important now to split or fork harness engineering into two things. One is shaping the harness like we talked about. These are the things that you do around the model to help it get better. But there's the other approach too, which is building the harness itself. And this is more like if you wanted to build your own version of cloud code or open code or whatever. So in this episode, what I thought it would make sense to do is We're going to split the episode into two parts. The first we're going to talk about shaping the harness because that feels like the most useful and effective to do now.
> Iury，我们在开始时简要地提到了这一点，但我认为现在将 harness engineering 分成两件事很重要。一个是像我们讨论的那样，塑造 harness。这些是你围绕模型所做的事情，以帮助它变得更好。但还有另一种方法，那就是构建 harness 本身。这更像是如果你想构建自己的 cloud code 或 open code 或其他什么。所以在这一集中，我认为有意义的做法是将这一集分成两部分。首先我们将讨论塑造 harness，因为这感觉是现在最有用和最有效的方法。

[(06:57)](https://app.podwise.ai/dashboard/episodes/7532722?locate=417)
So we'll spend a majority of our time there,  but we'll also touch on this concept of building the harness all together. OK, let's talk about shaping the harness, which is the first big area to speak here in harness engineering. What does that actually look like in practice? And I think in your newsletter, Iury, which again we'll add a link to that in the show notes,  We pointed towards these five areas or themes, so to speak, around shaping the harness. And I liked how you structured those. So maybe we just jump right in and talk about each of those five areas.
> 所以我们将在那里花费大部分时间，但我们也会触及完全构建 harness 这个概念。好的，让我们来谈谈塑造 harness，这是 harness engineering 中要说的第一个大领域。这在实践中到底是什么样的？我认为在你的时事通讯中，Iury，我们再次在节目说明中添加了一个链接，我们指出了围绕塑造 harness 的这五个领域或主题。我喜欢你构建这些的方式。所以也许我们直接跳进去谈谈这五个领域中的每一个。


---

## Agent Legibility: Making Code Repositories Navigable for AI Agents
> 代理可读性：使代码仓库对 AI 代理可导航

The discussion begins with the first theme in shaping the harness: agent legibility. This involves making knowledge accessible to AI agents by ensuring that repositories are navigable not just for humans but also for agents. Information in Slack, personal knowledge, or random docs is unusable by agents. The goal is to encode and integrate this knowledge into the codebase for agent accessibility.
> 讨论从塑造 Harness 的第一个主题开始：代理可读性。这涉及到通过确保仓库不仅对人类而且对代理可导航，从而使知识对 AI 代理可访问。Slack 中的信息、个人知识或随机文档对代理来说是不可用的。目标是将这些知识编码并整合到代码库中，以供代理访问。

**Iury Souza:**
[(07:30)](https://app.podwise.ai/dashboard/episodes/7532722?locate=450)
All right. Yeah. So I I've actually read a bunch of different like from different sources and they were not that structured,  but I try to organize them in a way. So this is not any official source or, you know,  like this is just the way I started thinking about this. So the first big theme I think is this idea of agent legibility, which is a weird,  maybe a weird word. I don't know.
> 好的。是的。所以我实际上阅读了很多不同的来源，它们没有那么结构化，但我尝试以某种方式组织它们。所以这没有任何官方来源，你知道，这只是我开始思考这件事的方式。所以我认为第一个大主题是 agent 的可读性，这可能是一个奇怪的词。我不知道。

**Kaushik Gopal:**
[(07:54)](https://app.podwise.ai/dashboard/episodes/7532722?locate=474)
No, no, I think, I think I understand,  but maybe you should explain that agent legibility,  which is like, how do you make it easy for the agent to understand? Can you expand on that? What is agent legibility?
> 不，不，我想，我想我理解，但也许你应该解释一下 agent 的可读性，也就是说，你如何使 agent 容易理解？你能详细说明一下吗？什么是 agent 的可读性？

**Iury Souza:**
[(08:05)](https://app.podwise.ai/dashboard/episodes/7532722?locate=485)
I think behind this is the idea that if knowledge lives in Slack or in someone's head or in some random doc,  That's linked elsewhere. The agent cannot use it. So for the agent, it essentially doesn't exist. So something that you think it's trivial is just not part of its context. And it's not, you know, like discoverable at all.
> 我认为这背后的想法是，如果知识存在于 Slack 中，或存在于某人的头脑中，或存在于其他地方链接的某个随机文档中。那么 agent 就无法使用它。所以对 agent 来说，它基本上是不存在的。所以你认为微不足道的事情，并不属于它的上下文。而且它根本无法被发现。

**Kaushik Gopal:**
[(08:26)](https://app.podwise.ai/dashboard/episodes/7532722?locate=506)
It's those things, those conversations you have with your product manager or other people in Slack. It's the Google Docs, the PRDs that don't exist in the code base itself. Those are the things you want to sort of capture and encode into this, right? So that feels like the theme here, which is like,  if there are things that the agent has no visibility into,  make sure that you encode and put that so that it can start to read this from your code base. Because otherwise it has no knowledge, right? If it can't see it, there's no chance it's going to incorporate that into its reasoning and thinking.
> 那些是你和产品经理或 Slack 中的其他人进行的对话。还有那些不在代码库中的 Google 文档、PRD。这些是你想要捕捉并编码到其中的东西，对吧？这就是这里的主题，如果 agent 无法看到某些东西，确保你对其进行编码并放入其中，以便它可以开始从你的代码库中读取它。因为否则它就一无所知，对吧？如果它看不到，它就不可能将其纳入推理和思考中。

**Iury Souza:**
[(08:58)](https://app.podwise.ai/dashboard/episodes/7532722?locate=538)
Yeah, it's the idea that the repo has to be more navigable by the agents. So not just for humans.
> 是的，这个想法是仓库必须更容易被 agent 导航。不仅仅是为人类。


---

## Enhancing Agent Understanding: Documentation and Test-Driven Feedback Loops
> 增强代理理解：文档和测试驱动的反馈循环

The hosts discuss how to improve agent legibility by creating a well-organized documentation folder with feature overviews, design rules, and coding practices. They emphasize the importance of closing feedback loops by using tests to inform agents when they make mistakes. The output from tests needs to be clear and actionable for agents to effectively learn from failures.
> 主持人讨论了如何通过创建一个组织良好的文档文件夹，其中包含功能概述、设计规则和编码实践，来提高代理的可读性。他们强调了通过使用测试来告知代理何时犯错来关闭反馈循环的重要性。测试的输出需要清晰且可操作，以便代理能够有效地从失败中学习。

**Kaushik Gopal:**
[(09:04)](https://app.podwise.ai/dashboard/episodes/7532722?locate=544)
I like that. Make it more navigable by agents. But the natural question is, how do you do that? What are you suggesting that I do to make it more navigable by the agents?
> 我喜欢这个说法。使 agent 更容易导航。但自然而然的问题是，你如何做到这一点？你建议我做些什么来使 agent 更容易导航？

**Iury Souza:**
[(09:16)](https://app.podwise.ai/dashboard/episodes/7532722?locate=556)
Right. So going back to the whole agents MD starting point. So now you can have, instead of just having a bunch of instructions,  like a thousand lines in the agents MD,  you can actually specify that, hey, If you want to understand how the repo works,  there is this docs folder where we organize by feature and or some kind of theme and some cross-cutting concerns of how the repo works. So you can have like some components overview, design rules, coding practices,  and all of this becomes more discoverable by the agents themselves.
> 对。回到整个 agents MD 的起点。现在你可以拥有，而不是仅仅拥有一堆指令，比如 agents MD 中的一千行，你可以明确指出，如果你想了解仓库的工作原理，这里有一个 docs 文件夹，我们按功能、主题以及仓库工作原理的一些交叉问题进行组织。这样你就可以有一些组件概览、设计规则、编码实践，所有这些对于代理本身来说都变得更容易发现。

**Kaushik Gopal:**
[(09:52)](https://app.podwise.ai/dashboard/episodes/7532722?locate=592)
And just to be clear, like, you know, the docs folder you're saying,  so one is actually creating the docs folder,  adding all of those things, but then also having that referenced in the agents.md like a map,  you know, and that's the important piece.
> 澄清一下，你说的文档文件夹，一是实际创建文档文件夹，添加所有这些内容，还要在 agents.md 中引用它，就像一个地图，这是很重要的一部分。

**Iury Souza:**
[(10:04)](https://app.podwise.ai/dashboard/episodes/7532722?locate=604)
Yeah. And like notes can link to other notes. So when the agent is reversing this documentation, it can figure out by itself,  like, well, where does this go and what this is related to.
> 是的。笔记可以链接到其他笔记。这样，当代理反向解析这些文档时，它可以自己弄清楚，嗯，这应该放在哪里，以及它与什么相关。

**Kaushik Gopal:**
[(10:18)](https://app.podwise.ai/dashboard/episodes/7532722?locate=618)
Maybe we move to the next one. What was the next theme that you brought about?
> 也许我们继续下一个。你提出的下一个主题是什么？

**Iury Souza:**
[(10:23)](https://app.podwise.ai/dashboard/episodes/7532722?locate=623)
Yeah,  this is something that I think a lot of people have been realizing to like and working on is the idea of closing the feedback loops.
> 是的，我认为很多人已经意识到并正在努力做的一件事是闭环反馈。

**Kaushik Gopal:**
[(10:32)](https://app.podwise.ai/dashboard/episodes/7532722?locate=632)
Hmm. And, you know, closed feedback loop sounds like this control flow theory, you know, some fancy machine learning term. But what do we mean by close the feedback loop? Because I hear a lot of people say this, but pragmatically, what do you mean by that?
> 嗯。闭环反馈听起来像是控制流理论，一些花哨的机器学习术语。但我们所说的闭环反馈是什么意思呢？因为我听到很多人这么说，但实际操作中，你是什么意思呢？

**Iury Souza:**
[(10:50)](https://app.podwise.ai/dashboard/episodes/7532722?locate=650)
Well, the agent needs to know when it messed up. So it needs some kind of feedback. So I think the first one could be probably tests. I think they're the baseline. So if you have. You asked me to implement something. It needs to have tests so that when it runs a test and it does fail,  you don't need to tell it that it's broken. It can figure it out by itself.
> 代理需要知道它什么时候搞砸了。所以它需要某种反馈。我认为第一个可能是测试。我认为它们是基准。如果你有。你让我实现一些东西。它需要有测试，这样当它运行测试并且失败时，你不需要告诉它出错了。它可以自己弄清楚。

**Kaushik Gopal:**
[(11:12)](https://app.podwise.ai/dashboard/episodes/7532722?locate=672)
And this makes sense. So this is the idea of even having the tests, right? Because in the last section with the agent legibility,  you want to also tell the agent how to run the tests that goes in that section. In this section, I mean, now I keep thinking about the term harness, which is a good term. Your code base needs to have the ability to even run these tests in the first place.
> 这很有道理。所以这就是甚至要有测试的想法，对吧？因为在上一节关于代理可读性中，你也要告诉代理如何运行测试，这放在那一节里。在这一节中，我的意思是，现在我一直在想 “harness” 这个词，这是一个好词。你的代码库首先需要有能力运行这些测试。

**Iury Souza:**
[(11:31)](https://app.podwise.ai/dashboard/episodes/7532722?locate=691)
Yeah, so for example, one thing that maybe is not immediately obvious is that,  OK, if the agent is going to run the test,  so the output from the test needs to be clear enough for the agents to act on it. So maybe it's not if you're if you're depending,  I don't know what kind of app you're building or kind of system you're building. But some tests are not, you know, like they're not immediately like actionable. You need to inspect the results somewhere. Maybe dumps the results into a file that the agent doesn't know where it is. So these tests are not useful actually for the feedback loop.
> 是的，例如，有一件事可能不是很明显，那就是，如果代理要运行测试，那么测试的输出需要足够清晰，以便代理能够对其采取行动。所以也许不是，如果你依赖于，我不知道你在构建什么类型的应用或什么类型的系统。但是有些测试不是，你知道，它们不是立即可以操作的。你需要在某个地方检查结果。也许将结果转储到一个代理不知道在哪里找到的文件中。所以这些测试实际上对反馈回路没有用处。

**Kaushik Gopal:**
[(12:07)](https://app.podwise.ai/dashboard/episodes/7532722?locate=727)
Oh, that's a really good point. So it's not just about writing the test. It's also how you read the results from the test.
> 哦，这是一个非常好的观点。所以不仅仅是编写测试。还在于你如何从测试中读取结果。

**Iury Souza:**
[(12:12)](https://app.podwise.ai/dashboard/episodes/7532722?locate=732)
Yeah. It needs to close the actual loop, right? So it needs to...
> 是的。它需要闭合实际的循环，对吧？所以它需要...

**Kaushik Gopal:**
[(12:16)](https://app.podwise.ai/dashboard/episodes/7532722?locate=736)
Ah, I see, I see. I like how you did that. So that's the closing of the loop part in this. That makes a lot of sense. So writing tests is basically the idea of closing the feedback loop. Is there anything else here?
> 啊，我明白了，我明白了。我喜欢你这样做的。这就是其中的闭环部分。这很有道理。所以编写测试基本上就是闭环反馈的想法。这里还有其他内容吗？


---

## Closing Feedback Loops: Integrating Static Analysis and Log Access for AI Agents
> 关闭反馈循环：为 AI 代理集成静态分析和日志访问

The discussion continues on closing feedback loops, emphasizing the need for tools like type checks, linters, and static analysis to provide feedback to agents. Access to logs is also crucial, requiring engineering efforts to ensure agents can effectively pull and use log data. The hosts highlight the importance of timestamped and filtered logs for specific moments, enabling agents to diagnose issues accurately.
> 讨论继续关于关闭反馈循环，强调需要像类型检查、linter 和静态分析这样的工具来向代理提供反馈。访问日志也至关重要，需要工程方面的努力来确保代理能够有效地拉取和使用日志数据。主持人强调了针对特定时刻的带有时间戳和经过筛选的日志的重要性，使代理能够准确地诊断问题。

**Iury Souza:**
[(12:30)](https://app.podwise.ai/dashboard/episodes/7532722?locate=750)
Right. So I think most of the things that we are used as developers, because we need these things as well,  right? So if you ever try to write code in a notepad, it's like really hard, right? Because you don't know exactly what's going on. It's just text.
> 对。所以我认为我们开发者使用的大部分东西，是因为我们也需要这些东西，对吧？所以如果你尝试在记事本中编写代码，会非常困难，对吧？因为你不知道到底发生了什么。它只是文本。

**Kaushik Gopal:**
[(12:45)](https://app.podwise.ai/dashboard/episodes/7532722?locate=765)
Hey man, 15 years back, Notepad++, I don't know, you know, when I had my C++ courses,  we had to do that. I mean, forget Notepad++, we had to write code on paper, like, you know, as crazy as that sounds.
> 伙计，15 年前，Notepad++，我不知道，当我有我的 C++ 课程时，我们不得不这样做。我的意思是，忘记 Notepad++ 吧，我们必须在纸上写代码，听起来很疯狂。

**Iury Souza:**
[(12:58)](https://app.podwise.ai/dashboard/episodes/7532722?locate=778)
Way harder. That's exactly it, it's way harder. So the agents need them as much as we do.
> 难多了。没错，难多了。所以代理和我们一样需要它们。

**Kaushik Gopal:**
[(13:06)](https://app.podwise.ai/dashboard/episodes/7532722?locate=786)
Oh, I like how you connected that. Okay, okay, okay, that's good, that's good. So you're basically saying, remember how hard that was? So don't do that.
> 哦，我喜欢你如何连接这一点。好的，好的，好的，很好，很好。所以你基本上是说，还记得那有多难吗？所以不要那样做。

**Iury Souza:**
[(13:15)](https://app.podwise.ai/dashboard/episodes/7532722?locate=795)
Especially like, for example, even basic things like, you know, like type checks or lead team,  any kind of feedback that you can give to the agent will help. So static analysis.
> 特别是像，例如，即使是像类型检查或代码检查这样的基本事项，任何你可以给代理的反馈都会有所帮助。所以是静态分析。

**Kaushik Gopal:**
[(13:26)](https://app.podwise.ai/dashboard/episodes/7532722?locate=806)
21st century tools, basically.
> 基本上是 21 世纪的工具。

**Iury Souza:**
[(13:28)](https://app.podwise.ai/dashboard/episodes/7532722?locate=808)
Right. And then you get to even more like higher level stuff or not high level,  but like things that maybe doesn't jump to the eye immediately that you need to build. But for example, like the agent needs to have access to the logs. Depending on how your system is built, the logs may be not so trivial to pull from. So you need to get the agent to have that at hand.
> 对。然后你会得到更高级的东西，或者不是高级的，而是你可能不会立即想到你需要构建的东西。例如，代理需要访问日志。根据你的系统构建方式，日志可能不容易提取。所以你需要让代理能够随时掌握这些日志。

**Kaushik Gopal:**
[(13:50)](https://app.podwise.ai/dashboard/episodes/7532722?locate=830)
I think even in the open AI post they mentioned, right, I think they use LogSQL or something. I forget what the tool is specifically that they use there. From first-hand experience, I can also say that, you know, at Instacart,  we had to spend some time figuring out How to draw the logs out from our systems in a way that we can feed to agents because there's so many minor points. For example, your logs could be a ginormous size. You may not even have APIs. You have to paginate your APIs or, you know, you set up MCPs,  but then the MCPs don't exist for the tools that you use. So all of that is this engineering, right?
> 我认为即使在 OpenAI 的帖子中他们也提到了，对吧，我认为他们使用 LogSQL 或其他东西。我忘记了他们具体使用的工具是什么。根据第一手经验，我也可以说，在 Instacart，我们不得不花一些时间弄清楚如何从我们的系统中提取日志，以便我们可以将其提供给代理，因为有很多小问题。例如，你的日志可能非常庞大。你可能甚至没有 API。你必须对你的 API 进行分页，或者你设置了 MCP，但是你使用的工具不存在 MCP。所有这些都是工程，对吧？

[(14:24)](https://app.podwise.ai/dashboard/episodes/7532722?locate=864)
How do you get to a point where You can get the agent to pull those logs effectively and then use those logs. Because even if you think about logs, there's timestamp. You don't want to pull the logs for the entire day. You want to pull it for that specific moment where it's useful for the agent to pick it up or the right filters on those logs. So there's a lot of, you know, code engineering that goes into making sure that You pull the information correctly for these agents when they need them.
> 你如何达到这样的程度：你可以让代理有效地提取这些日志，然后使用这些日志。因为即使你考虑日志，也有时间戳。你不想提取一整天的日志。你想提取对代理有用或对这些日志的正确过滤器特定的时刻的日志。所以有很多代码工程需要确保你在代理需要时正确地提取信息。


---

## Harness Engineering vs. Context Engineering: Practical Engineering for AI Agents
> Harness 工程 vs. 上下文工程：面向 AI 代理的实践工程

The hosts differentiate harness engineering from context engineering, noting that harness engineering involves actual engineering work, such as integrating logs and linters. This approach is more practical than context engineering, which relies on semantic maps and AI invocation. The discussion emphasizes the need to engineer systems so that agents can perform checks and tests, similar to human developers.
> 主持人区分了 Harness 工程和上下文工程，指出 Harness 工程涉及实际的工程工作，例如集成日志和 linter。这种方法比依赖于语义图和 AI 调用的上下文工程更实用。讨论强调需要对系统进行工程设计，以便代理可以执行检查和测试，类似于人类开发人员。

**Iury Souza:**
[(14:52)](https://app.podwise.ai/dashboard/episodes/7532722?locate=892)
This is a very good point that you made,  because I think this is what makes this idea of harness engineering more compelling to me,  because like the previous thing we had was context engineering, right? So context engineering is more in this, you know,  like the woo-woo kind of thing that you're just typing words and,  you know, trying to find Semantic, yeah, semantic maps and whatever from the code base,  like try to, you know, invoke this, this good part of the AI, but like here is actual engineering work,  right? Okay. No, I need logs. How do I get the logs in? Oh, I need to tie this in. Okay. Maybe the, I have a hook that whenever the model writes code,  then I will trigger the linter to format the,
> 你提出的这一点非常好，因为我认为这使得 “harness 工程” 的想法对我来说更具吸引力，因为我们之前有的是上下文工程，对吧？所以，上下文工程更像是这样，你知道的，有点像玄学的东西，你只是在输入文字，你知道，试图从代码库中找到语义，是的，语义地图之类的东西，比如尝试，你知道，调用 AI 的这一部分，但这里是实际的工程工作，对吧？好的。不，我需要日志。我怎样才能获得日志？哦，我需要把它绑进来。好的。也许，我有一个钩子，每当模型编写代码时，我就会触发 linter 来格式化，

[(15:37)](https://app.podwise.ai/dashboard/episodes/7532722?locate=937)
 my code base to make sure that it doesn't, you know, that Things are very tight. So this I think is closer to the engineering part.
> 我的代码库，以确保它不会，你知道，事情非常紧凑。所以我认为这更接近于工程部分。

**Kaushik Gopal:**
[(15:47)](https://app.podwise.ai/dashboard/episodes/7532722?locate=947)
Right, right. And it applies across the board, right? Say you have screenshot tests, then you need to know how to read screenshots or even set up screenshot tests in the first place. As mobile developers,  you need to be able to spin up an emulator or something so that the agent can then actually run the test on an emulator,  read the results. Whatever it is that you as a human do to check the system,  you need to engineer your system so that the agents can basically do that as well. What's next?
> 对，对。而且它适用于所有方面，对吗？假设你有屏幕截图测试，那么你需要知道如何读取屏幕截图，甚至首先设置屏幕截图测试。作为移动开发人员，你需要能够启动一个模拟器，以便代理可以真正在模拟器上运行测试，读取结果。无论你作为人类做什么来检查系统，你都需要设计你的系统，以便代理基本上也能做到。接下来是什么？


---

## Persistent Memory: Preventing Repeated Mistakes with AI Agents
> 持久内存：防止 AI 代理重复犯错

The conversation shifts to the need for persistent memory to prevent repeated mistakes by both humans and AI agents. Memory helps in remembering past decisions and picking up where one left off. Solutions range from simple markdown files to sophisticated systems like vector databases. Memory aims to hasten the process of finding the right answers and reduce token usage.
> 对话转向了需要持久内存来防止人类和 AI 代理重复犯错。内存有助于记住过去的决策并从上次停止的地方继续。解决方案范围从简单的 markdown 文件到像向量数据库这样的复杂系统。内存旨在加快找到正确答案的过程并减少 Token 使用量。

**Iury Souza:**
[(16:14)](https://app.podwise.ai/dashboard/episodes/7532722?locate=974)
Oh, that's, uh, now there comes a complicated one. Uh, lots of opinions out there, but, and it's that most definitely an open problem,  but we need to solve memory. Some kind of persistent memory.
> 哦，那是，呃，现在来了一个复杂的。呃，有很多不同的观点，而且这绝对是一个尚未解决的问题，但我们需要解决记忆问题。某种持久性记忆。

**Kaushik Gopal:**
[(16:29)](https://app.podwise.ai/dashboard/episodes/7532722?locate=989)
People approach this so differently. There's so many solutions out there for memory. But maybe you can start off by telling us, yeah, well, what do you mean by persistent memory? And then we can talk about the approaches.
> 人们对此的处理方式截然不同。有很多关于记忆的解决方案。但也许你可以先告诉我们，是的，你说的持久性记忆是什么意思？然后我们可以讨论这些方法。

**Iury Souza:**
[(16:39)](https://app.podwise.ai/dashboard/episodes/7532722?locate=999)
Yeah, so here's the idea that if you don't have a system of record or design decisions and some failure patterns,  both humans and agents will keep paying for the same confusion over and over,  right? So when something goes wrong, we need to be able to remember that so that doesn't happen again.
> 是的，所以这里的想法是，如果你没有记录系统或设计决策以及一些失败模式，那么人类和代理都会不断地为同样的困惑付出代价，对吧？所以当出现问题时，我们需要记住这一点，这样就不会再次发生。

**Kaushik Gopal:**
[(16:56)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1016)
We think of memory as preventing past mistakes. What is the difference then between persistent memory and say, just putting something in your agents.md file?
> 我们认为记忆是防止过去的错误。那么，持久性记忆和仅仅将内容放入你的 agents.md 文件之间有什么区别呢？

**Iury Souza:**
[(17:06)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1026)
Because there's basically like two things you can solve with memory. It's like one is this idea of like past decisions,  but it's also like basically trying to pick up where you left from.
> 因为基本上你可以通过记忆来解决两件事。一个是关于过去决定的想法，但基本上也是试图从你离开的地方继续。

**Kaushik Gopal:**
[(17:19)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1039)
Oh, that's very interesting. It's not just about if you're starting net new. You want to encode past memory. If you think about how people are approaching memory,  and maybe you can talk a little more about this,  there's as hacky solutions as I think what Claude is doing,  which is there's a memory.md file now,  and then you can just use the memory.md file. Then there are people who have tools like, what is it? I think Toby, the Shopify CEO has this QMD tool, right? Feed it across all and get encoded markdown and then that you save as embeddings or I think it puts it in a vector DB,  I forget. And then there's entire systems where you set up an entire indexing process.
> 哦，这很有趣。这不仅仅是关于你是否正在启动新的东西。你想要编码过去的记忆。如果你考虑人们如何处理记忆，也许你可以多谈谈这一点，有一些非常简陋的解决方案，比如我认为 Claude 正在做的，现在有一个 memory.md 文件，然后你可以直接使用 memory.md 文件。还有一些人拥有像这样的工具，那是什么？我想 Shopify 的 CEO Toby 有这个 QMD 工具，对吧？将它输入到所有内容中并获得编码的 markdown，然后将其保存为嵌入，或者我认为它将其放入向量数据库中，我忘记了。然后还有完整的系统，你可以在其中设置一个完整的索引过程。

[(17:59)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1079)
For those who don't remember, like cursor in the early days. You know, anytime you open your code base, it would index, you know,  there's a range from like a simple markdown to like sophisticated systems.
> 对于那些不记得的人，就像早期的 cursor。你知道，无论何时你打开你的代码库，它都会进行索引，你知道，范围从简单的 markdown 到复杂的系统。

**Iury Souza:**
[(18:09)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1089)
Yeah, because essentially it's the same thing, right? Because everything's marked down, but I think it's just the way you use it or how you feel that in.
> 是的，因为本质上它是一样的，对吧？因为所有东西都被标记下来了，但我认为这只是你使用它的方式，或者你如何将其融入其中。

**Kaushik Gopal:**
[(18:20)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1100)
You know how we have RAG, at one point RAG models were the rage. I have this powerful model, but then I want to layer in some of my learnings. You can put that in a Markdown file, like nothing stopped you, but then there are more efficient ways. And because sure, the model eventually might get to the same point and give you the results,  but you want to make that process faster. So memory feels like a good way to do that because eventually the agent,  as these models get really good, the agents will come up with the right answer. You want to hasten that process. You want to get those answers quickly and more efficiently. You don't want to keep burning tokens.
> 你知道我们如何使用 RAG，曾经 RAG 模型风靡一时。我有这个强大的模型，但我想加入我的一些学习成果。你可以将其放入 Markdown 文件中，没有什么可以阻止你，但还有更有效的方法。因为当然，该模型最终可能会达到相同的点并给你结果，但你想要加快这个过程。所以记忆感觉像是一个很好的方法，因为最终代理，随着这些模型变得非常好，代理将会提出正确的答案。你想要加速这个过程。你希望快速且更有效地获得这些答案。你不想继续消耗令牌。

[(18:54)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1134)
It feels like that's the powerful piece of memory.
> 感觉这才是记忆的强大之处。


---

## Entropy Control: Maintaining Order in AI-Generated Codebases
> 熵控制：在人工智能生成的代码库中维持秩序

The hosts discuss entropy control, which involves managing the increasing disorder in codebases. Entropy naturally increases over time, especially with AI-generated code. The discussion emphasizes the need for effort to keep things tidy, as codebases tend to become messy if left unattended.
> 主持人讨论了熵控制，它涉及管理代码库中不断增加的混乱程度。熵会随着时间的推移自然增加，尤其是在人工智能生成的代码中。讨论强调需要努力保持整洁，因为代码库如果无人照看，往往会变得混乱。

**Iury Souza:**
[(18:57)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1137)
This is honestly like super Interesting topic because you start thinking of like how we remember things and how we surface facts and things.
> 这确实是一个非常有趣的话题，因为你开始思考我们如何记住事物以及我们如何呈现事实和事物。

**Kaushik Gopal:**
[(19:08)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1148)
To your point,  maybe we should spend another episode just talking about memory once these solutions mature and people come up with more ideas. So we'll make sure to do that. What's the next one?
> 按照你的说法，也许我们应该再花一集专门讨论记忆，等到这些解决方案成熟，人们提出更多的想法。所以我们会确保这样做。下一个是什么？

**Iury Souza:**
[(19:18)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1158)
Entropy control, right?
> 熵控制，对吧？

**Kaushik Gopal:**
[(19:19)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1159)
This is maybe the one time I'm using my, you know, mechanical engineering background. I feel like, you know, I'm finally using something.
> 这可能是我唯一一次使用我的，你知道，机械工程背景。我感觉，你知道，我终于用上了一些东西。

**Iury Souza:**
[(19:25)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1165)
Exactly. It fits pretty well.
> 没错。非常合适。

**Kaushik Gopal:**
[(19:27)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1167)
It basically means the degree of randomness or disorder. So one of the rules or laws of thermodynamics says that entropy over time will gradually increase. Like, you know, entropy is always increasing. So how do I connect that to my code base?
> 它基本上意味着随机性或无序的程度。所以热力学的一个规则或定律说，随着时间的推移，熵会逐渐增加。就像，你知道，熵总是增加的。那么我如何将其连接到我的代码库？

**Iury Souza:**
[(19:42)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1182)
That's exactly what happens in a code base, right? If you leave it unattended, it just becomes a mess.
> 这正是代码库中发生的事情，对吧？如果你无人看管，它就会变成一团糟。

**Kaushik Gopal:**
[(19:47)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1187)
That's a good way to put it, which is don't do anything and don't expect it to naturally become orderly. By nature, it is going to become disorderly.
> 这是一个很好的说法，那就是什么都不做，也不要指望它自然而然地变得有序。本质上，它会变得无序。


---

## Entropy Control and Blast Radius: Managing Code Drift and Agent Permissions
> 熵控制和爆炸半径：管理代码漂移和代理权限

The hosts discuss entropy control, emphasizing the need to manage code drift and stale documentation in AI-generated codebases. They also introduce blast radius control, which involves setting up permissions to limit what agents can do, especially in sensitive areas of the codebase. This prevents agents from causing catastrophic damage.
> 主持人讨论了熵控制，强调需要管理人工智能生成的代码库中的代码漂移和过时文档。他们还介绍了爆炸半径控制，它涉及设置权限以限制代理可以执行的操作，尤其是在代码库的敏感区域。这可以防止代理造成灾难性损害。

**Iury Souza:**
[(19:55)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1195)
Needs a lot of effort to keep things tidy, right? Just like your bedroom. I had a roommate at some point that he used to say that no matter what,  the room drifts to chaos.
> 需要付出很多努力才能保持整洁，对吧？就像你的卧室。我曾经有一个室友，他说无论如何，房间都会朝着混乱的方向发展。

**Kaushik Gopal:**
[(20:08)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1208)
Great. Great roommate.
> 太棒了。很棒的室友。

**Iury Souza:**
[(20:10)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1210)
So I think the thing with agent generated code now is that this is multiplied a lot because there's a lot more moving things in the code base. There's just a lot more code being written. So the chances Of entropy taking over just increase a lot.
> 所以我认为现在由代理生成的代码的问题在于，这种情况被放大了许多，因为代码库中有很多移动的东西。只是有更多的代码正在被编写。所以熵接管的机会大大增加了。

**Kaushik Gopal:**
[(20:30)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1230)
So that's a good point because there's so much going in. Yeah, yeah.
> 这是一个很好的观点，因为有太多的东西在进入。是的，是的。

**Iury Souza:**
[(20:33)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1233)
So the patterns drift like even if you have like the whole harness engineering going on and you have a bunch of guardrails and you're reviewing very diligently,  it's still going to drift and docs will go stale and helper functions might start multiplying. So just, just kind of like we have with humans, right? Because I thought, I think a lot of people now kind of act like humans wrote perfect code before AI. This is true.
> 所以这些模式会漂移，即使你进行了完整的安全工程，并且你有很多护栏，并且你非常认真地进行审查，它仍然会漂移，文档会变得过时，辅助函数可能会开始成倍增加。就像我们和人类一样，对吧？因为我认为现在很多人都表现得好像人类在人工智能之前编写了完美的代码一样。这是真的。

**Kaushik Gopal:**
[(21:01)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1261)
It's like, Oh my God, all the AI slob code you wrote was not any better.
> 就像，天哪，你编写的所有人工智能的马虎代码并没有更好。

**Iury Souza:**
[(21:05)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1265)
I've seen a lot of atrocities from humans as well.
> 我也见过很多人类的暴行。

**Unknown Speaker:**
[(21:11)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1271)
So true, so true.
> 确实如此，确实如此。

**Iury Souza:**
[(21:13)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1273)
We need to try to control this, this drift. And I think the entropy control is basically that. So how do you do that in a harness? You can solve it manually. You can try to automate things. You can use more AI to try to control it. That's another thing that people are exploring. For example, you could have an agent for catering to documentation drift,  trying to make sure that the dots are not stale. You can do all sorts of things. And this is also like it could be an also an episode, I guess. But yeah, you have to do something about this.
> 我们需要尝试控制这种漂移。我认为熵控制基本上就是这样。那么如何在工具中做到这一点呢？你可以手动解决。你可以尝试自动化。你可以使用更多人工智能来尝试控制它。这是人们正在探索的另一件事。例如，你可以设置一个代理来处理文档漂移，确保这些点不是过时的。你可以做各种各样的事情。这也可以像一集节目，我猜。但是，是的，你必须对此采取一些措施。

**Kaushik Gopal:**
[(21:53)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1313)
And with that, we basically come to the last one, I think, that you added here,  which is blast radius control. Can you explain what you mean by this section specifically?
> 这样，我们基本上就到了最后一个，我认为，你在这里添加的，即爆炸半径控制。你能解释一下你在这个部分具体指的是什么吗？

**Iury Souza:**
[(22:04)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1324)
Yeah. So this one is just about scope permissions and risk aware checks. And approval gates and everything that you can use to explicitly control what the agent can do,  especially in sensitive areas of the code base, right?
> 是的。所以这只是关于范围权限和风险感知检查。还有审批关卡以及你可以用来显式控制代理可以做什么的一切，尤其是在代码库的敏感区域，对吧？

**Kaushik Gopal:**
[(22:19)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1339)
I see. So this is the idea that you set up the right permission so you don't let the agent basically suddenly go and RF your entire database. I'm sure people have seen the stories, but that's what this theme is about. The blast radius is make sure you don't let your agent actually do the bad things or go nuclear on your code base.
> 我明白了。所以这里的想法是，你设置正确的权限，这样你就不会让代理基本上突然去 RF 你的整个数据库。我相信人们已经看过这些故事了，但这就是这个主题的意义所在。爆炸半径就是确保你不要让你的代理真正地做坏事，或者在你的代码库中发生核爆。


---

## Blast Radius Control: Limiting Agent Permissions to Prevent Catastrophic Actions
> 爆炸半径控制：限制代理权限以防止灾难性操作

The discussion continues on blast radius control, emphasizing the importance of setting up permissions to prevent agents from causing catastrophic actions. The hosts share an anecdote about an AI agent sending an email without approval, highlighting the need to limit agent permissions. The goal is to build systems that prevent agents from doing the wrong thing.
> 讨论继续进行关于爆炸半径控制，强调设置权限以防止代理造成灾难性操作的重要性。主持人分享了一个关于人工智能代理在未经批准的情况下发送电子邮件的轶事，突出了限制代理权限的必要性。目标是构建能够防止代理做错事的系统。

**Iury Souza:**
[(22:41)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1361)
Exactly. I heard this before as well. When you When you hear a story that a junior developer nuked the company's database,  it's not the junior's developer fault, right? It's like the person that gave him access to the database.
> 没错。我之前也听说过这个。当你听到一个初级开发人员摧毁了公司数据库的故事时，这不是初级开发人员的错，对吧？而是给他访问数据库权限的人的错。

**Kaushik Gopal:**
[(22:58)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1378)
You should have bulletproof systems that don't allow you to even do the wrong thing.
> 你应该有万无一失的系统，不允许你做错事。

**Iury Souza:**
[(23:03)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1383)
Exactly. Yeah. If your agent is doing something catastrophic, it's not the agent's fault, actually. So you have to do something about that. For example, I had this thing, like very stupid example,  but I was trying this Gmail MCP the other day,  like some time ago actually.
> 没错。是的。如果你的代理正在做一些灾难性的事情，实际上这不是代理的错。所以你必须对此采取一些措施。例如，我遇到了这件事，一个非常愚蠢的例子，但我前几天在尝试这个 Gmail MCP，实际上是前一段时间。

**Kaushik Gopal:**
[(23:17)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1397)
Oh boy.
> 哎呀。

**Iury Souza:**
[(23:18)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1398)
And that's automated email drafting.
> 那是自动电子邮件起草。

**Kaushik Gopal:**
[(23:22)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1402)
Oh no, I can see where this story is going.
> 不，我可以预见到这个故事的走向了。

**Iury Souza:**
[(23:24)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1404)
And it really had this draft feature. I said, okay, let me use the draft feature. And I think I told it, we're going to draft an email and we're just,  you know, like back and forth over the email. But I think the thing just went on for some time. I don't know. And then at some point I said, OK, let's just do this change and I think we're good. And then it did the change and he sent the email. I was like, what?
> 它确实有这个草稿功能。我说，好吧，让我使用草稿功能。我想我告诉它，我们要起草一封电子邮件，我们只是，你知道，像这样来回发送电子邮件。但我认为这件事持续了一段时间。我不知道。然后在某个时候我说，好的，让我们做这个改变，我认为我们搞定了。然后它做了更改，并发送了电子邮件。我当时想，什么？

**Kaushik Gopal:**
[(23:47)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1427)
Oh, I mean, you didn't say we're good, so.
> 哦，我的意思是，你没说我们搞定了，所以。

**Iury Souza:**
[(23:52)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1432)
Right. OK, so then I learned, OK, though, I have to actually not let it send the email like,  you know, like in the permissions part.
> 对。好的，然后我明白了，哦，我实际上必须不让它发送电子邮件，就像，你知道，就像在权限部分一样。

**Kaushik Gopal:**
[(24:02)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1442)
Oh, but that's a great point there. So, like, you know, in the In this context of harness engineering and this controlling the blast radius,  what you would then do in this specific example is go and maybe either add an instruction or basically limit the permission so that you never. Allow the agent to send something. It can only make draft. You would only give it access to the draft permission. You would not give it access to the send permission, so to speak.
> 哦，但这是一个很好的观点。所以，就像，你知道，在这种工具工程的背景下，以及这种控制爆炸半径的情况下，你在这个具体例子中会怎么做，就是去添加一条指令，或者基本上限制权限，这样你就永远不会。允许代理发送任何东西。它只能制作草稿。你只会授予它访问草稿权限的权限。你不会授予它发送权限的权限，可以这么说。

**Iury Souza:**
[(24:28)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1468)
Build a SKU that uses the MCP and then blocks some of the tools that the MCP has, for example. But yeah, just the idea of controlling it.
> 构建一个使用 MCP 的 SKU，然后阻止 MCP 拥有的一些工具，例如。但是，是的，只是控制它的想法。


---

## Building a Harness: Customizing AI Tools for Enterprise Needs
> 构建安全环境：为企业需求定制人工智能工具

The conversation shifts to building a harness, which involves creating custom AI tools tailored to specific enterprise needs. Generic tools may not suffice for larger companies with unique requirements. The hosts discuss examples like Stripe Minions, a fork from Goose, customized for Stripe's payment security requirements and internal tooling.
> 对话转向构建安全环境，这涉及创建为特定企业需求量身定制的自定义人工智能工具。通用工具可能不足以满足具有独特需求的大型公司。主持人讨论了诸如 Stripe Minions 之类的示例，它是 Goose 的一个分支，专为 Stripe 的支付安全要求和内部工具而定制。

**Kaushik Gopal:**
[(24:38)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1478)
I like that. I think that covers shaping the harness pretty well. I feel I have a good grasp. Maybe let's spend the last few minutes in the episode talking about building a harness all together.
> 我喜欢这个。我认为这很好地涵盖了塑造工具。我觉得我掌握得很好。也许让我们用本集最后的几分钟来讨论一起构建一个工具。

**Iury Souza:**
[(24:49)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1489)
Sounds good. The idea is that at some point these generic tools that we're using, right? So like think of Claude or Cursor. They stop being enough for what your company's doing, right? They can only take you so far. Because especially in the context of larger enterprises, it's like you have a lot of custom stuff going on. So building software becomes something very specific, like very different from in other environments.
> 听起来不错。我们的想法是，在某个时候，我们正在使用的这些通用工具，对吧？就像想想 Claude 或 Cursor。它们对于你的公司正在做的事情来说就不够了，对吧？它们只能带你走这么远。因为尤其是在大型企业的背景下，就像你有很多定制的东西在进行。因此，构建软件变得非常具体，与其他环境中的软件非常不同。

**Kaushik Gopal:**
[(25:21)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1521)
I like that a lot. One of the most popular skills I think that's out there by Jesse Vincent, super smart guy. It's called Superpowers. And the idea is it's a bunch of skills that, you know, in a nutshell,  forces you to follow the software engineering process well. So the skill will automatically prompt you to first brainstorm, come up with a proper execution plan,  you know, or what sometimes you call like an ERD, writes the tests. It forces like a TDD kind of practice, makes sure that you set up work trees, get work trees. So it's almost a full system that will enable you automatically to do the right thing. That's like, I think, the first level, which is like, hey,  wouldn't it be nice if my company just had something like this?
> 我非常喜欢。我认为 Jesse Vincent 的一项最受欢迎的技能，他是个非常聪明的人。它叫做 Superpowers。这里的想法是一堆技能，你知道，简而言之，它会迫使你很好地遵循软件工程流程。因此，该技能会自动提示你首先进行头脑风暴，提出一个适当的执行计划，你知道，或者有时你称之为 ERD，编写测试。它强制执行类似 TDD 的实践，确保你设置工作树，获取工作树。因此，它几乎是一个完整的系统，可以让你自动地做正确的事情。我认为这就像第一个层次，就像，嘿，如果我的公司有类似的东西，那不是很好吗？

[(26:04)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1564)
Because different enterprises and companies, to your point, probably approach the process of building software differently. So wouldn't it be nice if I could encode that into my agent so that anyone who uses the agent at work We'll naturally gravitate towards that.
> 因为不同的企业和公司，就像你说的，可能会以不同的方式处理构建软件的过程。因此，如果我可以将它编码到我的代理中，这样任何在工作中使用该代理的人都会自然而然地倾向于它，那不是很好吗？

**Iury Souza:**
[(26:18)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1578)
Yeah. And when you stretch in that direction, like if you keep going that direction, what is it that you want? Like you want to trust the agent more. For example, when you have these superpowers things like, okay,  now I trust the agent more because I know that it's going to be doing this and I already tested it. So you start going that direction. So what else can you do? Maybe at the very end of this line is like, Having like autonomous agents, right? Like doing things without like involvement. And I think this is what, for example, companies like Stripe went for. So they shared this article recently, what they call Stripe Minions. It's a good name.
> 是的。当你朝着那个方向延伸时，如果你一直朝着那个方向前进，你想要的是什么？比如你想更信任代理。例如，当你拥有这些 superpowers 之类的东西时，比如，好吧，现在我更信任代理了，因为我知道它会做这些，而且我已经测试过了。所以你开始朝着那个方向前进。那么你还能做什么？也许在这条线的最后是，拥有像自主代理这样的东西，对吧？比如在没有参与的情况下做事情。我认为这就是像 Stripe 这样的公司所追求的。所以他们最近分享了这篇文章，他们称之为 Stripe Minions。这是个好名字。

[(26:58)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1618)
Basically it's a fork from Goose, which is also, what, a coding agent? What is Goose?
> 基本上它是 Goose 的一个分支，Goose 也是一个编码代理吗？Goose 是什么？

**Kaushik Gopal:**
[(27:05)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1625)
Oh yeah, yeah. It's an open source coding agent, right? This is from the Square or the Block guys. Almost like an open source version of Cloud Code.
> 哦，是的，是的。这是一个开源的编码代理，对吧？这是来自 Square 或 Block 的那些人做的。几乎就像一个开源版本的 Cloud Code。

**Iury Souza:**
[(27:13)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1633)
Stripe,  like how they justify is that they have this very heterodox They have payment security requirements and a lot of internal tooling. So they wanted to be, you know, like to have the confidence in the agent. So then they went all in and really customizing how the context is surfaced and how these dev boxes are launched and all these things.
> 像 Stripe，他们辩解的理由是他们有非常非正统的支付安全要求和大量的内部工具。所以他们想要，你知道，对代理有信心。所以他们全力以赴，真正定制了上下文如何呈现，这些开发环境是如何启动的，以及所有这些事情。

**Kaushik Gopal:**
[(27:40)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1660)
I honestly am also liking the approach where we explore using open code. The client like that you turn me on again. It's open source, so this is the beauty, right? So it's almost like I get. Cloud code, but an open source version of it. What does a world look like where I can take open code and layer in some of these things? I just think someone should try to do this. What if you built a custom version of open code with superpowers built in? Just something like that. I can see that being a really good natural evolution of the next step.
> 老实说，我也喜欢探索使用开源代码的方法。客户喜欢你再次启动我。它是开源的，所以这就是美妙之处，对吧？所以这几乎就像我得到。Cloud Code，但它是开源版本。如果我可以使用开源代码并叠加其中一些东西，世界会是什么样子的？我只是觉得应该有人尝试这样做。如果你构建了一个内置超能力的开源代码的自定义版本会怎么样？就像那样的事情。我认为这可能是下一个阶段非常好的自然演变。

**Iury Souza:**
[(28:12)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1692)
Yeah, very. Very early days. Very interesting.
> 是的，非常。非常早期。非常有趣。

**Kaushik Gopal:**
[(28:15)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1695)
I will say like the only issue with this is you have the more you go in the direction of trying to create something custom,  the onus of maintaining that is also on you. The burden of maintaining that is also on you. So that's one thing to be careful. That's why most big companies are able to do it because they can dedicate a team. But, you know, I wouldn't suggest the single developer out there go about, you know, building your own harness. Or maybe you should. I don't know. Maybe some people can.
> 我想说，这样做唯一的问题是，你越是朝着创建自定义东西的方向发展，维护它的责任也就越大。维护它的负担也在你身上。所以这是需要小心的一件事。这就是为什么大多数大公司都能做到这一点，因为他们可以专门成立一个团队。但是，你知道，我不会建议单打独斗的开发者去构建自己的工具。或者也许你应该。我不知道。也许有些人可以。


---

## Customization vs. Maintenance: Balancing Innovation and Responsibility in AI
> 定制与维护：平衡人工智能领域的创新与责任

The hosts caution against the burden of maintaining custom AI tools, noting that it requires dedicated teams. They advise individual developers to be careful when building their own harnesses. The discussion concludes with a summary of the evolution from prompt engineering to context engineering to harness engineering, each addressing different leverage points in AI development.
> 主持人警告说，维护自定义人工智能工具的负担很重，并指出这需要专门的团队。他们建议个人开发人员在构建自己的安全环境时要小心。讨论总结了从提示工程到上下文工程再到安全环境工程的演变，每种方法都解决了人工智能开发中不同的杠杆点。

**Iury Souza:**
[(28:42)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1722)
Watch out to not try to re-implement Kubernetes.
> 注意不要尝试重新实现 Kubernetes。

**Kaushik Gopal:**
[(28:47)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1727)
Deep cut there.
> 真是深刻。

**Iury Souza:**
[(28:48)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1728)
Right.
> 对。

**Kaushik Gopal:**
[(28:49)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1729)
Okay, Yuri. I like that. We talked about shaping the harness and building the harness. Maybe it's time to close this episode. Are there any parting thoughts you have?
> 好的，Yuri。我喜欢。我们讨论了塑造工具和构建工具。也许是时候结束这集了。你有什么临别赠言吗？

**Iury Souza:**
[(29:01)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1741)
If you zoom out, we've gone from prompt engineering back in the day, right?
> 如果你放大来看，我们已经从早期的提示工程发展过来了，对吧？

**Kaushik Gopal:**
[(29:07)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1747)
So long ago.
> 很久以前了。

**Iury Souza:**
[(29:08)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1748)
And then context engineering. And now we're at harness engineering. And it's kind of interesting that how each one will point to a different leverage point, right? From how to use the prompts. To when to surface the context and how to manage the context and finally to the harness,  which is the environment of the of the agent itself.
> 然后是上下文工程。现在我们到了工具工程。有趣的是，每一个都会指向不同的杠杆点，对吧？从如何使用提示。到何时呈现上下文以及如何管理上下文，最后到工具，即代理本身的环境。

**Kaushik Gopal:**
[(29:34)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1774)
Makes sense. I like it. Prompt engineering to context engineering to harness engineering.
> 有道理。我喜欢。从提示工程到上下文工程再到工具工程。

**Iury Souza:**
[(29:38)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1778)
I hope you stop at some point.
> 我希望你们在某个时候停下来。

**Kaushik Gopal:**
[(29:40)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1780)
I know, I know. All right. Thank you all for listening and we will catch you in the next episode.
> 我知道，我知道。好的。感谢大家的收听，我们下期再见。

**Iury Souza:**
[(29:47)](https://app.podwise.ai/dashboard/episodes/7532722?locate=1787)
Catch you guys in the next one.
> 下次见。

