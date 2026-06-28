---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-28_bypassing-waf-to-perform-xss.md
original_filename: 2020-05-28_bypassing-waf-to-perform-xss.md
title: Bypassing WAF to perform XSS
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
raw_sha256: d1cd8cb8fab17abebd619109b146eec3880143abe0814e73f1f8b7985421c830
text_sha256: 44862d46a012b157b95ab8c8731fb05e27237ddd0993a528d79e633dcd931713
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing WAF to perform XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-28_bypassing-waf-to-perform-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `d1cd8cb8fab17abebd619109b146eec3880143abe0814e73f1f8b7985421c830`
- Text SHA256: `44862d46a012b157b95ab8c8731fb05e27237ddd0993a528d79e633dcd931713`


## Content

---
title: "Bypassing WAF to perform XSS"
url: "https://medium.com/bugbountywriteup/bypassing-waf-to-perform-xss-2d2f5a4367f3"
authors: ["Kleiton Kurti (@kleiton0x7e)"]
bugs: ["XSS"]
publication_date: "2020-05-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4553
scraped_via: "browseros"
---

# Bypassing WAF to perform XSS

Top highlight

Bypassing WAF to perform XSS
kleiton0x7e
Follow
4 min read
·
May 28, 2020

772

1

Recently I was hunting for some XSS and I come up to a website (lets call it website.com for privacy reason) where it had an admin login form on /admin directory.

Admin Panel on website.com/admin

Instinctively I tried entering random credentials to see what kind of response I will get.

/admin/index.php?msg=Invalid%20Email%20and%20Password

/admin/index.php?msg=Invalid Email and Password

This is the URL I got redirected to, by default this is a very bad idea to display an error message, but it is an implementation I see a lot on different websites.

Any value of ?msg= could be reflected into the website, so lets try to change it to better understand.

What I tried was website.com/admin/index.php?msg=Hello World

?msg=Hello World was reflected

Now we see that every input we enter, gets reflected into that Red-Fonted text.

What if I try injecting some HTML tags?

?msg=<h1>Hello World</h1>

HTML Injection

We got a successful HTML Injection, now its time to put some Javascript code.

I tried more than 50 basic XSS payloads, with a hope for XSS to popup:

?msg=<script>alert(1)</script>
?msg=<img src=xss onerror=alert(1)>
?msg=<input/onmouseover=”javaSCRIPT&colon;confirm&lpar;1&rpar;”
?msg=<iframe %00 src=”&Tab;javascript:prompt(1)&Tab;”%00>

Get kleiton0x7e’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You get the idea that I bruteforced all type of XSS. All of them were blocked by the server, seems there is a WAF behind the scene:

Press enter or click to view image in full size
Malicious XSS requests blocked by WAF

By entering more than 50 XSS Payloads, I came up to a conclusion of what WAF was really filtering:

Every payload with <script>, <frame, <input, <form, was directly blocked by WAF.
Every payload with alert( ) was directly blocked by WAF.

So how will we popup a XSS when alert() was filtered out?

While guessing, I realised that <img wasn’t filtered out, so I start making more complex payload based on that:

?msg=<img/src=`%00`%20onerror=this.onerror=confirm(1)

was my next payload, it got reflected but no XSS :(

<img bypassed but no XSS

Seems like XSS by image isn’t the right path so I kept enumerating more, since it gets reflected, but it doesn’t execute anything inside it.

Soon, I realised that <svg> wasn’t filtered out, so I kept following this path. Since alert( ) is blocked, I’m trying confirm( ) since it worked.

<svg><script%20?>confirm(1)

svg injected but no XSS popup

I had a feeling I was close since it reflected a blank space, I just have to keep going on more. Since there is a WAF, I tried different bypasses, including Base64 decode with eval.atob. I kept using <svg> since It somehow worked.

<svg/onload=eval(atob(‘YWxlcnQoJ1hTUycp’))>

This payload basically decode the base64 value which is alert(‘XSS’). I immediately fired up the payload and, guess what I see, a XSS!!!

Press enter or click to view image in full size
Finally a XSS!!!

Encoding a XSS payload (which was filtered out by WAF) into a base64, it really gave me the freedom to execute whatever I want.

<svg/onload=eval(atob(‘YWxlcnQoZG9jdW1lbnQuY29va2llKQ==’))>

The following base64 is alert(document.cookie) and it went as expected.

Press enter or click to view image in full size

Now I have the freedom to execute everything I want since everything is encoded in Base64 and not detected by WAF, and this is something everyone wants! In additional, this XSS took me 20 minutes, but it was more like a fun challenge for me.
