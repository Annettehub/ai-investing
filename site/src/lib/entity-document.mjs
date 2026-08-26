import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import remarkRehype from 'remark-rehype';
import rehypeStringify from 'rehype-stringify';
import { toString } from 'mdast-util-to-string';
import GithubSlugger from 'github-slugger';

const parser = unified().use(remarkParse).use(remarkGfm);
const renderer = unified().use(remarkRehype).use(rehypeStringify);
export const plain = (node) => toString(node);
export const html = (nodes) => String(renderer.stringify(renderer.runSync({ type: 'root', children: Array.isArray(nodes) ? nodes : [nodes] })));
const inline = (node) => html({ type: 'paragraph', children: node.children }).replace(/^<p>|<\/p>$/g, '');

export function moduleFor(title) {
  if (/交叉检查/.test(title)) return 'crosscheck';
  if (/业务划分|两个腾讯/.test(title)) return 'business';
  if (/护城河分层/.test(title)) return 'moat';
  if (/竞争边界/.test(title)) return 'competition';
  if (/季度跟踪仪表盘/.test(title)) return 'dashboard';
  if (/核心假设/.test(title)) return 'hypotheses';
  if (/当前估值/.test(title)) return 'valuation';
  if (/分部收入/.test(title)) return 'revenue';
  if (/盈利能力/.test(title)) return 'profitability';
  if (/现金流与资本配置/.test(title)) return 'cashflow';
  if (/来源与参考|来源与关联|数据来源/.test(title)) return 'references';
  return 'prose';
}

// Split phrasing nodes without losing emphasis, punctuation, or link markup.
function splitInline(nodes, offset) {
  const left = [], right = [];
  for (const node of nodes) {
    const length = plain(node).length;
    if (offset >= length) { left.push(node); offset -= length; }
    else if (offset <= 0) right.push(node);
    else if (node.type === 'text') {
      left.push({ ...node, value: node.value.slice(0, offset) });
      right.push({ ...node, value: node.value.slice(offset) });
      offset = 0;
    } else if (node.children) {
      const [before, after] = splitInline(node.children, offset);
      left.push({ ...node, children: before });
      right.push({ ...node, children: after });
      offset = 0;
    } else return null;
  }
  return [left, right];
}

function duel(node) {
  if (node.type !== 'blockquote' || !plain(node).startsWith('多空张力') || node.children.some(n => n.type !== 'paragraph')) return null;
  const children = node.children.flatMap((n, i) => i ? [{ type: 'text', value: '\n\n' }, ...n.children] : n.children);
  const text = plain({ children });
  const bull = text.indexOf('多方'), bear = text.indexOf('空方');
  if (bull < 0 || bear < 0) return null;
  const first = Math.min(bull, bear), second = Math.max(bull, bear);
  const leadSplit = splitInline(children, first);
  if (!leadSplit) return null;
  const sideSplit = splitInline(leadSplit[1], second - first);
  if (!sideSplit) return null;
  const render = (parts) => html({ type: 'paragraph', children: parts });
  return { kind: 'duel', label: render(leadSplit[0]), bull: render(sideSplit[bull < bear ? 0 : 1]), bear: render(sideSplit[bull < bear ? 1 : 0]) };
}

export function statusOf(text) {
  if (text.includes('🔴')) return 'danger';
  if (text.includes('🟡')) return 'watch';
  if (text.includes('🟢')) return 'healthy';
  return 'neutral';
}

function tableData(node) {
  return node.children.map(row => row.children.map(cell => ({ text: plain(cell), html: inline(cell), node: cell })));
}

export function tableColumnWidths({ header }) {
  const count = header.length;
  if (count <= 1) return count ? ['100%'] : [];
  return ['280px', ...Array(count - 1).fill(`calc((100% - 280px) / ${count - 1})`)];
}

function primaryValue(cell) {
  const strong = cell.node.children.find(n => n.type === 'strong' && /\d/.test(plain(n)));
  if (strong) return plain(strong);
  return cell.text.match(/[+−-]?\d+(?:\.\d+)?(?:%|万|亿|天)/)?.[0] || '';
}

