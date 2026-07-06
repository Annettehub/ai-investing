---
podcast: "Latent Space: The AI Engineer Podcast"
episode: "Why the Frontier Ecosystem must be Open — Matei Zaharia and Reynold Xin, Databricks"
link: https://podwise.ai/dashboard/episodes/8304753
publish-time: "2026-06-24"
save-time: "2026-07-01"
---

# Why the Frontier Ecosystem must be Open — Matei Zaharia and Reynold Xin, Databricks

## Summary

Databricks founders Matei Zaharia and Reynold Xin discuss the company's evolution from a small Berkeley meetup to a global AI and data powerhouse. The conversation centers on the "modern AI stack," specifically introducing Omnigen, an open-source platform for collaborative agent development, and the "LTAP" (Lakehouse Transactional/Analytical Processing) architecture. LTAP aims to unify transactional and analytical workloads by using a single storage layer, eliminating the brittle and complex ETL/CDC pipelines that plague traditional data engineering. Beyond technical innovations, the discussion highlights the importance of open-source ecosystems, the necessity of AI governance, and a culture of rapid, incremental innovation. By prioritizing open data formats and leveraging massive internal traces to optimize database performance, Databricks continues to consolidate fragmented data infrastructure into a cohesive, scalable platform for enterprise AI applications.

Takeaways:
1. Unifying storage layers allows for real-time analytics on transactional data, effectively eliminating the need for brittle and complex Change Data Capture (CDC) pipelines.
2. Standardizing agentic workflows through a common API and server-side orchestration is essential for enabling secure, collaborative, and stateful agent interactions across diverse environments.
3. Building a "factory" for database engineering—using quadrillions of historical data points to model and predict algorithm performance—allows for faster, more reliable system development than relying solely on academic papers.
4. Prioritizing open data formats and ecosystems from the outset creates a stronger competitive advantage than proprietary, closed-loop architectures, as it aligns with enterprise requirements for long-term data sovereignty.
5. Specialized, smaller models often provide superior performance and cost-efficiency compared to general-purpose frontier models for high-volume, domain-specific tasks like document parsing.
6. Effective agent governance requires contextual, stateful policies that monitor session activity and risk, rather than relying on simple, binary permission controls.
7. Success in the enterprise market hinges on recognizing that non-tech organizations prioritize governance, security, and integration over building custom, proprietary internal tools.
8. Developing complex infrastructure incrementally—by solving specific, real-world customer pain points first—is significantly more effective than attempting to "boil the ocean" with massive, multi-year architectural overhauls.

## Chapters

### [00:03] Chapter 1: Omnigence and the Architecture of Collaborative Coding Agents

Omnigence addresses the fragmentation in agentic development by providing a unified, secure platform for coding agents. The architecture supports portability across environments, enabling developers to share sessions, maintain history, and implement security policies. Open-sourcing this platform fosters network effects, allowing the community to contribute integrations and cloud sandbox support, similar to the early development of Spark. This approach allows teams to move beyond "vibe coding" toward a structured, interoperable framework for agentic workflows.

### [12:36] Chapter 2: Governance and Security in Agentic Development Environments

Managing agentic workflows requires balancing usability with strict security and cost controls. Contextual, stateful policies allow for granular permission management, such as restricting risky actions like installing unverified packages or accessing confidential documents based on session state. Databricks processes exabytes of data daily, and implementing robust governance at the agent level is critical to preventing data leaks and managing token budgets effectively. The goal is to provide autonomy to developers while maintaining enterprise-grade security.

### [27:36] Chapter 3: LTAP and the Unification of Transactional and Analytical Processing

LTAP (Lakehouse Transactional/Analytical Processing) aims to solve the "continuous data corruption" issues inherent in brittle CDC pipelines by unifying storage. By writing data in a column-oriented format directly to the data lake, analytics engines can access information in real-time without complex replication. This architecture leverages idle CPU capacity in storage fleets to perform row-to-column transcoding, providing the benefits of a single system without the performance compromises of traditional HTAP, making data immediately available for reasoning and analytics.

### [37:01] Chapter 4: Engineering the Dream Engine via Machine Learning Optimization

The "Dream Engine" project represents a fundamental shift in database engineering by using machine learning models to optimize performance. Instead of relying solely on academic papers, the team built a factory that analyzes quadrillions of trace data points to determine the most efficient algorithms and data structures for specific workloads. This approach allows the system to dispatch the right implementation at runtime, handling trade-offs between throughput, latency, and data distribution with high fidelity.

### [48:01] Chapter 5: Strategic Differentiation and the Future of Data-Centric AI

Databricks differentiates itself through an open-format foundation and a focus on data-centric AI rather than proprietary models. The strategy emphasizes that data is the most valuable asset, and as AI agents become more capable, the focus shifts toward making model customization easier through synthetic data generation and specialized sub-agents. By maintaining an open ecosystem and avoiding vendor lock-in, the platform enables enterprises to build future-proof architectures that integrate seamlessly with the evolving landscape of AI and data processing.

## Q&A

### Q1 [swyx]: What led to the development of OmniAgent, and why did you decide to combine coding agents and custom agents into a single platform?
A1 [Matei Zaharia]: We saw several converging lines that signaled a need for a new approach. Internally, our developers were building their own workflows with various agents, and we were shipping data science agents like Genie. We realized that all these agents face the same fundamental problems: the need to switch models, the necessity of sharing sessions for collaboration, and the requirement for history and search. People initially thought it was strange to combine coding and custom agents, but the underlying challenges—delivering the agent, controlling it for security, and ensuring portability—are identical. We built OmniAgent to provide a unified layer that handles these shared needs, allowing for collaboration and secure, portable agent deployment.

### Q2 [swyx]: What is your philosophy regarding what to open source versus what to keep as a proprietary service?
A2 [Matei Zaharia]: We open source layers where we believe there will be a network effect, where the ecosystem benefits from collaboration, and where we don't have the time to build every single integration ourselves. Spark is a great example; by making it easy to add connectors, we benefited from the community's work. However, there are services that must be proprietary because they require an operational team to ensure reliability, such as maintaining streaming jobs or ensuring a database doesn't lose data overnight. We want to be as open as possible for what people build on top of our platform, while focusing our internal resources on the high-availability, operational services that require constant management.

### Q3 [swyx]: Can you explain the concept of LTAP (Lakehouse Transactional/Analytical Processing) and how it addresses the limitations of traditional database architectures?
A3 [Reynold Xin]: Traditional database engineering has long been split into two halves: OLTP (transactional) and OLAP (analytical). Usually, you start with an OLTP database like Postgres, but as you scale and need to perform complex analysis, you have to replicate that data into an analytical system using CDC (Change Data Capture) pipelines. These pipelines are often brittle, complex, and prone to failure during schema changes. LTAP is our solution to this "holy grail" problem. Instead of trying to build a single engine that does everything, we unify the storage layer. By writing data in a column-oriented format directly to the data lake, the analytical layer can read the data immediately without any pipeline delay. It gives you the benefits of both worlds without the overhead of maintaining complex synchronization.

### Q4 [swyx]: How do you balance the tension between security and usability when building agents?
A4 [Matei Zaharia]: Many current coding agents use basic binary policies—allowing or disallowing a tool—which creates a tough trade-off between being too restrictive and being insecure. We advocate for "contextual" or "stateful" policies. Instead of asking if an agent is allowed to push to a website, we track the state of the session. For example, if an agent has performed a risky action, like installing an unverified package or reading a large volume of confidential documents, the policy can automatically block further sensitive actions. By mapping low-level API events to high-level functional events, we can write policies that are both more secure and more useful, allowing the agent to operate autonomously until it hits a specific, defined boundary.

### Q5 [swyx]: How do you maintain a culture of innovation and rapid execution as the company scales?
A5 [Reynold Xin,  Matei Zaharia]: We focus on hiring brilliant people and empowering them to act without needing formal permission or endless design documents. We encourage an incremental approach—building a prototype in a few weeks and working directly with a target customer to see if it works. For instance, the LTAP engine was born when an engineer simply prototyped a column-oriented writer because we had idle CPU capacity in our storage fleet, rather than waiting for a committee to approve a formal design doc. We also keep our product portfolio coherent; we don't launch dozens of disparate services. We add one capability at a time—storage, then SQL, then machine learning—and ensure each is done well. This keeps the organization manageable and focused.

### Q6 [swyx]: What is the model strategy for Databricks, and why are you focusing on agents rather than just frontier models?
A6 [Matei Zaharia]: We believe there is a massive opportunity in domain-specific agents that are highly effective at querying data. Our focus is on building systems that utilize both external frontier models and fine-tuned, customized components. We do train models, especially for high-volume use cases where specialized models are significantly better and cheaper than general ones—such as document parsing. We are finding that model customization is getting easier because base models are becoming smarter at generating their own training data and traces. Our goal is to make it easy for anyone to plop in data and describe a task, which is why we are focusing on the "harness" and the interoperability layer, allowing sub-agents with specialized models to work together seamlessly.

### Q7 [swyx]: Looking at the competition, what do you believe is the core insight that allowed Databricks to outpace others in the cloud data space?
A7 [Reynold Xin]: The biggest fundamental difference is that we started with an open ecosystem. We never had a proprietary format; we built on Parquet and evolved into Delta and Iceberg. This was controversial early on, but it won because enterprises want a foundation that isn't locked into a single vendor. Additionally, we started "upstream" of many competitors by focusing on large-scale data processing and ingestion first. It is easier to take a broad, open, large-scale platform and optimize it for speed and business user needs than it is to take a specialized, fast, proprietary system and try to make it open and scalable for bulk processing. When you get the data in the right place, the AI magic becomes much easier to implement.

## Highlights

1. [30:37] CDC is one of the most fundamental operations powering modern society. It is so brittle that we joke it should be called continuous data corruption.
2. [44:45] Very few systems have the guts to go back to the drawing board, knowing everything we know today after a decade of workloads, and attempt to rewrite it from scratch.

## Keywords

1. **Databricks**: A data and AI company that provides a unified platform for data analytics, machine learning, and AI development. It is widely recognized for its Lakehouse architecture, which combines the performance of data warehouses with the flexibility of data lakes.
2. **Spark**: A fast, unified analytics engine designed for large-scale data processing. It allows users to run complex computational tasks across distributed clusters and serves as a foundational technology for many modern data workloads.
3. **Omnigent**: An open-source platform for building, hosting, and managing AI agents. It provides a standardized interface for agent sessions, enabling developers to collaborate, share history, and implement security policies across different agent frameworks.
4. **LTAP (Lakehouse Transactional/Analytical Processing)**: A concept introduced to unify transactional and analytical data processing within a single storage layer. It aims to make data immediately available for reasoning and analytics without the need for brittle, complex pipelines between separate systems.
5. **CDC (Change Data Capture)**: A process that monitors and identifies changes in a database, such as updates, insertions, or deletions. While it is a standard industry practice for replicating data, it is often described as complex and prone to failure when database schemas change.
6. **Second System Syndrome**: A concept in software engineering describing the tendency for a team's second project to fail due to excessive ambition and the desire to include every feature missed in the first system. It serves as a cautionary principle for architects designing new, large-scale systems.
7. **Delta Lake**: An open-source storage layer that brings reliability, performance, and transactional consistency to data lakes. It allows organizations to manage massive amounts of data while ensuring that the information remains accurate and accessible.
8. **Parquet**: A columnar storage file format that is highly optimized for analytical workloads. It allows for efficient data retrieval and compression, making it a standard choice for storing large datasets in modern data platforms.
9. **Genie**: A specialized data science agent developed by the research team at Databricks. It functions as a virtual assistant that understands a company's specific data, libraries, and tools to help users perform complex analysis through natural language.
10. **HTAP (Hybrid Transactional/Analytical Processing)**: An architectural goal in database engineering to run both transactional and analytical workloads on a single engine. While it is often viewed as the "holy grail" of database design, it typically requires significant trade-offs in performance and complexity.

## Transcript

[00:03] **swyx**
Matei and Reynold from Databricks. Welcome to Latent Space.

[00:06] **Reynold Xin**
Thanks for having us.

[00:07] **Matei Zaharia**
Yeah, thanks so much.

[00:08] **swyx**
Thanks for taking time out. You have your Databricks Data AI Summit going on. You were just telling me how the first summit that you guys ran was just 50 people.

[00:16] **Reynold Xin**
Yeah, it was a little meetup at Berkeley, I think.

[00:19] **Matei Zaharia**
Yeah, we do these tutorials and just teach people Spark.

[00:23] **swyx**
Yeah. You know, obviously now it's like, I think the headline number is like 100,000 people around the world, 30,000 in person. It's a crazy community. Well, I mean, I just saw the keynote. Ali is just, did you know, was it obvious back when that Ali would be like such a great CEO? What do you think?

[00:44] **Matei Zaharia**
I mean, I think among our group of founders, it was clear that I think he'd be the best at this. And, and yeah, it turned out great. And he's, I mean, he's ramped up on so many topics going to a company. He would just go in and like study it and, you know, talk to all the experts, like even if he can't hire the person, you know, learn enough about like finance and sales and whatever it was. And, you know, I'd go from there.

[01:09] **swyx**
Yeah.

[01:09] **Reynold Xin**
I mean, he's obviously very high IQ and very high EQ, but it wasn't like Ali today is quite different from Ali from like 10 years ago. I think there's a lot of work that he put in to get to this point.

[01:21] **swyx**
I mean, no, I mean, to me, the most appealing thing about him is that he's funny. And like, you know, it's it's hard to make jokes about, you know, data security and what have you.

[01:33] **Matei Zaharia**
Oh, yeah, that's for sure.

[01:34] **Reynold Xin**
Yeah.

[01:35] **swyx**
So you guys launch a whole bunch of things. I'll just sort of name check briefly the stuff because we're not going to cover everything. Omnigence, your baby. LTAP, your baby, your dream engine. We're also going to cover Genie, cover Customer Lake, you acquired Panther, OpenSharing, and there's Unity, AI Gateway. A lot of these, I think, are things that you would expect Databricks to do. It's like part of the roadmap. Everyone in your category has similar things. But I think probably the two of you are leading the two most unique and differentiated initiatives in the landscape. Maybe we'll start with Omnigent and then we'll go into it. I do think that a lot of people are exploring this sort of meta harness concept. What led you to it?

[02:22] **Matei Zaharia**
Yeah, there were actually a couple of like converging lines, which I think is a good sign that you need Something new. So, on the one hand, there's all the coding agent info internally. We have a really great dev info team. They built something called iZerk that's basically like a wrapper on cloud code and codecs and lets you use them either on the web in like sandboxes or just on your dev machine or on your laptop or whatever. And then, you know, they were adding all kinds of stuff there. And we saw all the The sort of more advanced engineers like were building their own workflows with tons of agents and they were building their own UIs and stuff on top or even on top of that. And then the other one was like us building agents. We ship this like data science agent called Genie on the research team, which I co-lead. Basically, we also build a lot of internal ones for various things.

[03:17] **Matei Zaharia**
And then we have all the customer ones and all of them running into this thing of like, oh, I need to switch. Model and harness and so on, you know, every few months. Plus, the agent is like completely useless if you can't share sessions with someone and have history and have search. All this like layer on top of it for collaboration. I thought a bit about it from both contexts. And at first people thought it was weird. They're like, why are you doing coding agents and custom agents in the same thing? But I said, it's basically the same problems. And you just want to build this stuff that lets you deliver the agent, maybe control it if you care about security and make it portable across things. And then we prototyped some things as experiments. We saw, yeah, actually we can make it work. And then we, you know, we sort of built that for real.

[04:06] **swyx**
I'm wondering if this kind of, let's call it architecture, maps to anything in your careers in the past. You know, like I always think about how a lot of things actually just tie back to operating systems. A lot of operating systems tie back to databases or the other way around.

[04:22] **Matei Zaharia**
I do think it ties a lot to like network protocols, you know, internet protocol.

[04:29] **swyx**
Communication between entities.

[04:30] **Matei Zaharia**
Yeah. We did stuff with like data sharing also, which is probably, you know, most viewers probably won't know unless they're...

[04:36] **swyx**
Open protocol is the term.

[04:38] **Matei Zaharia**
Yeah.

[04:38] **swyx**
Open sharing.

[04:38] **Matei Zaharia**
Open sharing. Yeah. So it's like you have a company, you maintain some kind of table, like, like, let's say like Walmart or something, they have like, you know, inventory and what's been sold in each store. And then you also have suppliers and they would love to produce more things and ship them like exactly the moment you need them. So they would love like real time access to your table. So instead of like sending emails around or Excel sheets or phone calls, why can't you share like a view of that table in real time with them, then they query They, you know, join it with their data and they decide what to send. So it's one of these things where you, like, you might ask, like, today, since we can vibe code anything so fast, why do we even need to design, like, protocols or APIs or software, right? Can't you just vibe code things on demand? But actually, for this type of interoperability, where multiple parties that are moving at different speeds are building stuff and you still want some layer on top to coordinate, you do want to design it and build it.

[05:35] **Matei Zaharia**
So it reminds me of that, like agents talking to each other, And users talking to agents and tools.

[05:42] **swyx**
Reynold, any other comments or alternative viewpoints?

[05:46] **Reynold Xin**
I think, but we had a debate on exactly which set of benefits would matter a lot. And I think around the time we decided to do this thing, I was telling Matei, hey, it just happened that there's a particular week that I was coding non-stop from the moment I woke up to like the moment I went to bed. I was like looking at my class sessions, my codec sessions, and one of the things particularly annoying was having to keep my laptop open. I was actually driving to a doctor's appointment and I remember because I wanted to make sure the whole thing continues.

[06:18] **swyx**
By the way, it's so comforting to hear you say that because I'm like, I don't know if I'm a clown and I'm doing this or like...

[06:25] **Reynold Xin**
Yeah, like honestly, I was driving and I was tethering my laptop to my phone, keeping it on the side. Whenever I hit a red light, I started looking at what's going on on my laptop. And I just felt that was ridiculous. It felt like we went back to the dark ages of programming. I mean, the productivity you gain from all this coding age is amazing.

[06:44] **swyx**
Have you heard of cloud?

[06:46] **Reynold Xin**
It was crazy to me.

[06:49] **Matei Zaharia**
The thing you were working on was the sandboxes or was this before that?

[06:52] **Reynold Xin**
It was a sandbox. So I was approaching from a very different angle. I wanted to say, hey, we're going to have cloud sandboxes that actually doesn't shut down. You can get one very quickly, but not just for running agentic sessions. It's actually also for running development. So I was actually personally building that that week and through building that, I ran into all these issues and then I wrote actually a document for my case. Here's my wish list of what the actual environment should do. He actually ended up almost implementing every single one of them.

[07:23] **Matei Zaharia**
Yeah, I remember Reynold Xin because my first prototype of this had just chats with your agent and he said I have to be able to open a shell, like my own shell, and like list files and like tail them and stuff.

[07:36] **swyx**
Basically, it says agent to the mainframe.

[07:37] **Matei Zaharia**
Yeah, actually it has that now. Telling my log. Yeah.

[07:41] **Reynold Xin**
And also another thing I think I asked was, I still use cursor for the sole purpose of rendering markdown files.

[07:48] **swyx**
Uh-huh. Yeah.

[07:49] **Reynold Xin**
So I said, just give me a way to see my Markdown files and render them properly. I don't need a separate tool anymore.

