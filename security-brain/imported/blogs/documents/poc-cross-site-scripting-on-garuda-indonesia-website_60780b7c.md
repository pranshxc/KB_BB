---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-16_poc-cross-site-scripting-on-garuda-indonesia-website.md
original_filename: 2018-11-16_poc-cross-site-scripting-on-garuda-indonesia-website.md
title: '[POC] Cross-Site Scripting on Garuda Indonesia Website'
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 60780b7c0c99163f9a459f5016057e986549660e2d49050c7aed0dfe85006160
text_sha256: 88e56731f01f2c31fa231ae983a8b84a69849c05fd8949e044ce809298f66ae0
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# [POC] Cross-Site Scripting on Garuda Indonesia Website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-16_poc-cross-site-scripting-on-garuda-indonesia-website.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `60780b7c0c99163f9a459f5016057e986549660e2d49050c7aed0dfe85006160`
- Text SHA256: `88e56731f01f2c31fa231ae983a8b84a69849c05fd8949e044ce809298f66ae0`


## Content

---
title: "[POC] Cross-Site Scripting on Garuda Indonesia Website"
url: "https://medium.com/@ariffadhlullah2310/poc-cross-site-scripting-on-garuda-indonesia-website-452f4864f615"
authors: ["Arif-ITSEC111"]
programs: ["Garuda Indonesia"]
bugs: ["XSS"]
publication_date: "2018-11-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5583
scraped_via: "browseros"
---

# [POC] Cross-Site Scripting on Garuda Indonesia Website

[POC] Cross-Site Scripting on Garuda Indonesia Website
Arif-ITSEC111
Follow
2 min read
·
Nov 16, 2018

20

2

Hello, This is my 3rd post about bug bounty. First of all, i want to say thank you to Garuda Indonesia and I’m sorry for my bad english. As we knew, Garuda Indonesia is the Best of the best airline on Indonesia. Ok, we go to the topic

1st, im was tying to register new member on https://www.garuda-indonesia.com/

There is a login/register page. Then i clicked register button.

As same as like the others people, i try to register my personal information on the website.

Fill all of personal information and then try to activated my email.

After that, i was trying to complete all of personal information. But wait, as a bug hunter maybe i can do something with this form site. i try to inject my XSS script.

Get Arif-ITSEC111’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

TADAAAAAAAAAAAAAAAAAAAAA, I found that vuln on “update companion form”

Press enter or click to view image in full size
XSS
Press enter or click to view image in full size
XSS inject script image

That’s It. See Ya………………………………………….

timeline
3/11/2018 (Submit Report)
5/11/2018 (Mitigation Bug)
16/11/2018 (Reward & Bug Closed)

Tools

Burpsuite
Nmap
Wappalyzer
