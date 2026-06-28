---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-14_credential-stuffing-in-bug-bounty-hunting.md
original_filename: 2021-07-14_credential-stuffing-in-bug-bounty-hunting.md
title: Credential stuffing in Bug bounty hunting
category: documents
detected_topics:
- ssrf
- xss
- sqli
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- sqli
- command-injection
language: en
raw_sha256: 65b6700c2991fdf98ac4ae8254b91611ad535f99fd0f1af8452818a415e908ba
text_sha256: a2942823647ddc2d7c4253df05c2c77c08827202d744cbed15e19c8c3db493fb
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Credential stuffing in Bug bounty hunting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-14_credential-stuffing-in-bug-bounty-hunting.md
- Source Type: markdown
- Detected Topics: ssrf, xss, sqli, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `65b6700c2991fdf98ac4ae8254b91611ad535f99fd0f1af8452818a415e908ba`
- Text SHA256: `a2942823647ddc2d7c4253df05c2c77c08827202d744cbed15e19c8c3db493fb`


## Content

---
title: "Credential stuffing in Bug bounty hunting"
url: "https://krevetk0.medium.com/credential-stuffing-in-bug-bounty-hunting-7168dc1d3153"
authors: ["Valeriy Shevchenko (@Krevetk0Valeriy)"]
bugs: ["Credential stuffing"]
bounty: "8,300"
publication_date: "2021-07-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3507
scraped_via: "browseros"
---

# Credential stuffing in Bug bounty hunting

Member-only story

Credential stuffing in Bug bounty hunting
Valeriy Shevchenko
Follow
6 min read
·
Jul 13, 2021

593

1

Bug hunting is not always about looking for classic vulnerabilities (XSS, SQLi, SSRF, RCE, etc). Sometimes it is a search for a new problem domain. In this article, I will tell you how this not-so-standard approach to vulnerability searching helped me to find many critical problems.

One evening I came up with the idea of crossing Credential Stuffing and Bug bounty hunting. Credential stuffing is the search for leaked usernames and passwords for their use in popular online services, as most of the users love to use the same password everywhere. More often than not, “black hats” hack accounts in various social networks, email services for subsequent scamming. But an idea occurred to me — what if we can try to apply this approach not to popular online services, but to specific services of a company with a bug bounty. Or checking credentials on the services often used in the development life cycle. So the right words about that story — It’s time to gather the stones in the right place.

Press enter or click to view image in full size
popular service where you can check your email regarding data leaks

In general, there is nothing new in all this because of the full-fledged pentest cover over Credential Stuffing. Smart pentester always starts with already leaked credentials. But I haven’t noticed anyone using such things in the bug hunting.

At the time when I started it, there was not a single disclosed report about this problem reported…
