---
podcast: "No Priors: AI, Machine Learning, Tech, & Startups"
episode: "Why Traditional Benchmarks Fail Modern AI Models with OpenAI Research Scientist Noam Brown"
link: https://podwise.ai/dashboard/episodes/8320330
publish-time: "2026-06-26"
save-time: "2026-07-01"
---

# Why Traditional Benchmarks Fail Modern AI Models with OpenAI Research Scientist Noam Brown

## Summary

Modern AI model evaluations fail to accurately reflect capabilities because they ignore the critical role of test-time compute. As models like 5.5 demonstrate, performance on complex reasoning tasks—such as solving mathematical conjectures—scales significantly with increased inference budgets, rendering static, one-size-fits-all benchmark grids obsolete. The industry currently operates in a suboptimal equilibrium, prioritizing standardized reporting over metrics that account for the cost or time invested in a response. Noam Brown, a pioneer in AI reasoning, emphasizes that as models become more capable, the primary bottleneck for both research breakthroughs and safety assessments is the lack of standardized, compute-aware evaluation frameworks. Future progress requires shifting toward plotting performance as a function of inference budget, ensuring that evaluations capture the true potential of frontier models rather than just their performance at arbitrary, low-cost settings.

Takeaways:
1. The industry is currently trapped in a suboptimal evaluation equilibrium by publishing static benchmark grids that fail to account for the variable amount of test-time compute used to achieve those results.
2. Modern AI models do not exhibit performance plateaus at short time horizons; instead, they can continue to improve over weeks of compute, necessitating a shift toward evaluating performance as a function of the inference budget.
3. A sudden, overnight intelligence explosion is unlikely because the most advanced model capabilities are bottlenecked by the significant time and compute resources required to unlock them.
4. Large-scale test-time compute allows models to solve complex mathematical problems, such as the Erdos unit distance conjecture, by using general-purpose scaffolding to explore promising paths at a fraction of the cost of traditional research methods.
5. AI models currently function most effectively as force multipliers for researchers—improving existing algorithms by orders of magnitude—rather than as autonomous agents capable of replacing the entire research and discovery cycle.
6. To accurately assess model progress, researchers should adopt a standardized evaluation framework that plots performance against an explicit x-axis of tokens, dollar cost, or time.
7. The transition from earlier models that frequently hallucinated or provided unreliable outputs to more recent iterations marks a significant improvement in zero-shot reasoning reliability, making them increasingly viable for high-stakes decision-making.

## Chapters

### [00:00] Chapter 1: Integrating Test-Time Compute into AI Evaluation Frameworks

Current AI evaluation policies and benchmark grids fail to account for test-time compute, which is a primary driver of model capability. While older models like GPT-3 showed limited improvement with increased compute, modern models exhibit significant performance gains when provided with more tokens or budget. Presenting benchmark results without controlling for the amount of thinking time leads to misleading comparisons. Effective evaluation requires either setting a fixed budget for benchmarks or plotting performance as a function of test-time compute. While long-running, multi-week thinking processes are possible, practical applications require flexible compute allocation that balances speed with depth of reasoning.

### [06:47] Chapter 2: Mitigating Benchmark Gaming through Private Evaluations

The industry faces a risk of "benchmark maxing," where models are optimized to score high on public tests through scaffolding or multiple-run selection rather than genuine capability improvements. To combat this, labs should prioritize held-out, private evaluation sets. Personal testing remains a critical, albeit informal, method for assessing model quality. For instance, using AI to build complex PokerBots serves as a robust evaluation because it requires deep reasoning, debugging, and optimization. While early models struggled with basic logic and "gaslighting," newer iterations demonstrate the ability to perform complex tasks with minimal human steering, approaching the level of a skilled research assistant.

### [11:26] Chapter 3: Challenges in Safety Testing and Long-Horizon Task Evaluation

Existing responsible scaling policies and preparedness frameworks were designed for an era where test-time compute was not a significant factor. These frameworks struggle to evaluate dangerous capabilities, such as bioweapon development, because a model's potential risk is now a function of the budget allocated to it. Furthermore, the rapid model release cycle—often every few months—conflicts with the time required to fully test models on long-horizon tasks. Evaluating an agent on a task that takes weeks or months to complete is currently impractical, yet it is the only way to truly understand the ceiling of a model's capabilities before public release.

### [17:14] Chapter 4: Unlocking Latent Capabilities and the Reality of Recursive Self-Improvement

Models already possess significant latent capabilities that remain under-explored due to the rapid pace of new releases. The successful disproof of the Erdos unit distance conjecture using an internal model demonstrates that even current-generation models can solve complex mathematical problems when properly scaffolded. However, the "wait for the next model" mentality can hinder progress, as researchers often prioritize scaling over pushing existing models to their limits. While recursive self-improvement is a dominant research goal, the necessity of large-scale test-time compute acts as a bottleneck, preventing an instantaneous "intelligence explosion" and ensuring that progress remains a gradual, time-dependent process.

### [26:50] Chapter 5: Future Frontiers in Multi-Agent Coordination and Practical Decision-Making

Future advancements in AI will likely center on multi-agent coordination, enabling models to share knowledge and build upon each other's work in a way that mimics human civilization's cumulative progress. Currently, models are limited by short context windows and a lack of persistent, global knowledge sharing. Despite intense competition between frontier labs, there is a shared recognition of the risks and potential of these technologies. For practical application, models have reached a level of reliability where they can be trusted for high-stakes decisions, such as tax or legal paperwork, often outperforming human experts. The path forward involves breaking the current "bad equilibrium" of benchmark reporting to foster more transparent and productive model evaluation.

## Q&A

### Q1 [Sarah Guo]: Why are the current benchmark grids used to evaluate AI models misleading?
A1 [Noam Brown]: The current benchmark grids are misleading because they fail to control for the amount of test-time compute used to generate a response. When a new model is released, it is often compared to previous versions on a static grid, but this ignores the fact that modern models can be configured to "think" for different durations. For instance, a model might appear to be only a marginal improvement over its predecessor on a standard benchmark, but once you control for the amount of compute or "thinking time" allocated, the performance jump is often substantial. We are currently in a "bad equilibrium" where everyone knows these grids are insufficient, but the industry continues to publish them out of habit and competitive pressure.

### Q2 [Sarah Guo]: How should the industry change its approach to evaluating model capabilities given that performance does not always plateau quickly?
A2 [Noam Brown]: We need to shift toward evaluating models by plotting performance as a function of the test-time compute budget. Instead of just running a benchmark once, we should either set a fixed budget—whether in tokens, cost, or time—or show how the model's accuracy scales as you increase that budget. For many complex tasks, performance does not asymptote for a very long time; it might continue to improve even after millions of tokens of computation. By explicitly plotting this relationship, we can make much more accurate comparisons between different models and understand their true potential.

### Q3 [Sarah Guo]: What is the "inconvenient truth" regarding current safety and preparedness frameworks?
A3 [Noam Brown]: The inconvenient truth is that most existing responsible scaling policies and preparedness frameworks were designed in the era of GPT-3, when test-time compute was not a significant variable. Back then, giving a model a $10 million budget didn't necessarily result in better performance than a $10 budget. Today, however, a model's capability is a direct function of the money and compute you invest in it. Current safety frameworks often ignore this, asking "what is the capability of the model?" without asking "at what budget?" This creates a blind spot because a model that seems safe at a low compute budget might exhibit dangerous capabilities—like the ability to design bioweapons—if it is allowed to run for a much longer, more expensive compute budget.

### Q4 [Sarah Guo]: How has the reasoning capability of models progressed over recent releases, using your work on PokerBots as a case study?
A4 [Noam Brown]: In earlier models, I had to do a lot of heavy lifting to create a "river solver" for poker, and the model would often "gaslight" me by providing incorrect, confident-sounding answers. It required constant, gentle steering, acting more like a junior student who needed significant guidance. By the time we reached the 5.5 model, the experience changed entirely; it could handle the task almost zero-shot. It has reached a level where it can optimize code significantly better than I can, in some cases making algorithms 10 to 100 times faster. We are approaching a point where a model could potentially solve a complex research problem, like my entire PhD thesis, in one go.

### Q5 [Sarah Guo]: Are we headed toward an "overnight intelligence explosion" where models suddenly become superhuman across the board?
A5 [Noam Brown]: I do not believe we are headed toward an overnight intelligence explosion, largely because of the reliance on large-scale test-time compute. Because these models require significant compute and time to unlock their most powerful reasoning capabilities, time itself becomes a bottleneck. You cannot simply have an instantaneous jump in intelligence if the process requires weeks of computation to achieve a breakthrough. We are seeing a gradual, intense acceleration, but the necessity of running these models for long horizons to reach their limits means that progress is constrained by the speed at which we can perform those computations.

### Q6 [Sarah Guo]: Why shouldn't researchers simply wait for the next model release rather than trying to push current models to their limits?
A6 [Noam Brown]: While it is tempting to wait for the next, more powerful model to make a task 100 times cheaper, there is immense value in experimenting with current models. A great example is the Erdos unit distance conjecture. We used an internal model to disprove it, not because we had a massive budget, but because we were curious and pushed the model to its limits. If people had explored the capabilities of the models we already had, they could have achieved these results much sooner. The focus should be on using current models to solve real problems and to build even more capable models, rather than just waiting on the sidelines.

### Q7 [Sarah Guo]: What are the fundamental limits of test-time compute?
A7 [Noam Brown]: Test-time compute is not a magic bullet for every type of problem. For factual retrieval tasks—like asking for a specific date in history—giving a model a week to think will not improve the outcome if it doesn't have the information. However, for reasoning-heavy tasks like Sudoku or complex mathematical proofs, more compute allows the model to explore strategies, verify constraints, and iterate until it finds a solution. The models are not yet at the point where they can replace human researchers entirely because they currently lack "research taste"—the ability to intuitively know which paths are worth pursuing and which are dead ends.

### Q8 [Sarah Guo]: How do you suggest the industry breaks the "bad equilibrium" of benchmark reporting?
A8 [Noam Brown]: The only way to break this is for companies to stop prioritizing the traditional benchmark grid as the top-line result. We need to normalize the inclusion of an x-axis in our evaluations—whether that is tokens, cost, or time—so that the community can see how models perform under different compute regimes. If a major lab decides to change how they present their data, it would force the rest of the industry to follow suit. We have to move toward a more transparent and productive way of evaluating models that reflects the reality of how they are actually used today.

## Highlights

1. [00:15] The capability of a model is a function of how much money you put into it. A model given a budget of $10,000 can do significantly more than one given a budget of $10.
2. [16:01] If you want to know what a model can do after running for a month, the only way to be fully sure is to run it for a month.
3. [26:39] Things can only go so fast because models need to run for long enough to do something powerful. Time itself becomes a bottleneck to what we can achieve.
4. [28:12] Humans are able to do more today than in caveman times because billions of humans have been thinking for a long time and building off each other's accumulated knowledge. We are not seeing that with AI models today.

## Keywords

