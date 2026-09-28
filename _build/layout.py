"""Shared layout for 247hrsCare.com static site generator."""
import json, html

SITE_URL = "https://webworksa1.github.io/247hrscare-com"   # change to https://247hrscare.com once DNS points here
SITE_NAME = "247hrsCare"
BROKER_URL = "https://web.works/contact"
TODAY = "2026-09-28"

I = {  # inline SVG icon paths (24x24, stroke)
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/>',
 "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 "moon": '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
 "brain": '<path d="M9 3a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 3 3h1V3z"/><path d="M15 3a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-3 3h-1V3z"/>',
 "hand": '<path d="M18 11V6a2 2 0 0 0-4 0v5"/><path d="M14 10V4a2 2 0 0 0-4 0v6"/><path d="M10 10.5V6a2 2 0 0 0-4 0v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.9-6-2.4L2.4 16a2 2 0 0 1 2.8-2.8L7 15"/>',
 "hospital": '<path d="M3 21h18"/><path d="M5 21V7l7-4 7 4v14"/><path d="M12 9v6M9 12h6"/>',
 "building": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1M10 21v-3h4v3"/>',
 "leaf": '<path d="M11 20A7 7 0 0 1 4 13c0-6 7-10 16-10 0 9-4 16-10 16z"/><path d="M4 21c3-6 7-9 12-11"/>',
 "check": '<path d="M5 12l5 5L20 7"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "calc": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h2M12 12h2M8 16h2M12 16h2M16 12v4"/>',
 "quiz": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14"/><path d="M12 17h.01"/>',
 "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
 "play": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9l5 3-5 3z"/>',
 "users": '<circle cx="9" cy="8" r="4"/><path d="M1 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1"/><path d="M16 4a4 4 0 0 1 0 8M23 21v-1a6 6 0 0 0-4-5.7"/>',
 "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
 "trophy": '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>',
 "gift": '<rect x="3" y="8" width="18" height="13" rx="1"/><path d="M12 8v13M3 12h18"/><path d="M12 8S10 3 7.5 4 9 8 12 8zM12 8s2-5 4.5-4S15 8 12 8z"/>',
 "megaphone": '<path d="M3 11v2a1 1 0 0 0 1 1h2l5 4V6L6 10H4a1 1 0 0 0-1 1z"/><path d="M15 9a4 4 0 0 1 0 6M18 6a8 8 0 0 1 0 12"/>',
 "handshake": '<path d="M11 17l2 2a1.4 1.4 0 0 0 2-2"/><path d="M14 14l2.5 2.5a1.4 1.4 0 0 0 2-2L15 11l-3 3-1-1a2 2 0 0 1 0-3l3-3 5 1 3-1v7l-2 1"/><path d="M2 7l3 1 5-2M2 7v7l6 6 1-1"/>',
 "star": '<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
 "x": '<path d="M6 6l12 12M18 6L6 18"/>',
 "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 "chart": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
 "download": '<path d="M12 3v12M7 10l5 5 5-5M4 21h16"/>',
 "pill": '<rect x="2" y="8" width="20" height="8" rx="4" transform="rotate(-45 12 12)"/><path d="M8.5 8.5l7 7"/>',
 "yt": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9l5 3-5 3z"/>',
}

def ic(name, size=24, sw=2):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[name]}</svg>'

LOGO_MARK = '''<svg width="38" height="38" viewBox="0 0 48 48" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#11939e"/><stop offset="1" stop-color="#0a5f67"/></linearGradient></defs><rect width="48" height="48" rx="13" fill="url(#lg)"/><circle cx="24" cy="24" r="14" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="66 22" transform="rotate(-60 24 24)"/><path d="M24 31s-7-4.3-7-9.2a3.9 3.9 0 0 1 7-2.3 3.9 3.9 0 0 1 7 2.3c0 4.9-7 9.2-7 9.2z" fill="#ff6b4a"/></svg>'''

