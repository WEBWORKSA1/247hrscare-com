"""Service, guide, media, community, business and legal pages"""
from layout import *
from services import SERVICES
from guides import GUIDES

def service_page(s):
    path = f"services/{s['slug']}.html"
    others = "".join(f'<li><a href="{{R}}services/{o["slug"]}.html">{e(o["name"])}</a></li>' for o in SERVICES if o is not s)
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),("{R}index.html#services","Services"),(None,s["name"])])}
 <span class="eyebrow">{ic(s["icon"],16)} Care service guide</span>
 <h1>{e(s["title"])}</h1>
 <p class="lead">{e(s["intro"])}</p>
 <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-cta" href="{{R}}get-care.html?care_type={s["ctype"]}">Get matched for {e(s["name"].lower())}</a><a class="btn btn-ghost" href="{{R}}cost-calculator.html">Estimate costs</a></div>
</div></section>
<section style="padding-top:20px"><div class="container article-wrap">
 <article class="prose">
  <h2>Who is {e(s["name"].lower())} for?</h2><ul class="checklist">{"".join(f"<li>{e(x)}</li>" for x in s["who"])}</ul>
  <h2>What's typically included</h2><div class="grid g2">{"".join(f'<div class="card" style="padding:16px"><b>{ic("check",18)} </b>{e(x)}</div>' for x in s["includes"])}</div>
  {ad(s["slug"])}
  <h2>What does it cost?</h2><p>{e(s["cost"])}</p>
  <div class="note">Costs and coverage rules vary by location and change over time. Confirm with providers and programmes directly.</div>
  <h2>Frequently asked questions</h2>{faq_html(s["faqs"])}
  <h2>Related care options</h2><ul>{others}</ul>
 </article>
 <aside class="aside-sticky">{mini_lead(s["ctype"], "Find " + s["name"].lower() + " near you")}</aside>
</div></section>
{cta_band()}'''
    return path, page(path, s["title"], s["desc"], body, [faq_schema(s["faqs"]), crumb_schema([("index.html","Home"),(path,s["name"])]),
        {"@context":"https://schema.org","@type":"Service","name":s["name"],"serviceType":s["name"],"provider":{"@type":"Organization","name":"247hrsCare"},"areaServed":["US","CA"]}])

def guide_page(g):
    path = f"guides/{g['slug']}.html"
    import re
    toc = "".join(f'<a href="#{i}">{t}</a>' for i, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', g["body"]))
    related = "".join(f'<li><a href="{{R}}guides/{o["slug"]}.html">{e(o["title"])}</a></li>' for o in GUIDES if o is not g and o["cat"] == g["cat"]) or "".join(f'<li><a href="{{R}}guides/{o["slug"]}.html">{e(o["title"])}</a></li>' for o in GUIDES[:3] if o is not g)
    body = f'''
<section class="page-hero"><div class="container" style="max-width:900px">
 {crumbs([("{R}index.html","Home"),("{R}guides/index.html","Guides"),(None,g["cat"])])}
 <span class="tag">{e(g["cat"])}</span>
 <h1 style="font-size:clamp(1.8rem,4vw,2.8rem)">{e(g["title"])}</h1>
 <p class="lead">{e(g["desc"])}</p>
 <p class="meta">By the 247hrsCare Editorial Team · Updated {TODAY} · {g["mins"]} min read · <button class="btn btn-ghost btn-sm share">Share</button></p>
</div></section>
<section style="padding-top:10px"><div class="container article-wrap">
 <article class="prose">{g["body"]}
  {ad("article")}
  <div class="note"><b>Medical disclaimer:</b> This guide is general information, not medical, legal or financial advice. Always consult qualified professionals about your situation. <a href="{{R}}disclaimer.html">Read more</a>.</div>
  <h2>Related guides</h2><ul>{related}</ul>
 </article>
 <aside class="aside-sticky">
  <div class="card toc"><h3>On this page</h3>{toc}</div>
  <div style="margin-top:18px">{mini_lead("", "Need care now? Get matched free")}</div>
 </aside>
</div></section>'''
    schema = [{"@context":"https://schema.org","@type":"Article","headline":g["title"],"description":g["desc"],"dateModified":TODAY,"datePublished":TODAY,
               "author":{"@type":"Organization","name":"247hrsCare Editorial Team"},"publisher":{"@type":"Organization","name":"247hrsCare"},"mainEntityOfPage":f"{SITE_URL}/{path}"},
              crumb_schema([("index.html","Home"),("guides/index.html","Guides"),(path,g["title"])])]
    return path, page(path, g["title"], g["desc"], body, schema, "article")

def guides_index():
    cats = sorted(set(g["cat"] for g in GUIDES))
    pills = '<button class="on" data-filter="all">All</button>' + "".join(f'<button data-filter="{e(c)}">{e(c)}</button>' for c in cats)
    cards = "".join(f'''<a class="card" href="{{R}}guides/{g['slug']}.html" data-cat="{e(g['cat'])}"><span class="tag">{e(g['cat'])}</span><h3>{e(g['title'])}</h3><p>{e(g['desc'])}</p><span class="meta">{g['mins']} min read</span></a>''' for g in GUIDES)
    svc = "".join(f'''<a class="card" href="{{R}}services/{s['slug']}.html" data-cat="Services"><span class="tag">Services</span><h3>{e(s['name'])}</h3><p>{e(s['desc'])}</p></a>''' for s in SERVICES)
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Guides")])}
 <h1>Care Guides &amp; Resources</h1>
 <p class="lead">Plain-language answers on costs, planning, dementia, safety and caregiver wellbeing — written for families making hard decisions.</p>
 <div class="search">{ic("search",20)}<input id="site-search" type="search" placeholder="Search guides (e.g. dementia, cost, falls)…" aria-label="Search guides"></div>
 <div class="pill-nav" data-target="#guide-grid">{pills}<button data-filter="Services">Services</button></div>
</div></section>
<section style="padding-top:10px"><div class="container"><div class="grid g3" id="guide-grid">{cards}{svc}</div></div></section>
{ad("guides")}
{cta_band()}'''
    return page("guides/index.html","Care Guides — Costs, Planning, Dementia & Caregiver Help",
        "Free guides on 24-hour care costs, choosing a home care agency, dementia sundowning, fall prevention, hospital discharge and caregiver burnout.", body)

