import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import assert from 'node:assert/strict';
import { parseEntity, plain } from '../src/lib/entity-document.mjs';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';

const [browserModule, artifactDir, target = 'http://127.0.0.1:4322/ai-investing/preview/entities/06181/', attachmentPath, sourcePath = '../../02-kb/entities/06181-老铺黄金.md'] = process.argv.slice(2);
if (!browserModule || !artifactDir) throw new Error('Usage: node scripts/check-entity-preview.mjs <playwright module path> <artifact directory> [preview URL]');
const { chromium } = await import(pathToFileURL(browserModule).href);
const source = await fs.readFile(new URL(sourcePath, import.meta.url), 'utf8');
const doc = parseEntity(source);
const normalized = text => text.replace(/\s+/g, '');
const leaves = node => node.children ? node.children.flatMap(leaves) : node.type === 'text' || node.type === 'inlineCode' ? [node.value] : [];
const sourceParser = unified().use(remarkParse).use(remarkGfm);
const baseline = sourceParser.parse(source);
// Expectations come from untouched source AST, not the page's transformed model.
const sourceBlocks = [];
let blockIndex = 0, sectionTitle = '建档信息与观点来源';
for (const node of baseline.children) {
  if (node.type === 'heading' && node.depth <= 3) { if (node.depth > 1) sectionTitle = plain(node); continue; }
  sourceBlocks.push({ id: `source-${++blockIndex}`, node, section: sectionTitle, line: node.position.start.line });
}
await fs.mkdir(artifactDir, { recursive: true });
const browser = await chromium.launch({ headless: true, ...(process.env.ENTITY_BROWSER_CHANNEL ? { channel: process.env.ENTITY_BROWSER_CHANNEL } : {}) });
const errors = [], report = { sourceBlocks: 0, textFragments: 0, tableCells: 0, widths: [], screenshots: [], interactions: [], strictTextAudit: { failures: [], sections: [], blocks: [], tableCells: 0, comparison: 'Exact text after removing whitespace and presentation-only labels; punctuation and qualifiers retained.' } };
try {
  const page = await browser.newPage({ viewport: { width: 1600, height: 1050 }, deviceScaleFactor: 1 });
  page.on('pageerror', error => errors.push(error.message));
  page.on('response', response => {
    if (response.status() >= 400 && ['stylesheet', 'script', 'image'].includes(response.request().resourceType())) errors.push(`Asset ${response.status()}: ${response.url()}`);
  });
  await page.goto(target, { waitUntil: 'networkidle' });
  assert.equal(await page.title(), `${doc.name} | AI Investing`);
  assert.equal(await page.locator('body[data-entity-layout="v1"]').count(), 1);
  assert.equal(await page.locator('link[href="/ai-investing/styles/entity.css"]').count(), 0, 'Legacy theme CSS leaked into standalone page');
  const theme = await page.evaluate(() => ({ scheme: getComputedStyle(document.documentElement).colorScheme, offset: getComputedStyle(document.documentElement).scrollPaddingTop, ink: getComputedStyle(document.body).color, background: getComputedStyle(document.body).backgroundColor }));
  assert.deepEqual(theme, { scheme: 'light', offset: '0px', ink: 'rgb(25, 45, 41)', background: 'rgb(251, 253, 252)' }, 'Starlight global styles overrode the entity layout');
  if (!target.includes('/preview/')) {
    assert.equal(await page.locator('meta[name="robots"][content*="noindex"]').count(), 0);
    assert.equal(await page.locator('.preview-badge').count(), 0);
  }
  const actualBlocks = await page.locator('[data-source-block]').evaluateAll(nodes => Object.fromEntries(nodes.map(node => {
    const text = (selector, scope = node) => scope.querySelector(selector)?.textContent || '';
    const kind = [...node.classList].find(c => c.startsWith('source-block--'))?.slice('source-block--'.length);
    const closed = node.closest('details:not([open])');
    let fullText = node.textContent;
    if (kind === 'hypotheses') fullText = [...node.querySelectorAll('.hypothesis-card')].map(card => text('.hypothesis-heading h4', card) + text('.hypothesis-body', card)).join('');
    const rows = kind === 'table' ? [...node.querySelectorAll('tbody tr')].map(row => [...row.children].map(cell => cell.textContent))
      : kind === 'moat' ? [...node.querySelectorAll('.moat-card')].map(card => ['h4', '.moat-description', '.moat-judgment p', '.status-badge'].map(selector => text(selector, card)))
      : kind === 'dashboard' ? [...node.querySelectorAll('.metric-card')].map(card => [String(Number(text('.item-index', card))), ...['h4', '.metric-detail', '.metric-threshold strong', '.metric-state'].map(selector => text(selector, card))]) : null;
    return [node.id, { kind, fullText, rows, headers: [...node.querySelectorAll('thead th')].map(cell => cell.textContent), duel: kind === 'duel' ? { label: text('.duel-heading'), bull: text('.duel-side--bull > div'), bear: text('.duel-side--bear > div') } : null, foldedUnder: closed?.querySelector('summary')?.textContent || null }];
  })));
  const checkExact = (expected, actual, location) => {
    if (normalized(expected) !== normalized(actual)) report.strictTextAudit.failures.push({ location, expected, actual });
  };
  for (const block of sourceBlocks) {
    if (block.node.type === 'thematicBreak') continue;
    const actual = actualBlocks[block.id];
    assert.ok(actual, `Missing independent source block ${block.id}`);
    const before = report.strictTextAudit.failures.length;
    if (block.node.type === 'table') {
      const expected = block.node.children.slice(1).map(row => row.children.map(plain));
      assert.equal(actual.rows.length, expected.length, `Row count changed at ${block.id}`);
      for (const [r, row] of expected.entries()) {
        assert.equal(actual.rows[r].length, row.length, `Column count changed at ${block.id}`);
        for (const [c, cell] of row.entries()) { checkExact(cell, actual.rows[r][c], `${block.id} row ${r + 1} column ${c + 1}`); report.strictTextAudit.tableCells++; }
      }
      if (actual.kind === 'table') for (const [c, header] of block.node.children[0].children.entries()) checkExact(plain(header), actual.headers[c], `${block.id} header ${c + 1}`);
    } else {
      let actualText = actual.fullText;
      if (actual.duel) {
        const original = plain(block.node);
        actualText = actual.duel.label + (original.indexOf('多方') < original.indexOf('空方') ? actual.duel.bull + actual.duel.bear : actual.duel.bear + actual.duel.bull);
      }
      checkExact(plain(block.node), actualText, block.id);
    }
    report.strictTextAudit.blocks.push({ id: block.id, section: block.section, sourceLine: block.line, kind: actual.kind, characters: normalized(plain(block.node)).length, foldedUnder: actual.foldedUnder, exact: before === report.strictTextAudit.failures.length });
  }
  checkExact(plain(baseline.children.find(n => n.type === 'heading' && n.depth === 1)), await page.locator('.source-title').textContent(), 'document title');
  const renderedHeadings = await page.locator('.entity-section > h2, .entity-section > h3').allTextContents();
  const sourceHeadings = baseline.children.filter(n => n.type === 'heading' && [2, 3].includes(n.depth));
  assert.equal(renderedHeadings.length, sourceHeadings.length);
  sourceHeadings.forEach((node, index) => checkExact(plain(node), renderedHeadings[index], `heading ${index}`));
  report.strictTextAudit.sections = [...new Set(report.strictTextAudit.blocks.map(b => b.section))].map(title => {
    const blocks = report.strictTextAudit.blocks.filter(b => b.section === title);
    return { title, blocks: blocks.length, characters: blocks.reduce((sum, b) => sum + b.characters, 0), exact: blocks.every(b => b.exact) };
  });
  if (attachmentPath) {
    const uploaded = sourceParser.parse(await fs.readFile(attachmentPath, 'utf8'));
    const textsBySection = tree => { const result = {}; let title = '前言'; for (const node of tree.children) { if (node.type === 'heading' && node.depth === 1) continue; if (node.type === 'heading' && node.depth <= 3) { title = plain(node); result[title] = ''; } else result[title] = (result[title] || '') + plain(node); } return result; };
    const oldText = textsBySection(uploaded), newText = textsBySection(baseline);
    report.attachmentComparison = { path: attachmentPath, sections: Object.keys(newText).map(title => ({ title, exact: normalized(oldText[title] || '') === normalized(newText[title]) })), titleBefore: plain(uploaded.children.find(n => n.type === 'heading')), titleAfter: plain(baseline.children.find(n => n.type === 'heading')) };
  }
  const folded = report.strictTextAudit.blocks.filter(b => b.foldedUnder);
  if (folded.length) await page.locator('.document-metadata summary').click();
  report.strictTextAudit.invisibleTextAfterExpanding = await page.locator('[data-source-block]').evaluateAll(blocks => blocks.flatMap(block => {
    const findings = [];
    const walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.textContent?.trim() || node.parentElement?.closest('script, style')) continue;
      const range = document.createRange(); range.selectNodeContents(node);
      if (![...range.getClientRects()].some(r => r.width > 0 && r.height > 0)) findings.push({ block: block.id, text: node.textContent });
    }
    return findings;
  }));
  if (folded.length) await page.locator('.document-metadata summary').click();
  await fs.writeFile(path.join(artifactDir, 'content-audit.json'), JSON.stringify({ strictTextAudit: report.strictTextAudit, attachmentComparison: report.attachmentComparison }, null, 2));
  assert.deepEqual(report.strictTextAudit.failures, [], 'Exact source-to-page text comparison failed');
  assert.deepEqual(report.strictTextAudit.invisibleTextAfterExpanding, [], 'Some source text remains hidden');
  const snapshot = await page.locator('[data-source-block]').evaluateAll(nodes => Object.fromEntries(nodes.map(n => [n.getAttribute('data-source-block'), n.textContent])));
  for (const block of doc.allBlocks) {
    // Competition separator rules have no textual content.
    if (block.node.type === 'thematicBreak') continue;
    assert.ok(block.id in snapshot, `Missing source block ${block.id}`);
    const visibleText = normalized(snapshot[block.id]);
    // Card headings and metric labels replace repeated table column headings.
    const textNodes = ['moat', 'dashboard'].includes(block.kind) ? { children: block.node.children.slice(1) } : block.node;
    const fragments = leaves(textNodes).flatMap(text => block.kind === 'duel' ? text.split(/(?=多方|空方)/) : [text]).map(normalized).filter(Boolean);
    for (const fragment of fragments) { assert.ok(visibleText.includes(fragment), `${block.id} missing: ${fragment}`); report.textFragments++; }
    if (block.rows) for (const row of block.rows) for (const cell of row) {
      assert.ok(visibleText.includes(normalized(cell.text)), `${block.id} missing cell: ${cell.text}`); report.tableCells++;
    }
    report.sourceBlocks++;
  }
  assert.deepEqual(await page.locator('.entity-section').evaluateAll(nodes => nodes.map(n => n.getAttribute('data-section-title'))), doc.sections.map(s => s.title));
  const metrics = doc.allBlocks.filter(b => b.kind === 'dashboard').flatMap(b => b.metrics);
  assert.equal(await page.locator('.duel-grid').count(), doc.allBlocks.filter(b => b.kind === 'duel').length);
  assert.equal(await page.locator('.metric-card').count(), metrics.length);
  assert.equal(await page.locator('.entity-chart').count(), doc.allBlocks.filter(b => b.chart).length);
  assert.equal(await page.locator('.hypothesis-card').count(), doc.allBlocks.filter(b => b.kind === 'hypotheses').flatMap(b => b.cards).length);
  assert.equal(await page.locator('.moat-card').count(), doc.allBlocks.filter(b => b.kind === 'moat').flatMap(b => b.rows).length);
  assert.equal(await page.locator('.competition-card').count(), doc.sections.flatMap(s => s.competitors || []).length);
  assert.equal(await page.locator('svg').evaluateAll(icons => icons.filter(icon => !icon.querySelector('path, use, circle, rect')).length), 0, 'Blank icon');
  for (const width of [1920, 1600, 1280, 1024, 768, 390, 375]) {
    await page.setViewportSize({ width, height: 950 });
    await page.evaluate(() => window.scrollTo(0, 0));
    const layout = await page.evaluate(() => ({ width: innerWidth, scroll: document.documentElement.scrollWidth, align: [...document.querySelectorAll('.duel-grid')].map(grid => [...grid.children].map(el => { const r = el.getBoundingClientRect(); return { top: r.top, height: r.height, width: r.width }; })) }));
    assert.ok(layout.scroll <= width + 1, `Page overflow at ${width}: ${layout.scroll}`);
    if (width >= 720) for (const [left, right] of layout.align) {
      assert.ok(Math.abs(left.top - right.top) < 1, `Duel top mismatch at ${width}`);
      assert.ok(Math.abs(left.height - right.height) < 1, `Duel height mismatch at ${width}`);
      assert.ok(Math.abs(left.width - right.width) < 1, `Duel width mismatch at ${width}`);
    }
    const tables = await page.locator('.table-scroll table').evaluateAll(nodes => nodes.map(table => ({
      section: table.closest('.entity-section')?.getAttribute('data-section-title'),
      columns: [...table.querySelectorAll('thead th')].map(cell => cell.getBoundingClientRect().width),
      bodyAligned: [...table.querySelectorAll('tbody tr')].every(row => [...row.children].every((cell, index) => {
        const header = table.querySelectorAll('thead th')[index].getBoundingClientRect();
        const body = cell.getBoundingClientRect();
        return Math.abs(header.x - body.x) < 1 && Math.abs(header.width - body.width) < 1;
      })),
    })));
    for (const table of tables) {
      const content = table.columns.slice(1);
      assert.ok(Math.abs(table.columns[0] - 280) < 1, `Title column not fixed at 280px in ${table.section} at ${width}`);
      assert.ok(content.every(column => column > 0 && Math.abs(column - content[0]) < 1), `Unequal content columns in ${table.section} at ${width}`);
      assert.ok(table.bodyAligned, `Header/body column mismatch in ${table.section} at ${width}`);
    }
    assert.ok(tables.length > 0, 'No tables were measured');
    report.widths.push({ width, scrollWidth: layout.scroll, duelsAligned: width >= 720 ? true : 'stacked', tables });
    if ([1600, 390].includes(width)) { const filename = `laopu-${width}.png`; await page.screenshot({ path: path.join(artifactDir, filename) }); report.screenshots.push(filename); }
  }
  await page.setViewportSize({ width: 1600, height: 1050 });
  for (const [name, selector] of [['dashboard', '.module-dashboard'], ['hypotheses', '.module-hypotheses'], ['moat', '.module-moat'], ['profitability', '.module-profitability'], ['risk', '[data-section-title$="风险清单"]'], ['management', '[data-section-title$="管理层与资本配置"]']]) {
    await page.locator(selector).scrollIntoViewIfNeeded();
    const filename = `laopu-${name}.png`; await page.locator(selector).screenshot({ path: path.join(artifactDir, filename) }); report.screenshots.push(filename);
  }
  await page.locator('[data-status-filter="danger"]').click();
  assert.equal(await page.locator('.metric-card:visible').count(), metrics.filter(m => m.status === 'danger').length);
  await page.locator('[data-status-filter="all"]').click();
  assert.equal(await page.locator('.metric-card:visible').count(), metrics.length);
  report.interactions.push('dashboard status filters');
  await page.locator('#entity-search').fill('核心假设');
  await page.locator('#search-results a').filter({ hasText: '核心假设' }).first().click();
  assert.ok(decodeURIComponent(new URL(page.url()).hash).includes('核心假设'));
  assert.equal(await page.locator('#search-results').isVisible(), false);
  await page.locator('#entity-search').fill('not-found-test-314159');
  assert.equal(await page.locator('#search-results').innerText(), '没有匹配的章节');
  await page.locator('#entity-search').fill('');
  report.interactions.push('search match, navigation, empty result');
  await page.locator('.entity-toc a').filter({ hasText: '季度跟踪仪表盘' }).click();
  await page.waitForFunction(() => document.querySelector('.entity-toc a[aria-current]')?.textContent?.includes('季度跟踪仪表盘'));
  report.interactions.push('TOC navigation and active state');
  const citation = page.locator('.entity-content a.citation').first();
  const reference = await citation.getAttribute('href');
  await citation.click();
  assert.equal(new URL(page.url()).hash, reference);
  assert.equal(await page.locator(reference).count(), 1);
  const citationTargets = await page.locator('a.citation').evaluateAll(links => links.map(link => link.getAttribute('href')));
  for (const href of new Set(citationTargets)) assert.equal(await page.locator(href).count(), 1, `Missing or duplicate citation target ${href}`);
  report.interactions.push('source superscript navigation');
  await page.setViewportSize({ width: 390, height: 844 });
  await page.locator('#menu-button').click();
  assert.equal(await page.locator('.app-sidebar').isVisible(), true);
  await page.keyboard.press('Escape');
  assert.equal(await page.locator('.app-sidebar').isVisible(), false);
  report.interactions.push('mobile navigation and Escape');
  const hrefs = await page.locator('.app-sidebar a, .breadcrumbs a').evaluateAll(nodes => [...new Set(nodes.map(n => n.getAttribute('href')).filter(href => href?.startsWith('/')))]);
  for (const href of hrefs) {
    const response = await page.request.get(new URL(href, target).href);
    assert.equal(response.status(), 200, `Broken internal navigation: ${href}`);
  }
  report.interactions.push(`${hrefs.length} internal navigation URLs`);
  assert.deepEqual(errors, []);
  await fs.writeFile(path.join(artifactDir, 'verification.json'), JSON.stringify(report, null, 2));
  console.log(JSON.stringify({ company: doc.name, sourceBlocks: report.sourceBlocks, tableCells: report.tableCells, viewports: report.widths.length, failures: report.strictTextAudit.failures.length, interactions: report.interactions, artifacts: artifactDir }, null, 2));
} finally { await browser.close(); }
