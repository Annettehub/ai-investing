@echo off
chcp 65001 >nul
title Feishu to GitHub Sync

:: 获取脚本所在目录
set "SCRIPT_DIR=%~dp0"

:: 运行 PowerShell 脚本
powershell.exe -ExecutionPolicy Bypass -File "%SCRIPT_DIR%sync_feishu.ps1" %*

pause
