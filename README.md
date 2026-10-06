# pubup

Public pages for my apps: privacy policies and support pages, served by
GitHub Pages from the `docs/` folder.

## Porta

| Page | URL once Pages is on |
| --- | --- |
| Privacy policy (picks the visitor's language) | `https://orocoro.github.io/pubup/porta/privacy.html` |
| Support (picks the visitor's language) | `https://orocoro.github.io/pubup/porta/support.html` |
| Per language | `…/porta/<en\|de\|fr\|it>/privacy.html`, `…/support.html` |

In App Store Connect, use the per-language URL for each store locale, and the
language-picking URL where a single URL is asked for.

## Publishing

1. Fill in `site.json`: publisher name or legal entity, postal address,
   contact e-mail and the policy date. Every `«…»` must be replaced.
2. Run `python3 tools/build.py --check`. It rebuilds `docs/` and fails while
   any placeholder is left.
3. Commit `site.json` and `docs/`.
4. In the repository settings, under **Pages**, choose **Deploy from a
   branch**, pick the default branch and the `/docs` folder.

The text lives in `tools/content.py` (one block per language). Edit it there
and rebuild; never edit `docs/` by hand. The privacy facts were checked
against the Porta app code (no accounts, empty privacy manifest, location
resolved once on device, network hosts as listed). If the app starts
contacting a new service, update `HOSTS` in `tools/content.py`.

This text is a careful draft, not legal advice. Have it reviewed against the
Swiss FADP (nDSG) and, if you target EU users, the GDPR before relying on it.