def videos():
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Videos")])}
 <span class="eyebrow">{ic("play",16)} Video library</span>
 <h1>Caregiving Video Library</h1>
 <p class="lead">Short, practical videos on dementia communication, safe transfers and day-to-day caregiving. New videos every week on our YouTube channel.</p>
 <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-cta yt-channel" href="#" target="_blank" rel="noopener">{ic("yt",20)} Subscribe on YouTube</a><a class="btn btn-ghost" href="#submit-video">Suggest a topic</a></div>
 <div class="pill-nav" data-target="#video-grid"><button class="on" data-filter="all">All</button><button data-filter="Dementia">Dementia</button><button data-filter="Caregiving skills">Caregiving skills</button></div>
</div></section>
<section style="padding-top:10px"><div class="container"><div class="grid g3" id="video-grid"></div>
 <p class="hint mt">Third-party videos are embedded using YouTube's standard embed player and remain the property of their creators. 247hrsCare is not affiliated with the channels shown.</p></div></section>
{ad("videos")}
<section class="section-alt" id="submit-video"><div class="container grid g2">
 <div><h2>Suggest a video or collaborate</h2><p class="lead">Are you a nurse, therapist, caregiver or creator? Suggest a topic, submit your video for feature, or pitch a sponsored series.</p><ul class="checklist"><li>Featured creator spotlights</li><li>Sponsored video series for care brands</li><li>Interview and podcast guest slots</li></ul></div>
 <div class="card"><form class="form" data-form data-subject="Video suggestion / collaboration" data-success="Thanks! Our content team will review your suggestion."><input type="hidden" name="form" value="video-suggestion">{HP}
  <div class="row2"><div><label for="v-n">Name</label><input id="v-n" name="name" required></div><div><label for="v-e">Email</label><input id="v-e" type="email" name="email" required></div></div>
  <div><label for="v-t">Type</label><select id="v-t" name="type"><option>Topic suggestion</option><option>Submit my video</option><option>Creator collaboration</option><option>Sponsored series</option></select></div>
  <div><label for="v-l">Video link or topic</label><textarea id="v-l" name="details" required></textarea></div>
  <button class="btn btn-cta" type="submit">Send</button><div class="form-msg" role="status"></div></form></div>
</div></section>'''
    return page("videos.html","Caregiving Videos — Dementia Care, Safe Transfers & More",
        "Watch free caregiving videos: dementia communication, understanding Alzheimer's, safe bed-to-wheelchair transfers and practical tips for family caregivers.", body)

def careers():
    roles = [("Caregiver / Companion","Hourly, overnight and live-in roles with partner agencies."),("Personal Support Worker / HHA / CNA","Certified hands-on care roles across home and community settings."),("Registered / Practical Nurse","Private duty, home health and care coordination roles."),("Dementia Care Specialist","Specialised roles for experienced memory-care caregivers.")]
    team = [("Health Content Writer","Remote · Freelance","Write and update evidence-based care guides."),("YouTube Video Editor","Remote · Freelance","Edit caregiving tutorials, shorts and interviews."),("Community & Social Manager","Remote · Part-time","Grow our community, run contests and moderate."),("Partnerships & Sales Lead","Remote · Commission","Onboard agencies, sponsors and advertisers."),("Clinical Reviewer (RN)","Remote · Per article","Medically review guides for accuracy."),("Campus / Community Ambassador","Volunteer","Spread free care resources in your community.")]
    rc = "".join(f'<div class="card" data-cat="care"><div class="ic">{ic("heart")}</div><h3>{e(t)}</h3><p class="mb0">{e(d)}</p></div>' for t,d in roles)
    tc = "".join(f'<div class="card"><span class="tag">{e(m)}</span><h3>{e(t)}</h3><p>{e(d)}</p><a class="more" href="#apply" onclick="document.getElementById(\'ap-role\').value=\'{e(t)}\'">Apply →</a></div>' for t,m,d in team)
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Careers")])}
 <span class="eyebrow">{ic("briefcase",16)} We're hiring</span>
 <h1>Caregiver Jobs &amp; Careers</h1>
 <p class="lead">Join our Caregiver Talent Network to be matched with home care, overnight and live-in roles — or join the team building 247hrsCare.</p>
 <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-cta" href="#apply">Join the talent network</a><a class="btn btn-ghost" href="#employers">I'm hiring caregivers</a></div>
</div></section>
<section style="padding-top:10px"><div class="container"><div class="section-head"><h2>Care roles we match</h2></div><div class="grid g4">{rc}</div></div></section>
<section class="section-alt" id="team"><div class="container"><div class="section-head"><span class="eyebrow">Join our team</span><h2>Help us build the most useful care resource online</h2><p>Remote-friendly roles for people who care about families and caregivers.</p></div><div class="grid g3">{tc}</div></div></section>
<section id="apply"><div class="container lead-wrap">
 <div class="card"><h2>Apply / join the talent network</h2>
 <form class="form" data-form data-subject="CAREER APPLICATION — 247hrsCare" data-success="Application received. If there's a match, we'll contact you by email or phone."><input type="hidden" name="form" value="career-application">{HP}
  <div class="row2"><div><label for="ap-n">Full name</label><input id="ap-n" name="name" required autocomplete="name"></div><div><label for="ap-e">Email</label><input id="ap-e" type="email" name="email" required autocomplete="email"></div></div>
  <div class="row2"><div><label for="ap-p">Phone</label><input id="ap-p" type="tel" name="phone" required autocomplete="tel"></div><div><label for="ap-l">City / ZIP / Postal code</label><input id="ap-l" name="location" required></div></div>
  <div><label for="ap-role">Role</label><select id="ap-role" name="role" required><option value="">Select…</option>{"".join(f"<option>{e(t)}</option>" for t,_ in roles)}{"".join(f"<option>{e(t)}</option>" for t,_,_ in team)}</select></div>
  <div class="row2"><div><label for="ap-x">Years of experience</label><select id="ap-x" name="experience"><option>Less than 1</option><option>1–3</option><option>3–5</option><option>5+</option></select></div>
  <div><label for="ap-a">Availability</label><select id="ap-a" name="availability"><option>Days</option><option>Nights / overnights</option><option>Weekends</option><option>Live-in</option><option>Flexible</option><option>Remote (team roles)</option></select></div></div>
  <div><label for="ap-c">Certifications / portfolio link</label><input id="ap-c" name="certifications" placeholder="e.g. CNA, HHA, PSW, CPR — or a portfolio URL"></div>
  <div><label for="ap-m">Tell us about yourself</label><textarea id="ap-m" name="message"></textarea></div>
  <label class="check"><input type="checkbox" name="consent" value="yes" required> <span>I consent to 247hrsCare storing my application and sharing it with potential employers for matching purposes.</span></label>
  <button class="btn btn-cta" type="submit">Submit application</button><div class="form-msg" role="status"></div></form></div>
 <aside class="aside-sticky"><div class="card"><h3>Why join?</h3><ul class="checklist"><li>Free for caregivers — always</li><li>Roles matched to your schedule</li><li>Free training videos and guides</li><li>Eligible for Caregiver Hero Awards</li></ul></div></aside>
</div></section>
<section class="section-alt" id="employers"><div class="container grid g2">
 <div><span class="eyebrow">For employers</span><h2>Hire caregivers faster</h2><p class="lead">Home care agencies and families can post openings to our talent network. Featured job posts appear across our careers page, newsletter and social channels.</p>
  <div class="grid g2"><div class="card tier"><h3>Standard post</h3><div class="price">Free</div><p class="mb0">Shared with matched candidates.</p></div><div class="card tier featured"><h3>Featured post</h3><div class="price">$49</div><p class="mb0">30 days · newsletter + social boost.</p></div></div></div>
 <div class="card"><h3>Post a caregiver job</h3>
 <form class="form" data-form data-subject="EMPLOYER JOB POST — 247hrsCare" data-success="Thanks! We'll confirm your job post by email within one business day."><input type="hidden" name="form" value="employer-job-post">{HP}
  <div class="row2"><div><label for="em-o">Organisation / family name</label><input id="em-o" name="organisation" required></div><div><label for="em-n">Contact name</label><input id="em-n" name="name" required></div></div>
  <div class="row2"><div><label for="em-e">Email</label><input id="em-e" type="email" name="email" required></div><div><label for="em-p">Phone</label><input id="em-p" type="tel" name="phone"></div></div>
  <div class="row2"><div><label for="em-r">Role</label><input id="em-r" name="role" required placeholder="e.g. Overnight caregiver"></div><div><label for="em-l">Location</label><input id="em-l" name="location" required></div></div>
  <div><label for="em-t">Listing type</label><select id="em-t" name="listing"><option>Standard (free)</option><option>Featured ($49 / 30 days)</option><option>Bulk hiring — contact me</option></select></div>
  <div><label for="em-d">Job details (pay, schedule, requirements)</label><textarea id="em-d" name="details" required></textarea></div>
  <button class="btn btn-brand" type="submit">Submit job post</button><div class="form-msg" role="status"></div></form></div>
</div></section>'''
    return page("careers.html","Caregiver Jobs & Careers — Join the Talent Network",
        "Find caregiver, PSW, HHA, CNA and nurse jobs, join the 247hrsCare talent network, or apply for remote roles on our content and community team.", body,
        [{"@context":"https://schema.org","@type":"WebPage","name":"Caregiver Jobs & Careers"}])

