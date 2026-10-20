# pubup

Public legal pages, served by GitHub Pages from the root of `main`.

- **Picso**: `index.html`, `privacy.html`, `terms.html` at the root
  (`https://orocoro.github.io/pubup/`).
- **Porta**: everything under `porta/`
  (`https://orocoro.github.io/pubup/porta/privacy.html` and `/support.html`,
  plus per-language pages under `porta/<en|de|fr|it>/`).
- **Nesto**: privacy policy under `nesto/` (German at
  `https://orocoro.github.io/pubup/nesto/`, plus `nesto/<fr|it|en>/`).
  The source is `Nesto/docs/privacy-site/` in orocoro/04xPorj; copy it
  from there rather than editing here.
- **Einbürgerly**: support page and privacy policy (German and English) under
  `einbuergerly/` (`https://orocoro.github.io/pubup/einbuergerly/` and
  `/privacy.html`). The source is `einbuergerly/site/` in orocoro/04xPorj;
  copy it from there rather than editing here.

Porta's pages are generated: edit the text in `tools/content.py` and the
publisher details in `site.json`, then run `python3 tools/build.py --check`.
Never edit `porta/` by hand. The policy is written under Swiss law (FADP);
it is a careful draft, not legal advice.