[07:55] **Matei Zaharia**
Yeah.

[07:56] **Reynold Xin**
I think you also built that in.

[07:57] **Matei Zaharia**
Yeah, we did that. Yeah. Yeah, we had a lot of engineers building, you know, their own vibe coding setup. But then the other thing they all said is like, hey, I built something that's amazing for me, but like no one else on the team can use it because I don't have a server to collaborate. And this is why we tried to set up Omnigent so you can have a server and have the security set up in there. So, you know, like log in with Google or whatever, and like actually Securely sure stuff. That's where we've seen a lot of other agents hit things. People think they prototyped an awesome agent, but it's not allowed to connect to some really important data or whatever because of the security team.

[08:38] **swyx**
At this point, for those watching along on YouTube, we're going to bring up an image of the structure here and we can talk a little bit of the architecture. I just want to have people understand because When we're talking about software, it can be very abstract. And like, here is actually what we're talking about. You've worked out in open source this entire platform, basically. And there's a runner component and server component with a sort of uniform API that you've figured out. Any other sort of element? And obviously, you can plug in all this persistence layers and compute layers. This is a whole cloud. It's an agent cloud.

[09:12] **Matei Zaharia**
Yeah, I mean, it's got these components to work with it. You know, a lot of the action happens like on the machine where you deploy your agent to. So whatever you've got on there, you can go on. But yeah, I think it's sort of the minimal thing you want to have hosted, like collaborative agents and to have that server. And one of the reasons we open sourced it is anyone building agents, this gives them an app they can start with and customize, which we were seeing in Databricks too, like someone would make a nice You know, agent app and then other teams would ask, oh, can I just use yours for my agent?

[09:45] **Reynold Xin**
Yeah, I think we had like five or six different agentic frameworks built by every different team. They do all do more or less the same thing.

[09:51] **swyx**
Yeah, you need to basically people want to take something that works in 4Kit and you might as well have something open source. Yeah, which also was another question, which is interesting for Databricks, like what do you choose to open source? What do you choose to make it? I mean, this goes back to Spark, right?

[10:05] **Matei Zaharia**
Yeah. So, I mean, one of the reasons to open source something is if you think it's a layer that will actually, there'll be some network effect. It will benefit from many people collaborating on it. So, for example, with Spark, I don't know if you know, when Spark came out, we also focused a lot on letting you have libraries on top. So, like, they used to be different. We distributed computing engines for like machine learning and graph computation. We said they should all be libraries that you can compose. And we made it super easy to add connectors to data sources too. And then we benefit because, you know, we don't have the time to write like connectors to like, you know, a thousand like different databases and file formats, but we can just use the ones people make. And of course they benefit from joining, you know, kind of this thing. So that's like one of the reasons. Another way to think about it is like, imagine, Our thing wasn't open. We had some kind of agent hosting thing, but it's not open. And then there is an open one.

[11:05] **Matei Zaharia**
Which one is going to win in the long run? So here, because there is this benefit from people writing integrations, it'll be that. And then there are other things that you just can't even deliver as open source that are things the company does. For example, how do you make sure you're streaming jobs or your Lakebase database doesn't You know, lose all your data at night. Well, that requires an operational team that's going to sit there. There's no way. It has to be a service. So like we want to make sure as a company, we're really good at those in front services and then we're as open as as we can in terms of like what you build on top.

[11:42] **Reynold Xin**
I mean, speaking from a benefits, I think we're already seeing pull requests of all kinds of ecosystem integration, even though it was only released on Saturday.

[11:50] **Matei Zaharia**
Yeah, Saturday. Yeah.

[11:51] **swyx**
So someone see what's going on. Yeah.

[11:53] **Matei Zaharia**
Yeah, you can look at the merge lines. I actually asked Omnigent this morning about the 400 merge already. Yeah, I think quite, I would guess around half are not from our team. But for example, someone added support for running it on Kubernetes. People added many cloud sandboxes. So this can launch a cloud sandbox and run your agent in there, which is great for sharing too, because it's not like on your laptop and someone's like running scary code on there. So yeah, many startups have put those in and we expect to see more of them. We also have more agent harnesses already. Courser, CLI, and antigravity also.

[12:34] **Reynold Xin**
Yeah.

[12:34] **swyx**
That's all beautiful. I feel like the last time this happened, there was the rise of the modern data stack. I don't know if it was that useful. I'm actually kind of curious. You're post-mortem. I think most people will agree that it is finally dead. But maybe this arises to a new modern AI stack that does the same thing. I don't know.

[12:53] **Reynold Xin**
I mean, I think the modern data stack was a pretty useful thing, probably even up until this day. I think what Maybe for the audience who don't actually understand the history, I think the modern data stack is effectively decomposed into you need a layer to ingest the data in, you need a layer to transform your data, and then you need a layer to maybe visualize your data. And all of this runs on some sort of data warehouse, or later on, as we're doing data warehouse, also Lakehouse. I think that concepts are all very powerful and very useful. It's enabled a lot of workloads. What people eventually run into It's kind of a question of unification and consolidation is, hey, do you really need to chop all of this into different pieces and work with so many different vendors and platforms in order to get like a very simple visualization done?

[13:40] **swyx**
Right.

[13:41] **Reynold Xin**
So I think like over time, everybody started realizing that customers are pushing us. We started to realize that. So we started building more and more capabilities and trying to consolidate. And at the end of the day, now customers don't have to worry about having me hook up five different systems in order to produce a chart. But the, I think honestly, something like this is probably happening in how many different frameworks do you want to hook up together in order to produce, like do a very simple agent?

[14:06] **Matei Zaharia**
Just to be clear, I would say the core of this is this common API on top of all the harnesses. So the API is basically like you've got an agent session and you can send in a message or like a file, basically, that's what you can send in. And then you get out, you know, these streams as it's streaming text or as it's doing tool calls. And the other thing you can send in is you can like tell it to cancel or turn. So that's the API. Now, the thing we did is we Could get you that on top of like Claude code running in a terminal codecs, you know, pi. Open AI SDK, all that stuff, we map them all to that same interface. So that is something that you'd have to maintain yourself if you built your own like agent orchestrator. And then whenever Claude changes its API, you got to, you know, tweak your thing or it's going to lose some messages. So that's the thing that's valuable to maintain. Then on top of that, like we built a few apps.

[15:00] **Matei Zaharia**
I think we built a pretty cool UI and stuff, but that's and we build the security and control piece, which I'm excited about. It's that common interface and that doesn't try to be a stack. And in fact, you could plug in your own UI on top of this server. That's one of the use cases we care a lot about because we want to use this in our own products.

[15:20] **swyx**
Yeah, it should be everywhere.

[15:22] **Matei Zaharia**
Yeah.

[15:22] **swyx**
I think one of those things that is really interesting to me is, well, first of all, I'll endeavor to do everything and not call it the modern AI stack because One of the first people that told me about compute sandboxing was Nikita from NEON. A lot of people think about NEON as serverless Postgres with the separation of compute and storage. you know, instant branching and all those things, but actually every database company is also a compute company.

[15:51] **Matei Zaharia**
Yeah.

[15:52] **swyx**
And so he was actually showing to me his whole, his sandboxing solution. I don't think he ever launched it.

[15:57] **Reynold Xin**
So our sandbox solution, the reason we could have built it so quickly was because we realized if you just take the actual lake-based architecture and remove the database from it, by the way, it was coming from Xeon. Now there are some, Differences, for example, in the one to support this particular workflow is important to have local persistence because you want your state to persist. Your libraries, you don't have to install your library every time. Whereas the Neo architecture, because of the separation of storage from compute, you don't need persistent local disk. So there's some differences, but at the end of the day, yeah, it's...

[16:35] **Matei Zaharia**
Yeah. So this is when you run like a coding sandbox, like if I use it, we have the DevInfo internally at Databricks. There's like many, many like tens of gigabytes of data just for like all the source code and like artifacts and stuff that I built. And I want that to come back next time. So, but yeah.

[16:52] **swyx**
Before the show, we were talking about some statistics that might be surprising at the adoption. It could be internal, it could be external, whatever comes to mind, just to impress people the scale of this is happening.

[17:02] **Reynold Xin**
So we on the analytics side, I think we launched We have maybe 50 or 60 million virtual machines a day across all three clouds. So we're one of the biggest compute orchestrators out there.

[17:13] **swyx**
That's for sure for CPU compute.

[17:15] **Reynold Xin**
And all of this process, I think, exabytes of data. I joked about depending on which time zone you are, typically before you have breakfast, Databricks would process exabytes of data already on that day. And on NEON, it's actually pretty interesting too. It's launching, I think, 13 million databases a day now.

[17:35] **swyx**
Yeah. To me, that was like a big, what do you mean?

[17:39] **Reynold Xin**
And a lot of those were thanks to agents and branching experimentation because we made it so easy and so quickly. And thanks a lot to Nikita's team to launch databases. So it's changing the way people We use databases.

[17:54] **swyx**
Yeah. Okay. We're going to go into more database talk in a bit, but I want to make sure we close up anything on Omnigent. You mentioned you're excited about the security and control side. A lot of companies are figuring that out right now, as well as the spend side. What have you found there?

[18:10] **Matei Zaharia**
Yeah. So I spent quite a bit of time talking to internal users, developers, security team, you know, managers, and also lots of customers. And there's a few things like, first of all, One thing that immediately became obvious is for security, there's this tension between usability and security. A lot of coding agents today have very basic things like, you can tell me which tool patterns I'll allow or disallow or whatever. It's like yes or no. But that puts you in a very tough spot. So just as an example, should my agent be able to read some confidential Documents or let's say should it be able to install new packages from NPM, which you know, maybe it's a it's compromised. Yes or no, like maybe maybe I want to allow it. Should my agent be able to publish stuff to the company website? Well, if I'm using at the code on the website, yes.

[19:08] **Matei Zaharia**
But should it be able to do both so it can like grab a confidential document and be prompt injected and leak it? Probably not. So the thing we decided we need is stateful or what we call contextual policies where you keep track of the state of that session. It's not like, is it allowed to push to the marketing site or not? But like, hey, if it did a risky thing, like it installed, you know, a one day old package from NPM or it read like a thousand confidential docs, then No, don't don't do it. Otherwise, maybe it's okay. That's one example of like moving that trade off. So it's both more secure and more useful by having A more powerful engine, essentially, this requires tracking sessions. The other piece that was interesting there is like there are these very low-level events it's doing, and you want some libraries on top that parse them. Like, for example, we have a MCP server on Google Drive internally. It's got 60 API calls.

[20:04] **Matei Zaharia**
Like, how do I know which of those, like, will share a document with stuff on the internet and which ones won't? It's annoying. So we designed in Omnigent the policy layer so that it's functions and you can have libraries, like someone can make something that maps the low-level events to high-level ones, and then you write a policy about the high-level things that came out.

[20:25] **swyx**
This is related to the Panther.

[20:27] **Matei Zaharia**
Yeah, Panther will help with that. Panther is kind of a similar idea on the event processing side and it's Python based versus a weird custom language. This is sort of more as in real time. But these are the cool things. I think the contextual or stateful part and then the way it can be libraries. And that was another reason to make it open source because others will write libraries and like we and our customers can use them. And the final thing, because it's stateful, one of the states we track is how much you spent in that session. So I've had like, I asked an agent to debug something and it spent $500. It's because it decided to read a lot of log files and burn a lot of tokens. But I can literally say, okay, launch a sub-agent to do this and cap it to spending $5. Like ask me for permission if it needs more.

[21:20] **Matei Zaharia**
And because we're counting that within that session, it will pop up and tell me, okay, you spent $5. Do you want to go on?

[21:27] **Reynold Xin**
So important context here. Matei spent the last five years, a lot of his time was architecting UND catalog at Databricks, which is the governance layer for data.

[21:35] **Matei Zaharia**
That's right. Yeah.

[21:35] **Reynold Xin**
And he's sort of combining expertise at that layer together with all the AI governance.

[21:40] **swyx**
Yeah.

[21:41] **Matei Zaharia**
Yeah. But I also spent a lot of time being annoyed by coding agents and getting prompts. And also as the CTO, I don't want to end up on the front page as like I installed some weird NPM package and leaked. I'm especially bad, but also I have very little time, so I don't want to sit there approving, like, do you want to run a 20-line, you know, bash script? Yes or no? So that's why I spend a lot of time figuring out, like, how can I make it as safe as possible and not annoying?

[22:10] **swyx**
Yeah. Is safety and let's call it security a bigger concern than token maxing or token budgets? You know, which one is like?

[22:19] **Matei Zaharia**
Oh, yeah, they're both there. I mean, I don't know. I guess it depends on the type of company you are. So I think some companies like the budget is limited and, you know, they really care about that.

[22:34] **swyx**
I mean, you can be Uber and still be concerned, you know?

[22:36] **Matei Zaharia**
Yeah. Oh, yeah, totally. Yeah, yeah, yeah.

[22:38] **Reynold Xin**
I mean, for us, security.

[22:40] **Matei Zaharia**
For us, security is absolutely critical as a cloud provider. It's the most important thing. And token maxing, we're not so worried about it yet, but I've seen that. For example, I talked to some consulting companies. They have 100,000 employees who are all coding for customers. If those each spend an extra $1,000 a month, that's not fun. We have only a few thousand engineers.

[23:06] **swyx**
What's the policy in Databricks? Is it just unlimited?

[23:08] **Matei Zaharia**
It's unlimited, but we use our own product to analyze the traces and stuff and we have a team that's You know, looking to optimize and to see if anyone's doing something weird. And we actually had some really cool insights just from analyzing current tracers, like which models are better at, say, Rust versus, like, you know, TypeScript or whatever. So, yeah, at least in our code base.

[23:31] **swyx**
Yeah, amazing. Obviously, I have to ask the token mixing question, obviously. I think that's a key thing. But yes, security and control above that and figuring out a sane layer that you can have some autonomy, but not too much.

[23:43] **Matei Zaharia**
Yeah. And we want to make it super easy as an engineer. You should set it. So in Omnigent, you can ask your agent, set a policy on yourself to do this.

[23:51] **swyx**
If there's something I should be showing, I don't, I don't see it on the GitHub, but in the docs, you can look at it later.

[23:59] **Matei Zaharia**
Let's look in the docs on contextual policies if you want to see.

[24:04] **swyx**
I just like to point people.

[24:05] **Matei Zaharia**
Look at the built-in policies.

[24:06] **swyx**
If you want to, you know, follow up on this, this is exactly where to look. Right.

[24:10] **Matei Zaharia**
Yeah, yeah. And the story of these is like I just wrote, you know, like I wrote a doc with like 10 ideas for things before as you were working on them. Well, that was like my wish list of things people asked. And I told the team, like, hey, can you do like at least five of these for the launch? And then they just got back with all of them. So you can come up with more, but some of them are just meant to be examples. Really, you can intercept any event the agent is making, and you can then either block or force it to ask the user or allow, and you can update states to keep track of stuff.

[24:46] **swyx**
Yeah, because, you know, ultimately I think of you as like a systems designer. You let people plug in, right? That's the whole modus operandi of what you do.

[24:54] **Matei Zaharia**
Yeah, yeah. And we care a lot about also composability. Like can someone else write a library that others use, which this is meant to.

[25:00] **Reynold Xin**
There's also a batteries included philosophy here, probably very similar to how you did Spark, which is you could just start using.

[25:06] **Matei Zaharia**
Yeah, that's right. It has to be good out of the box at certain things, and then you can build your own things on top that we don't want to do. But in Spark, if you just want to read a table or do aggregation, it should be awesome out of the box.

[25:23] **swyx**
People want to catch up on Omnigent. They should watch your keynote. They should go through the GitHub and the docs. If they wanted to contribute or they want to build on this ecosystem, where would you call out as the most high leverage places to get involved?

[25:36] **Matei Zaharia**
Yeah, do get involved in the Discord and in GitHub. Our team is there, is monitoring. And some of the things people ask for, we just built ourselves. Some of them, you know, we're collaborating with them to build it. And also tell us how you would like to I think especially for developers, everyone wants it to work their own way and a really good developer, you have to hear the feedback on all the ways and figure out the abstractions and how to let people customize. So we'd love to hear if you think, I don't want it to work this way, tell us. We really just want to get that compatibility layer across agents and then let you do stuff on top.

[26:14] **swyx**
Um, is there any, uh, you know, in terms of like the startup side, I'm, I'm a founder. I want to, I see an opportunity I want to get in front of you. What's your request for like a startup that like, you know, I wish someone was working on this.

[26:26] **Matei Zaharia**
Oh, for a startup.

[26:27] **swyx**
Yeah. Like, you know, you're, you got your own startup. It's doing well, but like, you know, if you weren't working on your own startup, what, what is like obvious that you should. You advise many startups too, obviously.

[26:37] **Matei Zaharia**
I mean, I do think just as a company with a lot of engineers, like anything that helps me make sense of how people are using coding agents, but also quality or like you should write, you know, you should add this skill or you should write this thing or your agents are really horrible at tasks involving this service. So I go spend time. That would be nice.

[27:00] **swyx**
Yeah, the closest I found is this team, Git AI. They started with like, we will just do code and human attribution, but they're basically building the analytics layer on top of that. I do think like there are a bunch of like artificial analysis is obviously doing super well with their stuff. So there will be people, I think this is like We're going to talk about the domain of consultants first, but then people who actually build software. Let's say we have the management plane for coding agents.

[27:31] **Matei Zaharia**
Yeah, I think there'll be a lot of insights there. You have it in other areas.

[27:34] **swyx**
Okay. Well, and then the other big thing is your dream engine. Maybe you want to tell the story of LTAP. I'm going to make people listen to our Ankur Goyal episode where we talk about single store, HTAP and all that history.

[27:53] **Reynold Xin**
The LTAP idea is actually pretty simple. So if people have heard of the Ankur's talk about HTAP, it's effectively the world of databases. Sorry, there's like maybe a lot of context needs to be injected here.

[28:05] **swyx**
I am happy to be the database podcast that I'm forcing people to like learn your databases, guys. You cannot vibe code with just markdown files.

[28:14] **Reynold Xin**
It's one of the most important fundamental systems technologies out there. But the world of database is effectively split into roughly two halves. There's what we call OLTP databases, which are transactional. And think of your Postgres, your MySQL, your Oracle databases. And the other side is what we call analytics. And sometimes you might have heard the term OLAP. And the difference is on OLTP, you typically have, maybe you run some transaction on some event that looks up at one specific role. We update that role, right? It's a very role oriented. So data structure and on analytics, you're trying to reason on the data. You're trying to compute, hey, what's my revenue per store? What's my, how's my website doing every day? And then you eventually want to probably end up running machine learning on it to predict, hey, how will my maybe sales be going in the future? They are so very different architecture and everybody start with OLTP databases. Every app, when you become serious enough, they need more than markdown files. You need to have a database. You want to boost your data.

[29:14] **Reynold Xin**
You want to have some transactional consistency. But once you want to reason on the data, if you only have like a hundred rows, it's probably okay to run it on your Postgres or your MySQL database. But once you have more data and want to run more complicated analysis, the very analysis might And we're here to help you crush your Postgres database. So you start doing, getting data out of the database. Replicate them into the analytic systems.

[29:40] **swyx**
Which for people, Elasticsearch is like a big...