def contests():
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Contests & Prizes")])}
 <span class="eyebrow">{ic("trophy",16)} Now accepting entries</span>
 <h1>Caregiver Hero Awards &amp; Community Contests</h1>
 <p class="lead">Caregivers rarely get thanked. We're changing that — nominate a caregiver, share your story, and win prizes funded by our sponsors and supporters.</p>
 <p style="font-weight:700;margin-bottom:8px">Autumn 2026 round closes December 15, 2026</p>
 <div class="countdown" data-countdown="2026-12-15T23:59:59-05:00"></div>
</div></section>
<section style="padding-top:10px"><div class="container grid g3">
 <div class="card reveal"><div class="ic gold">{ic("trophy")}</div><span class="tag">Award</span><h3>Caregiver Hero of the Season</h3><p>Nominate a professional or family caregiver who goes above and beyond. Winner featured on our homepage, newsletter and YouTube channel.</p><p class="mb0"><b>Prize:</b> $250 gift card + feature</p></div>
 <div class="card reveal"><div class="ic coral">{ic("book")}</div><span class="tag">Writing</span><h3>Care Stories Contest</h3><p>Share a true caregiving story (300–1,000 words) that could help another family. Best stories are published with credit.</p><p class="mb0"><b>Prize:</b> $100 gift card + publication</p></div>
 <div class="card reveal"><div class="ic">{ic("star")}</div><span class="tag">Photo / video</span><h3>Moments of Care</h3><p>Submit a photo or short video that captures a moment of care, connection or joy (with everyone's permission).</p><p class="mb0"><b>Prize:</b> $50 gift card + feature</p></div>
</div></section>
{ad("contests")}
<section class="section-alt" id="enter"><div class="container lead-wrap">
 <div class="card"><h2>Enter or nominate</h2>
 <form class="form" data-form data-subject="CONTEST ENTRY — 247hrsCare" data-success="Entry received! We'll confirm by email. Good luck!"><input type="hidden" name="form" value="contest-entry">{HP}
  <div><label for="ct-c">Contest</label><select id="ct-c" name="contest" required><option>Caregiver Hero of the Season (nomination)</option><option>Care Stories Contest</option><option>Moments of Care (photo / video)</option></select></div>
  <div class="row2"><div><label for="ct-n">Your name</label><input id="ct-n" name="name" required></div><div><label for="ct-e">Email</label><input id="ct-e" type="email" name="email" required></div></div>
  <div class="row2"><div><label for="ct-nom">Nominee name (if nominating)</label><input id="ct-nom" name="nominee"></div><div><label for="ct-loc">Country / region</label><input id="ct-loc" name="region" required></div></div>
  <div><label for="ct-s">Your story / why they deserve it</label><textarea id="ct-s" name="story" required minlength="100"></textarea></div>
  <div><label for="ct-l">Link to photo / video / document (optional)</label><input id="ct-l" type="url" name="media_link" placeholder="https://"></div>
  <label class="check"><input type="checkbox" name="rules" value="accepted" required> <span>I am 18+ and accept the Official Rules below. I confirm I have permission from everyone featured in my entry.</span></label>
  <button class="btn btn-cta" type="submit">Submit entry</button><div class="form-msg" role="status"></div></form></div>
 <aside class="aside-sticky"><div class="card"><h3>{ic("gift",20)} Sponsor a prize</h3><p>Put your brand in front of caregivers and families. Prize sponsors get logo placement, social mentions and a winner feature.</p><a class="btn btn-brand btn-sm" href="{{R}}advertise.html#packages">Become a prize sponsor</a></div>
 <div class="card" style="margin-top:18px"><h3>Fund the prize pool</h3><p class="mb0">Every donation allocated to "Contests &amp; prizes" goes straight into caregiver awards. <a href="{{R}}donate.html">Donate →</a></p></div></aside>
</div></section>
<section><div class="container" style="max-width:860px"><h2>Official Rules (summary)</h2>
<details><summary>Eligibility</summary><p>Open to legal residents of the United States (excluding where prohibited) and Canada (excluding Quebec where required by law), and other countries where permitted by local law, who are 18 or older. Employees of 247hrsCare, prize sponsors and their immediate families are not eligible.</p></details>
<details><summary>No purchase necessary</summary><p>No purchase, payment or donation is necessary to enter or win. A donation or purchase does not improve your chances of winning. Void where prohibited or restricted by law.</p></details>
<details><summary>Entry period &amp; limits</summary><p>The Autumn 2026 round runs until December 15, 2026 at 11:59 p.m. Eastern Time. One entry per person per contest.</p></details>
<details><summary>Judging</summary><p>Entries are judged by a panel on originality, impact and relevance to caregiving (40/40/20). This is a skill-based contest, not a game of chance. Canadian winners must correctly answer a time-limited skill-testing question.</p></details>
<details><summary>Prizes &amp; notification</summary><p>Prizes are digital gift cards of the stated value; no cash alternative except at the organiser's discretion. Winners are notified by email within 30 days of the close date and must respond within 14 days. Winners are responsible for any applicable taxes.</p></details>
<details><summary>Rights &amp; privacy</summary><p>By entering, you grant 247hrsCare a non-exclusive, royalty-free licence to publish your entry with credit. You retain ownership. Personal data is handled per our Privacy Policy. Do not include sensitive health information about others without consent.</p></details>
</div></section>'''
    return page("contests.html","Caregiver Hero Awards & Contests — Win Prizes",
        "Nominate a caregiver hero, share your care story or photo, and win prizes. Free to enter. Sponsors welcome.", body)

def donate():
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Support Our Mission")])}
 <span class="eyebrow">{ic("heart",16)} Reader-supported</span>
 <h1>Keep care guidance free for every family</h1>
 <p class="lead">247hrsCare is free for families. Your support pays for operations, outreach, the people who create our guides and videos, and prizes that celebrate caregivers.</p>
</div></section>
<section style="padding-top:10px"><div class="container lead-wrap">
 <div class="card"><h2>Choose your support</h2>
 <form class="form" id="donate-form" data-form data-subject="DONATION PLEDGE — 247hrsCare" data-success="Thank you! We'll email you a secure payment link and receipt details shortly."><input type="hidden" name="form" value="donation-pledge">{HP}
  <div><label>Frequency</label><div class="amounts"><label class="choice"><input type="radio" name="frequency" value="One-time" checked><span>One-time</span></label><label class="choice"><input type="radio" name="frequency" value="Monthly"><span>Monthly</span></label><label class="choice"><input type="radio" name="frequency" value="Yearly"><span>Yearly</span></label></div></div>
  <div><label>Amount (USD)</label><div class="amounts">{"".join(f'<label class="choice"><input type="radio" name="amount" value="${a}" {"checked" if a==25 else ""}><span>${a}</span></label>' for a in (10,25,50,100,250,500))}</div>
   <input style="margin-top:10px" name="custom_amount" type="number" min="1" placeholder="Or enter a custom amount" aria-label="Custom amount"></div>
  <div><label for="dn-f">Direct my support to</label><select id="dn-f" name="fund"><option>Where it's needed most</option><option>Operations &amp; free tools</option><option>Promotions &amp; outreach to families</option><option>Hiring writers, nurses &amp; video talent</option><option>Contests &amp; caregiver prizes</option></select></div>
  <div class="row2"><div><label for="dn-n">Name</label><input id="dn-n" name="name" required></div><div><label for="dn-e">Email</label><input id="dn-e" type="email" name="email" required></div></div>
  <label class="check"><input type="checkbox" name="anonymous" value="yes"> <span>Keep my support anonymous</span></label>
  <div><label for="dn-m">Message (optional)</label><textarea id="dn-m" name="message" style="min-height:80px"></textarea></div>
  <div id="pay-links" style="display:flex;gap:10px;flex-wrap:wrap"></div>
  <button class="btn btn-cta" type="submit">Pledge my support</button><div class="form-msg" role="status"></div>
  <p class="hint mb0">247hrsCare is an independent, privately operated website, not a registered charity. Contributions are not tax-deductible.</p>
 </form></div>
 <aside class="aside-sticky"><div class="card"><h3>Where your support goes</h3>
  <p class="mb0"><b>Operations &amp; free tools</b> — 40%</p><div class="meter"><i style="width:40%"></i></div>
  <p class="mb0" style="margin-top:12px"><b>Outreach &amp; promotion</b> — 25%</p><div class="meter"><i style="width:25%"></i></div>
  <p class="mb0" style="margin-top:12px"><b>Talent: writers, nurses, editors</b> — 20%</p><div class="meter"><i style="width:20%"></i></div>
  <p class="mb0" style="margin-top:12px"><b>Contests &amp; prizes</b> — 15%</p><div class="meter"><i style="width:15%"></i></div>
  <p class="hint" style="margin-top:12px">Target allocation for general donations. Directed gifts go 100% to the chosen area.</p></div>
 <div class="card" style="margin-top:18px"><h3>Other ways to help</h3><ul class="checklist"><li><a href="#" class="share">Share 247hrsCare</a> with a family who needs it</li><li>Subscribe to our <a class="yt-channel" href="#" target="_blank" rel="noopener">YouTube channel</a></li><li><a href="{{R}}advertise.html">Sponsor</a> a guide, video or prize</li><li><a href="{{R}}careers.html#team">Volunteer</a> as an ambassador</li></ul></div></aside>
</div></section>'''
    return page("donate.html","Support 247hrsCare — Donate to Keep Care Guidance Free",
        "Support free care guidance for families. Donations fund operations, outreach, hiring content talent, and caregiver contests and prizes.", body)

def providers():
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"For Care Providers")])}
 <span class="eyebrow">{ic("building",16)} For agencies &amp; communities</span>
 <h1>Receive qualified families looking for care</h1>
 <p class="lead">Home care agencies, live-in care providers, senior living and memory care communities: partner with 247hrsCare to receive pre-qualified care inquiries in your service area.</p>
 <a class="btn btn-cta" href="#apply-provider">Apply to join the network</a>
