# Annette投研系统投研 — Annette 股票池

> 最后更新：2026-06-30
>
> 格式：
> - ticker：港股 0XXXX.HK，A股 XXXXXX.SZ/.SH，美股无后缀
> - hypothesis：关联假设编号
> - notes：关注要点
>
> 行情拉取：`python scripts/fetch_market_data.py --from-watchlist`
> 宏观：`python scripts/fetch_macro_data.py`

---

## 🔴 重仓持有

| ticker | name | market | hypothesis | notes |
|--------|------|--------|------------|-------|
| 09992.HK | 泡泡玛特 | HK | — | 消费IP出海；东南亚/欧美扩张；毛利率70%+ |
| 06181.HK | 老铺黄金 | HK | — | 高端黄金珠宝；品牌溢价 vs 金价波动 |
| 0700.HK | 腾讯控股 | HK | — | 社交基本盘 + 视频号商业化；AI投流效率 |
| 1211.HK | 比亚迪 | HK | — | 新能源整车龙头；海外工厂扩张；智驾平权 |

## 🟡 轻仓持有

| ticker | name | market | hypothesis | notes |
|--------|------|--------|------------|-------|
| 1810.HK | 小米集团 | HK | — | 手机×汽车×AIoT三曲线；SU7交付/毛利率 |
| 3690.HK | 美团 | HK | — | 本地生活护城河；即时零售；海外探索 |

## 🟢 观察标的

| ticker | name | market | hypothesis | notes |
|--------|------|--------|------------|-------|
| 00981.HK | 中芯国际 | HK | H1-H6 | 主投研标的；7nm产能/28nm折旧/光刻胶断供 |
| NVDA | NVIDIA | US | — | AI芯片景气风向标；Rubin平台/CoWoS供给 |
| TSM | 台积电 | US | H1,H2,H5 | 先进制程定价权；CoWoS产能；折旧策略 |
| 300308.SZ | 中际旭创 | CN | — | 光模块龙头；800G/1.6T放量；AI算力基建 |
| 688372.SH | 伟测科技 | CN | — | 第三方芯片测试；先进封装检测；国产替代 |

## 🧭 产业方向（持续追踪，暂无具体标的）

| 方向 | 子领域 | 跟踪信号 |
|------|--------|---------|
| 机器人 | 人形机器人、工业协作、灵巧手/关节 | Tesla Optimus量产节点、宇树/傅利叶融资、减速器/丝杠国产突破 |
| 半导体-光刻机 | EUV国产化、DUV浸没式、SSA800 | 中科院EUV光源进度、SMEE 28nm量产验收、BIS新规 |
| 半导体-芯片 | AI芯片、先进制程、Chiplet | 寒武纪/海光营收、中芯N+2良率、华为麒麟迭代 |
| 半导体-存储 | HBM、NAND Flash、DRAM | 长鑫/长存产能爬坡、HBM3E国产化、三星/SK海力士扩产节奏 |

---

## 宏观指标

| ticker | name | 用途 |
|--------|------|------|
| ^GSPC | S&P 500 | 全球风险偏好 |
| ^IXIC | 纳斯达克 | 科技情绪 |
| ^VIX | 恐慌指数 | 避险信号 |
| GC=F | 黄金 | 地缘/通胀 |
| CL=F | 原油 | 宏观需求 |
| BTC-USD | 比特币 | 流动性边缘 |
| DXY | 美元指数 | 港股资金面 |

---

## 快捷命令

```bash
# 拉全部持仓+观察标的行情
python scripts/fetch_market_data.py --from-watchlist

# 只拉重仓（4只）
python scripts/fetch_market_data.py --tickers 09992.HK,06181.HK,0700.HK,1211.HK

# 拉宏观仪表盘
python scripts/fetch_macro_data.py
```
