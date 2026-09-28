/* 247hrsCare.com — site behaviour (vanilla JS, no dependencies) */
(function () {
  "use strict";
  var C = window.SITE_CONFIG || {};
  var ROOT = document.body.getAttribute("data-root") || "";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    sget: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    sset: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  };
  function inbox() { return (C.inbox || []).map(function (c) { return String.fromCharCode(c ^ 23); }).join(""); }
  function endpoint() { return "https://formsubmit.co/ajax/" + (C.formsubmitAlias || inbox()); }

  /* Theme */
  var saved = store.get("theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  $$(".theme-toggle").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme");
      if (!cur) cur = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
      var next = cur === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next); store.set("theme", next);
    });
  });

  /* Mobile menu */
  var menu = $(".menu"), scrim = $(".scrim");
  function closeMenu() { if (menu) menu.classList.remove("open"); if (scrim) scrim.classList.remove("show"); }
  $$(".burger").forEach(function (b) {
    b.addEventListener("click", function () {
      var o = menu.classList.toggle("open"); scrim.classList.toggle("show", o); b.setAttribute("aria-expanded", o);
    });
  });
  if (scrim) scrim.addEventListener("click", closeMenu);
  $$(".menu button.dd").forEach(function (b) {
    b.addEventListener("click", function () {
      var li = b.parentNode, o = li.classList.toggle("open"); b.setAttribute("aria-expanded", o);
    });
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeMenu(); closeModals(); } });

  /* Hidden email links: address is assembled only at click time and never written into the page */
  $$(".js-mail").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var subj = a.getAttribute("data-subject") || "Inquiry from 247hrsCare.com";
      window.location.href = "mailto:" + inbox() + "?subject=" + encodeURIComponent(subj);
    });
  });

  /* Prefill fields from URL (?type=dementia&zip=...) and from quiz result */
  var params = new URLSearchParams(location.search);
  params.forEach(function (v, k) {
    $$('[name="' + k + '"]').forEach(function (el) {
      if (el.type === "radio" || el.type === "checkbox") { if (el.value === v) el.checked = true; }
      else el.value = v;
    });
  });
  var quizRec = store.sget("quizRec");
  if (quizRec) $$('[name="quiz_result"]').forEach(function (el) { el.value = quizRec; });

  /* Form submission (FormSubmit AJAX) */
  function serialize(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) {
      if (data[k]) data[k] = data[k] + ", " + v; else data[k] = v;
    });
    return data;
  }
  function submitForm(form) {
    var msg = $(".form-msg", form);
    var btn = $('[type="submit"]', form);
    if (form._honey && form._honey.value) return;
    var data = serialize(form);
    data._subject = form.getAttribute("data-subject") || "New submission — 247hrsCare.com";
    data._template = "table";
    data._captcha = "false";
    data.page = location.pathname;
    data.submitted_at = new Date().toISOString();
    if (btn) { btn.disabled = true; btn.dataset.label = btn.innerHTML; btn.innerHTML = "Sending…"; }
    fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (res) {
        if (!res.ok || res.j.success === "false") throw new Error(res.j.message || "Submission failed");
        if (window.gtag) window.gtag("event", "generate_lead", { form: form.id || data._subject });
        var redirect = form.getAttribute("data-redirect");
        if (redirect) { location.href = ROOT + redirect; return; }
        if (msg) { msg.className = "form-msg ok"; msg.textContent = form.getAttribute("data-success") || "Thank you — we received your message and will reply shortly."; }
        form.reset();
      })
      .catch(function () {
        if (msg) { msg.className = "form-msg err"; msg.innerHTML = 'Sorry, something went wrong. Please try again, or <a href="#" class="js-mail-inline">email us</a>.'; 
          var a = $(".js-mail-inline", msg); if (a) a.addEventListener("click", function (e) { e.preventDefault(); location.href = "mailto:" + inbox(); }); }
      })
      .then(function () { if (btn) { btn.disabled = false; btn.innerHTML = btn.dataset.label; } });
  }
  $$("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      submitForm(form);
    });
  });

  /* Multi-step forms */
  $$(".msf").forEach(function (form) {
    var steps = $$(".step", form), i = 0, bar = $(".progress i", form), cnt = $(".step-count", form);
    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle("active", k === n); });
      if (bar) bar.style.width = ((n + 1) / steps.length * 100) + "%";
      if (cnt) cnt.textContent = "Step " + (n + 1) + " of " + steps.length;
      $$(".prev", form).forEach(function (b) { b.style.visibility = n === 0 ? "hidden" : "visible"; });
      $$(".next", form).forEach(function (b) { b.style.display = n === steps.length - 1 ? "none" : ""; });
      $$('[type="submit"]', form).forEach(function (b) { b.style.display = n === steps.length - 1 ? "" : "none"; });
      i = n;
    }
    function valid() {
      var ok = true;
      $$("input,select,textarea", steps[i]).forEach(function (el) {
        if (ok && !el.checkValidity()) { el.reportValidity(); ok = false; }
      });
      return ok;
    }
    $$(".next", form).forEach(function (b) { b.addEventListener("click", function () { if (valid()) { show(Math.min(i + 1, steps.length - 1)); form.scrollIntoView({ behavior: "smooth", block: "start" }); } }); });
    $$(".prev", form).forEach(function (b) { b.addEventListener("click", function () { show(Math.max(i - 1, 0)); }); });
    $$('.step .choices.auto input[type="radio"]', form).forEach(function (r) {
      r.addEventListener("change", function () { setTimeout(function () { if (i < steps.length - 1) show(i + 1); }, 220); });
    });
    show(0);
  });

  /* Quiz */
  var quiz = $("#quiz");
  if (quiz) {
    quiz.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!quiz.checkValidity()) { quiz.reportValidity(); return; }
      var s = { companion: 0, personal: 0, h24: 0, memory: 0, skilled: 0 };
      $$("input:checked", quiz).forEach(function (el) {
        (el.getAttribute("data-w") || "").split(",").forEach(function (p) {
          var kv = p.split(":"); if (kv[0] && s.hasOwnProperty(kv[0])) s[kv[0]] += parseFloat(kv[1] || 1);
        });
      });
      var best = Object.keys(s).sort(function (a, b) { return s[b] - s[a]; })[0];
      var R = {
        companion: ["Companion & homemaker care", "A few hours a day of companionship, errands, meals and light housekeeping is likely the right starting point.", "companion"],
        personal: ["Personal care at home", "Hands-on help with bathing, dressing, toileting and mobility on a scheduled basis (typically 4–12 hours a day).", "personal"],
        h24: ["24-hour or live-in care", "Round-the-clock supervision is indicated. Compare live-in care (one caregiver with sleep breaks) with 24-hour shift care (2–3 awake caregivers).", "24-hour"],
        memory: ["Specialized dementia & memory care", "Dementia-trained caregivers at home or a secure memory care community will provide the safest support.", "dementia"],
        skilled: ["Skilled nursing support", "Medical needs such as wound care, injections or complex medications suggest licensed nursing (home health or skilled nursing).", "skilled"]
      };
      var r = R[best];
      $("#qr-title").textContent = r[0];
      $("#qr-text").textContent = r[1];
      $("#qr-cta").setAttribute("href", ROOT + "get-care.html?care_type=" + encodeURIComponent(r[2]));
      store.sset("quizRec", r[0]);
      var box = $(".quiz-result"); box.classList.add("show"); box.scrollIntoView({ behavior: "smooth" });
    });
  }

  /* Cost calculator — medians: CareScout Cost of Care Survey 2025 (US national) */
  var calc = $("#calc");
  if (calc) {
    var fmt = function (n) { return "$" + Math.round(n).toLocaleString("en-US"); };
    function run() {
      var hrs = +$("#c-hours").value, days = +$("#c-days").value, rate = +$("#c-rate").value, idx = +$("#c-region").value;
      $("#c-hours-v").textContent = hrs; $("#c-days-v").textContent = days; $("#c-rate-v").textContent = "$" + rate;
      var r = rate * idx;
      var home = r * hrs * days * 4.33;
      var al = 6200 * idx, nhs = 315 * 30.42 * idx, nhp = 355 * 30.42 * idx;
      $("#c-month").textContent = fmt(home);
      $("#c-year").textContent = fmt(home * 12);
      var rows = [["In-home care (your plan)", home], ["Assisted living", al], ["Nursing home (semi-private)", nhs], ["Nursing home (private)", nhp]];
      var max = Math.max.apply(null, rows.map(function (x) { return x[1]; }));
      $("#c-bars").innerHTML = rows.map(function (x, k) {
        return '<div class="bar"><span>' + x[0] + '</span><div class="track"><i class="c' + (k + 1) + '" style="width:' + (x[1] / max * 100) + '%"></i></div><b>' + fmt(x[1]) + '/mo</b></div>';
      }).join("");
      var tip = $("#c-tip");
      if (tip) tip.textContent = home > al ? "At this schedule, a residential option may cost less than care at home — worth comparing." : "At this schedule, in-home care costs less than assisted living on average.";
    }
    $$("input,select", calc).forEach(function (el) { el.addEventListener("input", run); });
    run();
  }

  /* Video lite-embeds */
  function videoEl(v) {
    var d = document.createElement("div");
    d.className = "video"; d.setAttribute("data-id", v.id); d.setAttribute("role", "button"); d.tabIndex = 0;
    d.setAttribute("aria-label", "Play video: " + v.title);
    d.innerHTML = '<img loading="lazy" src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg" alt=""><span class="play"><i><svg width="22" height="22" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg></i></span>';
    return d;
  }
  var vg = $("#video-grid");
  if (vg && C.videos) {
    var limit = +(vg.getAttribute("data-limit") || 99);
    C.videos.slice(0, limit).forEach(function (v) {
      var card = document.createElement("div"); card.className = "card"; card.setAttribute("data-cat", v.cat);
      card.appendChild(videoEl(v));
      var h = document.createElement("h3"); h.style.marginTop = "14px"; h.style.fontSize = "1.05rem"; h.textContent = v.title;
      var t = document.createElement("span"); t.className = "tag"; t.textContent = v.cat;
      card.appendChild(h); card.insertBefore(t, h);
      vg.appendChild(card);
    });
  }
  document.addEventListener("click", function (e) {
    var v = e.target.closest && e.target.closest(".video[data-id]");
    if (v && !v.querySelector("iframe")) {
      v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + v.getAttribute("data-id") + '?autoplay=1&rel=0" title="YouTube video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
    }
  });
  document.addEventListener("keydown", function (e) {
    if ((e.key === "Enter" || e.key === " ") && e.target.classList && e.target.classList.contains("video")) { e.preventDefault(); e.target.click(); }
  });
  $$(".yt-channel").forEach(function (a) { a.href = C.youtubeChannel || "https://www.youtube.com/"; });

  /* Ad slots: AdSense when configured + consented; otherwise a house ad that sells the space */
  var consent = store.get("consent");
  function loadAds() {
    var slots = $$(".ad-slot");
    if (!slots.length) return;
    if (C.adsenseClient && consent === "all") {
      var s = document.createElement("script"); s.async = true; s.crossOrigin = "anonymous";
      s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient;
      document.head.appendChild(s);
      slots.forEach(function (el) {
        el.innerHTML = '<span class="ad-label">Advertisement</span><ins class="adsbygoogle" style="display:block;width:100%" data-ad-client="' + C.adsenseClient + '" data-ad-slot="' + ((C.adsenseSlots || {})[el.getAttribute("data-slot")] || (C.adsenseSlots || {}).default || "") + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
        try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
      });
    } else {
      slots.forEach(function (el) {
        el.innerHTML = '<div class="house-ad"><span class="ad-label">Sponsored</span><p><b>Reach families searching for care 24/7.</b> Your agency, product or brand could be featured here.</p><a class="btn btn-brand btn-sm" href="' + ROOT + 'advertise.html">Advertise with us</a></div>';
      });
    }
  }
  function loadGA() {
    if (!C.ga4 || consent !== "all") return;
    var s = document.createElement("script"); s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + C.ga4; document.head.appendChild(s);
    window.dataLayer = window.dataLayer || []; window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date()); window.gtag("config", C.ga4);
  }
  var cookie = $(".cookie");
  if (cookie && !consent) cookie.classList.add("show");
  $$("[data-consent]").forEach(function (b) {
    b.addEventListener("click", function () {
      consent = b.getAttribute("data-consent"); store.set("consent", consent); cookie.classList.remove("show"); loadAds(); loadGA();
    });
  });
  loadAds(); loadGA();

  /* Modals */
  function closeModals() { $$(".modal").forEach(function (m) { m.classList.remove("show"); }); }
  $$("[data-open]").forEach(function (b) {
    b.addEventListener("click", function (e) { e.preventDefault(); var m = $("#" + b.getAttribute("data-open")); if (m) m.classList.add("show"); });
  });
  $$(".modal").forEach(function (m) {
    m.addEventListener("click", function (e) { if (e.target === m || e.target.closest(".modal-x")) m.classList.remove("show"); });
  });
  /* Exit-intent lead magnet (desktop, once per session) */
  var exitM = $("#exit-modal");
  if (exitM && !store.sget("exitShown") && !$(".msf")) {
    document.addEventListener("mouseout", function h(e) {
      if (!e.relatedTarget && e.clientY < 8) { exitM.classList.add("show"); store.sset("exitShown", "1"); document.removeEventListener("mouseout", h); }
    });
  }

  /* Reveal + counters */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (en) {
      if (!en.isIntersecting) return;
      en.target.classList.add("in");
      var n = en.target.getAttribute("data-count");
      if (n) {
        var end = +n, t0 = null, suf = en.target.getAttribute("data-suffix") || "";
        var step = function (t) { if (!t0) t0 = t; var p = Math.min((t - t0) / 1200, 1); en.target.textContent = Math.round(end * p).toLocaleString() + suf; if (p < 1) requestAnimationFrame(step); };
        requestAnimationFrame(step);
      }
      io.unobserve(en.target);
    });
  }, { threshold: .15 }) : null;
  $$(".reveal,[data-count]").forEach(function (el) { if (io) io.observe(el); else el.classList.add("in"); });

  /* Countdown */
  $$("[data-countdown]").forEach(function (el) {
    var end = new Date(el.getAttribute("data-countdown")).getTime();
    function tick() {
      var d = Math.max(0, end - Date.now());
      var v = [Math.floor(d / 864e5), Math.floor(d / 36e5) % 24, Math.floor(d / 6e4) % 60, Math.floor(d / 1e3) % 60];
      el.innerHTML = ["Days", "Hours", "Mins", "Secs"].map(function (l, k) { return "<div><b>" + v[k] + "</b><span>" + l + "</span></div>"; }).join("");
    }
    tick(); setInterval(tick, 1000);
  });

  /* Filter + search (guides, videos, jobs) */
  $$(".pill-nav").forEach(function (nav) {
    var target = $(nav.getAttribute("data-target"));
    $$("button", nav).forEach(function (b) {
      b.addEventListener("click", function () {
        $$("button", nav).forEach(function (x) { x.classList.remove("on"); }); b.classList.add("on");
        var f = b.getAttribute("data-filter");
        $$("[data-cat]", target).forEach(function (c) { c.style.display = (f === "all" || c.getAttribute("data-cat") === f) ? "" : "none"; });
      });
    });
  });
  var sInput = $("#site-search");
  if (sInput) {
    sInput.addEventListener("input", function () {
      var q = sInput.value.toLowerCase().trim();
      $$("#guide-grid [data-cat]").forEach(function (c) { c.style.display = c.textContent.toLowerCase().indexOf(q) > -1 ? "" : "none"; });
    });
  }

  /* Donation amount → link to configured processor */
  var don = $("#donate-form");
  if (don) {
    var d = C.donate || {}, links = $("#pay-links"), any = false;
    [["paypal", "PayPal"], ["stripe", "Card (Stripe)"], ["buymeacoffee", "Buy Me a Coffee"], ["kofi", "Ko-fi"]].forEach(function (p) {
      if (d[p[0]]) { any = true; var a = document.createElement("a"); a.className = "btn btn-brand"; a.href = d[p[0]]; a.target = "_blank"; a.rel = "noopener"; a.textContent = "Give via " + p[1]; links.appendChild(a); }
    });
    if (!any && links) links.innerHTML = '<p class="hint mb0">Online checkout is being set up. Submit your pledge below and our team will send you a secure payment link.</p>';
  }

  /* Share buttons */
  $$(".share").forEach(function (b) {
    b.addEventListener("click", function () {
      var data = { title: document.title, url: location.href };
      if (navigator.share) navigator.share(data).catch(function () {});
      else if (navigator.clipboard) { navigator.clipboard.writeText(location.href); b.textContent = "Link copied"; }
    });
  });

  $$(".year").forEach(function (y) { y.textContent = new Date().getFullYear(); });
})();
