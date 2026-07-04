#!/usr/bin/env python3
"""
Static site generator for ai-investing knowledge base.
Scans markdown files and generates a beautiful static website.
"""

import os
import re
import json
import html as html_module
from pathlib import Path
from datetime import datetime
import markdown
from markdown.extensions import fenced_code, tables, toc

# Configuration
REPO_ROOT = Path(".")
OUTPUT_DIR = Path("site")
EXCLUDE_DIRS = {".git", ".github", ".obsidian", "site", "scripts", "processed", "tools", "__pycache__"}
EXCLUDE_FILES = {"README.md"}  # Will be handled specially

class WikiLinkExtension(markdown.Extension):
    """Convert Obsidian wiki links [[Page]] or [[Page|Text]] to HTML links."""
    def extendMarkdown(self, md):
        md.inlinePatterns.register(WikiLinkPattern(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'), 'wikilink', 175)

class WikiLinkPattern(markdown.inlinepatterns.InlineProcessor):
    def handleMatch(self, m, data):
        target = m.group(1).strip()
        text = m.group(2).strip() if m.group(2) else target
        # Convert to URL-friendly slug
        url = self.make_url(target)
        el = markdown.util.etree.Element('a')
        el.set('href', url)
        el.set('class', 'wiki-link')
        el.text = text
        return el, m.start(0), m.end(0)

    def make_url(self, target):
        # Remove .md extension if present
        if target.endswith('.md'):
            target = target[:-3]
        # Convert to slug
        slug = target.lower().replace(' ', '-').replace('_', '-')
        # For internal links, we'll handle routing in JS
        return f'#{slug}'

def get_markdown_files():
    """Scan repository for all markdown files."""
    files = []
    for root, dirs, filenames in os.walk(REPO_ROOT):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]

        for filename in filenames:
            if filename.endswith('.md'):
                full_path = Path(root) / filename
                rel_path = full_path.relative_to(REPO_ROOT)
                # Skip root README, handle separately
                if str(rel_path) == "README.md":
                    continue
                files.append(rel_path)

    return sorted(files)

def build_file_tree(files):
    """Build a nested tree structure from file paths."""
    tree = {}
    for f in files:
        parts = f.parts
        current = tree
        for part in parts[:-1]:
            if part not in current:
                current[part] = {"_files": []}
            current = current[part]
        current.setdefault("_files", []).append(parts[-1])
    return tree

def slugify_path(rel_path):
    """Convert a relative path to a URL-safe slug."""
    return str(rel_path).replace('/', '--').replace('\\', '--').replace('.md', '.html')

def path_to_title(rel_path):
    """Convert a file path to a display title."""
    name = rel_path.stem
    # Replace hyphens and underscores with spaces
    name = name.replace('-', ' ').replace('_', ' ')
    # Handle Chinese characters properly
    return name

def find_matching_file(target, all_files):
    """Find a file matching the wiki link target."""
    target_lower = target.lower().replace('.md', '')
    candidates = []
    for f in all_files:
        stem = f.stem.lower()
        name = str(f).lower().replace('.md', '')
        if stem == target_lower or name == target_lower:
            candidates.append(f)
        elif target_lower in stem or target_lower in name:
            candidates.append(f)

    if candidates:
        # Prefer exact match, then shortest path
        return min(candidates, key=lambda x: len(str(x)))
    return None

def convert_wiki_links(content, all_files, current_file):
    """Convert Obsidian wiki links to proper relative HTML links."""
    def replace_link(match):
        target = match.group(1).strip()
        text = match.group(2).strip() if match.group(2) else target

        # Find matching file
        matched = find_matching_file(target, all_files)
        if matched:
            # Calculate relative path from current file to target
            current_dir = current_file.parent if current_file else Path('.')
            try:
                rel_link = matched.with_suffix('.html')
                link_str = str(rel_link).replace('/', '--').replace('\\', '--')
                return f'<a href="{link_str}" class="wiki-link">{text}</a>'
            except:
                pass

        # Fallback: return as plain text with link style
        return f'<a href="#" class="wiki-link broken">{text}</a>'

    pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'
    return re.sub(pattern, replace_link, content)

def markdown_to_html(content, all_files, current_file):
    """Convert markdown content to HTML."""
    # First convert wiki links to HTML links (before markdown processing)
    content = convert_wiki_links(content, all_files, current_file)

    # Configure markdown parser
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'toc',
        'nl2br',
        'meta',
        WikiLinkExtension(),
    ])

    html = md.convert(content)
    toc_html = md.toc if hasattr(md, 'toc') else ''

    return html, toc_html

def render_sidebar(tree, all_files, current_file=None, prefix=""):
    """Render the sidebar navigation tree as HTML."""
    html = '<ul class="nav-tree">'

    # First render directories
    for name in sorted(tree.keys()):
        if name == '_files':
            continue
        subtree = tree[name]
        has_children = bool(subtree.get('_files') or any(k != '_files' for k in subtree.keys()))

        display_name = name.replace('-', ' ').replace('_', ' ')
        html += f'<li class="nav-folder">'
        html += f'<span class="folder-toggle" onclick="toggleFolder(this)">▶</span>'
        html += f'<span class="folder-name">{display_name}</span>'
        html += f'<ul class="nav-children collapsed">'
        html += render_sidebar(subtree, all_files, current_file, prefix + name + '/')
        html += '</ul></li>'

    # Then render files
    for filename in sorted(tree.get('_files', [])):
        rel_path = Path(prefix + filename)
        slug = slugify_path(rel_path)
        title = path_to_title(rel_path)
        active_class = 'active' if current_file and str(current_file) == str(rel_path) else ''
        html += f'<li class="nav-file {active_class}"><a href="{slug}">{title}</a></li>'

    html += '</ul>'
    return html