function chartFor(table, kind) {
  const { header, rows } = table;
  let selected = [], columns = [], title = '', unit = '', note = '';
  if (kind === 'revenue' && header.length === 5) {
    selected = rows.filter(r => !/合计|总计/.test(r[0].text)); columns = [1, 2];
    title = '年度收入结构'; unit = '亿元'; note = '年度口径；数据来自下方原表。';
  } else if (kind === 'revenue' && header.length === 4 && /收入/.test(header[1].text)) {
    selected = rows.filter(r => !/合计|总计/.test(r[0].text)); columns = [1];
    title = '年度收入结构'; unit = '亿元'; note = `${header[1].text}；数据来自下方原表。`;
  } else if (kind === 'profitability' && header.length === 5) {
    selected = rows.filter(r => ['毛利率', '经调整净利率'].includes(r[0].text)); columns = [1, 2, 3];
    title = '利润率变化'; unit = '%'; note = '2024、2025 为全年，2026H1 为半年度；比例指标。';
  } else if (kind === 'cashflow' && header.length === 5) {
    selected = rows.filter(r => r[0].text === '经营现金流'); columns = [1, 2, 3];
    title = '经营现金流'; unit = '亿元'; note = '全年与半年度分别展示，未作年化，不直接比较增速。';
  } else return null;
  const series = selected.map((row, index) => ({ label: row[0].text, color: index ? 'secondary' : 'primary', points: columns.map(col => {
    const raw = row[col].text;
    // Never turn ranges, missing values, or estimates into precise chart points.
    const match = raw.match(/^([+-]?\d[\d,]*(?:\.\d+)?)\s*(亿(?:元)?|%)$/);
    return { label: header[col].text, value: match ? Number(match[1].replaceAll(',', '')) : null, raw };
  }) }));
  if (!series.length || series.some(s => s.points.some(p => p.value === null))) return null;
  const max = Math.max(...series.flatMap(s => s.points.map(p => Math.abs(p.value))));
  return { title, unit, note, series, max, signed: series.some(s => s.points.some(p => p.value < 0)) };
}

function makeBlock(node, section, id) {
  const base = { id, node, sourceText: plain(node), sourceHtml: html(node), kind: 'prose' };
  const comparison = duel(node);
  if (comparison) return { ...base, ...comparison };
  if (node.type === 'table') {
    const [header, ...rows] = tableData(node);
    const kind = section.module === 'moat' && header.length === 4 ? 'moat' : section.module === 'dashboard' && header.length === 5 ? 'dashboard' : 'table';
    const table = { ...base, kind, header, rows, sectionKind: section.module, align: node.align };
    if (kind === 'dashboard') table.metrics = rows.map(row => ({ row, headline: primaryValue(row[2]), status: statusOf(row[4].text) }));
    table.chart = chartFor(table, section.module);
    return table;
  }
  if (node.type === 'list' && node.ordered && section.module === 'hypotheses') {
    return { ...base, kind: 'hypotheses', cards: node.children.map((item, index) => {
      const first = item.children[0];
      const splitTitle = first.type === 'paragraph' && first.children[0]?.type === 'strong' && first.children.length > 1;
      const title = splitTitle ? { ...first, children: first.children.slice(0, 1) } : first;
      const body = splitTitle ? [{ ...first, children: first.children.slice(1) }, ...item.children.slice(1)] : item.children.slice(1);
      return { title: html(title), body: html(body), number: (node.start || 1) + index };
    }) };
  }
  if (node.type === 'blockquote') return { ...base, kind: 'note' };
  return base;
}

