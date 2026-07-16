#Requires -Version 5.1
<#
.SYNOPSIS
    飞书云文档 → GitHub 自动同步脚本
.DESCRIPTION
    扫描飞书指定文件夹中的 docx 和 md 文件，导出/下载为 markdown，
    推送到 GitHub 仓库的 02-kb/sources/feishu/ 目录。
    增量模式：只同步新增或修改过的文件。
.PARAMETER DryRun
    预览模式：显示将要同步的文件但不执行实际操作
.EXAMPLE
    .\sync_feishu.ps1
    .\sync_feishu.ps1 -DryRun
#>
param([switch]$DryRun)

# ── 配置加载 ──────────────────────────────────────────
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptDir "..")
$envFile = Join-Path $repoRoot "config\feishu\.env"
$syncRecordFile = Join-Path $repoRoot "config\feishu\.sync_record.json"

if (-not (Test-Path $envFile)) {
    Write-Host "[错误] 找不到配置文件: $envFile" -ForegroundColor Red
    Write-Host "请复制 config/feishu/.env.example 为 .env 并填入你的飞书凭证" -ForegroundColor Yellow
    exit 1
}

# 加载 .env
Get-Content $envFile | ForEach-Object {
    if ($_ -match '^\s*([^#\s][^=]*)\s*=\s*(.*?)\s*$') {
        [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2], "Process")
    }
}

$appId = $env:FEISHU_APP_ID
$appSecret = $env:FEISHU_APP_SECRET
$folderToken = $env:FEISHU_FOLDER_TOKEN
$targetDir = Join-Path $repoRoot $env:TARGET_DIR
$syncMode = $env:SYNC_MODE

if (-not $appId -or -not $appSecret -or -not $folderToken) {
    Write-Host "[错误] FEISHU_APP_ID / FEISHU_APP_SECRET / FEISHU_FOLDER_TOKEN 未配置" -ForegroundColor Red
    exit 1
}

# ── 工具函数 ──────────────────────────────────────────
function Get-Token {
    $body = @{ app_id = $appId; app_secret = $appSecret } | ConvertTo-Json -Compress
    $res = Invoke-RestMethod -Uri "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" `
        -Method Post -Body $body -ContentType "application/json" -ErrorAction Stop
    if ($res.code -ne 0) { throw "获取 token 失败: $($res.msg)" }
    return $res.tenant_access_token
}

function Get-FolderFiles {
    param([string]$Token)
    $allFiles = @()
    $pageToken = $null
    do {
        $uri = "https://open.feishu.cn/open-apis/drive/v1/files?folder_token=$folderToken&page_size=200"
        if ($pageToken) { $uri += "&page_token=$pageToken" }
        $res = Invoke-RestMethod -Uri $uri -Headers @{ Authorization = "Bearer $Token" } -ErrorAction Stop
        if ($res.code -ne 0) { throw "获取文件列表失败: $($res.msg)" }
        $allFiles += $res.data.files
        $pageToken = $res.data.next_page_token
    } while ($pageToken)
    return $allFiles
}

function Export-DocxToMarkdown {
    param([string]$Token, [string]$DocToken)
    # 创建导出任务
    $body = @{ file_extension = "md"; token = $DocToken; type = "docx" } | ConvertTo-Json -Compress
    $res = Invoke-RestMethod -Uri "https://open.feishu.cn/open-apis/drive/v1/export_tasks" `
        -Method Post -Headers @{ Authorization = "Bearer $Token"; "Content-Type" = "application/json" } `
        -Body $body -ErrorAction Stop
    if ($res.code -ne 0) { throw "创建导出任务失败: $($res.msg)" }
    $ticket = $res.data.ticket

    # 轮询等待（最多 60 秒）
    for ($i = 0; $i -lt 30; $i++) {
        Start-Sleep -Seconds 2
        $res = Invoke-RestMethod -Uri "https://open.feishu.cn/open-apis/drive/v1/export_tasks/$ticket" `
            -Headers @{ Authorization = "Bearer $Token" } -ErrorAction Stop
        if ($res.data.result.file_token) { return $res.data.result.file_token }
    }
    throw "导出任务超时"
}

function Download-ExportedFile {
    param([string]$Token, [string]$FileToken, [string]$OutPath)
    $uri = "https://open.feishu.cn/open-apis/drive/v1/export_tasks/download?file_token=$FileToken"
    Invoke-RestMethod -Uri $uri -Headers @{ Authorization = "Bearer $Token" } `
        -OutFile $OutPath -ErrorAction Stop
}

function Download-MdFile {
    param([string]$Token, [string]$FileToken, [string]$OutPath)
    # 对于 md 文件，先获取下载链接
    $res = Invoke-RestMethod -Uri "https://open.feishu.cn/open-apis/drive/v1/files/$FileToken/download" `
        -Headers @{ Authorization = "Bearer $Token" } -ErrorAction Stop
    if ($res.code -ne 0) { throw "获取下载链接失败: $($res.msg)" }
    Invoke-RestMethod -Uri $res.data.file_token -OutFile $OutPath -ErrorAction Stop
}

