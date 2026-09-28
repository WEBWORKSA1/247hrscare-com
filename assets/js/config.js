/* 247hrsCare.com — site configuration. Edit values here; no rebuild needed. */
window.SITE_CONFIG = {
  // Encoded inbox for all form submissions (never rendered in the page).
  // After the first form submission, FormSubmit sends a one-time activation email.
  // Optional: once activated, paste FormSubmit's random alias string below to stop using the encoded inbox.
  inbox: [96,114,117,96,120,101,124,100,118,38,87,112,122,118,126,123,57,116,120,122],
  formsubmitAlias: "",

  // Google AdSense — paste your publisher ID (e.g. "ca-pub-1234567890123456") to switch house ads to AdSense.
  adsenseClient: "",
  adsenseSlots: { default: "" },

  // Google Analytics 4 measurement ID (e.g. "G-XXXXXXX"). Optional.
  ga4: "",

  // Donation / payment links (PayPal.me, Stripe Payment Link, Buy Me a Coffee, Ko-fi...).
  // Leave blank to use the pledge form (a team member follows up by email).
  donate: { paypal: "", stripe: "", buymeacoffee: "", kofi: "" },

  // Your YouTube channel URL (used for Subscribe buttons).
  youtubeChannel: "https://www.youtube.com/",

  // Video library (YouTube IDs). Replace with your own channel's videos to earn YouTube revenue.
  videos: [
    { id: "z_qN6FfqKwA", title: "Expert advice for dementia caregivers", cat: "Dementia" },
    { id: "Z0ADyksNRgg", title: "A family guide to Alzheimer's care", cat: "Dementia" },
    { id: "CT9dqYEIqbs", title: "What is dementia? Part 1", cat: "Dementia" },
    { id: "1EGhhZdQ_ts", title: "Understanding a person living with dementia", cat: "Dementia" },
    { id: "6E4cb8NdV44", title: "How to safely transfer a patient from bed", cat: "Caregiving skills" },
    { id: "cs6OC04lYio", title: "Transferring from bed to wheelchair", cat: "Caregiving skills" }
  ]
};
