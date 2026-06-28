---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-15_importance-of-burp-history-analysis-to-bypass-403.md
original_filename: 2021-06-15_importance-of-burp-history-analysis-to-bypass-403.md
title: Importance of burp history analysis to bypass 403
category: documents
detected_topics:
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 2dff0fd3d5a2c409abd4f8e3f4633cffb216eb7e0df35d03054287daed6b789e
text_sha256: 89863f9383083d48b7db600d0191ac1a00aa379c38a3b437b9fae1635de85fdf
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Importance of burp history analysis to bypass 403

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-15_importance-of-burp-history-analysis-to-bypass-403.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `2dff0fd3d5a2c409abd4f8e3f4633cffb216eb7e0df35d03054287daed6b789e`
- Text SHA256: `89863f9383083d48b7db600d0191ac1a00aa379c38a3b437b9fae1635de85fdf`


## Content

---
title: "Importance of burp history analysis to bypass 403"
url: "https://infosecwriteups.com/importance-of-burp-history-analysis-to-bypass-403-afc7af6c08b"
authors: ["Vuk Ivanovic"]
bugs: ["403 bypass"]
publication_date: "2021-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3576
scraped_via: "browseros"
---

# Importance of burp history analysis to bypass 403

Member-only story

Importance of burp history analysis to bypass 403
Vuk Ivanovic
Follow
3 min read
·
Jun 15, 2021

250

or, how I learned that specific Referer header can make all the difference

Press enter or click to view image in full size

When it comes to bug hunting, directory brute force is a necessary part, if you want to cover all the bases. And, at times, depending on bug bounty programs’ policy, or simply how the servers are configured, things like captcha or 429, or just blocking your ip completely will happen. There are ways around it, but this isn’t about that. This is about checking the results, seeing interesting endpoints being marked 403, and failing to bypass it using the usual techniques (headers like Host, x-forwarded-host, x-forwarded-for, etc.), what then? Time to move on?

Referer header, and the better-known bypass
Now, maybe some of you are aware that certain endpoints won’t accept requests without Referer header. The usual case is where the endpoint is for example:
https://admin.target.com/interestingendpoint.php

and unless Referer is matching the subdomain or at least base domain, it will result in 403 or 404 or redirect. But, sometimes, those values will fail as well. Enter burp or any other way to analyze what requests and responses are happening while browsing the website in question.

Referer header, and the lesser-known bypass
This happened by pure accident. I finished…
