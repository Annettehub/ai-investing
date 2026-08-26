import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { parseEntity, moduleFor, plain, tableColumnWidths } from './entity-document.mjs';

const source = fs.readFileSync(new URL('../../../02-kb/entities/06181-老铺黄金.md', import.meta.url), 'utf8');
const document = parseEntity(source);
const blocks = document.allBlocks;

test('all content columns share the remaining width equally', () => {
  for (const block of blocks.filter(b => b.kind === 'table')) {
    const widths = tableColumnWidths(block);
    assert.equal(widths.length, block.header.length);
    assert.equal(widths[0], '280px');
    assert.ok(widths.slice(1).every(width => width === widths[1]));
  }
});

test('title columns stay fixed at 280px independent of label length', () => {
  const table = title => ({ header: [{ text: '#' }, { text: 'Content' }, { text: 'Content' }], rows: [[{ text: title }]] });
  const width = title => tableColumnWidths(table(title))[0];
  assert.equal(width('1'), '280px');
  assert.equal(width('Short'), width('A longer label'));
  assert.equal(width('A'.repeat(200)), '280px');
  assert.equal(tableColumnWidths({ header: [{ text: 'A longer header' }, { text: 'Content' }], rows: [] })[0], width('A longer header'));
  assert.deepEqual(tableColumnWidths({ header: [{ text: 'Only column' }], rows: [] }), ['100%']);
  assert.deepEqual(tableColumnWidths({ header: [], rows: [] }), []);
});

test('all source sections and content blocks remain represented', () => {
  const sourceSections = document.tree.children.filter(n => n.type === 'heading' && [2, 3].includes(n.depth));
  assert.deepEqual(document.sections.map(s => s.title), sourceSections.map(plain));
  const sourceNodes = document.tree.children.filter(n => !(n.type === 'heading' && n.depth <= 3));
  assert.deepEqual(blocks.map(b => b.node), sourceNodes);
  assert.equal(document.sections.length, 29);
});

test('crosscheck and business remain matrices; all table cells survive', () => {
  for (const section of document.sections) for (const block of section.blocks.filter(b => b.rows)) {
    assert.deepEqual([block.header, ...block.rows].map(row => row.map(c => c.text)), block.node.children.map(row => row.children.map(plain)));
    if (['crosscheck', 'business'].includes(section.module)) assert.equal(block.kind, 'table');
  }
});

test('dashboard and hypotheses retain their complete source details', () => {
  assert.equal(blocks.find(b => b.kind === 'dashboard').metrics.length, 9);
  const hypotheses = blocks.find(b => b.kind === 'hypotheses');
  assert.equal(hypotheses.cards.length, 4);
  assert.match(hypotheses.cards[0].body, /2009年即开设首家古法金门店/);
  assert.match(hypotheses.cards[3].body, /回报预期/);
  assert.equal(blocks.find(b => b.kind === 'moat').rows.length, 5);
});

test('all five duel blocks render full text and correctly order bear-first input', () => {
  const duels = blocks.filter(b => b.kind === 'duel');
  assert.equal(duels.length, 5);
  const management = document.sections.find(s => s.title.includes('管理层与资本配置')).blocks.find(b => b.kind === 'duel');
  assert.match(management.bull, /16年持续深耕/);
  assert.match(management.bear, /在我这里都是扣分的/);
  assert.match(duels[0].bull, /重合率82.4%/);
  assert.match(duels[0].bear, /定价权未能真正脱离金价周期/);
});

test('charts use exact source cells and do not manufacture missing values', () => {
  const charts = blocks.filter(b => b.chart).map(b => b.chart);
  assert.equal(charts.length, 3);
  assert.deepEqual(charts.find(c => c.signed).series[0].points.map(p => p.value), [-12.28, -68.48, 20.08]);
  const incomplete = parseEntity('## 9 财务数据\n### 9.3 盈利能力\n| 指标 | 2024年 | 2025年 | 2026H1 | 评价 |\n|---|---|---|---|---|\n| 毛利率 | 41.2% | [待验证] | 41.3% | 待观察 |');
  assert.equal(incomplete.allBlocks.find(b => b.rows).chart, null);
});

test('semantic module mapping supports chapter renumbering and unknown sections', () => {
  assert.equal(moduleFor('2 季度跟踪仪表盘'), 'dashboard');
  assert.equal(moduleFor('7 季度跟踪仪表盘（每季财报后更新）'), 'dashboard');
  const unknown = parseEntity('## 19 新增内容\n\n完整原文 **不能遗漏**。\n\n| 项目 | 说明 |\n|---|---|\n| A \\| B | [链接](https://example.com) |');
  assert.equal(unknown.sections[0].module, 'prose');
  assert.match(unknown.allBlocks[0].sourceHtml, /不能遗漏/);
  assert.equal(unknown.allBlocks[1].rows[0][0].text, 'A | B');
  assert.match(unknown.allBlocks[1].rows[0][1].html, /href="https:\/\/example.com"/);
});

test('valuation preserves institution ranges and verification flags', () => {
  assert.equal(document.highlights.find(h => h.label === '2026E PE').value, '7-11倍（机构预测区间）');
  assert.match(document.highlights.find(h => h.label === '总市值').value, /待验证/);
  assert.match(document.highlights.find(h => h.label === '股息率TTM').value, /瑞银估算/);
});

for (const [file, expected] of [
  ['09992-泡泡玛特.md', { name: '泡泡玛特', metrics: 11, hypotheses: 4, marketCap: '2,109.54亿港元' }],
  ['0700-腾讯控股.md', { name: '腾讯控股', metrics: 16, hypotheses: 7, marketCap: '约 4.0 万亿港元' }],
]) {
  test(`${file}: reusable modules retain source text and valuation units`, () => {
    const doc = parseEntity(fs.readFileSync(new URL(`../../../02-kb/entities/${file}`, import.meta.url), 'utf8'));
    assert.equal(doc.name, expected.name);
    assert.equal(doc.allBlocks.find(b => b.kind === 'dashboard').metrics.length, expected.metrics);
    assert.equal(doc.allBlocks.find(b => b.kind === 'hypotheses').cards.length, expected.hypotheses);
    assert.equal(doc.allBlocks.find(b => b.kind === 'moat').rows.length, 5);
    assert.equal(doc.highlights.find(h => h.label === '总市值').headline, expected.marketCap);
    assert.equal(doc.highlights.length, 4);
    assert.ok(doc.allBlocks.some(b => b.chart));
    for (const block of doc.allBlocks.filter(b => b.rows)) {
      assert.deepEqual([block.header, ...block.rows].map(row => row.map(c => c.text)), block.node.children.map(row => row.children.map(plain)));
    }
    if (file.startsWith('0700')) {
      assert.match(doc.sections.find(s => s.module === 'references').blocks[0].sourceHtml, /id="reference-20"/);
      assert.match(doc.sections[0].blocks[0].sourceHtml, /href="#reference-11"/);
      assert.match(doc.sections[0].blocks[0].sourceHtml, /⁽¹¹⁾/);
      assert.equal(doc.sections.find(s => /两个腾讯/.test(s.title)).module, 'business');
    }
  });
}
