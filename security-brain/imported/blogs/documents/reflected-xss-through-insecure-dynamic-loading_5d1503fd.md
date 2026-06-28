---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-11_reflected-xss-through-insecure-dynamic-loading.md
original_filename: 2021-07-11_reflected-xss-through-insecure-dynamic-loading.md
title: Reflected XSS Through Insecure Dynamic Loading
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
raw_sha256: 5d1503fdaac64e8d19bd80030bac4433b0534810062c25d3951d0eb05ce676f8
text_sha256: 8d2a050dc1e81d7bdf8a908a2bb9953ebd9ddb11ad29581512b38276af29b6b0
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS Through Insecure Dynamic Loading

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-11_reflected-xss-through-insecure-dynamic-loading.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `5d1503fdaac64e8d19bd80030bac4433b0534810062c25d3951d0eb05ce676f8`
- Text SHA256: `8d2a050dc1e81d7bdf8a908a2bb9953ebd9ddb11ad29581512b38276af29b6b0`


## Content

---
title: "Reflected XSS Through Insecure Dynamic Loading"
url: "https://infosecwriteups.com/reflected-xss-through-insecure-dynamic-loading-dbf4d33611e0"
authors: ["Greg Gibson"]
bugs: ["XSS"]
publication_date: "2021-07-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3517
scraped_via: "browseros"
---

# Reflected XSS Through Insecure Dynamic Loading

Member-only story

Reflected XSS Through Insecure Dynamic Loading
Finding A Unique and Complex Payload To Load Remote Scripts
Greg Gibson
Follow
6 min read
·
Jul 11, 2021

157

STOP! Before reading this article, I encourage you to try this XSS Challenge for yourself. I’ve incorporated the core elements of the vulnerability into a simple static page here: https://d11dkd80d59ds1.cloudfront.net/. While this article will walk you through the full exploit, I’ll warn you that it is far more complicated than the typical injection and as such the solution might make more sense if you take the time to try it yourself.

Press enter or click to view image in full size
Try this XSS Challenge for yourself before reading this article. While this article will walk you through the full exploit, I’ll warn you that it is far more complicated than the typical injection and as such the solution might make more sense if you take the time to try it yourself.

Recently while hunting a private program on Bugcrowd I discovered both the user’s email address and security questions could be modified WITHOUT password verification or any other security checks in place. This combination would allow an attacker to successfully perform an account takeover; however, I needed a remote exploit to justify a submission.

For those new to or unfamiliar with Bug Bounty hunting, vulnerabilities in and of themselves do not translate to accepted submissions. In this case, I’d discovered a P5 Lack of Password Confirmation — Change Email Address¹. P5’s are the lowest severity level (with P1 being the highest) and one that typically does not receive a bounty. To truly demonstrate an impact you need a working, and importantly remote, exploit, but as it stood, an…
