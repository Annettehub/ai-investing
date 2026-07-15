2026-05-22 雷纳·波普——自下而上的芯片设计Reiner Pope – Chip design from the bottom up
Info
Podcast: Dwarkesh Podcast
Episode: Reiner Pope – Chip design from the bottom up
Link: https://app.podwise.ai/dashboard/episodes/8050864
Publish Time: 2026-05-22
Save Time: 2026-05-24
Summary
AI chip architecture centers on the fundamental primitive of the multiply-accumulate operation, which is critical for efficient matrix multiplication. Designing these chips requires balancing compute density against the high costs of data movement, as moving information between register files and logic units consumes significant die area. Systolic arrays address this by keeping weight matrices local to the compute logic, thereby maximizing throughput while minimizing external communication. Clock speed optimization involves inserting pipeline registers to manage logic paths, though excessive synchronization can degrade area efficiency. While GPUs utilize tiled streaming multiprocessors to handle diverse workloads, TPUs employ coarser-grained matrix units to amortize costs across large-scale operations. Ultimately, the design process is a series of sizing decisions aimed at maximizing compute relative to communication bandwidth, a constraint that dictates the performance and scalability of modern neural network accelerators.
AI 芯片架构的中心在于乘法累加操作这一基本原语，这对于高效的矩阵乘法至关重要。设计这些芯片需要在计算密度与高数据移动成本之间找到平衡，因为在寄存器文件和逻辑单元之间移动信息会消耗大量的晶圆面积。脉动阵列通过将权重矩阵保持在计算逻辑附近来解决这个问题，从而在最小化外部通信的同时最大化吞吐量。时钟速度优化涉及插入流水线寄存器以管理逻辑路径，尽管过度的同步可能会降低面积效率。尽管 GPU 利用平铺的流处理器来处理多样化的工作负载，但 TPU 采用更粗粒度的矩阵单元以在大规模操作中分摊成本。最终，设计过程是一系列尺寸决策，旨在最大化计算相对于通信带宽，这一约束决定了现代神经网络加速器的性能和可扩展性。
Takeaways
The primary constraint in modern chip design is minimizing data movement, as the energy and area cost of transporting information from register files to logic units significantly outweighs the cost of the actual computation.
现代芯片设计的主要限制是最小化数据移动，因为从寄存器文件到逻辑单元传输信息的能量和面积成本显著超过实际计算的成本。
Reducing bit precision provides quadratic, rather than linear, gains in compute efficiency, which serves as the fundamental driver behind the industry's rapid shift toward lower-precision arithmetic like FP4.
降低比特精度提供的是平方而不是线性的计算效率提升，这为行业快速转向低精度运算（如 FP4）提供了基本推动力。
Systolic arrays optimize performance by storing weight matrices locally, effectively amortizing the high cost of register file access by reusing data across multiple operations within the array.
脉冲阵列通过局部存储权重矩阵来优化性能，有效地摊销高昂的寄存器文件访问成本，通过在阵列内重复使用数据，实现多个操作间的数据重用。
Increasing clock speed via pipeline register insertion is a direct trade-off between throughput and die area, as excessive synchronization logic can consume more physical space than the actual compute units themselves.
通过管道寄存器插入来提高时钟速度是在吞吐量和硅片面积之间的直接权衡，因为过多的同步逻辑可能消耗比实际计算单元更多的物理空间。
AI accelerators often favor software-managed scratchpad memory over hardware-managed caches to ensure deterministic latency, a critical requirement for maintaining predictable performance in large-scale AI workloads.
AI 加速器通常更倾向于软件管理的临时存储器而非硬件管理的缓存，以确保确定性的延迟，这对于在大规模 AI 工作负载中保持可预测性能是一项关键要求。
FPGAs achieve field-programmability by using lookup tables to emulate logic gates, a process that is roughly an order of magnitude less efficient than ASICs due to the overhead required to implement programmable truth tables.
FPGA 通过使用查找表来模拟逻辑门，从而实现现场可编程性，这一过程的效率大约比 ASIC 低一个数量级，因为实现可编程真值表所需的开销。
GPUs rely on a tiled grid of small, identical streaming multiprocessors, whereas TPUs utilize coarser-grained matrix units, representing a fundamental difference in how they scale compute resources.
GPU 依赖于小型、相同的流处理器网格，而 TPU 则利用更粗粒度的矩阵单元，这代表了它们在计算资源扩展方式上的根本差异。
A significant portion of CPU die area is dedicated to branch prediction logic to maintain high clock speeds, a feature that is largely stripped away in specialized AI accelerators to prioritize compute density and throughput.
CPU 硅片面积的一大部分专用于分支预测逻辑，以维持高时钟速度，而在专用 AI 加速器中，这一特性在很大程度上被剥离，以优先考虑计算密度和吞吐量。
Q & A
Q: Why is the multiply-accumulate (MAC) operation the natural primitive for AI chips?
Q: 为什么乘累加 (MAC) 操作是 AI 芯片的自然原语？
A: The MAC operation is fundamental because it is the atomic step that occurs at every iteration of a matrix multiplication. If you look at the matrix multiplication loop—which is a triple loop over I, J, and K—the core operation is always output[i, k] += input[i, j] * other_input[j, k]. Because this calculation happens at every single step, it makes sense to bake it directly into the hardware. Furthermore, we observe that precision requirements differ between the multiplication and accumulation steps. You can multiply low-precision numbers, but because you are summing a large number of products, rounding errors accumulate quickly. Therefore, we often choose to perform 4-bit multiplication while using 8-bit precision for the accumulation to maintain accuracy.
A: MAC 操作是基础的，因为它是在矩阵乘法的每次迭代中发生的原子步骤。如果你观察矩阵乘法循环——这是一个在 I、J 和 K 上的三重循环——核心操作总是 output[i, k] += input[i, j] * other_input[j, k]。由于这个计算在每一个步骤中都会发生，因此将其直接集成到硬件中是合情合理的。此外，我们观察到乘法和累加步骤之间的精度要求是不同的。你可以乘以低精度数字，但由于你在对大量的乘积求和，舍入误差迅速累积。因此，我们通常选择进行 4 位乘法，同时使用 8 位精度进行累加以保持准确性。

Q: Why is lower bit precision so favorable for AI chips, and why does it scale better than one might expect?
Q: 为什么较低位精度对 AI 芯片如此有利，而它的扩展性又为何超出预期？
A: The advantage of lower precision is quadratic. Historically, every time you halve the bit precision, you don't just get a linear improvement; because the area cost of a multiplier scales quadratically with the bit width, reducing the precision provides an even larger speedup than expected. This is the single biggest reason why low-precision arithmetic has become the standard for neural networks. For example, in NVIDIA's B100 and B200 generations, we see that FP4 is three times faster than FP8, even though theoretically, you might expect a 4x speedup based on the quadratic scaling. This efficiency allows us to pack more compute into the same die area.
A: 较低精度的优势是平方级的。历史上，每次将位精度减半时，你不仅仅会获得线性改进；因为乘法器的面积成本与位宽的平方相关，因此降低精度提供的加速比预期的还要大。这是低精度算术成为神经网络标准的最大原因。例如，在 NVIDIA 的 B100 和 B200 代中，我们看到 FP4 的速度是 FP8 的三倍，即使理论上你可能基于平方扩展预期 4 倍的加速。这种效率使我们能够在相同的芯片面积内容纳更多的计算。

Q: What is the primary source of inefficiency in traditional processor designs like CUDA cores or CPUs?
Q: 在传统处理器设计（如 CUDA 核心或 CPU）中，主要的低效来源是什么？
A: The primary inefficiency is the cost of data movement between the register file and the logic units. In a standard processor, you have a register file and an arithmetic logic unit (ALU). To perform an operation, the processor must select three arbitrary registers from the file using a MUX (multiplexer). Building a MUX is surprisingly expensive; it requires a large number of AND and OR gates that scale with the number of registers and the bit width. In many cases, the circuitry required just to move data from the register file to the ALU and back is many times more expensive in terms of gate count and die area than the actual multiply-accumulate logic itself.
A: 主要的低效来源是寄存器文件和逻辑单元之间的数据移动成本。在标准处理器中，你有一个寄存器文件和一个算术逻辑单元 (ALU)。为了执行一个操作，处理器必须通过 MUX（多路复用器）从文件中选择三个任意的寄存器。构建 MUX 的成本出乎意料地昂贵；它需要大量的与寄存器数量和位宽相关的与或门。在许多情况下，仅将数据从寄存器文件移动到 ALU 然后再返回所需的电路，在门数和芯片面积方面的成本远高于实际的乘累加逻辑本身。

Q: How do systolic arrays, such as those found in Tensor Cores, solve the data movement problem?
Q: 类似于张量核心中的脉动阵列如何解决数据移动问题？
A: Systolic arrays solve the data movement problem by baking a larger loop of the matrix multiplication into the hardware. Instead of bringing the weight matrix in from the register file every single cycle—which is prohibitively expensive in terms of wiring and power—we store the weight matrix locally within the systolic array. By keeping the weights fixed in local registers and reusing them over many cycles for different input vectors, we drastically reduce the bandwidth requirements. We only need to trickle-feed the data into the array, keeping the wiring cost bounded to a linear factor relative to the array size, rather than scaling quadratically.
A: 脉动阵列通过将矩阵乘法的更大循环集成到硬件中来解决数据移动问题。与每个周期都从寄存器文件中提取权重矩阵——这在布线和功耗方面是极其昂贵的——相比，我们将权重矩阵保存在脉动阵列的本地内存中。通过将权重固定在本地寄存器中，并在多个周期中对不同的输入向量进行重复使用，我们大大减少了带宽需求。我们只需在阵列中涓涓而入数据，使布线成本相对于阵列大小保持在一个线性因子，而不是平方比例上升。

Q: What determines the clock cycle of a chip, and why is there a trade-off between clock speed and area?
Q: 什么决定了芯片的时钟周期，时钟速度与面积之间为什么存在权衡？
A: The clock cycle is the interval at which the entire chip synchronizes its state. Every nanosecond or so, the chip pauses to store the output of logic clouds into registers. The challenge is that any computation must finish before the next clock cycle hits. If you add too much logic between registers, the signal won't settle in time, and you risk missing the clock cycle. You can increase your clock speed by inserting more "pipeline registers" to break up the logic into smaller chunks, but this is a direct trade-off: you gain higher frequency, but you pay a massive cost in die area because you are spending most of your transistors on registers rather than actual compute.
A: 时钟周期是整个芯片同步其状态的时间间隔。每隔大约一个纳秒，芯片暂停以将逻辑云的输出存储到寄存器中。挑战在于，任何计算都必须在下一个时钟周期来临之前完成。如果你在寄存器之间添加太多逻辑，信号将无法及时稳定，你将面临错过时钟周期的风险。你可以通过插入更多 “流水线寄存器” 来提高时钟速度，从而将逻辑分解为更小的块，但这是一种直接的权衡：你获得了更高的频率，但在芯片面积上付出了巨大的代价，因为你将大部分晶体管用于寄存器而不是实际计算。

Q: What are the trade-offs between using an FPGA and an ASIC for high-frequency trading or other specialized tasks?
Q: 在高频交易或其他专业任务中，使用 FPGA 和 ASIC 之间的权衡是什么？
A: Anything you can express in an FPGA can also be expressed in an ASIC, and the ASIC will be about an order of magnitude cheaper and more energy-efficient. The trade-off is the upfront cost: an ASIC requires a "tape-out" that can cost  10,000. FPGAs are ideal when you need deterministic latency and high parallelism but plan to update your logic frequently—perhaps every month. You aren't paying the massive non-recurring engineering cost of an ASIC every time you change your algorithm.
A: 任何你可以在 FPGA 中表达的东西也可以在 ASIC 中表达，且 ASIC 的成本大约便宜一个数量级且更节能。权衡在于前期成本：ASIC 需要一次成本约 3000 万美元的 “流片”，而 FPGA 是一种成本约 10,000 美元的预制造设备。当你需要确定性延迟和高并行性，但又计划频繁更新你的逻辑（可能是每月一次）时，FPGA 是理想选择。每次改变算法你不需支付 ASIC 的庞大非重复工程成本。

Q: Why is latency non-deterministic in CPUs compared to AI accelerators?
Q: 为什么在 CPU 中延迟非确定性而在 AI 加速器中是确定性的？
A: Non-determinism in CPUs largely stems from the cache system. A CPU cache is an enormous optimization—it makes programs run 100 times faster by storing recent memory accesses—but whether you get a "cache hit" or a "cache miss" depends on the ambient environment, such as what other programs are running or what data was accessed recently. This introduces jitter. AI accelerators like TPUs often replace this cache with a "scratchpad" memory. In a scratchpad architecture, the software explicitly manages data movement between the off-chip memory and local memory using specific instructions. Because the hardware isn't making autonomous decisions about what to cache, the latency becomes perfectly deterministic.
A: CPU 中的非确定性主要源于缓存系统。CPU 缓存是巨大的优化——它通过存储最近的内存访问使程序运行快 100 倍——但你是否获得 “缓存命中” 或 “缓存未命中” 取决于环境，比如其他程序正在运行或者最近访问了什么数据。这引入了抖动。像 TPU 这样的 AI 加速器通常用 “临时存储” 内存替换这个缓存。在临时存储架构中，软件使用特定指令显式管理外部内存和本地内存之间的数据移动。由于硬件没有自主决定缓存内容，延迟变得完全确定。

Q: What is the high-level architectural difference between a GPU and a TPU?
Q: GPU 和 TPU 之间的高级架构差异是什么？
A: At a high level, a GPU is organized as a fairly regular grid of many small, identical units called Streaming Multiprocessors (SMs), each containing its own registers, schedulers, and tensor cores. A TPU, by contrast, uses much coarser-grained logic. It consists of a few massive matrix units (systolic arrays) flanked by vector units. You can think of a GPU as a collection of many tiny TPUs tiled across the chip. While the GPU's structure is excellent for moving data between vector and matrix units within a single SM, the TPU's coarse-grained approach allows for larger systolic arrays that can amortize the cost of the register files more effectively.
A: 从高层次来看，GPU 组织为一个相当规则的小单元网格，称为流处理器（SM），每个 SM 都包含自己的寄存器、调度器和张量核心。相比之下，TPU 使用更粗粒度的逻辑。它由少数巨大的矩阵单元（脉动阵列）和向量单元构成。你可以把 GPU 想象成一个在芯片上平铺的许多微小 TPU 的集合。虽然 GPU 的结构非常适合在单个 SM 内部在向量和矩阵单元之间移动数据，但 TPU 的粗粒度方法允许更大的脉动阵列，这样可以更有效地摊销寄存器文件的成本。
Keywords


Keywords

Explanation

AI chip

Specialized hardware designed to accelerate the complex mathematical calculations required for artificial intelligence, particularly matrix operations. Unlike general-purpose processors, these chips are optimized for the massive parallelism needed to train and run neural networks efficiently.

AI 芯片

专门的硬件设计用于加速人工智能所需的复杂数学计算，尤其是矩阵运算。与通用处理器不同，这些芯片针对训练和高效运行神经网络所需的巨大并行性进行了优化。

Matrix multiplication

A fundamental mathematical operation where two grids of numbers are multiplied to produce a new grid. It is the primary workload in AI, as neural networks rely on these calculations to process data and generate predictions.

矩阵乘法

一种基本的数学运算，其中两个数字网格相乘以产生一个新的网格。它是人工智能中的主要工作负载，因为神经网络依赖这些计算来处理数据和生成预测。

Multiply-accumulate (MAC)

A common operation in digital signal processing and AI that involves multiplying two numbers and adding the result to an existing sum. It is considered a core primitive in chip design because it is performed repeatedly at every step of a matrix multiplication.

乘加运算 (MAC)

数字信号处理和人工智能中常见的运算，涉及将两个数字相乘并将结果加到现有的和中。由于在矩阵乘法的每一步中都会反复执行此操作，因此被认为是芯片设计中的核心原语。

Full adder

A basic digital circuit that adds three single-bit numbers together and produces a two-bit output. It acts as a building block for more complex arithmetic units within a chip, helping to manage the binary summation required for larger calculations.

全加器

一种基本的数字电路，将三个单比特数字相加并产生一个双比特输出。它作为芯片内更复杂算术单元的构建块，帮助管理更大计算所需的二进制加法。

Systolic array

A specialized architecture consisting of a grid of processing units that pass data between neighbors in a rhythmic, pulse-like fashion. This design is highly efficient for matrix multiplication because it minimizes the need to move data to and from a central memory, saving energy and space.

脉动阵列

一种专门的架构，由一组处理单元组成，以节奏感、脉冲般的方式在邻近单元之间传递数据。该设计在矩阵乘法中非常高效，因为它最小化了将数据移动到中央存储器和从中央存储器移动的需求，从而节省了能源和空间。

MUX (Multiplexer)

A digital circuit that selects one of several input signals and forwards it to a single output line. It is essential for routing data within a chip, though it can become a significant source of area and power consumption when used extensively in memory systems.

多路选择器 (MUX)

一种数字电路，选择多个输入信号中的一个并将其转发到单个输出线。它对于在芯片内路由数据至关重要，但在内存系统中广泛使用时，可能成为显著的面积和功耗来源。

FPGA (Field Programmable Gate Array)

A type of integrated circuit that can be configured by the user after manufacturing to perform specific tasks. Because it can be reprogrammed in the field, it is useful for prototyping or applications requiring frequent changes, though it is generally less efficient than custom-built chips.

现场可编程门阵列 (FPGA)

