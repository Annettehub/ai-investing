"""Create candidate hypothesis files from ZsxqCrawler articles."""
import os
from datetime import datetime

base = "C:/Users/Annette Zhang/WorkBuddy/Claw/ai-investing/02-kb/hypotheses"

hypotheses = [
    # D1-Trend
    {
        "id": "H01",
        "dim": "D1-Trend",
        "title": "AI服务器Capex 2026-2028持续高增长，台积电先进工厂满载",
        "certainty": 60,
        "falsify": "台积电先进制程产能利用率Q3<85%，或云厂商Capex指引下调>15%",
        "theme": "AI算力投资",
        "company": "TSM, NVDA, ASML",
        "anchors": [
            "[知识星球] 吴梓豪：台积电2024-2030先进工厂全覆盖3nm-A10，海外美日德同步扩张(2024-05-04)",
            "[知识星球] 吴梓豪：24年全球半导体四大看点之首-AI继续主导行业增长与创新(2025-01-08)",
            "[知识星球] 吴梓豪：老黄GTC宣示6季度5000亿美元GPU销售预期(2025-10-29)"
        ]
    },
    {
        "id": "H02",
        "dim": "D1-Trend",
        "title": "存储产业周期特性不变，2026H2供给侧过剩导致价格回落",
        "certainty": 50,
        "falsify": "三星/海力士/美光持续控制资本开支至2027，HBM需求增速维持100%+",
        "theme": "存储周期",
        "company": "Samsung, SK Hynix, MU",
        "anchors": [
            "[知识星球] 吴梓豪：存储不会改变周期特性，是AI误导的产业幻觉，涨价是HBM挤占DDR5产能(2026-04-03)",
            "[知识星球] 吴梓豪：DDR4每GB从1-2美元飙至15美元，DDR4价格倒挂超过DDR5，本质是供给骤降(2026-04-03)"
        ]
    },
    # D2-Moat
    {
        "id": "H03",
        "dim": "D2-Moat",
        "title": "台积电先进制程+先进封装双重垄断在2027年前无可替代竞争者",
        "certainty": 75,
        "falsify": "英特尔18A量产良率>80%且获>2个大客户订单，或三星2nm GAA获Nvidia/AMD订单",
        "theme": "AI算力投资",
        "company": "TSM",
        "anchors": [
            "[知识星球] 吴梓豪：台积电2024-2030所有先进工厂完整布局，先进制程4年建厂周期(2024-05-04)",
            "[知识星球] 吴梓豪：英特尔失去最先进制造能力是衰败核心，封闭生态逐步崩塌(2025-03-22)",
            "[知识星球] 吴梓豪：2nm节点High-NA未必必须，可能被Intel带跑偏(2024)"
        ]
    },
    {
        "id": "H04",
        "dim": "D2-Moat",
        "title": "英伟达GPU训练市场统治地位2027年前稳固，但推理市场ASIC侵蚀加速",
        "certainty": 65,
        "falsify": "AVGO或MRVL获得>2个超大规模云厂商放弃GPU转向ASIC训练",
        "theme": "AI算力结构变化",
        "company": "NVDA, AVGO, MRVL",
        "anchors": [
            "[知识星球] 吴梓豪：2024-2027年ASIC的CoWoS消耗量复合增长率80%高于GPU(2025-01-08/2025-10-29)",
            "[知识星球] 吴梓豪：老黄推出NVLink Fusion开放生态是从卖铲子到修路收费(2025-10-29)",
            "[知识星球] 吴梓豪：博通拿下百亿大单，GPU与ASIC未来市场格局推演(2025)"
        ]
    },
    # D3-Fund
    {
        "id": "H05",
        "dim": "D3-Fund",
        "title": "中芯国际2026年为财务健康关键年，成熟制程利润支撑先进制程爬坡",
        "certainty": 50,
        "falsify": "中芯国际28nm毛利率跌破15%或7nm良率连续2季度<30%",
        "theme": "国产替代",
        "company": "00981(中芯国际)",
        "anchors": [
            "[知识星球] 吴梓豪：中芯国际战略转型与2026财务健康关键年，28nm/45nm是绝对支柱(2025-11-14)",
            "[知识星球] 吴梓豪：AI芯片量级太低对fab不吃产能，寒武纪0.5K wafer就能创造144亿营收(2025-11-14)",
            "[知识星球] 吴梓豪：Q4营收24亿与模型吻合，毛利率18-20%，先进制程需靠成熟制程利润喂养(2025-11-14)"
        ]
    },
    # D4-Macro
    {
        "id": "H06",
        "dim": "D4-Macro",
        "title": "BIS制裁持续切香肠升级，但国内28nm以上产能2027年前基本自主可控",
        "certainty": 55,
        "falsify": "BIS出台全面设备禁运取代切香肠模式，或ASML宣布对中所有已售设备远程锁定",
        "theme": "地缘供应链",
        "company": "00981(中芯国际), ASML, 北方华创",
        "anchors": [
            "[知识星球] 吴梓豪：BIS从2022年1007到2024年1202法案切香肠式升级，华为扛过(2024-09-08)",
            "[知识星球] 吴梓豪：美荷同时发难禁GAA与光刻机，国内Fab已利用漏洞获得设备(2024-09-08)",
            "[知识星球] 吴梓豪：ASML远程锁机不可能，但维护服务停滞是最现实威胁(2025)"
        ]
    },
    {
        "id": "H07",
        "dim": "D4-Macro",
        "title": "全球半导体产业链区域化已成定局，东南亚与日本受益于产能转移",
        "certainty": 60,
        "falsify": "中美达成全面贸易妥协并降低半导体关税至2018前水平",
        "theme": "地缘供应链",
        "company": "TSM, 马来西亚封测, 日本材料",
        "anchors": [
            "[知识星球] 吴梓豪：特朗普对等关税加速全球化终结，东南亚GDP连续创新高(2025-04-05)",
            "[知识星球] 吴梓豪：中国供应链份额从高点往下但仍是王者，区域化趋势已成(2025-04-05)"
        ]
    },
    # D5-Tech
    {
        "id": "H08",
        "dim": "D5-Tech",
        "title": "CPO在2026H2随Nvidia Rubin量产商用，1.6T可插拔光模块高增长终结",
        "certainty": 55,
        "falsify": "Nvidia Rubin延迟至2027H2，或CPO良率问题导致大规模推迟",
        "theme": "光互连技术迭代",
        "company": "TSM, NVDA, AVGO, 中际旭创",
        "anchors": [
            "[知识星球] 吴梓豪：CPO是围绕半导体制造生态的技术，2026H2随Ruby正式进入大发展(2025-03-22)",
            "[知识星球] 吴梓豪：CPO对国内光模块行业是灭顶之灾，制造全在fab内完成(2025-03-22)",
            "[知识星球] 吴梓豪：光互联从机箱外附件-封装内组件-计算结构本身一部分(2026-04-17)"
        ]
    },
    {
        "id": "H09",
        "dim": "D5-Tech",
        "title": "AI推理市场GPU与ASIC长期格局趋近5:5，ASIC增速持续高于GPU",
        "certainty": 45,
        "falsify": "Nvidia推理性能保持>2x优势且价格接近ASIC，或大客户放弃自研ASIC",
        "theme": "AI算力结构变化",
        "company": "NVDA, AVGO, MRVL",
        "anchors": [
            "[知识星球] 吴梓豪：ASIC CoWoS消耗量复合增长率80%高于GPU(2025-01-08)",
            "[知识星球] 吴梓豪：预训练增长见顶后推理将主导，ASIC替代GPU加速(2025-10-29)",
            "[知识星球] 吴梓豪：博通拿下百亿大单，未来三年GPU与ASIC推演(2025)"
        ]
    },
    # D6-Demand
    {
        "id": "H10",
        "dim": "D6-Demand",
        "title": "中国AI芯片本土化需求2026-2028呈爆发式增长，产能缺口推动制程升级",
        "certainty": 50,
        "falsify": "中芯国际7nm良率<30%持续2季度，或华为Ascend出货量<200万颗",
        "theme": "国产替代",
        "company": "00981(中芯国际), 寒武纪, 华为, 北方华创",
        "anchors": [
            "[知识星球] 吴梓豪：中国需要多少先进制程产能，答案是还差很远(2025)",
            "[知识星球] 吴梓豪：Nikkei报道国内先进制程需提高五倍满足AI需求，解读属实(2025)",
            "[知识星球] 吴梓豪：寒武纪0.5K wafer可产144亿营收，芯片单价高但产能需求小(2025-11-14)"
        ]
    },
    # D7-Chain
    {
        "id": "H11",
        "dim": "D7-Chain",
        "title": "AI产业链价值从硬件训练侧向推理+应用侧迁移，Foundry和设备商持续受益",
        "certainty": 50,
        "falsify": "Nvidia毛利率长期维持>70%且预训练芯片出货>推理芯片，或AI应用变现困难",
        "theme": "AI价值链迁移",
        "company": "TSM, NVDA, ASML",
        "anchors": [
            "[知识星球] 吴梓豪：逻辑7nm后摩尔定律cost scaling失效，进入性能溢价阶段(2026-04-03)",
            "[知识星球] 吴梓豪：台积电利用制造优势通过开放平台构建硅光生态链(2025-03-22)",
            "[知识星球] 吴梓豪：光互联定价权在系统架构定义者/DSP控制者/硅光制造平台(2026-04-17)"
        ]
    },
    {
        "id": "H12",
        "dim": "D7-Chain",
        "title": "先进封装(CoWoS/SoIC)是AI时代最稀缺产能，Foundry向下兼容封装，OSAT向上突破困难",
        "certainty": 60,
        "falsify": "OSAT(日月光/安靠/长电)量产CoWoS级别先进封装并获Nvidia/AMD下单",
        "theme": "先进封装",
        "company": "TSM, 日月光, 长电科技",
        "anchors": [
            "[知识星球] 吴梓豪：从CoWoS到SoW-X，台积电全面重构系统(2025)",
            "[知识星球] 吴梓豪：传统OSAT在先进封装几无话语权，先进封装适合Foundry向下兼容(2026-01-17)",
            "[知识星球] 吴梓豪：台积电OIP推3D IC设计新标准(2025)"
        ]
    },
]

