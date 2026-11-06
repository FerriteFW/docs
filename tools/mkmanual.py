#!/usr/bin/env python3
"""Build the readable Ferrite manual (docs/manual.html) from the chapter files in docs/manual/.

    python3 docs/tools/mkmanual.py            # writes docs/manual.html
    python3 docs/tools/mkmanual.py --open     # and opens it

needs: pip install markdown
The Markdown file is the source; never edit the HTML. Images are embedded, so the
HTML file stands alone. Blockquotes that start with "**Spec" become spec boxes, and
rule IDs such as **HOME-4** get anchors (manual.html#HOME-4).
"""
import base64, html, mimetypes, pathlib, re, subprocess, sys
import markdown

DOCS = pathlib.Path(__file__).resolve().parent.parent
ROOT = DOCS.parent
SRC = DOCS / "manual.md"        # the index; the book itself is the chapter files in docs/manual/
CHAPTERS = DOCS / "manual"
CHAPTER_FILE = re.compile(r"^(?:\d\d[a-z]?|[A-Z])-.*\.md$")


def chapter_files():
    """The chapter files in book order (00-front, 01.., 20, 20a, .., 38, A..I); RULES.md is not one."""
    return sorted(f for f in CHAPTERS.iterdir() if CHAPTER_FILE.match(f.name))


def read_book():
    return "".join(f.read_text() for f in chapter_files())
OUT = DOCS / "manual.html"

CSS = """
:root{--bg:#fbfaf7;--fg:#1b1d21;--muted:#5d6470;--line:#e2ded6;--card:#ffffff;--accent:#c2410c;
--spec:#f1f6ff;--specline:#3b6fd6;--code:#f2efe8;--side:#f4f1ea}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#121417;--fg:#e8e6e1;--muted:#9aa3ae;
--line:#2a2f36;--card:#181b20;--accent:#f08a4b;--spec:#15202f;--specline:#4da3ff;--code:#1e2228;--side:#15181c}}
:root[data-theme=dark]{--bg:#121417;--fg:#e8e6e1;--muted:#9aa3ae;--line:#2a2f36;--card:#181b20;--accent:#f08a4b;
--spec:#15202f;--specline:#4da3ff;--code:#1e2228;--side:#15181c}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:16px}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 "JetBrains Mono",ui-monospace,Menlo,monospace;}
.wrap{display:flex;min-height:100vh}
nav{position:sticky;top:0;align-self:flex-start;height:100vh;overflow:auto;width:290px;flex-shrink:0;
background:var(--side);border-right:1px solid var(--line);padding:20px 16px;font-size:13px;line-height:1.5}
nav .brand{font-weight:700;font-size:18px;margin-bottom:2px}
nav .sub{color:var(--muted);margin-bottom:16px}
nav a{color:var(--fg);text-decoration:none;display:block;padding:2px 6px;border-radius:4px}
nav a:hover{background:var(--line)}
nav .h2{margin-top:10px;font-weight:700}
nav .h3{padding-left:18px;color:var(--muted)}
main{flex:1;min-width:0;max-width:980px;padding:32px 40px 80px}
h1{font-size:30px;margin:0 0 4px}
h2{font-size:24px;margin:56px 0 12px;padding-top:12px;border-top:2px solid var(--line)}
h3{font-size:18px;margin:32px 0 8px;color:var(--accent)}
a{color:var(--specline)}
p,li{max-width:78ch}
code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:.92em}
table{border-collapse:collapse;margin:12px 0 20px;width:100%;font-size:14px;background:var(--card)}
th,td{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}
th{background:var(--code)}
img{max-width:100%;height:auto;border-radius:8px;display:block}
td img{max-width:240px;margin:0 auto;cursor:zoom-in}
td img.wide{max-width:100%}
main img{cursor:zoom-in}
.lb{position:fixed;inset:0;background:rgba(0,0,0,.85);display:none;align-items:center;justify-content:center;z-index:10;cursor:zoom-out;padding:24px}
.lb.on{display:flex}
.lb img{max-width:100%;max-height:100%;width:auto;height:auto;border-radius:6px;box-shadow:0 8px 40px rgba(0,0,0,.6);cursor:zoom-out}
.lb .cap{position:fixed;bottom:12px;left:0;right:0;text-align:center;color:#ddd;font-size:13px}
table.shots{background:none;border:none}
table.shots td,table.shots th{border:none;text-align:center;color:var(--muted);font-size:13px;background:none}
blockquote{margin:20px 0;padding:12px 18px;border-left:4px solid var(--line);background:var(--card);border-radius:0 8px 8px 0}
blockquote.spec{background:var(--spec);border-left-color:var(--specline)}
blockquote.spec>p:first-child strong{color:var(--specline);font-size:15px;letter-spacing:.02em}
blockquote.spec li{margin:6px 0}
.rule{font-weight:700;color:var(--specline);scroll-margin-top:16px}
.todo{color:var(--muted)}
.theme{float:right;font:inherit;font-size:12px;background:var(--card);color:var(--fg);border:1px solid var(--line);
border-radius:6px;padding:3px 8px;cursor:pointer}
hr{border:none;border-top:1px solid var(--line);margin:28px 0}
@media (max-width:900px){.wrap{display:block}nav{position:static;width:auto;height:auto;border-right:none;
border-bottom:1px solid var(--line)}main{padding:20px 16px 60px}}
@media print{nav,.theme{display:none}main{max-width:none;padding:0}h2{break-before:page}
blockquote,table,img{break-inside:avoid}body{background:#fff;color:#000}}
footer.licence{margin:48px 0 24px;padding-top:14px;border-top:1px solid var(--line, #2a2f36);font-size:12px;opacity:.75}
"""

