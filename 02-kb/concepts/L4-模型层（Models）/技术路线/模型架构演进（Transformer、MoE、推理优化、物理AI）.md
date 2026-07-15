# 模型架构演进（Transformer、MoE、推理优化、物理AI）

> （待补充，内容后续增加）

## 2026-07-15 IMA 补充：记忆、持续学习与推理效率

| 子议题 | 观察点 | 来源 |
|---|---|---|
| 记忆 vs RAG | RAG 适合外部化事实检索，但对团队隐性知识、长期工作流和抽象关联的表达不足；持续学习尝试把部分上下文内化为模型能力 | `02-kb/sources/2026-07-15-ima-sequoia-engram-memory.md` |
| Adapter fine-tuning | LoRA、prefix、adapter 和稀疏架构可作为企业持续学习的轻量路径，但需要解决训练信号、权限和记忆边界 | 同上 |
| Router / thinking budget | 模型 router 根据任务复杂度分配小模型、常规模型或 thinking 模型，核心是降低平均推理成本并保留高价值任务质量 | `02-kb/sources/2026-07-15-ima-a16z-nvidia-infra-future.md` |
| 软硬件协同 | 模型架构、kernel、硬件和数据中心软件协同优化，可能比单层优化产生更高效率跃迁 | `02-kb/sources/2026-07-15-ima-sequoia-dylanpatel-codesign.md` |

**待验证问题**：持续学习是否能在真实企业场景中降低 token 成本、提高任务成功率，并且不牺牲隐私、权限和可审计性。
