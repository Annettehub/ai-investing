# 飞书 → GitHub 同步与入库评审配置

## 前置要求

- Windows 10/11（自带 PowerShell 5.1+）
- Git 已安装并能 push 到 GitHub
- 飞书开发者平台已创建自建应用

## GitHub Actions 设置（推荐）

### 1. 配置 GitHub Secrets

在 GitHub 仓库 `Settings -> Secrets and variables -> Actions -> New repository secret` 中新增：

| Secret | 用途 |
|---|---|
| `FEISHU_APP_ID` | 飞书自建应用 App ID |
| `FEISHU_APP_SECRET` | 飞书自建应用 App Secret |
| `FEISHU_FOLDER_TOKEN` | 飞书资料库文件夹 token：`LsWZfobhDlImj0dEm47cJGFmn0Z` |
| `PAT` | 可选。默认 `GITHUB_TOKEN` 已可提交；如果 main 分支保护导致推送失败，再配置有 repo 写权限的 GitHub token |

不要把 App Secret、GitHub token 或 `.env` 提交进仓库。

### 2. 给飞书应用授权

打开飞书同步文件夹 → 设置 → 协作者 → 添加同步用的飞书自建应用。

飞书开放平台中至少需要：

- Drive 文件列表/下载相关权限。
- `docx:document` 和 `docx:document:readonly`，用于读取在线文档正文。

添加权限后需要发布或重新发布应用版本。

### 3. 运行方式

`.github/workflows/sync-feishu.yml` 已配置：

- 每天 UTC 08:00 自动运行。
- 支持在 GitHub Actions 页面手动 `Run workflow`。

运行链路：

```text
Feishu folder
  -> scripts/sync_feishu_drive.py
  -> 03-raw/feishu/
  -> scripts/review_feishu_ingest.py
  -> 05-meta/ingest-reviews/
  -> 02-kb/sources/（仅 G2 存储相关候选来源卡）
  -> 02-kb/log.md
  -> git commit + push
```

评审脚本只做“机器预筛”。它不会自动修改 G2 假设、概念页、实体页或 certainty。

本地路径链路：

```text
D:\WorkBuddy\Claw
  -> scripts/sync_workbuddy_local.py
  -> 03-raw/feishu/local-workbuddy/
  -> scripts/review_feishu_ingest.py
  -> 05-meta/ingest-reviews/
  -> 02-kb/sources/（仅 G2 存储相关候选来源卡）
  -> 02-kb/log.md
```

## 本地首次设置（可选）

你当前的本地资料根目录是：

```text
D:\WorkBuddy\Claw
```

如果飞书 API 权限还没配好，可以先走本地导入：

```powershell
cd ai-investing

# 从本地 WorkBuddy 资料目录导入近 30 天 Markdown/TXT/HTML 到 03-raw/feishu/local-workbuddy/
python scripts\sync_workbuddy_local.py --source "D:\WorkBuddy\Claw"

# 对本次导入资料执行同一套入库评审
python scripts\review_feishu_ingest.py --from-manifest .workbuddy-local-sync-manifest.json --write-source-cards --write-log

# 检查变更后再提交
git status
```

本地导入默认只抓近 30 天资料，并跳过 `.git`、`.workbuddy`、`.cache`、`node_modules`、`site/dist`、`_archive`、`99-backup` 等系统/备份目录，也会跳过 `README.md`、`requirements.txt`、`index.html` 和行情日志，避免把工作区缓存或网站产物当作研究资料。需要全量扫描时加 `--since-days 0`，需要导入工具说明文件时加 `--include-boilerplate`。PDF、DOCX、PPTX、XLSX 默认跳过；如需生成“待人工转换”占位卡，可加 `--include-unsupported`。

### 1. 配置飞书凭证

```powershell
# 复制配置模板
cd ai-investing\config\feishu
copy .env.example .env

# 用记事本编辑 .env，填入你的飞书凭证
notepad .env
```