JS = """
(function(){var lb=document.createElement('div');lb.className='lb';lb.innerHTML='<img alt=""><div class="cap"></div>';
document.body.appendChild(lb);var im=lb.querySelector('img'),cap=lb.querySelector('.cap');
function close(){lb.classList.remove('on')}
lb.addEventListener('click',close);document.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
document.querySelectorAll('main img').forEach(function(i){
 if(i.naturalWidth>i.naturalHeight*1.2)i.classList.add('wide');
 i.addEventListener('load',function(){if(i.naturalWidth>i.naturalHeight*1.2)i.classList.add('wide')});
 i.addEventListener('click',function(){im.src=i.src;cap.textContent=i.alt+'  ·  click or Esc to close';lb.classList.add('on')})});})();
(function(){var b=document.querySelector('.theme');if(!b)return;
function set(t){document.documentElement.setAttribute('data-theme',t);try{localStorage.setItem('ferrite-manual-theme',t)}catch(e){}}
try{var t=localStorage.getItem('ferrite-manual-theme');if(t)document.documentElement.setAttribute('data-theme',t)}catch(e){}
b.onclick=function(){var cur=document.documentElement.getAttribute('data-theme')||
(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');set(cur==='dark'?'light':'dark')}})();
"""


def embed_images(text, base):
    def sub(m):
        src = m.group(2)
        p = (base / src).resolve()
        if src.startswith(("http:", "https:", "data:")) or not p.exists():
            return m.group(0)
        mime = mimetypes.guess_type(p.name)[0] or "image/png"
        data = base64.b64encode(p.read_bytes()).decode()
        return f'{m.group(1)}data:{mime};base64,{data}"'
    return re.sub(r'(<img[^>]*?src=")([^"]+)"', sub, text)


# Generated appendices (Oct 8, 2026): the rule index and the retired rule IDs, rewritten into manual.md between
# <!-- rules:index --> and <!-- rules:retired --> markers on every build (like navgraph's nav: markers), then built
# into the HTML with everything else.
RULE = re.compile(r"^>\s+- \*\*([A-Z]{2,8}-\d{1,3}[a-z]?(?:\.\d{1,2})?)\*\* (.*)$", re.M)  # TX-30.1: a sub-rule
RETIRED_BODY = re.compile(r"^\(?(Dropped|Retired|Moved|Merged|Removed|Replaced|Smart scan, replaced)\b")
# Retired IDs that no longer have a rule line, with what replaced them.
RETIRED_GONE = {
    "DEC-10": "Sensor reader (315/345/433 MHz sensors): dropped, decision 75.",
    "DEC-11": "Sensor reader: dropped, decision 75.",
    "DEC-12": "Jamming alarm: dropped, decision 75; alerts are SAME and DSC distress only.",
    "LINK-27": "The web app setting the Bluetooth module's rate: dropped, decision 79; Bluetooth is stock's 115200 only (LINK-25).",
}


def slug(title):
    t = re.sub(r"[^\w\- ]", "", title.strip().lower())
    return t.replace(" ", "-")


def gist(text, n=80):
    t = re.sub(r"\*\*|`", "", text)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    parts = re.split(r"(?<=[.;])\s", t, maxsplit=1)
    first = parts[0]
    if len(parts) > 1 and first.endswith(";"):
        first = first[:-1] + "…"
    if len(first) > n:
        first = first[: n - 1].rsplit(" ", 1)[0] + "…"
    return first.replace("|", "\\|")


def rule_appendices(md_text):
    chap = None
    rows, retired = [], []
    for line in md_text.split("\n"):
        if line.startswith("## ") and not line.startswith("## Appendix H") and not line.startswith("## Appendix I"):
            chap = line[3:].strip()
        m = RULE.match(line)
        if m and chap:
            rid, body = m.groups()
            short = chap
            if RETIRED_BODY.match(body):
                why = re.sub(r"\\*\\*|`", "", body.strip("() ")).replace("|", "\\\\|")
                retired.append((rid, f"[{short}](#{slug(chap)})", why if len(why) <= 200 else why[:199].rsplit(" ", 1)[0] + "…"))
            else:
                rows.append((rid, f"[{short}](#{slug(chap)})", gist(body)))
    for rid, why in RETIRED_GONE.items():
        retired.append((rid, "—", why))
    index, last = [], None
    for r, c, g in rows:
        if c != last:
            index += (["", ""] if last else []) + [f"**{c}**", "", "| Rule | Says |", "| --- | --- |"]
            last = c
        index.append(f"| {r} | {g} |")
    ret = ["| Rule | Chapter | What happened |", "| --- | --- | --- |"] + [f"| {r} | {c} | {g} |" for r, c, g in sorted(retired, key=lambda x: (x[0].split("-")[0], [int(n) for n in re.findall(r"\d+", x[0].split("-")[1])]))]
    return "\n".join(index), "\n".join(ret), len(rows), len(retired)