function Get-SafeFileName {
    param([string]$Name)
    return ($Name -replace '[\\/:*?"<>|]', '_')
}

# ── 主流程 ──────────────────────────────────────────
Write-Host "`n===== 飞书 → GitHub 同步 =====" -ForegroundColor Cyan
Write-Host "仓库: $repoRoot"
Write-Host "目标: $($env:TARGET_DIR)"
Write-Host "模式: $syncMode"
if ($DryRun) { Write-Host "[预览模式] 不执行实际操作`n" -ForegroundColor Magenta }

# 确保目标目录存在
if (-not $DryRun) {
    if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Path $targetDir -Force | Out-Null }
}

# 读取同步记录
$syncRecord = @{}
if (Test-Path $syncRecordFile) {
    $syncRecord = Get-Content $syncRecordFile -Raw | ConvertFrom-Json -AsHashtable
    if (-not $syncRecord) { $syncRecord = @{} }
}

# 获取飞书文件列表
Write-Host "`n[1/4] 获取飞书文件列表..." -ForegroundColor Yellow
$token = Get-Token
$files = Get-FolderFiles -Token $token
$docFiles = $files | Where-Object { $_.type -in @("docx", "file") }
Write-Host "     共 $($files.Count) 个文件，文档 $($docFiles.Count) 个" -ForegroundColor Gray

# 过滤需同步的文件
$toSync = @()
foreach ($f in $docFiles) {
    $isMd = $f.name -like "*.md"
    $isDocx = $f.type -eq "docx"
    if (-not $isMd -and -not $isDocx) { continue }

    $safeName = Get-SafeFileName -Name $f.name
    if ($isDocx -and -not $safeName.EndsWith(".md")) { $safeName += ".md" }

    $lastEdit = $f.edited_time
    $prevEdit = $syncRecord[$f.token]

    if ($syncMode -eq "incremental" -and $prevEdit -and $prevEdit -eq $lastEdit) {
        continue  # 未修改，跳过
    }

    $toSync += [PSCustomObject]@{
        Token    = $f.token
        Name     = $f.name
        SafeName = $safeName
        Type     = $f.type
        EditTime = $lastEdit
    }
}

if ($toSync.Count -eq 0) {
    Write-Host "`n[✓] 所有文件已是最新，无需同步" -ForegroundColor Green
    exit 0
}

Write-Host "     需同步: $($toSync.Count) 个" -ForegroundColor Cyan

# 同步文件
Write-Host "`n[2/4] 同步文件..." -ForegroundColor Yellow
$successCount = 0
$failCount = 0

foreach ($f in $toSync) {
    $outPath = Join-Path $targetDir $f.SafeName
    $indicator = if ($syncRecord[$f.Token]) { "[更新]" } else { "[新增]" }
    Write-Host "     $indicator $($f.Name) " -NoNewline

    if ($DryRun) {
        Write-Host "→ 预览跳过" -ForegroundColor Magenta
        continue
    }

    try {
        if ($f.Type -eq "docx") {
            $fileToken = Export-DocxToMarkdown -Token $token -DocToken $f.Token
            Download-ExportedFile -Token $token -FileToken $fileToken -OutPath $outPath
        } else {
            Download-MdFile -Token $token -FileToken $f.Token -OutPath $outPath
        }

        $syncRecord[$f.Token] = $f.EditTime
        $successCount++
        Write-Host "✓" -ForegroundColor Green
    } catch {
        $failCount++
        Write-Host "✗ $_" -ForegroundColor Red
    }
}

# 保存同步记录
if (-not $DryRun) {
    $syncRecord | ConvertTo-Json | Set-Content $syncRecordFile -Encoding UTF8
}

# Git 推送
Write-Host "`n[3/4] Git 操作..." -ForegroundColor Yellow
if ($DryRun) {
    Write-Host "     [预览] git add + commit + push" -ForegroundColor Magenta
} else {
    Set-Location $repoRoot
    git add $env:TARGET_DIR $syncRecordFile 2>$null

    $diff = git diff --cached --quiet 2>$null; $hasChanges = $LASTEXITCODE -ne 0

    if ($hasChanges) {
        $commitMsg = "Sync feishu: $(Get-Date -Format 'yyyy-MM-dd') $($toSync.Count) files"
        git commit -m $commitMsg 2>$null | Out-Null
        git push 2>$null | Out-Null
        Write-Host "     ✓ 已推送 ($successCount 成功" -NoNewline
        if ($failCount -gt 0) { Write-Host ", $failCount 失败" -NoNewline -ForegroundColor Red }
        Write-Host ")" -ForegroundColor Green
    } else {
        Write-Host "     无变更需提交" -ForegroundColor Gray
    }
}

Write-Host "`n===== 同步完成 =====" -ForegroundColor Cyan