一种集成电路，用户可以在制造后进行配置以执行特定任务。由于可以在现场重新编程，它对于原型设计或需要频繁更改的应用程序非常有用，尽管通常不如定制芯片高效。

ASIC (Application-Specific Integrated Circuit)

A custom-designed chip created for a single, specific purpose rather than general use. While expensive to develop and manufacture, ASICs are far more energy-efficient and faster than general-purpose processors or FPGAs for their intended task.

应用专用集成电路 (ASIC)

为单一特定目的而设计的定制芯片，而非通用使用。虽然开发和制造成本高，但在其预期任务上，ASIC 比通用处理器或 FPGA 更为节能和快速。

LUT (Lookup Table)

A component used in FPGAs that acts as a programmable logic gate by storing a truth table of output values for every possible input combination. It allows the chip to be configured to perform any logical function, providing the flexibility needed for field programming.

查找表 (LUT)

用于 FPGA 的组件，作为可编程逻辑门，通过存储每个可能输入组合的真值表来工作。它使芯片能够配置为执行任何逻辑功能，提供了现场编程所需的灵活性。

Von Neumann architecture

A computer design model where a single processor shares a memory system for both data and instructions. Modern hardware often deviates from this classic serial model by incorporating massive parallelism and specialized memory structures to improve performance for AI tasks.

冯·诺依曼架构

一种计算机设计模型，其中单个处理器共享用于数据和指令的内存系统。现代硬件通常通过引入巨大的并行性和专用内存结构来偏离这一经典的串行模型，从而改善人工智能任务的性能。

Branch predictor

A digital circuit within a CPU that guesses the outcome of a conditional branch in a program before it is actually evaluated. By predicting the path, the processor can keep executing instructions without waiting, though this adds complexity and potential for errors to the chip's design.

分支预测器

一种数字电路，在 CPU 内部，用于在程序实际上进行评估之前，猜测条件分支的结果。通过预测路径，处理器可以继续执行指令而无需等待，尽管这增加了芯片设计的复杂性和潜在错误的可能性。

TSMC

A major semiconductor manufacturing company that produces chips for many of the world's leading technology firms. It provides the fabrication technology and design kits that chip architects use to turn their logical designs into physical hardware.

台积电

一家主要的半导体制造公司，为众多全球领先的科技公司生产芯片。它提供芯片架构师用于将其逻辑设计转化为实际硬件的制造技术和设计工具包。
Highlights
(16:05) Quadratic scaling with bit width is the single reason why low-precision arithmetic has worked so well for neural nets.
二次缩放与位宽是低精度算术对神经网络如此有效的唯一原因。
(31:30) Moving data from the register file to the logic unit is many times more expensive than the logic unit itself.
将数据从寄存器文件移动到逻辑单元的成本比逻辑单元本身高得多。
(53:01) Anything you can express in an FPGA, you can express in an ASIC, and it will be an order of magnitude cheaper and more energy-efficient.
你在 FPGA 中能够表达的任何东西，在 ASIC 中都能表达，且成本低了一个数量级，更加节能。
(1:14:58) Most of the energy consumption of a chip comes from charging and discharging capacitors when toggling bits from zero to one and back.
芯片的大部分能耗来自于在将比特从零切换到一和再切换回零时对电容器的充放电。
Transcript
Fundamentals of AI Chip Arithmetic and Precision Scaling
人工智能芯片算术和精度缩放的基础
AI chip design centers on the multiply-accumulate operation, which serves as the fundamental primitive for matrix multiplication. This operation involves multiplying pairs of numbers and accumulating the results, a process that requires higher precision in the accumulation step to mitigate rounding errors. The area cost of these multipliers scales quadratically with bit width, making lower-precision formats like FP4 significantly more efficient than FP8. By optimizing these arithmetic primitives, designers can achieve substantial performance gains, as evidenced by the shift toward specialized hardware that prioritizes these specific calculations over general-purpose logic.
人工智能芯片设计以乘积累加运算为中心，该运算作为矩阵乘法的基本原语。此操作涉及将数字对相乘并累加结果，这个过程在累加步骤中需要更高的精度以减少舍入误差。这些乘法器的面积成本随着位宽呈二次方增长，使得像 FP4 这样的低精度格式比 FP8 更为高效。通过优化这些算术原语，设计师可以实现显著的性能提升，正如转向专用硬件以优先处理这些特定计算而非通用逻辑所表明的那样。
Dwarkesh Patel:
(00:00)
I'm back with Reiner Pope, who is the CEO of MatX, which is a new AI chip company. Last time we were talking about what happens inside a data center. Now we're going to understand what happens inside an AI chip. How does a chip actually work? Full disclosure, by the way, I am an angel investor in MatX, so hopefully you have designed a good chip. Also, if you're listening to this on an audio platform, it's much preferable to watch this Blackboard lecture on a platform where you can see what's happening. So switch over to YouTube or Spotify.
我回来了，旁边是 MatX 的首席执行官 Reiner Pope，MatX 是一家新的 AI 芯片公司。上次我们谈到数据中心内部发生了什么。现在我们要了解 AI 芯片内部发生了什么。芯片实际上是如何工作的？需说明的是，我是 MatX 的天使投资者，所以希望你们设计了一个优秀的芯片。此外，如果你在音频平台上收听此内容，观看这个黑板讲座的体验会更好，尽量在可以看到实际内容的平台上观看。所以请切换到 YouTube 或 Spotify。
Reiner Pope:
(00:31)
So I'll start with sort of the very smallest fundamental unit of chip design and we'll sort of build up into what an overall like actual production chip, what are the components of that. At the very bottom level of a chip, the primitives that we work with Our logic gates, which are very simple things like AND or NOT, and then these are connected together by wires that have to be laid out physically as metal traces on a chip. The main function that AI chips want to compute is multiplication of matrices and really inside that is the fundamental primitive is multiply-accumulative just like of pairs of numbers. We're going to demonstrate what that calculation looks like by hand, and then infer what a circuit would look like for that.
我将从芯片设计的最基本单位开始，我们将逐步构建出一个整体的实际生产芯片，以及它的组成部分。在芯片的最底层，我们使用的原始元件是逻辑门，它们是非常简单的东西，比如与（AND）和非（NOT），然后通过必须以金属迹线物理布置在芯片上的电线连接在一起。AI 芯片想要计算的主要功能是矩阵的乘法，实际上其中的基本原件是累加乘法，类似于数字对的乘法。我们将手动演示这种计算的样子，然后推断出相应电路的样子。
(01:18)
It'll turn out to be sort of easiest if I do multiplication, accumulator, something like a 4-bit number with another 4-bit number. And then we're going to, the actual clearest primitive is actually multiply accumulate. So there's a multiply these two terms, and then we're going to add in, so product of these two terms, and then we're going to add in an 8-bit number.
如果我进行乘法运算，累加器的最佳方式是用一个 4 位数字和另一个 4 位数字进行相乘。然后，我们的基本原件实际上是累加乘法。所以我们有这两个项相乘，然后我们将再加上一个 8 位数字。
Dwarkesh Patel:
(01:50)
And can I ask a clarifying question? Why is this the natural primitive for You know, whatever computation happens at a computer.
我可以问一个澄清性问题吗？为什么这是计算机上发生任何计算的自然原件？
Reiner Pope:
(02:02)
Yeah, so there's a few reasons for this. It's a little bit more efficient, but the reason it's natural for AI chips is that if you look what's happening during a matrix multiply, what is matrix multiply in very short, it is there's a for loop over I and over J and over K. of output i, k plus equals to input i, j times other input j, k. And so multiply, accumulate happens at every single step of a matrix multiply.
是的，这里有几个原因。这效率稍微高一些，但对 AI 芯片而言，自然的原因在于，如果你查看矩阵乘法在做什么，简单来说，矩阵乘法就是在 I、J 和 K 上循环。输出 i, k 加上 输入 i, j 乘以 另一个输入 j, k。所以在每一个矩阵乘法的步骤中，都在进行累加乘法。
Dwarkesh Patel:
(02:48)
Makes sense.
有道理。
Reiner Pope:
(02:49)
And then the other observation is that the precision will almost always be higher in the accumulation step than in the multiplication step. This is maybe specific to AI chips, but you're multiplying low precision numbers, but then when you accumulate, errors accumulate quickly, and so you need more precision here. So this is why we've chosen to do a 4-bit multiplication and an 8-bit addition.
另外一个观察是，累加步骤的精度几乎总是高于乘法步骤。这可能是特定于 AI 芯片的，因为你在乘以低精度数字，但当你累加时，误差快速累积，因此你在这里需要更高的精度。所以这就是我们选择用 4 位乘法和 8 位加法的原因。
Dwarkesh Patel:
(03:09)
Let me make sure I understood that. There's two ways to understand that. One is that the value will be larger than the inputs and the other is that If it was a floating point number, maybe that part is less intuitive to me, but it's maybe the same principle.
让我确保我理解了。有两种方式理解这一点。一种是输出值会比输入值大，另一种是如果是浮点数的话，可能那部分对我来说不够直观，但也许是同样的原理。
Reiner Pope:
(03:25)
It is really the same principle. I guess the separate principle is that as you are summing up this number, you are summing up a whole bunch of numbers, and so you've got a lot of rounding errors accumulating. Whereas in this case, there's only one multiplication in that chain, and so there's not a lot of rounding errors accumulating in the multiplication.
的确是同样的原理。我想另一个原理是，当你在累加这个数字时，你是在累加很多数字，所以你会有很多四舍五入的误差。而在这种情况下，链中只有一个乘法，因此在乘法中不会积累太多四舍五入的误差。
Dwarkesh Patel:
(03:43)
Why are you summing up a whole bunch of numbers? It's just two numbers, right?
你为什么要累加一堆数字？其实只有两个数字，不是吗？
Reiner Pope:
(03:45)
Just, I mean, this summation happens. It's repeated many times.
其实，这个求和是发生的。它重复了很多次。
Dwarkesh Patel:
(03:49)
So, yeah, any errors accumulate. I see.
所以，任何误差都会累积。我明白了。
Reiner Pope:
(03:52)
So, how would we perform this calculation by hand? I mean, as a human, we would probably separate it into two, but we can sort of do it all in one using long multiplication. So the multiplication term first. We're going to multiply this number, this 4-bit number here, by every single bit position in the other 4-bit number. So we write that out. First, 1001 multiplied by this bit position. That is this number itself. Then shift it across by 1. We're multiplying by 0. That gives us an old zeros number. Shifted across even one more to multiply by this one, we get 1001. And then finally, for this last bit position, we get an old zeros number again.
那我们该如何手动进行这个计算呢？作为一个人，我们可能将其分开处理，但实际上我们可以用长乘法将其一次性完成。所以先进行乘法的部分。我们将这个 4 位数字乘以另一个 4 位数字的每个位。所以我们将其写下来。首先，1001 乘以这个位。这就是这个数字本身。然后向右移动 1 位。我们乘以 0。那会给我们一个全零的数字。再向右移动一位以乘以这一位，得到 1001。最后，对于这个最后一位，我们又得到一个全零的数字。
(04:47)
So this gives us a bunch of terms that we're going to have to add for the multiplication. Then while we're doing that summation of this, we might as well add in the actual accumulated term as well. So we just copy that directly across. So this is the sum. It's a five-way sum that we're going to want to compute. So firstly, what logic gates did it take us to even get to this intermediate step? We needed to produce all 16 of these partial products. How do I produce one of these partial products? So let's take this number one, for example, here. It is one. So how do we produce this number? By multiplying this number by this one over here. We can actually produce that by an AND gate.
这给我们提供了一堆必须用于乘法的项。然后在进行求和时，我们不妨直接加上实际的累加项。所以我们直接复制过来。这是总和。我们想计算的是五项和。首先，要达到这个中间步骤，我们需要什么逻辑门？我们需要生成这 16 个部分乘积。我如何生成其中一个部分乘积？比如说，取这个数字一。它是 1。那我们如何生成这个数字？通过将这个数字与这边的这个相乘。我们实际上可以用 AND 门来生成。
(05:44)
This number is 1 if both this bit is 1 and this bit is 1. If either of them is 0, then the multiplication of 0 times anything is 0. So to produce all of this stuff, we ended up consuming 16 AND gates. Or in the general case, if I were doing a like a P bit multiply times a Q bit multiply, then this will be like P times Q, many ands.
这个数字是 1，当且仅当这个位为 1 且这个位也为 1。如果其中任意一个是 0，则 0 乘以任何数都是 0。因此，为了生成这些东西，我们最终使用了 16 个 AND 门。或在一般情况下，如果我进行一个 P 位乘法与 Q 位乘法，这将是 P 乘 Q 个 AND 门。
Dwarkesh Patel:
(06:16)
Exactly.
确切。
Reiner Pope:
(06:21)
Finally, I sum them. Actually, most of the work is going to happen in the summing. Let me describe the other logic gate that we use here. AND is almost the simplest logic gate that exists on a chip. It's almost the smallest. At the other extreme, typically, the very largest logic gate that you'll use is something called a full adder. And what this does is, coming from software, you might think that a full adder adds 32-bit numbers together. In this case, it just adds three single-bit numbers together. And so you can think of it as adding 0, 1, and 1 together. Now, when I add these together, the result can be 0, 1, 2, or 3. So I can express that in binary using just two bits.
最后，我进行求和。其实大部分工作将在求和过程中进行。让我描述一下我们在这里使用的另一个逻辑门。AND 几乎是芯片上存在的最简单逻辑门。它几乎是最小的。在另一种极端情况下，通常你会使用的最大逻辑门是所谓的全加器。这个门的作用是，从软件的角度考虑，你可能认为全加器是将 32 位数字加在一起。在这种情况下，它只是将三个单位数字加在一起。所以你可以把它看作是将 0、1 和 1 加在一起。现在，当我将这些数字相加时，结果可能是 0、1、2 或 3。所以我可以用两个比特来表示这个结果。
(07:07)
So as input, it has three bits, and as output, it has two bits, which in this case, the number 2 in binary is 1, 0. So this is also known as a 3-to-2 compressor. Because it takes three bits of input and produces two bits of output.
作为输入，它有三个比特，作为输出，它有两个比特，在这个情况下，数字 2 的二进制表示是 1、0。所以这也被称为 3 到 2 的压缩器。因为它接收三个比特的输入，并产生两个比特的输出。
Dwarkesh Patel:
(07:29)
The two inputs are an x and a y value and then some carry that came in from like.
这两个输入是 x 和 y 的值，然后还有一些来自其他输入的进位。
Reiner Pope:
(07:36)
The three inputs are all bits that are in the same sort of bit position, like three bits that are in a column here. And then the two outputs, I have sort of drawn them vertically here and horizontally here to kind of match this vertical versus horizontal layout here, which is expressing that things that are in the same column are in the same bit position, whereas things that are in adjacent columns, like this is a carry out, whereas this was a sum.
这三个输入都是在同一位位置上的比特，就像在这里的一列中的三个比特。然后这两个输出，我在这里垂直绘制它们，而在这里水平绘制，以便与这个垂直与水平的布局相匹配，这表示在同一列中的事物位于相同的比特位置，而在相邻列中的事物，例如这是一个进位，而这是一个求和。
Dwarkesh Patel:
(08:03)
So, if the inputs in the full ladder are, let's say, like 101, then the output would still be 10. If it was 111, it'd be 11. If it was 000, it'd be 00. If it was like 010, it'd still be 01. So, yeah, it's just counting, essentially, the number of things and expressing that in binary.
所以，如果完整的阶梯输入是，比如说，101，那么输出仍然是 10。如果是 111，那么就是 11。如果是 000，那么就是 00。如果是 010，那么仍然是 01。所以，是的，这本质上就是在计数，事物的数量并用二进制表示出来。
Reiner Pope:
(08:23)
So, this circuit actually can sort of capture what we as humans naturally do when we're doing summing along a column. So, I'll show you sort of one iteration of using the full adder to sum. The way I sum here is going to be a little bit unnatural for humans. Humans, we would sort of sum along the column and then remember the carry. But instead of remembering the carry, we'll actually just explicitly write it out. In this, we proceed from the rightmost column towards the left. On the rightmost column, we sum the one and the one, and that produces a zero here and a carry of one. We've used this full adder circuit on this pair of bits and produced a pair of bits as output.
所以，这个电路实际上可以捕捉到我们人类在沿着一列进行求和时自然会做的事情。所以，我将展示使用全加器求和的一个迭代过程。我在这里求和的方式对于人类来说会有些不自然。人类会沿着列进行求和，然后记住进位。但我们不是记住进位，而是直接写出来。在这过程中，我们从最右边的一列开始向左推进。在最右边的一列，我们将 1 和 1 相加，产生一个零和一个进位 1。我们在这一对位上使用了这个全加器电路，并产生了一对位作为输出。
(09:09)
Now, we can do the same thing with this column. We've got a column of 1, 2, 3, 4 numbers. Maybe we'll take the first three of them, run a full adder on them, and that gives us a zero and a zero as output. Some of these is 0, 0. That's the full adder applied to all of these bits. As I've used up bits, I'm going to just cross them out to indicate that I've handled them. Let's just keep going a little bit more. So we'll go here. I'll take these three numbers, I add them, that gives me a 1 and a 0. I've dealt with these three numbers. Now I take 1, 2, and I can even take these three numbers, for example, right now, and add them, and that gives me a 1 and a 0, and I've dealt with these numbers.
现在，我们可以在这一列上做同样的事情。我们有一列 1、2、3、4 的数字。也许我们将取前三个数字，对它们进行全加器运算，这给我们输出一个零和一个零。这些数字的和是 0，0。这是对所有这些位应用全加器的结果。当我用完这些位时，我将把它们划掉，以表示我已处理它们。让我们再继续一下。所以我们在这里进行。我将这三个数字相加，得到 1 和 0。我已处理这三个数字。现在我取 1、2，甚至可以再取这三个数字，比如说，现在，加起来得到 1 和 0，我已处理这些数字。
(10:00)
The way I should view this is that I have this whole grid of numbers that need to be added. I'm going to just keep applying full adders to all the bits that are here, constantly removing three numbers from a column and then writing out two numbers as output. Keep going with this over and over and over and again until I eventually get just one single number coming out here, something like that. This is probably the wrong sum. So this approach that I've described here, this is called a data multiplier. And this is sort of like the standard for how you do area efficient multipliers using full adders.
我应该这样看待这个问题：我有这个整个数字网格需要进行求和。我将不断对所有的位应用全加器，持续从一列中移除三个数字，然后输出两个数字。不断重复这个过程，直到最终只得到一个数字出来，像这样。这可能是错误的总和。所以我在这里描述的这个方法被称为数据乘法器。这就像是使用全加器进行面积高效乘法器的标准。
(10:45)
Let's try and quantify the circuit size of this just so we have got a sense of like how big things are that so we can compare to them later. How many full adders did I use? I started with how many numbers? I have the 16 partial products, which is the product of all of these terms with all of these terms, plus the 8 terms that I'm adding here. So I started off with 24 bits. And then I produced eight bits on the output, eventually. And in every step, I was sort of crossing off three numbers and writing two numbers out as a result. And so every single use of a full adder eliminates one of the bits here. And so how many full adders? It must be the 24 minus the eight.
让我们试着量化一下这个电路的大小，这样我们就能有个大致的了解，以便以后进行比较。我使用了多少个全加器？我开始时有多少个数字？我有 16 个部分积，即所有这些项与所有这些项的乘积，加上我在这里添加的 8 项。所以我开始时有 24 位。然后最终产生了 8 位输出。在每一步中，我大致上是划掉三个数字并生成两个数字作为结果。因此，使用每一个全加器都会消除这儿的一个位。那么有多少个全加器？一定是 24 减去 8。
(11:36)
So that there were 16 full adders in this circuit. In general, this is true in the general case as well, there will be P times Q many full adders in this circuit.
所以这个电路中有 16 个全加器。一般来说，在一般情况下，这个电路中将有 P 乘 Q 个全加器。
Dwarkesh Patel:
(11:47)
Let me make sure I understand the logic of that. So the input bits 24 is P times Q plus P plus Q.
让我确认我是否理解这个逻辑。所以输入位 24 是 P 乘 Q 加上 P 加上 Q。
Reiner Pope:
(11:56)
That's right.
对的。
Dwarkesh Patel:
(11:57)
And the output bits is... Just P plus Q. And so P times Q plus P plus Q minus P plus Q equals P times Q.
而输出位是……仅是 P 加 Q。所以 P 乘 Q 加 P 加 Q 减去 P 加 Q 等于 P 乘 Q。
Reiner Pope:
(12:08)
That's right. So I think this explains sort of, or at least hints at the second reason why we chose to do a multiply-accumulate. First reason being that's actually what shows up in matrix multiplication. But second reason being it gave us this very slick P times Q, very simple algebra. We've described this whole procedure, every single atomic step that I took here becomes a logic gate and then the wires connected together. When I had these three inputs that I salvaged to produce these two outputs, if I think of mapping this to a physical device, there would be a wire that runs connecting all three of these things together into a logic gate that produced this output.
对的。我认为这可以解释或者至少暗示我们选择执行乘加的第二个理由。第一个理由就是这实际上出现在矩阵乘法中。而第二个理由是，它给了我们这个非常简洁的 P 乘 Q，非常简单的代数。我们描述了整个过程，我在这里采取的每一个单独步骤都变成了逻辑门，然后是相互连接的电线。当我有这三个输入可以用来生成这两个输出时，如果我把这个映射到一个物理设备上，会有一根电线连接这三个东西到一个生成这个输出的逻辑门。
(12:53)
Okay, so this is the main primitive at different bit widths that is inside an AI chip. We're going to build up from here to how would you use that to run all of the other operations you might want.
好的，这就是在 AI 芯片内部以不同位宽为主的主要原语。我们将从这里开始构建，看看如何用它来运行可能需要的所有其他操作。
Dwarkesh Patel:
(13:08)
This might be the wrong time to ask this question, but whenever NVIDIA reports that this chip can do X many FP4 or half as many FP8, It seems to imply that those circuits are fungible, that there's not as dedicated like FP4 versus FP8. But the way you're mapping it out here, it seems like you would need, if it has to be mapped out in the logic, you would need a dedicated FP4 multiply accumulate and then a dedicated FP8 accumulate. Basically, can you funge them?
这可能不是问这个问题的好时机，但每当 NVIDIA 报告这个芯片可以执行 X 个 FP4 或一半的 FP8，这似乎暗示这些电路是可替代的，并没有像 FP4 和 FP8 那样的专用。但在你这里的映射看起来，似乎如果必须在逻辑中进行映射，你需要一个专用的 FP4 乘加，以及一个专用的 FP8 累加。基本上，你能把它们换成吗？
Reiner Pope:
(13:44)
As drawn, they're actually not particularly fungible. This is actually one of the main choices you have to make when designing a chip, which is how much of FP4, how much of FP8 do I have? And then sometimes I'll make that consideration from the point of view of like, what do I think is the customer requirement? Another way to take an angle on that is to say, what is the power budget for, equalize the power budget between FP4 and FP8. But so then when they report those numbers, and they just happen to be the case of like, it does 2x as many FP4 as FP8.
按照目前的设计，实际上它们并不特别可互换。这实际上是设计芯片时你必须做出的主要选择之一，就是我有多少 FP4，多少 FP8？有时我会从客户需求的角度考虑这个问题。另一个角度的考虑是，FP4 和 FP8 之间如何平衡功耗预算。但当他们报告那些数字时，如果恰好有这样的情况，它执行的 FP4 是 FP8 的两倍。
Dwarkesh Patel:
(14:12)
They just happen to choose like give the equivalent die areas to all the floating points and as a result, that ended up being...
他们恰好选择为所有浮点数提供等效的芯片面积，因此，这就导致了……。
Reiner Pope:
(14:21)
Like why is the ratio exactly 2x?
为什么比例恰好是 2 倍？
Dwarkesh Patel:
(14:23)
Yeah, exactly.
是的，正是如此。
Reiner Pope:
(14:23)
Yeah. So part of it is, I mean, surely that won't be exactly like exactly equivalent to die area. There's a data movement reason, actually, and we'll maybe come back to this when we sort of look through how it goes into and out of memories. There's something really nice just from a software level of the fact that I can pack two 4-bit numbers into the same storage as an 8-bit number. And so when I store that to a memory or something like that, the sizing of the buses that I wire within the chip actually makes that work out really nicely.
对。所以部分原因是，我的意思是，这肯定不会完全等同于芯片面积。实际上，还有一个数据移动的原因，我们也许在探讨它如何进出内存时会回到这一点。从软件级别来看，把两个 4 位数字打包到一个 8 位数字的相同存储中，这一点真的很好。因此，当我将其存储到内存或其他地方时，芯片内部的总线尺寸实际上会让这一过程显得非常顺利。
Dwarkesh Patel:
(14:55)
Actually, come to think of it, it's not just 2X. The amount of area it takes, it sounds like, is quadratic.
实际上，回想一下，这不仅仅是 2 倍。它所占的面积，听起来是二次方的。
Reiner Pope:
(15:05)
It's quadratic, in fact.
事实上是二次方。
Dwarkesh Patel:
(15:06)
With the bit length. That's why smaller precision is even more favorable than you might think.
与位长有关。这就是为什么较小的精度比你想象的更具优势。
Reiner Pope:
(15:12)
There's a really big reason. In fact, NVIDIA made a change. Historically, up until B100 or B200, every time you have the bit precision, you double the flop count. For the reason you said, because of this quadratic scaling, that ratio is actually slightly wrong. You should get an even bigger speed up than you might otherwise think. And videos like product specs have sort of started acknowledging that in B3 and 100 and beyond where the FP4 is three times faster than the FP8. Though it should be 4x. Yeah, what I've shown here is like the simplest case of integer multiply when you are dealing with floating point as you do in FP4 and FP8.
有一个非常大的原因。实际上，NVIDIA 做出了一个改变。历史上，从 B100 或 B200 开始，每次你提升位精度时，翻转数都会加倍。由于你所说的原因，由于这种二次缩放，该比例实际上是略微错误的。你应该会比预期得到更大的加速。像产品规格这样的影片已经开始在 B3 和 100 及更高的地方承认这一点，FP4 的速度是 FP8 的三倍。虽然应该是 4 倍。是的，我这里展示的就是处理浮点数时，整型乘法的最简单案例，正如你在 FP4 和 FP8 中所做的。

