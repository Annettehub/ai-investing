# Active Context

## 当前状态

系统已进入 MVP 收敛阶段。目标不是继续扩展信息源，而是先跑通一个可循环的小知识通道。

当前唯一主动主题：

`H1.2 [D1-Trend] 存储周期特性是否向成长特性转变`

2026-07-12，H1.2 第一轮小循环已跑通，进入 `active-tracking` 阶段。

## 本次调整

2026-07-11 已完成：

- 保留 `03-raw/` 所有信息入口不变。
- 保留 `02-kb/` 既有知识库内容。
- 保留 `site/`、`scripts/`、`config/`，避免破坏网站和同步能力。
- 将旧系统、旧命令、旧维护层和非当前输出移入：
  - `99-backup/paused-until-h1-2-loop-runs-2026-07-11/`
- 重建根目录入口：
  - `README.md`
  - `AGENTS.md`
  - `CURRENT-FOCUS.md`
- 将命令收敛为：
  - `01-commands/collect.md`
  - `01-commands/distill.md`
  - `01-commands/weekly.md`
- 重写 H1.2 为当前固定假设模板。
- 新增 3 张吴梓豪存储链来源卡片。
- 新增第一篇 H1.2 周度复盘。

## 当前小循环

```text
03-raw/zsxq/
  -> 02-kb/sources/
  -> 02-kb/concepts/L2-芯片层（Chips）/供需周期与供应链/存储产业链与周期（HBM、DRAM、NAND）.md
  -> 02-kb/hypotheses/H1.2.md
  -> 04-output/reports/H1.2-storage-restructured-2026-07-12.md
  -> 04-output/tracking/H1.2-storage-tracking.md
  -> 04-output/weekly/
```

## 下一步

1. 按 `04-output/tracking/H1.2-storage-tracking.md` 跟踪 HBM4/HBM4E 价格、认证和良率。
2. 跟踪 CoWoS booking 与 HBM 产能差，确认瓶颈是否仍在存储。
3. 跟踪服务器 DDR5 合约价和 LTA 覆盖率。
4. 跟踪企业 SSD / AI SSD 订单，验证 NAND 是否真正被 AI 拉出新曲线。
5. 如果 H1.2 小循环连续跑通 2-3 次，再从 `99-backup/` 恢复其他模块。

## 注意

- `03-raw/` 原始资料不改写。
- 暂停区不是删除区，不要清空。
- H1.1 当前仍有未推送修改，保持不动。