需要填入：
- `FEISHU_APP_ID`：飞书应用的 App ID
- `FEISHU_APP_SECRET`：飞书应用的 App Secret
- `FEISHU_FOLDER_TOKEN`：已预填你的同步库文件夹 token

### 2. 给飞书应用授权

打开你的飞书同步文件夹 → 设置 → 协作者 → 添加 `Annette-KB-Sync` 应用

### 3. 测试运行

```powershell
# 仅拉取飞书资料到 03-raw/feishu/
cd ai-investing
$env:FEISHU_APP_ID="cli_xxxxxxxxxxxxxxxx"
$env:FEISHU_APP_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:FEISHU_FOLDER_TOKEN="LsWZfobhDlImj0dEm47cJGFmn0Z"
$env:FEISHU_SYNC_MANIFEST=".feishu-sync-manifest.json"
python scripts\sync_feishu_drive.py

# 对本次新增/更新 raw 做入库评审
python scripts\review_feishu_ingest.py --from-manifest .feishu-sync-manifest.json --write-source-cards --write-log

# 提交前检查变更
git status
```

如继续使用旧 PowerShell 包装脚本：

```powershell
cd ai-investing\scripts
.\sync_feishu.ps1 -DryRun
.\sync_feishu.ps1
```

旧脚本主要用于本地同步和 push；GitHub Actions 以 Python 脚本为准。

## 同步行为

| 模式 | 行为 |
|------|------|
| 飞书拉取 | 递归扫描 `FEISHU_FOLDER_TOKEN` 下的子文件夹 |
| 本地导入 | 从 `D:\WorkBuddy\Claw` 导入 Markdown/TXT/HTML |
| 增量 | 通过内容 hash 判断新增/更新，只保存变更文件 |
| 跳过 | 文件名包含 `勿同步` 的文档不会同步 |
| 入库评审 | 只评审本次同步新增/更新的 raw 文件 |

## 支持的文件类型

| 飞书文件类型 | 处理方式 | GitHub 文件 |
|-------------|---------|------------|
| 云文档（docx） | 读取 `docx/raw_content` 并保存为 Markdown 文本 | 保留原文件名 + `.md` |
| Markdown（.md） | 直接下载 | 保留原文件名 |

## 当前同步边界

- 会递归扫描 `FEISHU_FOLDER_TOKEN` 对应文件夹下的子文件夹。
- 文件名包含 `勿同步` 的文档会跳过。
- 如果某篇 docx 无法读取 `raw_content`，本次 Action 会失败，避免“显示成功但实际漏同步”。
- 该流程不是飞书官方 Markdown 导出；它使用在线文档正文接口，适合保存文字资料。复杂表格、图片和附件仍可能需要人工补充。
- 自动入库评审目前只按 `CURRENT-FOCUS.md` 中的 G2 存储小循环判断：HBM、DDR5、DRAM、NAND/SSD、SK Hynix、Micron、Samsung、TSMC、CoWoS、CAPEX 等。
- 符合门槛的资料会生成 `02-kb/sources/` 来源卡草稿；是否回写 G2、概念页、实体页，仍需要人工或 Codex 进一步 distill。

## GitHub Action 权限要求

如果 Action 日志出现 `Access denied`，并提示需要 `docx:document` 或 `docx:document:readonly`，需要在飞书开放平台给同步应用补充权限：

1. 打开飞书开放平台中的同步应用。
2. 进入权限管理，添加 `docx:document` 和 `docx:document:readonly`。
3. 发布或重新发布应用版本，使权限生效。
4. 确认该应用仍是同步文件夹的协作者。
5. 回到 GitHub Actions，重新运行 `Sync Feishu Drive Files`。

## 故障排查

| 问题 | 解决 |
|------|------|
| 执行策略限制 | 脚本已包含 `-ExecutionPolicy Bypass`，如仍报错先执行 `Set-ExecutionPolicy RemoteSigned` |
| 找不到 .env | 确认 `config/feishu/.env` 存在（不是 .env.example） |
| API 返回 403 | 确认飞书应用已添加到文件夹协作者中 |
| Git push 失败 | 确认仓库已 clone 且能正常 push |