</div></section>
<section style="padding-top:10px"><div class="container grid g3">
 <div class="card"><div class="ic">{ic("users")}</div><h3>Pre-qualified inquiries</h3><p class="mb0">Every inquiry includes care type, schedule, timeline, location and payment source, with documented consent to be contacted.</p></div>
 <div class="card"><div class="ic coral">{ic("chart")}</div><h3>Flexible pricing</h3><p class="mb0">Pay-per-inquiry, monthly territory plans or placement-based referral fees — whichever fits your model.</p></div>
 <div class="card"><div class="ic gold">{ic("shield")}</div><h3>Quality first</h3><p class="mb0">Families see at most three matches. We vet licensing and insurance and remove providers with poor feedback.</p></div>
</div></section>
<section class="section-alt"><div class="container"><div class="section-head"><h2>Partner plans</h2><p>Indicative pricing — final terms depend on market and volume.</p></div>
 <div class="grid g3">
  <div class="card tier"><h3>Pay per inquiry</h3><div class="price">from $45</div><p>per exclusive-to-3 inquiry</p><ul class="checklist" style="text-align:left"><li>No monthly commitment</li><li>Choose care types and ZIP codes</li><li>Credit for invalid inquiries</li></ul></div>
  <div class="card tier featured"><h3>Territory partner</h3><div class="price">from $399<small style="font-size:1rem">/mo</small></div><p>priority in your area</p><ul class="checklist" style="text-align:left"><li>Priority matching</li><li>Featured on service pages</li><li>Monthly performance report</li></ul></div>
  <div class="card tier"><h3>Placement referral</h3><div class="price">Custom</div><p>senior living &amp; memory care</p><ul class="checklist" style="text-align:left"><li>Fee on move-in only</li><li>Tour scheduling support</li><li>Family follow-up</li></ul></div>
 </div></div></section>
