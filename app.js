/**
 * AI Investing Knowledge Base - Site Interactive Features
 */

// ===== Sidebar Toggle =====
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('open');

  // Create or remove overlay
  let overlay = document.querySelector('.sidebar-overlay');
  if (sidebar.classList.contains('open')) {
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'sidebar-overlay';
      overlay.onclick = toggleSidebar;
      document.body.appendChild(overlay);
    }
    overlay.classList.add('active');
  } else if (overlay) {
    overlay.classList.remove('active');
  }
}

// ===== Folder Toggle =====
function toggleFolder(el) {
  const children = el.parentElement.querySelector('.nav-children');
  if (children) {
    children.classList.toggle('collapsed');
    el.classList.toggle('expanded');
    el.textContent = children.classList.contains('collapsed') ? '▶' : '▼';
  }
}

// ===== Auto-expand folders containing active file =====
function expandActivePath() {
  const activeFile = document.querySelector('.nav-file.active');
  if (activeFile) {
    let parent = activeFile.parentElement;
    while (parent) {
      if (parent.classList.contains('nav-children')) {
        parent.classList.remove('collapsed');
        const toggle = parent.parentElement.querySelector('.folder-toggle');
        if (toggle) {
          toggle.classList.add('expanded');
          toggle.textContent = '▼';
        }
      }
      parent = parent.parentElement;
    }
  }
}

// ===== Breadcrumbs =====
function generateBreadcrumbs() {
  const breadcrumbs = document.getElementById('breadcrumbs');
  if (!breadcrumbs) return;

  const path = window.location.pathname;
  const filename = path.split('/').pop().replace('.html', '');

  if (filename === 'index' || filename === '') {
    breadcrumbs.innerHTML = '<span>🏠 首页</span>';
    return;
  }

  // Decode and format filename
  const decoded = decodeURIComponent(filename).replace(/-/g, ' ').replace(/__/g, ' / ');

  breadcrumbs.innerHTML = `
    <a href="index.html">🏠 首页</a>
    <span class="sep">/</span>
    <span>${decoded}</span>
  `;
}

// ===== Search =====
function initSearch() {
  const searchInput = document.getElementById('searchInput');
  const searchResults = document.getElementById('searchResults');

  if (!searchInput || !searchResults || !window.SEARCH_INDEX) return;

  let debounceTimer;

  searchInput.addEventListener('input', (e) => {
    clearTimeout(debounceTimer);
    const query = e.target.value.trim();

    if (query.length < 1) {
      searchResults.classList.remove('active');
      return;
    }

    debounceTimer = setTimeout(() => performSearch(query), 150);
  });

  // Close search when clicking outside
  document.addEventListener('click', (e) => {
    if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
      searchResults.classList.remove('active');
    }
  });

  // Open search on focus if there's text
  searchInput.addEventListener('focus', () => {
    if (searchInput.value.trim().length >= 1) {
      performSearch(searchInput.value.trim());
    }
  });

  // Keyboard shortcut: / to focus search
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput.focus();
    }
    if (e.key === 'Escape') {
      searchResults.classList.remove('active');
      searchInput.blur();
    }
  });
}

function performSearch(query) {
  const searchResults = document.getElementById('searchResults');
  const index = window.SEARCH_INDEX;

  const lowerQuery = query.toLowerCase();
  const results = index.filter(item => {
    return item.title.toLowerCase().includes(lowerQuery) ||
           item.content.toLowerCase().includes(lowerQuery) ||
           item.path.toLowerCase().includes(lowerQuery);
  }).slice(0, 10);

  if (results.length === 0) {
    searchResults.innerHTML = '<div class="search-result-item"><div class="search-result-title">无搜索结果</div></div>';
    searchResults.classList.add('active');
    return;
  }

  searchResults.innerHTML = results.map(item => {
    const preview = item.content.length > 120 ? item.content.substring(0, 120) + '...' : item.content;
    return `
      <a href="${item.url}" class="search-result-item" style="text-decoration:none;display:block;">
        <div class="search-result-title">${highlightText(item.title, query)}</div>
        <div class="search-result-preview">${highlightText(preview, query)}</div>
        <div class="search-result-path">${item.path}</div>
      </a>
    `;
  }).join('');

  searchResults.classList.add('active');
}

function highlightText(text, query) {
  if (!query) return text;
  const regex = new RegExp(`(${escapeRegex(query)})`, 'gi');
  return text.replace(regex, '<mark style="background:rgba(88,166,255,0.3);color:#58a6ff;border-radius:2px;padding:0 2px;">$1</mark>');
}

function escapeRegex(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// ===== Smooth scroll for TOC links =====
function initSmoothScroll() {
  document.querySelectorAll('.toc-sidebar a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
}

// ===== Highlight TOC on scroll =====
function initTocHighlight() {
  const content = document.querySelector('.content');
  const tocLinks = document.querySelectorAll('.toc-sidebar a');
  if (!content || tocLinks.length === 0) return;

  const headings = content.querySelectorAll('h1, h2, h3, h4, h5, h6');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        tocLinks.forEach(link => {
          link.style.color = '';
          link.style.background = '';
          if (link.getAttribute('href') === `#${id}`) {
            link.style.color = '#58a6ff';
            link.style.background = 'rgba(88,166,255,0.1)';
          }
        });
      }
    });
  }, { root: content, threshold: 0 });

  headings.forEach(h => observer.observe(h));
}

// ===== Initialize =====
document.addEventListener('DOMContentLoaded', () => {
  expandActivePath();
  generateBreadcrumbs();
  initSearch();
  initSmoothScroll();
  initTocHighlight();
});
