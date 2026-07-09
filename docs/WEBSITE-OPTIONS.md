# 网站美化与部署方案

## 当前结论

旧 Quartz 工程已删除。你的目标是长期发布 AI 投研知识库和个人博客，阅读体验应该优先于关系图效果。

推荐路线：

1. 短期：保留干净知识库主目录，先把公开内容和内部工作系统分离。
2. 中期：用更适合阅读的静态站点框架重做前台。
3. 长期：GitHub 做唯一内容源，网站由 GitHub Actions 自动部署。

## 方案比较

| 方案 | 适合度 | 优点 | 代价 |
| --- | --- | --- | --- |
| Quartz 继续美化 | 中 | 改动小，保留双向链接、图谱、搜索 | 阅读体验仍受 Quartz 风格限制 |
| VitePress | 中高 | 清爽、稳定、Markdown 友好 | 更像技术文档，博客感一般 |
| Astro Starlight | 高 | 阅读体验好，结构清晰，适合知识库 | 需要迁移网站工程 |
| Docusaurus | 中 | 文档站成熟，版本化强 | 风格偏工程文档 |
| Next.js / Astro 自定义博客 | 高但成本高 | 最美观、最自由 | 需要维护前端代码 |

## 建议选择

如果目标是“知识库 + 阅读舒服 + 长期维护简单”，建议优先选择 **Astro Starlight**。

推荐公开目录：

```text
site/
  src/content/docs/
    index.md
    ai-infra/
    companies/
    concepts/
    investing/
    podcasts/
```

根目录继续保留主知识库：

```text
02-kb/
03-raw/
04-output/
value-investing/
```

然后用脚本把适合公开的内容复制到 `site/src/content/docs/`。

## 部署选择

| 部署方式 | 推荐度 | 说明 |
| --- | --- | --- |
| GitHub Pages | 高 | 免费、和 GitHub 仓库天然集成，适合静态知识库 |
| Cloudflare Pages | 高 | 免费额度好，全球访问快，支持自定义域名 |
| Vercel | 中高 | 体验好，适合 Next.js/Astro，但个人知识库不一定需要 |
| Netlify | 中 | 也适合静态站点，但现在不是首选必要项 |

建议先用 GitHub Pages 或 Cloudflare Pages。不要一开始上复杂服务。

## 网站信息架构建议

首页不要做营销页，直接做阅读入口：

```text
首页
  最近更新
  AI 投研地图
  核心主题

AI Infra
  算力
  数据中心
  电力
  GPU / ASIC

Companies
  NVIDIA
  TSMC
  CoreWeave
  OpenAI

Concepts
  Token
  KV Cache
  CapEx
  Inference

Investing
  假设
  框架
  周报

Podcasts
  播客精读
```

## 后续迁移步骤

1. 先清理公开内容范围。
2. 新建 `site/`，选择 Astro Starlight 或 VitePress。
3. 写同步脚本，把 `02-kb/`、`04-output/`、`value-investing/` 中可公开内容复制进 `site/`。
4. 本地预览阅读效果。
5. 配 GitHub Actions 自动部署。
6. 打开 GitHub Pages 或接入 Cloudflare Pages。