[29:42] **Reynold Xin**
Yeah. So some of them actually get into Elasticsearch for like block analysis. A lot of our customers obviously get into Databricks to run more sophisticated things. And there's this term called CDC. And what it does, it reads the binlog of the database. And if you don't understand what binlog is, it's fine. But it's a little delta of the data and it reconstructs based on the delta, the state of the database on the analytic side. But CDC is like a very painful thing. It's how basic standard in industry, everybody uses it. But it ends up being served. I think many data engineers ends up being waken up at like 3 a.m. because there's some pipeline thing.

[30:22] **swyx**
You know, my explanation is like everybody just like, you know, became a $5 billion company just by CDC.

[30:27] **Reynold Xin**
Yeah, exactly. CDC is like a very, it's one of the most boring, but one of the most fundamental operations, like powering modern society. But it's so brittle that we joke that it should be called continuous data corruption because you might change your schema on your LTP database and then the CDC pipeline fails to handle the schema change and then everything.

[30:50] **swyx**
And I mean, there's all sorts of tricks that you can do, like you add in like some versioning or whatever.

[30:54] **Reynold Xin**
Yeah. But it's a very, in general, very complicated. Like I think at my keynote, I asked the audience, put up their hand if they love their CDC pipeline. Only like maybe two people put it up. So if single store, like about maybe a decade ago, I think the industry had this idea, hey, what if I built a single database that can handle both workloads?

[31:12] **swyx**
Which like, by the way, every database person ever has always dreamed about this.

[31:16] **Reynold Xin**
This is the holy grail of database engineering. Why not build a single system that can do both of this? But it ends up just being a lot of compromises. One, I think one of the first issue is that, hey, each, they said Postgres has a massive ecosystem, right? You want to be using the tools that's built for Postgres. And Spark, for example, has a massive ecosystem. There's a lot of libraries you want to use. If you were to create now a new thing, You don't have an ecosystem. You tend to create a new, smaller proprietary API and you're lacking both. And it's also very difficult to make it performance-wise to be comparable on either side. So it ends up being actually sucking on both. And our whole idea of LTAP is kind of obviously a wordplay on the term HTAP is that we think this is HTAP done, right? HTAP wants to build a single engine for both. We think you can get 99% of what you need by unifying the storage. And just have a single storage layer.

[32:13] **Reynold Xin**
And once you have the single storage layer, if your Postgres databases are writing data in a column oriented format, everything analytics can just go read that data directly without any delay, right? There's no pipeline in between. So all the data will immediately be available for reasoning analytics. I think I was telling some customers earlier, hey, when we talked about this is going to be super useful for agents, I actually at first didn't really believe in it myself, even though we wrote that positioning. But then last night I was having dinner with an Australian customer and they actually told me, oh, hey, one of the big issues we have is we have all these logs from our services and we see SLA dips. And want to investigate. But then there's no way for those agents to even understand what's going on in the actual databases themselves. All we see is just like product telemetry of the database and the services. It would actually make those agents 10 times more powerful if they understand, for example, who's actually placing those orders. What is happening? What exactly are they doing?

[33:11] **Reynold Xin**
So now I'm actually still on our own message. I think it's really kind of, it gets you basically the, almost all of the benefits of the HTAP Holy Grail, which is, hey, make the data available immediate for reasoning analytics.

[33:26] **swyx**
Yeah, I think, you know, in the way that humans are generally intelligent and want to have the ability and access to query anything, even while they do the work, they also need history and need context and like, Where else is it going to get contacted? It's an analytical workload.

[33:42] **Matei Zaharia**
I remember when we had incidents with our databases and engineers said, well, I can't just run a giant query on it to see what's going on because that's going to bring down the database and hurt it even more. Like that's the kind of stuff that this gets rid of because you spin up a whole separate fleet of machines that's doing the analytics. You're not overloading like the main database, right? That's still trying to serve stuff.

[34:04] **swyx**
Yeah, so this has been a dream for a while. What had to get done in order to get to today? I feel like you have announced variants of this several times, but it wasn't as clear as LTAP. I think LTAP is like, okay, we've got it, guys.

[34:21] **Reynold Xin**
I was talking to somebody at Meta and he was asking me, hey, what's the catch? Why is it possible now? And I think the reality is we took a lot of time to actually work on the Lakebase architecture. And obviously a lot of it came from the NEON team, which is a separation of storage from compute. And it turned out we're just a tiny little step away. Going from that to this LTAP idea, which is, hey, we just In the NEON architecture and in Lakebase architecture, we're writing data in row-oriented format to the open data lake. But in there, we're writing in Postgres pages. Actually, Aliyah and I were spending a lot of time debating, hey, can we actually just change that to write in column-oriented format? And we're just debating. One day, one of our engineers was like super smart, came in. He's like, hey, I just prototyped it, it works.

[35:07] **swyx**
Wait, so prototype what?

[35:09] **Reynold Xin**
Prototype, instead of storing the data in the data lake in the row-oriented format, Like Postgres pages, write them in Parquet. And he just made the observation that, hey, our storage flea has a lot of extra idle CPUs. And we can use those CPUs to do the transcoding from row to column, where row is good for OLTP, but column is good for analytics. So let's do that transcoding at that time. And as a matter of fact, once you transcode the data, the data compresses better. So from those services writing to, for example, S3 or other data like object stores, you can actually write it faster because now they are now smaller. So there's no overhead. It's no compromise in performance.

[35:53] **swyx**
Some CPU overhead.

[35:54] **Reynold Xin**
Yeah, because, but we had extra CPUs anyway.

[35:56] **Matei Zaharia**
We had that fleet anyway.

[35:57] **Reynold Xin**
So the debate ended. I mean, it's one of the classics of a tech issue of a lot of debate, but then somebody actually went ahead and just tried to prototype it and it worked.

[36:06] **swyx**
But like something this strategic and important to the company, I expect there to be like a kickoff thing, like a design doc, nothing like that.

[36:13] **Reynold Xin**
Nothing like that. We were debating in many, many meetings and then we're just debating whether it's possible or not from first principle and then somebody just did it.

[36:22] **Matei Zaharia**
Yeah, I mean, if you set yourself up so people do that, that will be great. That happened a bit with Omnigent, too. I think if I just had a doc on like, we can make these together, everyone would, you know, would think, oh, what about this? What about this? But then if you try it out, it helps. And then if you have real users and they bash it and like it's still working, or in this case, if you have the workload, you know what the workload looks like. You can just test the same pattern.

[36:46] **swyx**
Tech aside, which is very cool. This is like the most important thing, the culture of Innovation. And you don't have to ask my permission. You don't have to do a whole formal process. Just do it.

[36:59] **Reynold Xin**
Well, especially these days, I think with AI, it's actually easier.

[37:02] **swyx**
I think you are very right. I mean, I made a lot of C-suite of large companies and I think at scale, things slow down. And I'm sure you felt it already, but somehow you have this core of people that are exempt.

[37:15] **Reynold Xin**
How? I think we hire and we work with really, really good people and that's a very important part of it, empowering them. But also spending a lot of time, maybe us in the trenches matter a lot also.

[37:28] **Matei Zaharia**
Yeah, I think people can adapt to being in the larger company. So that helps. And we want to make sure they know that they can try stuff and settle debates and have a lot of examples of how it was done before or launch a thing in beta or whatever. And then the other thing I do think as a company, like despite the size, Don't launch that many products. We try to keep it pretty coherent. That was actually the whole theory of the company. Instead of having 20 Amazon services, you need to set up an analytics and machine learning stack. You just have one. It's the same API, the same semantics across all of them, the same copy of the data. So that requires unification. And then we basically added one more thing at a time. We added storage with Delta Lake. We didn't used to do any storage. Then we added SQL. We added machine learning platform stuff. But yeah, don't do too many, but do those things well.

[38:28] **Matei Zaharia**
And that also helps keep it manageable.

[38:33] **swyx**
Yeah.

[38:33] **Reynold Xin**
The other thing we kind of encourage a lot is instead of building to borrow the ocean for everything, let's figure out how do we do it incrementally? How do we do it very quickly? Like many of our products, they're built in the span of weeks. And then we go to, Hey, like usually my first question to whoever team is building is who's the target customer? Who are you working with? Are you on a first name basis with them? Are you texting with them? I think having that very tight loop.

[38:59] **swyx**
Can you bring up another launch that comes to mind in this kind of thing? I just want to give examples.

[39:03] **Reynold Xin**
Omnigent itself happened that way.

[39:05] **swyx**
Who's the customer?

[39:06] **Matei Zaharia**
Omnigent was more of an internal thing, actually, because we would use it for our development. Basically, the whole AI team got access to it and was using it. And we made sure it works from the beginning with our internal code base, which is a monorepo that's enormous. We gave them some infrastructure. We gave them lots of token capacity. So it's all the developers. We had others. I don't know.

[39:32] **Reynold Xin**
This is, I think, a public story, but I'm just going to ask Marketplace, OpenSharing, all of them had I just don't remember exactly which ones publicly referenced.

[39:41] **Matei Zaharia**
Well, very early in the company, there was like Delta Lake, which is the transactional storage layer we did. We had our largest customer at the time said like, okay, I need some, I want something in the cloud because, you know, if the rest of our network is compromised, like this thing needs to be separate to store and query the events and then talk to us. He said, okay, this is the rate of events per second. This is like the freshness I want. Can you do it? So that was like way larger than any workload we had. And we had our engineer working on that, Michael Armbrust, and he worked just to make this work. And once it worked for them, you know, it worked for everyone else. Yeah, this was early in the company, probably like four years ago.

[40:24] **Reynold Xin**
2018? Yeah, 17, 18. Do you have other examples? I mean, there's Cleanroom, which is basically how you share data in a way without sharing underlying data, but you allow specific operations. Those were done effectively initially just for two customers. I think the industry has a sense of, hey, maybe if you overfit to like one or two customers, it's going to be really bad for you. But I think the downside of overfitting is much smaller than the upside itself. And if you sort of try to be too ambitious and boil the ocean, it's a much bigger problem.

[40:58] **swyx**
Yeah.

[40:58] **Reynold Xin**
Because you might end up actually having no customer.

[41:00] **swyx**
Yeah, that's the more likely outcome. And then you can sort of pivot from there. I do think there is such a thing as a bad customer that sometimes you shoot fire.

[41:08] **Reynold Xin**
They could exist sometimes if you drive. One of the challenges I think we probably see and maybe many newer generation companies are seeing is tech companies are very, very different from non-tech companies or traditional enterprises. And if you optimize everything just for tech companies, you might have various challenges, scaling them outside of tech companies.

[41:29] **swyx**
Okay. What are the top three differences that you always think about?

[41:33] **Reynold Xin**
Governance is a big one.

[41:34] **Matei Zaharia**
I think, yeah, a big one is like, yeah, security, you know, data privacy, governance, all that stuff. So usually if you're building some kind of like B2B or developer tool, like your biggest market is going to be enterprises, but it's just very different. A company that's existed for like, you know, It's had some form of IT for like 30 years. They have so many legacy systems or they operate in a regulated space. Whereas a startup or even like a, you know, like sort of more recent tech company, all the, everything is new and sort of pristine. So yeah, it's just different. And if you've never worked with enterprises or been in one, you just won't know about it.

[42:13] **Reynold Xin**
And the procurement process is probably quite different. There's actually far more stakeholders.

[42:17] **Matei Zaharia**
Yeah, that is one. Yeah. Another piece that's interesting is I think some tech companies, you know, people will say, oh, I can build that myself. I'll just build that myself.

[42:27] **swyx**
I don't think people say that about Databricks.

[42:33] **Matei Zaharia**
And it depends on the teams and things. But on the other hand, like many of the enterprises, I actually, I don't, I never want to be in the business of building that. Like I don't want my, you know, whatever, I'm a retailer or something. I never want to be down because like some weird, like nerd, like couldn't get We're streaming pipelines working. That is not what I'm doing.

[42:53] **swyx**
This makes them great customers, to be honest, right?

[42:55] **Matei Zaharia**
But you have to understand, it's hard without having work there and stuff like you may not appreciate.

[43:01] **Reynold Xin**
Look, I think they all agree. Don't get me wrong. They have different challenges. But many of the tech companies, for sure, there's a lot, far more DIY.

[43:09] **Matei Zaharia**
On the flip side, you have people who are, they're very much experts in their domain. Like they're building airplanes. They're, you know, designing medicines, whatever. They just want to bridge the technology. They don't want to learn databases or whatever, as cool as we think it is, even as interesting as the average software engineer might think it is to read a little bit. They just never want to know. They just say, I have a giant matrix or whatever with my clinical data. How do I cluster it or whatever? So yeah.

[43:40] **swyx**
Yeah. Yeah, that's true. Okay. So and then I wanted to actually build out the sort of Dream Engine vision. Where does log lead?

[43:49] **Reynold Xin**
So one of the things we realized maybe a couple years back is that actually every single database engine out there, especially on the analytics side, are kind of a decade old. Pretty much everything that had reasonable traction are about a decade old. And they all started targeting some very specific, narrow use cases. And then over time, it's become more and more successful. They have grown in their ambition, and then they try to support more and more use cases. But the fastest way to support those use cases tend to be hacked around the abstractions that were initially created that were not for those use cases. But you can kind of support them more or less okay. And before you know it, after 10 years of organic evolution that way, It becomes a gigantic pile of shit. And by the way, that includes Databricks. And very, very few company or very few systems I think have the gut to say, let's go start from scratch.

[44:45] **Reynold Xin**
Let's go back to the drawing board, the design, knowing everything we know today after a decade of workloads and probably billions in revenue, let's attempt to rewrite it from scratch and actually make sure it will work. And then we can support all of those use cases. So we started doing that. But it's a very ambitious project. By the way, you can search on Wikipedia. There's a thing called second system syndrome.

[45:09] **swyx**
Yeah, I know that.

[45:09] **Reynold Xin**
Our second system effect.

[45:11] **swyx**
Every developer must know what a second system is.

[45:12] **Reynold Xin**
It's basically you built your first thing and it works out great. And the second one is bound to fail because you become too ambitious. And then you ask so many requirements.

[45:20] **swyx**
You think you know everything. And then you're like, I'm going to design the perfect system this time.

[45:24] **Reynold Xin**
Yeah. And it turned out it's not perfect. And then they start failing and you're too ambitious, never launch and you get killed. The engineering team that actually started this, they were brilliant. I think we hired some of the best database engineers on the planet into Databricks, and they were brilliant. Thank God it's not their second system. Many of them have built more than Two in the past.

[45:44] **swyx**
Ah, nice.

[45:45] **Reynold Xin**
But they were still worried about this. Hey, building a database engine from scratch, I think the conventional wisdom is going to take like five years to mature. This would be a very long term project. It could fail. I think one of the engineers kind of jokingly said, hey, maybe we just call it Reynolds Dream Engine. If we name off the co-founder, maybe we're going to get canceled or killed. But I think they built something pretty remarkable. They went back to, they kind of changed the way the database engines were built from a paradigm point of view. Usually when you build a database engine, you read a lot of academic papers. You try to understand what the latest algorithms and data structures, and you put them together and see if they work or not. And there's a high risk of failure there also, because whatever that looks really good on paper might actually look really good in 70% of the workloads, but then it backfires on the other 30%. When built a more of a factory for building the database, so they spent more time building this factory and the factory takes the decade of traces we have.

[46:42] **Reynold Xin**
I think they count as a quadrillion data points in the trace table.

[46:47] **swyx**
You don't drop anything? Or you see sample?

[46:49] **Reynold Xin**
We for sure sample, but there's like massive amount of things and they use that to build a model. I'm like a machine learning model, not an LLM, machine learning model. Machine learning model basically can very, very quickly tell us how any algorithm and how any implementation will perform for any specific type of queries with very, very high fidelity. And based on that, they can pick the most likely algorithm and data structure that will actually help with the different kinds of workloads, both at runtime as well as at implementation time. Because there's like unlimited number of.

[47:26] **swyx**
I mean, it sounds like you want to route to different data structures.

[47:31] **Reynold Xin**
Yeah. I mean, if you think about it, a single database has many things implemented together, but you want to make sure they all work well with each other. And then for any given operation, there might be more than one implementation. So we make it actually run really, really well. The reality is, algorithms that work super well, for example, for very, very low latency, might not work very well for Say, scanning through petabytes of data. Actually, most often, there's a trade-off there between throughput and latency.

[47:58] **swyx**
What are the key dimensions, like scale, throughput, latency, anything else?

[48:03] **Reynold Xin**
And the distribution of data, right? How sparse the data is, that matters very a lot. How frequently do you hit the same data?

[48:10] **Matei Zaharia**
How many distinct values and stuff like that.

[48:12] **Reynold Xin**
Those things matter a lot. Number of distinct value basically impacts the memory consumption of your aggregation, your hash. At some point, there's a hash table.

[48:20] **swyx**
In my write-up, I'm going to try to list all these out because I really want a taxonomy. To me, taxonomies are so helpful because it covers everything that you should think about.

[48:28] **Reynold Xin**
I think if you actually try to list it out, it'd probably be like a million different features.

[48:34] **swyx**
I always find like, okay, give me like 12. You know, like someone did, I think an Oracle paper in like 40 years ago did like the, these are the eight fallacies of distributed systems. That kind of thing is super useful. It's like, okay, think through these eight.

[48:48] **Reynold Xin**
But let me give you a very weird example, but it actually has a profound implication on performance, which is like, is your string just ASCII or does it have Unicode in it? How should you encode it?

[48:59] **swyx**
I mean, strings are the most complex data types. Yeah.

[49:01] **Reynold Xin**
So the, and that, like, for example, if string is super dense, you could actually convert every string into a, like, imagine you have to do a hibernation. Instead of having a hash table, you could actually have an array. Because if your string is dense enough, if you only have 256 options, you don't need a hash table. You can just do array lookup.

[49:21] **swyx**
Yeah.

[49:22] **Reynold Xin**
And they'll be far faster.

[49:23] **Matei Zaharia**
Like a country code or something. Yeah. Yeah.

[49:26] **Reynold Xin**
So it's actually like, probably millions of features in that model. But using that, they can, one, basically prioritize the different algorithms that might actually impact in practice. And many of them are very counterintuitive. It isn't actually things that you think might work super well actually don't work that well in practice. But also, more importantly, at runtime, you can dispatch the right algorithm and structure.

[49:47] **swyx**
I'm listening to the dream. I feel like Databricks is doing a really good job of the incremental evolution. Do you have to hard cut to a new system at any point?

[49:57] **Reynold Xin**
We designed it in a way that it can be incremental. So first we're releasing a new endpoint. How about this goes to the broader ocean versus what we wanted to do is one to the bite design. This new engine should be able to do everything we're able to do before and better, right? It's been particular. The better part refers to very low latency, low latency workloads. I can finish in tens of milliseconds, but we want to roll it out incrementally with incremental capabilities. So it doesn't take like five years to actually see the light at the end of the tunnel.

[50:29] **swyx**
I think that's a heroic task. I don't know what other way to say it. I am really interested in any sort of new workload and new databases. I mean, obviously, I think I've maybe established that I'm a little bit of a database nerd. The transactional databases, sorry, the accounting databases, like the Tiger Beetles. I don't know if you've seen those.

[50:50] **Reynold Xin**
What do they do?

[50:51] **swyx**
Dual entry accounting database. It's just meant to really model Financial accounts and credit systems.

[50:56] **Reynold Xin**
It's like a very specific brand.

