# 飞书 → GitHub 同步配置

## 前置要求

- Windows 10/11（自带 PowerShell 5.1+）
- Git 已安装并能 push 到 GitHub
- 飞书开发者平台已创建自建应用

## 首次设置（一次性）

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
# 预览模式（不实际推送）
cd ai-investing\scripts
.\sync_feishu.ps1 -DryRun

# 正式运行
.\sync_feishu.ps1
```

### 4. 设置定时任务（每天自动运行）

```powershell
# 以管理员身份运行 PowerShell，执行以下命令：
$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-ExecutionPolicy Bypass -File D:\your\path\ai-investing\scripts\sync_feishu.ps1" `
    -WorkingDirectory "D:\your\path\ai-investing\scripts"

$trigger = New-ScheduledTaskTrigger -Daily -At 23:00
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable

Register-ScheduledTask -TaskName "Feishu-GitHub-Sync" `
    -Action $action -Trigger $trigger -Settings $settings
```

> 注意：将 `D:\your\path` 替换为你本地仓库的实际路径

## 同步行为

| 模式 | 行为 |
|------|------|
| 增量（默认） | 只同步新增或修改过的文件 |
| 全量 | 同步所有文件（修改 `.env` 中 `SYNC_MODE=full`） |

## 支持的文件类型

| 飞书文件类型 | 处理方式 | GitHub 文件 |
|-------------|---------|------------|
| 云文档（docx） | 导出为 markdown | 保留原文件名 + `.md` |
| Markdown（.md） | 直接下载 | 保留原文件名 |

## 故障排查

| 问题 | 解决 |
|------|------|
| 执行策略限制 | 脚本已包含 `-ExecutionPolicy Bypass`，如仍报错先执行 `Set-ExecutionPolicy RemoteSigned` |
| 找不到 .env | 确认 `config/feishu/.env` 存在（不是 .env.example） |
| API 返回 403 | 确认飞书应用已添加到文件夹协作者中 |
| Git push 失败 | 确认仓库已 clone 且能正常 push |
