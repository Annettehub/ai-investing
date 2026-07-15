# Agent Entry Protocol

本文件是 AI Agent 进入仓库后的唯一入口。先读本文件，再读 [CURRENT-FOCUS.md](CURRENT-FOCUS.md)。

## 当前原则

当前系统处于 MVP 收敛阶段。不要扩大信息源，不要新增复杂命令，不要重构网站。先跑通 H1.2 小循环。

## 必读顺序

1. `CURRENT-FOCUS.md`：当前唯一焦点。
2. `README.md`：当前目录分工。
3. `02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md`：当前假设。
4. `01-commands/`：只允许使用 collect、distill、weekly 三个动作。

## 当前闭环

```text
collect: 03-raw -> 候选材料
distill: 候选材料 -> sources / concepts / H1.2
weekly: H1.2 -> 周度复盘 -> 下周问题
```

## 工作约束

- `03-raw/` 是原始资料层，默认只读，不改写原文。
- 当前主动处理范围只限 H1.2：存储周期、HBM、DDR5、NAND、SK Hynix、Micron、Samsung、TSMC。
- 其他主题可以保留，但不要主动扩展。
- 每条关键判断必须标注来源：本地 raw、来源卡片、网页、数据或推测。
- 不确定的事实标记为“待验证”。
- 每次更新 H1.2 后，必须同时更新一条周度或操作记录。

## 暂停区

旧系统文件已移到：

`99-backup/paused-until-h1-2-loop-runs-2026-07-11/`

不要删除暂停区。等 H1.2 小循环连续跑通 2-3 次后，再从暂停区逐项恢复有用模块。
