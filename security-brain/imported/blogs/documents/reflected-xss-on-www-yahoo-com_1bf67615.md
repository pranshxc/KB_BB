---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-12_reflected-xss-on-wwwyahoocom.md
original_filename: 2017-08-12_reflected-xss-on-wwwyahoocom.md
title: Reflected XSS on www.yahoo.com
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
raw_sha256: 1bf67615d8a4516ee7ad329840cb6257801700b384f04a0786a9f8039f2e6767
text_sha256: 709348576a538436fcea2ac911788e5ae0ceb09d43bd66aa9c8781b049d37acb
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS on www.yahoo.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-12_reflected-xss-on-wwwyahoocom.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `1bf67615d8a4516ee7ad329840cb6257801700b384f04a0786a9f8039f2e6767`
- Text SHA256: `709348576a538436fcea2ac911788e5ae0ceb09d43bd66aa9c8781b049d37acb`


## Content

---
title: "Reflected XSS on www.yahoo.com"
url: "https://medium.com/@saamux/reflected-xss-on-www-yahoo-com-9b1857cecb8c"
authors: ["Samuel (@saamux)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Reflected XSS"]
publication_date: "2017-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6126
scraped_via: "browseros"
---

# Reflected XSS on www.yahoo.com

Reflected XSS on www.yahoo.com
Samuel
Follow
1 min read
·
Aug 12, 2017

238

3

Hello guys, my name is Samuel I’m a bug hunter from Chile, it’s my first post about bug bounty programs. Today, I want to share with you a XSS which I found in main domain of Yahoo.

I have detected a Reflected XSS in this website. The vulnerable endpoint was the next:

https://www.yahoo.com/author/vulnerablendpoint

Press enter or click to view image in full size
vulnerable endpoint

Every time I put any text, it was reflected on the web site. After adding the payload, I saw

https://www.yahoo.com/author/"><%2fscript><script>alert(document.domain)<%2fscript>

Get Samuel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The simple payload was working.

Press enter or click to view image in full size

I managed to notice the presence of the vulnerability, now I share the simple payload that I used. Finally I share the video that I did about this vulnerability.

Timeline
July 20 — I sent to report
July 20 —Triaged
July 23 — Resolved
August 8 — Bounty for me :D

Thanks

@saamux
