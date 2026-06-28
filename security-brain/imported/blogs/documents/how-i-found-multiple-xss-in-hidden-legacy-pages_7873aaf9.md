---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-02_how-i-found-multiple-xss-in-hidden-legacy-pages.md
original_filename: 2021-09-02_how-i-found-multiple-xss-in-hidden-legacy-pages.md
title: How I Found Multiple XSS in Hidden Legacy Pages
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 7873aaf91e480ec6684af64aedf80c7e3f3028655fd92c7a530ddbeae3d1374e
text_sha256: d32d5e4350f605a2133f14dbc1ec202f3cafb16f2c807e8e031b6ab85980921a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found Multiple XSS in Hidden Legacy Pages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-02_how-i-found-multiple-xss-in-hidden-legacy-pages.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `7873aaf91e480ec6684af64aedf80c7e3f3028655fd92c7a530ddbeae3d1374e`
- Text SHA256: `d32d5e4350f605a2133f14dbc1ec202f3cafb16f2c807e8e031b6ab85980921a`


## Content

---
title: "How I Found Multiple XSS in Hidden Legacy Pages"
url: "https://marxchryz.medium.com/how-i-found-multiple-xss-in-hidden-legacy-pages-a57a25d8ff1f"
authors: ["Marx Chryz"]
bugs: ["XSS"]
bounty: "1,000"
publication_date: "2021-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3359
scraped_via: "browseros"
---

# How I Found Multiple XSS in Hidden Legacy Pages

How I Found Multiple XSS in Hidden Legacy Pages
Marx Chryz Del Mundo
Follow
2 min read
·
Sep 2, 2021

302

Hello everyone, I am Marx Chryz and I do bug bounty hunting for about a year now. It’s also been two and a half years since I started doing web penetration testing.

Introduction

The site I am hunting on is a private program so I can’t disclose the urls, I am just going to discuss the method.

Get Marx Chryz Del Mundo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found an XSS once but it was just P5 and was counted as Self-XSS because the payload is only visible to the attacker.

Because of this, I tried improving my methods on finding URLs with potential XSS vulnerabilities. Here I started looking for hard to find places. Hidden legacy pages

Finding the vulnerability

For those who don’t know, legacy pages are old pages that are still available in the production site. Legacy pages exists, even old, because they are still functional and is still used by other portions of the application.

Upon recon, I found a common subdomain, lets call it sub.redacted.com. In the root of this url (https://sub.redacted.com), I can’t find any XSS vulnerabilities since I assume it is widely tested by fellow bug bounty hunters. So I tried finding folders inside the sub.redacted.com. I was lazy to fire up FFUF and Dirbuster because of my slow internet connection so I started by looking if the site has robots.txt

Open https://sub.redacted.com/robots.txt
Found a directory named “web-app”
/web-app/ is blank so I tried guessing random files.
/web-app/dashboard.php redirects to /web-app/logout.php
Then I view-souce and found lots of .js files.
.js files contains URLs and lots of parameters 😎
Manually checked all the URLs and parameters (a lot are not working since they are legacy pages). This is to see if any of the parameter values get reflected in the page.
Finally found 2 reflected XSS vulnerabilities (1 authenticated and 1 unauthenticated).
Report Timeline

July 19 and 21, 2021 — Report Submitted
Sept 1, 2021 — Triaged as P3 and eligible for $500 bounty each
