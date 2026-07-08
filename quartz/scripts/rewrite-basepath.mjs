#!/usr/bin/env node
/**
 * Post-build rewrite for GitHub Pages project sites.
 *
 * Quartz v5 emits relative internal links. When the site is served from a
 * subdirectory (e.g. https://annettehub.github.io/ai-investing/), those
 * relative links resolve to the host root and 404.
 *
 * This script:
 *   1. Reads the basePath from cfg.configuration.baseUrl in quartz.config.yaml.
 *   2. Adds data-basepath="<basePath>" to every <body> tag.
 *   3. Rewrites all internal href/src/fetch URLs so they include <basePath>.
 *
 * Run after `npx quartz build` and before deploying the public/ folder.
 */

import { readFile, writeFile, readdir, stat } from "node:fs/promises"
import { join, posix } from "node:path"
import { parse } from "yaml"

const PUBLIC_DIR = join(import.meta.dirname, "..", "public")
const CONFIG_PATH = join(import.meta.dirname, "..", "quartz.config.yaml")

async function parseBasePath() {
  let baseUrl
  try {
    const configText = await readFile(CONFIG_PATH, "utf-8")
    const config = parse(configText)
    baseUrl = config?.configuration?.baseUrl
  } catch (err) {
    console.warn(`Could not read ${CONFIG_PATH}: ${err.message}`)
  }

  if (baseUrl) {
    // baseUrl may be "annettehub.github.io/ai-investing" or a full URL.
    const withScheme = baseUrl.includes("://") ? baseUrl : `https://${baseUrl}`
    try {
      const url = new URL(withScheme)
      if (url.pathname && url.pathname !== "/") {
        return url.pathname.replace(/\/$/, "")
      }
    } catch {
      // fall through to env/default
    }
  }

  const fromEnv = process.env.QUARTZ_BASE_PATH
  if (fromEnv) return fromEnv

  return "/ai-investing"
}

const BASE_PATH = await parseBasePath()
console.log(`[rewrite-basepath] Using base path: ${BASE_PATH}`)

function shouldRewrite(url) {
  if (!url || url.length === 0) return false
  if (url.startsWith("#")) return false
  if (url.startsWith("javascript:")) return false
  if (url.startsWith("mailto:")) return false
  if (url.startsWith("tel:")) return false
  if (url.startsWith("data:")) return false
  if (url.startsWith("//")) return false
  if (/^[a-z][a-z0-9+.-]*:/i.test(url)) return false
  if (url.startsWith(BASE_PATH + "/") || url === BASE_PATH) return false
  return true
}

function rewriteUrl(url, currentDir) {
  if (!shouldRewrite(url)) return url

  let resolved
  if (url.startsWith("/")) {
    resolved = url
  } else {
    resolved = "/" + posix.join(currentDir, url)
  }

  resolved = posix.normalize(resolved)
  if (resolved === "/") resolved = ""
  return BASE_PATH + resolved
}

function addBasePathToBody(html) {
  const bodyTag = html.match(/<body([^>]*)>/i)
  if (!bodyTag) return html

  const attrs = bodyTag[1]
  if (attrs.includes("data-basepath")) return html

  return html.replace(
    /<body([^>]*)>/i,
    `<body$1 data-basepath="${BASE_PATH}">`,
  )
}

function rewriteLinksInHtml(html, currentDir) {
  // Rewrite href="..." and src="..." on any element
  html = html.replace(/\s(href|src)="([^"]*)"/g, (match, attr, url) => {
    const newUrl = rewriteUrl(url, currentDir)
    return ` ${attr}="${newUrl}"`
  })

  // Rewrite inline script fetch("...") URLs (e.g. contentIndex.json)
  html = html.replace(/fetch\("([^"]*)"\)/g, (match, url) => {
    const newUrl = rewriteUrl(url, currentDir)
    return `fetch("${newUrl}")`
  })

  return html
}

async function walk(dir, callback, relative = "") {
  const entries = await readdir(dir, { withFileTypes: true })
  for (const entry of entries) {
    const fullPath = join(dir, entry.name)
    const relPath = relative ? posix.join(relative, entry.name) : entry.name
    if (entry.isDirectory()) {
      await walk(fullPath, callback, relPath)
    } else if (entry.isFile()) {
      await callback(fullPath, relPath)
    }
  }
}

let filesProcessed = 0
let filesModified = 0

await walk(PUBLIC_DIR, async (fullPath, relPath) => {
  if (!relPath.endsWith(".html")) return

  const html = await readFile(fullPath, "utf-8")
  const currentDir = posix.dirname(relPath)
  let newHtml = addBasePathToBody(html)
  newHtml = rewriteLinksInHtml(newHtml, currentDir)

  filesProcessed++
  if (newHtml !== html) {
    await writeFile(fullPath, newHtml, "utf-8")
    filesModified++
  }
})

console.log(
  `[rewrite-basepath] Processed ${filesProcessed} HTML files, modified ${filesModified}.`,
)
