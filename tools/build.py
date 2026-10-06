#!/usr/bin/env python3
"""Render the public pages into docs/ (served by GitHub Pages).

    python3 tools/build.py          # render docs/ from site.json + tools/content.py
    python3 tools/build.py --check  # also fail if site.json still has «…» placeholders

Output layout:
    docs/index.html                     list of apps
    docs/porta/index.html               Porta landing page, links per language
    docs/porta/<lang>/privacy.html      privacy policy (en, de, fr, it)
    docs/porta/<lang>/support.html      support page
    docs/porta/privacy.html, support.html  redirect to the visitor's language
"""
import html
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content import HOSTS, LANG_NAMES, LANGS, PRIVACY, SUPPORT, UI  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
APP = "Porta"


def load_site():
    site = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
    return {k: html.escape(v) for k, v in site.items()}


def page(lang, title, body, css="../../style.css"):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""


def lang_switch(lang, name):
    links = []
    for other in LANGS:
        if other == lang:
            links.append(f'<strong>{LANG_NAMES[other]}</strong>')
        else:
            links.append(f'<a href="../{other}/{name}.html" hreflang="{other}" lang="{other}">{LANG_NAMES[other]}</a>')
    return f'<nav class="langs" aria-label="{UI[lang]["language"]}">' + " · ".join(links) + "</nav>"


def render_doc(lang, name, sections, site):
    ui = UI[lang]
    values = {**site, **HOSTS}
    other = "support" if name == "privacy" else "privacy"
    parts = [
        lang_switch(lang, name),
        f'<p class="app"><a href="../">{APP}</a></p>',
        f"<h1>{ui[name]}</h1>",
    ]
    if name == "privacy":
        parts.append(f'<p class="meta">{ui["updated"]}: {site["updated"]}</p>')
    else:
        parts.append(f"<p>{ui['not_official']}</p>")
    for heading, text in sections:
        parts.append(f"<h2>{heading}</h2>\n{text.format(**values)}")
    parts.append(f'<footer><a href="{other}.html">{ui[other]}</a></footer>')
    return page(lang, f"{ui[name]} · {APP}", "\n".join(parts))


def redirect(name):
    # Picks the visitor's language; falls back to English without JavaScript.
    langs = json.dumps(LANGS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{APP}</title>
<script>
  var langs = {langs};
  var pick = (navigator.languages || [navigator.language || "en"])
    .map(function (l) {{ return l.slice(0, 2).toLowerCase(); }})
    .find(function (l) {{ return langs.indexOf(l) >= 0; }}) || "en";
  location.replace(pick + "/{name}.html");
</script>
<noscript><meta http-equiv="refresh" content="0; url=en/{name}.html"></noscript>
</head>
<body><p><a href="en/{name}.html">{name}</a></p></body>
</html>
"""


def app_index():
    rows = []
    for lang in LANGS:
        ui = UI[lang]
        rows.append(
            f'<section lang="{lang}"><h2>{LANG_NAMES[lang]}</h2><p>{ui["home_intro"]}</p>'
            f'<p>{ui["not_official"]}</p>'
            f'<p><a href="{lang}/privacy.html">{ui["privacy"]}</a> · <a href="{lang}/support.html">{ui["support"]}</a></p></section>'
        )
    return page("en", APP, f"<h1>{APP}</h1>\n" + "\n".join(rows), css="../style.css")


def root_index():
    body = f'<h1>Apps</h1>\n<ul><li><a href="porta/">{APP}</a></li></ul>'
    return page("en", "Apps", body, css="style.css")


def main():
    site = load_site()
    if "--check" in sys.argv:
        missing = [k for k, v in site.items() if "«" in v]
        if missing:
            sys.exit(f"site.json still has placeholders: {', '.join(missing)}")

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "porta").mkdir(parents=True)
    shutil.copy(ROOT / "tools" / "style.css", OUT / "style.css")
    (OUT / ".nojekyll").write_text("")
    (OUT / "index.html").write_text(root_index(), encoding="utf-8")
    (OUT / "porta" / "index.html").write_text(app_index(), encoding="utf-8")
    for name in ("privacy", "support"):
        (OUT / "porta" / f"{name}.html").write_text(redirect(name), encoding="utf-8")
    for lang in LANGS:
        d = OUT / "porta" / lang
        d.mkdir()
        (d / "privacy.html").write_text(render_doc(lang, "privacy", PRIVACY[lang], site), encoding="utf-8")
        (d / "support.html").write_text(render_doc(lang, "support", SUPPORT[lang], site), encoding="utf-8")
    print(f"wrote {sum(1 for _ in OUT.rglob('*.html'))} pages to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
