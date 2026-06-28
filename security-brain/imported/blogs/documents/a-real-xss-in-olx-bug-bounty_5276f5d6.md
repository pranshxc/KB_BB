---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-21_a-real-xss-in-olx-bug-bounty.md
original_filename: 2019-03-21_a-real-xss-in-olx-bug-bounty.md
title: A real XSS in OLX Bug Bounty
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 5276f5d6c60ff74bd493408ce905054d452bbee0b2970823e29fdc6c33fda7f0
text_sha256: fea6433f55a4f72a61435df2762ee9c94854ac633e35e07b515ceb41108750fb
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# A real XSS in OLX Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-21_a-real-xss-in-olx-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `5276f5d6c60ff74bd493408ce905054d452bbee0b2970823e29fdc6c33fda7f0`
- Text SHA256: `fea6433f55a4f72a61435df2762ee9c94854ac633e35e07b515ceb41108750fb`


## Content

---
title: "A real XSS in OLX Bug Bounty"
url: "https://medium.com/@paulorcchoupina/a-real-xss-in-olx-7727ae89c640"
authors: ["Paulo Choupina (@PauloChoupina)"]
programs: ["OLX"]
bugs: ["Reflected XSS"]
publication_date: "2019-03-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5348
scraped_via: "browseros"
---

# A real XSS in OLX Bug Bounty

A real XSS in OLX Bug Bounty
Paulo Choupina
Follow
2 min read
·
Mar 21, 2019

1

1

I saw a couple of other write-ups and blog posts about “XSS in OLX” but when I got to read them, they end up being either stored XSS or in some other website that belongs within the scope of OLX…

SO!!

I figured, “hey if they are good enough for a write-up, so it’s my bug.” xD

Original report: https://hackerone.com/reports/477771

I was looking for bugs on another website when I came across this.
It is a reflected Cross Site Scripting (XSS) vulnerability in the parameter search[user_id] located at the main page of Olx.pt

If you navigate to Olx.pt
and choose a random item, open that item page and click
“outros anúncios” as in “other ads”
you will get redirected to:

https://www.olx.pt/ads/?search%5Buser_id%5D=xxx&view=galleryWide

Get Paulo Choupina’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Within that page, the parameter search[user_id] was vulnerable to XSS.

POC:

https://www.olx.pt/braga/?search%5Buser_id%5D=1zqjeu'%22()%7B%7D<x>:/1zqjeu;9</SCript><svG/onLoad=prompt(9)>, ;prompt(9);&view=galleryWide

Press enter or click to view image in full size

It was across all the domains, here is an example of it in Poland’s domain:

https://www.olx.pl/lubelskie/?search%5Buser_id%5D=1zqjeu'%22()%7B%7D<x>:/1zqjeu;9</SCript><svG/onLoad=prompt(9)>, ;prompt(9);&view=galleryWide

Press enter or click to view image in full size

I reported it and got added to the OLX’s Hall of Fame:
https://security.olx.com/security-hall-of-fame.html

Kudos to me!! xD
