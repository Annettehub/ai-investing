# 本地工具与 GitHub 推送流程

## 本机工具体检

当前已检测到：

| 工具 | 状态 | 说明 |
| --- | --- | --- |
| Git | 已安装 | 可提交和推送仓库 |
| Node.js | 已安装 | 当前为 Node 24，可运行网站构建工具 |
| npm / npx | 已安装 | 可安装和运行前端依赖 |
| Python | 缺失 | `python` 不可用，`py` 启动器存在但没有安装解释器 |
| GitHub CLI (`gh`) | 缺失 | 不影响 Git 推送，但影响命令行登录、PR、Actions 查看 |

建议补齐：

1. Python 3.12 或 3.13：用于运行 `scripts/*.py`。
2. GitHub CLI：用于检查登录状态、触发 Actions、查看部署状态。
3. 一个固定的本地预览命令：用于发布前检查网站。

## 从本地推送到 GitHub

当前远程仓库：

```powershell
git@github.com:Annettehub/ai-investing.git
```

日常推送流程：

```powershell
cd D:\WorkBuddy\Claw\Claw\ai-investing-quartz
git status
git add README.md docs .gitignore scripts
git add 02-kb 03-raw 04-output value-investing
git status
git commit -m "Update knowledge base"
git push origin main
```

如果只是修改网站工程：

```powershell
cd D:\WorkBuddy\Claw\Claw\ai-investing-quartz
git add site .github README.md docs
git commit -m "Improve website publishing"
git push origin main
```

## 推送前检查

每次推送前确认这些文件没有被加入：

```powershell
git status --short
git diff --cached --name-only
```

不应该出现在提交里的文件：

- `config/.env`
- `.env`
- token、key、secret 文件
- 本地账号数据库
- `site/dist/`
- `node_modules/`

如果 `.env` 已经被 Git 跟踪，保留本地文件但停止跟踪：

```powershell
git rm --cached config/.env
git commit -m "Stop tracking local env file"
```

## 本地预览未来网站

旧 Quartz 工程已删除。以后如果换成 Astro / Starlight 或 VitePress，预览命令会放在新网站目录里，通常是：

```powershell
cd D:\WorkBuddy\Claw\Claw\ai-investing-quartz\site
npm run dev
```