Data Movement Costs and Systolic Array Optimization
数据移动成本与脉动阵列优化
A significant portion of chip area is consumed by data movement between register files and logic units rather than the computation itself. MUX circuits, used to select inputs from register files, are surprisingly expensive in terms of gate count. Systolic arrays address this inefficiency by baking larger loops of matrix multiplication directly into hardware. By storing weight matrices locally within the array, these designs minimize the need to fetch data from external registers, effectively maximizing the ratio of compute to communication. This approach allows for high-throughput processing while keeping bandwidth requirements within manageable limits.
芯片区域的很大一部分被寄存器文件和逻辑单元之间的数据移动消耗，而不是计算本身。MUX 电路用于从寄存器文件选择输入，考虑到门数，这些电路的成本令人惊讶。脉动阵列通过将更大的矩阵乘法循环直接集成到硬件中来解决这种低效问题。通过在阵列内部本地存储权重矩阵，这些设计最小化了从外部寄存器获取数据的需要，有效地最大化了计算与通信的比率。这种方法允许高吞吐量处理，同时将带宽需求保持在可控范围内。
Reiner Pope:
(15:56)
There's this sort of other term, which is the exponent that just complicates this calculation. So what can we see already from this? I think the big observation you've made is that there's this quadratic scaling with bit width, which is like very effective and is the single reason why low precision arithmetic has worked so well for neural nets. But the other thing we're going to do now is we're going to compare sort of the area spent on the multiplication itself with all of the circuitry that is around it. So we'll walk back in time a little bit and see how did GPUs prior to tensor cores work, which is the same way as the way that CPUs worked, in fact.
还有一种其他的项，那就是指数，它只是使这个计算变得复杂。那么我们从中能看到什么呢？我认为你最大的观察是，位宽存在二次缩放，这非常有效，也是低精度算术在神经网络中表现如此良好的唯一原因。但我们现在要做的另一件事是比较乘法本身所花费的面积与周围所有电路的面积。所以我们会回顾一下时间，看看在张量核心之前的 GPU 是如何工作的，实际上与 CPU 的工作方式是相同的。
(16:41)
So which is like, where do we stick this multiplier accumulate unit? Generically, I'll describe like a CUDA core or a CPU. You'll have some register file. Which stores some number of entries, maybe it's like eight entries of like, in this case, I guess, four-bit numbers, but typically like 32-bit numbers or something like that, which are numbers. So this is the, like, inside the CUDA core, I'll have some register file of some depth, and then I will have my multiply accumulate circuit, multiply and accumulate circuit. And what it's going to do, it's going to take three arbitrary registers from this register file, perform the multiply accumulate, and then write back to the register file.
所以在哪里放置这个乘法累加单元呢？通用地说，我会描述一个 CUDA 核心或 CPU。你会有一些寄存器文件。它存储了一些条目，也许是八个条目的，像在这种情况下，我想，四位数，但通常是 32 位数或类似那样的数字。所以这是，像是在 CUDA 核心内，我会有一些深度的寄存器文件，然后我将有我的乘法累加电路，乘法和累加电路。它将从这个寄存器文件中取出三个任意的寄存器，执行乘法累加，然后写回寄存器文件。
(17:34)
So it's going to maybe write to this one, but it was able to read from this one, this one, and another random one. So it'll take three inputs like this. So this is the core data path of many processors. Most processors look like this. You've got some set of registers and then you've got some set of logic units or ALUs. We want to analyze the cost of the data movement from the register file to the ALU and back. Ultimately, there's going to be some circuit that says, well, I don't always have to select this guy, I might select any of the registers at any point in time. A first question is, how can I build a circuit? The circuit that I'm going to look for is a MUX.
所以它可能会写入这个寄存器，但它可以从这个寄存器读出，这个和另一个随机的寄存器。所以它将取出三个这样的输入。这是许多处理器的核心数据路径。大多数处理器都是这样的。你有一组寄存器，然后你有一些逻辑单元或算术逻辑单元。我们想要分析从寄存器文件到 ALU 的数据移动成本，以及返回的成本。最终，将会有一些电路说，我不必总是选择这个家伙，我可能在任何时候选择任何寄存器。第一个问题是，我如何构建一个电路？我将寻找的电路是一个 MUX。
(18:23)
In this case, it's going to have eight inputs, one from each entry of the register file. It's going to have one output, which is actually producing this output. And then, like, what is the cost of this thing? It's, like, all we have to build it out of is AND and OR. And so how do we build it? We do the dumbest thing possible. We, like, form a mask saying, okay, when we want to read, like, the third entry, we're going to AND every single entry with either 1 or 0 based on whether that's what we want to read, and then we're going to OR all of them together.
在这种情况下，它将有八个输入，来自寄存器文件的每个条目。它将有一个输出，实际上产生这个输出。然后，这个东西的成本是多少？我们构建它所需的只是与和与或。那我们怎么构建它呢？我们做最傻的事情。我们形成一个掩码，表示好吧，当我们想读取第三个条目时，我们将用 1 或 0 与每一个条目进行与操作，取决于那是否是我们想要读取的，然后我们将把它们全部或运算在一起。
Dwarkesh Patel:
(19:01)
Okay, just to make sure I understand the basics, what the MUX is doing is it's just like selecting.
好吧，为了确保我理解基础，MUX 所做的就是选择。
Reiner Pope:
(19:05)
Just selecting.
只是选择。
Dwarkesh Patel:
(19:06)
Just selecting an input.
只是选择一个输入。
Reiner Pope:
(19:08)
Yeah, so like invisible to software, it's like you say I want input number three, that means there's a MUX. Yeah. And so like what is the cost of this MUX? So an N input MUX operating on P bits Well, I'm going to, so I have n rows, that's this eight rows and I've got like each row is p bits wide. Well, I have to and every single bit. So I get n times p many and gates. Every single input I have to say, am I going to like mask it out or not? And then I'm going to or them all together. And so there's going to be like n minus one times p many or gates. Which is saying, I've got all of these different things, almost all of them are zeros, but I need to sort of collapse them down into like from my eight options down into one option.
是的，所以对软件而言是不可见的，你说我想要输入编号三，这意味着有一个 MUX。是的。那这个 MUX 的成本是多少？因此，N 输入 MUX 操作在 P 位上。那么，我有 n 行，这就是这八行，每一行宽度为 p 位。我必须对每一个位进行与运算。所以我得到 n 乘以 p 多个与门。每一个输入我都要说，是不是要遮蔽它？然后我将它们全部或运算在一起。所以将会有 n 减去 1 的 p 多个或门。这表示，我有所有不同的东西，几乎所有的都是零，但我需要将它们缩减为，从八个选项中选择一个选项。
(20:04)
And so every step I need to or like one row into an existing row.
所以我每一步需要将一行或到现有的一行中。
Dwarkesh Patel:
(20:09)
Got it, yeah. It's actually kind of funny that you would sort of, you don't think at the level of hardware You sort of just think like, oh, I'll just select element three. And something as simple as that is sort of like in and of itself a quite complicated circuit.
明白了，是的。实际上，有点好玩的是，你不会在硬件层面思考，你只是想着，哦，我就选择第三个元素。这么简单的事情本身就是一种相当复杂的电路。
Reiner Pope:
(20:24)
Yeah. I mean, this is the first step of all of the hidden data movement costs that the shop. Yeah. We're just going to compare. I have to pay this cost, and I've got one MUX here, and then in fact I have two more copies of that for each of the three inputs to my multiply-accumulate operation. And so I have this cost, which is like 3 times N times P and gates over here, compared to this P times Q, like gates in the actual circuit that is doing the thing I care about. And if we plug in actual numbers like this n being 8, I get like 24 times p gates over just in the data movement compared to like if q is 4, like 4 times p gates just in the adder, multiply adder.
是的。我是说，这是所有隐藏数据移动成本的第一步。是的。我们只会进行比较。我必须支付这个成本，而我这里有一个 MUX，实际上我对此乘法累加操作有两个备份。所以我有这个成本，大约是 3 乘 N 乘 P 的与门，相比于这个 P 乘 Q，这个执行我关心的操作的电路中的门。如果我们代入实际数字，比如 n 是 8，那么我在数据移动中得到大约 24 乘 p 的门，而在加法器、乘法加法器中，则是大约 4 乘 p 的门。
Dwarkesh Patel:
(21:14)
And sorry, where is the 3 coming from?
抱歉，3 是从哪里来的？
Reiner Pope:
(21:16)
Three different inputs here.
这里有三个不同的输入。
Dwarkesh Patel:
(21:17)
Got it, okay.
明白了，好的。
Reiner Pope:
(21:21)
Really just what I'm hinting at here is that all of this work, which scales as the size of the register file, and this is a very small register file, all of this work just moving the data from the register file to the logic unit is many, many times more expensive than the logic unit.
我这里暗示的其实是，所有这些工作，随着寄存器文件的大小而增加，而这是一个非常小的寄存器文件，所有这些将数据从寄存器文件移动到逻辑单元的工作要花费的成本是逻辑单元的多，多倍成本。
Dwarkesh Patel:
(21:39)
In the most recent ClusterMax report, Semianalysis ranked almost 100 different GPU clouds. Crusoe was one of only five that made the gold tier. Semianalysis found that gold tier providers like Crusoe had a total cost of ownership that was 5 to 15% lower than silver tier ones, even when they had identical GPU pricing. This makes sense because total cost of ownership is downstream of a bunch of different things that don't necessarily show up in the sticker price, but that Crusoe has optimized. Things like how well you detect faults and how quickly you replace failed nodes. For example, Crusoe was one of the first clouds to adopt NV Sentinel, NVIDIA's own GPU monitoring and self-healing software for enhanced GPU uptime,
在最近的 ClusterMax 报告中，Semianalysis 对近 100 个不同的 GPU 云进行了排名。Crusoe 是仅有的五个进入金牌等级的云服务之一。Semianalysis 发现，像 Crusoe 这样的金牌等级供应商的拥有总成本比银牌等级供应商低 5% 到 15%，即使它们的 GPU 定价相同。这很有道理，因为拥有总成本是许多不同因素的结果，而这些因素在标价中并不一定反映出来，但 Crusoe 已进行了优化。比如说，您检测故障的效率和更换故障节点的速度。例如，Crusoe 是首批采用 NV Sentinel 的云之一，这是 NVIDIA 自家的 GPU 监控和自我修复软件，用于提高 GPU 的正常运行时间，
(22:18)
utilization, and reliability. This sets Crusoe to make use of everything that NVIDIA has learned about why chips fail across all their different fleets and deployments, so that Crusoe can catch faults earlier in the process. And once they identify a failure, Crusoe can swap in a healthy node in less than 10 minutes. Because they're not running bare metal, Crusoe doesn't have to spend time installing an operating system or configuring drivers. They can just spin up a new VM on an already running and pre-qualified host. If you want to learn more about this or the other reasons that Crusoe made Gold tier, go to Crusoe.ai slash Dwarkesh.
利用率和可靠性。这使 Crusoe 能够充分利用 NVIDIA 在各个不同车队和部署中对芯片故障原因的研究，以便 Crusoe 能够在过程早期捕捉到故障。一旦他们识别出故障，Crusoe 可以在不到 10 分钟内更换一个健康的节点。因为他们不是在运行裸金属，Crusoe 不必花时间安装操作系统或配置驱动程序。他们只需在一个已经运行并经过预审的主机上启动一个新的虚拟机。如果您想了解更多关于这个或 Crusoe 进入金牌等级的其他原因，请访问 Crusoe.ai slash Dwarkesh。
(22:52)
It may be helpful to just see what a MUX looks like, maybe like a 2-bit or a 4-bit MUX.
看看 MUX 的样子也许会有帮助，可以是 2 位或 4 位的 MUX。
Reiner Pope:
(22:57)
Yeah, great. So we'll take some inputs. We'll just do a two-way box. So we've got two different numbers. We've got these two inputs. So these are the inputs that are being selected between, and then we have a selector. Which can either be like, I want this one or it could be I want the other one. So this is a one-hot encoding. So this is what we all start with. And then the output we want to produce, let's focus on this case. So this is the actual input we got. We just want to produce this guy as the result. And so very laboriously what we do is we AND this bit with all of these. And so that produces like ANDing this bit with this row. And likewise, we AND this bit with this row. That produces all zeros.
是的，太好了。所以我们将输入一些参数。我们将做一个双向框。我们有两个不同的数字。我们有这两个输入。这些是正在选择的输入，然后我们有一个选择器。它可以是，我想要这个，或者我想要另一个。这是一个独热编码。这就是我们开始时的样子。然后我们想要生成的输出，让我们集中在这个案例上。所以这是我们得到的实际输入。我们只想把这个作为结果输出。所以很费劲的是，我们将这个位与所有这些进行与运算。这将生成对这个位和这一行的与运算。同样地，我们将这个位与这一行进行与运算。这样就生成了全零。
(24:09)
So this was the, there's four ands here, there's four ands here, and then finally we just OR these two together. This gives a one, we OR these two together, this gives a one, we OR these two together, gives a zero, we OR these two together, gives a one. And so this is the four ORs. This actually ends up looking a little bit like addition, in fact. We did exactly the same set of ands here. We've added all of these things together, but then instead of Collapsing it by using these full ladder circuits, we just get a very simple collapsing with OR gates.
所以这里有四个与运算，这里有四个与运算，最后我们将这两个进行或运算。这会生成一个，我们将这两个进行或运算，这会生成一个，我们将这两个进行或运算，生成零，我们将这两个进行或运算，产生一个。所以这是四个或运算。事实上，这最终看起来有点像加法。我们在这里做了完全相同的一组与运算。我们将这些东西都加在一起，而不是通过将这些完整的梯级电路压缩，我们只是通过或门得到一个非常简单的压缩。
Dwarkesh Patel:
(24:49)
But I guess that doesn't look like n times p.
但我想这看起来不像 n 乘 p。
Reiner Pope:
(24:52)
So yeah, so this was with n equals 2 inputs. In the general case, we will have n And so this is n rows, and then we'll have p bits per row. So that gives us the n times p many and gates. So this circuit I've described here, almost all of the cost, like seven-eighths of the cost, is in the reading and writing the register file, and only a tiny fraction of the cost is in the logic unit itself. So this is the problem to solve. This essentially was the state of play. Prior to the Volta generation of NVIDIA GPUs, this kind of thing is what was inside the CUDA cores, and this sort of problem statement is what motivated the introduction of Tensor cores, which are more generically called systolic arrays.
是的，所以这是 n 等于 2 的输入。在一般情况下，我们将有 n，所以这就是 n 行，然后我们每行将有 p 位。这给我们提供了 n 乘 p 个与门。所以我在这里描述的电路，几乎所有的成本，像七分之八的成本，都在读取和写入寄存器文件中，只有很小一部分成本在逻辑单元本身。所以这是一个需要解决的问题。这基本上是当时的局势。在 NVIDIA GPU 的 Volta 代之前，这种东西是在 CUDA 核心内部的，而这种问题陈述促使了张量核心的引入，更通用地称为脉动阵列。
(25:55)
So if we think about how are we going to solve this problem, like we're spending almost all of our circuit area on something that we just really don't care about and is hidden to the software programmer, and the thing that we actually care about is not much of the area. Well, make this one bigger somehow while keeping this at the same size. That's the goal. So the evolution was like we had baked this much into hardware in this stage. This single line is a multiply-accumulate, and this single thing was baked into hardware. The idea of a systolic array is to go two levels of loop up and bake this entire loop out here into hardware.
所以如果我们考虑我们将如何解决这个问题，几乎把所有的电路区域都花在一些我们其实并不关心的东西上，而这些东西对软件程序员来说是隐藏的，而我们实际上关心的东西占用的区域并不多。好吧，以某种方式将这个放大，同时保持这个大小不变。这就是目标。所以演变是，我们在这个阶段把这么多东西内嵌到硬件中了。这一行是一个乘加操作，这个单独的东西也内嵌到硬件中。收缩阵列的思想是提升两个循环层级，并把整个循环内嵌到硬件中。
(26:31)
So the idea being that if we have a much bigger granularity fixed function piece of logic, maybe the taxes we pay on the input and output are much smaller.
所以这个想法是，如果我们有一个更大的粒度固定功能逻辑，也许输入和输出的开销会小得多。
Dwarkesh Patel:
(26:40)
It sounds like you're suggesting that if you go up one step in the... In the matrix multiply loop, you can tilt the balance more towards compute than communication.
听起来你是在暗示，如果在矩阵乘法循环中上升一步，你可以让计算更倾向于计算而不是通信。
Reiner Pope:
(26:54)
That's right. So there's two effects that we're going to take advantage of here. One is just that we can do more stuff per every trip through a register file. And then the other thing we're going to take advantage of is, in fact, in some of this loop, we can take advantage of, for example, certain things staying fixed. So visually, we're going to look at this matrix multiplication. So this portion of the loop corresponds to a matrix vector multiplication, in fact. So we'll take a matrix and multiply it by a vector. How do we do this? We take every column gets multiplied by the vector and then sum. We're going to sum along columns. This 0 and 3 gets multiplied by the 3 and 7 and get summed, and then the 1 and 2 gets multiplied by the 3 and 7 and get summed.
没错。所以我们将在这里利用两个效应。一个就是我们每次通过寄存器文件时可以做更多的事情。另一个我们将利用的事情是，实际上在这个循环中的某些部分，我们可以利用某些东西保持不变。所以在视觉上，我们将观察这个矩阵乘法。这个循环的这一部分实际上对应于矩阵与向量的乘法。所以我们将取一个矩阵并与一个向量相乘。我们该如何做到这一点？每一列都与向量相乘，然后求和。我们将沿列求和。这个 0 和 3 会与 3 和 7 相乘并求和，然后 1 和 2 会与 3 和 7 相乘并求和。
(27:47)
There is a multiply accumulate associated with every single one of these entries in the matrix. We'll just draw out these four multiply accumulates.
每一个矩阵中的条目都有一个与之相关的乘加操作。我们将把这四个乘加操作画出来。
Dwarkesh Patel:
(28:04)
And just to make sure I understand why there's four multiply accumulates, so if each entry in the column that corresponds to the output vector is a dot product, and in this case it'll be like Two multiplications and then the addition of those two multiplications, so like you're accumulating.
只是为了确保我理解为什么会有四个乘加操作，所以如果列中每个条目对应于输出向量是一个点积，在这种情况下，它会像是两个相乘，然后加上这两个相乘的结果，所以就是在累积。
Reiner Pope:
(28:28)
Yeah, so the addition, so really there's only one addition per dot product, but like we like to start with the initialization of zero. Yeah.
是的，加法，实际上每个点积只有一个加法，但我们喜欢从零初始化开始。是的。
Dwarkesh Patel:
(28:34)
Yeah.
是的。
Reiner Pope:
(28:35)
So what we're going to aim for is to have, so we've got to, we want to have quadratically more compute. We do, we have, we've got sort of X times Y as much compute. as we had before, but we're going to want to somehow aim for having only x times as much communication. And this is sort of the intention so that we get this advantage term going as y. So we've laid down the multiplications. We're going to want to bring in a vector of size 2, and so that sort of already is in line with our comms target. That's fine. However, we need to somehow manage the communication of this matrix, which exceeds our budget of x. And so the idea is that In an AI context, this matrix is actually going to stay fixed for a long period of time.
所以我们的目标是实现，增加计算能力，所以我们必须要有更多的计算。是的，我们有，达到了大约 X 乘 Y 的计算能力。和之前相比，不过我们希望尽量只达到 x 倍的通信量。这就是我们的意图，以便我们获得这个随着 y 增长的优势项。所以我们已经进行了乘法操作。我们想要引入一个大小为 2 的向量，这基本上符合我们的通信目标。没问题。然而，我们需要以某种方式管理这个超出我们 x 预算的矩阵通信。所以想法是在 AI 上下文中，这个矩阵实际上会在长时间内保持固定。
(29:37)
Instead of bringing it in from the outside, so we've got some register file sitting over here, we don't want to have the amount of stuff coming out of this register file. This is the term that we want to go as X in some sense. We don't want to bring this full matrix in from the register file every cycle because we don't have enough. That would cost too much in terms of wiring from the register file. And so instead, we're going to store... Our key trick is that this matrix can be stored locally to the systolic array. And so we'll store these numbers 0, 1, 2, and 3.
不像从外部引入，所以我们有一个寄存器文件坐在这里，我们不想从这个寄存器文件中取出太多的数据。这个项目在某种意义上就是我们想要的 X。我们不想每个周期都从寄存器文件引入整个矩阵，因为我们没有足够的。那样在寄存器文件的布线开销太大。所以相反，我们的关键策略是，这个矩阵可以在收缩阵列附近本地存储。所以我们将保存这些数字 0、1、2 和 3。
(30:21)
In just like a gate called a register that like physically stores these numbers and we're going to reuse these numbers over and over again for a large number of different vectors.
在一个叫做寄存器的门电路中，物理上存储这些数字，我们将多次重用这些数字用于不同的向量。
Dwarkesh Patel:
(30:32)
And so the optimization here is that like the nature of matrix multiplication is you can store this like square quadratic thing directly where the logic is happening. And which is like higher dimension than the Or has an extra dimension compared to the inputs which you keep swapping in and out.
所以这里的优化是，矩阵乘法的特性是你可以直接将这个平方的二次项存储在逻辑发生的地方。这比你不断进出交换的输入要高一个维度。
Reiner Pope:
(30:56)
That's right.
没错。
Dwarkesh Patel:
(30:56)
I mean, this is the nature of what a matrix multiplication is, is that you do a lot of multiplication to get one value out. Like a dot product is the result of a lot of multiplications. And so that optimization means that you can stuff a lot of multiplication in before you get some value out of it.
我的意思是，这就是矩阵乘法的本质，你需要进行大量乘法才能得到一个值。点积就是大量乘法的结果。所以这个优化意味着，你可以在获得某个值之前装入很多乘法。
Reiner Pope:
(31:13)
That's right. That's right. Yeah. So just to complete the picture here of concretely how that looks, I swapped the three and the two here, three and two. So just like this 0 and 3 is going to multiply by the 3 and 7, and so we're going to form a dot product along columns here. So somehow we're going to feed a 3 and a 7 in here. These participate in, this feeds into this multiplication and also feeds into this multiplication. Likewise, the 3 feeds into here and also into here. Then we're going to sum Along here, starting at the top of a column, we feed in zeros, and then coming out the bottom, we get results coming out.
没错。没错。是的。所以为了完整地展示这个具体是如何运作的，我在这里交换了三和二，三和二。所以这个 0 和 3 将与 3 和 7 相乘，我们将在这里形成一个沿列的点积。所以我们将以某种方式将 3 和 7 输送到这里。这些参与这一乘法操作，并且也参与这次乘法。同样，3 也参与这里，并且也在这里。然后我们将在这里沿着列求和，从一列的顶部开始，我们输入零，然后从底部得到结果。
(32:05)
Just to visually see what we've got, there's a dot product that is performed along columns in a matrix, and that maps exactly to what is done spatially in the systolic array here. This is one dot product summed vertically, and this is a second dot product also summed vertically. And then what is the data that needs to go into and out of the register file? We have We have X amount of data that's coming out here on the output, and we also have this data coming from the input, X amount of data from the input. With respect to the input and output vectors at least, we've met our goal of having only X as much data going in and out of the register file.
只是为了直观地看到我们所获得的，在矩阵中沿列执行了一个点积，这正好映射到在这个收缩阵列中空间上完成的操作。这是一个垂直求和的点积，这是第二个点积也垂直求和。然后，进出寄存器文件的数据是什么呢？我们有 X 量的数据从这里输出，同时我们也有 X 量的数据从输入中流入。至少就输入和输出向量而言，我们实现了只进出 X 量数据的目标。
(32:55)
This leaves open the question of, like, I said that the weight matrix is stored locally in the systolic array. How did it get there in the first place? At some point you need to boot your chip and populate this data, and so where did that come from? The trick is just we just do it very slowly. So we very slowly trickle feed it in into the systolic array. The sort of the simplest strategy is that we sort of run this daisy chain that says like feed a number into here and then on the next clock cycle it'll move down to the next entry of the systolic array. And so we can do that in every column in parallel and that gives us the sort of This is also going to come from here, and this is going to be another factor of approximately X units of bandwidth coming in.
这开放了一个问题，我说权重矩阵在收缩阵列中本地存储。它最初是怎么到那里的？在某个时刻你需要启动芯片并填充这些数据，那么这些数据来自哪里？诀窍就是我们非常缓慢地将其引入。我们慢慢地将其灌入收缩阵列中。最简单的策略是运行这个菊花链，意思是将一个数字输入到这里，然后在下一个时钟周期它将移动到收缩阵列的下一个条目。所以我们可以在每一列并行执行，这也将是来自这里的，另一个大约是 X 单位带宽的输入。
Dwarkesh Patel:
(33:42)
Would you mind repeating that sentence one more time?
你能再重复一遍那句话吗？
Reiner Pope:
(33:45)
We know that we're going to be bringing in numbers only rarely into the matrix, and so we just want to come up with any construction at all such that the amount of wiring that actually crosses this boundary of the systolic array, like this boundary right here, we just want to keep that bounded to x and not go as xy. A particularly simple strategy is that we We bring in a number into the top row of the systolic array. That's what we can do in one clock cycle. For Y consecutive clock cycles, we're going to be bringing in the top row every time and then shift all of the other rows down by one.
我们知道在矩阵中只会很少引入数字，所以我们只想构造任何一种方法，使得实际穿过这个脉动阵列边界的布线量，就像这个边界一样，我们只想将其限制在 x 内，而不是 xy。一种特别简单的策略是，我们将在收缩数组的顶行中引入一个数字。这就是我们能在一个时钟周期内做到的事情。在 Y 个连续的时钟周期中，我们将每次引入顶行，然后将所有其他行下移一行。
(34:27)
And that keeps the wiring that needs to come from this expensive register file only down to a factor of X rather than X1. I see.
这使得必须来自于这个昂贵寄存器文件的布线只减少到一个 X 的因素，而不是 X1。我明白了。
Dwarkesh Patel:
(34:35)
Okay. So there's two questions in terms of communication. There's communication time and then there's communication And you're saying, since we're only going to be loading this in once, let's minimize bandwidth. That's right. Because bandwidth equals die area. And let's just load it in slowly over smaller lanes because we're just going to keep this value in there for a while. Interesting. So it's interesting to me that when we were talking last time about inference across many chips, The big high-level thing we're trying to optimize for is increase the amount of compute per memory bandwidth, that is to say, per communication. And here also, we're trying to increase the amount of actual multiplies or actual additions relative to transporting information from registers to the logic.
好的。关于通信有两个问题。有通信时间，以及通信。你是说，由于我们只会加载一次，我们尽量减少带宽。没错。因为带宽等于芯片面积。我们慢慢通过较小的通道将其加载，因为我们会在里面保留这个值一段时间。很有趣。所以我觉得有趣的是，当我们上次讨论多个芯片的推理时，我们试图优化的主要目标是提高每个内存带宽的计算量，也就是说，每次通信。在这里，我们也试图相对于将信息从寄存器传输到逻辑来增加实际的乘法或实际的加法数量。
(35:27)
So, in both cases, you're trying to maximize compute relative to communication.
因此，在这两种情况下，你都在努力最大化相对于通信的计算。
Reiner Pope:
(35:30)
Yeah, this shows up sort of all the way up and down the stack. This is sort of close to the bottom, sort of like to the gates. There's sort of a version that's maybe even closer to the gates of just like even the precision of number format that you choose to use. We saw that same effect. There's like a square cube law or like squared versus linear term going on both in just purely the precision of this ALU, but then also in terms of the size of the matrix.
是的，这在整个堆栈中都有所体现。这大致接近底部，类似于门电路。还有一种版本，可能甚至更接近门电路，就像是你选择使用的数字格式的精度。我们看到了同样的效果。这里存在平方立方定律，或者像平方与线性项的关系，既在纯粹的 ALU 精度中，也在矩阵的大小上。
Dwarkesh Patel:
(36:01)
Yeah. Very interesting.
是的。非常有趣。

