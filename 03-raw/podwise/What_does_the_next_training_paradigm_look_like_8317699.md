---
podcast: "Dwarkesh Patel"
episode: "What does the next training paradigm look like?"
link: https://podwise.ai/dashboard/episodes/8317699
publish-time: "2026-06-26"
save-time: "2026-07-01"
---

# What does the next training paradigm look like?

## Summary

The current AI research paradigm relies on Reinforcement Learning from Verifiable Rewards (RLVR) to build general-purpose agents capable of solving diverse, verifiable tasks. While scaling compute has historically driven progress, current models face significant bottlenecks regarding sample efficiency and continual learning. Because real-world environments are often non-stationary and lack deterministic simulators, models struggle to learn from sparse, unstructured data. To overcome these limitations, future advancements may depend on techniques like On-Policy Self-Distillation (OPSD) and "dreaming," where models generate their own simulated environments to rehearse skills. By distilling these experiences back into model weights, AI systems could evolve from static, pre-trained tools into agents that continuously learn through broad economic deployment, effectively turning every user interaction into a source of intelligence rather than relying solely on pre-release training.

Takeaways:
1. The current industry-wide bet on AGI hinges on the assumption that training models on millions of verifiable tasks within diverse reinforcement learning environments will naturally produce a general-purpose problem-solving agent.
2. Progress in computer use lags behind coding and math because it lacks "grindable" environments—deterministic, replayable simulators that allow for thousands of parallel, identical rollouts.
3. Achieving human-level proficiency requires the ability to learn from sparse, unstructured, and ambiguous real-world data, a capability that current models lack due to their extreme sample inefficiency during training.
4. While expanding context windows allows models to simulate competence, it fails to provide a scalable solution for long-term learning because it does not distill knowledge into the model's weights, resulting in significant wasted inference compute.
5. On-policy self-distillation (OPSD) offers a superior path for continual learning compared to reinforcement learning, as it provides a denser supervision signal and allows models to consolidate relevant insights without overwriting existing knowledge.
6. "Dreaming"—where models generate and rehearse against their own simulated environments—could emerge as a fourth axis of scaling, enabling models to gain experience orders of magnitude faster than real-world interaction allows.
7. The primary driver of AI capability will eventually shift from pre-training to continuous on-the-job learning, where models refine their weights based on the tacit knowledge and specific failure modes encountered during broad economic deployment.

## Chapters

### [00:00] Chapter 1: The RLVR Paradigm for Achieving AGI

The prevailing research bet in AI labs suggests that training models on millions of verifiable tasks across diverse reinforcement learning (RL) environments will effectively build AGI. This approach aims to create problem-solving agents capable of sustained progress on open-ended tasks despite ambiguity. Proponents argue that current limitations, such as data inefficiency and lack of continual learning, can be overcome through increased scale. Furthermore, as in-context learning improves, the need for traditional weight-based continual learning may diminish, as models could potentially fit months of on-the-job experience directly into increasingly large context windows.

### [02:12] Chapter 2: The Bottleneck of Non-Replayable Environments in Computer Use

Progress in computer use has lagged behind domains like coding and math because it lacks a "grindable" environment. Effective training requires running thousands of parallel, deterministic, and replayable rollouts from identical starting points, which is difficult to achieve with real-world applications like Amazon or Gmail. While building high-fidelity clones of software environments is a potential solution, it remains labor-intensive. This lethargy highlights a fundamental truth: models struggle to make progress in domains where the training target cannot be easily replicated, making it difficult to isolate successful actions in complex, real-world scenarios.

### [06:10] Chapter 3: The Necessity of Continual Learning and Weight Updates [ad]

Relying solely on in-context learning for complex, long-horizon tasks is insufficient because it fails to distill knowledge into the model's weights. Current inference-time compute is largely wasted, as models cannot permanently learn from the tacit knowledge gained during deployment. Unlike humans, who consolidate insights into long-term memory, current AI models are limited by the size of their KV cache. True proficiency in domains like business building or politics requires the ability to update weights based on sparse, real-world interactions, rather than relying on ephemeral in-context information that disappears once a session ends.

### [11:48] Chapter 4: Advancing Continual Learning via OPSD and Dreaming [ad]

On-Policy Self-Distillation (OPSD) offers a superior method for continual learning by encouraging base models to match the performance of a veteran teacher model that has accumulated experience during a session. This provides a denser supervision signal than naive reinforcement learning and avoids the pitfalls of supervised fine-tuning, which often leads to overfitting on transcripts. Additionally, "dreaming"—where models build and rehearse against their own internal simulations—could serve as a fourth axis of scaling. By practicing in self-generated environments, models can achieve orders of magnitude more experience, potentially overcoming the sample efficiency deficit inherent in real-world data.

### [17:23] Chapter 5: Future Trajectory of Autonomous AI Deployment

The future of AI improvement lies in broad economic deployment, where agents learn on the job through a combination of OPSD, dreaming, and other emerging techniques. Once an agent is competent enough to handle unfamiliar problems, it can be deployed to perform real work. Upon receiving positive feedback, the base model can distill the lessons learned during that session, allowing it to improve in domains adjacent to its original training. Eventually, the primary driver of AI capability will shift from pre-training to the continuous accumulation of knowledge from diverse, real-world interactions across the global economy.

## Q&A

### Q1: What is the primary "research bet" that major AI labs are currently making to achieve AGI?
A1: The prevailing strategy is to train AI models on millions of verifiable tasks across thousands of diverse reinforcement learning (RL) environments. The hypothesis is that by forcing models to make progress on open-ended tasks over long time horizons—while handling errors and ambiguity—we will essentially build a general-purpose problem-solving agent. Proponents believe that current limitations like data inefficiency or a lack of continual learning are not fundamental roadblocks; they can be "steamrolled" simply by scaling up the training compute, much like how massive compute solved many core problems in natural language processing.

### Q2: Why has progress in "computer use" lagged behind other domains like coding or mathematics?
A2: While computer use is highly verifiable—you can easily check if a tax form was submitted or an item was ordered—it lacks "grindability." To make rapid progress, you need to run thousands of parallel, deterministic, and replayable simulations from the same starting point. In coding, you can easily spin up a thousand identical containers to test a feature. You cannot do this with live websites like Amazon because the platforms will block your bots. Until AIs are capable enough to build high-fidelity clones of these applications to train against, progress in computer use will remain constrained by the difficulty of creating these replayable environments.

### Q3: Is "continual learning"—the ability for a model to update its weights based on deployment experience—actually necessary for AGI?
A3: There is a debate here. Some argue that as in-context learning becomes more powerful and context windows grow to effectively infinite sizes, we may not need to distill every lesson back into the model's weights. However, I believe this is a limited view. Humans don't just keep every experience in their "working memory"; we consolidate important insights into our long-term intuitions. If we want AIs to master complex, real-world tasks—like building a business or navigating politics—they need a way to move beyond in-context learning and actually update their fundamental parameters to reflect tacit, organization-specific knowledge.

### Q4: What is "on-policy self-distillation" (OPSD), and why is it a promising approach for continual learning?
A4: OPSD is a technique where you encourage a base model to match the predictions of a "veteran" version of itself that has already accumulated context and experience during a session. It is superior to naive reinforcement learning because it doesn't require an outer-loop reward signal; you simply use the veteran model as a teacher. It is also better than supervised fine-tuning because, instead of forcing the model to memorize every single token from a transcript, it extracts only the knowledge necessary to achieve the teacher's results. This allows for dense, targeted updates that improve the model without overwriting its existing knowledge.