[50:58] **swyx**
Very high throughput. No, it's the way you were talking about how everyone like starts with a thing and then they scale up and then they tack on other things. It's exactly that. And then I recently interviewed Simon from TurboCoffer. Same thing. And Chroma as well. All the vector database companies of 2023, all are suddenly now just, we're just generally, general storage, blob storage.

[51:18] **Reynold Xin**
Vector database should have never been a separate category.

[51:21] **swyx**
I think it used to be a hot take. Now it's like the conventional wisdom nowadays. What should be a separate category? You know, if everything becomes LTAP, like what's...

[51:30] **Reynold Xin**
I think the thesis of LTAP is we're not collapsing the databases at the actual query layer.

[51:37] **swyx**
We're just collapsing the storage layer.

[51:39] **Reynold Xin**
And that's, I think, a very important part. And we actually don't think it makes sense to collapse And we're going to talk about how to integrate the query layer into a single like HTAP style database. And part of it, the other thing I think a lot of people had is, hey, it would be nice if there's only one query language I have to worry about. Instead of worrying about PostgreSQL and maybe Spark SQL, why not just one? But I don't think that's an issue for agents. Agents are very eloquent in PostgreSQL or Spark SQL. It's never going to get confused. As long as the data is there and it's accessible, agents will do fine. That might have been, so five years ago, might have been a problem for humans.

[52:17] **Matei Zaharia**
That could arise over time also, but it should, and this leads to how to do things incrementally, right? Like we realize you don't need it right now. We don't need to solve that problem to have a lot of value from the core Intel tap.

[52:30] **swyx**
Yeah.

[52:31] **Matei Zaharia**
Okay.

[52:31] **swyx**
I'm going to end the pod with a little bit or more of sort of spicier things. Everyone has like had the received within a separation of storage and compute and try to build the clouds. I had the same pitches from Snowflake. How have you succeeded where they failed?

[52:50] **Unknown Speaker**
That's rough.

[52:52] **swyx**
I mean, respecting that they are a competitor, objectively, you have outpaced them. What is the core insight from your point of view that you guys just went different directions?

[53:02] **Reynold Xin**
Probably the biggest fundamental difference. Both companies started around the same time. Both went to the cloud. Both focused on storage from compute architecture. But the biggest difference, one is open. Databricks never had a proprietary format. We started with the open ecosystem, started with Parquet and then evolved into Delta and Iceberg and all that. That's one big thing. I think it matters a lot. The other one is AI. Before October 2022, when ChatGPT came out, we had always pitched Databricks as a machine learning plus data. And a lot of the platform were built with machine learning use cases in mind. And obviously, AI is a little bit different. And Matei spent far more time there than I do. But the whole platform was, we never felt, hey, we're just a data infrastructure platform.

[53:53] **Matei Zaharia**
I think they started with, they thought, okay, we'll just manage the most valuable data and try to make it really fast. For that, we'll have Our own storage, you know, which is optimized with the engine. And then we'll just target like the small amount of data that like the managers and whatever, you know, finance people and so on, look at and make that super fast to serve. And, you know, it was a different space, whereas we started with like, we'll do the bulk processing and ingest. Like you've got a bunch of, you know, JSON log files, you've got whatever. We do that very large scale stuff, because that's what Spark was for, the large scale mappages like stuff. And then we'll keep the data in an open format. It might be slower, but like it's already out there. You can consume it downstream.

[54:41] **Matei Zaharia**
And it turned out that, you know, It's easier to go from that broad thing that's really good at the scale and ingesting and super low cost and create versions in it that have the speed and features of the, you know, super easy to use, like smaller data for business users thing.

[55:02] **swyx**
Start open and then optimize.

[55:04] **Matei Zaharia**
Yeah, start open and start large. Like in some sense, we started upstream of them. And there was a time actually when we both like sort of listed each other as partners because he said, if you use both solutions together, use Databricks for like your ingest and compute and then serve the tables out of Snowflake, you get all the visualization, all the very fast stuff like that's great. And then, you know, we both realized like customers were telling us like, why do I need this other thing? Why can't I just query your tables? And we said, no, we're horrible at that. Like, please use our partner for the SQL warehouse. And then they realized that like, wait a minute, so much of the computer is moving upstream into this other thing.

[55:43] **swyx**
You have to go into each other's territory.

[55:45] **Matei Zaharia**
But I think we did start with like the bigger scope and with the open thing. And that's important to architecture. Like as a, again, it goes to enterprises. Like if your company's existed for like 30 years, you've experienced, you know, being locked into Oracle and like all kinds of like crazy things. And if you're the CTO, There and you're setting up the architecture for the future for your company, you're going to want to pick a foundation that's open. And you only want like one way to manage data in your company. Ideally, you don't want like seven different systems.

[56:17] **Reynold Xin**
By the way, the open data format had won. I think now every enterprise wants to put data in open data format, but it was actually very controversial back then. When exactly? The Snowflake co-founders actually wrote a blog called Choosing Open Wisely, which basically I go against. I think they might have taken it down. You have to find it on archive now.

[56:38] **swyx**
It's never going away now. No, no, it's still there. I love the sort of perspective that only you guys will have because obviously you run the company. Thank you for indulging us. It's an incredible perspective.

[56:52] **Reynold Xin**
Maybe one last one. As you were talking, I think I have to give Ali a lot of credit. He's an incredible CEO. I think he's the perfect combination of IQ, EQ, technology, obsession, execution, business acumen. And he's also a founder, which makes it a lot easier for him to mobilize and execute. I think that's it.

[57:17] **swyx**
I thought there was going to be some technical choice that he contributed to.

[57:28] **Matei Zaharia**
He did for a lot of these. There were sort of forks in the road where he pushed for one way and then it became clear that that was the right way.

[57:37] **swyx**
I mean, there's a whole book that needs to be written about how the eight of you like, you know, work together and all that. I think there's been profiles that people have done. Second one, not a cleared question again. Mosaic. A lot of people in our community are curious on what's the sort of the model story of Databricks, right? Like when you guys bought Mosaic, the thing was like, okay, well, we can do fine tuning. We're going to do in-house model because they had the Mosaic models. And it seems like you're not doing that. And it seems like you're going towards more of the LTAP and the Harness stuff. What's the story there?

[58:14] **Matei Zaharia**
Yeah, I guess when Mosaic started, it was well known or became most well known for releasing open source LLMs early on. And they were general models. Actually, before that, they were doing other things. They were about optimizing training systems, basically. So they had the fastest image model training stack in the world and stuff like that. And then they decided to do LLMs, which was smart. They moved into it before ChatGPT. So they had some of the first open source LLMs.

[58:43] **swyx**
We interviewed John Franco and Avi for MPC7B.

[58:46] **Matei Zaharia**
Yeah, exactly. Yeah. Oh, yeah. Very cool. Yeah. Yeah. So we decided, you know, even though we did launch an open source model, DBRX, and, you know, we went up to like sort of above the LLAMR3 scale, we decided that we really want to focus on there'll be so many people releasing models. Instead of doing the general model where like, you know, a big part of the recipe is just throw in a lot of compute and just scale, we want to focus on like the next step also of, let's say you have the very smart model, how do you make it You know, useful for us. It was a lot about automating, like how, like, like making it very good at querying data. That's the first party agents we have called Genie. So it's like a virtual data scientist. Imagine, you know, there's someone who already knows all the stuff in your company inside out and knows all the machine learning libraries, all the data libraries, you know, all this stuff on the web, and you can ask them, Questions, you know, that's that's what we wanted to do first.

[59:46] **Matei Zaharia**
So that meant like, let's not focus as much on like, let's just train some kind of frontier model. But let's build this system using either external models or fine tuned, customized components. We're still doing quite a bit of model training though. And in fact, we're always, you know, we're procuring like lots of GPUs and stuff all the time to do it. And there's a few places where we're doing it. One is there are many high volume use cases where if you have a specialized model, it's just so much better than any of the general models you get. A nice example of that is understanding like documents, like PDF, Word documents, stuff like that. Parsing them. If you've ever tried to do that, it's It's frustrating because you send it to like, you know, like Claude Fable or whatever, it like almost gets it, but it gets some things wrong and it's super expensive. You just burnt a huge amount of tokens plopping in an image into there.

[01:00:41] **Matei Zaharia**
So our team built this document sort of vision model that takes a page and gives you back a nice JSON with all the components. And it's very competitive. It's like probably like a hundred X cheaper than those frontier models and still better. And that's actually done by one of the researchers who came from DeepMind, was a co-founder of ADAPT, like very early LLM scaling person, but focused on this. Likewise, we have, we're doing specialized sub-agents for part of what the coding agent does. And if you've seen the stuff on advisor models from Harvey and Anthropic. And UC Berkeley, actually, one of my grad students there wrote a paper called Advisor Models, I think before those came out. I mean, I'm sure others had the idea at the same time, but that's something that helps a ton. So, yeah, we actually showed some stuff just today at the keynote on...

[01:01:38] **swyx**
Is it Parth? Oh, you know Parth?

[01:01:39] **Matei Zaharia**
Yeah, yeah, Parth.

[01:01:39] **swyx**
Oh, he's speaking at my thing. He's doing Continual Learning Bench.

[01:01:42] **Matei Zaharia**
Yes, yes, yeah. I'm one of his advisors. Oh, yeah.

[01:01:45] **swyx**
We interviewed his brother, Chai, because he's also at a bridge.

[01:01:48] **Matei Zaharia**
Yeah, yeah, yeah.

[01:01:49] **swyx**
That family is very smart.

[01:01:53] **Matei Zaharia**
We're doing some of that and as we get experience with these in the first party agents, we're also doing them with customers. So my feeling is like customizing models is actually going to get way easier over time. That's what we're finding because the base models are smarter, so they generate better Traces and RL already, and then RL is about learning from your own past traces. And then synthetic data generation is way better, way easier now. We have pipelines just using open source models, like the same model generates training environments and trains itself and beats like OPRS and GPD 5.5 and stuff at a task. So I do think it's going to pick up like, you know, the thing is the ease of training, the algorithms is only going to go up over time. There's a question of when it crosses into mainstream, like instead of this, like, you know, specialized document parsing thing we did where like, you need a hardcore LLM researcher. When does it get easy enough that anyone can like sort of plop in some stuff and describe a task?

[01:02:53] **swyx**
Yeah. Well, you know what makes it easy? Interfaces. Yeah. And unified APIs. Because obviously if it's not interoperable, then you cannot switch.

[01:03:00] **Matei Zaharia**
That's what we're seeing with Omnigent and the composable agents. You can have sub-agents with specialized models and then you can train the whole thing. I think that'll help a lot too.

[01:03:11] **swyx**
The last thing I was going to leave, actually, I'm sequencing this, so I'm actually kind of proud of myself. Safia is, you know, talking about this. I interviewed him at Microsoft Build a couple of weeks ago, and then he wrote this essay, which I'm sure you've seen, which is talking about building a frontier ecosystem. He sounded, when I was talking to him, more like a Databricks CEO. I mean, this thing presumably went viral in my circles. I don't know in your circles. What's the sort of theory of like, you know, I guess tokens as IP building up the context, you know, he basically said everything but Data is the new oil or context is the new oil. Some version of that, you know, that you guys have heard before.

[01:03:54] **Matei Zaharia**
Yeah, I agree. I think the data you have, as you get better technology around that, like you can just do more in your domain with it. It's not even just about AI. Even when people, you know, started collecting stuff in real time, like I remember all the power companies put like the smart meters and stuff and all the car manufacturers started putting like sensors and cameras and stuff. Any technology makes data more valuable and can give you some advantage, anything that helps you do something with it and make some decisions, and AI is the same way. You had all this stuff that's just sitting there. Now you can have an agent automatically tell you. For example, instead of, I discovered a feature in my product is broken because a customer complained, the agent tells me, I noticed no one is uploading files anymore because they get errors or whatever. And as you saw with like radar and like as a database company, because we have all these.

[01:04:46] **Matei Zaharia**
The history of all the queries and all the table layouts and like how they work, we can build a new engine very quickly that actually is good. And we're confident that it's going to be good. So I think this is right. I think the question is exactly how it will land. But I do think like custom model customization, which Sajat talked about, is going to get easier over time.

[01:05:10] **swyx**
Yeah, which is why, by the way, I brought the model thing because they have their MEI things and you guys don't. That was to be the mental question.

[01:05:17] **Matei Zaharia**
Yeah, we do have, we're doing like RL fine tuning as a service and with a bunch of customers. We don't have like, basically, you know, we have like preview customers and we have a general something called AI Runtime that's like, we get your GPU clusters on demand with software stack in there that makes it easy to do training. We didn't like sort of, that's existed for a while. We've had like GPU compute for a while and that's where a lot of the mosaic stack went to help scale that. But yeah, we found that the engagements, like some of the, there's two types of customers. There's some who just want GPUs and libraries to like get data in and out and monitor. So that's what AI Runtime is. And then there's some that say, Hey, you know, can you actually work with me, build evals, build synthetic data?

[01:06:04] **swyx**
And that's what we're doing.

[01:06:08] **Matei Zaharia**
And as more things will transition from like being custom to not, but that's sort of how it is today.

[01:06:15] **Reynold Xin**
Going back to your original question, I think one of the thesis we have is actually the ones you can get the data in the right place. The AI models are becoming pretty good. The generic agents are fairly, I mean, Ali talked about AGIs already here. They have pretty good reasoning capabilities. Actually, I think many of the traditional software will be sort of rewritten. With the Zoom paradigm, which is just get the data to be there and then slap some agent on top, magic will come out. But without the right data, you can't really do that. And actually, our approach to going to security and our approach to going to the customer data platform space is like we launched two products at Data and AI Summit, one targeting So security teams and the other one targeting marketing teams. And those all have a lot of existing technologies out there. And I think our approach is just, hey, once you get the data in, everything is a lot easier with agents on top.

[01:07:09] **swyx**
Yeah, yeah. Well, you guys have been fantastic guests. I just love this discussion. I just love the ability to dive in on the tech side, but also culture and strategy. I hope this isn't the last time we chat. I mean, congrats on all the success so far.

[01:07:23] **Reynold Xin**
Thank you. Congrats on your success also.

[01:07:27] **Matei Zaharia**
Yeah.

[01:07:27] **swyx**
Yeah. I mean, Databricks is actually supporting my event, which is, so I run AI Engineer Conference and it is actually, I was, I've been attendee of Data AI Summit for a long time. And I noticed that it was like kind of, this is back in 2022. It was like 90% data and then 10% AI. And I was just like, well, okay, like we need it. We need the community thing that is like, Just 90% AI, which like now everybody is. So Databricks will be at the conference. And I know it's just amazing to see you guys build out the most like Interesting cloud that I haven't seen outside of the big three. And it's amazing how far you've grown. One of the most insightful, I'm not a VC, but I play one on TV. Ben Horowitz, when he was talking to you guys, advising you on just like, where is this company going? He was like, don't sell it to 100 billion or some version of that story, right?

[01:08:22] **Reynold Xin**
It was like, the company should be worth a trillion dollars. You're underselling it for 10 billion.

[01:08:26] **swyx**
And he doesn't do that for everyone. Like for some reason, like, you know, I think he saw the vision, but also the infinite runway that you have.

[01:08:36] **Reynold Xin**
We're lucky to have Ben. Yeah. He's a big supporter. Yeah.

[01:08:39] **swyx**
Amazing.

[01:08:40] **Matei Zaharia**
Okay.

[01:08:40] **swyx**
Well, thank you so much.

[01:08:41] **Reynold Xin**
All right. Thank you so much, Swyx.

---

# 中文翻译 (Chinese Translation)

---
podcast: "Latent Space: The AI Engineer Podcast"
episode: "Why the Frontier Ecosystem must be Open — Matei Zaharia and Reynold Xin, Databricks"
link: https://podwise.ai/dashboard/episodes/8304753
publish-time: "2026-06-24"
save-time: "2026-07-01"
---

# Why the Frontier Ecosystem must be Open — Matei Zaharia and Reynold Xin, Databricks

## Summary

Databricks 的创始人 Matei Zaharia 和 Reynold Xin 讨论了公司从一个小型伯克利聚会演变为全球人工智能和数据强国的过程。谈话的中心是 “现代人工智能技术栈”，特别介绍了 Omnigen，一个用于协作代理开发的开源平台，以及 “LTAP”（湖屋事务性/分析性处理）架构。LTAP 旨在通过使用单一存储层来统一事务性和分析性工作负载，消除传统数据工程中困扰的脆弱和复杂的 ETL/CDC 管道。除了技术创新，讨论还强调了开源生态系统的重要性、人工智能治理的必要性，以及快速、增量创新的文化。通过优先考虑开放数据格式并利用大量内部痕迹来优化数据库性能，Databricks 继续将分散的数据基础设施整合为一个统一、可扩展的企业人工智能应用平台。

Takeaways:
1. 统一存储层实现对事务数据的实时分析，有效消除了脆弱复杂的变更数据捕获（CDC）管道的需求。
2. 通过统一的 API 和服务器端编排标准化代理工作流，对于在多样化环境中实现安全、协作和有状态的代理交互至关重要。
3. 建立一个用于数据库工程的 “工厂”——利用数千亿历史数据点来建模和预测算法性能——可以比单靠学术论文更快、更可靠地进行系统开发。
4. 从一开始就优先考虑开放数据格式和生态系统，比起专有的闭环架构，能够创造更强大的竞争优势，因为这符合企业长期数据主权的需求。
5. 对于高容量、特定领域的任务（如文档解析），专业化的较小模型通常比通用前沿模型提供更优越的性能和成本效率。
6. 有效的代理治理需要上下文、有状态的政策，监控会话活动和风险，而不是依赖简单的二元权限控制。
7. 在企业市场取得成功的关键在于认识到非技术组织优先考虑治理、安全和集成，而不是构建定制的专有内部工具。
8. 逐步开发复杂基础设施——通过优先解决特定的现实客户痛点——显著比尝试 “煮海” 的巨大多年度架构改造更有效。

## Chapters

### Chapter 1: Omnigence 和协作编码代理的架构

Omnigence 通过提供一个统一、安全的平台来解决代理开发中的碎片化问题。该架构支持跨环境的可移植性，使开发人员能够共享会话、维护历史记录和实施安全策略。开源这个平台促进了网络效应，使社区能够贡献集成和云沙箱支持，类似于 Spark 的早期开发。这种方法使团队能够超越 “直觉编码”，迈向结构化、互操作的代理工作流框架。

### Chapter 2: 代理开发环境中的治理和安全

管理代理工作流需要平衡可用性与严格的安全和成本控制。上下文状态策略允许进行细粒度权限管理，例如根据会话状态限制安装未经验证的软件包或访问机密文档等高风险行为。Databricks 每天处理 Exabytes 的数据，在代理级别实施强大的治理对于防止数据泄露和有效管理令牌预算至关重要。目标是为开发人员提供自主权，同时保持企业级安全性。

### Chapter 3: LTAP 与事务性和分析性处理的统一

LTAP（Lakehouse 事务/分析处理）旨在通过统一存储解决脆弱 CDC 管道中固有的 “持续数据损坏” 问题。通过将数据以列式格式直接写入数据湖，分析引擎可以实时访问信息，无需复杂的复制。这种架构利用存储设备中的闲置 CPU 能力执行行到列的转换，提供单一系统的好处，而不牺牲传统 HTAP 的性能，使数据可立即用于推理和分析。