Chip Sizing, Clock Cycles, and Pipeline Synchronization
芯片尺寸、时钟周期与流水线同步
Designing an AI chip involves balancing the size of systolic arrays against register file capacity to optimize area usage. Clock cycles serve as the global synchronization mechanism, requiring all logic to complete within a specific timeframe. Designers use pipeline registers to split complex logic into smaller, faster segments, allowing for higher clock frequencies at the cost of increased area. However, excessive pipelining can lead to diminishing returns, where the overhead of synchronization registers outweighs the throughput gains. Achieving the right balance is critical for maintaining both high performance and energy efficiency.
设计人工智能芯片涉及平衡脉动阵列的大小与寄存器文件容量，以优化面积使用。时钟周期作为全局同步机制，要求所有逻辑在特定的时间框架内完成。设计师使用流水线寄存器将复杂逻辑拆分为更小、更快的段，从而以增加面积为代价提高时钟频率。然而，过度的流水线设计可能导致收益递减，即同步寄存器的开销超过了吞吐量的增加。实现正确的平衡对维持高性能和能效至关重要。
Reiner Pope:
(36:03)
So this unit is sort of the next bigger unit. We had the multiplication circuit, and then on top of that, we have a pretty large systolic array. I drew it as 2x2, but for example, older TPUs, they were described as 128x128 of this circuit shown here. And This circuit ends up being, this is the most efficient known mechanism for, circuit for implementing a matrix multiply.
所以这个单元大致是下一个更大的单元。我们有乘法电路，然后在此基础上，我们有一个比较大的收缩阵列。我把它画成 2x2，但例如，旧的 TPU 被描述为这里显示的 128x128 电路。这个电路最终是实现矩阵乘法的已知效率最高机制。
Dwarkesh Patel:
(36:31)
I see. So we've talked about sort of It seems obvious that you should try to maximize compute relative to communication. What are non-obvious trade-offs that actually keep you up at night about should we do X or should we do Y? And it's not obvious what the answer is.
我明白了。我们讨论过，所以显然你应该尽量最大化相对于通信的计算。什么是那些非显而易见的权衡，实际让你失眠的关于我们应该做 X 还是做 Y？这个答案并不明显。
Reiner Pope:
(36:50)
Yeah. So, I mean, I think most of the decisions in chip design are sizing decisions. And so, already in what we've drawn so far, AI chips all have this circuit in it. They have a systolic array and then somewhere near it a register file providing inputs and outputs. The two, even within this scope, sizing questions that you have are, how big should I make my systolic array and how big should I make the register file? The trade-off for the size of the systolic array, actually these two questions are coupled, is One way to think of it is to say, I'm going to have a budget for what percentage of my chip area I want to spend on data movement.
是的。所以，我认为大多数芯片设计中的决策都是规模决策。到目前为止，我们所绘制的 AI 芯片上都有这个电路。它们有一个收缩阵列，然后在某个地方有一个寄存器文件提供输入和输出。即使在这个范围内，你面临的两个规模问题是，我应该将收缩阵列做多大，寄存器文件又应该多大？收缩阵列的规模权衡，实际上这两个问题是耦合的，可以这样理解：。我将为我的芯片面积要花费多少百分比在数据移动上设定一个预算。
(37:45)
So maybe I just say that I want this to be 10% and the systolic array to be 90%. And then I can size my register file. Bigger register files are more flexible. They allow me to run more. I can get more application-level performance out. But then they sort of take away from this area spent on the system.
也许我只是说我希望这占 10%，而收缩阵列占 90%。然后我可以调整我的寄存器文件的大小。更大的寄存器文件更灵活。它们让我能够运行更多。我可以获得更多的应用级性能。但它们又会消耗掉在系统上的面积。
Dwarkesh Patel:
(38:04)
I recently ran an essay contest where I asked people to write about what I consider to be some of the biggest open questions about AI. The submission window closed last week, so I used Cursor to create a couple of different interfaces to help me review the entries. One interface anonymizes submissions and hides unnecessary information. It lets me group responses by question, add notes, and record my scores. The other interface helps me review entrants who also want to be considered for the researcher role that I'm hiring for. The UI puts the applicant's essay right next to their resume and their personal website so that I can see everything at once.
我最近举办了一个作文竞赛，问人们写下我认为关于 AI 的一些最大开放问题。提交窗口上周关闭，所以我使用 Cursor 创建了几个不同的界面来帮助我审查条目。一个界面匿名化提交并隐藏不必要的信息。这样我可以按问题分组回复，添加备注，并记录我的评分。另一个界面帮助我审查那些也想被考虑为我正在招聘的研究人员角色的参与者。界面将申请人的文章放在他们的简历和个人网站旁边，这样我可以一次性看到所有内容。
(38:36)
Cursors Harness is really good at helping these models see and improve their UIs. I watched it render these interfaces in the built-in browser, take screenshots, click through sections, and keep iterating. At this point, Cursor is where I do most of my work. Whether I'm reading and visualizing a bunch of research papers, or coding up an interface to review applications, or making flashcards for my Blackboard lectures, Cursor just makes it very easy for an AI to look at whatever I'm looking at and help me understand it and work with me on it. So whatever you're working on, you should do it in Cursor. Where does the clock cycle of a chip come in? What determines what that is?
Cursor 的 Harness 在帮助这些模型查看和改进它们的 UI 方面非常出色。我看到它在内置浏览器中渲染这些界面，截屏，浏览各个部分，并不断迭代。到目前为止，Cursor 是我进行大部分工作的地方。无论我是阅读和可视化一堆研究论文，还是编写接口来审核申请，或者为我的 Blackboard 讲座制作抽认卡，Cursor 让人工智能轻松查看我正在查看的内容，帮助我理解并与我一起进行工作。所以无论你在做什么，最好在 Cursor 中进行。一个芯片的时钟周期是怎么回事？到底是什么决定了这个？
Reiner Pope:
(39:18)
Yeah.
是的。
Dwarkesh Patel:
(39:18)
And what is a clock cycle of a chip?
那么芯片的时钟周期是什么？
Reiner Pope:
(39:20)
So I guess at baseline, it's sort of worth observing that chips are incredibly, incredibly powerful, right? You've got 100 billion transistors in a chip. A key thing that you need to do whenever you have massive parallelism is you need to synchronize between the different parallel units. In software, typically, you have these very expensive synchronization methods like a mutex. So one thread will finish what it's doing. It will grab a lock somewhere stored in memory and then notify the other thread that it's done. On chips, we take a very different approach and say that Every nanosecond or so, all circuitry in the chip will pause for a moment and then synchronize.
我想一般来说，可以观察到芯片是非常非常强大的，对吧？一块芯片里有 1000 亿个晶体管。你需要在拥有大量并行性的情况下做的一件重要事情就是在不同的并行单元之间进行同步。在软件中，通常你有一些非常昂贵的同步方法，比如互斥锁。所以一个线程会完成它正在做的事情。它会在内存中获取一个锁，然后通知另一个线程它已经完成。在芯片上，我们的方法截然不同，我们说每纳秒左右，芯片中的所有电路会暂停片刻然后进行同步。
(40:03)
It actually synchronizes every single nanosecond or so. That is the clock cycle. The entire chip, typically all in one fell swoop, goes in lockstep to the next operation that happens. What this looks like in circuitry is that you will have It's typically drawn, so the clock is sort of mediated by registers, which are these storage devices that we've drawn elsewhere. And the way to think of it is that I have some storage, which is storing like a bit, which might be zero or one. And then I have some sort of cloud of logic, which maybe is like this systolic array or this multiplier or something like that. And then I've got some, and that's going to produce some output.
它实际上每纳秒左右进行一次同步。这就是时钟周期。整个芯片通常是一次性全速前进到下一个操作。这在电路中的表现是，你会有……它通常是绘制出来的，时钟是通过寄存器来调节的，这些通常是我们在其他地方绘制的存储设备。我们可以这样理解：我有一些存储，它存储的是一个比特，可能是零或者一。然后我有某种逻辑云，可能是这样的脉动阵列或乘法器或类似的东西。然后我有一些东西，那会产生一些输出。
(40:50)
So my inputs, I've got a bunch of inputs feeding into this cloud of logic. And then eventually later, there's going to be some output register that this writes to. There is a global clock signal which drives all of these registers, and it says at a certain instance in time when the clock strikes, whatever value happens to be on this wire at that instant, that's what's going to get stored in there. The challenge here is I would like to have my clock speed run as fast as possible because if I can run at two gigahertz, I can get twice as many operations done per second than if I run at one gigahertz.
所以我的输入，有一堆输入提供给这个逻辑云。然后最终会有一个输出寄存器来写入这个输出。有一个全局时钟信号驱动这些寄存器，它在某个时刻发出信号，当时钟开始时，在那个瞬间，这条线上的任何值将被存储在里面。这里的挑战是我希望我的时钟速度尽可能快，因为如果我能以 2 GHz 运行，那么每秒可以完成的操作数将是以 1 GHz 运行时的两倍。
(41:35)
But what that ends up meaning is that I'm very sensitive to the delay through this cloud of logic because any computation that is going to happen in here needs to finish before the next clock cycle hits. So, a major point of sort of optimization on any chip then is to sort of make this delay from here as short as possible.
但这就意味着我对这个逻辑云的延迟非常敏感，因为在这里要发生的任何计算都需要在下一个时钟周期到来之前完成。所以，任何芯片上的一个主要优化点就是尽量将这里的延迟缩短。
Dwarkesh Patel:
(42:04)
Interesting. And is there ever, because the constraint here seems to be that if you If you add too much logic, then you might risk missing the clock cycle. But if you don't add enough, then you're leaving potential compute on the table. Is there ever a situation where you'd take a probabilistic chance that a computation finishes? Or is it just like, no, either it's going to finish by clock cycle or not?
有趣。这种情况下，总是有这样的限制，就是如果你添加太多的逻辑，你可能会有错过时钟周期的风险。但如果你添加得不够，那你就会错失潜在的计算机会。有没有可能在某种情况下冒险计算完成？还是说，就只是，哦，要么在时钟周期前完成，要么不完成？
Reiner Pope:
(42:35)
Yeah. In standard chip design, you margin it such that, I mean, there is a probability, but it's like many, many standard deviations, like way standard deviations out such that for all intents and purposes, it is a reliable part. It will always meet the clock. There are some weird exceptions to that. There are clock domain crossings where you go from one clock to the other clock, and then you actually do have to reason about this probability.
嗯。在标准的芯片设计中，你会留出余量，我是说，确实有概率，但它像是多个标准差，远远超出，使得实际上，它是一个可靠的部件。它总是会符合时钟。其中有一些奇怪的例外情况。有时钟域交叉，当你从一个时钟切换到另一个时钟时，实际上你确实需要考虑这个概率。
Dwarkesh Patel:
(42:58)
Interesting.
有趣。
Reiner Pope:
(42:59)
In the main path, you just, like, you margin it such that you'll get there, like, 25% of the clock cycle in advance, so that it's very unlikely.
在主路径中，你只需留出余量，使得你将在时钟周期开始前的 25% 处达到，因此事情是非常不可能的。
Dwarkesh Patel:
(43:09)
In this, the clock... Where the clocks synchronize, I guess, where the registers are, this is not something you determined as a chip designer. This is sort of just like an artifact of, hey, I want whatever sequence of logic. And then the software you use to convert your Verilog into the thing you send to TSMC, that just determines like, hey, in order to make this work, you got to put a register here, here and here to make sure that there's no one step That is like too long such that it makes the whole clock cycle of the entire chip longer than it has to be.
在这里，时钟……时钟同步的地方，我想，那些寄存器的位置，这不是你作为芯片设计师决定的。这有点像是，我想要的任何逻辑序列的一个副产品。然后你用来将 Verilog 转换成发送给 TSMC 的东西的软件，决定了，为了使其正常工作，你必须在这里、这里和这里放置寄存器，以确保没有一段步骤过长，以至于使整个芯片的时钟周期比必要的要长。
Reiner Pope:
(43:47)
Yeah. So, this is actually a huge part of the work of designing a chip actually is inserting them. So, it is done in a combination of manually and automatically. So, I mean like just like to show the very sort of dumb version of like what you can do here, you can take this logic and split it in half. And so, like say actually instead of just one cloud of logic, I'm gonna I have two smaller clouds of logic, which do the same thing, but split them up by a register.
是的。所以，这实际上是设计芯片工作中一个重要的部分，就是插入它们。这是一种手动和自动结合的方式来完成的。我是说，就像展示你在这里可以做的非常简单的版本，你可以把这个逻辑分成两半。所以，我的意思是，实际上，我有两个更小的逻辑云，而不是只有一个逻辑云，它们做同样的事情，但通过一个寄存器将它们分开。
Dwarkesh Patel:
(44:16)
Right.
对。
Reiner Pope:
(44:17)
Feeding in like this. And this is like, like if you split it like in the middle, you can hit twice the clock frequency. That's great. You get twice the performance at the cost of this extra register. And so at the cost of some more storage.
像这样输入。如果你把它分成中间，你可以达到两倍的时钟频率。这太棒了。你以额外的这个寄存器为代价获得两倍的性能。所以，这会增加一些存储的成本。
Dwarkesh Patel:
(44:32)
And so stepping back, why do we need to synchronize the whole chip? Like if you have like, if you imagine playing Factorio or something, there's no like global clock cycle. It just, shit is done when it's done. There's iron on the plate. You can take it if you want.
那么回过头来，为什么我们需要同步整个芯片？就像如果你想象玩 Factorio 或其他游戏，没有全球时钟周期。一切都是在完成的时候完成的。板上有铁块。如果你想，可以拿走。
Reiner Pope:
(44:45)
Taking that analogy, the thing that you need to be mindful of is if I've got two different paths through some logic, so I have to do a computation like F here and then computation G here, and then they're going to come and meet for computation H somewhere here. There's going to be manufacturing variants here. In some chips, F will take a little longer. Maybe in some chips, G will take a little bit longer. And so if I've got some signal that's propagating through here and the result from F and G have to sort of meet up at H, the thing that can go wrong is that F can get there early and it meets the previous value of G or the next value of G.
以这个类比，你需要注意的是，如果我有两条不同的路径通过某些逻辑，所以我必须在这里做一个计算 F，然后在这里做计算 G，然后它们将在这里某处相遇进行计算 H。在这里会有制造方面的差异。在某些芯片中，F 可能会花费更长的时间。也许在某些芯片中，G 可能会花费更长的时间。所以如果我有一些信号在这里传播，并且 F 和 G 的结果必须在 H 处相遇，可能出错的地方是 F 可能提前到达，并与 G 的前一个值或下一个值相遇。
Dwarkesh Patel:
(45:29)
And H needs to know when to start.
H 需要知道什么时候开始。
Reiner Pope:
(45:31)
Exactly.
没错。
Dwarkesh Patel:
(45:32)
When has this next iteration of And so this explains why different chips made at the same process node, the same like TSMC technology, can have different clock cycles. Two chips made at three nanometer might have different clock cycles based on Whether they were able to optimize making sure that there's no one critical path that is so long that it slows down the whole chip's clock cycle.
这次迭代的开始时间。那么这也解释了为什么在相同工艺节点、相同的 TSMC 技术下，不同的芯片可以有不同的时钟周期。制作于三纳米的两个芯片可能会有不同的时钟周期，取决于它们是否能够优化，以确保没有一个关键路径过长，从而减缓整个芯片的时钟周期。
Reiner Pope:
(46:01)
That's right. This optimization that I showed here, this is just the pipeline register insertion, it's called. We've inserted in the middle of the pipeline a register here. This is a pure trade-off between clock speed and an area. This is the easy case. There is a harder case too, which is sort of drawn as a pipeline of logic here, but in other cases you may have some Some calculation which actually feeds back in on itself. So it runs some function F and then writes back to itself like this. So for example, this might be this addition, like you've got some number that you're adding into every clock cycle. And so this could be like a plus where adding in some number every clock cycle. Mm-hmm.
对的。我在这里展示的优化，称为流水线寄存器插入。我们在流水线中间插入了一个寄存器。这是时钟速度和面积之间的纯权衡。这是简单的情况。还有更复杂的情况，这里画成了逻辑流水线，但在其他情况下，你可能会有一些计算实际上是反馈到自己的。因此，它运行一些函数 F，然后像这样写回自身。举例来说，这可能是这个加法，比如你在每个时钟周期中要添加的某个数字。因此，这可以理解为一个加法，每个时钟周期中添加一个数字。嗯嗯。
(46:53)
So this little circuit, essentially, it's just going to sum all of the numbers that you presented on different clock cycles. And the challenge is, if this plus takes too long, what can I do? If I try and put a pipeline register right in the middle of it, like here in the middle of it, This will end up changing the computation that's done. Instead of forming a running sum of everything that comes here, I will actually have two different running sums. I'll end up having a running sum of the even numbers and a running sum of the odd numbers. So this constraint where I have a loop in my logic, which all chips have somewhere, this is actually the thing that is the hardest thing to address and sets the clock cycle.
所以这个小电路，基本上它将对你在不同的时钟周期中呈现的所有数字进行求和。挑战是，如果这个加法运算耗时太长，我该怎么办？如果我试着在中间放一个流水线寄存器，就像这里这样，这将最终改变所做的计算。我不会形成这里所有输入的运行总和，而是会有两个不同的运行总和。我将得到一个偶数的运行总和和一个奇数的运行总和。因此，在我的逻辑中有一个循环的约束，所有芯片都有这样的约束，这实际上是最难解决的事情，并且决定了时钟周期。
Dwarkesh Patel:
(47:39)
I don't understand why it would be a problem to have that, or I'm not sure even what it would mean to have a register there. I think it's a sort of atomic operation, right?
我不理解为什么将其放在那是个问题，或者我甚至不确定在那里的寄存器意味着什么。我认为这是一个原子操作，对吧？
Reiner Pope:
(47:47)
Yeah. Well, so PLUS is not really atomic.
是的。好吧，PLUS 并不是真正的原子操作。
Dwarkesh Patel:
(47:50)
As you just demonstrated.
正如你刚刚演示的那样。
Reiner Pope:
(47:51)
Yeah. It took a whole lot of work to do a summation. And so you can take the early parts of that work and then stick a register in the middle and then take the late parts of that work. Got it.
是的。进行求和花费了很多工作。因此，你可以先进行早期的工作，然后在中间插入一个寄存器，然后进行后期的工作。明白了。
Dwarkesh Patel:
(47:59)
Okay. Yeah. And I guess it's then up to... So TSMC offers a PDK, which says, hey, here's the primitives of... Logic that we can grant you in the chip. And it's up to them to determine that no primitive is bigger than like the clock cycle they're hoping a process node targets. But other than that, is there like what further optimization? Can't you just say like, hey, here's all the primitives from TSMC? And keep adding registers in between the primitives as much as is needed until you get to your desired clock cycle.
好的。是的。我想事情就得交给... TSMC 提供了一种 PDK，告诉你，嘿，这里是我们可以在芯片中提供的基本逻辑。他们需要决定没有基本逻辑比他们希望的工艺节点目标的时钟周期更大。除此之外，还有没有其他优化？难道你不能说，嘿，这里是所有来自 TSMC 的基本逻辑吗？然后在基本逻辑之间添加尽可能多的寄存器，直到达到所需的时钟周期。
Reiner Pope:
(48:34)
Yeah, as a logic designer, like the chip architects set the clock cycle. So just for one example, The primitives you get from TSMC are on the order of like AND gates or full adders. They depend a lot on voltage and which library you choose and so on. But generally, you can typically have about like 10 or 20 or 30 of these in a clock cycle sequentially. So these primitives are very, very fast, like 10 picoseconds or something like that. And so as a logic designer, I mean, like in principle, if you literally just had like register and then AND gate kind of in a loop like that, you could get insanely fast clock speed, like more than four or five, six gigahertz, something like that.
是的，作为逻辑设计师，芯片架构师设定时钟周期。作为一个例子，来自 TSMC 的基本逻辑大致上是与与与门或全加器相关的。它们在很大程度上依赖于电压以及你选择的库等等。但通常情况下，你可以在一个时钟周期中顺序使用大约 10、20 或 30 个。因此，这些基本逻辑非常快，大约 10 皮秒或类似的。作为逻辑设计师，原则上，如果你只是在一个循环中有寄存器和与门，你可以获得极快的时钟速度，超过四、五、六千兆赫兹之类的速度。
(49:21)
But if you take this really simple circuit and you look at the area you're spending here, this is called one gate equivalent in size, so unit of one in area, and this thing is unit of eight in area or something like that. Again, almost all of your cost has been this like synchronization or communication cost compared to the actual logic. And so this would be a case where you've gone too far. You've made your clock speed really, really fast at the cost of spending almost all of your area on pipeline registers.
但如果你把这个非常简单的电路拿出来，看看你在这里花费的面积，这被称为一个门等效面积，因此是单位面积的一个，而这个东西的面积单位是八或什么的。再次强调，几乎所有的成本都是这个同步或通信成本，与你实际的逻辑相比。因此，这将是你走得太远的一个案例。你让时钟速度变得非常快，以至于几乎所有的面积都花在了流水线寄存器上。
Dwarkesh Patel:
(49:58)
Interesting. So what you're hinting at is a dynamic where you can have really fast clock speed, but you're not getting that much work done.
有趣。所以你暗示了一种动态关系，你可以拥有非常快的时钟速度，但却没有完成多少工作。
Reiner Pope:
(50:05)
Yeah.
对的。
Dwarkesh Patel:
(50:06)
And so you can have like low latency, but low bandwidth.
因此，你可能有低延迟，但带宽也低。
Reiner Pope:
(50:13)
It hurts your throughput, in fact, because the throughput of your chip you can think of as the product of how much I can get done per clock cycle, which is based on this area efficiency thing, times how many clocks I get per second.
实际上，这会影响你的吞吐量，因为你可以将芯片的吞吐量视为每个时钟周期内能完成多少工作，这基于该面积效率，再乘以每秒钟的时钟数量。
Dwarkesh Patel:
(50:26)
This is actually so similar to the thing we were discussing last time about batch size Where if you have a low batch size, then any one user can receive their next token really fast. But the total number of tokens that are processed in, say, an hour will be kind of lower than it could otherwise be.
这实际上与我们上次讨论的批量大小非常相似。如果你有一个低的批量大小，那么任何一个用户都可以非常快地收到他们的下一个令牌。但处理的总令牌数，比如在一个小时内会低于其他情况。
Reiner Pope:
(50:45)
Yeah, exactly. You get less parallelism out if you drive your clock speed up.
是的，正是如此。如果你提高时钟速度，你的并行性就会减少。
Dwarkesh Patel:
(50:49)
Language models are starting to compete against the best human forecasters. I sat down with two senior Jane Streeters, Ron Minsky and Dan Pontecorvo, and asked, at some point, does AI just do what Jane Street does?
语言模型开始与最优秀的人类预测者竞争。我和两位高级的 Jane Streeters，Ron Minsky 和 Dan Pontecorvo 坐下来讨论，有没有可能 AI 会做 Jane Street 做的事？
Unknown Speaker:
(51:01)
There's a world that we should take seriously where, you know, we're going to build large language models or some other AI systems that are like strictly smarter than all humans on the planet and more capable at all cognitive tasks. Trading in particular feels to me as like kind of AGI complete, sort of like NP complete, because at the end of the day, Trading involves figuring out what things are worth, which means making predictions about the future.
我们应该认真对待这样的世界，您知道，我们将构建大型语言模型或其他某些 AI 系统，严格比地球上所有人都更聪明，在所有认知任务上更具能力。交易特别让我觉得有点像 AGI 完全，就像 NP 完全一样，因为归根到底，交易涉及弄清楚物品的价值，这意味着做出关于未来的预测。
Dwarkesh Patel:
(51:27)
Jane Street isn't betting against AI. They just signed a $6 billion compute deal. But Ron's view is that the edge keeps moving.
Jane Street 并不是在押赌 AI。他们刚刚签署了一项价值 60 亿美元的计算协议。但 Ron 的看法是，优势在不断变化。
Unknown Speaker:
(51:33)
I have never been more desperate to hire more engineers and more traders than I am today. You know, you have the usual thing of like the other hard parts that we don't yet know how to automate. Well, that ends up being where the competitive edge lies.
今天，我从未如此渴望招聘更多的工程师和交易员。你知道，还有一些我们尚不知道如何自动化的困难部分。好吧，这正是竞争优势所在。

