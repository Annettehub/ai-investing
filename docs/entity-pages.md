# 三家实体页的定制阅读层

## 发布范围

2026-08-26 经用户授权，仅将以下既有网址接入定制模板：

| 实体 | 正式路由 | 仓库原文 |
| --- | --- | --- |
| 老铺黄金 | /ai-investing/kb/entities/06181-301dfca8/ | 02-kb/entities/06181-老铺黄金.md |
| 泡泡玛特 | /ai-investing/kb/entities/09992-4857c5af/ | 02-kb/entities/09992-泡泡玛特.md |
| 腾讯控股 | /ai-investing/kb/entities/0700-da695dbe/ | 02-kb/entities/0700-腾讯控股.md |

`site/src/pages/kb/entities/` 中三个显式页面是发布白名单，不扫描其他实体自动推广。
老铺旧预览路由保留并标记 noindex，正式页保留可索引正文。
仓库设置、GitHub Actions 发布流程、原始资料和实体 Markdown 均不修改。

## 实现

- `site/src/lib/entity-document.mjs` 使用 Markdown AST 按章节语义提取模块，未知内容按原文渲染。
- `site/src/layouts/EntityPage.astro` 为独立阅读布局，显式导入实体页 CSS，不依赖主题覆盖。
- `site/src/components/entity/` 承载完整论述、左右多空对照、护城河、假设、仪表盘、图表与表格。
- 表格首列固定 280px，其余列等宽且每列至少 160px。窄屏只在表格内部滚动。
- 数值、统计期间、估算和待验证说明来自原文，不在组件维护第二份公司数据。
- 腾讯的 Unicode 上标和其他文章的方括号引用均保留原文字形，并链接到对应来源。
- 发布页沿用原网址，现有索引和站内链接无需重写；Pagefind 只索引正文区域。
- 已存在的 `postbuild-entity-css.mjs` 对独立实体布局跳过旧样式注入，其他行为不变。

Astro 显式静态路由优先于通配路由，见 [官方路由文档](https://docs.astro.build/en/guides/routing/#route-priority-order)。

## 检查

在 `site/` 下执行 `npm ci`、`npm run test:entity`、`npm run build`。
`scripts/check-entity-preview.mjs` 使用独立的原文 AST 逐段、逐单元格核对渲染结果，并测试七种视口、固定首列与等宽内容列、引用、目录、搜索及仪表盘筛选。

```text
node scripts/check-entity-preview.mjs <Playwright模块绝对路径> <检查输出目录> <页面URL> <可选原始附件路径或空字符串> <原文相对脚本路径>
```

如使用已安装的 Edge，设置环境变量 `ENTITY_BROWSER_CHANNEL=msedge`。
测试产物保存在指定输出目录，不提交截图和本机日志。

继续新增公司前需单独确认发布范围。模板提示词见 `docs/entity-page-prompt.md`。
