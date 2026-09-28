"""Core pages: home, lead gen, quiz, calculator, checklist, thank-you"""
from layout import *
from services import SERVICES
from guides import GUIDES

def home():
    svc_cards = "".join(f'''<a class="card reveal" href="{{R}}services/{s['slug']}.html"><div class="ic">{ic(s['icon'])}</div><h3>{e(s['name'])}</h3><p>{e(s['desc'][:118].rsplit(' ',1)[0])}…</p><span class="more">Explore →</span></a>''' for s in SERVICES)
    guide_cards = "".join(f'''<a class="card reveal" href="{{R}}guides/{g['slug']}.html" data-cat="{e(g['cat'])}"><span class="tag">{e(g['cat'])}</span><h3>{e(g['title'])}</h3><p>{e(g['desc'])}</p><span class="meta">{g['mins']} min read</span></a>''' for g in GUIDES[:6])
    body = f'''
<section class="hero">
 <div class="container hero-grid">
  <div>
   <span class="eyebrow"><i class="pulse"></i> Care guidance, 24 hours a day</span>
   <h1>Find trusted care — <span style="color:var(--brand)">day, night &amp; everything in between</span></h1>
   <p class="lead">Compare 24-hour home care, live-in care, overnight care, dementia care and senior living. Get honest costs, expert guides and free matching with vetted local providers.</p>
   <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:22px">
    <a class="btn btn-cta" href="{{R}}get-care.html">Get a free care match</a>
    <a class="btn btn-ghost" href="{{R}}care-quiz.html">{ic("quiz",20)} Take the 2-minute quiz</a>
   </div>
   <div class="trust-row"><span>{ic("check",18)} 100% free for families</span><span>{ic("check",18)} No obligation</span><span>{ic("check",18)} Independent guidance</span><span>{ic("check",18)} US, Canada &amp; global inquiries</span></div>
  </div>
  <div class="hero-card">
   <h2>What kind of care do you need?</h2>
   <form class="form" action="{{R}}get-care.html" method="get">
    <div class="choices">
     <label class="choice"><input type="radio" name="care_type" value="24-hour" checked><span>{ic("clock",20)} 24-hour care</span></label>
     <label class="choice"><input type="radio" name="care_type" value="overnight"><span>{ic("moon",20)} Overnight care</span></label>
     <label class="choice"><input type="radio" name="care_type" value="dementia"><span>{ic("brain",20)} Dementia care</span></label>
     <label class="choice"><input type="radio" name="care_type" value="personal"><span>{ic("hand",20)} Hourly help</span></label>
    </div>
    <div><label for="h-zip">ZIP / Postal code</label><input id="h-zip" name="zip" placeholder="e.g. 10001 or H2X 1Y4" required></div>
    <button class="btn btn-cta btn-block" type="submit">See my care options →</button>
    <p class="hint mb0">{ic("lock",14)} Private &amp; secure. We never sell your data to third parties without your consent.</p>
   </form>
  </div>
 </div>
</section>
{ad("home-top")}
<section style="padding-top:30px">
 <div class="container grid g4">
  <div class="stat reveal"><b>$<span data-count="35">35</span>/hr</b><span>U.S. median for in-home care (2025)</span></div>
  <div class="stat reveal"><b data-count="8">8</b><span>care types compared side by side</span></div>
  <div class="stat reveal"><b>24/7</b><span>access to tools, guides &amp; requests</span></div>
  <div class="stat reveal"><b>$0</b><span>cost to families for matching</span></div>
 </div>
</section>
<section class="section-alt" id="services">
 <div class="container">
  <div class="section-head"><span class="eyebrow">Care services</span><h2>Every level of care, explained clearly</h2><p>From a few hours of companionship to round-the-clock nursing support — understand the options, costs and trade-offs before you decide.</p></div>
  <div class="grid g4">{svc_cards}</div>
 </div>
</section>
<section>
 <div class="container">
  <div class="section-head"><span class="eyebrow">How it works</span><h2>From worried to organised in four steps</h2></div>
  <ol class="steps">
   <li class="reveal"><h3>Tell us the situation</h3><p class="muted mb0">Two minutes: who needs care, where, and how urgently.</p></li>
   <li class="reveal"><h3>Get a clear recommendation</h3><p class="muted mb0">Our quiz and advisors translate needs into the right level of care.</p></li>
   <li class="reveal"><h3>Compare vetted options</h3><p class="muted mb0">Up to three matched providers, with costs and questions to ask.</p></li>
   <li class="reveal"><h3>Start care with confidence</h3><p class="muted mb0">Checklists and follow-up so nothing gets missed in week one.</p></li>
  </ol>
  <div class="center mt"><a class="btn btn-cta" href="{{R}}get-care.html">Start my free care match</a></div>
 </div>
</section>
<section class="section-alt">
 <div class="container grid g2" style="align-items:center">
  <div class="reveal"><span class="eyebrow">Free tools</span><h2>Know the real cost before you call anyone</h2><p class="lead">Our calculator compares in-home care with assisted living and nursing homes using the latest national medians — adjusted for your schedule and region.</p>
   <ul class="checklist"><li>Hourly, overnight and 24-hour schedules</li><li>Low, average and high-cost regions</li><li>Instant monthly and annual totals</li></ul>
   <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px"><a class="btn btn-brand" href="{{R}}cost-calculator.html">{ic("calc",20)} Open the calculator</a><a class="btn btn-ghost" href="{{R}}checklist.html">{ic("download",20)} Free checklist</a></div></div>
  <div class="card reveal">
   <h3>Quick comparison (U.S. national medians)</h3>
   <div class="bars">
    <div class="bar"><span>In-home, 8 hrs/day</span><div class="track"><i style="width:33%"></i></div><b>$8,500/mo</b></div>
    <div class="bar"><span>Assisted living</span><div class="track"><i class="c2" style="width:24%"></i></div><b>$6,200/mo</b></div>
    <div class="bar"><span>Nursing home (private)</span><div class="track"><i class="c3" style="width:42%"></i></div><b>$10,800/mo</b></div>
    <div class="bar"><span>24-hour home care</span><div class="track"><i class="c4" style="width:100%"></i></div><b>$25,500/mo</b></div>
   </div>
   <p class="hint" style="margin-top:12px">Source: CareScout Cost of Care Survey 2025. Local prices vary.</p>
  </div>
 </div>
</section>
<section>
 <div class="container">
  <div class="section-head"><span class="eyebrow">Care guides</span><h2>Answers families search for at 2 a.m.</h2><p>Practical, plain-language guides on costs, planning, dementia, safety and caregiver wellbeing.</p></div>
  <div class="grid g3">{guide_cards}</div>
  <div class="center mt"><a class="btn btn-ghost" href="{{R}}guides/index.html">Browse all guides →</a></div>
 </div>
</section>
{ad("home-mid")}
<section class="section-alt">
 <div class="container">
  <div class="section-head"><span class="eyebrow">Video library</span><h2>Learn caregiving skills in minutes</h2><p>Short, practical videos on dementia communication, safe transfers and more.</p></div>
  <div class="grid g3" id="video-grid" data-limit="3"></div>
  <div class="center mt"><a class="btn btn-ghost" href="{{R}}videos.html">{ic("play",20)} Watch all videos</a> <a class="btn btn-brand yt-channel" href="#" target="_blank" rel="noopener">Subscribe on YouTube</a></div>
 </div>
</section>
<section>
 <div class="container grid g3">
  <a class="card reveal" href="{{R}}careers.html"><div class="ic coral">{ic("briefcase")}</div><h3>Caregiver careers</h3><p>Join our talent network for home care, overnight and live-in roles — or apply to join the 247hrsCare team.</p><span class="more">Apply now →</span></a>
  <a class="card reveal" href="{{R}}contests.html"><div class="ic gold">{ic("trophy")}</div><h3>Caregiver Hero Awards</h3><p>Nominate a caregiver who goes above and beyond. Winners receive prizes and are featured on our site and channel.</p><span class="more">Nominate someone →</span></a>
  <a class="card reveal" href="{{R}}donate.html"><div class="ic">{ic("heart")}</div><h3>Support our mission</h3><p>Help keep care guidance free for every family. Your support funds tools, outreach, talent and caregiver prizes.</p><span class="more">Give today →</span></a>
 </div>
</section>
<section class="section-alt">
 <div class="container grid g2" style="align-items:center">
  <div class="reveal"><span class="eyebrow">For care providers</span><h2>Reach families actively looking for care</h2><p class="lead">Home care agencies, senior living communities and care-tech brands: receive qualified inquiries, featured placement and sponsorship opportunities.</p>
   <div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-brand" href="{{R}}providers.html">List your agency</a><a class="btn btn-ghost" href="{{R}}advertise.html">Advertising packages</a></div></div>
  <div class="grid g2">
   <div class="card reveal"><div class="ic">{ic("users")}</div><h3>Qualified leads</h3><p class="mb0">Families with verified needs, location and timeline.</p></div>
   <div class="card reveal"><div class="ic coral">{ic("megaphone")}</div><h3>Sponsorships</h3><p class="mb0">Guides, videos, newsletter and contest prizes.</p></div>
   <div class="card reveal"><div class="ic gold">{ic("star")}</div><h3>Featured listings</h3><p class="mb0">Priority placement on service pages.</p></div>
   <div class="card reveal"><div class="ic">{ic("handshake")}</div><h3>Partnerships</h3><p class="mb0">Co-branded tools and content.</p></div>
  </div>
 </div>
</section>
{cta_band()}
<section style="padding-top:0">
 <div class="container" style="max-width:860px">
  <div class="section-head"><h2>Frequently asked questions</h2></div>
  {faq_html(HOME_FAQ)}
 </div>
</section>
'''
    return page("index.html", "247hrsCare — 24/7 Home Care, Live-In & Dementia Care Guidance",
        "Compare 24-hour home care, live-in, overnight and dementia care. Real costs, expert guides, free care-needs quiz and free matching with vetted providers.",
        body, [faq_schema(HOME_FAQ), {"@context":"https://schema.org","@type":"WebSite","name":"247hrsCare","url":SITE_URL+"/"}])

