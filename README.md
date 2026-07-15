# Annette Knowledge Hub - AI Investing

这是 Annette 的 AI 投研知识库。当前目标不是继续扩大系统，而是先跑通一个最小、可循环、可生长的知识闭环。

## 当前工作模式

当前只聚焦一个小循环：

```text
03-raw/ 原始资料
  -> 02-kb/sources/ 来源卡片
  -> 02-kb/concepts/ 长期概念
  -> 02-kb/hypotheses/G-需求与周期/G2-storage-growth-and-cycle.md 当前假设
  -> 04-output/weekly/ 周度复盘
```

当前焦点见 [CURRENT-FOCUS.md](CURRENT-FOCUS.md)。

## 当前范围

| 路径 | 状态 | 说明 |
| --- | --- | --- |
| `03-raw/` | 保留 | 信息入口不变，继续接收 feishu、podwise、wechat、weread、zsxq、ima 等原始资料 |
| `02-kb/` | 保留 | 知识库主体，假设层采用 GSR，当前主动更新 G2 存储主题 |
| `04-output/weekly/` | 保留 | 当前小循环的输出位置 |
| `site/` | 保留 | 网站阅读层，不作为当前闭环的核心维护对象 |
| `scripts/` / `config/` | 保留 | 自动同步工具和配置继续保留 |
| `99-backup/` | 暂停 | 旧系统和旧结构备份；D1-D7 假设体系已完整归档，按需追溯 |

## 当前三条命令

MVP 阶段只使用三个动作：

1. `collect`：从 `03-raw/` 找到和当前假设有关的新材料。
2. `distill`：把有价值的材料沉淀成 `02-kb/sources/` 来源卡片，并更新概念或假设。
3. `weekly`：每周复盘一次 G2 的证据、反证、certainty 和下周问题。

命令说明见 `01-commands/`。

## 入库原则

不是所有资料都进入知识库。只有满足任一条件，才从 `03-raw/` 晋升到 `02-kb/`：

- 改变 G2 的判断方向或 certainty。
- 补强或反驳 G2 的关键证据链。
- 更新 `存储产业链与周期` 概念框架。
- 需要进入周度复盘。

否则资料留在 `03-raw/`，不急着处理。

## G2 存储研究驾驶舱

驾驶舱把长期跟踪表拆成两层：底层保留具体指标和阈值，页面只显示结论、四条验证线、触发条件、数据新鲜度和最新证据。

本地刷新并打开页面：

```powershell
python scripts\update_h12_dashboard_data.py
cd site
npm.cmd run dev
```

访问 `http://127.0.0.1:4321/ai-investing/dashboard/h1-2-storage/`。

TrendForce 数据取得后，先按 `config/trendforce/H1.2-template.csv` 整理列名，再导入：

```powershell
python scripts\import_trendforce_h12.py "D:\path\TrendForce.xlsx"
python scripts\update_h12_dashboard_data.py --offline
```

SEC、TWSE 和 OpenDART 采集结果只作为外部验证信号，不会自动修改 G2 的 `certainty`。OpenDART 需要在 `config/.env` 中配置 `OPENDART_API_KEY`。