### Chapter 4: 通过机器学习优化工程梦想引擎

“梦想引擎” 项目通过使用机器学习模型来优化性能，代表了数据库工程的根本转变。该团队并未仅依赖学术论文，而是建立了一个工厂，分析数万亿个跟踪数据点，以确定特定工作负载最有效的算法和数据结构。这种方法使系统能够在运行时调度正确的实现，以高保真度处理吞吐量、延迟和数据分布之间的权衡。

### Chapter 5: 战略差异化与数据驱动 AI 的未来

Databricks 通过开放格式的基础和专注于数据驱动的 AI，而非专有模型，实现了自身差异化。该策略强调数据是最有价值的资产，随着 AI 代理变得越来越强大，关注点转向通过合成数据生成和专门子代理使模型定制更容易。通过保持开放生态系统并避免供应商锁定，该平台使企业能够构建能够与不断发展的 AI 和数据处理环境无缝集成的未来-proof 架构。

## Q&A

### Q1: 什么促成了 OmniAgent 的开发，你为什么决定将编码代理和自定义代理合并到一个平台中？
A1: 我们看到了几条交汇的线索，表明需要一种新方法。在内部，我们的开发者正在使用各种代理构建自己的工作流程，而我们也在推出数据科学代理如 Genie。我们意识到所有这些代理都面临着相同的基本问题：需要切换模型、需要共享会话以便协作，以及需要历史记录和搜索。人们最初觉得将编码代理和自定义代理结合在一起很奇怪，但基础挑战——交付代理、控制安全性以及确保可移植性——是相同的。我们构建 OmniAgent 来提供一个统一的层，处理这些共享需求，允许协作和安全、可移植的代理部署。

### Q2: 你对开源与保持专有服务之间的哲学是什么？
A2: 我们开源那些我们认为会产生网络效应的层，那些生态系统从合作中受益的层，以及我们没有时间自己构建每一个集成的层。Spark 就是一个很好的例子；通过简化连接器的添加，我们得益于社区的工作。然而，有些服务必须是专有的，因为它们需要运营团队来确保可靠性，例如维护流处理作业或确保数据库不会在夜间丢失数据。我们希望在用户在我们的平台上构建的内容上尽可能开放，同时将内部资源集中在需要持续管理的高可用性运营服务上。

### Q3: 你能解释一下 LTAP（湖仓交易/分析处理）的概念吗？它如何解决传统数据库架构的局限性？
A3: 传统数据库工程长期以来分为两个部分：OLTP（事务性）和 OLAP（分析性）。通常，你会先使用像 Postgres 这样的 OLTP 数据库，但随着扩展和需要进行复杂分析，你必须将数据复制到使用 CDC（变更数据捕获）管道的分析系统中。这些管道往往脆弱、复杂，并且在模式变化时容易失败。LTAP 是我们对这个 “圣杯” 问题的解决方案。我们不再试图构建一个能做所有事情的单一引擎，而是统一存储层。通过将数据以列式格式直接写入数据湖，分析层可以立即读取数据，而不需要任何管道延迟。它让你享受两者的好处，而无须维护复杂的同步开销。

### Q4: 在构建代理时，你如何平衡安全性和可用性之间的紧张关系？
A4: 许多当前的编码代理使用基本的二进制策略——允许或不允许某个工具——这在过于限制和不安全之间创造了艰难的权衡。我们提倡 “上下文” 或 “有状态” 的政策。我们不是问代理是否被允许推送到网站，而是跟踪会话的状态。例如，如果代理执行了风险较高的操作，比如安装未验证的包或读取大量机密文档，政策可以自动阻止进一步的敏感操作。通过将低级 API 事件映射到高级功能事件，我们可以制定更安全和更有用的政策，允许代理在遇到特定的定义边界之前自主操作。

### Q5: 随着公司规模扩大，你如何保持创新和快速执行的文化？
A5: 我们专注于招聘优秀人才，并授权他们在不需要正式许可或无休止设计文档的情况下采取行动。我们鼓励渐进的方法——在几周内构建一个原型，并直接与目标客户合作以查看其效果。例如，LTAP 引擎的诞生是因为一位工程师简单地原型一个列式写入器，因为我们在存储团队中有闲置的 CPU 能力，而不是等待委员会批准一份正式的设计文档。我们还保持产品组合的一致性；我们不会推出数十个不同的服务。我们一次增加一个功能——存储，然后是 SQL，然后是机器学习——并确保每个功能都做得很好。这让组织保持可管理和专注。

### Q6: Databricks 的模型战略是什么？你为什么选择关注代理而不是仅仅关注前沿模型？
A6: 我们相信在领域特定代理中存在巨大的机会，这些代理在查询数据方面非常有效。我们专注于构建利用外部前沿模型和经过微调的自定义组件的系统。我们确实会训练模型，尤其是在高容量用例中，专用模型的表现要远好于一般模型，比如文档解析。我们发现模型自定义变得越来越容易，因为基础模型在生成自己的训练数据和跟踪方面变得更智能。我们的目标是让任何人都能够轻松地输入数据并描述任务，这就是我们专注于 “工具” 和互操作性层的原因，允许具有专用模型的子代理无缝协作。

### Q7: 在竞争方面，你认为是什么核心洞察使 Databricks 在云数据领域超越其他公司？
A7: 最大的根本区别是我们从开放生态系统开始。我们从未有过专有格式；我们基于 Parquet 构建并演变为 Delta 和 Iceberg。这在早期是有争议的，但它赢了，因为企业希望有一个不被锁定在单一供应商中的基础。此外，我们通过优先关注大规模数据处理和摄取，在许多竞争对手 “上游” 开始。这更容易将一个广泛的、开放的大规模平台优化以满足速度和商业用户需求，而不是将一个专用的、快速的专有系统改造成开放和可扩展的大量处理。当你把数据放在正确的地方，人工智能的魔力就容易得多实施。

## Highlights

1. [30:37] CDC 是推动现代社会的最基本操作之一。它脆弱到我们开玩笑说它应该被称为持续数据损坏。
2. [44:45] 几乎没有系统有勇气在经历了十年的工作负载后，了解到我们今天所知道的一切，重新从头开始编写它。

## Keywords

1. **Databricks**: 一家提供数据分析、机器学习和人工智能开发统一平台的数据和人工智能公司。它因其 Lakehouse 架构而广受认可，该架构将数据仓库的性能与数据湖的灵活性相结合。
2. **Spark**: 一个快速的统一分析引擎，旨在大规模数据处理。它允许用户在分布式集群上运行复杂的计算任务，并作为许多现代数据工作负载的基础技术。
3. **Omnigent**: 一个开源平台，用于构建、托管和管理人工智能代理。它为代理会话提供了标准化接口，使开发者能够协作、共享历史记录并在不同的代理框架中实施安全策略。
4. **LTAP（Lakehouse 事务/分析处理）**: 一个概念，旨在统一事务和分析数据处理于单一存储层。它旨在使数据即时可用于推理和分析，而无需在不同系统之间建立脆弱复杂的管道。
5. **CDC（变更数据捕获）**: 一个监控和识别数据库变化的过程，例如更新、插入或删除。虽然它是复制数据的行业标准实践，但当数据库模式发生变化时，通常被描述为复杂且容易失败。
6. **二号系统综合症**: 一个软件工程中的概念，描述团队第二个项目因过度雄心和希望包含在第一个系统中遗漏的每个功能而失败的倾向。它作为对设计新大规模系统的架构师的警示原则。
7. **Delta Lake**: 一个开源存储层，为数据湖带来了可靠性、性能和事务一致性。它允许组织管理大量数据，同时确保信息保持准确和可访问。
8. **Parquet**: 一种高度优化的列式存储文件格式，适用于分析工作负载。它允许高效的数据检索和压缩，使其成为现代数据平台中存储大型数据集的标准选择。
9. **Genie**: 一个由 Databricks 研究团队开发的专门数据科学代理。它作为一个虚拟助理，理解公司的特定数据、库和工具，帮助用户通过自然语言执行复杂分析。
10. **HTAP（混合事务/分析处理）**: 一个数据库工程中的架构目标，旨在单一引擎上运行事务和分析工作负载。虽然通常被视为数据库设计的 “圣杯”，但它通常需要在性能和复杂性上做出显著权衡。

## Transcript

[00:03] **swyx**
Matei 和 Reynold 来自 Databricks。 欢迎来到潜在空间。

[00:06] **Reynold Xin**
谢谢你们邀请我们。

[00:07] **Matei Zaharia**
是的，非常感谢。

[00:08] **swyx**
感谢你们抽出时间。 你们正在举行 Databricks 数据 AI 峰会。 你刚刚告诉我你们举办的第一次峰会只有 50 人。

[00:16] **Reynold Xin**
是的，那应该是在伯克利的小型聚会。

[00:19] **Matei Zaharia**
是的，我们会做这些教程，只教人们 Spark。

[00:23] **swyx**
是的。 很明显，现在全球的参与人数大约有 10 万，其中有 3 万人亲自到场。 这是个疯狂的社区。 嗯，我刚刚看了主题演讲。 Ali，你知道吗，当时就很明显 Ali 会成为一个如此出色的首席执行官吗？ 你觉得呢？

[00:44] **Matei Zaharia**
我觉得在我们的创始团队中，显然他是最适合这个职位的。 而且，是的，结果非常好。 而且，我的意思是，他在许多主题上都有了很高的水平进入公司。 他会进入并研究这些事情，和所有专家交谈，即使他不能雇佣这个人，你知道， 也会对金融、销售和其他各种事情有所了解。 然后，知道从那里出发。

[01:09] **swyx**
是的。

[01:09] **Reynold Xin**
我的意思是，他显然智商和情商都很高，但 Ali 今天与十年前的 Ali 是很不同的。 我觉得他为达到这一点付出了很多努力。

[01:21] **swyx**
我是说，对我来说，最吸引他的地方在于他的幽默。 而且你知道，很难在数据安全等问题上开玩笑。

[01:33] **Matei Zaharia**
哦，是的，确实如此。

[01:34] **Reynold Xin**
是的。

[01:35] **swyx**
所以你们推出了一大堆新东西。 我会简要提及一些内容，因为我们不会覆盖所有内容。 Omnigence，你们的宝贝。 LTAP，你们的宝贝，你们的梦想引擎。 我们还将讨论 Genie，讨论 Customer Lake，你们收购的 Panther，OpenSharing，以及 Unity，AI Gateway。 我觉得这些大多是你期望 Databricks 会做的事情。 这就是路线图的一部分。 你们类别中的每一个人都有类似的产品。 但我认为你们两人可能在这个领域推进了两个最独特和不同的举措。 也许我们先从 Omnigent 开始，然后再深入讨论。 我确实认为很多人都在探索这种元装置的概念。 是什么促使你们走向这个方向的？

[02:22] **Matei Zaharia**
是的，其实有几个趋势在汇聚，我认为这是一个好迹象，表明你们需要一些新的东西。 所以，一方面，所有内部的编码代理信息。 我们有一个非常棒的开发信息团队。 他们建立了一个叫 iZerk 的东西，基本上是一个云代码和编解码器的包装器，允许你在网页的沙盒中或者在你的开发机器上或笔记本电脑上使用它们。 然后，他们也在增加各种内容。 我们看到那些更高级的工程师在用大量代理构建自己的工作流，他们在其上建造自己的 UI 等等。 另一个方面是我们在构建代理。 我们在我共同领导的研究团队中发布了这个叫 Genie 的数据科学代理。 基本上，我们也为各种事情构建了许多内部代理。 然后，我们也有所有的客户代理，他们都遇到了这样的情况：哦，我需要切换。

[03:22] **Matei Zaharia**
模型和装置等等，每隔几个月就要这样。 此外，如果你无法与他人共享会话，没有历史记录和搜索，这个代理完全没用。 所以在协作中必须有很多这种东西的层次在上面。 我从这两个上下文中都思考过这个问题。 起初人们觉得很奇怪。 他们会说，为什么你要在同一个东西中做编码代理和自定义代理？ 但我说，这基本上是同样的问题。 你只想构建这些东西，让你能够交付代理，可能在你关心安全时控制它，并使其可移植。 然后我们原型了一些实验。 我们看到了，是的，实际上可以使其投入运行。 然后我们，你知道，我们真正构建了这个。

[04:06] **swyx**
我想知道这种架构是否与你们过去的职业生涯有任何对应。 我总是想很多事情实际上都是与操作系统联系在一起的。 很多操作系统与数据库之间，或者相反，都是相互联系的。

[04:22] **Matei Zaharia**
我认为它与网络协议有很大关联，你知道，互联网协议。

[04:29] **swyx**
实体之间的沟通。

[04:30] **Matei Zaharia**
是的。 我们也做了数据共享的工作，这可能，知道的观众不会太多，除非他们是......

[04:36] **swyx**
公开协议就是这个术语。

[04:38] **Matei Zaharia**
是的。

[04:38] **swyx**
公开共享。

[04:38] **Matei Zaharia**
公开共享。 是的。 所以你有一家企业，维护某种表格，比如说沃尔玛之类的，他们有，知道， 每家商店的库存和销售情况。 然后你也有供应商，他们希望能在你需要的那一刻生产更多东西并发货。 所以他们希望能实时访问你的表格。 因此，为什么不能实时与他们共享这个表格的视图，而不是发送电子邮件、Excel 表格或打电话呢， 然后他们查询它，他们将与他们的数据连接并决定发送什么。 所以这是你可能会问的一个问题，今天，由于我们能够如此迅速地编写代码，为什么我们还需要设计， 像协议、API 或软件呢，对吧？ 难道你不能根据需要动态编写代码吗？ 但实际上，对于这种互操作性，多个速度不同的参与者构建东西，而你仍希望在上面有某种层次来协调， 你确实希望设计并构建它。

[05:35] **Matei Zaharia**
所以这让我想起了代理相互交流的样子，以及用户与代理和工具之间的交流。

[05:42] **swyx**
Reynold，还有其他意见或不同的观点吗？

[05:46] **Reynold Xin**
我认为，但我们就具体哪些利益重要进行了辩论。 我认为在我们决定做这件事的时候，我告诉 Matei，嘿， 恰好有一周我一直从醒来的那一刻编码到睡觉的那一刻。 我记得我在查看我的课程、我的编解码课程，其中一个特别烦人的事情是必须保持我的笔记本电脑开着。 我那时候正开车去看医生，我记得我想确保整个过程可以继续进行。

[06:18] **swyx**
顺便提一下，听你这么说让我感到非常安心，因为我不知道我是不是个小丑在做这个，或者...

[06:25] **Reynold Xin**
是的，老实说，我在开车，把我的笔记本电脑连接到我的手机，放在旁边。 每当我遇到红灯时，我就开始看看我的笔记本电脑上发生了什么。 我觉得这真是太荒谬了。 感觉就像我们回到了编程的黑暗时代。 我的意思是，你从这个编码时代获得的生产力是惊人的。

[06:44] **swyx**
你听说过云吗？

[06:46] **Reynold Xin**
对我来说，这简直是疯狂。

[06:49] **Matei Zaharia**
你在做的那个事情是沙盒，还是在此之前？

[06:52] **Reynold Xin**
是的，确实是一个沙盒。 所以我从一个非常不同的角度来接近这个问题。 我想说，嘿，我们将拥有不会关闭的云沙盒。 你可以很快获得一个，但不仅仅是为了运行代理会话。 实际上也是为了进行开发。 所以我实际上是在那一周亲自构建它，通过构建，我遇到了所有这些问题，然后我实际上为我的案例写了一份文档。 这是我对实际环境应该做的愿望清单。 他实际上最终几乎实现了每一个愿望。

[07:23] **Matei Zaharia**
是的，我记得 Reynold Xin，因为我的第一个原型只是与你的代理聊天，他说我必须能够打开一个 shell， 就像我自己的 shell，列出文件并查看文件尾部等。

[07:36] **swyx**
基本上，它是代理到主机。

[07:37] **Matei Zaharia**
是的，现在实际有这个功能。 记录我的日志。 是的。

[07:41] **Reynold Xin**
另一个我认为我问过的事情是，我仍然使用光标来专门渲染 markdown 文件。

[07:48] **swyx**
嗯。 是的。

[07:49] **Reynold Xin**
所以我说，给我一种方式查看我的 Markdown 文件并正确渲染它们。 我不再需要一个单独的工具了。

[07:55] **Matei Zaharia**
是的。

[07:56] **Reynold Xin**
我认为你也把这个功能内置了。

[07:57] **Matei Zaharia**
是的，我们做到了。 是的。 是的，我们有很多工程师在建立他们自己的编码设置。 但他们都有一个共同的声音，说我构建了对我来说很棒的东西，但团队中的其他人无法使用，因为我没有服务器来协作。 这就是我们试图建立 Omnigent 的原因，这样你就可以拥有一个服务器，并在那里设置安全性。 所以，你知道的，像用谷歌登录或其他方式，并且实际安全地确保事物。 这就是我们看到许多其他代理遇到问题的地方。 人们认为他们原型了一个很棒的代理，但由于安全团队的原因，无法连接到一些非常重要的数据。

[08:38] **swyx**
在这一点上，对于在 YouTube 上观看的人，我们将展示结构的图像，我们可以稍微讨论一下架构。 我只想让大家理解，因为我们在谈论软件时，它可能非常抽象。 而且，这实际上就是我们所谈论的。 你已经在开源中构建了整个平台。 有运行组件和服务器组件，以及你已经找出来的统一 API。 还有其它元素吗？ 显然，你可以插入所有这种持久性层和计算层。 这是一个完整的云。 这是一个代理云。

[09:12] **Matei Zaharia**
是的，意思是，它有这些组件来与之协作。 你知道，大多数操作都发生在你部署代理的机器上。 所以在那里你拥有的任何东西，都可以使用。 但是是的，我认为这是你希望拥有的最小的托管服务，像协作代理，并且有那个服务器。 我们开源的原因之一是，任何构建代理的人都可以用这个应用程序作为起点来定制， 我们在 Databricks 也看到了这一点，像有人会制作一个不错的代理应用程序，然后其他团队会问，哦， 我可以用你的应用程序来做我的代理吗？

[09:45] **Reynold Xin**
是的，我认为我们每个团队都建立了大约五六种不同的代理框架。 它们基本上都做差不多的事情。

[09:51] **swyx**
是的，你基本上需要人们想要在 4Kit 中使用的东西，反正你可以有开源的东西。 是的，这也是另一个问题，这对 Databricks 来说很有意思，你们选择开源什么？ 你们选择把它做成什么？ 我的意思是，这又回到了 Spark，对吧？

[10:05] **Matei Zaharia**
对。 所以，我的意思是，开源某个东西的原因之一是如果你认为这是一个可以实际产生网络效应的层。 它会受益于许多人在上面协作。 比如说，关于 Spark，我不知道你是否知道，当 Spark 出现时，我们也非常专注于让你有可以在其上构建的库。 所以，比如说，它们过去是不同的。 我们为机器学习和图计算分布式计算引擎。 我们说它们都应该是可以组合的库。 我们还让添加与数据源的连接器变得超级简单。 然后我们受益于此，因为你知道，我们没有时间去编写像，类似于一千种不同数据库和文件格式的连接器， 但我们可以使用人们制作的连接器。 当然他们也从加入这样的事情中受益。 所以这就是原因之一。 另一种思考方式是，想象一下，我们的东西不是开放的。 我们有某种代理托管的东西，但它不是开放的。 然后有一个是开放的。