1. **Test-time compute**: The amount of processing power or time an AI model uses while actively working to solve a specific problem. In the transcript, it is described as a critical factor in determining performance, as increasing this budget allows models to tackle significantly more complex tasks.
2. **Recursive self-improvement**: A theoretical process where an AI system is capable of modifying its own code or architecture to become more intelligent. The speaker discusses this as a gradual mechanism for future advancements rather than an immediate, overnight "intelligence explosion."
3. **Scaffolding**: A technique of wrapping an AI model in a structure or framework to guide its reasoning and help it complete complex, multi-step tasks. It allows the model to iterate and build on its own intermediate outputs to reach a final, more accurate goal.
4. **Erdos unit distance problem**: A famous mathematical conjecture that was recently disproved using an AI model. This serves as a key example of how modern AI can contribute to genuine scientific discovery when given appropriate guidance and sufficient compute resources.
5. **Benchmark maxing**: The practice of fine-tuning or scaffolding AI models specifically to achieve high scores on standardized tests. The speaker warns that this is often misleading, as it may not reflect a model's true capability or efficiency in practical, real-world scenarios.
6. **Inference budget**: The specific limit on resources, such as processing time, tokens, or financial cost, allocated for an AI to process a single request. The transcript argues that current industry evaluations are flawed because they fail to account for this budget when comparing different models.
7. **AISI (AI Safety Institute)**: An organization responsible for evaluating the safety and capabilities of advanced AI models. They conduct rigorous testing to determine if a model possesses dangerous capabilities, such as the ability to assist in the creation of biological weapons.
8. **Zero shot**: A capability where an AI model can perform a task or solve a problem without needing specific prior training examples or demonstrations. The speaker notes that newer, more advanced models have become significantly better at this compared to earlier, less capable versions.
9. **River solver**: A specific software component used in poker-playing AI to handle the final stage of a hand. It is mentioned as a practical example of how the speaker used AI to optimize complex algorithms and improve his own research productivity.

## Transcript

[00:00] **Noam Brown**
With GPT-3, you couldn't scale test-time compute. Like, if you gave it a budget of $10 million and said, OK, well, let's see what GPT-3 can do, it really can't do that much. The procurator's frameworks and responsible scaling policies, they don't really account for the amount of test-time compute. They just say, OK, well, what's the capability of the model? The problem is we're in a world now where The capability of the model is a function of how much money you put into it, basically. If you give it a budget of $10,000, it can do a lot more than what it can do with a budget of $10. Give it a budget of $10 million, it can do even more. At what budget should you evaluate these models? The policies that exist today don't really address that question.

[00:42] **Sarah Guo**
Hi, listeners. I'm Sarah Guo, and welcome back to No Priors. Today, I'm here with Noam Brown, one of our godfathers of AI reasoning. We talk about the broken state of evaluations, very large-scale test-time compute, how he thinks about recursive self-improvement, and what's next on the horizon for competition at the frontier. Welcome. Noam, I'm so excited to have you back.

[01:05] **Noam Brown**
That's great to be back, yeah.

[01:06] **Sarah Guo**
You are our first guest. I'm very proud of my taste in friends and researchers for the pod, given how important inference time scaling has become to the industry. You should be proud too, having actually pioneered it.

[01:21] **Noam Brown**
Played a part, yeah, among many others.

[01:24] **Sarah Guo**
You just wrote this essay that really resonated about large-scale test-time compute and why the industry is not evaluating these models as robustly as it should be. What was the motivation for it?

[01:37] **Noam Brown**
Yeah, the motivation was we released 5.5 and the initial reaction was I'm going to talk a little bit about how I came up with this model. I think a lot of people were kind of skepticism that it was a substantially better model. To be fair, that only lasted for a few hours before people had some time to play around with it and try it out themselves. And they saw that it was actually substantially better. But I think a lot of the skepticism came from the benchmark grid that was published. Basically, whenever a new model is released, there's this benchmark grid where they show all these different benchmarks on the x-axis and then the performance of different models on the y-axis. And you can just compare different models. And if you look on paper at the difference between 5.5 and 5.4 or other models, it was an improvement, but it wasn't a huge improvement. It was only a few percentage points in some benchmarks. So people looked at that and they were skeptical that it was actually a better model. Once they played around with it, the story changed.

[02:28] **Noam Brown**
I think the reason why it doesn't show up as so much better on the benchmarks is because the benchmarks are being presented, the benchmark results are being presented in the wrong way. They're not controlling for the amount of test-time compute that is being used on that benchmark question. It turned out that 5.5 is just much more efficient with its thinking. If you run it at max settings, 5.4 is thinking for a lot longer. It takes longer to get back a response than 5.5. And once you control for the amount of thinking time, actually you can see that 5.5 is a substantial jump over 5.4. That is, I think, people's day-to-day experience with it. And then when I mention this to people, the reaction, the typical question I get is like, okay, well, why not just have 5.5 think for as long as 5.4? And the question is like, well, how long should they think for? Typically the response I get is, well, until the performance plateaus. This is at some point where the performance on the benchmark is going to plateau and you just evaluate to that point. The thing is, the point at which it plateaus is actually really far out these days.

[03:23] **Noam Brown**
I mean, it's true in GPT-3 land back in 2022, the models couldn't really think productively for that long and so you could just run them until they plateau. It's not that far away. But what we're seeing today with the modern models is that 5.5 and other models can think for, if you scaffold them reasonably well, can think for weeks even before having performance plateau on some of these benchmarks. And so the point at which they plateau is simply too far out to reasonably test.

[03:52] **Sarah Guo**
We all need to actually reinforce either like a patience limit or a budget limit from a token perspective now, and that wasn't true a few years ago.

[04:00] **Noam Brown**
Exactly. And so my claim is the proper way to evaluate the models now is you either have some kind of budget for the benchmark, whether it's tokens or cost or time or whatever, or you plot the performance as a function of the amount of test-time compute that's going into the model. And then it becomes much more clear how to compare the performance between these different models.

[04:20] **Sarah Guo**
Given the model evaluation cycle and the fact that performance does not asymptote for many tasks over quite a long period of time, what do you do about that issue, the fact that some of the evals that you would want to run are both beyond the scope of budget or time that's reasonable given the current model release cycle?

[04:41] **Noam Brown**
I mean, I think for things like cyber, we've seen and actually the AISI in their evaluations has shown that the models continue to improve At 100 million tokens, if you run them for 100 million tokens, they're still improving at beyond that point. And that can take a very long time to run. But you also do see that like, the performance is, it's not just like a discontinuous jump. It's actually like you can see the slope of improvement over those 100 million tokens. And so you could probably We're going to do some kind of evaluation up to a certain budget and then just say, okay, well, this is what we project the performance to look like. And I think there hasn't been a lot of research on this yet. I actually think this would be a great paper to publish if there's any academics out there looking for something to research. Can you predict what the performance looks like at an inference budget of, let's say, $10,000? And we're only using inference budgets up to 10 or $100. So maybe an orthogonal question for you.

[05:37] **Sarah Guo**
Do you think users are systematically like not thinking long enough with their models about problems?

[05:42] **Noam Brown**
What do you mean by not thinking long enough?

[05:47] **Sarah Guo**
And I'm here to talk to you about how to build an agent or control the amount of test-time compute being used. There's what is done by the model itself, and there's what the user can do. Do you think that the industry is using test-time compute an optimal amount, way undershooting it, or it's a problem in the models where they just need to be able to do that thinking faster?

[06:08] **Noam Brown**
I think it depends on the problem. I think this idea that the models, you just let them think for a week or whatever, and then they respond, it sounds nice. And yes, the benchmarks look great, but it's not very practical when working. Because like, okay, you ask the model a question, and then you sit there for a week waiting for it to come back to you. I think what people have found most effective is to kind of like iterate quickly with the models. And so the thinking time, I think, needs to be flexible. When it makes sense to respond quickly to the user, it should respond quickly. And then when it makes sense to think for a long time and the user wants it to think for a long time, then it makes sense to think for a long time. I think people have been striking the right balance given what they have to deal with right now.

[06:47] **Sarah Guo**
How would you characterize, you know, there's a lot of talk about benchmark maxing and the ability to game different benchmarks. What would you characterize the like landscape of benchmarks as today? And then do you have like favorites that you think are more indicative of capability than others?

[07:03] **Noam Brown**
So the benchmark maxing thing is also motivation for writing the essay that I think it's really easy to show you can do much better than previous benchmarks or previous models on benchmarks by just, for example, scaffolding a bunch of models together. So if you say, okay, well, we're going to, instead of just running this model once, we're going to run it five times and take the best of the five responses or like ask a judge which one it thinks is best. Then you can get much higher scores than that model. And so it's really easy to make something that looks a lot better on paper, but is actually not better once you control for the amount of test-time compute. That is one thing that I'm worried about when it comes to benchmark maxing. I mean, it's a little misleading is the only concern that I have. And then as far as the benchmarks themselves, I think there is always a risk of just optimizing for the benchmark. And I've certainly encouraged my team, and I think at OpenAI, we're pretty good about not trying to optimize for specific benchmarks. But once you put out a benchmark, it's always at risk of just being optimized for.

[08:03] **Noam Brown**
And I think one way to address that is to keep held out private sets that isn't publicly available.

[08:10] **Sarah Guo**
The most popular fallback advice for figuring out if a model is significantly better or not is to just play with it for a while. Do you have anything more sophisticated than that that you suggest people do? Do you create your own set of new evaluations each time besides Private holdback at OpenAI?

[08:30] **Noam Brown**
I think everybody has their own set of questions that they like to ask the model whenever it comes out. For me, lately, it's been I use them to make PokerBots and see how good they can make a PokerBot. I think it's a nice eval because there is very little open source code for making PokerBots. And there's a lot of published papers on it, but you really have to reason through everything. It requires a lot of just And today we're going to talk about reasoning and iteration and like a lot of small gotchas that I can kind of I've already worked through myself so I can see where the models fail along the way. They've gotten really good at it now.

[09:04] **Sarah Guo**
Can you describe perhaps like with your Pokerbot creation, like how reasoning might have progressed in model releases for you guys over a few releases?

[09:15] **Noam Brown**
Yeah, when the early models were really bad at it, like they could not basically do anything. I was able to work with it to make a river solver. So that's like the final stage of poker and that itself was I thought really impressive and had to work with it a little bit but I was actually really impressed because I was able to make. And I think I would have done the River Solver probably about five times faster than I would have alone. There were a couple things that it got tripped up on. Blockers was always a big, big issue. But overall, like, you know, with a bit of gentle steering, it just kind of like, it kind of felt like a grad student where, okay, they would run into issues, but at least like I would know what those issues were and know how to fix it. I could just make suggestions and it would go off and then do it. Pretty quickly it would actually come back with something really good. And then especially the optimization I thought was very impressive.

[10:08] **Noam Brown**
It was able to make it like 10 times faster than what I was able to do because it was just able to optimize the code so well. The downsides with 5.2 is I felt like it was gaslighting me a lot. And I always had to be very careful checking it and making sure like, okay, is it actually doing what it said it did? Are there any things that are like glaring issues that it's not recognizing or just pretending aren't issues? I remember there was like one point where for one of the models, I was playing around with it, not 5.2. Kind of like as a unit test, I told it, okay, well, let's say I have $100 in the pot and I fold, how much am I losing? And the model said $92. And I was like, that's crazy. I have $100 in the pot and I just fold it. How do I not lose $100? And it said, oh, you know, it's 92. It's close to 100. It's fine. It's no big deal. And I was like, clearly this is a problem, right? So the models did have this problem where they would gaslight you a lot. But once we got to 5.5, I actually thought, It was way better. It was able to basically do it zero shot.

[11:08] **Noam Brown**
And in fact, I've been working on just doing a full scale poker solver. And it's basically able to do the whole thing with some gentle steering from me. And I wouldn't be surprised if, you know, six months or a year from now, the model is able to do zero shot an entire poker solver, basically my entire PhD thesis in one go.

