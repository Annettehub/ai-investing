# 变更日志（changelog）

> 记录系统架构、规则、工具链的重大变更，便于追溯和回滚。

## 格式

```markdown
- YYYY-MM-DD [类型] [文件/模块] [变更内容] [变更原因] [影响范围]
```

类型：新增 / 修改 / 删除 / 修复 / 优化

## 记录

- 2026-07-04 [新增] 01-commands/today.md 增加每日跟踪命令，补齐六环节工作流
- 2026-07-04 [新增] 02-kb/rules.md 初始化规则库，支撑规则晋升闭环
- 2026-07-04 [新增] 02-kb/index.md 初始化知识库总索引
- 2026-07-04 [新增] 02-kb/log.md 初始化操作日志
- 2026-07-04 [新增] 05-meta/ 目录 搭建元系统（config, skills, commands, maintenance, evolution）
- 2026-07-04 [修改] 00-system/connectors.md 增加腾讯云、IMA 工具映射
- 2026-07-04 [修改] AGENTS.md 统一为 ai-investing 协议
- 2026-07-04 [新增] 02-kb/hypotheses/H7 MLCC涨价假设（闭环1测试）
- 2026-07-04 [新增] 02-kb/sources/SRC-MLCC + concepts + entities（闭环2测试）
- 2026-07-04 [修改] 02-kb/rules.md R1晋升为生效规则（闭环3测试）
- 2026-07-04 [新增] 04-output/today/2026-07-04.md + weekly/2026-W27.md（闭环输出）
- 2026-07-04 [修改] health-mx.md 首次健康度评估（5绿3黄）
- 2026-07-04 [修改] friction-log.md 记录API中断+规则晋升流程不明确2条摩擦