[11:05] **Matei Zaharia**
从长远来看，哪一个会获胜？ 在这里，因为人们撰写集成带来的好处，所以会是这样。 还有其他一些事情，你根本无法开源，因为那是公司做的事情。 例如，如何确保你的流式作业或你的 Lakebase 数据库不会在夜间丢失所有数据。 好吧，那需要一个运营团队来坐在那里。 这是不可能的。 它必须是一个服务。 所以我们想确保作为一家公司，我们在前端服务方面做得非常好，同时在你构建的部分尽可能开放。

[11:42] **Reynold Xin**
我是说，从收益的角度来看，我认为我们已经看到各种生态系统集成的拉取请求，尽管它仅在星期六发布。

[11:50] **Matei Zaharia**
是的，星期六。 是的。

[11:51] **swyx**
所以有人关注发生了什么。 是的。

[11:53] **Matei Zaharia**
是的，你可以查看合并的记录。 我今天早上实际上问了 Omnigent 关于 400 次合并的事情。 是的，我认为大约一半的合并不是来自我们团队。 但例如，有人添加了在 Kubernetes 上运行的支持。 人们添加了许多云沙箱。 所以这可以启动一个云沙箱，并在其中运行你的代理，这对共享也很不错，因为它不是在你的笔记本电脑上，有人正在运行令人害怕的代码。 因此，是的，很多初创公司已经将这些整合进来了，我们期待看到更多。 我们已经有更多的代理工具。 Courser、CLI 和 antigravity 也有。

[12:34] **Reynold Xin**
是的。

[12:34] **swyx**
这一切都很美好。 我感觉上一次发生这种事时，现代数据栈兴起了。 我不知道这是否有那么有用。 我实际上很好奇。 你的事后分析。 我认为大多数人会同意它终于死了。 但也许这会产生一种新的现代 AI 栈，做同样的事情。 我不知道。

[12:53] **Reynold Xin**
我的意思是，我认为现代数据栈是一个相当有用的东西，甚至可能一直到今天。 我认为，也许对于那些实际上不理解历史的观众来说，现代数据栈有效地被分解为需要一个层来摄取数据， 需要一个层来转换数据，然后需要一个层来可视化数据。 所有这些都运行在某种数据仓库上，或者在我们进行数据仓库时，也可以是湖仓。 我认为这些概念都非常强大且非常有用。 它使许多工作负载得以实现。 人们最终遇到的问题是统一和整合的问题，嘿， 你真的需要把这一切拆分成不同的部分，并与这么多不同的供应商和平台合作，以便完成一个非常简单的可视化吗？

[13:40] **swyx**
对。

[13:41] **Reynold Xin**
所以我认为随着时间的推移，每个人开始意识到客户正在推动我们。 我们开始意识到这一点。 所以我们开始构建越来越多的功能，并尝试进行整合。 到最后，现在客户不必担心需要连接五个不同的系统来生成图表。 但我认为老实说，这样的事情可能发生在你要连接多少不同框架以生成， 做一个非常简单的代理？

[14:06] **Matei Zaharia**
为了明确，我会说核心是所有这些载体之上的共同 API。 所以这个 API 基本上就像你有一个代理会话，你可以发送一条消息或者一个文件，基本上就是你可以发送的内容。 然后你会得到，你知道的，这些流，就像是流式文本或进行工具调用时那样。 你可以发送的另一件事是，你可以告诉它取消或转变。 所以这就是 API。 现在，我们所做的事情是，我们可以在 Claude 代码运行的终端编解码器之上为你提供这个， 你知道的，pi。 Open AI SDK，所有这些东西，我们将它们都映射到同一接口。 如果你自己构建一个代理协调器，那么这是你必须自己维护的东西。 然后每当 Claude 更改其 API 时，你就得调整你的东西，否则会丢失一些消息。 所以维护这个是有价值的。 然后在此基础上，我们构建了一些应用程序。

[15:00] **Matei Zaharia**
我认为我们构建了一个相当酷的用户界面等，但这就是我们构建安全和控制部分的原因， 这让我非常兴奋。 这是一个共同的接口，并且并不试图成为一个堆栈。 事实上，你可以在这个服务器之上插入自己的用户界面。 这是我们非常关注的用例之一，因为我们想在自己的产品中使用这个。

[15:20] **swyx**
是的，它应该无处不在。

[15:22] **Matei Zaharia**
是的。

[15:22] **swyx**
我认为其中一个对我来说非常有趣的事情是，首先， 我会努力做到这一切，不用称它为现代 AI 堆栈，因为第一个告诉我关于计算沙箱的人是 NEON 的 Nikita。 很多人把 NEON 想成是无服务器的 Postgres，有计算与存储的分离。 你知道的，即时分支和所有这些事情，但实际上每个数据库公司也是一家计算公司。

[15:51] **Matei Zaharia**
对。

[15:52] **swyx**
所以他实际上给我展示了他的整个沙箱解决方案。 我认为他从来没有发布过它。

[15:57] **Reynold Xin**
所以我们沙箱解决方案能够如此快速构建的原因是，我们意识到如果你只是将实际的湖基础架构取出数据库， 顺便说一下，它是来自 Xeon。 现在有一些区别，例如，支持这个特定工作流程很重要，因为你希望你的状态保持持久。 你的库，你不必每次都安装你的库。 而 Neo 架构由于计算与存储的分离，你不需要持久的本地磁盘。 所以有一些区别，但到头来，是的，...

[16:35] **Matei Zaharia**
是的。 所以这是当你运行像编码沙箱一样的东西，如果我用的话，我们在 Databricks 内部有 DevInfo。 就有很多很多，像几十个千兆字节的数据仅仅用于我构建的所有源代码和工件。 我希望下次能回来。 所以，但是是的。

[16:52] **swyx**
在节目之前，我们谈到了可能令人惊讶的某些统计数字，关于它的采用。 它可以是内部的，也可以是外部的，无论什么让人印象深刻，这规模正在发生。

[17:02] **Reynold Xin**
所以在分析方面，我认为我们推出了，我们可能每天在三云平台上有 5000 万到 6000 万个虚拟机。 所以我们是最大的计算协调器之一。

[17:13] **swyx**
这点毫无疑问是用于 CPU 计算。

[17:15] **Reynold Xin**
而所有这些过程，我认为是以字节为单位的数据。 我开玩笑说，看你在哪个时区，通常在你吃早餐之前，Databricks 那天就会处理以字节为单位的数据。 在 NEON 上，这也真的很有趣。 它现在每天推出大约 1300 万个数据库。

[17:35] **swyx**
是的。 对我而言，那是个大，是什么意思？

[17:39] **Reynold Xin**
而且许多得益于代理和分支实验，因为我们让这变得如此简单且快速。 非常感谢 Nikita 的团队推出数据库。 所以这改变了人们使用数据库的方式。

[17:54] **swyx**
是的。 好的。 我们刚才要讨论更多关于数据库的话题，但是我想确保在 Omnigent 方面总结一下。 你提到你对安全和控制方面感到兴奋。 许多公司现在也在解决这个问题，以及支出方面。 你发现了什么？

[18:10] **Matei Zaharia**
是的。 所以我花了相当多的时间与内部用户、开发者、安全团队、你知道的，经理，以及许多客户进行交谈。 有几点首先变得非常明显的是，对于安全性， 在可用性和安全性之间存在张力。 许多编码代理今天只有非常基本的功能，比如，你可以告诉我我允许或不允许的工具模式或者其他。 就是是或否。 但这让你处于一个非常困难的境地。 举个例子，我的代理是否应该能够读取一些机密文档，或者说它是否应该能够从 NPM 安装新包， 你知道的，也许它是被攻击的。 是还是不是，也许我想允许它。 我的代理是否应该能够将内容发布到公司网站？ 好吧，如果我在网站上使用代码，那是肯定的。

[19:08] **Matei Zaharia**
但是它应该能够同时做这两件事，这样它就可以抓取机密文件并被快速注入然后泄露吗？ 大概不行。 所以我们决定需要的是有状态的或者我们称之为上下文策略，能够跟踪会话的状态。 这并不是说，是否允许推送到营销网站。 但是，如果它做了一些风险较高的事情，比如安装了你知道的一个一天前的 NPM 包，或者它读取了大约一千个机密文件， 那么不，不要这么做。 否则，也许可以。 这就是移动权衡的一个例子。 所以，通过拥有一个更强大的引擎，实际上，它既更安全又更有用，这就需要跟踪会话。 另外一个有趣的点是，它正在处理一些非常低级别的事件，你希望顶部有一些库来解析它们。 比如，我们在 Google Drive 内部有一个 MCP 服务器。 它有 60 个 API 调用。 我怎么知道其中哪些会与互联网共享文档，哪些不会？

[20:09] **Matei Zaharia**
这很烦人。 所以我们在 Omnigent 中设计了政策层，以便它能正常工作，并且你可以有库，像有人可以制作将低级事件映射到高级事件的东西， 然后你写一个关于所产生的高级事物的政策。

[20:25] **swyx**
这与 Panther 有关。

[20:27] **Matei Zaharia**
是的，Panther 会对此有所帮助。 Panther 是类似于事件处理的想法，并且是基于 Python 的，而不是某种奇怪的自定义语言。 这在某种程度上更接近实时。 但这些都是很酷的事情。 我认为上下文或有状态部分，然后它可以是库的方式。 这也是使其开源的另一个原因，因为其他人会编写库，而我们和我们的客户可以使用它们。 最后一点，因为它是有状态的，我们跟踪的状态之一是你在该会话中花费了多少。 所以我有过这样的经历，我让一个代理调试某些东西，它花了 500 美元。 这是因为它决定读取很多日志文件并消耗大量令牌。 但我可以明确地说，好吧，启动一个子代理来做这个，并将花费限制在 5 美元。 如果需要更多，请问我是否同意。 并且因为我们在该会话中计算它，它会弹出并告诉我，好的，你花了 5 美元。你想继续吗？

[21:27] **Reynold Xin**
所以这里有一个重要的背景。 Matei 在过去五年中，花了很多时间在 Databricks 架构 UND 目录，这是数据治理层。

[21:35] **Matei Zaharia**
没错。 是的。

[21:35] **Reynold Xin**
他将该层的专业知识与所有的 AI 治理结合在一起。

[21:40] **swyx**
是的。

[21:41] **Matei Zaharia**
是的。 但是我也花了很多时间被编码代理和获取提示弄得烦恼。 作为 CTO，我不想出现在头条上，因为我安装了某个奇怪的 NPM 包并泄露了信息。 我尤其容易出错，但我时间有限，所以我不想花时间去批准， 你想运行一个 20 行的 bash 脚本吗？ 是还是不是？ 所以这就是我花很多时间去思考如何尽可能安全又不烦人的原因。

[22:10] **swyx**
是的。 安全性和我们称之为的安全问题，是比令牌最大化或令牌预算更大的关注吗？ 你知道，哪一个更重要？

[22:19] **Matei Zaharia**
哦，是的，它们都是存在的。 我的意思是，我不知道。 我想这取决于你是什么样的公司。 所以我认为有些公司预算有限，他们真的很关心这个。

[22:34] **swyx**
我的意思是，你可以是 Uber，仍然会在意，对吗？

[22:36] **Matei Zaharia**
是的。 哦，完全是。 是的，是的，是的。

[22:38] **Reynold Xin**
我的意思是，对我们来说，安全性。

[22:40] **Matei Zaharia**
对我们来说，安全性作为云服务提供商绝对是关键。 这是最重要的事情。 至于令牌最大化，我们现在并不太担心，但我见过。 例如，我和一些咨询公司交谈过。 他们有 100,000 名员工，都在为客户编码。 如果他们每人多花 1,000 美元，那就不好玩了。 我们只有几千名工程师。

[23:06] **swyx**
Databricks 的政策是什么？ 是不是就没有限制？

[23:08] **Matei Zaharia**
是不限制的，但我们使用自己的产品来分析跟踪信息，我们还有一个团队，你知道，专门来优化，看看是否有人在做一些奇怪的事情。 而且我们实际上通过分析当前的跟踪器得到了非常有趣的见解，比如哪些模型在 Rust 和 TypeScript 等方面表现更好。 所以，是的，至少在我们的代码库中。

[23:31] **swyx**
是的，太神奇了。 显然，我必须问关于令牌混合的问题。 我认为这是一个关键问题。 但是是的，安全性和控制这在上面，找到一个理智的层次，让你有一些自主权，但又不太多。

[23:43] **Matei Zaharia**
是的。 我们希望作为工程师，使其超级简便。 你应该设置它。 因此在 Omnigent 中，你可以要求你的代理，为自己设置一个政策去做这个。

[23:51] **swyx**
如果我该展示什么，我在 GitHub 上没有看到，但在文档中，你可以稍后查看。

[23:59] **Matei Zaharia**
如果你想查看上下文策略的文档，我们来看看。

[24:04] **swyx**
我只是喜欢指引人们。

[24:05] **Matei Zaharia**
查看内置的政策。

[24:06] **swyx**
如果你想继续，这是确切的查看位置。 对吧。

[24:10] **Matei Zaharia**
是的，是的。 这些的故事就像我写的，你知道，我写了一个文档，里面有 10 个点子，是在你们在工作之前的想法。 嗯，那就像是我的愿望清单，大家都问过的事情。 我告诉团队，嘿，你们能在发布时做到至少五个吗？ 然后他们就把所有的都弄回来了。 所以你可以想出更多，但有些只是作为例子。 真的，你可以拦截代理产生的任何事件，然后你可以选择阻止或强制它询问用户或允许， 并且你可以更新状态来跟踪信息。

[24:46] **swyx**
是的，因为归根结底，我把你看作是一名系统设计师。 你让人们接入，对吧？ 这就是你所做事情的全部操作方式。

[24:54] **Matei Zaharia**
是的，是的。 我们也非常关心可组合性。 比如是否可以让其他人编写一个库，供其他人使用，这正是我们所希望的。

[25:00] **Reynold Xin**
这里还有一个 “自带电池” 的理念，可能和你做 Spark 的方式非常相似，你只需开始使用即可。

[25:06] **Matei Zaharia**
对，没错。 它必须在某些方面开箱即用，然后你可以在其基础上构建自己想做的事情。 但是在 Spark 中，如果你只想读取表格或进行聚合，它应该在开箱时就很出色。

[25:23] **swyx**
人们想了解 Omnigent。 他们应该观看你的主题演讲。 他们应该浏览 GitHub 和文档。 如果他们想贡献或者想在这个生态系统上构建，你会指出哪些是最有杠杆效应的参与地方？

[25:36] **Matei Zaharia**
是的，确实要参与到 Discord 和 GitHub 中。 我们团队会在那儿监控。 一些人询问的事情，我们自己刚刚构建出来。 有些事情，你知道，我们正与他们合作来构建。 还要告诉我们你希望如何做，我认为特别是对于开发者，每个人都希望以自己的方式运行，而优秀的开发者， 你必须听取所有方式的反馈，找出抽象层，并让人们自定义。 所以如果你认为，我不想这样工作，告诉我们。 我们真正想要的是在代理之间建立兼容层，然后让你在其上做事情。

[26:14] **swyx**
嗯，关于创业方面，有没有，呃，你知道的，作为一名创始人，我， 我想要，我看到了一个机会，我想在你面前展示。 对于像这样的创业公司，你有什么请求，像是，你知道的，我希望有人在做这个。

[26:26] **Matei Zaharia**
哦，对于创业公司。

[26:27] **swyx**
是的。 像，你知道，你有自己的创业公司。 它发展得很好，但是你知道，如果你不在做自己的创业公司，您认为显而易见的是什么呢？ 你显然也为许多创业公司提供建议。

[26:37] **Matei Zaharia**
我的意思是，作为一家拥有大量工程师的公司，我确实认为任何帮助我理解人们如何使用编码代理的东西都很重要， 但也包括质量，或者说你应该添加这种技能，或者你应该写这个功能，或者你的代理在涉及这个服务的任务上表现得真的很糟糕。 所以我去花时间。 那会很好。

[27:00] **swyx**
是的，我发现的最接近的是这个团队，Git AI。 他们一开始是说，我们只做代码和人工归因，但他们基本上是在此基础上构建分析层。 我确实认为像有很多人工智能分析的东西显然做得很好。 所以会有一些人，我认为这就像我们将先讨论顾问领域，但实际上是构建软件的人。 假设我们有针对编码代理的管理层。

[27:31] **Matei Zaharia**
是的，我认为那里会有很多见解。 你在其他领域也能看到。

[27:34] **swyx**
好的。 然后另一个重要的事情是你的梦想引擎。 也许你想讲一下 LTAP 的故事。 我将让大家听我们的 Ankur Goyal 节目，讨论单一存储、HTAP 和所有相关历史。

[27:53] **Reynold Xin**
LTAP 的想法其实很简单。 如果人们听过 Ankur 讲关于 HTAP 的话，这是关于数据库的世界。 抱歉，这里可能需要很多背景信息。

[28:05] **swyx**
我很高兴成为那个强迫人们学习数据库的数据库播客。 你不能只用 markdown 文件来写代码。

[28:14] **Reynold Xin**
这是最重要的基础系统技术之一。 但是数据库的世界实际上大致分为两个部分。 我们称之为 OLTP 的数据库，是事务性的。 你可以想象你的 Postgres、MySQL 和 Oracle 数据库。 另一方面是我们称之为分析的部分。 有时候你可能听过 OLAP 这个术语。 它们的区别在于 OLTP 通常是在某个事件上运行某些事务，这会查看一个特定的角色。 我们更新那个角色，对吧？ 它是非常以角色为导向的。 在分析中，你是试图对数据进行推理。 你试图计算，比如说，我每个商店的收入是多少？ 我的网站每天的表现如何？ 然后你最终可能想在上面运行机器学习来预测，比如说，我的销售在未来可能会怎么样？ 它们是截然不同的架构，每个人都从 OLTP 数据库开始。 每个应用程序，只要你变得足够认真，就需要比 markdown 文件更多的东西。 你需要有一个数据库。 你想要提升你的数据。

[29:14] **Reynold Xin**
你想要有一些事务一致性。 但是一旦你想要对数据进行推理，如果你只有大约一百行数据， 在你的 Postgres 或 MySQL 数据库上运行可能没问题。 但一旦你有更多数据并且想要进行更复杂的分析，这种分析可能会出现。我们在这里帮助你解决 Postgres 数据库的问题。 所以你开始从数据库中获取数据。 将它们复制到分析系统中。

[29:40] **swyx**
对于大家来说，Elasticsearch 就像一个大型的...

[29:42] **Reynold Xin**
是的。 所以实际上有一些客户会使用 Elasticsearch 进行块分析。 很多我们的客户显然会使用 Databricks 来运行更复杂的事情。 还有一个术语叫做 CDC。 它的作用是读取数据库的 binlog。 如果你不理解 binlog 是什么，没关系。 但它是数据的小增量，它基于增量重构数据库在分析端的状态。 但 CDC 是一件非常痛苦的事情。 这是行业中的基本标准，所有人都在使用它。 但最后被服务。 我认为很多数据工程师最终在凌晨 3 点被叫醒，因为有某些管道问题。

[30:22] **swyx**
你知道，我的解释就像是每个人都只通过 CDC 成为了一家 50 亿美元的公司。