[11:26] **Sarah Guo**
Let's talk about the larger implications of needing to evaluate these models relative to, let's say, speed of their reasoning or efficiency versus token volume or dollar budget or whatever your scaler is. Can you describe some of the larger implications in your essay, including around safety evaluations?

[11:49] **Noam Brown**
Yeah, the safety evaluations thing, it's a bit of an inconvenient truth thing where Okay, so I guess for background, a lot of the, all the labs have these things called either responsible scaling policies, preparedness frameworks, they go by various names. But the idea is that whenever a model is released, they go through a series of evaluations to measure, are there dangerous capabilities? Could these models do things that we wouldn't want a bad actor to do? And if the model isn't very capable, then it's no big deal. But if it is very capable, if it could be used, for example, to make bioweapons, then you want to put in mitigations against that. But the question is, okay, well, how do you evaluate whether the model is capable of that? And they have various protocols about how they do these valuations. But a lot of these frameworks were developed around the era of ChatGPT, either before or after, when test-time compute scaling was not really as much of a thing. And it made sense. With GPT-3, you couldn't scale test-time compute.

[12:45] **Noam Brown**
If you gave it a budget of $10 million and said, okay, well, let's see what GPT-3 can do, it really can't do that much. More than what you could do with like $10 or $1. The preparedness frameworks and responsible scaling policies, they don't really account for the amount of test-time compute. They just say, okay, well, what's the capability of the model? The problem is we're in a world now where the capability of the model is a function of how much money you put into it, basically. If you give it a budget of $10,000, it can do a lot more than what it can do with a budget of $10. If you give it a budget of $10 million, it can do even more. And so at what budget should you evaluate these models? The policies that exist today don't really address that question. Some do, some do better than others, but for the most part, this is not really a factor that's being heavily considered. Now, whether it should be released anyway, I don't want to wade into this question.

[13:35] **Noam Brown**
I think there's, you know, there's arguments on both sides, but I think the important thing to recognize is that this is a question that is not being, we're just kind of like, you know, pretending that this issue doesn't exist. And I think it's important to just, you know, one way or the other, account for it.

[13:50] **Sarah Guo**
Yeah, it was the mirror image of the capability question of if the models can continue to do more and more without asymptoting on some tasks at very large budgets. Then they should also be able to do so for tasks we don't want them to do as a society, right? And so testing for that and what budget is allocated, it also seems out of sync from the model release cycle itself, right? There's been this acceleration of, you know, you get a new model every sometimes few days and weeks at this point versus six months. And you have a line in the essay where you say, like, the only way to truly evaluate an agent on some very long-running task might be to run it for a year. And that's going to be true of both, like, useful and negative tasks, right? And so how do you think about that versus the model release cycle?

[14:44] **Noam Brown**
Yeah, this is also an interesting dynamic where Basically, as the models have become stronger, they're better able to operate over longer horizons. So again, with GPT-3, if you wanted to run it for a week, there's really not much you could do to scaffold it into something useful that could actually run for a week. But we're seeing now with the most recent models that you can actually scaffold, for example, 5.5 into doing a series of experiments that can run for weeks, for months.

[15:13] **Sarah Guo**
Have you given your poker solver tasks like infinite budget yet?

[15:19] **Noam Brown**
I haven't really scaffolded something together where I just tell it like, okay, just run this for four weeks. I think I could probably give it slash goal and just like, yeah, tell it to go nuts. But I think at this point it could 100% do the river solver if I just give it a slash goal. I don't think it's at the level yet where it could do like the full poker solver if I gave it just slash goal and told it, yeah, go run for a month. But we're going to pretty soon be at that point where I probably could just tell it like, yeah, go work on this for a month and then come back to me with a full, complete poker solver that's state of the art. And the problem is, if you want to evaluate the capabilities of a model, what it can do after running for a month, the only way to be fully sure is to actually run it for a month. And if you want to know after six months, the only way to know fully is to run it for six months. I'll get to things we can do to address that a little bit later, but it's important to recognize that the model release cycle is...

[16:16] **Noam Brown**
Look, we're releasing new models every two or three months at this point. And so a model comes out, it takes two or three months to push it to its limits, and then you have another model come out. And so nobody actually knows what the ceiling of capabilities are for these models because nobody's actually run them for long enough to really tell. When SlashGoal came out, for example, I mean, people started running things that it took over a week for it to finish. And so people actually didn't realize that this was a big deal until after a week, until a week after it was released. I think that's going to be more and more true. You know, the implications of that are, I think, pretty interesting, because what do the labs do to like fully evaluate their models before the release? It's actually very difficult. Because yeah, you would have to The only way to really do the evaluations is then delay the model release cycle. And there's a lot of competitive pressure right now to not do that.

[17:06] **Sarah Guo**
Do you think there's exciting latent capability in the models that are already released that people have not fully explored given timeline?

[17:14] **Noam Brown**
I think absolutely. I think actually a really great example is the Erdos unit distance problem. So for the viewers that don't know, we used an internal model at OpenAI a few weeks ago to disprove the Erdos unit distance conjecture. Now, I'm not a mathematician, but this seems like it was a pretty big deal. In the math community, it was like the first problem that a lot of mathematicians had really spent a lot of time on, and the model was able to do something that they weren't able to do, and do it in a way that was actually interesting and useful for mathematicians. Honestly, it did it at a budget that was dirt cheap. I mean, we didn't put a lot of effort into this. We just, we tried a new model, and we were just curious what it could do, and we ran it through some problems. And this one, at a pretty low budget, it was like, oh yeah, I think I have a disproof. We were able to verify that, yeah, this proof is correct. After we announced the results, a bunch of people found that you could get the answer out of 5.5 as well. Now, it's not as simple as just asking 5.5, hey, here's the unit distance, what's the disk proof?

[18:14] **Noam Brown**
You had to scaffold it a bit. You had to like steer it a bit. And so somebody found, okay, you asked 5.5, list a bunch of ways that you could tackle this problem. And then it lists one of the paths that are actually promising to get to the disk proof. And then you tell it like, okay, explore this some more. And then if you do this enough times, it actually ends up arriving at the disk proof. What this means is you could, in principle, ask 5.5 to, you know, as a general purpose scaffold, list a bunch of different strategies, and then for each strategy, tell it to investigate that strategy, and then it would probably be able to arrive at the disk proof with a general purpose scaffold. Now, that scaffold would be very expensive. I mean, it would probably cost, I just ballpark like $1,000 to $100,000. But it would be possible and it would have been possible for somebody to disprove the Erdos-Renyin distance conjecture before we did using a general purpose model.

[19:10] **Noam Brown**
And nobody had explored sufficiently what happens if I put $100,000 worth of compute into 5.5. What could it do? And the answer is like, yeah, you probably could get stuff like that out of it.

[19:21] **Sarah Guo**
So people should be experimenting more with the current generation in terms of...

[19:24] **Noam Brown**
Well, this is I think is an interesting question of is it worth it to experiment with? Because again, the model release cycle is every couple months we put out a new model that's even more powerful. And so the cost of Disproving the Erdos unit distance conjecture drops by like 10 or 100x with every bottle release cycle, probably in some cases more.

[19:43] **Sarah Guo**
You've seen the meme that's like, oh, why bother doing any engineering work when I should just wait for the next bottle release?

[19:48] **Noam Brown**
Yeah, just go on vacation and come back two months later and then it's, you know, a thousand times cheaper.

[19:53] **Sarah Guo**
Do you agree with that? Is that what you're doing right now at OpenAI, just waiting for the next model release?

[19:58] **Noam Brown**
I think, I mean, I will say that we're in a period where progress is very fast. And like, yeah, the models are becoming more capable. I can say like at OpenAI, one of the things that we're not doing, and look, we have a lot of mathematicians, we have a lot of physicists, people are very excited about what these models can do right now, especially, you know, the internal models. We are trying to encourage people to not spend all their time just like Going through all the mathematical open problems, physics problems, and just pushing the models to their limits to see what they can prove or disprove because we really think the focus should be on how do we make even more capable models? How can we get them out safely to the world as quickly as possible so that all the scientists in the world can use these models to solve the problems themselves? So yeah, in some sense, we are thinking about this that yes, it's really tempting to just put all of our efforts into scaling up these models and see what they can do with their limits right now.

[20:48] **Noam Brown**
But really, the focus should be on how do we use these models to make even more powerful models, even more capable models that can do everything much more cost effectively.

[20:59] **Sarah Guo**
What is changing about the direction or allocation of resources for research in your mind, given your beliefs about the impact of very large-scale test-time compute? How does this interact with the idea of recursive self-improvement, for example, where it's a dominant idea for how you know, any lab gets to the best capability model?

[21:23] **Noam Brown**
So one thing I should clarify, I don't think we're at the point where, okay, you just give it an arbitrary, an extremely high inference budget, and it's just, it's just super intelligent across the board.

[21:32] **Sarah Guo**
Flash goal.

[21:33] **Noam Brown**
Yeah. Make GPT-7 or whatever and like, yeah, just go nuts.

[21:37] **Sarah Guo**
What's between us in there then?

[21:39] **Noam Brown**
I think having played around with the model, okay, so first of all, there are some benchmarks where the models will just not improve if they have more inference budget. So I think a lot of factual retrieval kind of questions fall into this category of if you ask a person, when was Abraham Lincoln born, and they don't know the date, they could sit there, they could think about it for a week. If they don't have access to Wikipedia or something, they're not gonna be able to do better answering that question if they thought about it for a week compared to five seconds. Same with the model. Actually, interestingly enough, if you give the model these kinds of factual retrieval questions and you give them a little bit of time to think, they do actually do better. But if you give them a week, they're not suddenly going to do better at remembering dates. So there are some benchmarks where they clearly improve with more test-time compute, and there's some where they don't. I think on the other extreme, there are benchmarks where they kind of obviously will keep improving without limit with more test-time compute. So the example I'd like to point to is Sudoku.

[22:40] **Noam Brown**
There's a really simple strategy to solving Sudoku, which is just try a bunch of different random numbers and then see if it fits the criteria, if it matches all the constraints. And if it doesn't, just try a different random combination of numbers. And clearly with enough time, you will be able to solve any pseudocomposal with this strategy. You can kind of trivially see like, okay, any model could keep doing better and better if it was just given more test-time compute. So you have, and all the benchmarks kind of exist somewhere between these two extremes. The models are not at the level where if you just give them enough test-time compute, they will be able to do All of our jobs, just because, yeah, there's some benchmarks where they will not improve. There are some things where they will not improve. One thing I see for research in particular is they don't have very good research taste right now. And so I think they're actually very good complements to researchers, especially, you know, I've found that I've found much more effective by using these models, but they're not able to fully replace the whole research cycle. Now, does that change with time? Probably.

[23:39] **Noam Brown**
I mean, I think the models are getting better across the board. Some things are getting better the faster than others. But They're not at the point where they're fully replacing researchers with just enough test-time compute.

[23:52] **Sarah Guo**
Can you give an example or two of like asking the model to do a research test or just like this is a terrible idea?

[23:59] **Noam Brown**
I mean, I think going back to my poker solver example, I was really impressed with the model's ability to optimize the algorithms that I had developed in my PhD. It was honestly, it was shocking to see how inefficient I was in retrospect, and they were able to make it like, you know, 10, 100x faster. And then I was like, okay, can you come up with an algorithm that is better Than the algorithms that I came up with or that anybody else came up with. Go ahead and like look at all the published work and synthesize that and then try to come up with something novel. And it's not able to do it. And I can give it a lot of time and it's still not able to do it. Now, it's possible that if I scaffolded something and like kind of constrain it a bit more that maybe it could eventually come up with something better. But it would take a lot of, it's not just as simple as saying, okay, please come up with a better algorithm.