### Q5: What is the concept of "dreaming" as a potential fourth axis of AI scaling?
A5: "Dreaming" is the speculative idea that an AI could build its own internal simulations of reality to rehearse skills and test strategies. If an AI can generate its own training environments, it could experience orders of magnitude more "practice" than it could ever get from real-world data. If this works, it would become a new axis of scaling alongside pre-training, RL, and inference-time compute. Instead of just relying on external data, the model would spend compute to "dream" up a video-game version of the world, allowing it to refine its capabilities in a sandbox before applying them to production.

### Q6: Why is the current separation between model parameters and activations a bottleneck for AI development?
A6: Currently, a significant portion of a lab's compute goes to inference, which is essentially "wasted" because the model doesn't learn from those interactions. Humans don't have a clean separation between parameters and activations; we learn by chiseling intuitions into our "weights" (our brains) through experience. If we continue to rely solely on in-context learning, we are effectively running a "genius grad student" who is never allowed to take a real internship. We need architectural or algorithmic breakthroughs that allow models to consolidate the tacit knowledge they encounter in the real world back into their weights, rather than just relying on an ever-expanding KV cache.

### Q7: What does a successful future for continual learning look like by 2027 or 2028?
A7: I envision a cycle where an AI is deployed to do real work, and at the end of a week, it receives a performance review from the user. If the work is successful, the base model distills everything the AI learned during that session—perhaps using a combination of OPSD, dreaming, or other techniques. This allows the AI to improve in domains adjacent to its original training. Over time, the primary way AIs get smarter won't be pre-training, but the massive amount of experience they accumulate from being broadly deployed across the economy. Every interaction will make the model smarter, not just for that specific user, but for the entire system.

## Highlights

1. [03:12] It is not enough for a domain to be verifiable. It also has to be grindable, in the sense that you must be able to run parallel rollouts against a deterministic and replayable simulator.
2. [08:53] There is no clean separation in our brain between parameters and activations. It is not like some part of your skull keeps expanding as you learn more things throughout your lifetime.
3. [14:16] The way you get better at your job is not by recalling the transcript of every single thing that happened with perfect fidelity. Rather, it is by consolidating the handful of insights and pieces of knowledge that are actually relevant to your improvement.
4. [19:22] Every time you interact with an AI, it will be smarter. It learns not only from your previous sessions but also from all its interactions with every other user in the world.

## Keywords

1. **AGI (Artificial General Intelligence)**: A hypothetical form of AI that possesses the ability to understand, learn, and apply knowledge across any intellectual task, similar to a human. In the transcript, it is described as the ultimate goal that research labs are aiming for by training agents on millions of diverse tasks.
2. **RLVR (Reinforcement Learning with Verifiable Rewards)**: A training method where AI agents are rewarded for successfully completing specific, measurable tasks within controlled environments. The transcript identifies this as a primary strategy used by labs to build problem-solving agents that can handle complex, open-ended work.
3. **Transformer**: A type of neural network architecture that serves as the foundation for modern large language models. It is designed to process data in sequences, allowing models to understand context and relationships between information over long distances.
4. **Context Window**: The total amount of information or data a model can "see" or process at one time during a single interaction. The transcript suggests that expanding this window is a key way to help models handle complex, long-term tasks without needing to permanently update their internal memory.
5. **Continual Learning**: The ability of an AI to learn and adapt to new information or environments after its initial training phase is complete. The transcript argues that this is essential for AI to function effectively in real-world jobs where conditions and requirements are constantly changing.
6. **OPSD (On-policy self-distillation)**: A technique where a base AI model is trained to mimic the behavior of a more experienced version of itself that has already completed a task. By distilling the knowledge gained during a specific session back into the model's core memory, it allows the AI to retain what it has learned for future use.
7. **AlphaZero**: A powerful AI system developed by DeepMind that taught itself to play games like Chess and Go at a superhuman level through self-play. It is mentioned in the transcript as a benchmark for how AI can master complex skills through reinforcement learning.
8. **KV Cache**: A technical component in AI models that stores previously computed information to speed up the generation of new text. The transcript notes that while this is useful for short-term performance, it is not a scalable way for models to store or learn new, permanent knowledge.
9. **EfficientZero**: An AI model recognized for its high data efficiency, meaning it can learn to master complex tasks using far fewer examples than traditional models. It is used in the discussion to illustrate the potential for AI to learn more effectively by practicing against its own internal simulations.

## Transcript

[00:00] **Dwarkesh Patel**
So, here's the big research bet that all the labs are making. They think that if we train AIs to accomplish millions of verifiable tasks across thousands of diverse RL environments, then we will have basically built AGI. Because this kind of training will have created a kind of problem-solving agent, the kind of thing that can make progress on open-ended tasks for weeks on end in the face of errors and mistakes and ambiguity. And the people who are optimistic about this vision will say that all these things that we talk about as the fundamental deficits in the current training paradigm, for example, the data inefficiency of these models or the fact that they lack continual learning, these things can just be steamrolled if we just scale training more. And the same way that all the fundamental research problems in natural language processing collapsed when we just threw enough compute into LLMs. So, in the previous essay, I talked about how these models are one one millionth as sample efficient as humans.

[00:55] **Dwarkesh Patel**
And the people who are in favor of the current training paradigm will say, look, that might be true, but this is only true during training. And training is this one-time cost that is amortized across billions of sessions that a model will experience. And what really matters is how smart and general and sample efficient the model is during a session. And this has clearly been improving as we've been doing more RL training. AI agents are able to solve more and more ambitious problems over longer and longer time spans. Anybody who has used these models for coding knows that. Similarly, people would say, look, continual learning, this capability I keep harping about where the model's weights get updated based on what it's learning from deployment, may simply not be necessary. Because if in-context learning gets so good across longer and longer time horizons, then you don't need to distill back everything the model is learning on the job into the weights. People often say that their employees are not net productive until six months or more of them working on the job.

[01:52] **Dwarkesh Patel**
So clearly online learning is necessary for competence. But what if you could just fit those six months into the context window? There's been tons of architectural innovations that dramatically increase the amount of information or the amount of context that a transformer can store. And why not think with a couple more years of progress, you might have what feels like infinitely large context windows. Okay, so before we discuss this research a bit further, I want to step back and I want to ask a completely tangential question, which I find actually very interesting and confusing about the nature of current AI progress. Why has progress on computer use been so much slower than other domains? Computer use is so clearly verifiable. You could ask a question like, did the desired Etsy item I ordered get delivered? Is the venue for an event I'm trying to organize booked? Have my taxes been submitted? So isn't it weird that computer use has been making so much slower progress than coding and math and these other verifiable domains? I'm sure there's many reasons for this.

[02:51] **Dwarkesh Patel**
And one of them, of course, is the fact that the models are exposed to far less high quality multimodal data during pre-training. But one reason that I think is actually quite underrated by people and which I think reveals the canyon walls against which this river of AI progress will only slowly chip away at is that It is not enough for a domain to be verifiable. It also has to be very grindable, in the sense that you have to be able to run lots of parallel rollouts against a deterministic and replayable simulator. And you have to run those rollouts from the same starting point. If you're trying to make a model better at coding, you can define some container that has the software repo with a missing feature that you have tasked the AIs with creating. And then you have a thousand parallel agents that go at the problem, each of which has an identical copy of the container. But this doesn't work with computer use, at least not trivially. You can't just have a thousand agents go try the same checkout flow on Amazon to get better at using websites because Andy Jassy will find your bots and shut your ass down.