FPGA Architecture and Deterministic Latency
FPGA 架构与确定性延迟
FPGAs provide a flexible alternative to ASICs by using lookup tables (LUTs) and MUXes to emulate logic gates. While ASICs are more energy-efficient and cost-effective for mass production, FPGAs allow for rapid reconfiguration, making them ideal for applications requiring deterministic latency, such as high-frequency trading. The overhead of FPGAs stems from the complexity of the programmable routing and the LUTs, which require significantly more gates to implement simple functions compared to hardwired ASIC logic. Despite this, the ability to maintain precise control over timing makes them a vital tool in specialized computing environments.
FPGA 通过使用查找表（LUT）和 MUX 来模拟逻辑门，为 ASIC 提供了一种灵活的替代方案。尽管 ASIC 在大规模生产中更具能耗效率和成本效益，但 FPGA 允许快速重新配置，使其非常适合需要确定性延迟的应用，如高频交易。FPGA 的开销源于可编程路由和 LUT 的复杂性，相较于硬件 ASIC 逻辑，实施简单功能所需的门数显著增加。尽管如此，能够对时序进行精确控制使其在专用计算环境中成为重要工具。
Dwarkesh Patel:
(51:45)
You can find these open positions and watch the full interview at janestreet.com slash dwarkesh. Okay, so I remember talking to an FPGA engineer at Jane Street, Clark, who actually helped me prep for the previous interview we did together, and he was explaining why they use FPGAs. I imagine that for high-frequency trading, throughput is less important than latency, and so having very specific control over the clock cycle in a deterministic way is the most important thing. Maybe it'd be interesting to talk about why you can't just achieve that with an ASIC or why you might use an FPGA too. Have deterministic clock cycles for like high frequency trading?
你可以在 janestreet.com slash dwarkesh 找到这些空缺职位并观看完整的采访。好吧，我记得和 Jane Street 的 FPGA 工程师 Clark 交谈，他实际上帮助我准备了我们之前的访谈，他在解释他们为什么使用 FPGA。我想，对于高频交易，吞吐量不如延迟重要，因此以确定的方式非常具体地控制时钟周期是最重要的。也许谈谈为什么你不能仅仅用 ASIC 实现这一点，或者为什么你也可能使用 FPGA。有高频交易的确定性时钟周期？
Reiner Pope:
(52:34)
Yeah. So, I mean, firstly, like, let's consider the sort of the business case for an FPGA versus an ASIC. FPGAs and ASICs use largely the same sort of conceptual model, which is that I have a series of gates built from ANDs, ORs, XORs, those like very small primitives, connected together with a fixed clock cycle and connected together with wires that are running in a fixed clock cycle. So anything you can express in an FPGA, you can express in an ASIC too, and it'll be about an order of magnitude cheaper and better energy efficiency on an ASIC than an FPGA.
是的。首先，让我们考虑 FPGA 和 ASIC 的业务案例。FPGA 和 ASIC 在概念模型上基本相同，就是我有一系列由与门构成的门，或或门、异或门等非常小的基本逻辑，连接在一起，具有固定的时钟周期，并通过运行在固定时钟周期的电缆连接在一起。所以你在 FPGA 上能够表达的任何内容，你也可以在 ASIC 上表达，而且 ASIC 的成本大约会便宜一个数量级，能效也更好。
(53:12)
The trade-off is that the first FPGA costs you  30 million because it requires an entire tape out. So the business use case for an FPGA would be that I want something that has this very deterministic latency and fast runtime and high parallelism. But I'm going to change it very frequently, change what I do every month or something like that, and so then I don't want to pay the payback cost every time. Now, how does an FPGA actually implement? It emulates the ASIC programming model, but in a fixed piece of hardware. How does that work, actually? What it has at the base is it's got the two components we just talked about.
权衡是，第一个 FPGA 的成本是  3000 万，因为它需要整套的流片。所以 FPGA 的商业使用案例就是我想要一些具有非常确定的延迟、快速运行时间和高并行性的东西。但我会非常频繁地更改每个月做的事情或类似的事情，所以我不想每次都支付回报成本。现在，FPGA 是如何实现的呢？它模拟了 ASIC 编程模型，但在一个固定的硬件中。这实际上是如何工作的？它的基础是我们刚刚谈到的两个组件。
(54:05)
It's got these registers as storage devices. And then it's got these, these are called LUTs, lookup tables. which actually provide all of the gates. Then we're going to see even the third component, we then have a swarm of these registers and lots. And all of these are available, and then they're connected by sort of this big set of sort of muxes. So in front of every single one of these, we've got something like one of these muxes, which selects one input from everywhere else, sort of selecting from all of these things. You know, we've got a whole bunch of different options feeding into all of these things. So what this allows is essentially, when I program my FPGA, I can say that I'm going to take all of these components and I'm going to superimpose on top of this a particular wiring which goes through this lot and then feeds into this lot and then goes to this register and then feeds into this lot or something like that.
它有这些寄存器作为存储设备。然后它有这些，称为 LUT 的查找表。它们实际上提供了所有的逻辑门。然后我们甚至会看到第三个组件，我们有一群这样的寄存器和大量资源。所有这些都是可用的，然后它们通过一组大型多路复用器连接在一起。所以在每一个这样的前面，我们有类似于这些多路复用器的东西，它从其他地方选择一个输入， sort of 从所有这些东西中选择。你知道，我们有很多不同的选项输入到所有这些东西中。所以这允许我在编程我的 FPGA 时，可以说我将把所有这些组件叠加在一起，并在上面加上一个特定的线路，这条线路经过这一部分，然后进入这一部分，再到这个寄存器，然后再进入这一部分，或者类似的东西。
(55:26)
So, what I've drawn in orange is FPGA means Field Programmable Gate Array. The orange is what has been programmed in the field, whereas the white is all of the wires that must exist in the FPGA in order to actually make the device in the first place.
所以，我用橙色画出的 FPGA 是指现场可编程门阵列。橙色部分是现场编程的内容，而白色部分是 FPGA 中必须存在的所有线，以便于实际制造该设备。
Dwarkesh Patel:
(55:41)
What does it mean to be programmed into a field?
被编程到现场是什么意思？
Reiner Pope:
(55:43)
Programmed in the field. So, the device has been deployed in a data center, it's sitting in the field, and then you can come and program it.
在现场编程。所以，该设备已经在数据中心部署，它就在现场，然后你可以过来对它进行编程。
Dwarkesh Patel:
(55:48)
Not field as in electric field, but field as in out there in the world field. How the field programming comes out of the first lookup table and goes into the second one. How is it? Yeah, how?
这里的 “现场” 不是指电场，而是指世界上的 “现场”。现场编程是如何从第一个查找表出来，然后进入第二个查找表。怎么样？是的，怎么做？
Reiner Pope:
(56:07)
Like, where are the wires that made that happen?
像是，造成这一切的线路在哪里？
Dwarkesh Patel:
(56:09)
Yeah.
是的。
Reiner Pope:
(56:10)
So I got a little bit, like, lazy in drawing all of these. Every single device here has a MUX sitting in front of it, which can select from all of the, like, nearby, like, circuits that are available.
所以我画这些图的时候有点懒。这里每一个设备前面都有一个 MUX，可以从附近的所有电路中选择。
Dwarkesh Patel:
(56:26)
Yeah.
是的。
Reiner Pope:
(56:26)
And so the actual configuration of the FPGA is, like, Amounts to it is the MUX control. So like we in this MUX here we have the data inputs and then we have like the control that selects. And so like there's a little storage device sitting next to every single one of these. Marks is saying, this is where you're going to source your input from. And so programming it consists of like configuring every single one of these boxes.
所以 FPGA 的实际配置就是，归根结底就是 MUX 控制。在这个 MUX 中，我们有数据输入，然后我们还有选择性的控制。所以每一个这样的旁边都有一个小的存储设备。这个标记表示，你将从这里获取你的输入。所以编程的过程就是配置每一个这些框。
Dwarkesh Patel:
(56:58)
So that makes sense. What is happening inside of the lookup table?
所以这很有道理。查找表里发生了什么？
Reiner Pope:
(57:00)
Yeah. So the purpose of the lookup table, so it's going to also have a little bit of control feeding, telling it what to do as well. The purpose of the lookup table is to function, to be able to configurably take the role of an AND gate or gate XOR, any of those different things. So there's many ways you could consider doing that. The way it is done in sort of traditional FPGAs is to say it will support So a lookup table will have four bits of input, one bit of output. How many different functions are there from four bits to one bit? There are 16 different functions. You can actually just tabulate this as 16 different numbers. You've got a table of 0, 1, 1, 1, 0, 0, 1, 16 entries.
是的。查找表的目的，所以它也会有一些控制信号，告诉它该做什么。查找表的目的是能灵活地充当与或门或异或门等多种功能。这些不同的功能。所以有许多方法可以考虑这样做。在传统 FPGA 的做法上，是说它会支持。所以一个查找表会有四个位输入，一个位输出。从四个位到一个位有多少不同的函数？有 16 种不同的函数。你实际上可以将其列为 16 个不同的数字。你有一个表，内容是 0, 1, 1, 1, 0, 0, 1，共有 16 个条目。
(58:00)
And so what it does is this table is stored in this blue configuration bit and then it views these four bits as binary, looks up the relevant row of the table and emits that bit. So this is a truth table view of lookup tables, essentially.
这张表存储在这个蓝色配置位中，然后把这四个位视为二进制，查找表的相关行并发出那个位。所以这 essentially 是查找表的真值表视图。
Dwarkesh Patel:
(58:22)
Okay, so the lookup table, if you think about it, NAND gate, OR gate, NOR gate, XOR gate, these are all like take as input.
好吧，所以查找表，如果你考虑到与与门、或门、或非门、异或门，这些都是作为输入来处理的。
Reiner Pope:
(58:29)
Those are like two input functions. Sometimes we have like more complicated, like a three input function would be a three-way XOR.
那些都是双输入函数。有时我们会有更复杂的，比如三输入函数会是三路异或。
Dwarkesh Patel:
(58:35)
Right.
对。
Reiner Pope:
(58:36)
Or a four-way XOR.
或者四路异或。
Dwarkesh Patel:
(58:37)
And in this case, how many, it just depends how big it is?
在这种情况下，多少，取决于大小？
Reiner Pope:
(58:40)
Typical size for LUTs is four input, which is sort of just a sweet spot between There's another communication trade-off like here, like if it has too few inputs, then you need to use more lots.
通常 LUT 的大小是四个输入，这在与其他的通信权衡之间是一个平衡点。如果输入太少，那么需要使用更多的 LUT。
Dwarkesh Patel:
(58:53)
Yeah. But basically the lookup table is like a truth table.
是的。但是基本上查找表就像是真值表。
Reiner Pope:
(58:56)
It's a truth table. Yeah.
它就是一个真值表。是的。
Dwarkesh Patel:
(58:57)
And with a truth table, you can program in any gate you want.
有了真值表，你可以编程任何你想要的门。
Reiner Pope:
(59:00)
That's right.
没错。
Dwarkesh Patel:
(59:01)
And so is it a lookup table just thinks like a programmable gate?
所以查找表是否就像是一个可编程的门？
Reiner Pope:
(59:04)
That's right. One of the things you can do here is you can see why the rule of thumb that an FPGA is like an order of magnitude more expensive than an ASIC comes from, is to count how many gates would be inside this lookup table. So we can view this lookup table essentially as one of these muxes. And so it is a mux with, has to select between 16 different values. And so it is a mux with sort of n equals 16 options. P equals one bits. And so what we saw way earlier is that this circuit costs like N times P many gates. And so it's like, so it costs like N times P equals 16 AND gates and also 16 ORs.
没错。你可以在这里看到的一件事情是，为什么 FPGA 的经验法则是比 ASIC 贵一个数量级，是要计算这个查找表里有多少门。所以我们可以将这个查找表视为这些 MUX 之一。所以它是一个选择 16 个不同值的 MUX。所以它是一个选择有 n=16 选项的 MUX。P 等于 1 位。而我们很早之前看到的电路大约需要 N 乘以 P 个门。所以它大约需要 N 乘以 P 等于 16 的与门和 16 个或门。
Dwarkesh Patel:
(1:00:00)
This circuit being the MUX.
这个电路是 MUX。
Reiner Pope:
(1:00:02)
Yeah, exactly. The MUX. The MUX is the core.
是的，没错。MUX。MUX 是核心。
Dwarkesh Patel:
(1:00:04)
The MUX that goes into the lookup table.
进入查找表的 MUX。
Reiner Pope:
(1:00:06)
So the lookup table itself, you can think of as being actually a big MUX that like selects from all 16 rows down to one output.
所以查找表本身可以认为是一个大型 MUX，选择从所有 16 行到一个输出。
Dwarkesh Patel:
(1:00:14)
Yeah, okay.
是的，好的。
Reiner Pope:
(1:00:15)
That is the lookup table.
这就是查找表。
Dwarkesh Patel:
(1:00:16)
But the way you've drawn it here, there's like a MUX and then a lookup table.
但你这样画时，看来有一个 MUX 然后是查找表。
Reiner Pope:
(1:00:19)
It's MUXs all the way down. So I mean, there's a second MUX that is inside here. This MUX is this MUX.
是的，下面全是 MUX。所以我的意思是，这里有第二个 MUX。这个 MUX 就是这个 MUX。
Dwarkesh Patel:
(1:00:25)
Got it, okay. And then the other MUX is just saying.
明白了，好的。然后另一个 MUX 只是说。
Reiner Pope:
(1:00:29)
Where it came from in this sort of mess of gates.
它在这堆门中来自哪里。
Dwarkesh Patel:
(1:00:32)
And then the second mux is, OK, now you have one value, but that value is still still a four bit value.
然后第二个 MUX 是，好的，现在你有一个值，但这个值仍然是四位的值。
Reiner Pope:
(1:00:40)
Yeah. So I've selected four bits from the soup.
是的。所以我从这些 “汤” 中选择了四个位。
Dwarkesh Patel:
(1:00:43)
Right.
对。
Reiner Pope:
(1:00:43)
And then and then I use those four bits to select which entry in the lookup table I'm going to use.
然后我使用那四个位来选择我要使用的查找表中的条目。
Dwarkesh Patel:
(1:00:49)
Right. OK. So like suppose in the first mux there's like eight nearby You're pulling from eight nearby registers as input. And so that's a total of like 32 bits going in. And then out of that, four bits come out. Those four bits go into the second mux, which is inside the lookup table.
对。好的。所以假设在第一个 MUX 中有八个附近的寄存器作为输入。所以总共有大约 32 位输入。然后其中四个位输出。这四个位进入查找表内部的第二个 MUX。
Reiner Pope:
(1:01:11)
So actually, I would say in this case, these registers are single bit registers. So if there are eight nearby registers and lookup tables, then I have eight bits total coming in nearby. I select from eight down to four different values. So there's actually like four different muxes, one associated with each of these inputs. Little bucks associated with each of these input bits, each of them is selecting one out of eight.
所以实际上我会说在这种情况下，这些寄存器是单位寄存器。所以如果有八个附近的寄存器和查找表，那么我总共有八个位输入。我从八个选择到四个不同的值。所以实际上有四个不同的 MUX，每个输入一个。每个都选择八个中的一个。
Dwarkesh Patel:
(1:01:37)
And where are those eight coming from?
那么这八个来自哪里？
Reiner Pope:
(1:01:39)
Nearby registers and other lots.
附近的寄存器和其他 LUT。
Dwarkesh Patel:
(1:01:41)
And each register is one bit?
每个寄存器都是一位吗？
Reiner Pope:
(1:01:42)
Yes. Yeah.
是的。嗯。
Dwarkesh Patel:
(1:01:44)
And so I guess AMD or whoever makes these FPGAs still has to be opinionated about what registers are connected to which registers. And then you can program in the actual gates, but they add a wire in the connection, like the communication topology, right?
所以我想 AMD 或者其他制造这些 FPGA 的公司仍然必须对哪些寄存器连接到哪个寄存器有明确的看法。然后你可以编程实际的逻辑门，但它们在连接中添加了一根线，就像通讯拓扑对吧？
Reiner Pope:
(1:02:03)
Yeah. So there's the sort of like you get flexibility in a local grain thing. There's a sort of nearby neighborhood where you can select from. But then more grossly, like more coarsely, longer distant connections, they form an opinion.
嗯。所以有一种像是你在局部层面上获得灵活性。还有一种附近的邻域，你可以选择。但更粗略地说，像是更长距离的连接，它们会形成一种观点。
Dwarkesh Patel:
(1:02:16)
Right.
对。
Reiner Pope:
(1:02:16)
Yeah.
嗯。
Dwarkesh Patel:
(1:02:16)
And the reason it's 10x slower is why?
它为什么会慢 10 倍？
Reiner Pope:
(1:02:19)
So if you look at the cost of like building this lookup table, it's like 32 gates. And then it can give me the equivalent of like, what's one interesting thing I can do here? I can do a four-way AND gate. And so that's like, I am using 32 gates of lookup table to sort of implement like a four-way AND means like, what is a four-way AND? I would do like AND, AND, and then AND of AND. This is a circuit that I could implement in an ASIC directly using these three AND gates, but using a LUT, I can also implement it, but it's going to take these 32 gates instead of three.
所以如果你看一下构建这个查找表的成本，大约是 32 个逻辑门。然后它可以给我相当于我可以在这里做的一个有趣的事情是什么？我可以做一个四路与门。所以这就是我使用 32 个查找表门来实现像四路与门的方式，四路与门是什么意思？我会做与、与，然后与与的与。这是我可以直接在 ASIC 中使用这三个与门实现的电路，但使用 LUT，我也可以实现它，但这会使用 32 个门而不是 3 个。
Dwarkesh Patel:
(1:02:57)
So the overhead is really coming from the fact that the MUX in the lookup table is There's a more concise way to describe a truth table than listing out every single possible combination of inputs, which is just to like write out the gate.
所以开销确实来自于查找表中的 MUX，描述真值表有更简洁的方式，而不是列出所有可能的输入组合，也就是直接写出这个门。
Reiner Pope:
(1:03:19)
Yeah, like to place down the polysilicon and the lattice and so on.
嗯，就像放置多晶硅和晶格等等。
Dwarkesh Patel:
(1:03:23)
That's right. Yeah, yeah. Interesting. One important point you made to me is that the reason they prefer FPGAs to CPUs is because they get deterministic clock cycles. They know when a packet will come in and go out. Why is it not a guarantee in CPUs?
没错。嗯，嗯。有趣。你告诉我的一个重要点是他们更喜欢 FPGA 而不是 CPU 的原因是因为他们得到确定性的时钟周期。他们知道包什么时间会进来和出去。为什么在 CPU 中没有这种保证？
Reiner Pope:
(1:03:38)
So you can actually design a CPU that has deterministic latency as well. And in fact, the processors that are inside a lot of AI chips actually also have deterministic latency too. Grok has advertised this. TPUs have that in the core as well. The challenge is getting sort of deterministic latency and high speed at the same time. And so where does the non-determinism in latency come from? Non-deterministic latency comes from specific design choices in a CPU. It's actually possible to remove those design choices and make a CPU that has deterministic latency. Those are not very attractive in the market, and so people don't make those CPUs anymore.
所以你实际上可以设计一个具有确定性延迟的 CPU。而且实际上，很多 AI 芯片内部的处理器也有确定性延迟。Grok 已经宣传过这一点。TPU 也在其核心中具备这一点。挑战是同时获得确定性延迟和高速。那么延迟中的非确定性来自哪里？非确定性延迟来自于 CPU 中的特定设计选择。实际上可以消除这些设计选择，制造出具有确定性延迟的 CPU。这些在市场上并不太受欢迎，所以人们不再制造这些 CPU。
(1:04:25)
But actually, in some sense, deterministic latency is maybe a simpler designing starting point. Then some chip designers have added things into it to be non-deterministic. To take a concrete example of that, probably the most important example is on a CPU just like the CPU cache itself. So in a CPU, you have the CPU. This is the CPU die itself, and then there is a memory off on the side. This is the DDR memory off on the side. And then you have a cache system here. Inside it is the cache. That sort of remembers recent accesses to DDR and stores them. And so when I'm running through my CPU instructions, every time I have an instruction that accesses memory,
但实际上，从某种意义上说，确定性延迟可能是一个更简单的设计起点。然后有些芯片设计者在其上添加了一些东西，使其变得非确定性。举个具体例子，最重要的一个例子就是 CPU 就像 CPU 缓存本身。所以在 CPU 中，你有 CPU。这是 CPU 芯片本身，然后旁边有一个内存。这是旁边的 DDR 内存。然后你有一个缓存系统。里面就是缓存。那个缓存会记住最近对 DDR 的访问并存储它们。所以当我执行 CPU 指令时，每次有访问内存的指令，