<section id="apply-provider"><div class="container lead-wrap">
 <div class="card"><h2>Apply to become a partner</h2>
 <form class="form" data-form data-subject="PROVIDER PARTNER APPLICATION — 247hrsCare" data-success="Thanks! Our partnerships team will contact you within two business days."><input type="hidden" name="form" value="provider-application">{HP}
  <div class="row2"><div><label for="pv-o">Organisation name</label><input id="pv-o" name="organisation" required></div><div><label for="pv-w">Website</label><input id="pv-w" type="url" name="website" placeholder="https://"></div></div>
  <div class="row2"><div><label for="pv-n">Contact name</label><input id="pv-n" name="name" required></div><div><label for="pv-t">Title</label><input id="pv-t" name="title"></div></div>
  <div class="row2"><div><label for="pv-e">Business email</label><input id="pv-e" type="email" name="email" required></div><div><label for="pv-p">Phone</label><input id="pv-p" type="tel" name="phone" required></div></div>
  <div><label for="pv-type">Provider type</label><select id="pv-type" name="provider_type" required><option value="">Select…</option><option>Home care agency (non-medical)</option><option>Home health agency (skilled)</option><option>Live-in care provider</option><option>Assisted living / memory care</option><option>Nursing home / skilled nursing</option><option>Hospice / palliative</option><option>Care technology / product</option><option>Other</option></select></div>
  <div class="row2"><div><label for="pv-a">Service area (cities / ZIPs)</label><input id="pv-a" name="service_area" required></div><div><label for="pv-l">Licence number (if applicable)</label><input id="pv-l" name="licence"></div></div>
  <div><label for="pv-pl">Interested in</label><select id="pv-pl" name="plan"><option>Pay per inquiry</option><option>Territory partner</option><option>Placement referral</option><option>Advertising / sponsorship</option><option>Not sure — let's talk</option></select></div>
  <div><label for="pv-m">Capacity &amp; notes</label><textarea id="pv-m" name="notes"></textarea></div>
  <button class="btn btn-cta" type="submit">Apply now</button><div class="form-msg" role="status"></div></form></div>
 <aside class="aside-sticky"><div class="card"><h3>How inquiries are delivered</h3><ul class="checklist"><li>Real-time email alert</li><li>Consent record included</li><li>CSV export on request</li><li>Families capped at 3 providers</li></ul></div></aside>
