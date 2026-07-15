# SEC 官方财报入口

这里保存美股 watchlist 的 SEC 官方披露同步结果。

## 数据范围

- 公司提交历史：10-Q、10-K、8-K、20-F、6-K。
- 结构化财务指标：来自 SEC XBRL companyfacts。
- 电话会材料：只在公司通过 8-K / 6-K 或附件正式披露时记录官方链接；第三方免费 transcript 暂不自动抓取。

## 当前文件

- `us-equity-earnings/YYYY-MM-DD-sec-earnings-update.md`：当日可读摘要。
- `us-equity-earnings/YYYY-MM-DD-sec-earnings-update.json`：当日结构化快照。

## 更新方式

本地运行：

```bash
python scripts/sync_sec_earnings.py --days 45
```

GitHub Actions：

- `.github/workflows/sync-sec-earnings.yml`
- 工作日每天两次检查。
- 通过 SEC accession number 去重，只有新增披露或指标变化时才提交。