[30:27] **Reynold Xin**
是的，没错。 CDC 是一件非常无聊但是又是最基础的操作之一，推动了现代社会的发展。 但它是如此脆弱，以至于我们开玩笑说它应该叫做持续数据损坏，因为你可能会在 LTP 数据库上更改 schema，然后 CDC 管道无法处理 schema 变化，结果一切都崩溃了。

[30:50] **swyx**
我的意思是，你可以做各种各样的技巧，比如说你加入一些版本控制或者其他的。

[30:54] **Reynold Xin**
是的。 但总体来说，这是非常复杂的。 我认为在我的主题演讲中，我问观众，如果他们喜欢自己的 CDC 管道，请举手。 只有大约两个人举手。 所以如果单一存储，大约十年前，我认为行业有这个想法，嘿，如果我构建一个可以同时处理这两种工作负载的单一数据库呢？

[31:12] **swyx**
顺便说一下，每个数据库的人都一直梦想这个。

[31:16] **Reynold Xin**
这是数据库工程的圣杯。 为什么不构建一个可以同时处理这两种工作负载的单一系统呢？ 但最终只是造成了很多妥协。 我认为第一个问题是，嘿，他们说 Postgres 有一个庞大的生态系统，对吧？ 你想使用为 Postgres 构建的工具。 比如 Spark 有一个庞大的生态系统。 有很多库你想使用。 如果你现在创建一个新东西，你就没有生态系统。 你往往会创建一个新的、更小的专有 API，你两者都缺乏。 而且在性能方面要做到可比性也是非常困难的。 所以最后实际上两方面都不尽如人意。 我们的 LTAP 整体理念显然是在 HTAP 这个术语上的玩笑，我们认为这是正确实现的 HTAP。 HTAP 想要为两者构建一个单一引擎。 我们认为通过统一存储可以获得 99% 的需求。 只需拥有一个单一的存储层。

[32:13] **Reynold Xin**
一旦你有了单一存储层，如果你的 Postgres 数据库以列存储格式写入数据， 所有分析就可以直接读取这些数据，而没有任何延迟，对吧？ 中间没有管道。 所以所有数据将立即可用于推理分析。 我想我之前告诉一些客户，嘿，当我们谈论这对代理来说会非常有用时， 我实际上一开始自己并不相信，即使我们写了这个定位。 但就在昨晚我和一位澳大利亚客户共进晚餐，他们实际上告诉我，哦，嘿， 我们面临的一个大问题是，我们有来自服务的所有这些日志，我们发现 SLA 的下降。 想要进行调查。 但是这些代理根本无法理解实际数据库中的情况。 我们看到的只是数据库和服务的产品遥测数据。 如果他们能理解，举例来说，谁在下这些订单，那他们的能力就会提高十倍。 发生了什么？ 他们到底在做什么？

[33:11] **Reynold Xin**
所以现在我实际上还在消息中。 我认为这其实是，基本上提供了 HTAP 圣杯几乎所有的好处， 也就是说，让数据可以立即用于推理分析。

[33:26] **swyx**
是的，我认为，人类通常是聪明的，想要具备查询任何内容的能力和访问权限，即使在工作时，他们也需要历史和上下文等等， 还有在哪里会被联系？ 这是一种分析工作负载。

[33:42] **Matei Zaharia**
我记得当我们的数据库发生事故时，工程师说，我无法直接在上面运行一个巨大的查询来查看发生了什么，因为那样会导致数据库崩溃，甚至伤害它。 就是这种问题被解决了，因为你可以启动一整套独立的机器来进行分析。 你不会给主数据库带来压力，对吧？ 它仍在尝试提供服务。

[34:04] **swyx**
是的，因此这是一个梦想已经有一段时间了。 为了达到今天需要做些什么？ 我觉得你对这个有多次的不同版本发布，但并不像 LTAP 那样清晰。 我觉得 LTAP 就像是，我们搞定了，伙计们。

[34:21] **Reynold Xin**
我在 Meta 和某人谈话，他问我，嘿，这有什么猫腻？ 为什么现在可能？ 我认为现实是我们花了很多时间来实际处理 Lakebase 架构。 而且显然其中很多来自 NEON 团队，即存储和计算的分离。 结果发现我们只差那么一点点。 从这个到 LTAP 的想法，也就是说，我们在 NEON 架构和 Lakebase 架构中， 以行导向格式将数据写入开放的数据湖。 但在其中，我们以 Postgres 页面进行写入。 实际上，Aliyah 和我花了很多时间在争论，嘿，我们能否将其更改为写入列导向格式？ 我们一直在辩论。 某天，我们的一个工程师非常聪明，进来了。 他说，嘿，我刚刚做了原型，它可行。

[35:07] **swyx**
等等，原型什么？

[35:09] **Reynold Xin**
原型， instead of 在数据湖中以行导向格式存储数据，像 Postgres 页面那样，改为写入 Parquet。 他只是观察到，嘿，我们的存储群拥有很多额外的闲置 CPU。 我们可以利用这些 CPU 来完成行到列的转码，行适合 OLTP，而列适合分析。 所以让我们在那个时候进行转码。 事实上，一旦你转码数据，数据的压缩效果更好。 所以从这些服务写入，比如 S3 或其他数据对象存储，你可以实际上更快地写入，因为它们变得更小。 所以没有额外的开销。 性能没有妥协。

[35:53] **swyx**
一些 CPU 开销。

[35:54] **Reynold Xin**
是的，因为，但反正我们有多余的 CPU。

[35:56] **Matei Zaharia**
我们反正有那一批机器。

[35:57] **Reynold Xin**
所以争论结束了。 嗯，这是许多技术问题的经典案例，经过很多辩论，之后有人实际上去原型并且成功了。

[36:06] **swyx**
但像这样对公司战略和重要的事情，我希望有个启动会议， 比如设计文档，什么都没有。

[36:13] **Reynold Xin**
没有那样的事情。 我们在很多会议上争论，然后我们只是从第一原理辩论是否可能，然后有人做到了。

[36:22] **Matei Zaharia**
是啊，我的意思是，如果你能给自己预留出这样的人，那就太好了。 这在 Omnigent 也发生过一点。 我认为如果我有一份文档，比如说，我们可以一起做这些，每个人都会想，哦，那这个呢？ 这又如何？ 但是如果你试一试，它会有帮助。 然后如果你有真实的用户，他们进行测试并且仍然有效，或者在这种情况下，如果你有负载，你知道负载看起来如何。 你可以测试同样的模式。

[36:46] **swyx**
技术抛开不谈，这非常酷。 这就像是最重要的事情，创新的文化。 你无需征得我的许可。 你不需要进行一个正式的流程。 只要去做。

[36:59] **Reynold Xin**
嗯，尤其是在这些日子，我认为有了 AI，实际上变得更容易。

[37:02] **swyx**
我认为你非常正确。 我的意思是，我跟很多大型公司的 C 级进行过交流，我认为在规模化的情况下，事情会变得缓慢。 我相信你已经感受到了，但通过某种方式你会拥有这一核心免于此的人员。

[37:15] **Reynold Xin**
怎么做到的？ 我认为我们招募并与非常优秀的人合作，这是非常重要的一部分， 给予他们权利。 但同样花费大量时间，我们一起在前线的努力也很重要。

[37:28] **Matei Zaharia**
是的，我认为人们可以适应大型公司。 所以这很有帮助。 我们想确保他们知道他们可以尝试新事物，解决争论并有很多先前完成的实例，或者推出测试版或其他。 然后我认为作为一家公司，尽管规模太大，实际上不推出那么多产品。 我们尽量保持一致性。 这实际上就是公司的整体理论。 不希望拥有 20 个 Amazon 服务，你需要设置一个分析和机器学习堆栈。 你只需一个。 它们使用相同的 API，相同的语义和相同的数据副本。 所以这需要统一。 然后我们基本上一次添加一项内容。 我们添加了带有 Delta Lake 的存储。 我们过去并不做任何存储。 然后我们添加了 SQL。 我们添加了机器学习平台的内容。 但是，是的，不要做太多，但要做好这些事情。

[38:28] **Matei Zaharia**
这也有助于保持可管理性。

[38:33] **swyx**
是啊。

[38:33] **Reynold Xin**
我们鼓励的另一件事是，别总想着借助海洋做一切，让我们想想如何逐步实现？ 我们如何能非常快速地做到这一点？ 就像我们的许多产品，都是在几周内建立的。 然后我们会问，嘿，我通常对任何开发团队的第一个问题是目标客户是谁？ 你和他们的关系如何？ 你和他们是用名字称呼吗？ 你和他们发短信吗？ 我觉得要有这样一个紧密的循环。

[38:59] **swyx**
你能提到一个类似的发布吗？ 我只想给出一些例子。

[39:03] **Reynold Xin**
Omnigent 本身就是这样发生的。

[39:05] **swyx**
谁是客户？

[39:06] **Matei Zaharia**
实际上，Omnigent 更像是一个内部项目，因为我们会将其用于我们的开发。 基本上，整个 AI 团队都可以访问它，并在使用它。 我们确保它从一开始就能与我们的内部代码库正常工作，这是一份庞大的单体代码库。 我们给他们一些基础设施。 我们给了他们很多令牌容量。 所以是所有的开发人员。 我们还有其他人。 我不知道。

[39:32] **Reynold Xin**
我认为这是一个公开的故事，但我只是想问 Marketplace、OpenSharing，这些都有人提到过，我只是不记得具体是哪些。

[39:41] **Matei Zaharia**
好吧，在公司成立很早的时候，就有像 Delta Lake 这样的事务存储层。 当时我们最大的客户说，好的，我需要一些，我想要一些云端的东西，因为，你知道， 如果我们其余的网络受到损害，那这个东西必须是独立存储和查询事件，然后再和我们联系。 他说，好的，这是每秒的事件速率。 这是我想要的实时性。 你能做到吗？ 所以这远远超过了我们曾经处理过的任何工作负载。 我们的工程师 Michael Armbrust 在这方面工作，他努力确保它能实现。 一旦它为他们工作，你知道，它就为其他人工作了。 是的，这在公司成立初期，大约四年前。

[40:24] **Reynold Xin**
2018 年？是的，17 年，18 年。你还有其他例子吗？ 我的意思是，Cleanroom 基本上是如何在不共享底层数据的情况下共享数据，但允许特定操作。 这些最初仅有效地为两个客户完成。 我觉得行业有一种感觉，就是如果你对一两个客户过于拟合， 这对你来说会非常糟糕。 但我认为过拟合的缺点远小于其好处。 如果你试图过于雄心勃勃，涉及太多，就会成为一个更大的问题。

[40:58] **swyx**
是的。

[40:58] **Reynold Xin**
因为你可能最终真的没有客户。

[41:00] **swyx**
是的，那是更可能的结果。 然后你可以从那里转变。 我确实认为有这样的坏客户，有时候你会碰上。

[41:08] **Reynold Xin**
如果你推动的话，他们有时会存在。 我觉得我们可能看到的一个挑战，以及许多新一代公司看到的挑战是，科技公司与非科技公司或传统企业非常不同。 如果你仅为科技公司优化一切，你可能在将它们推广到科技公司之外时会遇到各种挑战。

[41:29] **swyx**
好吧。 你始终考虑的前三大差异是什么？

[41:33] **Reynold Xin**
治理是一个重要问题。

[41:34] **Matei Zaharia**
我认为，一个重要的问题是，安全性、数据隐私、治理，所有这些问题。 所以通常如果你在构建某种 B2B 或开发者工具，你最大的市场将是企业，但这真的非常不同。 一家存在了大约 30 年的公司，已经有某种形式的 IT。 他们有很多遗留系统，或者他们在受监管的领域运营。 而初创公司或甚至一些更新的科技公司，所有一切都是新的，几乎是完美的。 所以，是的，这就是不同之处。 如果你从未与企业合作过或是其中一员，你就不会了解这些。

[42:13] **Reynold Xin**
而采购流程可能也会非常不同。 实际上，涉及的利益相关者要多得多。

[42:17] **Matei Zaharia**
是的，这就是一个。 是的。 还有一个有趣的点是，我认为一些科技公司，人们会说，哦，我可以自己构建。 我会自己构建。

[42:27] **swyx**
我不认为人们会对 Databricks 这样说。

[42:33] **Matei Zaharia**
这取决于团队和其他因素。 但另一方面，像许多企业，我实际上，我从不想进入构建那样的业务。 我不希望我的，哦，无论我是什么零售商之类的。 我从不想因为某个奇怪的 “书呆子” 无法让我们的流媒体管道正常运行而停滞不前。 这不是我所做的事情。

[42:53] **swyx**
说实话，这让他们成为优秀的客户，对吧？

[42:55] **Matei Zaharia**
但你必须理解，这很难，在没有在那里的工作经验的情况下，可能你不会欣赏。

[43:01] **Reynold Xin**
听着，我觉得他们都同意。 别误会我的意思。 他们面临着不同的挑战。 但许多科技公司，确实，他们有更多的 DIY。

[43:09] **Matei Zaharia**
另一方面，你有一些人，他们在自己的领域里非常专业。 就像他们在造飞机。 他们在设计药物，无论怎样。 他们只想连接技术。 他们不想学习数据库之类的，尽管我们认为这很酷，即使是普通软件工程师也可能觉得这很有趣。 他们只是从不想知道。 他们只是说，我有一个巨大的矩阵，或者其他的东西，有我的临床数据。 我该如何进行聚类或者其他的？ 所以，是的。

[43:40] **swyx**
是的。 是的，确实如此。 好吧。 所以我想实际构建出那种梦想引擎的愿景。 日志指向哪里？

[43:49] **Reynold Xin**
我们大约在几年前意识到的一件事是，实际上每一个数据库引擎，特别是在分析方面，都是有点过时的。 基本上所有有合理吸引力的产品都大约有十年历史。 而且它们都是针对一些非常特定的、狭窄的用例开始的。 然后随着时间的推移，它变得越来越成功。 它们在抱负上不断增长，然后尝试支持越来越多的用例。 但支持这些用例的最快方式往往是绕过最初创建的那些抽象，因它们并不是为这些用例而设计的。 但你在某种程度上可以勉强支持它们。 而在你意识到之前，经过十年的有机演变，它变成了一堆庞然大物。 顺便说一下，这也包括 Databricks。 我认为很少有公司或系统敢于说，让我们从头开始。

[44:45] **Reynold Xin**
让我们回到设计图，考虑到在经历了十年的负载和可能数十亿的收入之后所知的一切， 让我们尝试从头开始重写，并确保它能够正常工作。 然后我们可以支持所有这些用例。 所以我们开始这样做。 但这是一个非常雄心勃勃的项目。 顺便说一下，你可以在维基百科上搜索。 有一种叫做第二系统综合症的东西。

[45:09] **swyx**
是的，我知道这个。

[45:09] **Reynold Xin**
我们的第二系统效应。

[45:11] **swyx**
每个开发者都应该知道什么是第二系统。

[45:12] **Reynold Xin**
基本上你先构建了第一个东西，并且效果很好。 而第二个注定会失败，因为你变得过于雄心勃勃。 然后你提出了太多要求。

[45:20] **swyx**
你认为自己什么都知道。 然后你想，我这次要设计完美的系统。

[45:24] **Reynold Xin**
是的。 然后结果证明并不完美。 然后它们开始失败，你的雄心勃勃，永远无法推出，你就被淘汰了。 实际上启动这个项目的工程团队，他们非常优秀。 我认为我们在 Databricks 雇了一些地球上最优秀的数据库工程师，他们非常优秀。 感谢上天这不是他们的第二个系统。 他们当中许多人在过去构建过超过两个系统。

[45:44] **swyx**
啊，太好了。

[45:45] **Reynold Xin**
但他们仍然对此感到担忧。 嘿，从头构建一个数据库引擎，我认为传统智慧是这将花费五年成熟。 这将是一个非常长期的项目。 它可能会失败。 我觉得其中一位工程师开玩笑说，嘿，也许我们就叫它 Reynolds Dream Engine。 如果我们以联合创始人的名字命名，可能会被取消或被取缔。 但我认为他们构建了一些相当了不起的东西。 他们回到了一种改变数据库引擎构建方式的范式观念。 通常，当你构建一个数据库引擎时，你会阅读大量学术论文。 你试图了解最新的算法和数据结构，然后将它们组合在一起，看看它们是否有效。 而且那里还有很高的失败风险，因为在纸面上看起来很好的东西可能在 70% 的负载上效果不错， 但在其他 30% 上却反而失败。 当构建出一个更像是数据库的工厂时，他们花更多的时间构建这个工厂，而这个工厂使用我们十年的跟踪数据。

[46:42] **Reynold Xin**
我认为他们在跟踪表中列出了一个千万亿的数据点。

[46:47] **swyx**
你不丢失任何东西吗？ 或者你查看样本？

[46:49] **Reynold Xin**
我们肯定会取样，但有大量的事物，他们利用这些建立模型。 我是说机器学习模型，而不是 LLM，机器学习模型。 机器学习模型基本上可以非常非常快速地告诉我们任何算法和任何实现对于任何特定类型查询的表现如何， 精确度非常高。 而且基于此，他们可以选择最有可能的算法和数据结构，这些都会帮助处理不同类型的负载，无论是在运行时还是在实现时。 因为存在无限数量的。

[47:26] **swyx**
我是说，这听起来你想要路由到不同的数据结构。

[47:31] **Reynold Xin**
是的。 我是说，如果你考虑的话，单个数据库实现了许多东西在一起，但你想要确保它们彼此之间都能良好工作。 对于任何给定的操作，可能有多个实现。 所以我们使它实际运行得非常好。 现实是，对于超级低延迟非常有效的算法，可能在扫描数 PB 数据时效果不好。 实际上，通常存在吞吐量和延迟之间的权衡。

[47:58] **swyx**
关键维度是什么，比如规模、吞吐量、延迟，还有其他吗？

[48:03] **Reynold Xin**
以及数据的分布，对吧？ 数据的稀疏程度很重要。 你多频繁访问相同的数据？

[48:10] **Matei Zaharia**
不同值的数量等等。

[48:12] **Reynold Xin**
这些都很重要。 不同值的数量基本上会影响你聚合的内存消耗，你的哈希。 在某个时刻，会有一个哈希表。

[48:20] **swyx**
在我的写作中，我将尝试列出所有这些，因为我真的想要一个分类法。 对我来说，分类法非常有帮助，因为它涵盖了你应该考虑的一切。

[48:28] **Reynold Xin**
我认为如果你真的尝试列出来，大概会有百万个不同的特性。

[48:34] **swyx**
我总是觉得，好吧，给我 12 个。你知道，就像有人说，我想 40 年前做的 Oracle 论文中写的那样， 这些是分布式系统的八个谬误。 这种事情非常有用。 就是，好吧，考虑这八个。

[48:48] **Reynold Xin**
但让我给你一个非常奇怪的例子，但它实际上对性能有深远的影响， 就是你的字符串只是 ASCII 还是里面有 Unicode？ 你应该如何对其进行编码？

[48:59] **swyx**
我是说，字符串是最复杂的数据类型。 是的。

[49:01] **Reynold Xin**
所以，比如说，如果字符串超级稠密，你实际上可以把每个字符串转换成一个， 比如你必须进行休眠。 而不是使用哈希表，你实际上可以使用一个数组。 因为如果你的字符串足够密集，如果你只有 256 个选项，你就不需要哈希表。 你可以直接进行数组查找。