for h in hypotheses:
    fid = h["id"]
    fname = f"_candidate_{fid}.md"
    fpath = os.path.join(base, fname)
    today = datetime.now().strftime("%Y-%m-%d")
    anchors_txt = "\n".join(f"  - {a}" for a in h["anchors"])

    content = f"""# {fid} [{h["dim"]}] {h["title"]}

- **状态**: 候选（待审核）
- **维度**: {h["dim"]}
- **certainty%**: ?%（初始建议: {h["certainty"]}%）
- **证伪条件**: {h["falsify"]}
- **关联 theme**: {h["theme"]}
- **关联 company**: {h["company"]}
- **数据锚点**: 
{anchors_txt}
- **创建日期**: {today}
- **最后更新**: {today}

## 来源文章

- 主要来源：吴梓豪知识星球「半导体大佬的会议室」

## 变更记录

| 日期 | certainty% 变更 | 原因 | 来源 |
|------|----------------|------|------|
| （创建） | 初始: {h["certainty"]}%（建议值，待审核确认） | AI从星球专栏提炼 | 知识星球专栏 |
"""
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Created: {fname}")

# Summary
print(f"\nTotal: {len(hypotheses)} candidate hypotheses")
print("Coverage by dimension:")
dims = {}
for h in hypotheses:
    d = h["dim"]
    dims[d] = dims.get(d, 0) + 1
for d, c in sorted(dims.items()):
    print(f"  {d}: {c}")