SERVICES_NAV = [
 ("services/24-hour-home-care.html","24-Hour Home Care"),
 ("services/live-in-care.html","Live-In Care"),
 ("services/overnight-care.html","Overnight Care"),
 ("services/dementia-care.html","Dementia & Alzheimer's Care"),
 ("services/personal-companion-care.html","Personal & Companion Care"),
 ("services/post-hospital-respite-care.html","Post-Hospital & Respite Care"),
 ("services/assisted-living-memory-care.html","Assisted Living & Memory Care"),
 ("services/palliative-hospice-support.html","Palliative & Hospice Support"),
]

def e(s):
    return html.escape(s, quote=True)

def head(title, desc, path, r, schema=None, og_type="website"):
    url = f"{SITE_URL}/{path}".replace("/index.html", "/")
    full = title if "247hrsCare" in title else f"{title} | 247hrsCare"
    sch = ""
    for s in (schema or []):
        sch += f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>\n'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0e7c86">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="247hrsCare">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
{sch}</head>
'''

def header(r):
    svc = "".join(f'<li><a href="{r}{p}">{e(n)}</a></li>' for p, n in SERVICES_NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership — <a href="{BROKER_URL}" target="_blank" rel="noopener">web.works/contact</a></div>
<div class="emergency"><b>Medical emergency?</b> Call 911 (US/Canada) or your local emergency number now. 247hrsCare is an information &amp; care-matching service, not an emergency provider.</div>
<header class="site-header">
 <div class="container nav">
  <a class="logo" href="{r}index.html" aria-label="247hrsCare home">{LOGO_MARK}<span>247hrs<b>Care</b><small>Care guidance, around the clock</small></span></a>
  <nav aria-label="Main">
   <ul class="menu" id="menu">
    <li><button class="dd" aria-expanded="false">Find Care ▾</button><ul class="sub">
      <li><a href="{r}get-care.html">Free Care Match</a></li><li><a href="{r}care-quiz.html">Care Needs Quiz</a></li><li><a href="{r}cost-calculator.html">Care Cost Calculator</a></li><li><a href="{r}checklist.html">Free Care Checklist</a></li></ul></li>
    <li><button class="dd" aria-expanded="false">Services ▾</button><ul class="sub">{svc}</ul></li>
    <li><a href="{r}guides/index.html">Guides</a></li>
    <li><a href="{r}videos.html">Videos</a></li>
    <li><a href="{r}careers.html">Careers</a></li>
    <li><button class="dd" aria-expanded="false">Community ▾</button><ul class="sub">
      <li><a href="{r}contests.html">Contests &amp; Prizes</a></li><li><a href="{r}donate.html">Support Our Mission</a></li><li><a href="{r}faq.html">FAQ</a></li><li><a href="{r}about.html">About Us</a></li></ul></li>
    <li><button class="dd" aria-expanded="false">For Business ▾</button><ul class="sub">
      <li><a href="{r}providers.html">For Care Providers</a></li><li><a href="{r}advertise.html">Advertise &amp; Sponsor</a></li><li><a href="{r}careers.html#employers">Hire Caregivers</a></li><li><a href="{BROKER_URL}" target="_blank" rel="noopener">Acquire / Partner</a></li></ul></li>
    <li><a href="{r}contact.html">Contact</a></li>
   </ul>
  </nav>
  <div class="nav-actions">
   <button class="icon-btn theme-toggle" aria-label="Toggle dark mode">{ic("moon",20)}</button>
   <a class="btn btn-cta btn-sm btn-cta" href="{r}get-care.html">Free Care Match</a>
   <button class="icon-btn burger" aria-label="Open menu" aria-controls="menu" aria-expanded="false">{ic("menu",22)}</button>
  </div>
 </div>
</header>
<div class="scrim"></div>
'''