</div></section>'''
    return page("providers.html","For Care Providers — Get Qualified Home Care Leads",
        "Home care agencies and senior living communities: receive pre-qualified family care inquiries with pay-per-inquiry, territory or placement-based plans.", body)

def advertise():
    pk = [("Community Sponsor","$99/mo",["Logo in footer sponsor strip","1 newsletter mention / month","Social thank-you post"]),
          ("Category Sponsor","$499/mo",["Exclusive banner on one service category","Sponsored guide (clearly labelled)","Monthly performance report"]),
          ("Video Series Sponsor","$750/series",["Pre-roll mention in 4 videos","Link in video descriptions","Feature on video library page"]),
          ("Newsletter Takeover","$299/issue",["Top placement in the weekly Care Brief","Dedicated CTA button","Click report"]),
          ("Contest Prize Sponsor","$250+",["Brand named on the prize","Logo on contests page","Winner announcement feature"]),
          ("Custom Partnership","Let's talk",["Co-branded tools or calculators","Lead-gen integrations","Content syndication"])]
    cards = "".join(f'<div class="card tier{" featured" if i==1 else ""}"><h3>{e(n)}</h3><div class="price" style="font-size:1.8rem">{e(p)}</div><ul class="checklist" style="text-align:left">{"".join(f"<li>{e(x)}</li>" for x in f)}</ul></div>' for i,(n,p,f) in enumerate(pk))
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Advertise & Sponsor")])}
 <span class="eyebrow">{ic("megaphone",16)} Media kit</span>
 <h1>Advertise &amp; sponsor on 247hrsCare</h1>
 <p class="lead">Reach adult children, spouses and professional caregivers at the exact moment they are researching care, costs and products.</p>
 <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-cta" href="#ad-inquiry">Request the media kit</a><a class="btn btn-ghost" href="{BROKER_URL}" target="_blank" rel="noopener">Domain / acquisition inquiries</a></div>
</div></section>
<section style="padding-top:10px"><div class="container grid g4">
 <div class="card"><div class="ic">{ic("users")}</div><h3>High-intent audience</h3><p class="mb0">Families actively comparing care options and budgets.</p></div>
 <div class="card"><div class="ic coral">{ic("globe")}</div><h3>North America first</h3><p class="mb0">U.S. and Canada focus, with global reach.</p></div>
 <div class="card"><div class="ic gold">{ic("play")}</div><h3>Multi-channel</h3><p class="mb0">Web, YouTube, newsletter and social.</p></div>
 <div class="card"><div class="ic">{ic("shield")}</div><h3>Brand-safe</h3><p class="mb0">All sponsored content is clearly labelled.</p></div>
</div></section>
<section class="section-alt" id="packages"><div class="container"><div class="section-head"><h2>Sponsorship packages</h2><p>Indicative starting prices. Custom bundles available.</p></div><div class="grid g3">{cards}</div></div></section>
<section id="ad-inquiry"><div class="container lead-wrap">
 <div class="card"><h2>Advertising &amp; partnership inquiry</h2>
 <form class="form" data-form data-subject="ADVERTISING / SPONSORSHIP INQUIRY — 247hrsCare" data-success="Thanks! We'll send the media kit and availability shortly."><input type="hidden" name="form" value="advertising-inquiry">{HP}
  <div class="row2"><div><label for="ad-c">Company</label><input id="ad-c" name="company" required></div><div><label for="ad-n">Your name</label><input id="ad-n" name="name" required></div></div>
  <div class="row2"><div><label for="ad-e">Email</label><input id="ad-e" type="email" name="email" required></div><div><label for="ad-p">Phone</label><input id="ad-p" type="tel" name="phone"></div></div>
  <div><label for="ad-i">Interest</label><select id="ad-i" name="interest">{"".join(f"<option>{e(n)}</option>" for n,_,_ in pk)}<option>Domain / website acquisition</option></select></div>
  <div><label for="ad-b">Monthly budget</label><select id="ad-b" name="budget"><option>Under $250</option><option>$250–$1,000</option><option>$1,000–$5,000</option><option>$5,000+</option></select></div>
  <div><label for="ad-m">Goals &amp; timing</label><textarea id="ad-m" name="message"></textarea></div>
  <button class="btn btn-cta" type="submit">Send inquiry</button><div class="form-msg" role="status"></div></form></div>
 <aside class="aside-sticky"><div class="card"><h3>Interested in the whole website?</h3><p>This website and the 247hrsCare.com domain name may be available for acquisition, sponsorship or partnership.</p><a class="btn btn-brand btn-sm" href="{BROKER_URL}" target="_blank" rel="noopener">Contact via web.works</a></div></aside>
</div></section>'''
    return page("advertise.html","Advertise & Sponsor — Reach Families Researching Care",
        "Sponsorship and advertising packages on 247hrsCare: category sponsorships, sponsored guides, video series, newsletter and contest prize sponsorships.", body)

def about():
    body = f'''
<section class="page-hero"><div class="container" style="max-width:900px">
 {crumbs([("{R}index.html","Home"),(None,"About")])}
 <h1>About 247hrsCare</h1>
 <p class="lead">Care needs don't keep office hours. 247hrsCare exists so that any family — at any hour — can understand their options, know the real costs and reach trustworthy help.</p>
</div></section>
<section style="padding-top:10px"><div class="container" style="max-width:900px"><div class="prose">
 <h2>Our mission</h2><p>To make finding and paying for care less confusing, less lonely and less expensive — through clear information, free tools and honest matching.</p>
 <h2>What we do</h2><ul><li><b>Guides</b> — plain-language, practical articles reviewed for accuracy.</li><li><b>Tools</b> — the care needs quiz, cost calculator and planning checklist.</li><li><b>Matching</b> — connecting families with up to three vetted providers.</li><li><b>Community</b> — celebrating caregivers through awards, stories and videos.</li><li><b>Careers</b> — a talent network for caregivers and the people who support them.</li></ul>
 <h2>Our editorial standards</h2><p>Guides cite recognised sources (such as national cost-of-care surveys and government programmes), are dated, and are updated when facts change. Sponsored content is always labelled. Advertisers and partners never influence our editorial recommendations.</p>
 <h2>Independence &amp; transparency</h2><p>We are an independent information service — not a care agency, insurer or government body. Read exactly <a href="{{R}}how-we-make-money.html">how we make money</a>.</p>
 <h2>Work with us</h2><p>We're looking for writers, nurses, video editors and community builders. <a href="{{R}}careers.html#team">See open roles</a>. For partnerships, sponsorship or to acquire this website or domain, visit <a href="{BROKER_URL}" target="_blank" rel="noopener">web.works/contact</a>.</p>
</div></div></section>
{cta_band()}'''
    return page("about.html","About 247hrsCare — Our Mission & Standards","About 247hrsCare: an independent care guidance and matching service helping families find 24/7, live-in, overnight and dementia care.", body)

def contact():
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Contact")])}
 <h1>Contact us</h1>
 <p class="lead">Questions, feedback, corrections or partnership ideas — we read every message.</p>
</div></section>
<section style="padding-top:10px"><div class="container lead-wrap">
 <div class="card"><form class="form" data-form data-subject="CONTACT FORM — 247hrsCare" data-success="Thanks — your message has been sent. We'll reply by email."><input type="hidden" name="form" value="contact">{HP}
  <div class="row2"><div><label for="ct-name">Name</label><input id="ct-name" name="name" required autocomplete="name"></div><div><label for="ct-email">Email</label><input id="ct-email" type="email" name="email" required autocomplete="email"></div></div>
  <div><label for="ct-topic">Topic</label><select id="ct-topic" name="topic"><option>General question</option><option>I need care for someone</option><option>Careers / talent network</option><option>Provider partnership</option><option>Advertising / sponsorship</option><option>Contest question</option><option>Donation question</option><option>Content correction</option><option>Privacy request</option><option>Copyright / trademark notice</option></select></div>
  <div><label for="ct-msg">Message</label><textarea id="ct-msg" name="message" required></textarea></div>
  <button class="btn btn-cta" type="submit">Send message</button><div class="form-msg" role="status"></div></form></div>
 <aside class="aside-sticky">
  <div class="card"><h3>{ic("mail",20)} Prefer email?</h3><p>Open a message in your own email app.</p><a href="#" class="btn btn-brand btn-sm js-mail" data-subject="Inquiry from 247hrsCare.com">Email us</a></div>
  <div class="card" style="margin-top:18px"><h3>Need care now?</h3><p>Use the <a href="{{R}}get-care.html">free care match</a> for the fastest response.</p><p class="hint mb0">Medical emergency? Call 911 or your local emergency number.</p></div>
  <div class="card" style="margin-top:18px"><h3>Domain, sponsorship &amp; partnership</h3><p class="mb0"><a href="{BROKER_URL}" target="_blank" rel="noopener">web.works/contact</a></p></div>
 </aside>