[03:50] **Dwarkesh Patel**
You can solve this by making clones of Slack and Gmail and all the other common applications and websites. But at least currently, this is a very labor intensive and unscalable way to build environments. Of course, once AIs get good enough at coding themselves to build these clones with extremely high fidelity, then I'm sure the computer use will make quicker progress than it is right now. And you're also killing two birds with one stone with this kind of procedure because getting AIs to rebuild whole applications from scratch is also a great RL objective for coding. So while computer use itself may soon be solved, its current lethargy is telling us the following, that unless you can build a very replayable training target for a domain, the models will struggle to make much progress. And the reason this is true, of course, the models are incredibly sample inefficient during training. This is a point I was making in my last video essay. So for computer use, we might be able to make up for the sample efficiency deficit by building these formidable deterministic simulators.

[04:46] **Dwarkesh Patel**
But for so many other different kinds of skills that we need AIs to have, we simply can't do this. How do we train an AI to get really good at building a business from scratch? How about winning court cases or having a profitable day of trading in the markets or helping a candidate win an election? The rollout here requires interacting with the real world, and you can't recreate it from just within the datacenter. The outer loop verification here may take months or even years of real-world actions to elicit, and you can't re-observe it by perturbing the model's actions slightly in thousands of parallel rollouts to isolate exactly what the model did that actually worked. Now, dealing with such reset-free, non-stationary environments is a known open problem in RL. I'm not pointing out anything new. But I really do want to emphasize that because of the idiosyncratic and sparse nature of data in most domains in the world, you need sample efficiency in order to get proficient.

[05:40] **Dwarkesh Patel**
If AIs are to develop all the skills that humans have, And even skills that humans don't have, that they need to be able to learn from information revealed in unstructured, unverifiable and ambiguous ways from scarce amounts of real-world interaction. Because in many domains, the relevant training information simply doesn't exist in any other way. What is the RL environment to make an AI that is as good at politics as Lyndon Johnson or as good at building a space launcher business as Elon Musk? The labs are betting that RLVR will generalize. That is that if you train on enough containerized reproducible environments, you will develop a very general agent that can make and execute plans and learn rapidly from new information and even pick up new skills all within a single session. If you dropped this endlessly RLVR'd AI into Texas politics in 1948, it could give you better advice than LBJ about winning the Senate seat. And if you gave it $100 million in 2002 and let it cook, it would build SpaceX for you.

[06:39] **Dwarkesh Patel**
Now whether RLVR can generalize this well is an empirical question. If the labs went from spending billions of dollars on RL environments to a trillion dollars, would you get the kind of thing that is a fully human-like general intelligence within the context window? Dario gave a telling quote during our podcast together, which I think hints that RLV, our generalization is not infinitely strong, but he was explaining why model performance tends to degrade at long context. He said, there's two things. There's the context length you train at, and there's a context length that you serve at. If you train at a small context length and then try to serve at a long context length, like maybe you get these degradations. Now, maybe I'm reading too much into this, but it seems like he's saying that short horizon RL training doesn't necessarily generalize to long horizon RL performance.

[07:25] **Dwarkesh Patel**
And if you can't generalize from short horizon to long horizon, then how are agents supposed to generalize from getting trained at a bunch of white-collar tasks to, say, having the ability to be dropped in the real world and build a business from scratch as well as Sam Walton? And even if after enough in-context experience, the AIs can become like Henry Ford or Albert Einstein, all that would be ephemeral and wasted if you couldn't get those learnings back into the weights. Around 30 to 50 percent of a lab's compute goes to inference. And that compute is currently not playing any productive role in helping improve the model. This is a huge waste. And it's even worse than it sounds because it is only in deployment that the most valuable bits of information which your model could learn from are actually revealed. Things like what's actually happening in the organizations where I'm being used? And what are they using me for? And what kinds of mistakes do I tend to make in the real world? We've got some genius grad student who's never been allowed to take a real internship. And we keep giving it more and more classroom case studies in the form of RL training on environments.

[08:25] **Dwarkesh Patel**
It's so bizarre that we have AIs that are broadly deployed through the economy already and are participating in so many different kinds of tasks and are privy to so much domain and organization specific tacit knowledge. And they're not able to make use of it. But this kind of continual learning requires going back to the weights. AIs can't just keep building up a bigger and bigger KV cache as they learn from more and more users. That's just not scalable. And that's also not how humans do it. There's no clean separation in our brain between parameters and activations. And it's not like some part of your skull keeps expanding as you learn more things through your lifetime. When we learn stuff, there's clearly some kind of compression. And this aids our generalization and rocking. There are, in fact, some humans who have this autistic savant type ability to recall random tables of numbers or nonsense syllables years later. Basically, the kind of fidelity information that models have in context.

[09:23] **Dwarkesh Patel**
And such sheer volume cripples these humans' ability to understand abstractions and metaphors. Human continual learning is less about having all your observations at the tip of your tongue and more about chiseling the right intuitions and big picture knowledge back into the weights. But the moment you move into the weights, you have to give up on in-context learning sample efficiency. Because gradient updates are super sample inefficient, all of the successfully shipped online learning models have had to learn the exact same thing across millions of users. For example, the cursor tab model online learns by predicting the same exact objective for over 400 million requests a day. The objective here being which edits actually got accepted by the user. At least so far, we haven't seen models online learn different kinds of things for different users. Because while a single session may generate more than enough data for a human to learn from, it's not enough to train a more capable AI. Current online learning can work for a very limited number of use cases.

[10:22] **Dwarkesh Patel**
But the whole point of continual learning is that the world is very complicated. And each job and company and problem is different. And you need your intelligence to be able to learn the specific information related to a particular deployment, which simply can't be stuffed into some shared training run. These are all the things we're talking about when we talk about on-the-job learning. Things like how does everything in your organization work and fit together and how to cooperate with all the infrastructure and the other people around you to make progress on some larger project and what the common failure modes are and many other things like this. As the podcast has grown, I've had to deal with more and more operational overhead. Take paying bills. In the past, contractors would just email me their invoices. Every few weeks, I'd dig through my inbox, I'd create a folder with all the bills, and I'd manually pay each one. At this point though, I just give everybody an email address that goes straight to Mercury, which is my banking platform.

[11:17] **Dwarkesh Patel**
Whenever anybody sends an invoice to that address, Mercury automatically downloads it, scans it, and extracts all the relevant information. Things like the contractor name, address, payment amount, invoice number, and due date, and then uses all of this to create a draft payment. Mercury then stores a list of these drafts for me to review. I just go through this list and double check that I've been billed correctly. I don't have to track anything or enter any information myself. Mercury does all the fundamental things for your business extremely well and it puts them all in one place. If you want to learn more, go to mercury.com. Mercury is a fintech company, not an FDIC insured bank. Banking services provided through Choice Financial Group and Column NA members FDIC. In this way, sample efficiency and continual learning are actually deeply connected problems. Relatively little data is available to the model on the job. Now, to learn from this data requires sample efficiency.

