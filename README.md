# AI Investing Knowledge Base

这是 Annette 的 AI 投研知识库仓库。它同时承担三件事：

1. 保存长期知识库内容和原始资料。
2. 通过 Git 同步到 GitHub。
3. 通过 Astro Starlight 发布为一个可阅读的网站。

## 当前目录分工

| 路径 | 作用 | 是否建议公开到网站 |
| --- | --- | --- |
| `02-kb/` | 沉淀后的知识库：概念、公司、假设、来源整理 | 是 |
| `03-raw/` | 原始资料：播客、飞书、微信读书、知识星球等 | 视情况，默认不全部公开 |
| `04-output/` | 日报、周报、研究输出 | 是 |
| `value-investing/` | 价值投资框架和资料 | 是 |
| `00-system/` | Agent/工作系统规则 | 否 |
| `01-commands/` | 本地工作流命令 | 否 |
| `05-meta/` | 维护、配置、演进记录 | 否 |
| `config/` | 本地配置和 watchlist | 否 |
| `scripts/` | 本地自动化脚本 | 否 |
## 当前状态

- Git remote: `git@github.com:Annettehub/ai-investing.git`
- 主分支: `main`
- 当前网站实现: `site/`，使用 Astro Starlight + Rose Pine 主题。
- GitHub Pages: 使用 `.github/workflows/deploy-site.yml` 发布。仓库设置里需要选择 GitHub Actions 作为 Pages 来源。

## 维护原则

1. 根目录知识库是主本，未来网站目录只作为发布副本。
2. 本地密钥、token、`.env`、缓存、账号数据库不进入 Git。
3. 公开网站只发布整理后的知识内容，不发布 Agent 协议、环境配置和内部命令。
4. 每次新增资料后，先入 `03-raw/`，再沉淀到 `02-kb/` 或 `04-output/`。
5. 推送前先看 `git status`，确认没有把本地配置或隐私文件带上去。

## 常用文档

- [本地工具与 GitHub 推送流程](docs/LOCAL-WORKFLOW.md)
- [网站美化与部署方案](docs/WEBSITE-OPTIONS.md)
- [内容管线](docs/CONTENT-PIPELINE.md)