def footer(r):
    svc = "".join(f'<li><a href="{r}{p}">{e(n)}</a></li>' for p, n in SERVICES_NAV[:6])
    return f'''
<footer class="site-footer">
 <div class="container">
  <div class="fgrid">
   <div>
    <a class="logo" href="{r}index.html">{LOGO_MARK}<span>247hrs<b>Care</b></span></a>
    <p style="margin-top:14px">Independent care guidance, tools and matching for families who need help — day, night and everything in between.</p>
    <form class="form" data-form data-subject="Newsletter signup — 247hrsCare" data-success="You're subscribed. Watch your inbox for the weekly Care Brief.">
      <label for="nl-email" style="color:#fff">Weekly Care Brief (free)</label>
      <div style="display:flex;gap:8px"><input id="nl-email" type="email" name="email" placeholder="you@example.com" required aria-label="Email address"><button class="btn btn-cta btn-sm" type="submit">Join</button></div>
      <input type="hidden" name="form" value="newsletter"><input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="form-msg" role="status"></div>
    </form>
    <div class="social"><a class="yt-channel" href="#" aria-label="YouTube" target="_blank" rel="noopener">{ic("yt",18)}</a><a href="#" class="js-mail" aria-label="Email us" data-subject="Hello from a 247hrsCare visitor">{ic("mail",18)}</a><a href="{r}contact.html" aria-label="Contact form">{ic("phone",18)}</a></div>
   </div>
   <div><h4>Care Services</h4><ul>{svc}</ul></div>
   <div><h4>Tools &amp; Guides</h4><ul>
     <li><a href="{r}get-care.html">Free Care Match</a></li><li><a href="{r}care-quiz.html">Care Needs Quiz</a></li><li><a href="{r}cost-calculator.html">Cost Calculator</a></li><li><a href="{r}checklist.html">Care Checklist</a></li><li><a href="{r}guides/index.html">All Guides</a></li><li><a href="{r}videos.html">Video Library</a></li></ul></div>
   <div><h4>Get Involved</h4><ul>
     <li><a href="{r}careers.html">Caregiver Jobs</a></li><li><a href="{r}careers.html#team">Join Our Team</a></li><li><a href="{r}contests.html">Contests &amp; Prizes</a></li><li><a href="{r}donate.html">Donate</a></li><li><a href="{r}providers.html">List Your Agency</a></li><li><a href="{r}advertise.html">Advertise</a></li></ul></div>
   <div><h4>Company</h4><ul>
     <li><a href="{r}about.html">About</a></li><li><a href="{r}contact.html">Contact</a></li><li><a href="{r}how-we-make-money.html">How We Make Money</a></li><li><a href="{r}privacy.html">Privacy Policy</a></li><li><a href="{r}terms.html">Terms of Use</a></li><li><a href="{r}disclaimer.html">Medical Disclaimer</a></li><li><a href="{r}trademark.html">Trademark &amp; Copyright</a></li><li><a href="{r}sitemap.xml">Sitemap</a></li></ul></div>
  </div>
  <div class="fbottom">
   <span>© <span class="year">2026</span> 247hrsCare.com. All rights reserved. “247hrsCare” is used as an unregistered trade name — see <a href="{r}trademark.html">Trademark &amp; Copyright Disclosure</a>.</span>
   <span>Information only — not medical, legal or financial advice. <a href="{BROKER_URL}" target="_blank" rel="noopener">Domain / partnership inquiries</a></span>
  </div>
 </div>
</footer>
<div class="sticky-cta"><a class="btn btn-ghost" href="{r}care-quiz.html">Take the Quiz</a><a class="btn btn-cta" href="{r}get-care.html">Free Care Match</a></div>
<div class="cookie" role="dialog" aria-label="Cookie consent">
 <p><b>Your privacy.</b> We use essential storage to run this site and, with your permission, cookies for analytics and personalized ads (Google AdSense). See our <a href="{r}privacy.html">Privacy Policy</a>.</p>
 <div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn btn-brand btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div>
</div>
<div class="modal" id="exit-modal" role="dialog" aria-modal="true" aria-labelledby="exit-t">
 <div class="modal-box">
  <button class="icon-btn modal-x" aria-label="Close">{ic("x",18)}</button>
  <span class="tag">Free download</span>
  <h2 id="exit-t" style="font-size:1.5rem">Before you go — get the 24/7 Care Planning Checklist</h2>
  <p class="muted">The 40-point checklist families use to compare agencies, plan costs and avoid the most common mistakes.</p>
  <form class="form" data-form data-subject="Lead magnet: Care Checklist" data-redirect="checklist.html?unlocked=1">
   <input type="text" name="name" placeholder="First name" required aria-label="First name">
   <input type="email" name="email" placeholder="Email address" required aria-label="Email">
   <input type="hidden" name="form" value="exit-intent-checklist"><input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
   <button class="btn btn-cta btn-block" type="submit">Send me the checklist</button>
   <div class="form-msg" role="status"></div>
   <p class="hint mb0">No spam. Unsubscribe anytime.</p>
  </form>
 </div>
</div>
<script src="{r}assets/js/config.js"></script>
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
'''

