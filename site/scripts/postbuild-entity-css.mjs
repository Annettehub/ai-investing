// 实体卡专属样式后期注入脚本
// build 后跑：在 dist HTML 的 </head> 前注入 entity.css link，
// 位置精确在 Starlight 全局资源之后，确保级联覆盖 rose-pine 主题。

import fs from "node:fs";
import path from "node:path";

const ENTITY_CSS_HREF = "/ai-investing/styles/entity.css";
// 实验期只对老铺黄金页面生效（后续要全部实体卡生效，把这里改成实体卡路径列表）
// 用完整路径段（前后加斜杠）避免误匹配 sidebar 中的子串
const ENTITY_PAGE_PATHS = [
  "/kb/entities/06181-301dfca8/",
];

function walk(dir, callback) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === ".prerender" || entry.name === "_astro" || entry.name === ".vite") continue;
      walk(full, callback);
    } else {
      callback(full);
    }
  }
}

const ROOT = process.cwd();
const DIST = path.join(ROOT, "dist");
if (!fs.existsSync(DIST)) {
  console.error("[postbuild-entity-css] dist/ 不存在，跳过");
  process.exit(0);
}

let count = 0;
walk(DIST, (file) => {
  if (!file.endsWith(".html")) return;
  const content = fs.readFileSync(file, "utf-8");
  // 仅处理实体卡页面：通过 canonical href 路径段精确匹配（避免被 sidebar 链接误匹配）
  const canonicalMatch = content.match(/<link\s+rel="canonical"\s+href="([^"]+)"/);
  if (!canonicalMatch) return;
  let canonicalPath = new URL(canonicalMatch[1]).pathname;
  // 去掉 base 前缀（/ai-investing/），便于只比较子路径
  canonicalPath = canonicalPath.replace(/^\/ai-investing/, "");
  if (!ENTITY_PAGE_PATHS.some((p) => canonicalPath === p)) return;
  // 已注入过则跳过
  if (content.includes(ENTITY_CSS_HREF)) return;

  const injected = content.replace(
    "</head>",
    `    <link rel="stylesheet" href="${ENTITY_CSS_HREF}">\n  </head>`,
  );
  if (injected === content) return;
  fs.writeFileSync(file, injected);
  count += 1;
  console.log(`[postbuild-entity-css] 注入: ${path.relative(DIST, file)}`);
});

console.log(`[postbuild-entity-css] 共注入 ${count} 个实体卡页面`);