[12:10] **Dwarkesh Patel**
Models can do that in context, but using the fast weights that are built on the fly by attention, which allows for the sample efficiency, but scales very poorly in terms of memory. We need architectural innovations that allow for some intermediate representation. I talked before about how we already have many different working ideas for this kind of thing, from sparse attention to KV cache compaction. And every week somebody releases a new paper suggesting some kind of other architectural optimization. It doesn't seem to me that architecture is fundamentally what is bottlenecking continual learning. So perhaps the bottleneck is the loss function. How do we update the weights, a.k.a. how do we improve the model itself based on information that was learned from one particular session? Even here, naively, it seems like there are many ideas that ought to work. A lot of people are talking about this technique called on-policy self-distillation recently. If you want to learn more about it, I recorded a little impromptu Blackboard lecture on my iPhone with Sasha Rush a couple of weeks ago, and it's in the link in the description.

[13:09] **Dwarkesh Patel**
But to summarize the explanation, the idea is that we encourage the base model to make the same predictions when trying to solve some real-world problem as the model with all the context accumulated after a long session would have made. The whole point of this procedure is to distill what the model learned in a session back into the weights themselves. This is better than RLVR for two reasons. One, OPSD doesn't require us to have some outer loop verifiable reward. We just need a model that can learn the right things within the context window. As long as we have that, we can train the base model to match our veteran teacher model, which has built up all this experience during the session. And two, OPSD provides a much denser supervision signal than naive RL. Instead of projecting a single reward through the whole trajectory, you can train on the per token probability discrepancy between the teacher and student. For continual learning, OPSD is also superior to supervised fine tuning.

[14:06] **Dwarkesh Patel**
The most naive version of SFT for this application that you can imagine is just to train the base model to predict all the tokens that are observed during this session. But this makes no sense if you think about it as a learning target. The way you get better at your job is not by recalling the transcript of every single thing that happened every day with perfect fidelity. Rather, it's by consolidating the handful of insights and pieces of knowledge that are actually relevant to you getting better at your job. RL training doesn't suffer from this failure mode. RL is great at concentrating the update to only what is relevant to getting the outcome right. That's why actually very few parameters are changed during an RL training step. And this is a very important property for continual learning because as you're learning on the job, you don't want to overwrite and forget all the other things that the base model knows. I wrote a post a few months earlier arguing that RL learns much less information per sample than supervised learning. But this may be a good thing rather than a bad thing.

[15:00] **Dwarkesh Patel**
You only change the model as much as is absolutely necessary to achieve the outcome and no more. OPSD preserves this property of supervised learning where instead of slingshotting towards the teacher distribution as supervised learning would have you do, you only extract the knowledge that is necessary for you to achieve the same results of the teacher on actual real-world tasks. OPSD is one way to attack the sample efficiency problem. You take this scarce real-world experience and you squeeze all the signal into a tiny well-targeted update. But there's also another much more speculative idea. Let's call it dreaming. If the AI can build a good simulation of reality against which to rehearse new skills or try alternative strategies and reinforce what actually works, then AIs could experience orders of magnitude more simulated samples in the same wall clock time. Let's go back in history a bit. A couple of years after DeepMind released AlphaZero, a group of researchers trained a model called EfficientZero.

[15:58] **Dwarkesh Patel**
And the whole point of this model is to be very efficient with data. So if this model and a human both got two hours to play against a simulator of an Atari game that they hadn't seen before, this model would actually probably beat the novice human. Does this mean that the model was more sample efficient than the humans? Well, that was the goal of the training, but it depends on how you measure sample efficiency. Because for each step in the real game, Efficient Zero is playing dozens of simulated games in its head. In a similar way, future LLMs might be able to consume far less real-world data while practicing endlessly against environments that they build for themselves. The big difference, of course, is that it will be much harder to build a simulation of the whole world than it is to emulate the game of Go. That's why I said this is a much more speculative idea. If it works, it would become a fourth axis of scaling alongside pre-training, RL, and inference time compute. You call it test time training or dreaming.

[16:53] **Dwarkesh Patel**
The model spends compute writing up RL environments and then training against them, and it's rehearsing all the skills that will actually be used in production for a specific user. So instead of hitting forward slash compact in Codex or Cursor or Claude, which kindles a small amount of compute to write up a summary, and which gives you the simulacrum of continual learning, you hit forward slash dream. And this incinerates huge amounts of compute to build and train against a video game version of what the model is witnessing in the real world. So what might continual learning look like by 2027 or 2028? And how do we get there? Here's one scenario. All of this RLVR training is producing an agent that can get its bearings when it's thrown at an unfamiliar problem, and it can try different strategies, and it can iterate when it hits a roadblock. This is the crucial thing that RLVR has given you. An AI that is at least competent enough to start getting some real-world experience if you could learn from it.

[17:50] **Dwarkesh Patel**
And once you have that, you send it out into the world to do real work, even on projects that are off the trading distribution. Now, let's say at this point, the effective context lengths have expanded such that AIs can jam and co-work with you for a full week of wall clock time. At the end of a week, you give it a thumbs up or a thumbs down, give it a work review. And if you give it a thumbs up, the base model distills everything that the AI learned during the session. And it may use OPSD, it may use dreaming, it may use some other technique that we aren't even aware of, or it'll use a combination of all of the above. And once it does so, the AI starts getting better at domains that are adjacent to what it was explicitly trained to beforehand with our LVR training. And in the next round after that, it can get better at things that are adjacent to what it had previously online learned. In this way, the gamut of AI skills and knowledge and capabilities can expand far beyond the verifiable domains that the model was originally trained against before it was deployed.

[18:48] **Dwarkesh Patel**
Just as pre-training created a base intelligence that was smart enough to become a competent agent with enough RLVR on top, so RLVR has created an agent that is competent enough to be actually broadly deployed in the world and from this broad deployment to learn on the job once the training recipe for continual learning actually arrives. By this point, the main way that AIs get better is not from the training they have received before they are released to the public. Rather, it's from all this experience that they'll be accumulating from being broadly deployed in the economy and engaging in so many different kinds of tasks. Every time that you interact with an AI, it'll be smarter. Not only because it's been learning from your previous sessions, but also because it's been learning from all its interactions with all the other users in the world. And that's very scary and exciting and different from the way that AI improves right now. This was a narration of a blog post that I also released on my website at dwarkesh.com.

[19:44] **Dwarkesh Patel**
Go there if you want to read all the footnotes or if you want to sign up so you can find out when I release the next blog post. Otherwise, I'll see you on the next episode.

---

# 中文翻译 (Chinese Translation)

---
podcast: "Dwarkesh Patel"
episode: "What does the next training paradigm look like?"
link: https://podwise.ai/dashboard/episodes/8317699
publish-time: "2026-06-26"
save-time: "2026-07-01"
---

# What does the next training paradigm look like?

## Summary

当前的人工智能研究范式依赖于可验证奖励的强化学习（RLVR）来构建能够解决多样化、可验证任务的通用代理。虽然计算能力的扩展在历史上推动了进展，但目前的模型在样本效率和持续学习方面面临重大的瓶颈。由于现实世界环境往往是不稳定的，并且缺乏确定性的模拟器，模型在从稀疏的、非结构化的数据中学习时遇到困难。为了克服这些限制，未来的进展可能依赖于像在线自蒸馏（OPSD）和 “梦境” 这样的技术，在这些技术中，模型生成自己的模拟环境来练习技能。通过将这些经验蒸馏回模型权重，人工智能系统可以从静态的、预训练的工具演变为在广泛经济部署中持续学习的代理，有效地将每次用户交互转化为智能的来源，而不仅仅依赖于预发布的训练。

