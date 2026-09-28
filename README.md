# 247hrsCare.com

Independent 24/7 care guidance and care-matching website: guides, a care-needs quiz, a cost calculator, lead generation, caregiver careers, contests, donations and advertising. It's a pure static site (HTML/CSS/vanilla JS) that runs on the **GitHub Pages free plan**.

## Structure
```
index.html, get-care.html (main lead funnel), care-quiz.html, cost-calculator.html, checklist.html
services/*.html   8 care-service landing pages (FAQ + Service schema)
guides/*.html     guide hub + 8 long-form articles (Article schema)
videos.html, careers.html, contests.html, donate.html, providers.html, advertise.html
about, contact, faq, how-we-make-money, privacy, terms, disclaimer, trademark, thank-you, 404
assets/css/style.css   design system (light and dark themes)
assets/js/config.js    ← all monetization settings (AdSense, GA4, donation links, YouTube videos)
assets/js/main.js      forms, quiz, calculator, ads, consent, video lite-embeds
_build/                Python generator (source of truth for page HTML)
```

## Branches and deploy
* `main` holds the source: the generator, CSS, JS and config.
* `gh-pages` holds the built, published site. GitHub Pages serves it from **Settings → Pages → Deploy from a branch → `gh-pages` / root**.
* **To redeploy:** run `python3.12 _build/build.py`, then copy the generated `*.html`, `services/`, `guides/`, `assets/`, `sitemap.xml`, `robots.txt`, `ads.txt`, `manifest.webmanifest` and `.nojekyll` to the `gh-pages` branch.

## Editing
* **Content and page HTML:** edit `_build/*.py`, then run `python3.12 _build/build.py` from the repo root. Any Python 3.12 or later works. The shared footer, cookie banner, sticky CTA and exit modal are generated into `assets/js/chrome.js`.
* **Monetization settings (no rebuild needed):** edit `assets/js/config.js`
  * `adsenseClient`: your `ca-pub-…` ID. House ads are replaced by AdSense automatically. Also update `ads.txt`.
  * `ga4`: your Google Analytics 4 ID.
  * `donate`: PayPal.me, Stripe Payment Link, Buy Me a Coffee or Ko-fi URLs.
  * `youtubeChannel` and `videos`: your channel and video IDs.

## Forms and the inbox
Every form posts through FormSubmit's AJAX endpoint. The destination inbox is stored **encoded** in `config.js` and decoded only when a form is submitted or an email link is clicked, so it never appears in the page HTML or as visible text. **The first submission triggers a one-time FormSubmit activation email. Click "Activate" in it.** After that, you can paste FormSubmit's random alias into `formsubmitAlias`.

## Custom domain
1. Set `SITE_URL = "https://247hrscare.com"` in `_build/layout.py` and rebuild.
2. Add a `CNAME` file containing `247hrscare.com`, then set the custom domain in Settings → Pages.
3. At your DNS provider, add A records for 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153, plus a `www` CNAME to `webworksa1.github.io`.

## Legal
© 2026 247hrsCare.com. See `trademark.html` for the trademark and copyright disclosure.
For domain, sponsorship, advertising or partnership inquiries, go to https://web.works/contact
