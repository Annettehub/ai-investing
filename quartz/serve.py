"""
Static file server that serves .html files without requiring .html extension.
e.g. /foo/bar -> looks for /foo/bar.html if /foo/bar doesn't exist
"""
import http.server
import os

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".html": "text/html",
    }

    # Strip the GitHub Pages project-site base path so the rewritten links
    # can be previewed locally at the repository root.
    base_path = "/ai-investing"

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def translate_path(self, path):
        import urllib.parse
        import posixpath

        # Decode percent-encoded path
        path = urllib.parse.unquote(path)
        path = posixpath.normpath(path)

        # Strip the base path so /ai-investing/foo/bar -> /foo/bar
        if path.startswith(self.base_path):
            path = path[len(self.base_path):]

        words = path.split("/")
        words = [w for w in words if w]

        base = os.getcwd()
        for word in words:
            if os.path.dirname(word) or word in (os.curdir, os.pardir):
                continue
            base = os.path.join(base, word)

        # If path doesn't exist, try adding .html
        if not os.path.exists(base):
            html_path = base + ".html"
            if os.path.exists(html_path):
                return html_path

        return base

    def log_message(self, format, *args):
        pass  # silence logs

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    with http.server.HTTPServer(("", port), QuietHandler) as httpd:
        print(f"Serving at http://localhost:{port}", flush=True)
        httpd.serve_forever()