[24:52] **Sarah Guo**
And how do you think that that gets improved?

[24:55] **Noam Brown**
What I've seen is with every model release cycle, it does get better at this sort of thing. It's still bad in my opinion, but it's not as bad as it used to be. And I wouldn't be surprised if at some point, same thing with coding, same thing with math, where there's just like this inflection point where suddenly it's actually good enough to be useful. I wouldn't be surprised if we encounter that point for research taste as well.

[25:18] **Sarah Guo**
In that, what do you, like, what is your framing of RSI today? Like, how should we think about it?

[25:23] **Noam Brown**
The models are definitely accelerating what researchers can do inside the labs. But I think they are accelerating some things and not other things. And currently, we're at the point where, okay, if something goes 100x faster, you get bottlenecked by the things that don't go 100x faster. Over time, the things that we're getting bottlenecked on are going to shrink. And there will be, I think, kind of a gradual takeoff in that respect. But it's more about transforming. Right now, it's more about transforming what researchers do rather than fully replacing the researchers.

[25:52] **Sarah Guo**
So that actually implies that you don't I think we're close to a very fast takeoff right now.

[25:58] **Noam Brown**
I think fast takeoff is relative. Things are moving very fast. But I think there is this hypothesis that you could have basically an overnight intelligence explosion where the models discover some kind of breakthrough to make themselves smarter. And then that leads to more breakthroughs that make themselves even smarter immediately. And you have basically in an instance, the models just You know, becoming very superhuman across the board in moments. And I don't think we're headed to that world, largely because of the fact that the models rely so much on large-scale test-time compute in order to achieve their greatest intelligence. If it requires so much test-time compute to unlock the full capabilities of the model, then that means you're bottlenecked by time. Things can only go so fast because the models need to run for long enough to actually do something really, really powerful. Time itself becomes a bottleneck to what we can do. And I think that is the case right now for a lot of the labs that ultimately I think the biggest bottleneck For all of us, it's time.

[26:57] **Noam Brown**
And that's why all the researchers are working so intensely right now. It's just so many hours per week are being put into this because we all see what the overhang is, we see what the capabilities are, and we're just bottlenecked by how quickly can we do things.

[27:10] **Sarah Guo**
What do you think is on the frontier that is less explored now? Like, we've talked about multi-agent before.

[27:17] **Noam Brown**
I think multi-agent is quite explored. I think...

[27:22] **Sarah Guo**
At sufficient scale?

[27:23] **Noam Brown**
I think there's a lot more that could be done. But it's also one of the things that's hard to do. A lot of research is hard to do with small scale. I think multi-agent in particular, it really requires, in order to fully unlock the capabilities, it requires like frontier models. I think we've seen some pretty interesting multi-agent scaffolds. I think they're able to do a lot, but I think it's really just scratching the surface of what it will be able to do. I mean, one way that I think about it is if you look at Human civilization, it's not that humans have become smarter over, it's not that they evolved to become smarter over, you know, the past 50,000 years. It's that humans are able to do a lot more today than they were back in caveman times because there have been billions of humans thinking for a long time and building off of each other's accumulated knowledge.

[28:12] **Sarah Guo**
We have very good retrieval and scaffolding versus 50,000 years ago.

[28:15] **Noam Brown**
I wouldn't even call it a scaffold. This is a very organic emergent property of just humans being able to accumulate knowledge, share it, and build off of it. We're not seeing that with AI models today. They're born into a world and they exist for a very short context window and then they just disappear. And yeah, there are things that you can kind of do to continue them, but it's very limited. I do think eventually we will, and we're starting to see signs that we're entering a world where they can coordinate on a large scale. I think Multbook and OpenClaw, when they first came out, I think it was obviously a bit overhyped, but they were An indication of where things could go in the future. And I do think that eventually we get to that kind of world.

[29:01] **Sarah Guo**
Of some sort of coordinated compounding state.

[29:04] **Noam Brown**
Yeah, the ability of the models to share knowledge on a more global level and be able to build on that knowledge productively.

[29:11] **Sarah Guo**
Given this set of beliefs and your work, how would you characterize just competition at the frontier between the between the three kingdoms if there is no overnight takeoff? It's just researchers grinding away, trying to make good high taste algorithmic and investment decisions about where to go, and then compute allocation, and then policy decisions, and eval decisions. It feels like slightly more grounded than I suppose like racing towards some immediate hard takeoff that nobody can catch you on.

[29:48] **Noam Brown**
I think the competition is very intense right now. I do think the models That exist today are accelerating what researchers at the Frontier Labs can do. There's obviously, like I said, limits to that right now, but the ability to use the models to improve the model research is a real thing and it's, it is like an amplifying force. I think that will continue to be true. I think they'll become more true over time. One thing that I am comforted by is I think all the researchers at the Frontier Labs, all the Frontier Labs I think recognize what is at stake and what these models like, what the risks are. And that's something that I find comforting that I think everybody really understands like, okay, this is a pretty serious thing and it can lead to really great things or it can lead to really bad things. And yes, there's a competitive dynamic between the labs, but like, We can also try to figure out how we all get to the positive outcomes rather than the very negative outcomes.

[30:43] **Sarah Guo**
I think, you know, I'd be remiss to ask, just because you have been right very early for a long time on the importance of test-time compute and reasoning as a framework, like, are there ways in which you use the models that you should, you would encourage others to, right? Is it just goal everything?

[31:03] **Noam Brown**
I think for a lot of people, they worked, I mean, this is probably not even true for your audience necessarily, but there's a lot of people that experimented with AI back in like 2023 and felt like they couldn't trust the outputs and then don't use it for really high stakes decisions. And actually, I think the models have progressed to a point where they are very good for these kinds of things. I mean, I asked them tax advice or I bought a condo recently and I was asking it for advice on like, okay, well, what's all the paperwork that I have to fill out and like, how do I What does it all mean? It's actually really good for these kinds of questions. So I use it day to day for a lot of this kind of stuff. And I think they're at a point now where And they've actually been at a point for a while now where I feel like I can just trust the outputs arguably more than I could trust the output from a human.

[31:49] **Sarah Guo**
An expert human.

[31:50] **Noam Brown**
Yeah.

[31:51] **Sarah Guo**
Okay. I have two final questions for you. One is, is there something you think that the rest of the research community doesn't agree with you on or doesn't understand the importance of quite yet?

[32:05] **Noam Brown**
This is such a good question. I wish I had time to think about this ahead of time.

[32:07] **Sarah Guo**
You can just hang out with me and think about it. Is it weird to be like consensus now? You're a bit salty three years ago when you're like, why don't people understand how important this is?

[32:15] **Noam Brown**
I still feel like it's not consensus though, because people still don't publish the benchmarks this way.

[32:21] **Sarah Guo**
That's true, yeah.

[32:23] **Noam Brown**
I think that's like inertia. Yeah, but that's kind of why I wrote the essay. I was just like, look, I mean, we can talk about this, but like, yeah, part of the motivation is like, I would talk to researchers about, it makes sense to show the benchmarks with an x-axis, whether it's tokens or cost or time, there should be an x-axis. And everybody would say like, yeah, that makes sense. We should do that.

[32:42] **Sarah Guo**
But they're not acting with the importance of like, good heart, like this is, we have to measure the correct thing.

[32:47] **Noam Brown**
Well, really, their response is, People expect us to publish the grid. And then, okay, well, why do people expect the grid to be published? Because everybody publishes the grid. And so you kind of end up in this bad equilibrium where everybody kind of knows that it's a bad equilibrium, but like nobody wants to break out. And I felt like, okay, well, if I just hopefully come out and say like, look, guys, let's all recognize that we're in a bad equilibrium and let's move to this different equilibrium where we're plotting things with an x-axis that hopefully that can Next time there's a model release, a company can feel comfortable not publishing the grid, at least not at the very front, the top line. We can have a more productive evaluation of these models.

[33:29] **Sarah Guo**
Then a last question for you. How do you think about companies across all of these specialized domains who feel the value that they have is essentially like the routing layer, the choice layer of my Goals composed of a bunch of discreet tasks some require more intelligence and last and within my my job as a vendor is to solve that problem or achieve the optimal outcome with. Taking into account the budget constraints and so i will manage like. The parallelization and how much inference to spend on it from what model? Because I think the Frontier Lab point of view is that that routing happens both within the You know, behind the API, behind the application, and then some of it in the model itself.

[34:25] **Sarah Guo**
And that's pieces of that are clearly being externalized in all these applications.

[34:30] **Noam Brown**
Yeah, I do think this is related to the fact that like benchmarks should be evaluated with an x-axis of tokens or cost. I have seen some evals recently that show like, okay, well, with a routing layer, you can achieve much better performance by Basically doing consensus among the models.

[34:46] **Sarah Guo**
Yeah.

[34:46] **Noam Brown**
And I definitely believe that if you do consensus among the models, they are going to achieve better performance than any individual model. But It's important to ask, are you going to do better than having that model basically think for longer? Once you control for the amount of test-time compute, is it actually still doing better? That's the question that you want to figure out.

[35:04] **Sarah Guo**
That's very principle of you, which is like, yes, routing is fine, but it's all subject to the same budget question. If you put it on the same scalar, then you can make an optimal decision and I think maybe I win.

[35:15] **Noam Brown**
I don't even know necessarily that I would believe that the routing does better. But then there's still a question of, is it going to do significantly better? Is it very fragile? Is it reflective of real world use cases compared to benchmarks? Because like one issue you could run into is that you could optimize for certain benchmarks with the routing and the show like, oh, yeah, we see there's big improvement on these benchmarks. But in real world use cases, it actually ends up not being a significant improvement. So I would say at the very least, like I would say, you want to control for test-time compute, and then you also want to have all the same skepticism about benchmarks that you would normally have.

[35:50] **Sarah Guo**
Awesome. Noam, thanks so much and for being on the mission for breaking us out of this false equilibrium.

[35:57] **Noam Brown**
Oh, it's great to be back.

[36:00] **Sarah Guo**
Find us on Twitter at NoPriorsPod. Subscribe to our YouTube channel if you want to see our faces. Follow the show on Apple Podcasts, Spotify, or wherever you listen. That way you get a new episode every week. And sign up for emails or find transcripts for every episode at no-priors.com.

---

# 中文翻译 (Chinese Translation)

---
podcast: "No Priors: AI, Machine Learning, Tech, & Startups"
episode: "Why Traditional Benchmarks Fail Modern AI Models with OpenAI Research Scientist Noam Brown"
link: https://podwise.ai/dashboard/episodes/8320330
publish-time: "2026-06-26"
save-time: "2026-07-01"
---

# Why Traditional Benchmarks Fail Modern AI Models with OpenAI Research Scientist Noam Brown

## Summary

现代人工智能模型评估无法准确反映能力，因为它们忽视了测试时计算的关键作用。随着像 5.5 这样的模型的出现，复杂推理任务的表现——例如解决数学猜想——随着推理预算的增加而显著提升，从而使静态的、千篇一律的基准网格变得过时。当前行业处于一种非最优的平衡状态，优先考虑标准化报告，而非考虑响应中投入的成本或时间的指标。人工智能推理的先驱诺姆·布朗强调，随着模型能力的提升，研究突破和安全评估的主要瓶颈是缺乏标准化的、考虑计算的评估框架。未来的进步需要转向绘制性能与推理预算的关系，确保评估能够捕捉前沿模型的真正潜力，而不仅仅是它们在任意低成本设置下的表现。

