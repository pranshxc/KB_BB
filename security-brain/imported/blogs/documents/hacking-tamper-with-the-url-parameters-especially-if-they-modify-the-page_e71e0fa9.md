---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-09_hacking-tamper-with-the-url-parameters-especially-if-they-modify-the-page.md
original_filename: 2020-12-09_hacking-tamper-with-the-url-parameters-especially-if-they-modify-the-page.md
title: Hacking — Tamper with the URL Parameters, especially if they modify the page
category: documents
detected_topics:
- xss
- command-injection
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: e71e0fa99e42f7f69c115debfe6b483ef2bb2fd1e5728e7b8c0ebf1df59d2b51
text_sha256: 5b1072331d3dc8d07f15ee36006cf5123553f6829e6795b7f29499be21a5089a
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking — Tamper with the URL Parameters, especially if they modify the page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-09_hacking-tamper-with-the-url-parameters-especially-if-they-modify-the-page.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `e71e0fa99e42f7f69c115debfe6b483ef2bb2fd1e5728e7b8c0ebf1df59d2b51`
- Text SHA256: `5b1072331d3dc8d07f15ee36006cf5123553f6829e6795b7f29499be21a5089a`


## Content

---
title: "Hacking — Tamper with the URL Parameters, especially if they modify the page"
url: "https://medium.com/the-volatile-triad/hacking-tamper-with-the-url-parameters-especially-if-they-modify-the-page-7edf158c8db9"
authors: ["Jack"]
bugs: ["HTTP parameter pollution"]
publication_date: "2020-12-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4080
scraped_via: "browseros"
---

# Hacking — Tamper with the URL Parameters, especially if they modify the page

Jack
 highlighted

Hacking — Tamper with the URL Parameters, especially if they modify the page
Jack
Follow
3 min read
·
Dec 9, 2020

11

Concise tip: If you run into a page with interesting URL parameters, always tamper with them and see what you can do, especially if they modify an iframe within the page. Depending on what type of integration it is you may be able to inject content into that iframe.

My report: https://hackerone.com/reports/367589

Another one to reference is https://hackerone.com/reports/298265; I have found this same vulnerability in many different programs but unfortunately none of my reports are disclosed yet.

Full story: Many websites use different third-party services throughout their sites for things such as review forms, job applications, search functionalities, and more. Sometimes these services are integrated into pages via iframes and if this is the case, the parent URL oftentimes contains parameters that modify this iframe. These can vary from stylistic modifiers to identifiers, but if they modify the iframe, there is a great opportunity to tamper with them.

Get Jack’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That explanation is a bit vague and confusing, so let’s dive into my Starbucks report for a more specific example. In their case, they were using a PowerReviews iframe integration and when you clicked to write a review for a product, various URL parameters were appended to the parent URL that all began with “pr”, giving away that they were PowerReviews parameters. The “pr_merchant_id” parameter stood out to me in particular because every PowerReviews form has a unique merchant ID tied to the creator. By modifying this URL parameter to a different ID, I could load any PowerReviews form on a page within athome.starbucks.com.

In most of these URL parameter pollution scenarios when you can load your own content within the iframe, the impact is similar to Stored XSS. An attacker could design a phishing form on one of these services that looks like a page prompting a victim to log in, for example, and upon sending the victim that link on the trusted website they would see the phishing form prompting them for their login information. The only issue is that in many cases such as PowerReviews or Greenhouse, it requires a bit of social engineering to acquire an account to make these job/review forms. I did not perform this step because that would be illegal, but it adds a level of difficulty in execution versus XSS that may lower the impact.

Overall, URL parameter pollution into iframes, especially third-party integration iframes, can lead to content injection similar to Stored XSS and can be a serious vulnerability. Every third-party service will be different in how it operates though, so the work comes in figuring out which URL parameters can be modified and how one could inject their own content into the page.

Press enter or click to view image in full size
Starbucks’ new integration of PowerReviews without iframes.

Starbucks seems to continue to use PowerReviews on athome.starbucks.com but without iframes anymore to avoid the whole parameter situation in the first place, and Greenhouse appears to be avoid iframes entirely now (See Github’s Greenhouse job integration, for example). Thank you to the Starbucks team for helping with categorization and thank you to Hackerone for disclosing that Greenhouse vulnerability.