Takeaways:
1. 当前全行业对 AGI 的赌注基于这样的假设：在多样的强化学习环境中对数百万个可验证任务进行模型训练将自然产生一个通用问题解决代理。
2. 计算机使用的进展落后于编码和数学，因为它缺乏 “可磨练” 的环境——确定性的、可重复的模拟器，允许数千个平行、相同的运行。
3. 达到人类水平的熟练度需要从稀疏、无结构和模糊的现实世界数据中学习的能力，目前的模型因在训练过程中极度样本效率低下而缺乏这种能力。
4. 虽然扩展上下文窗口可以让模型模拟能力，但它未能提供长期学习的可扩展解决方案，因为它没有将知识提炼到模型的权重中，导致显著的推理计算浪费。
5. 相较于强化学习，政策自蒸馏（OPSD）为持续学习提供了一条更优的路径，因为它提供了更密集的监督信号，并允许模型在不覆盖现有知识的情况下整合相关见解。
6. “梦境”——模型在自己的模拟环境中生成和排练——可能成为扩展的第四个轴，使模型能够比现实世界的交互更快地获得数个数量级的经验。
7. AI 能力的主要驱动因素最终将从预训练转向持续的在职学习，模型根据在广泛经济部署中遇到的隐性知识和具体失效模式来优化其权重。

## Chapters

### Chapter 1: RLVR 范式实现 AGI

当前 AI 实验室的研究趋势表明，在各种强化学习 (RL) 环境中对数百万个可验证任务进行模型训练，将有效地构建 AGI。这种方法旨在创建能够在面对模糊性时持续解决开放式任务的智能体。支持者认为，当前的限制，例如数据效率低和缺乏持续学习，可以通过扩大规模来克服。此外，随着上下文学习的改善，对传统基于权重的持续学习的需求可能会减少，因为模型可能会将几个月的工作经验直接适应到日益扩大的上下文窗口中。

### Chapter 2: 计算机使用中不可重放环境的瓶颈

计算机使用的进展落后于编码和数学等领域，因为缺乏一个 “可磨练” 的环境。有效的训练需要从相同起点运行数千个并行的、确定性的和可重放的演练，这在像亚马逊或 Gmail 这样的真实应用中很难实现。虽然构建高保真度的软件环境克隆是一个潜在解决方案，但这仍然需要大量人力。这种迟缓突显了一个基本真理：模型在训练目标无法轻易复制的领域中难以取得进展，这使得在复杂的现实场景中隔离成功行为变得困难。

### Chapter 3: 持续学习和权重更新的必要性

仅依靠上下文学习来处理复杂的长时间任务是不够的，因为它未能将知识提炼到模型的权重中。当前的推理时间计算在很大程度上被浪费，因为模型无法永久性地从部署期间获得的隐性知识中学习。与人类不同，人类能够将见解巩固到长期记忆中，而当前的 AI 模型则受限于其 KV 缓存的大小。在商业构建或政治等领域，真正的熟练程度要求能够根据稀疏的现实世界交互更新权重，而不是依赖于会话结束后消失的瞬时上下文信息。

### Chapter 4: 通过 OPSD 和梦境促进持续学习

在策略自蒸馏 (OPSD) 提供了一种优越的持续学习方法，通过鼓励基础模型匹配在会话过程中积累经验的老教师模型的性能。这提供了比幼稚强化学习更密集的监督信号，并避免了监督微调的陷阱，这通常导致对抄本的过拟合。此外，“梦境”——当模型在自身的内部模拟中构建和排练——可以作为放大的第四个轴。通过在自生成的环境中练习，模型可以获得数量级更多的经验，可能克服真实世界数据中固有的样本效率缺陷。

### Chapter 5: 人工智能自主部署的未来轨迹

AI 改进的未来在于广泛的经济部署，代理人在通过 OPSD、梦境和其他新兴技术的结合中实现现场学习。一旦代理人有足够的能力处理不熟悉的问题，就可以部署其进行实际工作。在获得积极反馈后，基础模型可以提炼在该会话中学到的教训，使其在与原始训练相邻的领域中得以提升。最终，AI 能力的主要推动力将从预训练转向从全球经济中广泛的现实世界交互中持续积累知识。

## Q&A

### Q1: 当前主要人工智能实验室在实现 AGI 上所做的主要 “研究押注” 是什么？
A1: 当前的主要策略是对数百万个可验证任务进行训练，涵盖数千个多样化的增强学习（RL）环境。假设是，通过迫使模型在开放式任务上长时间取得进展——同时处理错误和模糊性——我们将基本上构建出一个通用的问题解决代理。倡导者认为，当前的数据低效或缺乏持续学习等限制并不是根本障碍；它们可以通过扩大训练计算资源 “冲破”，就像大规模计算在自然语言处理中的解决许多核心问题一样。

### Q2: 为什么 “计算机使用” 的进展落后于编码或数学等其他领域？
A2: 虽然计算机使用是高度可验证的——你可以轻松检查税表是否已提交或物品是否已下单——但它缺乏 “磨练性”。要取得快速进展，你需要从同一个起点运行数千个并行的、确定性的、可重播的仿真。在编码中，你可以轻松启动一千个相同的容器来测试一个功能。你不能对像亚马逊这样的实时网站这样做，因为这些平台会封锁你的机器人。直到人工智能足够强大，可以构建这些应用程序的高保真克隆以供训练，计算机使用的进展将始终受到创建这些可重播环境的难度限制。

### Q3: “持续学习”——模型基于部署经验更新权重的能力——对 AGI 来说真的必要吗？
A3: 这里存在争论。有人认为，随着上下文学习变得越来越强大且上下文窗口有效增长到无限大，我们可能不需要将每一条教训提炼回模型的权重中。然而，我认为这是一个有限的观点。人类并不仅仅将每个经验保留在 “工作记忆” 中；我们将重要的见解整合到我们的长期直觉中。如果我们希望人工智能掌握复杂的现实任务——例如建立一个企业或驾驭政治——它们需要一种超越上下文学习并真实更新其基本参数以反映隐性、组织特定知识的方法。

### Q4: “策略自蒸馏”（OPSD）是什么，为什么它是持续学习的一个有前途的方法？
A4: OPSD 是一种技术，鼓励基础模型匹配其 “资深” 版本的预测，后者在一个会话中已经积累了上下文和经验。它优于简单的增强学习，因为它不需要外部奖励信号；你只需将资深模型用作老师。与监督微调相比，它也更优越，因为它不是迫使模型记住来自转录本的每一个单独标记，而是仅提取实现老师结果所需的知识。这允许进行密集、针对性的更新，改善模型而不覆盖其现有知识。

### Q5: 作为人工智能扩展潜在第四个轴的 “梦境” 概念是什么？
A5: “梦境” 是一个推测性想法，即人工智能可以构建自己的内部现实仿真，以排练技能和测试策略。如果人工智能能够生成自己的训练环境，它可以体验到数量级更多的 “练习”，而不是来自现实世界数据的学习。如果这项技术成功，它将成为一个与预训练、增强学习和推理时计算并行的新扩展轴。模型不仅依赖外部数据，而是花费计算能力 “梦见” 一个视频游戏版本的世界，从而使其在沙盒中提升能力，然后再将其应用到生产中。

### Q6: 为什么当前模型参数和激活之间的分离对人工智能发展构成瓶颈？
A6: 目前，实验室计算的很大一部分用于推理，这本质上是 “浪费的”，因为模型没有从这些交互中学习。人类在参数和激活之间没有明确的分离；我们通过经验将直觉雕刻进我们的 “权重”（大脑）中。如果我们继续仅依赖上下文学习，我们实际上是在运行一个 “天才研究生”，而不允许他参加真正的实习。我们需要架构或算法突破，允许模型将它们在现实世界中遇到的隐性知识重新整合回它们的权重中，而不仅仅依赖日益扩大的 KV 缓存。

