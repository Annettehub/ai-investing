# Podwise 播客知识库 - 来源索引

> 通过 Podwise.ai MCP/CLI 同步的播客内容，包含 AI 转录、摘要、大纲、问答和逐字稿。
> 同步脚本: `scripts/sync_podwise.py`
> 原始数据: `03-raw/podwise/`
> GitHub 仓库: [Annettehub/podwise-readings](https://github.com/Annettehub/podwise-readings) (手机阅读)
> 需要VPN访问 app.podwise.ai

## 订阅播客列表

### 英文播客
| 播客 | 类型 | 关注方向 |
|------|------|---------|
| The a16z Show (Andreessen Horowitz) | VC/科技 | AI, 创投, 技术趋势 |
| Prof G Markets (Scott Galloway) | 投资/商业 | 市场分析, 科技股, 宏观 |
| TechSurge: Deep Tech Podcast | 硬科技 | 半导体, AI基础设施, 深度技术 |
| 20VC (Harry Stebbings) | VC | 创投, AI, 能源, 芯片 |
| Sequoia Capital | VC/深度 | 半导体, AI, 企业级技术 |
| Moonshots with Peter Diamandis | 前沿科技 | 太空AI, 量子计算, 未来趋势 |
| Dwarkesh Patel / Dwarkesh Podcast | AI深度访谈 | AI研究, 训练范式, 技术哲学 |
| Latent Space: The AI Engineer Podcast | AI工程 | AI基础设施, 开源模型, 工程实践 |
| No Priors: AI, Machine Learning | AI研究 | AI模型, 机器学习前沿 |
| Lenny's Podcast: Product | 产品/AI | AI产品, Codex, 产品策略 |
| Capital Allocators | 机构投资 | 对冲基金, 资产配置, 机构视角 |
| Anthropic News | AI公司动态 | Anthropic产品发布, 行业新闻 |

### 中文播客
| 播客 | 类型 | 关注方向 |
|------|------|---------|
| 硅谷101 | 科技深度 | AI教育, 芯片产业, 中美科技 |
| 投资实战派 | 投资/深度 | 半导体系列, 价值投资 |

## 数据格式

每期节目导出为独立 Markdown 文件，包含:
1. **Front Matter** — 元数据(播客名/标题/链接/日期)
2. **Summary** — AI摘要 + 关键要点(Takeaways) — 中文
3. **Chapters** — 按大纲分组的章节摘要 — 中文
4. **Q&A** — AI提取的问答对 — 中文
5. **Highlights** — 金句摘录(带时间戳) — 中文
6. **Keywords** — 关键词+解释 — 中文
7. **Transcript** — 完整逐字稿(带时间戳+说话人) — 中文

## 同步状态

> 最后同步时间由 `.sync_state.json` 自动维护

## 使用说明

```bash
# 同步最近7天的已处理节目
python scripts/sync_podwise.py

# 同步最近30天
python scripts/sync_podwise.py --days 30

# 预览（不下载）
python scripts/sync_podwise.py --dry-run

# 强制重新下载已有文件
python scripts/sync_podwise.py --force

# 同步后自动推送到 GitHub (手机可读)
python scripts/sync_podwise.py --push

# 组合使用：同步30天 + 推送GitHub
python scripts/sync_podwise.py --days 30 --push
```

**注意**: 只有在 Podwise Inbox 中标记为 **Ready** (已AI处理) 的节目才能下载。
未处理的节目需先在 [app.podwise.ai](https://app.podwise.ai) 点击 Process。

## 手机阅读

打开 **https://github.com/Annettehub/podwise-readings** → 点击任意 `.md` 文件即可阅读。
推荐安装 GitHub App，支持离线缓存和全文搜索。