export function parseEntity(markdown) {
  const tree = parser.parse(markdown);
  const referenceIds = new Set();
  const referenceLabel = (id, value) => {
    referenceIds.add(id);
    return { type: 'strong', children: [{ type: 'text', value }], data: { hName: 'span', hProperties: { id: `reference-${id}`, className: ['reference-label'] } } };
  };
  function markReferenceLines(node) {
    if (!node.children || ['link', 'code'].includes(node.type)) return;
    node.children = node.children.flatMap(child => {
      if (child.type === 'inlineCode' && /^\[\d+[a-z]?\]$/.test(child.value)) return [referenceLabel(child.value.slice(1, -1), child.value)];
      if (child.type !== 'text') { markReferenceLines(child); return [child]; }
      const parts = []; let start = 0;
      for (const match of child.value.matchAll(/(^|\n)(\[(\d+[a-z]?)\])(?=\s)/g)) {
        const offset = match.index + match[1].length;
        if (offset > start) parts.push({ type: 'text', value: child.value.slice(start, offset) });
        parts.push(referenceLabel(match[3], match[2]));
        start = offset + match[2].length;
      }
      if (!start) return [child];
      if (start < child.value.length) parts.push({ type: 'text', value: child.value.slice(start) });
      return parts;
    });
  }
  let inReferences = false;
  for (const node of tree.children) {
    if (node.type === 'heading') inReferences = moduleFor(plain(node)) === 'references';
    if (inReferences && node.type !== 'heading') markReferenceLines(node);
  }
  function linkCitations(node) {
    if (!node.children || ['link', 'code', 'inlineCode'].includes(node.type) || node.data?.hProperties?.className?.includes('reference-label')) return;
    node.children = node.children.flatMap(child => {
      if (child.type !== 'text') { linkCitations(child); return [child]; }
      const output = []; let start = 0;
      for (const match of child.value.matchAll(/\[(\d+[a-z]?)\]|⁽([⁰¹²³⁴⁵⁶⁷⁸⁹]+)⁾/g)) {
        const id = match[1] || [...match[2]].map(char => '⁰¹²³⁴⁵⁶⁷⁸⁹'.indexOf(char)).join('');
        if (!referenceIds.has(id)) continue;
        if (match.index > start) output.push({ type: 'text', value: child.value.slice(start, match.index) });
        output.push({ type: 'link', url: `#reference-${id}`, children: [{ type: 'text', value: match[0] }], data: { hProperties: { className: ['citation', ...(match[2] ? ['citation--unicode'] : [])], ariaLabel: `来源 ${id}` } } });
        start = match.index + match[0].length;
      }
      if (!start) return [child];
      if (start < child.value.length) output.push({ type: 'text', value: child.value.slice(start) });
      return output;
    });
  }
  linkCitations(tree);
  const slugger = new GithubSlugger();
  const intro = { id: 'document-intro', title: '', module: 'intro', depth: 1, blocks: [] };
  const sections = [];
  let current = intro, title = '', blockIndex = 0;
  for (const node of tree.children) {
    if (node.type === 'heading' && node.depth === 1 && !title) { title = plain(node); continue; }
    if (node.type === 'heading' && [2, 3].includes(node.depth)) {
      const text = plain(node), number = text.match(/^\d+(?:\.\d+)?\.?/)?.[0] || '';
      current = { id: slugger.slug(text), title: text, label: text.slice(number.length).trimStart(), number, depth: node.depth, module: moduleFor(text), blocks: [] };
      sections.push(current);
    } else {
      current.blocks.push(makeBlock(node, current, `source-${++blockIndex}`));
    }
  }
  const allBlocks = [intro, ...sections].flatMap(s => s.blocks);
  for (const section of sections) {
    if (section.module !== 'competition') continue;
    section.competitors = [];
    for (const block of section.blocks) {
      if (block.node.type === 'paragraph' && /^(核心竞争对手|次要竞争对手|潜在颠覆者)/.test(block.sourceText)) section.competitors.push([]);
      if (section.competitors.length && block.node.type !== 'thematicBreak') section.competitors.at(-1).push(block);
    }
    if (section.competitors.flat().length !== section.blocks.filter(b => b.node.type !== 'thematicBreak').length) section.competitors = null;
  }
  const valuation = sections.find(s => s.module === 'valuation');
  const valuationTable = valuation?.blocks.find(b => b.kind === 'table');
  const highlights = ['总市值', 'PE-TTM', '2026E PE', '股息率TTM', '股价', '市净率'].flatMap(key => {
    const row = valuationTable?.rows.find(r => r[0].text === key);
    if (!row) return [];
    const value = row[1].text;
    const headline = value.match(/^约?\s*\d[\d,]*(?:\.\d+)?(?:\s*[-–]\s*\d+(?:\.\d+)?)?\s*(?:万亿港元|亿港元|港元|倍|%)/)?.[0] || value;
    const qualifier = value.replace(headline, '').replace(/[\[\]（）:：]/g, '').trim();
    return [{ label: row[0].text, value, headline, qualifier, source: row[2].text, href: `#${valuation.id}` }];
  }).slice(0, 4);
  const quote = intro.blocks.find(b => b.node.type === 'blockquote')?.sourceText || '';
  const code = title.match(/[0-9]{4,5}\.HK/)?.[0] || '';
  const name = title.replace(code, '').split(/[—–]/)[0].trim();
  return { title, code, name, intro, sections, allBlocks, highlights, updated: quote.match(/最后更新:\s*(\d{4}-\d{2}-\d{2})/)?.[1] || '', status: quote.match(/状态:\s*([^\n]+)/)?.[1] || '', tree };
}