### Q7: 到 2027 年或 2028 年，成功的持续学习未来是什么样子？
A7: 我设想一个周期，其中人工智能被部署进行实际工作，并在一周结束时收到用户的绩效评估。如果工作成功，基础模型会提炼出人工智能在该会话中学到的一切——也许使用 OPSD、梦境或其他技术的组合。这允许人工智能在与其原始训练相邻的领域中改进。随着时间的推移，人工智能变得更聪明的主要方式将不是预训练，而是它们从广泛部署在经济中所积累的大量经验。每次交互都将使模型更聪明，不仅仅是对于特定用户，而是对于整个系统。

## Highlights

1. [03:12] 仅仅能够验证一个领域是不够的。它还必须是可磨取的，意味着你必须能够在一个确定性和可重放的模拟器上进行并行的测试。
2. [08:53] 我们的大脑中并没有参数和激活之间的明确分隔。并不是你的头骨某部分在你一生中学习更多事物时不断扩展。
3. [14:16] 你提升工作能力的方式并不是完美地回忆起每一件事情的逐字记录。相反，是通过整合那些实际上与改善相关的少数见解和知识。
4. [19:22] 每次你与人工智能互动时，它会变得更加智能。它不仅从你之前的会话中学习，还从与全球每个其他用户的互动中学习。

## Keywords

1. **AGI (人工通用智能)**: 一种假设的人工智能形式，具有理解、学习和应用知识的能力，类似于人类。在文字记录中，它被描述为研究实验室通过在数百万种不同任务上训练代理人所追求的终极目标。
2. **RLVR (可验证奖励的强化学习)**: 一种培训方法，AI 代理人因在受控环境中成功完成特定、可衡量任务而获得奖励。文字记录将其标识为实验室用于构建能够处理复杂、开放性工作的解决问题代理人的主要策略。
3. **Transformer**: 一种神经网络架构，作为现代大型语言模型的基础。它被设计为按序列处理数据，使模型能够理解上下文和信息之间的关系。
4. **Context Window**: 模型在单次交互中可以 “看到” 或处理的总信息量或数据。文字记录建议，扩展此窗口是帮助模型处理复杂、长期任务的关键方式，而无需永久更新其内部记忆。
5. **Continual Learning**: AI 在初始培训阶段完成后，学习和适应新信息或环境的能力。文字记录认为，这对于 AI 在实时工作的环境中有效运作是至关重要的，因为这些环境的条件和要求不断变化。
6. **OPSD (政策内自我蒸馏)**: 一种技术，通过训练基础 AI 模型来模仿自己更有经验版本的行为，该版本已经完成了任务。通过将特定会话中获得的知识蒸馏回模型的核心记忆，使 AI 能够保留它学到的知识以供未来使用。
7. **AlphaZero**: 由 DeepMind 开发的强大 AI 系统，通过自我对弈学习掌握象棋和围棋等游戏，以超人水平进行游戏。文字记录提到它作为 AI 通过强化学习掌握复杂技能的基准。
8. **KV Cache**: AI 模型中的一个技术组件，存储先前计算的信息以加快新文本的生成。文字记录指出，尽管这对于短期表现很有用，但并不是模型存储或学习新永久知识的可扩展方式。
9. **EfficientZero**: 一种因高数据效率而闻名的 AI 模型，即它可以使用远少于传统模型的示例来学习掌握复杂任务。它在讨论中用于说明 AI 通过与自身内部模拟练习来更有效学习的潜力。

## Transcript

[00:00] **Dwarkesh Patel**
所以，这就是所有实验室正在进行的重大研究赌注。 他们认为，如果我们训练人工智能在成千上万种多样的强化学习环境中完成数百万个可验证的任务，那么我们基本上就建立了通用人工智能。 因为这种训练将创造出一种问题解决代理，可以在面对错误、失误和模糊性的情况下，持续数周在开放式任务上取得进展。 对于这一愿景持乐观态度的人会说，我们所谈论的当前训练范式中的基本缺陷，比如这些模型的数据效率低下或缺乏持续学习， 如果我们只是扩大训练规模，这些问题都可以迎刃而解。 就像我们在把足够的计算资源投入到大型语言模型时，所有自然语言处理中的基本研究问题一样崩溃。 所以，在之前的文章中，我谈到这些模型的样本效率仅为人类的百万分之一。 支持当前训练范式的人会说，你看，这可能是真的，但这只在训练过程中成立。

[01:01] **Dwarkesh Patel**
而训练是一次性的费用，这笔费用会摊销到模型经历的数十亿次会话中。 而真正重要的是模型在会话中有多聪明、多通用以及样本效率有多高。 随着我们进行更多的强化学习训练，这一点显然在不断改善。 人工智能代理能够在越来越长的时间跨度内解决越来越雄心勃勃的问题。 任何使用过这些模型进行编码的人都知道这一点。 同样，人们会说，持续学习，这种我一直在强调的能力，即模型的权重基于它在部署中所学的内容进行更新，可能根本不必要。 因为如果在越来越长的时间范围内，情境学习变得如此优秀，那么你就不需要将模型在工作中学习到的所有东西提炼回权重中。 人们经常说，他们的员工在工作六个月或更长时间之前并没有产生净生产力。 因此，显然在线学习对能力是必要的。 但如果你能将这六个月的时间装入上下文窗口呢？

[01:58] **Dwarkesh Patel**
已经有大量的架构创新极大地增加了变换器能够存储的信息或上下文的量。 为什么不考虑在未来几年取得更多进展，你可能会获得感觉上几乎无穷大的上下文窗口。 好的，那么在我们进一步讨论这项研究之前，我想退一步，问一个完全不相关的问题， 我发现这个问题其实非常有趣也令人困惑，关于当前人工智能进展的本质。 为什么计算机使用的进展比其他领域要慢得多？ 计算机使用显然是可以验证的。 你可以问这样的问题，比如，我订购的所需 Etsy 项目是不是已经交付？ 我正在组织的活动场地是否已被预定？ 我的税务是否已提交？ 所以计算机使用的进展比编码、数学或其他可验证领域慢得多，难道这不奇怪吗？ 我相信这背后有很多原因。

[02:51] **Dwarkesh Patel**
其中一个原因当然是模型在预训练期间接触到的高质量多模态数据远远少于其他领域。 但我认为一个被低估的原因是，领域仅仅可以验证是不够的。 它还必须非常可磨练，意味着你必须能够对确定性和可重放的模拟器运行大量的并行实验。 而且你必须从相同的起点运行这些实验。 如果你想让模型在编码方面变得更好，你可以定义一个包含缺失特性的软件下载库容器，任务是让人工智能创建这个特性。 然后你有一千个并行代理处理这个问题，每个代理都有一个相同的容器副本。 但这在计算机使用中并不好用，至少并不简单。 你不能仅让一千个代理尝试同样的亚马逊结账流程以提高网站使用能力，因为 Andy Jassy 会发现你的机器人并关闭它。