Takeaways:
1. 目前，行业正陷于一种次优评估均衡状态，因为发布的静态基准网格未能考虑为实现这些结果而使用的测试时间计算变量。
2. 现代 AI 模型在短期内并不表现出性能平台期；相反，它们可以在数周的计算中继续改进，这需要将性能评估为推断预算的函数。
3. 突如其来的智力爆炸不太可能发生，因为最先进的模型能力受到解锁所需的显著时间和计算资源的制约。
4. 大规模的测试时间计算使模型能够通过使用通用支架以传统研究方法不到一小部分的成本解决复杂的数学问题，例如厄尔多斯单位距离猜想。
5. 目前，AI 模型最有效的运作方式是作为研究人员的力量倍增器——将现有算法提高几个数量级——而非能够取代整个研究和发现周期的自主代理。
6. 为了准确评估模型进展，研究人员应采用一个标准化评估框架，绘制出性能与显式的 token、美元成本或时间的 x 轴。
7. 早期模型经常出现幻觉或提供不可靠输出的转变到更近期迭代标志着零样本推理可靠性的显著改善，使得它们在高风险决策中变得越来越可行。

## Chapters

### Chapter 1: 将测试时计算整合到人工智能评估框架中

当前的人工智能评估政策和基准网格未能考虑测试时计算，这是模型能力的主要驱动因素。虽然像 GPT-3 这样的老模型在计算增加时显示出有限的改进，但现代模型在提供更多标记或预算时表现出显著的性能提升。在未控制思维时间的情况下呈现基准结果，会导致误导性比较。有效的评估需要为基准测试设定固定预算，或将性能绘制为测试时计算的函数。虽然长期运行的、多周的思维过程是可能的，但实际应用需要灵活的计算分配，以在速度和推理深度之间取得平衡。

### Chapter 2: 通过私密评估减轻基准游戏的影响

行业面临 “基准极限” 的风险，即模型通过脚手架或多次运行选择来优化，在公共测试中获得高分，而不是通过真正的能力提升来实现。为此，实验室应优先考虑保留的私人评估集。个人测试仍然是评估模型质量的一个重要但非正式的方法。例如，使用人工智能构建复杂的德州扑克机器人是一个强有力的评估，因为它需要深度推理、调试和优化。虽然早期模型在基本逻辑和 “煤气灯效应” 方面存在困难，但更新版本展示了在最小人类指导下执行复杂任务的能力，达到了熟练研究助理的水平。

### Chapter 3: 安全测试和长时间任务评估中的挑战

现有的负责任扩展政策和准备框架是在测试时计算不是重要因素的时代设计的。这些框架在评估危险能力（如生物武器开发）方面困难重重，因为模型的潜在风险现在是其分配预算的函数。此外，快速的模型发布周期——通常是每几个月一次——与全面测试模型在长时间任务上所需的时间相矛盾。在一个任务上评估一个需要数周或数月才能完成的代理目前是不切实际的，但这是在公开发布之前真正了解模型能力上限的唯一方法。

### Chapter 4: 解锁潜在能力与递归自我改进的现实

模型已经拥有显著的潜在能力，但由于新版本发布的快速步伐，这些能力仍然未得到充分探索。利用内部模型成功驳斥厄尔多斯单位距离猜想表明，即使是当前一代模型，在适当的脚手架下也能解决复杂的数学问题。然而，“等待下一个模型” 的心态可能会阻碍进展，因为研究人员往往将扩展作为优先，而不是将现有模型推向极限。尽管递归自我改进是重要的研究目标，但大规模测试时计算的必要性充当了瓶颈，阻止了瞬间 “智能爆炸”，确保了进展仍然是一个渐进且依赖时间的过程。

### Chapter 5: 多智能体协调和实用决策的未来前沿

未来人工智能的发展可能将以多智能体协调为中心，使模型能够共享知识并在某种程度上模仿人类文明的累积进步。目前，模型受到短期上下文窗口和缺乏持久的全球知识共享的限制。尽管前沿实验室之间竞争激烈，但对于这些技术的风险和潜力有着共同的认识。在实际应用中，模型的可靠性已达到了可以信赖高风险决策（例如税务或法律文书）的水平，往往超过人类专家。前进的道路需要打破当前的不良平衡状态，以促进更透明和高效的模型评估。

## Q&A

### Q1: 当前用于评估 AI 模型的基准网格为何具有误导性？
A1: 当前的基准网格具有误导性，因为它们未能控制用于生成响应的测试时间计算量。当新模型发布时，它通常会在静态网格上与以前的版本进行比较，但这忽视了现代模型可以配置为在不同时间段内 “思考” 的事实。例如，一个模型在标准基准上可能看起来只比其前任有微弱的改进，但一旦控制了分配的计算量或 “思考时间”，性能的跃升通常是显著的。我们目前处于一种 “糟糕的均衡” 中，大家都知道这些网格是不够的，但行业仍因习惯和竞争压力而继续发布它们。

### Q2: 鉴于性能并不总是迅速趋于平稳，行业应该如何改变评估模型能力的方法？
A2: 我们需要转向通过将性能绘制为测试时间计算预算的函数来评估模型。我们不应该只运行一次基准，而是应该设定一个固定预算——无论是以 token、成本还是时间——或者展示当你增加预算时模型的准确度是如何变化的。对于许多复杂任务，性能不会在很长时间内趋于平稳；即使在计算了数百万 token 后，它仍可能继续改善。通过明确绘制这种关系，我们可以更准确地比较不同模型，并理解它们的真正潜力。

### Q3: 当前安全和准备框架的 “令人不悦的真相” 是什么？
A3: 令人不悦的真相是，大多数现有的负责任的扩展政策和准备框架是在 GPT-3 时代设计的，当时测试时间计算并不是一个显著的变量。那时，给一个模型设定 1000 万美元的预算并不一定会比设定 10 美元的预算产生更好的性能。然而，今天，模型的能力直接取决于你投入的金钱和计算量。当前的安全框架往往忽视这一点，询问 “模型的能力是什么？” 却不问 “在什么预算下？” 这造成了一个盲点，因为在较低的计算预算下看似安全的模型，允许其运行更长、更昂贵的计算预算时，可能会表现出危险的能力——例如设计生物武器的能力。

### Q4: 在最近的版本中，模型的推理能力如何进展，以你在 PokerBots 上的工作为案例研究？
A4: 在早期模型中，我不得不进行大量的重压以创建扑克的 “河牌解算器”，而模型经常通过提供错误且自信的答案来 “毒害” 我。它需要持续、温和的引导，表现得更像是一个需要重大指导的初级学生。当我们达到 5.5 模型时，体验完全改变；它几乎可以零样本处理任务。在某些情况下，它能比我更好地优化代码，使算法变得快 10 到 100 倍。我们正在接近一个点，模型有可能一次性解决复杂的研究问题，比如我的整个博士论文。

### Q5: 我们是朝着模型突然在各个方面变得超人类的 “瞬间智能爆炸” 前进吗？
A5: 我认为我们并不是朝着瞬间智能爆炸前进，主要是因为对大规模测试时间计算的依赖。因为这些模型需要显著的计算和时间才能解锁它们最强大的推理能力，时间本身就成为了瓶颈。如果过程需要数周的计算才能取得突破，你不可能简单地实现智能的瞬间飞跃。我们正在看到一种渐进的、激烈的加速，但为了达到模型的极限，长时间运行这些模型的必要性意味着进展受到我们执行这些计算速度的限制。

### Q6: 为什么研究人员不应该仅仅等待下一个模型发布，而是不尝试将当前模型推向极限？
A6: 虽然等待下一个更强大的模型使任务便宜 100 倍是令人心动的，但对当前模型进行实验具有巨大的价值。一個很好的例子是埃尔德斯单位距离猜想。我们使用一个内部模型来反驳它，并不是因为我们有巨额预算，而是因为我们出于好奇并推动模型到其极限。如果人们探讨我们已经拥有的模型的能力，他们本可以更早实现这些结果。重点应该是利用当前模型来解决实际问题，并构建更强大的模型，而不是仅仅在一旁等待。

### Q7: 测试时间计算的基本限制是什么？
A7: 测试时间计算并不是解决所有问题的灵丹妙药。对于事实检索任务——如询问历史上的特定日期——如果模型没有信息，给它一周的思考时间也不会改善结果。不过，对于像数独或复杂数学证明这样的推理密集型任务，更多的计算使模型能够探索策略、验证约束并迭代直至找到解决方案。模型尚未达到可以完全取代人类研究者的程度，因为它们目前缺乏 “研究品味”——直观地知道哪些路径值得追求，哪些是死胡同的能力。

### Q8: 你建议行业如何打破基准报告的 “坏均衡”？
A8: 打破这种局面的唯一方法是公司停止将传统基准网格作为首要结果。我们需要规范在评估中包含 x 轴——无论是 token、成本还是时间——以便社区可以看到模型在不同计算模式下的表现。如果一家主要实验室决定改变其数据呈现方式，这将迫使其他行业跟着改变。我们必须朝着一种更透明和更具生产力的方式评估模型，以反映它们今天实际使用的现实。

## Highlights

1. [00:15] 一个模型的能力取决于你投入了多少资金。一个预算为 10,000 美元的模型可以做的事情比一个预算为 10 美元的模型要多得多。
2. [16:01] 如果你想知道一个模型在运行一个月后的表现，唯一完全确定的方法就是运行一个月。
3. [26:39] 事情的进展速度有限，因为模型需要足够长的时间才能做出强大的成果。时间本身成为我们能够实现的瓶颈。
4. [28:12] 今天的人类能够做的事情比原始人时代要多，因为数十亿人已经思考了很长时间，并在彼此积累的知识基础上进行构建。我们在今天的人工智能模型中并没有看到这种现象。

## Keywords

1. **测试时间计算**: 人工智能模型在积极解决特定问题时所使用的处理能力或时间。在文本中，这被描述为决定性能的关键因素，因为增加这个预算允许模型处理更复杂的任务。
2. **递归自我改进**: 一种理论过程，其中人工智能系统能够修改自己的代码或架构以变得更智能。演讲者讨论了这作为一个逐步机制，用于未来的进步，而不是一个立刻发生的 “智能爆炸”。
3. **支架**: 一种将人工智能模型包裹在结构或框架中的技术，以指导其推理并帮助其完成复杂的多步骤任务。它允许模型迭代并基于自己的中间输出构建，以达到最终更准确的目标。
4. **厄尔多斯单位距离问题**: 一个著名的数学猜想，最近通过使用人工智能模型被驳斥。这作为一个关键例子，说明现代人工智能在得到适当的指导和足够的计算资源时可以为真正的科学发现做出贡献。
5. **基准最大化**: 专门对人工智能模型进行微调或支架以在标准化测试中获得高分的做法。演讲者警告说，这通常具有误导性，因为它可能并不反映模型在实际世界场景中的真实能力或效率。
6. **推理预算**: 分配给人工智能处理单个请求的资源特定限制，例如处理时间、标记或财务成本。文本认为目前行业评估存在缺陷，因为在比较不同模型时未能考虑这一预算。
7. **AISI（人工智能安全研究所）**: 一个负责评估高级人工智能模型的安全性和能力的组织。他们进行严格测试，以确定模型是否具备危险的能力，例如协助制造生物武器的能力。
8. **零样本**: 一种能力，人工智能模型可以在没有需要特定先前训练示例或演示的情况下执行任务或解决问题。演讲者指出，较新、更先进的模型在这方面比早期能力较弱的版本有了显著改善。
9. **河流求解器**: 一种用于扑克-playing AI 的特定软件组件，用于处理一手牌的最后阶段。它被提到作为一个实际例子，说明演讲者如何使用人工智能优化复杂算法，提高自己的研究生产力。