</div></section>'''
    return page("contact.html","Contact 247hrsCare","Contact 247hrsCare with questions, feedback, partnership or advertising inquiries.", body)

FAQ = [("What is 247hrsCare?","An independent website offering care guides, free planning tools and free matching with third-party care providers."),
 ("Do you provide caregivers directly?","No. Care is provided by independent third-party agencies, communities and professionals. We help you compare and connect."),
 ("How much does it cost to use 247hrsCare?","Nothing. Families never pay us. We earn from advertising, provider partnerships, sponsorships and reader support."),
 ("Who will contact me after I submit a request?","A 247hrsCare advisor and, with your consent, up to three matched providers."),
 ("Can I request that my data be deleted?","Yes. Use the contact form and choose 'Privacy request'."),
 ("Are your guides medical advice?","No. They are general information. Always consult a qualified professional."),
 ("How do I become a partner or advertiser?","See For Care Providers and Advertise & Sponsor, or submit the inquiry forms on those pages."),
 ("Are contest entries free?","Yes. No purchase or donation is necessary to enter or win."),
 ("Is my donation tax-deductible?","No. 247hrsCare is a privately operated website, not a registered charity."),
 ("Is this website or domain for sale?","For acquisition, sponsorship or partnership inquiries, please use web.works/contact.")]

def faq():
    body = f'''<section class="page-hero"><div class="container" style="max-width:860px">{crumbs([("{R}index.html","Home"),(None,"FAQ")])}<h1>Frequently Asked Questions</h1></div></section>
<section style="padding-top:10px"><div class="container" style="max-width:860px">{faq_html(FAQ + HOME_FAQ_EXTRA)}</div></section>{ad("faq")}{cta_band()}'''
    return page("faq.html","FAQ — 247hrsCare","Answers about how 247hrsCare works, costs, privacy, partnerships, contests and donations.", body, [faq_schema(FAQ + HOME_FAQ_EXTRA)])

HOME_FAQ_EXTRA = [("What is the difference between home care and home health care?","Home care is non-medical help (companionship, personal care). Home health care is skilled clinical care ordered by a doctor, such as nursing or therapy."),
 ("Does Medicare pay for 24-hour care?","Generally no. Medicare covers part-time skilled home health and hospice, not ongoing custodial care.")]

def legal(slug, title, desc, content):
    body = f'''<section class="page-hero"><div class="container" style="max-width:900px">{crumbs([("{R}index.html","Home"),(None,title)])}<h1>{e(title)}</h1><p class="meta">Last updated: {TODAY}</p></div></section>