[03:50] **Dwarkesh Patel**
你可以通过制作 Slack、Gmail 和所有其他常见应用程序和网站的克隆来解决这个问题。 但至少目前，这是一种非常劳动密集且无法扩展的构建环境的方法。 当然，一旦人工智能在编码方面足够出色，能够以极高的忠实度构建这些克隆，我相信计算机使用的进展会比现在快得多。 而且通过这种程序你也可以一箭双雕，因为让人工智能从零开始重建整个应用程序也是一个很好的强化学习目标。 因此，虽然计算机使用本身可能很快就会被解决，但它目前的懒散告诉我们以下几点， 除非你能够为一个领域构建一个非常可重放的训练目标，否则模型将难以取得显著进展。 当然，这是真的，模型在训练期间的样本效率极其低下。 这是我在上一个视频文章中提出的观点。 因此，对于计算机使用，我们可能能够构建这些强大的确定性模拟器来弥补样本效率的不足。

[04:46] **Dwarkesh Patel**
但对于许多其他不同类型的技能，我们需要人工智能具备的技能，我们根本无法做到这一点。 我们如何训练一个人工智能，让它在从零开始建立一个商业方面变得非常优秀？ 如何赢得法庭案件、在市场中进行有利可图的交易或帮助候选人赢得选举？ 这里的实验需要与现实世界互动，而你不能仅通过数据中心内部的操作来重现现实世界。 这里的外部验证可能需要几个月甚至几年真实世界的行动来引出，而你无法通过轻微扰动模型的行为，在数千个并行实验中重新观察到它的实际有效操作。 现在，处理这样的无重置、非平稳环境是强化学习中的一个已知未解问题。 我并没有指出什么新东西。 但我确实想强调，由于世界上大多数领域数据的特异性和稀疏性，你需要样本效率才能变得熟练。

[05:40] **Dwarkesh Patel**
如果人工智能要发展出人类拥有的所有技能，甚至人类没有的技能，那么它们需要能够从不结构化、 不可验证和模糊的信息中学习，这些来自稀缺的真实世界互动。 因为在许多领域，相关的训练信息根本以任何其他方式不存在。 有什么强化学习环境可以让人工智能在政治上和林登·约翰逊一样出色，或者在构建航天发射器业务方面和埃隆·马斯克一样优秀？ 实验室正在押注强化学习虚拟现实（RLVR）会普遍适用。 也就是如果你在足够多的容器化可重现环境中进行训练，你将开发出一个非常通用的代理，能够制定和执行计划，迅速从新信息中学习，甚至在单个会话中掌握新技能。 如果你把这个无尽的 RLVR 人工智能投放到 1948 年德克萨斯州的政治中，它能给你比 LBJ 更好的赢得参议院席位的建议。 如果你在 2002 年给它一亿美元，然后让它发展，它将为你建立 SpaceX。

[06:39] **Dwarkesh Patel**
现在，RLVR 是否能够如此通用是一个经验性的问题。 如果实验室将花费从数十亿美元的 RL 环境增加到一万亿美元，你会得到那种能够在上下文窗口内具有人类般通用智能的东西吗？ 达里奥在我们一起的播客中给出了一个启发性的引用，我认为这暗示了 RLVR 的普遍性并不是无限强的，但他在解释为何模型性能在长上下文中往往会降低。 他说，有两点。 你训练时的上下文长度和你服务时的上下文长度。 如果你在小的上下文长度下进行训练，然后尝试在长上下文长度中提供服务，那么你可能会出现这些性能下降。 现在，也许我对此解读得过于深入，但似乎他在说，短期内的强化学习训练并不一定能推广到长期的强化学习表现。 如果你无法从短期到长期进行推广，那么代理又如何能从训练一堆白领任务中推广到， 比如，在现实世界中建立一门业务的能力，像山姆·沃尔顿那样？

[07:40] **Dwarkesh Patel**
即便在经过足够的情境经验后，人工智能可以变得像亨利·福特或阿尔伯特·爱因斯坦一样，所有这一切都是短暂的、浪费的，如果你无法将这些学习反馈回权重。 实验室的计算资源大约有 30% 到 50% 用于推理。 而这些计算资源目前并没有在帮助改进模型方面发挥任何生产性作用。 这是一个巨大的浪费。 而且情况比听起来还要糟糕，因为只有在部署中，模型可以学习到的最有价值的信息才会显露出来。 比如，我正在使用的组织中到底发生了什么？ 他们用我做什么？ 我在现实世界中往往会犯什么错误？ 我们有一个天才的研究生，他从未被允许参加真正的实习。 而我们持续给它越来越多的课堂案例研究，形式为在环境中进行的强化学习训练。 这太奇怪了，我们的人工智能已经广泛部署在经济中，参与许多不同类型的任务，并掌握了大量领域和组织特定的隐性知识。

[08:39] **Dwarkesh Patel**
但他们无法利用它。 但是这种持续学习需要回到权重上。 人工智能不能仅仅随着越来越多用户的学习而不断增加更大更大的 KV 缓存。 这根本不可扩展。 这也并不是人类的做法。 我们的大脑中参数和激活之间没有清晰的分离。 也不是说你的颅骨某部分会随着你一生中学习的内容而不断扩大。 当我们学习事物时，显然会有某种压缩。 这有助于我们的概括和摇摆。 事实上，有些人类拥有这种自闭症天才类型的能力，能够在多年后回忆起随机的数字表或无意义音节。 基本上，模型在上下文中具有的那种信息保真度。 这种庞大的信息量削弱了这些人类理解抽象和隐喻的能力。 人类的持续学习更关乎于将正确的直觉和宏观知识重新雕刻进权重中，而不是将所有观测放在舌尖上。

[09:38] **Dwarkesh Patel**
但一旦你进入权重，你就必须放弃上下文学习的样本效率。 因为梯度更新非常样本低效，所有成功推出的在线学习模型不得不在数百万用户之间学习完全相同的内容。 例如，光标标签模型在线学习的方式是对每天超过 4 亿个请求预测完全相同的目标。 这里的目标是哪些编辑实际上被用户接受。 至少到目前为止，我们还没有看到模型在线上学习到不同用户的不同内容。 因为虽然一个会话可能生成足够多的数据供人类学习，但这不足以训练出更具能力的人工智能。 目前在线学习只能适用于非常有限的用例。 但持续学习的意义在于世界非常复杂。 每个工作、公司和问题都是不同的。 你需要你的智能能够学习与特定部署相关的具体信息，而这根本无法被塞进某个共享训练环中。

[10:41] **Dwarkesh Patel**
当我们谈论在职学习时，所有这些都是我们所讨论的内容。 比如，如何让你在组织中的一切运作并相互配合，以及如何与周围的基础设施和其他人协作，以在更大项目上取得进展，以及常见的失败模式是什么等等。 随着播客的增长，我不得不处理越来越多的操作开销。 比如支付账单。 过去，承包商只需通过电子邮件将发票发送给我。 每隔几周，我会翻阅我的收件箱，创建一个包含所有账单的文件夹， 然后我会手动支付每一笔。 但目前，我只需给每个人一个直接发送到 Mercury（我的银行平台）的电子邮件地址。 只要有人将发票发送到该地址，Mercury 会自动下载、扫描并提取所有相关信息。 比如承包商的姓名、地址、付款金额、发票号码和到期日期，然后利用所有这些来创建草稿付款。 然后，Mercury 会存储这些草稿的清单供我审核。 我只需查看此清单并仔细检查我是否被正确计费。 我不需要跟踪任何东西或自己输入任何信息。

