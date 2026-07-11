# 内容管线

这个仓库按“原始资料 -> 知识沉淀 -> 网页发布”三层维护。

## 1. 原始资料进入 `03-raw`

| 来源 | 目录 | 当前方式 |
| --- | --- | --- |
| Feishu | `03-raw/feishu` | GitHub Actions 定时同步 |
| WeRead | `03-raw/weread` | GitHub Actions 定时同步 |
| Podwise | `03-raw/podwise` | 本地 `tools/podwise.exe` + `scripts/sync_podwise.py` |
| WeChat / IMA / 网页摘录 | `03-raw/wechat` | 手动放入或 IMA 同步 |
| ZSXQ | `03-raw/zsxq` | 手动或脚本导入 |
| Gmail | `03-raw/gmail` | 暂时保留，未来接通 |

不再保留 `03-raw/github`、`03-raw/inbox`、`03-raw/manual`、`03-raw/web` 四个入口目录。GitHub 和 WebSearch 仍可作为研究工具使用，但不会直接写入原始资料库；手动资料、网页摘录和 IMA 同步内容先统一进入 `03-raw/wechat`。

## 2. 知识沉淀到 `02-kb` 和 `04-output`

- `02-kb` 放长期概念、公司、假设和来源索引。
- `04-output` 放日报、周报、专题研究和阶段性输出。
- 进入网页前，先把长文件名改写成短标题、清晰摘要和可阅读结构。

## 3. 网页发布到 `site`

`site/` 是发布层，不是资料主本。它只放适合公开阅读的整理版内容。

本地构建：

```powershell
cd D:\WorkBuddy\Claw\ai-investing\site
npm.cmd install
npm.cmd run build
```

推送到 GitHub 后，`Deploy Starlight Site` 会构建并发布 GitHub Pages。

## GitHub Secrets

Feishu 同步需要：

- `FEISHU_APP_ID`
- `FEISHU_APP_SECRET`
- `FEISHU_FOLDER_TOKEN`

WeRead 同步需要：

- `WEREAD_API_KEY`

如果希望同步 workflow 的提交继续触发其他 workflow，可以额外配置 `PAT`。没有 `PAT` 时会使用 GitHub 默认 token，同步仍可提交到仓库。
