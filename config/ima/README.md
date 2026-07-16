# IMA 原文入库流程

目标：把腾讯 IMA 知识库中的原文资料推送到 `03-raw/wechat`，不做摘要、不做改写、不清洗正文。

## 推荐流程

1. 在本机创建或使用这个文件夹：

```powershell
D:\WorkBuddy\Claw\ima-inbox
```

2. 从 IMA 中导出或复制原文，保存为 `.md`、`.txt`、`.html`、`.pdf` 或 `.docx`，放入上面的 inbox。

3. 预览入库：

```powershell
cd D:\WorkBuddy\Claw\ai-investing
python scripts\import_ima_wechat.py
```

4. 确认无误后推送 GitHub：

```powershell
python scripts\import_ima_wechat.py --push
```

## 行为说明

- 脚本只复制原始文件字节，不改正文。
- 默认入库位置：`03-raw/wechat`。
- 默认 inbox：`D:\WorkBuddy\Claw\ima-inbox`。
- 用 SHA256 去重，状态记录在 `05-meta/ima-wechat-import-state.json`。
- 默认保留 inbox 源文件；如果确认已经入库并想清理 inbox，加 `--delete-source`。
- 文件名会做最小安全处理，仅替换 Windows/Git 不适合的路径字符。

## 为什么不用 WorkBuddy 直接写入

WorkBuddy 当前容易把 IMA 内容改写成摘要。这个脚本的边界更窄：只做“原文搬运 + 去重 + GitHub 推送”，不做知识整理。

## 自动化边界

如果未来 IMA 提供稳定的全文 API，可以再增加自动抓取层。但自动抓取层也必须先把原文落到 `03-raw/wechat`，后续知识整理另走 ingest review 流程。
