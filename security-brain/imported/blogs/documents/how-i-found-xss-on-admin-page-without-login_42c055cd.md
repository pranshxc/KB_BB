---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-22_how-i-found-xss-on-admin-page-without-login.md
original_filename: 2023-01-22_how-i-found-xss-on-admin-page-without-login.md
title: How I found XSS on Admin Page without login!
category: documents
detected_topics:
- xss
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- api-security
language: en
raw_sha256: 42c055cdb962582a8dae17a7a996a4024dcad87be22ac0406f2118a835c5cc77
text_sha256: c76a815dea8b2cae2d70b9647709b2008f7c67f20b1f00836f017b0831bc4f8a
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# How I found XSS on Admin Page without login!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-22_how-i-found-xss-on-admin-page-without-login.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `42c055cdb962582a8dae17a7a996a4024dcad87be22ac0406f2118a835c5cc77`
- Text SHA256: `c76a815dea8b2cae2d70b9647709b2008f7c67f20b1f00836f017b0831bc4f8a`


## Content

---
title: "How I found XSS on Admin Page without login!"
url: "https://sl4x0.medium.com/how-i-found-xss-on-admin-page-without-login-fe165a5f89c2"
authors: ["Abdelrhman Allam (@sl4x0)"]
bugs: ["Reflected XSS"]
publication_date: "2023-01-22"
added_date: "2023-01-23"
source: "pentester.land/writeups.json"
original_index: 1639
scraped_via: "browseros"
---

# How I found XSS on Admin Page without login!

1

·

Top highlight

Abdelrhman Allam (sl4x0)
 highlighted

How I found XSS on Admin Page without login!
Abdelrhman Allam (sl4x0)
Follow
2 min read
·
Jan 22, 2023

743

10

Press enter or click to view image in full size
Introduction

بسم الله الرحمن الرحيم
Hello Awesome Hackers, this is my first Write-Ups in Real Target; I will explain how Fuzzing helped me get an XSS on Admin Page Just in 1 Minute!

Approaching

I am doing Bug Bounty Hunting On Open-Source Projects; As I like doing this and giving back support to these projects and its community!

Get Abdelrhman Allam (sl4x0)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I chose an Application running PHP as I can understand its code!
I Begin with collecting Subs and Endpoints to map the full Application to have a full picture of how it works and what its capabilities are!

Interesting Endpoint

When I am checking the collecting results; Actually i check it with CTRL+F to find interesting keywords like admin, panel, dev, internal ..etc.
While doing this, I found this Link:

https://redacted.redacted.com/admin/login

Trying Some Dumb Default Password and SQLi Payload; with no Successfully Login or Bypassing!

Fuzzing

So I start Fuzzing Using Arjun as I can find any Parameter But when I do this I found a really helpful error 🤓

Press enter or click to view image in full size
Arjun Helpful Error!

Arjun just pushed a helpful error as I didn’t skip it so let’s try combining the full URL; then injecting XSS Payload!

Exploitation

The full URL with the Payload becomes:

https://redacted.redacted.com/admin/login?perspective=asdf1234

After Submitting and Viewing the Source code:

ME HURRYING UP TO MAKE XSS PAYLOAD!
https://redacted.redacted.com/admin/login?perspective=asdf"onload%3d"alert('Slax Was Here!')"asdf

SUBMITTING!!

Press enter or click to view image in full size
Poping-up
Wrapping Up

Remember the one rule
“Fuzzing, Fuzzing, Fuzzingggg”
I hope you guys enjoyed the Write-Up, See you on the Other one!

Twitter🐦: sl4x0
LinkedIn👨‍💼: sl4x0