def splice(text, marker, body):
    a, b = f"<!-- rules:{marker} -->", f"<!-- /rules:{marker} -->"
    i, j = text.index(a) + len(a), text.index(b)
    return text[:i] + "\n" + body + "\n" + text[j:]


def write_rules_map():
    """docs/manual/RULES.md: rule prefix -> chapter file(s), so a job greps one line and reads one chapter."""
    by = {}
    for f in chapter_files():
        if f.name.startswith(("H-", "I-")):
            continue
        for m in RULE.finditer(f.read_text()):
            by.setdefault(m.group(1).split("-")[0], {}).setdefault(f.name, 0)
            by[m.group(1).split("-")[0]][f.name] += 1
    lines = ["# Rule prefix to chapter file", "",
             "Generated by `docs/tools/mkmanual.py`; don't edit. Grep a prefix (or `^PREFIX-N`), then read only that chapter file.", ""]
    for pre in sorted(by):
        lines.append(f"- `{pre}` -> " + ", ".join(n for n, _ in sorted(by[pre].items(), key=lambda x: -x[1])))
    out = "\n".join(lines) + "\n"
    r = CHAPTERS / "RULES.md"
    if not r.exists() or r.read_text() != out:
        r.write_text(out)


def update_md():
    text = read_book()
    index, ret, n, r = rule_appendices(text)
    for f, marker, body in ((CHAPTERS / next(x.name for x in chapter_files() if x.name.startswith("H-")), "index", index),
                            (CHAPTERS / next(x.name for x in chapter_files() if x.name.startswith("I-")), "retired", ret)):
        old = f.read_text()
        new = splice(old, marker, body)
        if new != old:
            f.write_text(new)
    write_rules_map()
    print(f"rule index: {n} rules, {r} retired IDs")


def build():
    md_text = read_book()
    # The decision log lives in decisions.md (Oct 13, 2026); the HTML shows it in Appendix E as before.
    # Archives (decisions/NNN-NNN.md, in order) then the current file's entries (from its first "N. " line).
    # The public manual (tools/export-manual.py) has no decision log and no Appendix E.
    if (DOCS / "decisions.md").exists():
        cur = (DOCS / "decisions.md").read_text()
        cur = cur[re.search(r"^\d+\. ", cur, re.M).start():]
        dec = "\n" + "".join(f.read_text() for f in sorted((DOCS / "decisions").glob("*.md"))) + cur
        md_text = re.sub(r"(## Appendix E\. Decision log\n\n)Every numbered decision[^\n]*\n", lambda m: m.group(1) + dec,
                         md_text)
    md = markdown.Markdown(extensions=["tables", "toc", "sane_lists", "attr_list"],
                           extension_configs={"toc": {"toc_depth": "2-3"}})
    body = md.convert(md_text)
    toc = md.toc_tokens

    # spec boxes and rule anchors
    body = re.sub(r"<blockquote>\s*<p><strong>Spec", '<blockquote class="spec">\n<p><strong>Spec', body)
    body = re.sub(r"<strong>([A-Z]{2,8}-\d{1,3}(?:\.\d{1,2})?)</strong>",
                  lambda m: f'<span class="rule" id="{m.group(1)}">{m.group(1)}</span>', body)
    # screenshot grids: tables whose cells are mostly images
    body = re.sub(r"<table>(\s*<thead>\s*<tr>\s*<th>\s*</th>)", r'<table class="shots">\1', body)
    body = body.replace("<em>(to convert)</em>", '<span class="todo">(to convert)</span>')
    body = embed_images(body, SRC.parent)

    title = "The Ferrite Manual"
    nav = ['<div class="brand">Ferrite</div><div class="sub">The manual · draft</div>']
    tops = [c for t in toc for c in t.get("children", [])] if toc and toc[0]["level"] == 1 else toc
    for h2 in tops:
        if True:
            nav.append(f'<a class="h2" href="#{h2["id"]}">{html.escape(h2["name"])}</a>')
            pass  # chapters only; every chapter has the same sections
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body><div class="wrap"><nav>{''.join(nav)}</nav>
<main><button class="theme" type="button">Light / dark</button>
{body}
<footer class="licence">© 2026 Alex Harvey. This manual is licensed under
<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>: share and adapt it with credit, not for
sale, under the same licence. The Ferrite firmware is under the PolyForm Noncommercial License 1.0.0.</footer>
</main></div><script>{JS}</script></body></html>
"""
    OUT.write_text(page)
    print(f"wrote {OUT.relative_to(ROOT)} ({len(page)//1024} KB)")


if __name__ == "__main__":
    update_md()
    build()
    if "--open" in sys.argv:
        subprocess.run(["open", str(OUT)])
