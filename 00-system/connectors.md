# 多源信息管道配置

> 当前环境：三端打通，GitHub 做中枢。详见 `ENV-GUIDE.md`。

## 总览

```
Gmail(未来) ─┐
飞书(文档) ──┤   ┌──────────┐   ┌──────────┐
微信读书 ────┼──→│ 03-raw/  │──→│ 02-kb/   │──→ /research
Podwise ─────┤   │(原料层)   │   │(知识库)   │    /today
微信/IMA ────┤   └──────────┘   └──────────┘
知识星球 ────┘
GitHub / WebSearch：作为研究和自动化工具，不再写入单独的 03-raw 子目录
腾讯云：备份
```

---

## 1. GitHub — ✅ 已连接

**用途：** 追踪技术趋势、开源项目、行业工具，三端共享中枢。

**已可用操作：**
- 搜索 GitHub 仓库和代码
- 获取 Star/Watch 的项目更新
- 通过 GitHub Actions 运行定时同步
- 三端通过 WorkBuddy connector 读写文件

---

## 2. 飞书云盘 — ⚡ 你已有应用，现在就配置

### 2.1 飞书开放平台配置（你现在要做）

**你的飞书开放平台应用需要：**

**① 获取 App ID 和 App Secret**
1. 登录 [飞书开放平台](https://open.feishu.cn/app)
2. 点击你的应用 → 左侧「凭证与基础信息」
3. 复制 **App ID** 和 **App Secret**

**② 开通云文档权限**
1. 同一页面，左侧「权限管理」
2. 搜索并添加以下权限：
   - `drive:drive` — 访问云空间
   - `drive:drive:readonly` — 读取云空间文件
3. 点「批量开通」→ 需要管理员审批（如果是企业应用）
4. ⚠️ **如果是个人版应用**，可能无需审批，确认权限已添加即可

**③ 获取要同步的文件夹 Token**
1. 在飞书客户端，打开你要同步的文件夹
2. 看浏览器/客户端 URL，格式类似：
   ```
   https://xxx.feishu.cn/drive/folder/xxxxxxxxxxx
   ```
3. URL 末尾 `folder/` 之后的那串字符就是 **FOLDER_TOKEN**

**如果看不到 folder token，备用方案：**
1. 在飞书开放平台 → API 调试台
2. 调用「获取文件夹列表」API：
   ```
   GET https://open.feishu.cn/open-apis/drive/v1/files
   ```
3. 先用 tenant_access_token 调通，返回的 JSON 里找你要的文件夹 token

**④ 发布应用**
1. 权限添加后 → 点右上角「创建版本」
2. 填写版本号（如 1.0.0）→ 发布
3. 可能需要管理员审核

### 2.2 配置 GitHub Secrets

打开 https://github.com/Annettehub/ai-investing/settings/secrets/actions

添加三个 Repository secrets：

| Name | Value |
|------|-------|
| `FEISHU_APP_ID` | 你的 App ID |
| `FEISHU_APP_SECRET` | 你的 App Secret |
| `FEISHU_FOLDER_TOKEN` | 要同步的文件夹 Token |

### 2.3 测试飞书同步

方式一：手动触发 GitHub Actions
1. 打开 https://github.com/Annettehub/ai-investing/actions
2. 点左侧「Sync Feishu Drive Files」
3. 点右边「Run workflow」→ 绿色「Run workflow」按钮
4. 等 1-2 分钟看结果

方式二：对 WorkBuddy 说
```
"去 GitHub Actions 手动触发飞书同步 workflow"
```

### 2.4 飞书上的日常操作

建立同步后，你只需要：
1. 在飞书客户端 → 打开同步文件夹
2. 新建或编辑 .md 文件（飞书支持在线编辑 Markdown）
3. GitHub Actions 每 6 小时自动同步
4. 同步后的文件出现在 `03-raw/feishu/`

**推荐工作流：**
- 飞书上收到研报/行业分析 → 粘贴到同步文件夹的 .md 文件
- 手机飞书看到好内容 → 直接收藏到该文件夹
- 回家后对 WorkBuddy 说："处理 03-raw/feishu/ 中新文件"

### 2.5 故障排查

| 问题 | 检查 |
|------|------|
| 同步不触发 | GitHub Actions 是否 enabled？ |
| 获取 token 失败 | App ID/Secret 是否正确？飞书应用是否已发布？ |
| 列出文件为空 | 文件夹 Token 是否正确？文件夹是否有 .md 文件？ |
| 权限不足 | 飞书应用是否已开通 drive:drive 权限？ |

---

## 3. Gmail — 🔜 待配置

**用途：** 自动采集行业研究邮件、券商研报推送、产业新闻。

**方案 A（推荐零配置）：Gmail 过滤器 + 手动触发**

1. Gmail 中创建标签 `Industry-Intel`
2. 设置过滤器：发件人含特定关键字 → 打标签 `Industry-Intel`
3. 在任何环境对 WorkBuddy 说：
   ```
   "检查 Gmail 中 Industry-Intel 标签的新邮件，提取关键信息入库"
   ```

**推荐订阅的信息源：**
- 券商研报推送（中金/华泰/中信）
- SEMI 半导体行业协会 newsletter
- Seeking Alpha / ValueWalk
- 雪球/东方财富推送

---

## 4. 微信读书 — ⚡ 现在就配置

**用途：** 自动同步全部划线、想法、笔记到知识库。

### 4.1 获取 API Key（2 分钟）

1. 打开 [微信读书开放平台](https://cp.weread.qq.com/)
2. 微信扫码登录
3. 创建应用 → 获取 **API Key**（格式 `wrk-xxxxxxxx`）
4. 打开 https://github.com/Annettehub/ai-investing/settings/secrets/actions
5. 点 **New repository secret**：
   - Name: `WEREAD_API_KEY`
   - Value: 粘贴你的 API Key

### 4.2 测试同步

1. 打开 https://github.com/Annettehub/ai-investing/actions
2. 左侧选 **Sync WeRead Notes**
3. 点 **Run workflow** → **Run workflow**
4. 等 1-2 分钟，看日志输出

成功标志：
```
📚 微信读书笔记同步
📋 获取笔记本列表...
   找到 X 本有笔记的书，共 Y 条笔记
✅ 同步完成：X 本书 → 03-raw/weread/
```

### 4.3 同步后的文件

同步到 `03-raw/weread/`，每本书一个 .md 文件，格式：
```
微信读书-《芯片战争》-Chris Miller.md
```
包含：全部划线（按章节分组）+ 个人想法 + 阅读进度 + 日期

### 4.4 日常使用

**自动化：** GitHub Actions 每天早上 8 点自动同步
**手动：** 在任何环境对 WorkBuddy 说：
```
"同步微信读书笔记"
"从微信读书导出《芯片战争》的笔记并入库"
```

### 4.5 碎片粘贴（低门槛备选）

如果暂时不想配 API：
1. 微信读书里划线 → 复制
2. 粘贴给 WorkBuddy 说"整理入库"
3. 适合单条笔记场景

---

## 5. 腾讯云 — ⚡ 配置中

**用途：** 数据存储、备份、计算、COS 对象存储、Cloud Studio 静态站点部署。

### 5.1 腾讯云 COS 备份

1. 开通 [腾讯云 COS](https://console.cloud.tencent.com/cos)
2. 创建存储桶（如 `ai-investing-backup`）
3. 获取 `SecretId` 和 `SecretKey`
4. 配置 GitHub Secrets 或 WorkBuddy 环境变量：
   - `TENCENT_SECRET_ID`
   - `TENCENT_SECRET_KEY`
   - `TENCENT_COS_BUCKET`
   - `TENCENT_COS_REGION`
5. 使用 GitHub Actions 或 WorkBuddy 自动化定期备份 `02-kb/` 和 `04-output/` 到 COS

### 5.2 Cloud Studio 部署

- 可将静态研报/看板部署到 Cloud Studio 沙箱，获得可分享链接
- 适合输出给人看的产物（如 HTML 图表、周报站点）

**推荐工作流：**
- 每周生成周报后，打包 `04-output/weekly/` 为静态站点
- 通过 WorkBuddy 一键部署到 Cloud Studio
- 在手机/飞书分享链接

---

## 6. IMA 知识库 — ✅ 已连接

**用途：** 腾讯 IMA 知识库作为正式数据管道，从「Workbuddy同步库」推送资料，经 ima-sync-ingest 入库到 `02-kb/sources/`。

### 6.1 管道配置状态

| 项 | 配置 |
|----|------|
| 知识库名称 | Workbuddy同步库 |
| 知识库 ID | 7479412815576231 |
| 接入方式 | WorkBuddy `ima-mcp` connector |
| 入库工具 | `/ima-sync-ingest` |
| 同步方向 | IMA 知识库 → 03-raw/wechat/ → 分类摘要 → 02-kb/sources/ |
| 当前状态 | ✅ 已连接，已执行过同步 |

### 6.2 同步流程

1. 在 IMA 客户端将资料加入「Workbuddy同步库」知识库
2. 对 WorkBuddy 说 `/ima-sync-ingest 跑 IMA 同步`
3. 脚本拉取新增资料 → `03-raw/wechat/` → 生成结构化摘要
4. 确认分发 → 写入 `02-kb/sources/`，并在 `index.md` 数据管道登记

### 6.3 推荐用法

- **统一入口**：后续新增资料统一推送到 IMA，不再分散写入各子目录
- **检索增强**：执行 /research 前，先在 IMA 检索历史观点
- **碎片整理**：把 IMA 中的问答结论回写为 `02-kb/sources/`

---

## 7. WebSearch — ✅ 内置可用

**用途：** 实时信息补充、新闻扫描、数据验证。

在任何环境对 WorkBuddy 说：
```
"搜索最近一周关于 00981 的新闻"
"搜索 SMIC 7nm 最新进展"
"搜索 光刻胶 断供 最新消息"
```

---

## 8. Substack — ⚡ 待接入

**用途：** 订阅 AI / 投资类 Newsletter（如 a16z、Stratechery、The Generalist 等），自动入库为研究素材。

**当前状态：** 待接入。规划通过 RSS / Substack API 或手动转发，经 WorkBuddy 入库到 `03-raw/` 或直接写入 `02-kb/sources/`。

---

## 9. Gantise — ⚡ 待接入

**用途：** A 股数据终端，获取行情、财务、资金流向等结构化数据，支撑量化筛选与基本面验证。

**当前状态：** 待接入。规划作为行情 / 财务数据源接入，补充 A 股实时与历史数据。

---

## 管道状态一览

| 管道 | 状态 | 当前操作 | 三端可用 |
|------|------|---------|---------|
| GitHub | ✅ 已连接 | 零配置即用 | 🏢 🏠 📱 |
| 飞书 | ✅ 已连接 | 通过 WorkBuddy connector 读写 | 🏢 🏠 📱 |
| Gmail | 🔜 | 建标签 + 说一句话 | 🏢 🏠 📱 |
| 微信读书 | ⚡ 配置中 | 获取 API Key → 填 WEREAD_API_KEY Secret | 🏢 🏠 📱 |
| 腾讯云 | ⚡ 配置中 | 开通 COS → 配置备份 workflow | 🏢 🏠 |
| IMA | ✅ 已连接 | 知识库推送 → ima-sync-ingest 入库 | 🏢 🏠 📱 |
| WebSearch | ✅ | 内置即用 | 🏢 🏠 📱 |
| Podwise | ✅ | 播客摘要入库 | 🏢 🏠 |
| ZsxqCrawler | ✅ | 知识星球采集 | 🏢 🏠 |
| Substack | ⚡ 待接入 | 订阅 AI/投资 Newsletter → 入库 | 🏢 🏠 |
| Gantise | ⚡ 待接入 | A 股数据终端接入（行情/财务） | 🏢 🏠 |

---

## 推进顺序（更新）

| 顺序 | 管道 | 你现在要做的 | 时间 |
|------|------|------------|------|
| 1 | GitHub | ✅ 已完成 | — |
| 2 | 飞书 | ✅ 已通过 WorkBuddy connector 连接 | — |
| 3 | 手动入料 | 粘贴文章说"入库这篇" | **今天** |
| 4 | WebSearch | 说"搜索 XX" | 随时 |
| 5 | Gmail | 建 Industry-Intel 标签 | 本周 |
| 6 | 微信读书 | 看书时复制笔记粘贴入库 | 按需 |
| 7 | 腾讯云 | 开通 COS → 配置备份 workflow | 本周 |
| 8 | IMA | ✅ 已连接，资料推送到 Workbuddy同步库 | — |