<section style="padding-top:10px"><div class="container" style="max-width:900px"><div class="prose">{content}</div></div></section>'''
    return page(slug, title, desc, body)

LEGAL = {
"how-we-make-money.html": ("How We Make Money", "Transparent disclosure of how 247hrsCare earns revenue while staying free for families.", """
<p>247hrsCare is free for families. To keep it that way, we earn revenue in the following ways. None of them change what families pay a provider.</p>
<h2>1. Provider partnerships (lead generation)</h2><p>When you request a care match and consent to be contacted, we may share your request with up to three participating providers. Those providers may pay us a fee per inquiry, a monthly partnership fee, or a referral fee if you choose their services. We only share your information with your consent.</p>
<h2>2. Advertising</h2><p>We display advertising, including Google AdSense, and clearly labelled sponsorships. Advertisers do not control our editorial content.</p>
<h2>3. Video</h2><p>We publish videos on YouTube and may earn revenue from YouTube advertising and sponsored segments, which are always disclosed.</p>
<h2>4. Affiliate links</h2><p>Some product recommendations may contain affiliate links. If you purchase through them, we may earn a commission at no extra cost to you. Affiliate links are disclosed where they appear.</p>
<h2>5. Job listings</h2><p>Employers may pay to feature caregiver job listings. Listings for caregivers are always free.</p>
<h2>6. Reader support</h2><p>Visitors may choose to donate. Donations fund operations, outreach, hiring content talent, and contests and prizes. 247hrsCare is not a registered charity; contributions are not tax-deductible.</p>
<h2>Our promise</h2><ul><li>Families never pay us.</li><li>We cap matches at three providers to prevent unwanted calls.</li><li>Sponsored content is always labelled.</li><li>Payment never buys a recommendation in our editorial guides.</li></ul>"""),
"privacy.html": ("Privacy Policy", "How 247hrsCare collects, uses and protects your personal information.", """
<p>This Privacy Policy explains how 247hrsCare.com ("247hrsCare", "we", "us") collects, uses and shares information when you use this website.</p>
<h2>Information we collect</h2><ul><li><b>Information you provide</b> through forms: name, email, phone, location, care needs, career details, contest entries, donation pledges and messages.</li><li><b>Automatically collected data</b> such as device, browser, pages visited and approximate location, collected through analytics and advertising cookies when you consent.</li><li><b>Local storage</b> on your device to remember preferences (theme, cookie choice, quiz result).</li></ul>
<h2>How we use information</h2><ul><li>To respond to your requests and provide care matching.</li><li>To share your care request with up to three providers <b>only with your consent</b>.</li><li>To process applications, contest entries, pledges and inquiries.</li><li>To send newsletters you subscribe to (unsubscribe anytime).</li><li>To operate, secure and improve the website, and to show advertising.</li></ul>
<h2>Health information</h2><p>If you describe care needs, you may share health-related information. We use it only to respond to your request and share it only with providers you consent to. 247hrsCare is not a healthcare provider or a covered entity under HIPAA; please share only what is needed.</p>
<h2>Form processing</h2><p>Form submissions are transmitted securely through a third-party form processing service (FormSubmit) and delivered to our team's inbox.</p>
<h2>Cookies &amp; advertising</h2><p>With your consent, we use Google Analytics and Google AdSense. Google and its partners may use cookies to serve ads based on your visits to this and other websites. You can opt out of personalised advertising at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>. You can change your cookie choice by clearing your browser's site data.</p>
<h2>Embedded content</h2><p>Videos are embedded using YouTube's privacy-enhanced mode and load only when you click play.</p>
<h2>Sharing</h2><p>We do not sell personal information. We share information with service providers (hosting, forms, analytics, advertising), with care providers you consent to, and when required by law.</p>
<h2>Your rights</h2><p>Depending on where you live (including under GDPR, UK GDPR, PIPEDA, Quebec Law 25 and U.S. state privacy laws such as the CCPA/CPRA), you may request access, correction, deletion or portability of your data, or opt out of certain processing. Submit requests via our <a href="{R}contact.html">contact form</a> ("Privacy request").</p>
<h2>Retention &amp; security</h2><p>We retain information only as long as needed for the purposes above. We use reasonable safeguards, but no online transmission is completely secure.</p>
<h2>Children</h2><p>This website is not directed to children under 16, and we do not knowingly collect their information.</p>
<h2>Changes</h2><p>We may update this policy and will revise the date above.</p>"""),
"terms.html": ("Terms of Use", "Terms governing use of the 247hrsCare.com website.", """
<p>By using 247hrsCare.com you agree to these Terms. If you do not agree, please do not use the website.</p>
<h2>Nature of the service</h2><p>247hrsCare provides general information, planning tools and a referral/matching service. We do not provide medical, nursing, legal or financial services, and we do not employ, supervise or control third-party providers. You are responsible for evaluating and selecting any provider.</p>
<h2>No emergency service</h2><p>This website is not for emergencies. Call 911 or your local emergency number.</p>
<h2>Accuracy</h2><p>We work to keep information accurate and current, but make no warranties about completeness or suitability. Costs and programme rules change.</p>
<h2>User submissions</h2><p>You agree to submit accurate information and not to submit unlawful, infringing or harmful content. You grant us a licence to use submissions (e.g. contest entries, stories) as described where submitted.</p>
<h2>Intellectual property</h2><p>Site content, design, logo and code are owned by 247hrsCare.com or its licensors. See the <a href="{R}trademark.html">Trademark &amp; Copyright Disclosure</a>.</p>
<h2>Third-party links &amp; content</h2><p>We are not responsible for third-party websites, videos, products or services.</p>
<h2>Limitation of liability</h2><p>To the maximum extent permitted by law, 247hrsCare is not liable for indirect, incidental or consequential damages arising from use of the website or any third-party provider.</p>
<h2>Accessibility</h2><p>We aim to meet WCAG 2.1 AA. If you encounter a barrier, please tell us through the contact form.</p>
<h2>Changes &amp; governing law</h2><p>We may update these Terms at any time. Continued use means acceptance. These Terms are governed by applicable laws of the operator's jurisdiction, without regard to conflict-of-law rules.</p>"""),
"disclaimer.html": ("Medical & Professional Disclaimer", "247hrsCare provides general information only, not medical, legal or financial advice.", """
<div class="note warn"><b>If you think you or someone else may be having a medical emergency, call 911 or your local emergency number immediately.</b></div>
<h2>Not medical advice</h2><p>All content on 247hrsCare — including guides, quizzes, calculators and videos — is for general informational purposes only. It is not a substitute for professional medical advice, diagnosis or treatment. Always seek the advice of a physician or other qualified health provider with any questions about a medical condition.</p>
<h2>Not legal or financial advice</h2><p>Information about costs, insurance, Medicare, Medicaid, VA benefits and other programmes is general and may change. Consult a qualified elder law attorney, financial adviser or the programme directly.</p>
<h2>Tools are estimates</h2><p>The care needs quiz is not a clinical assessment. The cost calculator uses published national medians and your inputs; actual prices vary.</p>
<h2>Third-party providers</h2><p>247hrsCare does not provide care services and is not responsible for the acts or omissions of any provider. Verify licences, insurance and references before engaging any provider.</p>
<h2>Third-party videos</h2><p>Embedded videos are produced by third parties. Their inclusion is not an endorsement, and their creators are not affiliated with 247hrsCare.</p>"""),
"trademark.html": ("Trademark & Copyright Disclosure", "Trademark and copyright disclosure for 247hrsCare.com.", """
<h2>Name and domain</h2><p>"247hrsCare" and "247hrsCare.com" are used as the trade name and domain name of this independent website. "247hrsCare" is <b>not a registered trademark</b>; any use of ™ in future indicates an unregistered claim only. The name is formed from the common descriptive phrase "24/7 hours care".</p>
<h2>No affiliation</h2><p>247hrsCare.com is <b>not affiliated with, endorsed by, or sponsored by</b> any other business using similar names or descriptive phrases such as "24/7", "24 Hour Care", "24 Hour Home Care", "24/7 Home Care" or "24 Hrs Care", including any home care agency, franchise, staffing company or healthcare organisation in any country. Any resemblance to other names arises solely from the use of the generic, descriptive phrase for round-the-clock care.</p>
<h2>Third-party marks</h2><p>All third-party names, trademarks, service marks and logos mentioned on this site (including Google, AdSense, YouTube, Medicare, Medicaid, CareScout and the names of any organisations or programmes) are the property of their respective owners. Their mention is for identification and informational purposes only and does not imply endorsement or affiliation.</p>
<h2>Copyright</h2><p>© 2026 247hrsCare.com. All original text, page designs, the logo mark, graphics, tools and source code on this website are protected by copyright. You may share links and brief quotations with attribution. Reproduction, republication or scraping of substantial portions without written permission is prohibited.</p>
<h2>Original work &amp; licensed elements</h2><ul><li>All written content is original to 247hrsCare. Statistics are attributed to their sources (e.g. CareScout Cost of Care Survey 2025).</li><li>Icons and illustrations are original inline graphics created for this site.</li><li>Typography uses "Plus Jakarta Sans", licensed under the SIL Open Font License via Google Fonts.</li><li>Videos are embedded via YouTube's standard embed player under YouTube's Terms of Service and remain the property of their creators.</li></ul>
<h2>Copyright &amp; trademark complaints (DMCA)</h2><p>If you believe content on this site infringes your copyright or trademark, submit a notice via our <a href="{R}contact.html">contact form</a> (topic: "Copyright / trademark notice") including: identification of the work or mark, the URL of the material, your contact details, a good-faith statement, a statement of accuracy under penalty of perjury, and your signature. We will respond promptly and remove infringing material where appropriate.</p>
<h2>Domain, sponsorship and acquisition</h2><p>For inquiries about this website, the domain name, sponsorship, advertising or partnership, visit <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</p>"""),
}
