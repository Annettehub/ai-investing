# Annette Knowledge Hub - AI Investing

这是 Annette 的 AI 投研知识库。当前目标不是继续扩大系统，而是先跑通一个最小、可循环、可生长的知识闭环。

## 当前工作模式

当前只聚焦一个小循环：

```text
03-raw/ 原始资料
  -> 02-kb/sources/ 来源卡片
  -> 02-kb/concepts/ 长期概念
  -> 02-kb/hypotheses/H1.2.md 当前假设
  -> 04-output/weekly/ 周度复盘
```

当前焦点见 [CURRENT-FOCUS.md](CURRENT-FOCUS.md)。

## 当前范围

| 路径 | 状态 | 说明 |
| --- | --- | --- |
| `03-raw/` | 保留 | 信息入口不变，继续接收 feishu、podwise、wechat、weread、zsxq、ima 等原始资料 |
| `02-kb/` | 保留 | 知识库主体，当前只主动更新 H1.2 相关内容 |
| `04-output/weekly/` | 保留 | 当前小循环的输出位置 |
| `site/` | 保留 | 网站阅读层，不作为当前闭环的核心维护对象 |
| `scripts/` / `config/` | 保留 | 自动同步工具和配置继续保留 |
| `99-backup/` | 暂停 | 旧系统、旧命令、旧维护层、非当前输出先移到这里，等 H1.2 小循环跑通后再逐步恢复 |

## 当前三条命令

MVP 阶段只使用三个动作：

1. `collect`：从 `03-raw/` 找到和当前假设有关的新材料。
2. `distill`：把有价值的材料沉淀成 `02-kb/sources/` 来源卡片，并更新概念或假设。
3. `weekly`：每周复盘一次 H1.2 的证据、反证、certainty 和下周问题。

命令说明见 `01-commands/`。

## 入库原则

不是所有资料都进入知识库。只有满足任一条件，才从 `03-raw/` 晋升到 `02-kb/`：

- 改变 H1.2 的判断方向或 certainty。
- 补强或反驳 H1.2 的关键证据链。
- 更新 `存储产业链与周期` 概念框架。
- 需要进入周度复盘。

否则资料留在 `03-raw/`，不急着处理。