[11:39] **Dwarkesh Patel**
Mercury 对您的业务所有基本需求做得非常好，并且将它们放在一个地方。 如果您想了解更多，请访问 mercury.com。Mercury 是一家金融科技公司，而不是 FDIC 保险的银行。 银行服务由 Choice Financial Group 和 Column NA 成员 FDIC 提供。 通过这种方式，样本效率和持续学习实际上是深度关联的问题。 在工作中可用的数据相对较少。 现在，从这些数据中学习需要样本效率。 模型可以在上下文中做到这一点，但利用由注意力实时构建的快速权重，这允许样本效率，但在内存方面扩展非常差。 我们需要允许某种中间表示的架构创新。 我之前谈到过我们已经有许多有效的想法，这种事情，从稀疏注意力到 KV 缓存压缩。 每周都会有人发布新的论文，建议某种其他的架构优化。

[12:37] **Dwarkesh Patel**
在我看来，架构似乎并不是制约持续学习的根本瓶颈。 所以也许瓶颈在于损失函数。 我们该如何更新权重，换句话说，如何根据从某个特定会话学习到的信息来改进模型本身？ 即便在这里，简单来看，似乎存在许多理应有效的想法。 最近很多人在谈论一种叫做在政策自蒸馏（on-policy self-distillation）的技术。 如果您想了解更多，我几周前在我的 iPhone 上与 Sasha Rush 录制了一个即兴 Blackboard 讲座， 链接在描述中。 但为了总结一下解释，核心思想是我们鼓励基本模型在尝试解决某个现实世界的问题时做出与长期会话后所有上下文累积的模型相同的预测。 这个过程的整体目的就是将模型在会话中学到的内容提炼回到权重中。 出于两个原因，这是比 RLVR 更好的选择。 第一，OPSD 不需要我们有某种外部循环可验证奖励。

[13:36] **Dwarkesh Patel**
我们只需要一个可以在上下文窗口中学习正确内容的模型。 只要我们有这一点，我们就可以训练基本模型以匹配我们的资深教师模型，该模型在会话中积累了所有这些经验。 第二，OPSD 提供的监督信号比简单的强化学习要浓密得多。 你可以在教师和学生之间的每个 token 概率差异上进行训练，而不是在整个轨迹中投影一个单一的奖励。 对于持续学习，OPSD 也优于监督微调。 在这个应用中，你能想象的最简单的 SFT 版本就是训练基本模型去预测在这个会话中观察到的所有 tokens。 但如果你把它当作学习目标来考虑，这没有意义。 你在工作中变得更好的方式并不是完美地回忆起每天发生的每一件事的完整记录。 相反，是巩固那些与提升你的工作表现实际相关的少数见解和知识。 强化学习训练并不受此失败模式的影响。

[14:32] **Dwarkesh Patel**
强化学习非常善于将更新集中在仅与获得正确结果相关的内容上。 这就是为什么在强化学习训练步骤中实际上改变的参数非常少。 这一点对持续学习非常重要，因为在你在工作中学习时，你不希望覆盖并忘记基本模型所知道的所有其他内容。 几个月前，我写了一篇帖子，认为强化学习每个样本学习的信息比监督学习少得多。 但这可能是件好事，而不是坏事。 你只会改变模型到达结果绝对必要的程度，而不会超过。 OPSD 保留了监督学习的这一特性，即与监督学习会让你朝着教师分布猛冲不同，你只提取实现与教师在实际现实任务上取得相同结果所需的知识。 OPSD 是解决样本效率问题的一种方法。 你将这种稀缺的现实世界经验进行压榨，提炼出一个非常小的、目标明确的更新。

[15:31] **Dwarkesh Patel**
但还有另一种更加投机的想法。 我们称之为梦境。 如果人工智能能够构建一个良好的现实模拟，以便排练新技能或尝试替代策略，并强化真正有效的内容，那么人工智能在相同的实时中可以体验数量级更多的模拟样本。 让我们回顾一下历史。 在 DeepMind 发布 AlphaZero 的几年后，一组研究人员训练了一种叫做 EfficientZero 的模型。 这个模型的整个目的就是高效利用数据。 所以如果这个模型和一个人都有两个小时的时间对抗他们从未见过的 Atari 游戏的模拟器，这个模型实际上可能会击败那个新手人类。 这是否意味着模型比人类更有效地利用样本？ 好吧，那是训练的目标，但要看你如何衡量样本效率。 因为在真实游戏的每一步中，Efficient Zero 在脑海中进行数十场模拟游戏。 以类似的方式，未来的 LLM 可能在与它们自行构建的环境无休止地练习时，能够消耗更少的真实世界数据。

[16:34] **Dwarkesh Patel**
当然，最大的区别在于，构建整个世界的模拟将远比模拟围棋游戏困难得多。 这就是我说这是一个更具投机性的想法的原因。 如果它能行得通，它将成为旁边的预训练、强化学习和推理计算时间之外的第四个扩展维度。 你可以称之为测试时间训练或梦境训练。 模型花费计算能力来编写强化学习环境，然后针对它们进行训练，并排练在特定用户的生产中实际使用的所有技能。 所以，它不再是像在 Codex、Cursor 或 Claude 中按下斜杠紧凑，这会点燃少量计算能力来写一个摘要， 并且给你创造持续学习的模拟，而是按下斜杠梦境。 这会消耗大量计算能力来构建和训练一个视频游戏版本，反映模型在真实世界中所见的内容。 那么，到 2027 或 2028 年持续学习可能是什么样子？我们该如何实现？ 这里有一个场景。

[17:30] **Dwarkesh Patel**
所有这些 RLVR 训练正在培养一个能够在遇到不熟悉问题时找到方向的代理，它可以尝试不同的策略，在遇到障碍时进行迭代。 这是 RLVR 给你带来的关键点。 一个至少足够有能力开始获取一些真实世界经验的 AI，如果你能从中学习的话。 一旦你有了这个，你就可以将它送入世界进行真实的工作，甚至是一些不在交易分布上的项目。 现在，假设此时有效的上下文长度已经扩展，使得 AI 可以与你共同工作整整一周的实际时间。 一周结束时，你给它一个赞或踩，进行工作评估。 如果你给它赞，基础模型会提炼 AI 在期间学习到的所有内容。 它可能会使用 OPSD，可能会使用梦境，可能会使用一些我们尚未意识到的其他技术， 或者会使用以上所有技术的组合。 一旦这样做，AI 开始在与它之前通过我们的 LVR 训练明确训练的领域相邻的领域中变得更好。

[18:31] **Dwarkesh Patel**
在下一个回合之后，它可以在与以前在线学习的内容相邻的事物上变得更好。 以这种方式，AI 的技能、知识和能力的范围可以远远超出模型最初部署前经过验证的领域。 正如预训练创造了足够聪明的基础智能，使其能够成为一个合格的代理，而在此基础上又进行了足够的 RLVR 训练一样，RLVR 也创造了一个足够能胜任的代理，可以在世界范围内广泛部署，并从这种广泛部署中在实际工作中学习，等到连续学习的训练方案真正到来时。 到这个时候，人工智能变得更好的主要方式并不是它们在公开发布之前所接受的训练。 而是它们在经济中广泛部署并参与各种不同任务所积累的经验。 每次你与人工智能互动时，它都会变得更聪明。 不仅因为它从你之前的会话中学习，还因为它从与世界上所有其他用户的互动中学习。

[19:33] **Dwarkesh Patel**
这非常令人感到恐惧、兴奋，并且与目前人工智能的改进方式不同。 这是我在我的网站 dwarkesh.com 上发布的博客文章的一段叙述。如果你想阅读所有的脚注或者想注册以便了解我发布下一个博客文章的时间，可以去那里。 否则，我会在下一集见到你。