HOME_FAQ = [
 ("Is 247hrsCare a home care agency?","No. 247hrsCare is an independent information and care-matching service. We help families understand options and connect with third-party providers, who deliver the care."),
 ("Is the care match really free?","Yes. Families never pay us. We may receive fees from providers or advertisers — explained openly on our How We Make Money page."),
 ("How quickly will someone contact me?","We aim to respond within one business day, and faster for urgent requests. For emergencies, always call 911 or your local emergency number."),
 ("Do you serve my area?","Our guides and tools are available everywhere. Provider matching is focused on the United States and Canada, and we accept inquiries from other countries."),
 ("How much does 24-hour care cost?","In the U.S., non-medical in-home care has a national median of about $35/hour (CareScout 2025), so 24 hours a day costs roughly $25,000+ per month. Live-in care and residential care can cost less — use our calculator."),
]

def get_care():
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Free Care Match")])}
 <span class="eyebrow"><i class="pulse"></i> Free · 2 minutes · No obligation</span>
 <h1>Get matched with the right care</h1>
 <p class="lead">Answer a few questions. A care advisor reviews your request and connects you with up to three vetted providers that fit your needs, schedule and budget.</p>
</div></section>
<section style="padding-top:10px"><div class="container lead-wrap">
 <div class="card" style="padding:28px">
 <form class="form msf" id="care-match" data-form data-subject="NEW CARE LEAD — 247hrsCare" data-redirect="thank-you.html">
  <div class="progress" aria-hidden="true"><i></i></div>
  <div class="step-count" aria-live="polite"></div>
  <input type="hidden" name="form" value="care-match"><input type="hidden" name="quiz_result" value="">{HP}
  <div class="step"><h2 style="font-size:1.4rem">Who needs care?</h2>
   <div class="choices auto">
    <label class="choice"><input type="radio" name="recipient" value="Parent" required><span>My parent</span></label>
    <label class="choice"><input type="radio" name="recipient" value="Spouse / partner"><span>My spouse / partner</span></label>
    <label class="choice"><input type="radio" name="recipient" value="Myself"><span>Myself</span></label>
    <label class="choice"><input type="radio" name="recipient" value="Grandparent"><span>Grandparent</span></label>
    <label class="choice"><input type="radio" name="recipient" value="Other relative / friend"><span>Other relative / friend</span></label>
    <label class="choice"><input type="radio" name="recipient" value="Client / patient (professional)"><span>A client (I'm a professional)</span></label>
   </div></div>
  <div class="step"><h2 style="font-size:1.4rem">What type of care?</h2>
   <div class="choices auto">
    <label class="choice"><input type="radio" name="care_type" value="24-hour" required><span>{ic("clock",20)} 24-hour care</span></label>
    <label class="choice"><input type="radio" name="care_type" value="live-in"><span>{ic("home",20)} Live-in care</span></label>
    <label class="choice"><input type="radio" name="care_type" value="overnight"><span>{ic("moon",20)} Overnight care</span></label>
    <label class="choice"><input type="radio" name="care_type" value="dementia"><span>{ic("brain",20)} Dementia / memory care</span></label>
    <label class="choice"><input type="radio" name="care_type" value="personal"><span>{ic("hand",20)} Hourly personal / companion</span></label>
    <label class="choice"><input type="radio" name="care_type" value="post-hospital"><span>{ic("hospital",20)} After hospital / respite</span></label>
    <label class="choice"><input type="radio" name="care_type" value="assisted-living"><span>{ic("building",20)} Assisted living / community</span></label>
    <label class="choice"><input type="radio" name="care_type" value="not-sure"><span>{ic("quiz",20)} Not sure yet</span></label>
   </div></div>
  <div class="step"><h2 style="font-size:1.4rem">Timing &amp; schedule</h2>
   <div class="form">
    <div><label for="gc-when">When do you need care to start?</label><select id="gc-when" name="timeline" required><option value="">Select…</option><option>Immediately (within 48 hours)</option><option>Within 2 weeks</option><option>Within 1–3 months</option><option>Just researching</option></select></div>
    <div><label for="gc-hours">Estimated hours of care</label><select id="gc-hours" name="hours" required><option value="">Select…</option><option>Under 20 hours / week</option><option>20–40 hours / week</option><option>40+ hours / week</option><option>Overnights only</option><option>24/7 or live-in</option><option>Not sure</option></select></div>
    <div><label>Current situation (select all that apply)</label>
     <div class="choices">
      <label class="choice"><input type="checkbox" name="needs" value="Mobility / falls"><span>Mobility / fall risk</span></label>
      <label class="choice"><input type="checkbox" name="needs" value="Memory loss"><span>Memory loss</span></label>
      <label class="choice"><input type="checkbox" name="needs" value="Bathing / dressing"><span>Bathing / dressing</span></label>
      <label class="choice"><input type="checkbox" name="needs" value="Medication help"><span>Medication help</span></label>
      <label class="choice"><input type="checkbox" name="needs" value="In hospital now"><span>In hospital now</span></label>
      <label class="choice"><input type="checkbox" name="needs" value="Lives alone"><span>Lives alone</span></label>
     </div></div>
   </div></div>
  <div class="step"><h2 style="font-size:1.4rem">Location &amp; budget</h2>
   <div class="form">
    <div class="row2"><div><label for="gc-zip">ZIP / Postal code</label><input id="gc-zip" name="zip" required autocomplete="postal-code"></div>
    <div><label for="gc-city">City</label><input id="gc-city" name="city" autocomplete="address-level2"></div></div>
    <div><label for="gc-country">Country</label><select id="gc-country" name="country" required><option>United States</option><option>Canada</option><option>United Kingdom</option><option>India</option><option>Australia</option><option>Other</option></select></div>
    <div><label for="gc-pay">How will care be paid for?</label><select id="gc-pay" name="payment" required><option value="">Select…</option><option>Private pay / savings</option><option>Long-term care insurance</option><option>Veterans benefits</option><option>Medicaid / government programme</option><option>Combination</option><option>Not sure — need guidance</option></select></div>
    <div><label for="gc-budget">Monthly budget (optional)</label><select id="gc-budget" name="budget"><option value="">Prefer not to say</option><option>Under $2,000</option><option>$2,000–$5,000</option><option>$5,000–$10,000</option><option>$10,000+</option></select></div>
   </div></div>
  <div class="step"><h2 style="font-size:1.4rem">Where should we send your matches?</h2>
   <div class="form">
    <div class="row2"><div><label for="gc-fn">First name</label><input id="gc-fn" name="first_name" required autocomplete="given-name"></div>
    <div><label for="gc-ln">Last name</label><input id="gc-ln" name="last_name" required autocomplete="family-name"></div></div>
    <div class="row2"><div><label for="gc-ph">Phone</label><input id="gc-ph" type="tel" name="phone" required autocomplete="tel"></div>
    <div><label for="gc-em">Email</label><input id="gc-em" type="email" name="email" required autocomplete="email"></div></div>
    <div><label for="gc-best">Best time to reach you</label><select id="gc-best" name="best_time"><option>Any time</option><option>Morning</option><option>Afternoon</option><option>Evening</option></select></div>
    <div><label for="gc-notes">Anything else we should know? (optional)</label><textarea id="gc-notes" name="notes" placeholder="e.g. diagnosis, languages spoken, pets in the home, preferred caregiver gender"></textarea></div>
    {CONSENT}
   </div></div>
  <div class="step-nav"><button type="button" class="btn btn-ghost prev">← Back</button><button type="button" class="btn btn-brand next">Continue →</button><button type="submit" class="btn btn-cta">Get my free matches</button></div>
  <div class="form-msg" role="status"></div>
 </form>
 </div>
 <aside class="aside-sticky">
  <div class="card"><h3>Why families use 247hrsCare</h3><ul class="checklist"><li>Free, independent guidance</li><li>Up to 3 vetted provider matches — not 30 calls</li><li>Transparent: we explain how we're paid</li><li>Your details shared only with your consent</li><li>Help with costs, benefits and next steps</li></ul></div>
  <div class="card" style="margin-top:18px"><h3>{ic("shield",20)} Your privacy</h3><p class="mb0">We use your information only to respond to your request. Read our <a href="{{R}}privacy.html">Privacy Policy</a>.</p></div>
  <div class="card" style="margin-top:18px"><h3>Prefer to explore first?</h3><p><a href="{{R}}care-quiz.html">Take the care needs quiz</a> or <a href="{{R}}cost-calculator.html">estimate costs</a>.</p><p class="mb0 hint">Emergency? Call 911 or your local emergency number.</p></div>
 </aside>
</div></section>'''
    return page("get-care.html","Free Care Match — Get Matched With Vetted Caregivers",
        "Tell us about your care needs and get matched with up to three vetted home care, live-in, overnight or dementia care providers. Free, no obligation.", body)

QUIZ = [
 ("q1","How much help is needed with bathing, dressing or toileting?",[("None","companion:2"),("Some help","personal:2"),("Full help","personal:2,h24:1"),("Full help plus incontinence care","h24:2,personal:1")]),
 ("q2","How is memory and thinking?",[("No concerns","companion:1"),("Mild forgetfulness","companion:1,personal:1"),("Diagnosed dementia, mostly settled","memory:2"),("Wandering, confusion or agitation","memory:3,h24:1")]),
 ("q3","What happens at night?",[("Sleeps through","companion:1"),("Up once, manages alone","personal:1"),("Needs help once a night","personal:1,h24:1"),("Needs help several times a night","h24:3")]),
 ("q4","Falls in the last six months?",[("None","companion:1"),("One","personal:1"),("Two or more","h24:2"),("Can't get up without help","h24:2,personal:1")]),
 ("q5","Medical needs?",[("None beyond routine","companion:1"),("Medication reminders","personal:1"),("Wound care, injections or catheter","skilled:3"),("Frequent hospital visits","skilled:2,h24:1")]),
 ("q6","Can they be safely left alone?",[("Yes, all day","companion:2"),("A few hours","personal:2"),("Only briefly","h24:1,memory:1"),("No, never","h24:3")]),
 ("q7","Who helps now?",[("Nobody — they live alone","personal:1,companion:1"),("Family, a few hours a week","personal:1"),("Family, daily and exhausted","h24:1,personal:1"),("Family, 24/7 and burning out","h24:2")]),
 ("q8","What matters most?",[("Staying at home","personal:1,h24:1"),("Social life and activities","companion:1,memory:1"),("Medical oversight","skilled:2"),("Lowest total cost","companion:1")]),
]

def quiz():
    qs = ""
    for n,(name,q,opts) in enumerate(QUIZ):
        o = "".join(f'<label class="choice"><input type="radio" name="{name}" value="{e(t)}" data-w="{w}" {"required" if k==0 else ""}><span>{e(t)}</span></label>' for k,(t,w) in enumerate(opts))
        qs += f'<fieldset class="card" style="border:1px solid var(--line);margin:0 0 16px"><legend class="tag" style="margin:0">Question {n+1} of {len(QUIZ)}</legend><h3>{e(q)}</h3><div class="choices">{o}</div></fieldset>'
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Care Needs Quiz")])}
 <span class="eyebrow">Free · 2 minutes · Instant result</span>
 <h1>Care Needs Quiz: what level of care is right?</h1>
 <p class="lead">Eight questions based on the factors care professionals use — daily activities, memory, nights, falls and medical needs. You'll get an instant recommendation and next steps.</p>
</div></section>
<section style="padding-top:10px"><div class="container" style="max-width:860px">
 <form id="quiz">{qs}<button class="btn btn-cta btn-block" type="submit">See my recommendation</button></form>
 <div class="quiz-result card" style="margin-top:24px;border:2px solid var(--brand)" aria-live="polite">
  <span class="tag">Your recommendation</span><h2 id="qr-title"></h2><p id="qr-text" class="lead"></p>
  <div style="display:flex;gap:10px;flex-wrap:wrap"><a id="qr-cta" class="btn btn-cta" href="{{R}}get-care.html">Get matched for this care</a><a class="btn btn-ghost" href="{{R}}cost-calculator.html">Estimate the cost</a></div>
  <p class="hint" style="margin-top:14px">This quiz is educational and not a clinical assessment. Discuss care needs with a physician or care professional.</p>
 </div>
</div></section>
{ad("quiz")}'''
    return page("care-quiz.html","Care Needs Quiz — Which Level of Care Is Right?",
        "Free 8-question care needs quiz: find out whether companion care, personal care, 24-hour care, dementia care or skilled nursing fits best.", body)

def calculator():
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Care Cost Calculator")])}
 <span class="eyebrow">Updated with 2025 national medians</span>
 <h1>Care Cost Calculator</h1>
 <p class="lead">Estimate the monthly and annual cost of in-home care for your schedule, then compare it with assisted living and nursing homes.</p>
</div></section>
<section style="padding-top:10px"><div class="container lead-wrap">
 <div class="card" id="calc">
  <div class="form">
   <div><label for="c-hours">Hours of care per day: <b id="c-hours-v">8</b></label><input id="c-hours" type="range" min="2" max="24" value="8"></div>
   <div><label for="c-days">Days per week: <b id="c-days-v">7</b></label><input id="c-days" type="range" min="1" max="7" value="7"></div>
   <div><label for="c-rate">Hourly rate: <b id="c-rate-v">$35</b></label><input id="c-rate" type="range" min="18" max="60" value="35"><span class="hint">U.S. national median ≈ $35/hr (CareScout 2025). Adjust to local quotes.</span></div>
   <div><label for="c-region">Region cost level</label><select id="c-region"><option value="0.8">Lower-cost area (−20%)</option><option value="1" selected>Average</option><option value="1.25">Higher-cost area (+25%)</option><option value="1.45">Major metro (+45%)</option></select></div>
  </div>
  <hr>
  <div class="result-box" aria-live="polite">
   <div class="grid g2"><div><span class="muted">Estimated monthly</span><div class="big-num" id="c-month">—</div></div><div><span class="muted">Estimated annual</span><div class="big-num" id="c-year" style="color:var(--accent)">—</div></div></div>
   <div class="bars" id="c-bars"></div>
   <p id="c-tip" style="margin:14px 0 0;font-weight:600"></p>
  </div>
  <p class="hint" style="margin-top:12px">Estimates only. Assisted living $6,200/mo and nursing home $315/$355 per day are U.S. national medians (CareScout Cost of Care Survey 2025), scaled by the region setting.</p>
 </div>
 <aside class="aside-sticky">{mini_lead("", "Get real local quotes — free")}</aside>
</div></section>
{ad("calc")}
{cta_band("Want help paying for care?","Our guide covers long-term care insurance, VA benefits, Medicaid waivers and more.")}'''
    return page("cost-calculator.html","Care Cost Calculator — In-Home vs Assisted Living vs Nursing Home",
        "Free care cost calculator: estimate in-home, overnight and 24-hour care costs and compare with assisted living and nursing homes using 2025 medians.", body)

CHECK = [("Assess needs",["List daily tasks that are unsafe or not getting done","Note night-time needs and how often","Record falls, hospital visits and medication changes","Ask the doctor for a functional assessment","Take the 247hrsCare care needs quiz"]),
 ("Budget & benefits",["Estimate hours per week needed","Run the cost calculator for 3 scenarios","Check long-term care insurance policy terms","Check VA, Medicaid or provincial programme eligibility","Agree on family financial contributions in writing"]),
 ("Vet providers",["Verify licence and insurance","Ask about background checks and training","Ask about dementia training if relevant","Confirm backup coverage for sick days","Get all rates and minimums in writing","Read the contract cancellation terms","Check online reviews and inspection reports","Ask for 2 client references"]),
 ("Prepare the home",["Clear walkways and add night-lights","Install grab bars and a shower chair","Set up a medication organiser","Create a care binder: contacts, meds, routines","Arrange a caregiver space (for live-in care)"]),
 ("First week",["Meet the caregiver before the first shift","Walk through routines and preferences","Share emergency contacts and plans","Review shift notes daily","Schedule a 2-week care plan review"])]

def checklist():
    blocks = "".join(f'<div class="card reveal"><h3>{e(h)}</h3><ul class="checklist">{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>' for h, items in CHECK)
    body = f'''
<section class="page-hero"><div class="container">
 {crumbs([("{R}index.html","Home"),(None,"Care Planning Checklist")])}
 <span class="eyebrow">Free resource</span>
 <h1>The 24/7 Care Planning Checklist</h1>
 <p class="lead">Everything to check — from assessing needs to the first week of care. Print it, share it with family, and tick it off together.</p>
 <div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn btn-brand" onclick="window.print()">{ic("download",20)} Print / save as PDF</button><button class="btn btn-ghost share">Share with family</button></div>
</div></section>
<section style="padding-top:10px"><div class="container grid g2">{blocks}
 <div class="card"><h3>Get the checklist by email</h3><p>Plus our weekly Care Brief with new guides and tools.</p>
  <form class="form" data-form data-subject="Checklist request" data-success="Sent! Check your inbox shortly."><input type="hidden" name="form" value="checklist-email">{HP}
   <input name="name" placeholder="First name" required aria-label="First name"><input type="email" name="email" placeholder="Email" required aria-label="Email">
   <button class="btn btn-cta" type="submit">Email me the checklist</button><div class="form-msg" role="status"></div></form></div>
</div></section>
{ad("checklist")}'''
    return page("checklist.html","Free 24/7 Care Planning Checklist (Printable)",
        "Free printable care planning checklist: assess needs, budget, vet home care agencies, prepare the home and manage the first week of care.", body)

def thank_you():
    body = f'''
<section class="page-hero"><div class="container" style="max-width:820px;text-align:center">
 <div class="ic" style="margin:0 auto 16px;width:72px;height:72px;background:#e3f6ec;color:var(--ok)">{ic("check",36,3)}</div>
 <h1>Thank you — your request is in</h1>
 <p class="lead" style="margin:0 auto">A care advisor will review your details and contact you, usually within one business day. Urgent requests are prioritised.</p>
</div></section>
<section style="padding-top:0"><div class="container grid g3">
 <a class="card" href="{{R}}checklist.html"><div class="ic">{ic("download")}</div><h3>1. Get organised</h3><p class="mb0">Use the care planning checklist while you wait.</p></a>
 <a class="card" href="{{R}}guides/choosing-a-home-care-agency.html"><div class="ic coral">{ic("quiz")}</div><h3>2. Prepare your questions</h3><p class="mb0">25 questions to ask every provider.</p></a>
 <a class="card" href="{{R}}cost-calculator.html"><div class="ic gold">{ic("calc")}</div><h3>3. Know your numbers</h3><p class="mb0">Estimate costs before the first call.</p></a>
</div>
<div class="container center mt"><p>Know someone else who needs help? <button class="btn btn-ghost btn-sm share">Share 247hrsCare</button> · <a href="{{R}}donate.html">Support our free service</a></p></div></section>'''
    return page("thank-you.html","Thank You","Your request has been received.", body).replace('content="index,follow,max-image-preview:large"','content="noindex"')

def not_found():
    body = f'''<section class="page-hero"><div class="container center" style="max-width:720px"><h1>Page not found</h1><p class="lead" style="margin:0 auto 20px">The page you're looking for has moved or doesn't exist.</p>
<div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap"><a class="btn btn-cta" href="get-care.html">Get a free care match</a><a class="btn btn-ghost" href="guides/index.html">Browse guides</a></div></div></section>'''
    return page("404.html","Page Not Found","Page not found.", body)
