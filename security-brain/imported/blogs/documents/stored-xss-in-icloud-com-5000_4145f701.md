---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-14_stored-xss-in-icloudcom-5000.md
original_filename: 2021-02-14_stored-xss-in-icloudcom-5000.md
title: Stored XSS in icloud.com — $5000
category: documents
detected_topics:
- xss
- idor
- command-injection
- csrf
- business-logic
tags:
- imported
- documents
- xss
- idor
- command-injection
- csrf
- business-logic
language: en
raw_sha256: 4145f7012b4f1c7f21ea072230a954aabfa26b995b960906d7a5a8e162d2f429
text_sha256: 2cf5a02a9a22c0d081e34c28c905b40942612f45bfec4edfde300c96694b199b
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in icloud.com — $5000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-14_stored-xss-in-icloudcom-5000.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, csrf, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `4145f7012b4f1c7f21ea072230a954aabfa26b995b960906d7a5a8e162d2f429`
- Text SHA256: `2cf5a02a9a22c0d081e34c28c905b40942612f45bfec4edfde300c96694b199b`


## Content

---
title: "Stored XSS in icloud.com — $5000"
url: "https://vbharad.medium.com/stored-xss-in-icloud-com-5000-998b8c4b2075"
authors: ["Vishal Bharad"]
bugs: ["Stored XSS"]
bounty: "5,000"
publication_date: "2021-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3907
scraped_via: "browseros"
---

# Stored XSS in icloud.com — $5000

Member-only story

Stored XSS in icloud.com — $5000
Vishal Bharad
Follow
2 min read
·
Feb 14, 2021

650

5

Hello Guys hope you all are doing well, fine and healthy during this hard time.

Introduction :

Hello, I am Vishal Bharad, from India and working as Penetration Tester, Now today I am going to share how I found Stored Cross-Site Scripting (XSS) in icloud.com.

Initial Discovery & Exploitation :

First of all I am not the XSS guy :D

Finally I decided to hunt on Apple. As we all know that apple is having large scope so I blindly choose icloud.com and decided to find at least 1 bug on icloud.com.

I tried many vulnerabilities on icloud.com such as CSRF, IDOR, Business Logic Bugs etc. and got nothing. I keep tried to find bugs on icloud.com and after so many attempts I decided to find XSS on icloud.com. (As I am still not good at finding XSS :D)

So here I started the initial recon to find XSS. As we all know that we can try XSS where strings are reflected on webpage or in response.

So I have logged in with icloud.com and inserted payloads everywhere and looked for the webpages where my payloads or strings over getting reflected in response. After so many attempts I got one endpoint where my payload was fired and It was my “Pursuit of Happiness”

Press enter or click to view image in full size
XSS fired in Settings >> Browser All Versions.