[49:21] **swyx**
是的。

[49:22] **Reynold Xin**
这样会快得多。

[49:23] **Matei Zaharia**
就像国家代码之类的。 是的。 是的。

[49:26] **Reynold Xin**
所以在那个模型中，实际上可能有数百万个特征。 但利用这一点，他们可以基本上优先考虑那些在实践中可能实际影响的不同算法。 其中许多是非常反直觉的。 实际上，许多你认为可能效果很好但实际上效果并不好。 但更重要的是，在运行时，你可以分派合适的算法和结构。

[49:47] **swyx**
我在听梦。 我觉得 Databricks 在逐步演进方面做得很好。 你有没有在任何时候硬切换到新系统？

[49:57] **Reynold Xin**
我们的设计方式使其可以逐步过渡。 所以我们首先推出一个新的端点。 这个端点与我们想要做的范围相比如何？ 这个新引擎应该能够做我们之前能够做的一切且更好，对吗？ 这非常特别。 更好的部分是指非常低的延迟，低延迟工作负载。 我可以在数十毫秒内完成，但我们希望逐步展开，具备逐步能力。 这样不需要花五年时间才能看到隧道尽头的光明。

[50:29] **swyx**
我认为这是一个艰巨的任务。 我不知道还有什么别的方式来表达。 我对任何新工作负载和新数据库都非常感兴趣。 我想，我可能已经确立了我是有点数据库迷的身份。 交易数据库，抱歉，指的是会计数据库，比如虎甲虫。 我不知道你是否见过那些。

[50:50] **Reynold Xin**
它们有什么用？

[50:51] **swyx**
双重记账数据库。 它的目的是很好地建模财务账户和信用系统。

[50:56] **Reynold Xin**
这就像一个非常特定的品牌。

[50:58] **swyx**
非常高的吞吐量。 不，是你谈到如何每个人都从某样东西开始，然后逐渐扩展并附加其他东西。 就是那样。 然后我最近采访了 TurboCoffer 的 Simon。 同样的情况。 Chroma 也是如此。 2023 年所有的向量数据库公司，现在突然都变成了通用存储，Blob 存储。

[51:18] **Reynold Xin**
向量数据库本来就不该是一个独立类别。

[51:21] **swyx**
我觉得这曾经是一个热门观点。 现在它就像是当今的传统智慧。 什么应该是一个独立类别？ 你知道，如果一切都变得 LTAP，那...

[51:30] **Reynold Xin**
我认为 LTAP 的主旨是我们并没有在实际查询层上合并数据库。

[51:37] **swyx**
我们只是合并存储层。

[51:39] **Reynold Xin**
我认为这是一个非常重要的部分。 我们实际上认为合并没有意义，我们将讨论如何将查询层整合到一个单一的 HTAP 风格数据库中。 另外一个我认为很多人提到的是，嘿，如果只有一种查询语言需要我去关注，那就太好了。 而不是关注 PostgreSQL 和 Spark SQL，为何不只用一种呢？ 但我认为这对代理来说并不是问题。 代理在 PostgreSQL 或 Spark SQL 中非常流畅。 它们绝不会搞混。 只要数据存在并且可访问，代理将会表现良好。 这可能是五年前对人类来说的一个问题。

[52:17] **Matei Zaharia**
随着时间的推移，也可能会出现，但这应该会导致如何逐步进行的讨论，对吧？ 就像我们意识到你现在不需要它。 我们不需要解决那个问题就能从核心 Intel tap 中获取很大的价值。

[52:30] **swyx**
是的。

[52:31] **Matei Zaharia**
好的。

[52:31] **swyx**
我要用一点更刺激的东西来结束这个播客。 每个人都经历了存储和计算的分离，并尝试构建云。 我从 Snowflake 得到过相同的推销。 你们是如何在他们失败的地方取得成功的？

[52:50] **Unknown Speaker**
这很棘手。

[52:52] **swyx**
我是说，尊重他们是竞争对手，从客观的角度来看，你们超越了他们。 从你的角度来看，你们之间的核心洞察是什么，以至于你们走上了不同的方向？

[53:02] **Reynold Xin**
可能最大的根本区别。 两家公司几乎在同一时间成立。 两者都转向了云。 两者都专注于存储而不是计算架构。 但最大的区别是，一个是开放的。 Databricks 从未有过专有格式。 我们从开放生态系统开始，以 Parquet 开始，然后发展为 Delta 和 Iceberg 等。 这是一件大事。 我认为这非常重要。 另一个是人工智能。 在 2022 年 10 月 ChatGPT 发布之前，我们一直将 Databricks 昭告为机器学习加数据。 平台的许多功能都是针对机器学习用例构建的。 而显然，人工智能有点不同。 Matei 在这里花费的时间比我多得多。 但整个平台，我们从不觉得，嘿，我们只是一个数据基础设施平台。

[53:53] **Matei Zaharia**
我认为他们开始是想，好的，我们只管理最有价值的数据，并尽量做到快速。 为此，我们会有自己的存储，你知道，优化与引擎结合。 然后我们会只针对小量数据，比如管理人员和财务人员等查看的那些，将其速度提升到服务。 而且，你知道，这是一个不同的空间，而我们开始的想法是，好的，我们来做批量处理和数据摄取。 就像你有一堆 JSON 日志文件，无论是什么。 我们做的是大规模的数据处理，因为这是 Spark 的用途，对于大规模的映射等工作。 然后我们会以开放格式保存数据。 这可能会慢一些，但它已经存在。 你可以在下游使用它。

[54:41] **Matei Zaharia**
结果发现，从那种在规模上非常优秀、能快速获取且成本极低的广泛事物转变过来，创建具有速度和功能的版本更容易， 那种对于商业用户来说超级易用的小型数据的东西。

[55:02] **swyx**
先开放，然后进行优化。

[55:04] **Matei Zaharia**
对，先开放，再开始大规模。 在某种意义上，我们是从他们上游开始的。 其实有一段时间，我们彼此都把对方列为合作伙伴，因为他说，如果你同时使用两个解决方案，使用 Databricks 进行数据摄取和计算，然后从 Snowflake 提供表格， 你就可以获得所有的可视化，所有非常快速的功能，这太棒了。 然后，你知道，我们都意识到，客户在告诉我们，为什么我需要这个其他东西？ 为什么我不能直接查询你们的表？ 我们说，不，我们在这方面很糟糕。 请使用我们的合作伙伴来处理 SQL 仓库。 然后他们意识到，等一下，计算机的大部分功能正转向这个其他东西。

[55:43] **swyx**
你们必须进入彼此的领域。

[55:45] **Matei Zaharia**
但我认为我们确实是从更大的范围和开放的事物开始的。 这对架构很重要。 作为一个，嗯，这与企业有关。 如果你的公司已经存在了大约 30 年，你就会经历，知道被锁定在 Oracle 里，以及各种疯狂的事情。 如果你是首席技术官，并且正在为你的公司未来搭建架构，你会想选择一个开放的基础。 而且你只想要一种方法来管理你公司的数据。 理想情况是，你不想要七种不同的系统。

[56:17] **Reynold Xin**
顺便说一下，开放数据格式已经获胜。 我想现在每个企业都想采用开放数据格式，但那时其实是非常有争议的。 具体是什么时候？ Snowflake 的联合创始人实际上写了一篇名为《明智地选择开放》的博客，这基本上是和我对立的。 我想他们可能已经把它撤下了。 你现在得去档案里找。

[56:38] **swyx**
它现在永远不会消失。 不，不，它还在那儿。 我喜欢你们只有的这种视角，因为显然你们经营着公司。 谢谢你们的宽容。 这是个令人难以置信的视角。

[56:52] **Reynold Xin**
也许最后一个。 当你在谈话时，我想我必须给 Ali 很多赞扬。 他是一位令人难以置信的首席执行官。 我认为他是 IQ、EQ、技术、痴迷、执行力和商业头脑的完美结合。 而且他也是一位创始人，这使得他更容易动员和执行。 我认为就这些。

[57:17] **swyx**
我以为会有一些他参与的技术选择。

[57:28] **Matei Zaharia**
他确实参与了很多这些。 在分叉的路口，他推动了一种方式，然后变得明确那是正确的方向。

[57:37] **swyx**
我的意思是，有整本书需要写出来，关于你们八个人如何合作等等。 我认为有人做过一些专题。 第二个，不是清晰的问题。 Mosaic。 我们社区的许多人对 Databricks 的模型故事感到好奇，对吧？ 就像当你们购买 Mosaic 时，事情是这样的，我们可以进行微调。 我们要做内部模型，因为他们有 Mosaic 模型。 看起来你们并没有这样做。 看起来你们正在朝着更多的 LTAP 和 Harness 的方向发展。 这里有什么故事？

[58:14] **Matei Zaharia**
是的，我想当 Mosaic 开始的时候，它是众所周知的，或者说以早期发布开源 LLM 而最出名。 他们是通用模型。 事实上，在那之前，他们在做其他事情。 他们主要是在优化训练系统。 所以他们拥有世界上最快的图像模型训练堆栈等等。 然后他们决定做 LLM，这是聪明的。 在 ChatGPT 之前他们就已经开始了。 所以他们拥有一些首批开源 LLM。

[58:43] **swyx**
我们采访了 John Franco 和 Avi 关于 MPC7B。

[58:46] **Matei Zaharia**
是的，没错。 是的。 哦，是的。 非常酷。 是的。 是的。 所以我们决定，尽管我们推出了一个开源模型 DBRX，且我们达到了大约 LLAMR3 的规模， 我们决定我们真的想专注于将会有这么多人发布模型。 我们不想做那种普通模型，比如说，成分中很大一部分就是投入大量计算并进行扩展， 我们想关注像下一步这样的内容，假设你有一个非常聪明的模型， 你如何让它对我们有用。 这主要是关于自动化，比如如何让它在查询数据方面变得非常出色。 这就是我们称之为 Genie 的第一方代理。 所以它就像一个虚拟数据科学家。 想象一下，有人已经熟悉你们公司所有的东西，了解所有的机器学习库，所有的数据库，知道网络上的这些东西，你可以问他们， 问题，你知道的，这就是我们想要首先做的事情。

[59:46] **Matei Zaharia**
所以这意味着，让我们不要过多关注，我们只是训练某种前沿模型。 但让我们使用外部模型或经过微调、定制的组件来构建这个系统。 不过我们仍在进行相当多的模型训练。 实际上，我们一直在不断采购大量的 GPU 等设备来完成这项工作。 这方面我们有几个地方在进行。 一方面是有许多高频使用案例，如果你有一个专业的模型，它比任何通用模型都要好得多。 一个很好的例子是理解文档，比如 PDF、Word 文档，类似的东西。 对它们进行解析。 如果你曾经尝试过这个过程，会发现这很令人沮丧，因为你将其发送到，比如说，Claude Fable 等等，它几乎能理解， 但它会搞错一些东西，而且成本非常高。 你在这里输入一张图片，耗费了大量的令牌。

[01:00:41] **Matei Zaharia**
所以我们的团队构建了这种文档视图模型，它能够接收一页，并给你返回一个漂亮的 JSON，包括所有组件。 它的竞争力非常强。 可能比那些前沿模型便宜大约一百倍，而且效果更佳。 这个模型实际上是由一位来自 DeepMind 的研究人员开发的，他是 ADAPT 的共同创始人，是非常早期的 LLM 扩展人员，但专注于此。 同样，我们正在为编码代理所做的部分开发专业子代理。 如果你看过 Harvey 和 Anthropic 的顾问模型相关的内容。 还有加州大学伯克利分校，其实，我的一位研究生在那儿写了一篇名叫顾问模型的论文，我想是在这些内容发布之前。 我的意思是，我相信其他人同时也有这个想法，但这东西确实帮了很多忙。 所以，是的，我们今天在主题演讲中展示了一些内容……

[01:01:38] **swyx**
是 Parth 吗？ 哦，你认识 Parth？

[01:01:39] **Matei Zaharia**
是的，是的，Parth。

[01:01:39] **swyx**
哦，他会在我的活动上发言。 他正在进行持续学习基准测试。

[01:01:42] **Matei Zaharia**
是的，是的，没错。 我是他的顾问之一。 哦，是的。

[01:01:45] **swyx**
我们采访过他的兄弟 Chai，因为他也在一座桥上。

[01:01:48] **Matei Zaharia**
是的，是的，是的。

[01:01:49] **swyx**
那个家庭非常聪明。

[01:01:53] **Matei Zaharia**
我们正在做一些这样的事情，随着我们在第一方代理上的经验增加，我们也在与客户一起做这些。 所以我的感觉是，自定义模型实际上会随着时间的推移变得更加容易。 这是我们发现的，因为基础模型更智能，因此它们产生更好的轨迹，而强化学习已经在进行中， 而强化学习就是从你自己过去的轨迹中学习。 然后合成数据生成现在要好得多，容易得多。 我们有管道只使用开源模型，比如同一个模型生成训练环境并自我训练，并在某个任务上击败像 OPRS 和 GPD 5.5 这样的模型。 所以我确实认为，训练的简易性只会逐渐提高。 有一个问题是它何时会进入主流，比如说不再是我们做的这种专业文档解析，需要硬核 LLM 研究者的那种。 什么时候才会简单到任何人可以随便放入一些东西并描述一个任务？

[01:02:53] **swyx**
是的。 嗯，你知道是什么让这变得简单吗？ 接口。 是的。 以及统一 API。 因为显然如果不具备互操作性，那么你就无法切换。

[01:03:00] **Matei Zaharia**
这就是我们在 Omnigent 和可组合代理上看到的。 你可以拥有与专业模型的子代理，然后你可以训练整个系统。 我认为这也会有很大帮助。

[01:03:11] **swyx**
我最后要提到的事情，实际上，我正在安排这个，所以我对自己有点自豪。 Safia 在讨论这个。 我几周前在微软 Build 上采访了他，然后他写了这篇文章，我相信你已经看过，谈论的是建设一个前沿生态系统。 当我和他交谈时，他听起来更像一个 Databricks 的首席执行官。 我是说，这个事情在我的圈子里大概已经疯传了。 我不知道在你的圈子里怎么样。 关于代币作为知识产权构建上下文的理论是什么， 他基本上说了一切，除了数据是新的石油或上下文是新的石油。 这种版本，你知道的，你们以前听过的。

[01:03:54] **Matei Zaharia**
是的，我同意。 我认为你拥有的数据，随着技术的进步，你可以在你的领域内做更多事情。 这不仅仅是关于人工智能。 即使当人们开始实时收集数据时，我记得所有的电力公司都安装了智能电表，所有汽车制造商也开始安装传感器和摄像头之类的设备。 任何技术都让数据更有价值，并且能给你带来一些优势，任何可以帮助你利用数据并做出决策的事情， 人工智能也是一样。 你拥有的所有这些数据都只是静静地放着。 现在你可以让代理自动告诉你。 例如，不是我发现我的产品中的某个功能因客户投诉而损坏，而是代理告诉我，我注意到没有人再上传文件了，因为他们出现了错误或其他问题。 正如你看到的，像雷达以及作为一个数据库公司，因为我们拥有所有这些数据。 所有查询的历史和所有表的布局，以及它们是如何工作的，我们可以非常快速地构建出一个实际良好的新引擎。

[01:04:55] **Matei Zaharia**
我们相信它会很好。 所以我认为这是对的。 我认为问题在于它将如何落地。 但我确实认为，Sajat 所说的定制模型的个性化，随着时间的推移会变得更容易。

[01:05:10] **swyx**
是的，这也是为什么顺便提到这个模型，因为他们有他们的 MEI，而你们没有。 这是一个心理问题。

[01:05:17] **Matei Zaharia**
是的，我们确实有，我们正在做 RL 微调作为一种服务，并且有一堆客户。 我们并没有像，基本上，你知道，我们有预览客户，还有一种叫做 AI Runtime 的一般服务，就是当你需要时，可以获取你的 GPU 集群，并在其中有软件栈，使得训练变得简单。 我们并没有像这样做，这种服务已经存在了一段时间。 我们已经有了 GPU 计算一段时间，这就是很多马赛克堆栈帮助扩展的地方。 但是是的，我们发现参与度就像其中的一些，有两种类型的客户。 有些人只是想要 GPU 和库来进出数据并进行监控。 所以这就是 AI Runtime 的用途。 然后还有一些人说，嘿，你知道吗，你能和我合作吗，构建评估，构建合成数据？

[01:06:04] **swyx**
这就是我们正在做的。

[01:06:08] **Matei Zaharia**
随着越来越多的事物从定制转变为非定制，但今天大概就是这样。

[01:06:15] **Reynold Xin**
回到你最初的问题，我认为我们的一个论点是，实际上是将数据放在正确的位置。 AI 模型正在变得相当优秀。 通用代理相当，我是说，Ali 已经提到 AGI 已经出现。 他们具备不错的推理能力。 其实，我认为许多传统的软件将会被重新编写。 采用 Zoom 模式，即将数据放到那里，然后在上面加上某种代理，魔法就会出现。 但是没有合适的数据，你真的无法做到这一点。 实际上，我们在安全领域的做法以及在客户数据平台领域的做法就是，我们在数据与 AI 峰会上推出了两个产品， 一个针对安全团队，另一个针对营销团队。 而且这些都有很多现有的技术。 我认为我们的做法就是，嘿，一旦你将数据导入，一切在上面加上代理后就会容易得多。

[01:07:09] **swyx**
是的，是的。 嗯，你们真是优秀的嘉宾。 我非常喜欢这个讨论。 我喜欢深入探讨技术方面，还有文化和战略。 我希望这不是我们最后一次聊天。 意思是，恭喜你们迄今取得的所有成功。

[01:07:23] **Reynold Xin**
谢谢。 也恭喜你们的成功。

[01:07:27] **Matei Zaharia**
是的。

[01:07:27] **swyx**
是的。 我的意思是，Databricks 实际上支持我的活动，也就是，我主办了 AI 工程师大会，实际上是， 我曾经是 Data AI 峰会的参与者很长时间。 我注意到那时大约是 2022 年。数据占了 90%，而 AI 占了 10%。 我只想说，嗯，好吧，我们需要这个。 我们需要这样一个社区活动，就是 90% 是 AI，现在每个人都是。 所以 Databricks 会出现在大会上。 我知道看到你们建立出我在大三之外未曾见过的最有趣的云服务实在令人惊叹。 你们的成长速度真是令人惊讶。 这是最有洞察力的，我不是风险投资人，但我在电视上扮演过。 本·霍洛威茨在和你们谈话时，给你们提供建议，问你们这个公司要往哪里去？ 他是这样说的，别以 1000 亿美元或者那种故事去销售，对吧？

[01:08:22] **Reynold Xin**
他认为，这家公司应该值 1 万亿美元。 你们以 100 亿美元的价格卖太低了。

[01:08:26] **swyx**
他并不是对每个人都这样做。 不知为何，我认为他看到了愿景，以及你们无限的发展空间。

[01:08:36] **Reynold Xin**
我们很幸运能有本的支持。 是的。 他是一个大力支持者。 是的。

[01:08:39] **swyx**
真令人惊叹。

[01:08:40] **Matei Zaharia**
好的。

[01:08:40] **swyx**
非常感谢你们。

[01:08:41] **Reynold Xin**
好的。 非常感谢你，Swyx。