## Transcript

[00:00] **Noam Brown**
在 GPT-3 的情况下，你无法扩展测试时间的计算。 比如，如果你给它一个 1000 万美元的预算并说，好吧，让我们看看 GPT-3 能做到什么，它实际上做不了太多。 检察官的框架和负责任的扩展政策，实际上并没有考虑测试时间的计算量。 他们只是说，好吧，这个模型的能力是什么？ 问题在于，我们现在处于一个模型能力基本上是取决于你投入多少钱的世界。 如果你给它 1 万美元的预算，它能够做的事情比用 10 美元的预算要多得多。 给它 1000 万美元的预算，它能做的事情会更多。 你应该在什么预算下评估这些模型？ 现有的政策并没有真正解决这个问题。

[00:42] **Sarah Guo**
嗨，各位听众。 我是 Sarah Guo，欢迎回来收听《无先例》。 今天，我和 Noam Brown 在一起，他是我们人工智能推理的教父之一。 我们谈论评估的破碎状态、大规模测试时间计算、他如何看待递归自我改进，以及前沿竞争的下一个趋势。 欢迎。 Noam，我很高兴你能回来。

[01:05] **Noam Brown**
很高兴能回来，是的。

[01:06] **Sarah Guo**
你是我们的第一位嘉宾。 鉴于推理时间扩展对行业变得如此重要，我对我的朋友和研究者的品味感到非常自豪。 你也应该感到自豪，毕竟你实际开创了这方面。

[01:21] **Noam Brown**
参与了，是的，在许多其他人中。

[01:24] **Sarah Guo**
你刚刚写了这篇文章，关于大规模测试时间计算，以及为什么行业没有像它应该的那样评估这些模型。 这篇文章的动机是什么？

[01:37] **Noam Brown**
是的，动机是我们发布了 5.5，而最初的反应是我想谈谈我是如何想出这个模型的。 我觉得很多人对它是否是一个更好的模型持怀疑态度。 公平地说，这种怀疑只持续了几个小时，之后人们有时间去玩玩它，并自己尝试。 他们看到它实际上确实更好。 但我认为很多怀疑来自于发布的基准网格。 基本上，每当发布一个新模型时，都会有这个基准网格，其中显示了所有不同的基准在 x 轴上，然后不同模型的性能在 y 轴上。 你可以直接比较不同的模型。 如果你在纸面上查看 5.5 和 5.4 或其他模型之间的差异，虽然有所改善，但并不是巨大的改善。 在一些基准中，仅仅是几个百分点的提升。 所以人们看到这一点，怀疑它实际上是一个更好的模型。 一旦他们试着玩，它的故事就改变了。 我认为它在基准上没有表现得更好是因为基准在呈现时，基准结果的呈现方式是错误的。

[02:38] **Noam Brown**
他们没有控制在该基准问题上使用的测试时间计算量。 结果显示 5.5 的思考效率更高。 如果你以最大设置运行它，5.4 的思考时间会长得多。 它响应的时间比 5.5 更长。一旦你控制思考时间，实际上你会发现 5.5 相比 5.4 领先大幅。这是我认为的， 人们在日常使用中的体验。 当我提到这一点时，人们的反应，通常问的问题是，好的，那为什么不让 5.5 思考和 5.4 一样长呢？而我的问题是， 好吧，他们应该思考多长时间呢？ 通常我得到的回应是，好吧，直到性能达到平台期。 这是在某个时刻，基准的性能将达到平台期，你只需评估到那个点。 问题是，平台期实际上离现在的时间很远。 我是说，2022 年的 GPT-3 领域，模型实际上不能有效地思考那么长时间，所以你可以一直运行它们直到平台期。 这个时间并不远。

[03:33] **Noam Brown**
但我们今天看到的现代模型是，如果你合理地支架它们，5.5 和其他模型可以思考几周，甚至在某些基准上尚未达到性能的平台期。 因此，它们达到平台期的这一点实在是太远，无法合理测试。

[03:52] **Sarah Guo**
我们现在都需要从令牌的角度来强化耐心限制或预算限制，而几年前并不是这样。

[04:00] **Noam Brown**
完全正确。 所以我的观点是，现在评估模型的正确方式是，您要么有一些基准的预算，无论是代币、成本、时间还是其他， 要么您将性能绘制为投入模型的测试时间计算量的函数。 然后比较这些不同模型的性能就变得更加清晰了。

[04:20] **Sarah Guo**
鉴于模型评估周期以及许多任务的性能在相当长的时间内并不会趋于平稳，你对这个问题有什么看法， 也就是说，有些你想要运行的评估超出了预算或时间范围，而这些在当前模型发布周期内是合理的？

[04:41] **Noam Brown**
我是说，我认为像网络这样的事情，我们已经看到，实际上 AISI 在他们的评估中显示模型随着 1 亿个标记的使用而持续改进， 如果你运行它们达到 1 亿个标记，它们在那之后仍在改进。 这可能需要很长时间来运行。 但你也会看到，性能并不仅仅是一个不连续的跳跃。 事实上，你可以看到在这 1 亿个标记中的改进斜率。 所以你大概可以我们会进行某种评估，直到达到某个预算，然后就说，好的，这就是我们预计的性能。 我认为对此尚未进行很多研究。 我实际上认为如果有任何学术界的人在寻找研究课题，这将是发表的一篇好论文。 你能预测在 1 万美元的推理预算下性能会是什么样子吗？ 我们只使用高达 10 或 100 美元的推理预算。所以这可能是你们的一个正交问题。

[05:37] **Sarah Guo**
你认为用户在使用模型时系统性地没有深入思考问题吗？

[05:42] **Noam Brown**
你所说的 “没有深入思考” 是什么意思？

[05:47] **Sarah Guo**
我在这里是要和你谈谈如何构建一个代理或控制使用的测试时间计算量。 模型自身完成的和用户可以做的都是有区别的。 你认为行业在使用测试时间计算方面是最佳的，还是明显不足，或者是模型的问题，他们只是需要更快地进行思考？

[06:08] **Noam Brown**
我认为这取决于问题。 我认为这个想法，即模型，你只需让它们思考一周或更长时间，然后它们就会回应，这听起来不错。 是的，基准测试看起来很棒，但在实际工作中并不实用。 因为，比如说，你问模型一个问题，然后你就等了一周希望它能给你回复。 我认为人们发现最有效的方法是快速与模型迭代。 所以思考时间，我认为需要灵活。 当快速回应用户有意义时，它应该迅速回应。 而当需要花更长时间思考，并且用户希望它长时间思考时，那么长时间思考是有意义的。 我认为人们在目前所面临的挑战下找到了正确的平衡。

[06:47] **Sarah Guo**
你如何描述，你知道，现在有很多关于基准最大化和操控不同基准的讨论。 你如何描述今天基准的整体情况？ 你有认为哪些基准更能代表能力的偏好吗？

[07:03] **Noam Brown**
所以基准最大化的事情也是我写论文的动力，我认为这很容易证明，你可以通过把一堆模型组合在一起，比以前的基准或模型做得更好。 所以如果你说，好吧，我们不是只运行这个模型一次，而是运行五次，并选择五个响应中最好的那个，或者问评委他们认为哪个最好。 那你可以得到比那个模型高得多的分数。 因此，做一些在纸面上看起来更好的事情实际上变得非常容易，但一旦你控制测试时间的计算量，其实并不更好。 这是我在基准最大化方面担心的一件事。 我的意思是，稍微误导是我唯一担心的。 至于基准本身，我认为总是存在仅仅优化基准的风险。 我当然鼓励我的团队，我认为在 OpenAI，我们非常擅长不尝试优化特定基准。 但一旦你发布了基准，它总是有被优化的风险。

[08:03] **Noam Brown**
我认为解决这个问题的一种方法是保留非公开的私有数据集。

[08:10] **Sarah Guo**
了解一个模型是否显著更好的最流行备选建议就是玩一段时间。 你有没有更高级的建议让人们去做？ 除了 OpenAI 的私有保留之外，你是否每次都创建自己的一套新评估？

[08:30] **Noam Brown**
我认为每个人都有自己喜欢在模型出来时问的问题。 对我来说，最近，我用它们来创建扑克机器人，看看它们能做出多好的扑克机器人。 我认为这是一个不错的评估，因为几乎没有开源代码用来制作扑克机器人。 虽然有很多相关的论文，但你真的需要理清所有内容。 这需要很多时间，而今天我们将讨论推理和迭代以及许多小问题，我已经亲自解决过，因此我能看出模型在过程中失败的地方。 他们现在已经变得非常优秀了。

[09:04] **Sarah Guo**
你能描述一下你在扑克机器人创建中，推理在模型发布中是如何进步的吗？

[09:15] **Noam Brown**
是的，当早期模型在这方面表现很差时，他们基本上无法做到任何事情。 我能够与之合作制作出河牌解决器。 所以这就是扑克的最后阶段，我觉得那真的很令人印象深刻，我需要稍微调整一下，但实际上我真的很惊讶，因为我能够制作出来。 我认为我单独完成河牌解决器的速度可能会快五倍。 有几件事情让它感到困惑。 阻塞者一直是一个大问题。 但总体来说，你知道，在一些温和的引导下，它就像一个研究生，虽然他们会遇到问题， 但至少我会知道那些问题是什么，也知道如何解决它。 我可以只是提出建议，然后它就会去执行。 很快它就会带回来一些非常好的东西。 尤其是我觉得优化部分非常令人印象深刻。

[10:08] **Noam Brown**
它能够比我能做到的快大约 10 倍，因为它能很好地优化代码。 对于 5.2 的缺点，我觉得它经常在给我打心理战。 我总是需要非常小心地检查它，确保它确实在做它说的事情。 有没有什么明显的问题是它没有识别出来，或者仅仅是在装作没有问题？ 我记得有一次，对于其中一个模型，我在玩的时候，不是在 5.2。就像是作为单元测试，我告诉它，好吧，假设我在赌池里有 100 美元，我选择弃牌， 我到底损失了多少？ 模型说 92 美元。我当时想，这太疯狂了。 我在赌池里有 100 美元，我刚弃牌。 我怎么可能不损失 100 美元？它说，哦，你知道，92。接近 100，可以的。 没什么大不了。 我觉得这显然是个问题，对吧？ 所以这些模型确实存在心理战的问题。 但一旦到了 5.5，我觉得，效果好得多。 它基本上能够做到零样本。

[11:08] **Noam Brown**
事实上，我一直在努力做一个完整规模的扑克求解器。 基本上它可以在我的温和引导下完成整个事务。 如果你知道，六个月或一年后，这个模型能够零样本完成整个扑克求解器，我不会感到惊讶， 基本上是我整个博士论文一次性完成。

[11:26] **Sarah Guo**
我们来谈谈评估这些模型的更大意义，比如它们推理的速度或效率与代币量或预算的关系。 你能在你的文章中描述一些更大意义的事项吗，包括安全评估方面的内容？