CPU Architecture and High-Level Comparisons to Biological Systems
CPU 架构与生物系统的高级比较
Modern CPU architecture relies on caches to bridge the speed gap between processors and memory, though this introduces non-deterministic latency. In contrast, accelerators like TPUs often use scratchpad memory, where software explicitly manages data movement to ensure predictable performance. Beyond memory, CPUs dedicate significant area to branch predictors to maintain high clock speeds despite instruction dependencies. Comparing these silicon-based systems to biological brains reveals fundamental differences in sparsity and energy consumption; while silicon chips prioritize high-speed, batch-processed throughput, biological systems operate with lower clock speeds and unstructured sparsity, offering unique insights into future hardware design.
现代 CPU 架构依靠缓存来弥补处理器与内存之间的速度差距，尽管这引入了非确定性延迟。相比之下，TPU 等加速器通常使用临时存储器，软件显式管理数据移动以确保可预测的性能。除了内存外，CPU 还将相当大的区域专用给分支预测器，以保持高速时钟频率，尽管存在指令依赖关系。将这些硅基系统与生物大脑进行比较揭示了稀疏性和能耗的根本差异；硅芯片优先考虑高速、大批量处理的吞吐量，而生物系统在较低的时钟速度和无结构的稀疏性下运行，提供了对未来硬件设计的独特见解。
Reiner Pope:
(1:05:24)
it first checks in cache, was the data stored in cache, and then if not, it goes, it fetches out to DDR. This is a huge optimization. The cache is like two orders of magnitude faster than DDR. If you never use the cache, basically all programs would run 100 times slower. So the presence of a cache is absolutely necessary for a CPU to run at reasonable speed. But Whether or not you get a cache hit is dependent on the ambient environment of the CPU, like what other programs are running, what has run recently, what is the random number generator inside the cache system doing. So that is a big source of non-determinism in the runtime of a CPU. So this is the memory system for a CPU.
它首先检查缓存，数据是否存储在缓存中，如果没有，它会从 DDR 中抓取。这是一个巨大的优化。缓存比 DDR 快大约两个数量级。如果你从不使用缓存，基本上所有程序都会慢 100 倍。因此，缓存的存在对于 CPU 以合理速度运行是绝对必要的。但是，无论你是否获得缓存命中取决于 CPU 的环境，比如其他正在运行的程序、最近运行过的程序，缓存系统中的随机数生成器正在做什么。所以这在 CPU 的运行时间中是一个非确定性的主要来源。所以这就是 CPU 的内存系统。
(1:06:12)
The big thing that you can do differently is instead of having the hardware say, I'm going to read memory and then the hardware decides whether or not it comes from cache or not, you can actually bake this decision into software. So a different design philosophy is And you see this in maybe, for example, TPUs. The TPU instead has, I mean, I'll draw the same diagram, but I'll call it a scratchpad. And so the main difference is, so this would be like a TPU and then like HBM in this case, rather than DDR, but it's still an off-chip memory. And instead of like the software saying first access like memory and then the hardware decides, you've got some instructions that go here.
你可以以不同的方式处理的一个重要事情是，不是让硬件说我要读取内存，然后硬件决定是否来自缓存，你实际上可以将这个决定内置于软件中。所以一种不同的设计理念是，你可以在 TPU 中看到这点。TPU 改为，我的意思是，我会画同样的图，但我会称其为临时存储器。因此主要区别在于，这将是 TPU，然后像 HBM 在这种情况下，而不是 DDR，但仍然是一个外部内存。而不是让软件首先访问像内存，然后硬件决定，你可以在这里获得一些指令。
(1:07:01)
This is like one kind of instruction and then a totally different kind of instruction that goes to HBM. And so this style is generically known as scratchpad instead of cache. The key distinction being that you have like one kind of instruction that says read or write scratchpad and a totally different instruction that says read or write HBM.
这是一种指令，然后是一种完全不同的指令去 HBM。因此，这种风格通常被称为临时存储而不是缓存。关键区别在于你有一种指令说读取或写入临时存储和一种完全不同的指令说读取或写入 HBM。
Dwarkesh Patel:
(1:07:21)
So scratchpad being the cache.
所以临时存储是缓存。
Reiner Pope:
(1:07:23)
Yeah, this thing here is the scratchpad.
是的，这个东西就是临时存储。
Dwarkesh Patel:
(1:07:26)
So stepping way back, people say computers have the quote-unquote John Moynihan Von Neumann architecture, where there's this I'm a serial processing automation. And maybe just because we've been talking about parallel accelerators, but I just don't like the FPGAs super parallel, the kinds of AI accelerators, TPUs are super parallel. Even CPUs are super parallel if you think about all the cores they have. And so is it actually, like in what sense is modern hardware actually the von Neumann architecture? Is that actually a fair way to describe modern hardware?
所以再往回退一步，人们说计算机有所谓的约翰·莫伊尼汉冯·诺依曼架构，那里有这个我是一个串行处理自动化。也许正因为我们一直在谈论并行加速器，但我只是觉得 FPGA 完全是并行的，各种人工智能加速器，TPU 是超级并行的。即使是 CPU 如果考虑到它们拥有的所有内核，也是超级并行的。那么在什么意义上现代硬件实际上是冯·诺依曼架构？这实际上是描述现代硬件的公平方式吗？
Reiner Pope:
(1:08:03)
I think it's a fair way to describe CPUs. Like just the amount of parallelism, like on a CPU, the amount of parallelism you get is about 100 cores times maybe like 16-way vector unit. So about a thousand-way parallelism on a CPU.
我认为这是描述 CPU 的公平方式。就 CPU 而言，你获得的并行性大约是 100 个核心乘以可能的 16 路向量单元。所以 CPU 上大约有千倍的并行性。
Dwarkesh Patel:
(1:08:16)
Yeah. One question is, there is a die that is being used for the CPU, and if there's fewer threads, And just as a matter of like transistor voltages are like switching on and off, is it just that there's like literally one control flow, like a small part of the die where like voltages are switching on and off? How do you actually occupy the die area of a CPU?
嗯。一个问题是，用于 CPU 的晶片上有一个电路，如果线程更少，还有因为晶体管电压就像开和关一样，是否只是有一个控制流，晶片上的一个小部分电压在开和关？你实际上是如何占用 CPU 的芯片面积的？
Reiner Pope:
(1:08:43)
If there's so few cores, like what am I spending a lot of time in there? The cores are just much bigger and more complicated. I guess we should compare a CPU core, which takes up 1 hundredth of the die, to a LUT. A LUT is just only these 16 gates. It's clear why there are so many more LUTs in an FPGA than cores in a CPU. But then sort of maybe the, like, why are there more CUDA cores, for example, than CPU cores, I think would be like, what's the difference between a CPU and a GPU or something like that would be a big difference. Inside the CPU, you have, so one big use of, sort of the top uses of area inside a CPU are the cache.
如果核心数量太少，我到底花那么多时间在里面干什么？这些核心确实更大更复杂。我想我们应该将占用 1 百分之一芯片面积的 CPU 核心与 LUT 进行比较。LUT 仅仅只有这 16 个门电路。很明显，FPGA 中的 LUT 数量远远超过 CPU 中的核心数量。但接下来或许是，像，为什么 CUDA 核心比 CPU 核心多，这可能是因为，CPU 和 GPU 之间的区别，或者类似的东西可能是一个很大的区别。在 CPU 内部，某种来说，CPU 内部占用面积的主要用途之一是缓存。
(1:09:34)
Very little is actually the ALUs, like mostly it's like these register files rather than the logic units. Both of these things have equivalents in a GPU and so that's not a big difference. But the thing that does not have an equivalent in a GPU is this branch predictor. There's a whole big area in the CPU which is just a whole bunch of predictors that are saying, when will my next branch be and where's the branch target for that. Stripping a lot of that out as well as making these register files tighter, in a sense, is driving a lot of where the GPU gains.
实际上，ALU 的占用面积非常小，主要是这些寄存器文件而不是逻辑单元。这两者在 GPU 中都有对应，所以这不是一个很大的区别。但 GPU 没有对应物的是这个分支预测器。CPU 中有一个很大的区域，里面有很多预测器在说，我的下一个分支是什么时候以及该分支的目标在哪里。将很多东西剥离掉，同时把这些寄存器文件做得更紧凑，从某种意义上来说，推动了 GPU 的很多性能提升。
Dwarkesh Patel:
(1:10:19)
What is the purpose of the branch predictor to execute both branches at once or what does it do?
分支预测器的目的是什么，是同时执行两个分支，还是它的作用是什么？
Reiner Pope:
(1:10:24)
The issue is that when I've got a series of instructions like instructions, instructions, instructions, instructions, if I have a branch like here, if this instruction is branch, The actual processing step of processing an instruction takes a really long amount of time. It takes like maybe five nanoseconds or something like that. So like the time to actually notice that I've got a branch and then like We're going to evaluate the Boolean, whether it's true, and then update the program counter to the new target and then read from the instruction memory for that. That could take like actually five nanoseconds to finish. And so in reality, this may finish somewhere down here.
问题在于，当我有一系列指令，比如指令、指令、指令、指令，如果我这里有一个分支，如果这个指令是分支，实际上处理一个指令的步骤需要很长时间。可能需要大约五纳秒或者类似的时间。所以，实际上注意到我有一个分支的时间，以及像我们要评估布尔值是否为真，接着更新程序计数器到新的目标，然后从指令存储器中读取这个指令。实际上可能需要五纳秒才能完成。所以实际上，这可能在这里的某个地方完成。
(1:11:12)
I want to run a clock speed that is much faster than what five nanoseconds allows. Like five nanoseconds is 200 megahertz clock speed. I would like to run at one or two gigahertz or something like that. And so I need to run other instructions while the branch is being evaluated. And so I really just want to keep running the following instructions that happen after me. But that might have been wrong. Like if the branch ended up being taken, then I need to know that instead of evaluating these instructions, I actually need to like jump to wherever the target is and run these instructions instead.
我希望运行的时钟速度远远快于五纳秒所允许的速度。五纳秒对应 200 兆赫兹的时钟速度。我希望能够运行在一或两吉赫兹或者类似的频率上。所以我需要在评估分支的同时运行其他指令。所以我真的只想继续执行在我之后发生的指令。但那可能是错的。如果分支最终被采取，那么我需要知道，而不是评估这些指令，我实际上需要跳转到目标，并运行这些指令。
(1:11:48)
And so the purpose of the branch predictor is like genuinely to predict based on like before you even get to the destruction to be like five cycles earlier to predict there was going to be a branch that's going to happen.
所以分支预测器的目的就是真正基于像在你到达之前，就像提前五个周期预测会发生分支。
Dwarkesh Patel:
(1:12:00)
So if I think about how the brain works versus what you're describing here, at a high level, the differences might be that While you can do structured sparsity in these accelerators and then save yourself some area that you would have otherwise had to dedicate to these gates, in the brain, there's unstructured sparsity. You know, any neuron can connect to any other neuron and not in like ways where they'd be column lined or whatever. Then there's the fact that memory and computer are co-located. I guess you could say in a way the memory and computer are co-located on...
所以如果我考虑大脑如何工作与您在这里描述的内容，总体而言，这两者之间的区别可能在于，虽然您可以在这些加速器中进行结构化稀疏，从而节省原本需要分配给这些门的面积，但在大脑中则存在无结构稀疏。你知道，任何神经元都可以连接到任何其他神经元，而不是像那样列成一列或其他方式。然后还有一个事实是，内存和计算机是共同放置的。我想你可以说在某种意义上内存和计算机是共同放置的…。
Reiner Pope:
(1:12:34)
This is exactly the co-location in some sense of the memory and computer.
从某种意义上说，这正是内存和计算机的共同放置。
Dwarkesh Patel:
(1:12:37)
That's right.
没错。
Reiner Pope:
(1:12:37)
That's right.
没错。
Dwarkesh Patel:
(1:12:37)
Yeah. Yes, maybe that actually isn't a big difference. And the other, maybe a big difference is that the clock cycle on the brain is much slower than on... On computers, and partly that's to preserve energy because the faster the clock cycle, the bigger the voltage needs to be in order to identify for the signal to settle and to like identify what state of transistor is that. I don't know if you have other high level takes about like how Any commentary on what the brain might be doing versus how these chips work?
是的。是的，也许这实际上并没有太大区别。另一个可能的重大区别是，大脑的时钟周期比计算机上的要慢得多，这部分是为了节省能量，因为时钟周期越快，电压就需要更大，以便信号稳定并识别出晶体管的状态。我不知道你是否有其他关于大脑可能在做什么与这些芯片如何工作的高级看法？
Reiner Pope:
(1:13:16)
Yeah, so let's take the clock speed one first, actually. The clock speed is quite high on a chip because that drives higher throughput. When we compare a GPU running some workload, it's running batch size 1,000 or something like that, whereas the brain is not running batch size 1,000. There's only one of me. You could imagine saying, well, take a GPU and instead of running at a gigahertz, run at a megahertz or something like that. That would start to look maybe a little bit more like equivalent things that you're talking about in the brain. There is, in the way that silicon works, that does not give you a 1000x advantage in energy efficiency.
是的，我们先讨论时钟速度的问题。芯片上的时钟速度相当高，因为这会推动更高的吞吐量。当我们比较一个运行某个工作负载的 GPU 时，运行的批次大小是 1,000 或者类似那样，而大脑并不是以 1,000 的批次大小在运行。只有我一个人。你可以想象说，将 GPU 的时钟频率从吉赫运行到兆赫或类似那样。这可能开始看起来更像你在大脑中谈论的等效事物。从硅的工作方式来看，并不会给你在能效上 1000 倍的优势。
(1:14:07)
So what it ends up looking like is you can You sort of just end up running this circuit once to stabilization and then it'll sit idle for a long period of time. It doesn't consume a lot of energy while it's sitting idle because most of the energy is consumed in toggling bits from zero to one and back. So actually let's talk about the energy consumption of a circuit like this. The way to think of a bit being stored is you've actually deposited some charge in a capacitor somewhere, sitting somewhere in the chip implicitly. So it becomes charged when it becomes a one and then it becomes discharged when it next goes to a zero.
所以最终看起来是，你可以说你只需运行这个电路一次以达到稳定，然后它会在很长一段时间内保持闲置。当它闲置时，不消耗很多能量，因为大部分能量是在切换比特位从零到一再回到零的时候消耗的。所以实际上我们来谈谈这样电路的能量消耗。思考比特存储的方式是，你实际上在芯片的某个地方隐含地在一个电容器中储存了一些电荷。当它变成 1 时，它会变得充电，而当它下次变成 0 时它会被放电。
(1:14:52)
And that cycle of like charging the capacitor and then dumping that charge out to ground, that is where the energy is consumed. This is called the dynamic or switching power. This is most of the energy consumption of a chip. There is some other energy consumption just coming from the fact that insulators aren't perfect insulators, but we'll just discard that. Most of the energy consumption actually comes from just the charging and discharging of like toggling from zero to one and back to zero. So if you run a chip much slower and you only clock it once every thousand clock cycles or something, you will have a thousand times fewer transitions.
而充电电容器然后将电荷释放到地面的这个循环，才是能量消耗的地方。这被称为动态或切换功率。这就是大部分芯片的能量消耗。还有一些其他能量消耗，仅仅是因为绝缘体并不完美，但我们就忽略它。实际上大部分能量消耗来自于充电和放电，如切换从零到一再回到零。所以如果你让芯片运行得更慢，只在每千次时钟周期中时钟一次，你将会有一千次更少的过渡。
(1:15:25)
It'll be about a thousand times less energy consumption, but not a substantial advantage in energy efficiency.
这将减少大约一千倍的能量消耗，但在能效上并没有显著的优势。
Dwarkesh Patel:
(1:15:33)
Okay, so you described how a TPU works at a high level. What is the difference at a high level between how a GPU and a TPU work?
好的，你描述了一下 TPU 如何在高层次上工作。在高层次上，GPU 和 TPU 工作之间的区别是什么？
Reiner Pope:
(1:15:43)
Yeah, so I mean, I think there's sort of a high-level organization principle that is different. And then there's sort of inside the cores that are different. But we'll look outside, at the high level. So we'll take a GPU and a TPU, and what does the top-level block structure look like? If you think of this as the whole chip in each case, The organization of the GPU is mostly a bunch of almost identical units, which are these. These are the SMs, and then they've got an L2 memory in the middle, and then a bunch more of these SMs on the bottom. And so there's sort of this fairly regular grid of cores. And then if we look at a TPU in comparison, you end up with much coarser grained units of logic.
是的，我觉得在高级组织原则上有一些不同。然后，在内核内部也有一些不同。不过我们先从外部看，从高层次出发。所以我们拿一个 GPU 和一个 TPU，这个顶层的块结构看起来是什么样子？如果你认为这就是整个芯片，那么 GPU 的组织大多是几乎相同的单位，就是这些。这些是 SM，然后它们中间有一块 L2 内存，底部有更多的这些 SM。所以这里有一个相当规则的核心网格。然后如果我们比较 TPU，你最终会得到更粗粒度的逻辑单元。
(1:16:44)
And so you end up with something like some large number of maybe just a few matrix units. These are the big systolic arrays. And then in the middle, you've got some vector units. And then you've got your matrix units at the bottom. So now sort of like matrix units with a vector unit in the middle, sort of this is the whole TPU chip. You can sort of think of scaling this thing down into a really tiny unit with a smaller matrix unit, smaller vector unit, and that is sort of what an SM is. So sort of at a very high level point of view, the GPU has a lot of tiny, tiny TPUs sort of tiled across the whole chip.
所以你最后得到一些可能只有几个的大型矩阵单元。这些是大型脉冲阵列。然后在中间，你有一些向量单元。以及底部的矩阵单元。所以现在的结构是矩阵单元中间夹着一个向量单元，这基本就是整个 TPU 芯片。你可以将这个东西缩小到一个真的很小的单元，配上较小的矩阵单元和较小的向量单元，基本上这就是 SM。从非常高的层面来看，GPU 在整个芯片上有很多小型的 TPU。
Dwarkesh Patel:
(1:17:35)
Oh, interesting. So like you're suggesting the tensor core within a streaming SM is analogous to an MXU.
哦，有趣。所以你在暗示流式 SM 中的张量核心类似于 MXU。
Reiner Pope:
(1:17:42)
Yeah, it's very, very similar.
是的，它非常非常相似。
Dwarkesh Patel:
(1:17:44)
I see. And so if you had more like More lack of structure, having a bunch of tiny TPUs makes a lot of sense. Whereas if you kind of just have like huge matrix multiplications, you're like, why don't we just, why don't we avoid the cost of having the individual SMs with their own registers and work schedulers and things like that? Why don't we just like make a huge thing? And like amortize those costs across the whole thing.
我明白了。如果你更缺乏结构，拥有一堆小型 TPU 是合理的。而如果你只是有大型的矩阵乘法，你就会想，为什么我们不避免拥有各自注册表和工作调度器的单独 SM？为什么我们不就做一个大的东西呢？把这些成本摊薄到整个东西上。
Reiner Pope:
(1:18:12)
And I mean, I think this shows up in how large you can grow things. We've sort of seen this theme, like especially with the systolic array, where largest systolic array amortizes the register file costs better. This sort of design allows you to have largest systolic arrays, whereas the sort of GPU design constrains you to having small units of everything. There is a trade-off, however. There ends up being, because of this coarse-grained separation of things there, you need to move a lot of data from the vector unit to the matrix units. You need to move a lot of data through two lines of perimeter here. Whereas if you sort of look at the equivalent thing here, you've got vector units everywhere and you need to move data through this line,
我觉得这表现出你能做到多大的东西。我们看到这个主题，特别是在脉冲阵列中，最大的脉冲阵列能更好地摊薄寄存器文件的成本。这种设计让你拥有更大的脉冲阵列，而 GPU 的设计则限制你拥有小单位的一切。不过这里有一个权衡。由于这种粗粒度的分离，你需要将大量数据从向量单元移动到矩阵单元。你需要通过两条周边线移动大量数据。而如果你查看这里的等效事物，你会发现在各处都有向量单元，你需要通过这条线来移动数据，
(1:19:01)
through this line, through this line, through this line, through this line, through this line. So the amount of data you can move between a vector unit and a matrix unit is actually much higher in a GPU than in a TPU because Because like it's like instead of having to like move all the data through these just two lines, you're moving all these data through like 16 lines or something of wiring instead in a GPU.
通过这条线，通过这条线，通过这条线，通过这条线，通过这条线。所以在 GPU 中，你可以在向量单元和矩阵单元之间移动的数据量实际上比在 TPU 中要高得多，因为你不需要通过仅仅两条线路移动所有数据，而是通过大约 16 条线路或其他线路来移动所有这些数据。
Dwarkesh Patel:
(1:19:27)
Right. But also you might have to move across less area.
对。但你可能还需要在更小的区域内移动。
Reiner Pope:
(1:19:31)
Which, I mean, is also a saving, like it's an energy saving. So data ends up moving, like, if you can operate entirely within an SM, the data movement is much smaller. But then the moment you want to operate across SMs, it becomes sort of more complicated and expensive.
这也是一种节省，像是节能。所以数据最终会移动，如果你可以完全在一个 SM 内操作，数据的移动就会小得多。但一旦你想在 SM 之间操作，这就变得有点复杂且昂贵。
Dwarkesh Patel:
(1:19:47)
So you don't have a comment, but one might expect that a thing that MatX might try to do The goal is to get the GPU-like smaller structure of systolic arrays surrounded by SRAM, but also at the same time make it so that the things you need in an SM to support the CUDA architecture, but take a bunch of space, you might discard.
所以你没有评论，但人们可能会期待 MatX 会尝试的目标是获取类似 GPU 的较小结构的脉动阵列，周围环绕着 SRAM，同时确保在 SM 中支持 CUDA 架构的那些占用大量空间的东西，你可能会舍弃。
Reiner Pope:
(1:20:13)
Yeah. We've talked publicly about something which we call a splittable systolic array, which is sort of, in some sense, you can think of as like big systolic arrays that can be small systolic arrays as well. Cool.
是的。我们公开谈论过一些我们称之为可拆分的脉动阵列的东西，某种意义上可以把它看作是既可以是大脉动阵列也可以是小脉动阵列。很酷。
Dwarkesh Patel:
(1:20:25)
Okay, I think that's a good note to close on. Reiner, thank you so much.
好的，我觉得这是一个好的结束语。谢谢你，Reiner。
Reiner Pope:
(1:20:29)
Thanks, Dwarkesh.
谢谢你，Dwarkesh。
