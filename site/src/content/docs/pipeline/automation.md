---
title: 自动同步
description: GitHub Actions 和本地工具如何把资料放入 03-raw
---

当前仓库采用“自动拉取 + 人工整理”的方式管理资料。自动同步只负责把来源资料放入 `03-raw`，不会直接把内容发布成网页。

## 已配置

| 来源 | 写入目录 | 运行方式 | 需要的 GitHub Secret |
| --- | --- | --- | --- |
| Feishu | `03-raw/feishu` | 每 6 小时自动同步，也可手动触发 | `FEISHU_APP_ID`、`FEISHU_APP_SECRET`、`FEISHU_FOLDER_TOKEN` |
| WeRead | `03-raw/weread` | 每天自动同步，也可手动触发 | `WEREAD_API_KEY` |
| Podwise | `03-raw/podwise` | 先保留本地同步，因为依赖本机 CLI 登录状态 | 暂无 |
| Gmail | `03-raw/gmail` | 暂时保留，未来接通 | 待定 |

## GitHub Pages

网站部署使用 GitHub Actions。推送到 `main` 后，会构建 `site/` 并发布到 GitHub Pages。

如果 GitHub Pages 仍处于关闭状态，需要在 GitHub 仓库设置里选择：

`Settings -> Pages -> Build and deployment -> Source -> GitHub Actions`