[11:49] **Noam Brown**
是的，安全评估的事情，基本上是一个不太方便的真相，好的，作为背景，很多的， 所有实验室都有一些东西，称为负责的扩展政策、准备框架，它们有各种名字。 但是这个想法是，每当一个模型发布时，他们会进行一系列评估来衡量， 是否存在危险的能力？ 这些模型是否可能做出我们不希望坏人做的事情？ 如果模型的能力不强，那就没什么大不了的。 但如果它非常强大，例如可以用于制造生物武器，那么你就需要采取防范措施。 那么问题是，好的，你如何评估模型是否具备这种能力？ 他们有各种针对如何进行这些评估的协议。 但很多框架是在 ChatGPT 时代周围开发的，或是在测试时计算扩展并不算重要的时期。 这也很有道理。 对于 GPT-3，你无法扩展测试时的计算能力。 如果你给它 1000 万美元的预算，然后说，好吧，让我们看看 GPT-3 能做什么，它实际上做的事情并不多。

[12:51] **Noam Brown**
比起你用 10 美元或 1 美元能做的事情要少得多。准备框架和负责任的扩展政策，并没有真正考虑到测试时的计算量。 他们只是说，好吧，模型的能力是什么？ 问题是，我们现在处于一个模型的能力基本上是你投入多少资金的函数的世界。 如果你给它 10000 美元的预算，它能做的事情就比 10 美元预算时多得多。 如果你给它 1000 万美元的预算，它能做的事情就会更多。 那么在什么预算下你应该评估这些模型？ 现有的政策并没有真正解决这个问题。 一些解决了，有些做得比其他的好，但在大多数情况下，这并不是一个被高度考虑的因素。 现在，模型是否应该被发布，我不想掺和这个问题。 我认为两边都有论据，但我认为重要的是要认识到这是一个没有被， 我们只是在假装这个问题不存在。 我认为重要的是以某种方式来考虑这个问题。

[13:50] **Sarah Guo**
是的，这与模型是否能继续在非常高的预算下做越来越多事情的能力问题正好相反。 那么它们也应该能够在社会上我们不希望它们做的任务中做到这一点，对吧？ 所以测试这一点以及分配什么预算，似乎也与模型释放周期不太协调， 对吧？ 现在每隔几天或几周就会出一个新模型，而不是六个月出一个。 你在文章中有一句话提到，真正评估一个代理在某个长期任务上表现的唯一方法可能是运行一年。 这对于有用任务和负面任务都是正确的，对吧？ 那么你如何看待这个与模型释放周期的关系？

[14:44] **Noam Brown**
是的，这也是一个有趣的动态，因为基本上，随着模型变得更强大，它们能够在更长的时间内更好地运行。 所以再一次，对于 GPT-3，如果你想让它运行一周，实际上你很难把它构建成能够有效运行一周的有用事物。 但是我们现在看到最近的模型实际上可以将 5.5 进行构建，使其进行可以运行数周甚至数月的实验。

[15:13] **Sarah Guo**
你是否给你的扑克求解器任务设置了无限预算？

[15:19] **Noam Brown**
我还没有真的构建一个让我只告诉它，好的，运行这个四周的项目。 我想我可能可以给它 slash goal，并让它随意使用。 但我认为在这一点上，如果我只是给它一个 slash goal，它可以 100% 完成 river solver。 我认为它还没有达到足以在我给它 slash goal，告诉它去运行一个月的水平。 但我们很快就会达到那个点，我可能可以告诉它，好的，去为这个工作一个月，然后再给我一个完整的， 最先进的扑克求解器。 问题是，如果你想评估一个模型在运行一个月后的能力， 唯一完全确定的方法就是实际运行一个月。 如果你想在六个月后知道，唯一完全了解的方法就是运行六个月。 我会稍后谈谈我们可以做什么来解决这个问题，但重要的是要认识到模型释放周期是……看看，我们在这个时点每两到三个月就发布新模型。

[16:19] **Noam Brown**
所以一个模型发布出来后，需要两到三个月才能达到其极限，然后又会有另一个模型发布。 因此，没有人真正知道这些模型的能力上限是什么，因为没有人实际运行它们足够长的时间来真正判断。 以 SlashGoal 为例，人们开始运行需要超过一周才能完成的任务。 因此，人们直到一周后才意识到这是一个大问题，也就是在发布后一周。 我认为这将会越来越真实。 你知道，这一点的影响我认为非常有趣，因为实验室要如何在发布之前充分评估他们的模型？ 实际上是非常困难的。 因为，是的，你必须唯一真正进行评估的方法就是延迟模型发布周期。 现在有很多竞争压力不去这样做。

[17:06] **Sarah Guo**
你是否认为已经发布的模型中有令人兴奋的潜在能力，人们尚未充分探索给定的时间表？

[17:14] **Noam Brown**
我绝对认为是。 我认为一个非常好的例子是 Erdős 单位距离问题。 对于不知情的观众，我们几周前在 OpenAI 使用了一个内部模型来反驳 Erdős 单位距离猜想。 现在，我不是数学家，但这似乎是一个相当重要的事情。 在数学界，这就像是许多数学家花费大量时间的第一个问题，而模型能够做到他们无法做到的事情， 而且以一种对数学家真正有趣和有用的方式来实现。 说实话，它是在一个非常便宜的预算下完成的。 我的意思是，我们没有花很多精力在这个上面。 我们只是尝试了一个新的模型，出于好奇看看它能做什么，然后让它解决了一些问题。 而这一点，在相当低的预算下，就像哦，是的，我想我有一个反例。 我们能够验证，确实，这个证明是正确的。 在我们宣布结果后，一堆人发现你也可以从 5.5 得到答案。 现在，这并不像仅仅询问 5.5 那样简单，嘿，这里是单位距离，圆盘证明是什么？

[18:14] **Noam Brown**
你必须稍微搭建一下。 你必须稍微引导一下。 所以有人发现，好的，你问 5.5，列出一些可以解决这个问题的方法。 然后它列出了实际有希望到达圆盘证明的路径之一。 然后你告诉它，好吧，再深入探讨一下。 然后如果你这样做够多次，它实际上会到达圆盘证明。 这意味着，原则上你可以要求 5.5 作为通用支架，列出一堆不同的策略，然后针对每个策略，让它调查该策略， 然后它可能能够通过一个通用支架得出磁盘证明。 现在，这个脚手架会非常昂贵。 我的意思是，它可能需要大约 $1,000 到 $100,000。 但是有人在我们之前可能使用通用模型来反驳埃尔德什 - 雷尼距离猜想是有可能的。

[19:10] **Noam Brown**
而且没人充分探索过如果我投入价值 $100,000 的计算资源到 5.5，会发生什么。 答案是，是的，你可能能够从中得到这样的东西。

[19:21] **Sarah Guo**
所以人们应该更多地尝试当前这一代的模型，关于…

[19:24] **Noam Brown**
嗯，我认为这是一个有趣的问题，值得去尝试吗？ 因为再次强调，模型发布周期是每隔几个月我们发布一个更强大的新模型。 所以反驳埃尔德什单位距离猜想的成本会随着每次发布周期下降大约 10 或 100 倍，可能在某些情况下更多。

[19:43] **Sarah Guo**
你见过那个表情包吗，意思是，哦，为什么要费心去做任何工程工作，我只要等下一个发布就行？

[19:48] **Noam Brown**
是的，去度假，过两个月再回来，那时候就会便宜一千倍。

[19:53] **Sarah Guo**
你同意这样吗？ 这就是你在 OpenAI 现在所做的，等下一个模型发布？

[19:58] **Noam Brown**
我想说，我们正处于一个进展非常快的时期。 而且，是的，这些模型变得越来越强大。 我可以说在 OpenAI，我们没有做的一件事是，看看，我们有很多数学家，也有很多物理学家， 人们对这些模型现在能做的事情非常兴奋，尤其是，你知道的，内部模型。 我们正在尝试鼓励人们不要把所有时间都花在解决所有数学和物理的开放问题上， 而是推动模型到极限，看看它们能证明或反驳什么，因为我们真的认为重点应该放在如何让模型变得更强大？ 我们如何能尽快安全地将它们引入世界，以便全球所有科学家都能利用这些模型解决问题？ 所以在某种意义上，我们认为是的，把所有精力投入到扩展这些模型上，看看它们目前的极限能做什么，确实非常吸引人。 但真正的重点应该是我们如何利用这些模型创造更强大、更有效的模型，以更具成本效益的方式完成更多事情。

[20:59] **Sarah Guo**
考虑到你对大规模测试计算影响的看法，您认为研究方向或资源分配有什么变化？ 这与递归自我改进的想法有什么交互作用，例如，这是你知道的主要想法， 任何实验室如何获得最佳能力模型？

[21:23] **Noam Brown**
所以我应该澄清一件事，我认为我们还没有达到这样的阶段，哦，只要给它一个任意的、极高的推理预算，它就会， 在各个方面都是超级智能。

[21:32] **Sarah Guo**
闪电目标。

[21:33] **Noam Brown**
嗯。 制作 GPT-7 或其他的，像，是的，尽情发挥吧。

[21:37] **Sarah Guo**
那我们之间有什么呢？

[21:39] **Noam Brown**
我认为玩弄这个模型后，好吧，首先，有些基准是在增加推理预算的情况下，模型根本不会改善。 我觉得很多事实检索类的问题都属于这种情况，如果你问一个人，亚伯拉罕·林肯是什么时候出生的，如果他们不知道日期，他们可以坐在那里， 他们可以考虑一周。 如果他们没有访问维基百科或其他资料，他们在思考了一周后回答这个问题不会比在五秒钟内好。 模型也是如此。 实际上，有趣的是，如果你给模型这些事实检索问题并给他们一点时间考虑， 他们实际上会做得更好。 但如果你给他们一周，他们不会突然就更好地记住日期。 所以有些基准显然会随着测试计算的增加而改善，而有些则不会。 我认为在另一极端，有些基准明显会在测试计算的增加下无限改善。 我想指出的例子是数独。

[22:40] **Noam Brown**
解数独有一个非常简单的策略，就是尝试一堆不同的随机数字，然后看看它是否符合条件， 是否符合所有限制。 如果不符合，就尝试另一种随机数字组合。 而且显然，花足够的时间，你将能够用这个策略解决任何伪组合。 你可以直观地看到：好吧，任何模型只要给更多的测试时间计算，就可以不断变得更好。 所以所有的基准其实都存在于这两个极端之间。 模型还未达到如果你只给它足够的测试计算，就能完成所有工作的水平，毕竟，是的， 有些基准它们将不会改善。 有些事物它们不会改善。 我看到的一件事是，尤其在研究中，他们目前没有很好地把握研究的品味。 所以我认为它们实际上是对研究人员非常好的补充，特别是，你知道，我发现使用这些模型效果更好， 但它们无法完全替代整个研究周期。 现在，随着时间的推移，这种情况会改变吗？ 可能会。

[23:39] **Noam Brown**
我的意思是，我认为模型的整体表现正在提高。 有些事情的改善速度比其他事情快。 但它们并未达到仅凭足够的测试时间计算就能完全取代研究人员的程度。

[23:52] **Sarah Guo**
你能举个例子，比如要求模型做一个研究测试或这绝对是个糟糕的主意吗？