def generate_search_index(all_files):
    """Generate a JSON search index from all markdown files."""
    index = []
    for rel_path in all_files:
        try:
            content = (REPO_ROOT / rel_path).read_text(encoding='utf-8')
            # Strip markdown syntax for search content
            plain = re.sub(r'[#*`\[\]\(\)|>]', ' ', content)
            plain = re.sub(r'\s+', ' ', plain).strip()[:2000]  # Limit length

            index.append({
                'path': str(rel_path),
                'url': slugify_path(rel_path),
                'title': path_to_title(rel_path),
                'content': plain,
            })
        except Exception as e:
            print(f"Warning: Could not index {rel_path}: {e}")

    return index

def build_page_template(title, content_html, toc_html, sidebar_html, search_index_json, search_index):
    """Build a complete HTML page."""
    template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__TITLE__ - AI投研知识库</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="layout">
        <!-- Sidebar -->
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h1><a href="index.html">📚 AI投研知识库</a></h1>
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="搜索知识库..." autocomplete="off">
                    <div id="searchResults" class="search-results"></div>
                </div>
            </div>
            <nav class="sidebar-nav">
                __SIDEBAR__
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main">
            <div class="content-header">
                <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                <nav class="breadcrumbs" id="breadcrumbs"></nav>
            </div>
            <article class="content">
                __CONTENT__
            </article>
            <footer class="footer">
                <p>最后更新: __BUILD_TIME__ | 共 __PAGE_COUNT__ 篇文档</p>
            </footer>
        </main>

        <!-- TOC Sidebar -->
        <aside class="toc-sidebar" id="tocSidebar">
            <div class="toc-title">📑 目录</div>
            __TOC__
        </aside>
    </div>

    <script>
        window.SEARCH_INDEX = __SEARCH_INDEX__;
    </script>
    <script src="app.js"></script>
</body>
</html>
'''
    return template.replace('__TITLE__', title).replace('__CONTENT__', content_html).replace('__TOC__', toc_html).replace('__SIDEBAR__', sidebar_html).replace('__SEARCH_INDEX__', search_index_json).replace('__BUILD_TIME__', datetime.now().strftime('%Y-%m-%d %H:%M')).replace('__PAGE_COUNT__', str(len(search_index)))

def main():
    print("🔍 Scanning markdown files...")
    all_files = get_markdown_files()
    print(f"📄 Found {len(all_files)} markdown files")

    # Build file tree
    tree = build_file_tree(all_files)

    # Generate search index
    print("🔎 Building search index...")
    search_index = generate_search_index(all_files)
    search_index_json = json.dumps(search_index, ensure_ascii=False)

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Generate pages for each markdown file
    print("📝 Generating pages...")
    for rel_path in all_files:
        try:
            content = (REPO_ROOT / rel_path).read_text(encoding='utf-8')
            content_html, toc_html = markdown_to_html(content, all_files, rel_path)

            # Generate sidebar with active state
            sidebar_html = render_sidebar(tree, all_files, rel_path)

            title = path_to_title(rel_path)
            page_html = build_page_template(title, content_html, toc_html, sidebar_html, search_index_json, search_index)

            output_path = OUTPUT_DIR / slugify_path(rel_path)
            output_path.write_text(page_html, encoding='utf-8')
            print(f"  ✓ {rel_path}")
        except Exception as e:
            print(f"  ✗ {rel_path}: {e}")

    # Generate index page from README.md or 02-kb/index.md
    print("🏠 Generating index page...")
    index_content = ""
    index_title = "首页"

    # Try 02-kb/index.md first (it has the main index)
    kb_index = REPO_ROOT / "02-kb" / "index.md"
    root_readme = REPO_ROOT / "README.md"

    if kb_index.exists():
        index_content = kb_index.read_text(encoding='utf-8')
        index_title = "知识库总索引"
    elif root_readme.exists():
        index_content = root_readme.read_text(encoding='utf-8')

    # Add a nice header if using the kb index
    if kb_index.exists():
        header = "# 🏠 AI投研知识库\n\n> 基于 GitHub 的自动化知识管理系统\n\n"
        index_content = header + index_content

    if index_content:
        content_html, toc_html = markdown_to_html(index_content, all_files, None)
        sidebar_html = render_sidebar(tree, all_files, None)
        page_html = build_page_template(index_title, content_html, toc_html, sidebar_html, search_index_json, search_index)
        (OUTPUT_DIR / "index.html").write_text(page_html, encoding='utf-8')
    else:
        # Fallback index
        fallback = "# AI投研知识库\\n\\n欢迎浏览知识库。"
        content_html, _ = markdown_to_html(fallback, all_files, None)
        sidebar_html = render_sidebar(tree, all_files, None)
        page_html = build_page_template("首页", content_html, "", sidebar_html, search_index_json, search_index)
        (OUTPUT_DIR / "index.html").write_text(page_html, encoding='utf-8')

    # Copy static files
    print("📦 Copying static assets...")
    static_dir = Path(__file__).parent / "static"
    if static_dir.exists():
        for f in static_dir.iterdir():
            if f.is_file():
                import shutil
                shutil.copy(f, OUTPUT_DIR / f.name)

    print(f"\\n✅ Site built successfully in '{OUTPUT_DIR}/'")
    print(f"🌐 Open '{OUTPUT_DIR}/index.html' to preview")

if __name__ == "__main__":
    main()
