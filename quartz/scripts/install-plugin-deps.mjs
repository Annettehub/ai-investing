#!/usr/bin/env node
/**
 * Install npm dependencies for all Quartz community plugins.
 * This is needed because npx quartz plugin install only fetches source code,
 * but doesn't install each plugin's npm dependencies.
 * Run this before npx quartz build in CI environments.
 */
import { readdirSync, existsSync } from "node:fs"
import { join } from "node:path"
import { execSync } from "node:child_process"

const pluginsDir = join(import.meta.dirname, "..", ".quartz", "plugins")

if (!existsSync(pluginsDir)) {
  console.log("No .quartz/plugins directory found, skipping plugin dependency install.")
  process.exit(0)
}

const entries = readdirSync(pluginsDir, { withFileTypes: true })
const pluginDirs = entries.filter((e) => e.isDirectory()).map((e) => join(pluginsDir, e.name))

let successCount = 0
let failCount = 0

for (const dir of pluginDirs) {
  const pkgJson = join(dir, "package.json")
  if (!existsSync(pkgJson)) continue

  // Skip if node_modules already exists (already installed)
  if (existsSync(join(dir, "node_modules"))) {
    successCount++
    continue
  }

  const name = dir.split(/[/\\]/).pop()
  console.log(`Installing dependencies for plugin: ${name}...`)

  try {
    execSync("npm install --no-audit --no-fund --prefer-offline", {
      cwd: dir,
      stdio: "pipe",
      timeout: 120_000,
    })
    console.log(`  ✓ ${name} done`)
    successCount++
  } catch (err) {
    console.warn(`  ⚠ ${name} npm install failed (may still work): ${err.message}`)
    failCount++
  }
}

console.log(`\nPlugin dependency install: ${successCount} OK, ${failCount} failed`)
