---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-18_server-side-misconfigurartion-a-funny-fix.md
original_filename: 2020-11-18_server-side-misconfigurartion-a-funny-fix.md
title: Server Side Misconfigurartion - A Funny Fix
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: aea80c3e018c783aab42c12b8d1cf72d2e40d14dfc78e91710dd735bab406309
text_sha256: 91ac5ba10983b2a86d984d084e66a2491915b238f0ff7cab426ce1b549630822
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Server Side Misconfigurartion - A Funny Fix

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-18_server-side-misconfigurartion-a-funny-fix.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `aea80c3e018c783aab42c12b8d1cf72d2e40d14dfc78e91710dd735bab406309`
- Text SHA256: `91ac5ba10983b2a86d984d084e66a2491915b238f0ff7cab426ce1b549630822`


## Content

---
title: "Server Side Misconfigurartion - A Funny Fix"
url: "https://shahjerry33.medium.com/server-side-misconfigurartion-a-funny-fix-63cc12b4c7fc"
authors: ["Jerry Shah (@Jerry)"]
programs: ["Basecamp"]
bugs: ["Information disclosure"]
bounty: "100"
publication_date: "2020-11-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4121
scraped_via: "browseros"
---

# Server Side Misconfigurartion - A Funny Fix

Server Side Misconfigurartion - A Funny Fix
Jerry Shah (Jerry)
Follow
3 min read
·
Nov 18, 2020

363

Summary :

I would like to enlighten you guys about my recent finding. It was my luck that I by mistakenly clicked the Reload button on a 404 page and got an information disclosure. The vulnerability is resolved properly now.

I was recently reading the Hackerone Hacktivity page and saw a published report (https://hackerone.com/reports/981796) which was related to information disclosure on one of the subdomain of hey.com and the endpoint was https://gopher.hey.com/metrics. While reading the report the steps to reproduce the issue was mentioned, so I thought of reproducing the issue and at first it gave me 404 not found error but when I clicked on reload button I got the access to the endpoint again. The issue was resolved in the above mentioned report but due to improper fix it was reproducible again.

When I tried to reproduce the issue using curl command (curl https://gopher.hey.com/metrics) it gave me 404 every time but when I visited the web with the same URL the 1st thing was 404 and then after clicking reload button the information was disclosed. The information was related to garbage collection cycle.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Previously deployed fix :

Press enter or click to view image in full size
Previous Fix

How I found this vulnerability ?

I went to https://gopher.hey.com/metrics and got 404 error
Press enter or click to view image in full size
404 Not Found

2. Then I clicked on reload and got the information disclosure

Press enter or click to view image in full size
Garbage Collection Cycle - 1
Press enter or click to view image in full size
Garbage Collection Cycle - 2
Press enter or click to view image in full size
Garbage Collection Cycle - 3

Impact :

In this type of vulnerabilities the impact completely depends upon what kind of information is getting leaked. In my case the severity was low but if the information is related to PII then the severity could be high to critical.

Mitigation :

When the fix is deployed it should be tested properly with all the ways of how it can be reproduced.

Press enter or click to view image in full size
