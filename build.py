"""Baut index.html (für GitHub Pages) aus src/app.html.

src/app.html ist die Quelle (ohne <html>/<head>-Gerüst, so wie Claude-Artifacts sie erwarten).
Aufruf: python3 build.py
"""
from pathlib import Path

root = Path(__file__).parent
body = (root / "src" / "app.html").read_text(encoding="utf-8")
head = (
    '<!doctype html><html lang="de"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<meta name="theme-color" content="#1e4d78">'
    "<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);"
    "padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}"
    "img{max-width:100%}[hidden]{display:none!important}</style></head><body>\n"
)
(root / "index.html").write_text(head + body + "\n</body></html>\n", encoding="utf-8")
print("index.html geschrieben")