def page(path, title, desc, body, schema=None, og_type="website"):
    depth = path.count("/")
    r = "../" * depth
    base = [{
        "@context": "https://schema.org", "@type": "Organization", "name": "247hrsCare",
        "url": SITE_URL + "/", "logo": SITE_URL + "/assets/img/favicon.svg",
        "contactPoint": {"@type": "ContactPoint", "contactType": "customer support", "url": SITE_URL + "/contact.html"}
    }] if path == "index.html" else []
    body = body.replace("{R}", r)
    return head(title, desc, path, r, base + (schema or []), og_type) + f'<body data-root="{r}">\n' + header(r) + '<main id="main">\n' + body + '\n</main>' + footer(r)

def ad(slot="default"):
    return f'<div class="container"><div class="ad-slot" data-slot="{slot}" aria-label="Advertisement"></div></div>'

def crumbs(items):
    """items: list of (href or None, label). hrefs use {R} placeholder."""
    out = []
    for h, l in items:
        out.append(f'<a href="{h}">{e(l)}</a>' if h else f'<span>{e(l)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " › ".join(out) + "</nav>"

def crumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": l, "item": f"{SITE_URL}/{p}".replace("/index.html", "/")} for i, (p, l) in enumerate(items)]}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs):
    return "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faqs)

HP = '<input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'
CONSENT = '<label class="check"><input type="checkbox" name="consent" value="yes" required> <span>I agree to be contacted by 247hrsCare and up to 3 vetted care partners by phone, text or email about my request. Consent is not a condition of any purchase. I have read the <a href="{R}privacy.html">Privacy Policy</a> and <a href="{R}how-we-make-money.html">How We Make Money</a>.</span></label>'

def mini_lead(care_type="", title="Get matched with vetted caregivers — free"):
    return f'''<div class="card" id="quick-match">
 <span class="tag">Free · No obligation</span>
 <h3>{e(title)}</h3>
 <p>Tell us where and when. A care advisor aims to reply within one business day — urgent requests first.</p>
 <form class="form" data-form data-subject="Quick care match request ({e(care_type or 'general')})" data-redirect="thank-you.html">
  <input type="hidden" name="form" value="quick-match"><input type="hidden" name="care_type" value="{e(care_type)}">{HP}
  <div><label for="qm-name">Your name</label><input id="qm-name" name="name" autocomplete="name" required></div>
  <div class="row2"><div><label for="qm-phone">Phone</label><input id="qm-phone" type="tel" name="phone" autocomplete="tel" required></div>
  <div><label for="qm-zip">ZIP / Postal code</label><input id="qm-zip" name="zip" autocomplete="postal-code" required></div></div>
  <div><label for="qm-email">Email</label><input id="qm-email" type="email" name="email" autocomplete="email" required></div>
  <div><label for="qm-when">When is care needed?</label><select id="qm-when" name="timeline" required><option value="">Select…</option><option>Immediately (within 48 hours)</option><option>Within 2 weeks</option><option>Within 1–3 months</option><option>Just researching</option></select></div>
  {CONSENT}
  <button class="btn btn-cta btn-block" type="submit">Get my free care match</button>
  <div class="form-msg" role="status"></div>
 </form>
</div>'''

def cta_band(h="Not sure what kind of care you need?", p="Answer 8 quick questions and get a personalised care recommendation in under 2 minutes — then compare options side by side."):
    return f'''<section><div class="container"><div class="cta-band reveal">
 <div><h2>{e(h)}</h2><p class="mb0">{e(p)}</p></div>
 <div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:flex-end"><a class="btn btn-cta" href="{{R}}care-quiz.html">Take the free quiz</a><a class="btn btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.5)" href="{{R}}get-care.html">Talk to an advisor</a></div>
</div></div></section>'''