[23:59] **Noam Brown**
我的意思是，我想回到我的扑克求解器的例子，我对模型优化我在博士期间开发的算法的能力印象深刻。 说实话，回想起来，我是多么低效，令我感到震惊，他们能够让速度提升到比原来快 10 倍、100 倍。 然后我就想，好的，你能否想出一个比我想出的方法更好的算法，或者比其他任何人想出的更好。 请查看所有已发布的工作并综合它们，然后尝试想出一些新颖的东西。 它无法做到。 我可以给它很多时间，但它仍然无法做到。 现在，如果我给它搭建一些框架，稍微约束一下，或许它最终能够想出更好的东西。 但这需要很多，不能简单地说，好吧，请想出一个更好的算法。

[24:52] **Sarah Guo**
你认为这会如何改善？

[24:55] **Noam Brown**
我观察到每个模型发布的周期中，在这方面它确实有所提升。 在我看来，它仍然很糟糕，但不如以前那么糟糕。 我不会感到惊讶，如果有一天，与编码、数学一样，可能会有一个拐点，突然变得足够好以便于使用。 我不会感到惊讶，如果我们在研究品味上也遇到那个拐点。

[25:18] **Sarah Guo**
在这方面，你的看法是如何？今天 RSI 的框架是什么？ 我们应该如何看待它？

[25:23] **Noam Brown**
这些模型无疑正在加速研究人员在实验室内所能做的事情。 但我认为它们正在加速某些事情，而不是其他事情。 目前，我们处在这样一个阶段：好吧，如果某样东西速度提高了 100 倍，那么你就会受到未提高 100 倍的事物的制约。 随着时间的推移，我们所面临的瓶颈将会减少。 我认为在这方面会有一种逐渐的起飞。 但关键在于转变。 目前，更重要的是转变研究人员的工作，而不是完全取代研究人员。

[25:52] **Sarah Guo**
所以这实际上暗示着你不认为我们现在接近一个非常快速的起飞点。

[25:58] **Noam Brown**
我觉得快速起飞是相对的。 事情发展得非常快。 但我认为有这样一个假设，即可能在一夜之间发生智能爆炸，模型发现某种突破使它们变得更聪明。 然后这将导致更多的突破使其更聪明，瞬息之间。 基本上，在瞬间，模型就会在各个方面迅速超越人类。 而我并不认为我们正在朝这个方向发展，主要是因为模型在实现其最大智能时非常依赖大规模的测试计算。 如果需要如此多的测试时间计算才能释放模型的全部能力，那么这意味着你受到时间的制约。 事情的进展速度是有限的，因为模型需要足够长的时间才能真正做一些非常、非常强大的事情。 时间自身也成为我们所能做事情的瓶颈。 我认为目前大部分实验室的情况都是这样，我最终认为我们所有人最大的瓶颈是时间。

[26:57] **Noam Brown**
这就是为什么所有研究人员现在都在如此努力工作。 每周投入这么多时间，因为我们都看到了未来的潜力，看到能力所在，而我们被我们能多快完成事情的速度所制约。

[27:10] **Sarah Guo**
你认为现在探索较少的前沿是什么？ 就像，我们之前谈到过多智能体。

[27:17] **Noam Brown**
我认为多智能体已经相当深入探索了。 我认为……

[27:22] **Sarah Guo**
达到足够的规模？

[27:23] **Noam Brown**
我认为还有很多工作可以做。 但这也是比较难做的事情之一。 很多研究在小规模下很难进行。 我认为特别是多智能体，它确实需要，为了完全释放潜力，需要前沿模型。 我认为我们已经看到一些相当有趣的多智能体框架。 我认为它们能做很多事情，但我认为这只是触及了它们将能做到的表面。 我的意思是，我考虑的一个方式是，如果你看人类文明，事实并不是人类变聪明了， 并不是说他们在过去的 50,000 年中进化得更聪明。 而是人类今天能够做更多的事情，原因是过去有数十亿人进行思考，并在彼此积累的知识基础上进行构建。

[28:12] **Sarah Guo**
我们与五万年前相比，拥有非常好的检索和支架。

[28:15] **Noam Brown**
我甚至不想称其为支架。 这是一种非常有机的自发性质，仅仅是人类能够积累知识、分享知识并在此基础上进行建设。 我们今天在 AI 模型中没有看到这种现象。 它们生于一个世界，只存在于一个非常短的背景窗口中，然后就消失了。 是的，有些事情可以继续维持它们，但是非常有限。 我确实认为最终我们会看到，并且我们开始看到一些迹象，表明我们正在进入一个能够大规模协作的世界。 我认为 Multbook 和 OpenClaw 初推出时，显然有些被过分炒作， 但它们是未来事物发展方向的一个迹象。 我确实认为最终我们会到达那样的世界。

[29:01] **Sarah Guo**
一种某种协调的复合状态。

[29:04] **Noam Brown**
是的，模型在更全球层面上分享知识的能力，能够在此知识基础上有效建立。

[29:11] **Sarah Guo**
鉴于这一系列信念和你的工作，如果没有一夜之间的突破，你会如何描述三国之间的前沿竞争？ 这只是研究人员不断努力，试图做出良好的高品味算法和投资决策，关于该去哪里，然后进行计算分配，再进行政策决策和评估决策。 感觉比我想象的稍微更为扎实，而不是朝着某个没有人能追上你的即时硬起飞狂奔。

[29:48] **Noam Brown**
我认为现在竞争非常激烈。 我确实认为如今存在的模型正在加速前沿实验室研究人员的工作。 显然，正如我所说，目前对此是有一定限制的，但利用模型来改进模型研究的能力是真实存在的，这是一种， 这就像是一种增强力量。 我认为这种情况将会持续存在。 我认为随着时间的推移，它们会愈发真实。 让我感到安心的一件事是，我认为前沿实验室的所有研究人员，以及所有的前沿实验室，都认清了其中的利害关系，以及这些模型所涉及的， 风险是什么。 这让我感到欣慰，我觉得每个人都真的理解，比如， 这是一件相当严重的事情，可以导致非常伟大的事情，也可以导致非常糟糕的事情。 是的，实验室之间存在竞争动态，但我们也可以尝试找出如何让我们所有人都得到积极的结果，而不是非常消极的结果。

[30:43] **Sarah Guo**
我觉得，我应该问一下，因为你一直早早就正确地认识到测试时计算和推理作为一个框架的重要性， 有哪些方式是你使用模型的，你会鼓励其他人也这样做，对吧？ 这只是目标一切吗？

[31:03] **Noam Brown**
我认为对许多人来说，他们工作，我是说，这可能对你的听众来说并不一定正确， 但是有很多人在 2023 年左右尝试了 AI，并且觉得他们无法信任输出，因此在高风险决策中不使用它。 实际上，我认为模型已经进步到一个非常适合这些事情的程度。 我是说，我询问过他们的税务建议，最近买了一套公寓，问它关于，好的，那我必须填写的所有文件是什么，以及， 我该如何理解这一切？ 对于这些问题，它实际上非常有效。 所以我日常使用它来处理很多这类事情。 我认为它们现在已经到了一个程度，而且实际上已经有一段时间处于这个程度，我觉得我可以比信任人类的输出更信任它的输出。

[31:49] **Sarah Guo**
一个专业的人类。

[31:50] **Noam Brown**
是的。

[31:51] **Sarah Guo**
好的。 我有两个最后的问题要问你。 第一个是，你认为在其他研究界是否有一些事情与你意见不合或尚未意识到重要性？

[32:05] **Noam Brown**
这是个很好的问题。 我希望我能提前考虑这个问题。

[32:07] **Sarah Guo**
你可以和我一起放松一下，想一想。 现在这样一致是不是很奇怪？ 三年前你有点失落，为什么人们不理解这有多重要？

[32:15] **Noam Brown**
我仍然觉得这不是共识，因为人们仍然不以这种方式发布基准。

[32:21] **Sarah Guo**
这确实是，是的。

[32:23] **Noam Brown**
我认为这像是惯性。 是的，但这就是我写这篇文章的原因。 我只是想说，听着，我的意思是，我们可以讨论这个，但是，部分动机是，我会和研究人员谈论， 显示基准需要一个 x 轴，无论是标记、成本还是时间，应该有一个 x 轴。 每个人都会说，是的，这很有道理。 我们应该这样做。

[32:42] **Sarah Guo**
但他们并没有以良好的心态行动，像这样，我们必须衡量正确的事物。

[32:47] **Noam Brown**
嗯，他们的回应实际上是，人们期待我们发布网格。 那么，好的，为什么人们期待发布网格？ 因为每个人都发布网格。 所以你最终陷入了这种坏的平衡，大家都知道这是个坏平衡，但没有人想打破它。 我觉得，好吧，如果我能够出来说，大家听着， 让我们都意识到我们处于一个糟糕的平衡状态，接着转向这个新的平衡状态，在这个状态下，我们用 x 轴来绘制，希望下次有模型发布时，公司能安心不发布网格，至少在一开始时不发布， 最上面那一行。 我们可以对这些模型进行更有效的评估。

[33:29] **Sarah Guo**
那么最后一个问题给你。 你怎么看待这些专业领域的公司，他们觉得自己的价值基本上像是我目标的路由层，选择层，由一系列离散任务组成，有些任务需要更多的智能，而在我的工作作为供应商中，就是解决这个问题或实现最佳结果。 考虑到预算限制，我将会进行管理。 并行处理和从哪个模型上花费多少推理？ 因为我认为前沿实验室的观点是，路由发生在 API 背后、应用程序背后，还有一部分发生在模型本身。

[34:25] **Sarah Guo**
这些元素显然在所有这些应用程序中被外部化。

[34:30] **Noam Brown**
是的，我确实认为这与基准应该用令牌或成本的 x 轴进行评估有关。 我最近看到了一些评估显示，好的，通过路由层，您可以通过在模型之间进行共识获得更好的表现。

[34:46] **Sarah Guo**
是的。

[34:46] **Noam Brown**
我绝对相信，如果您在模型之间达成共识，它们的表现会比任何单一模型更好。 但重要的是要问，您是否会比让模型基本上思考更长时间表现得更好？ 一旦您控制了测试时间的计算，它是否真的仍然表现得更好？ 这是您想要弄清楚的问题。

[35:04] **Sarah Guo**
这很有原则，像是，是的，路由没有问题，但所有这些都受制于同样的预算问题。 如果您把它放在同一标量上，那么您就可以做出最佳决策，我想我可能会赢。

[35:15] **Noam Brown**
我甚至不知道我是否会相信路由做得更好。 但问题仍然是，它是否会显著更好？ 它非常脆弱吗？ 与基准相比，它是否反映了现实世界的用例？ 因为像是，您可能遇到的一个问题是，您可以为某些基准进行路由优化，显示 “哦，是的，我们看到这些基准有很大的改善”。 但在现实世界的用例中，它实际上并没有显著改善。 所以我会说，至少您想控制测试时间的计算，然后您还想对基准保持正常的怀疑态度。

[35:50] **Sarah Guo**
太棒了。 Noam，非常感谢你参与这个使命，帮助我们打破这种虚假的平衡。

[35:57] **Noam Brown**
哦，回到这里真好。

[36:00] **Sarah Guo**
在 Twitter 上关注我们 @NoPriorsPod。 如果您想看到我们的脸，请订阅我们的 YouTube 频道。 在 Apple Podcasts、Spotify 或您收听的任何地方关注我们的节目。 这样您每周都会收到一集新节目。 还可以注册电子邮件或在 no-priors.com 找到每集的 transcripts。
