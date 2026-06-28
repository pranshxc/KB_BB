---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-30_cross-site-scripting-the-power-of-the-hidden-parameters.md
original_filename: 2020-05-30_cross-site-scripting-the-power-of-the-hidden-parameters.md
title: 'Cross-site scripting: The power of the hidden parameters.'
category: documents
detected_topics:
- xss
- idor
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- csrf
- api-security
language: en
raw_sha256: f955f1f20306ecc1cd8e79f148be0622b6b1b6c01f7dca65a8650f17207a0d22
text_sha256: 36414e61d9fbcd5a5c5db40178040e66c7b08c480dd487f9439c8711b3cc075e
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Cross-site scripting: The power of the hidden parameters.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-30_cross-site-scripting-the-power-of-the-hidden-parameters.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `f955f1f20306ecc1cd8e79f148be0622b6b1b6c01f7dca65a8650f17207a0d22`
- Text SHA256: `36414e61d9fbcd5a5c5db40178040e66c7b08c480dd487f9439c8711b3cc075e`


## Content

---
title: "Cross-site scripting: The power of the hidden parameters."
url: "https://medium.com/@kassihmouhssine/cross-site-scripting-the-power-of-the-hidden-parameters-259a4d2c4c09"
authors: ["Kassih Mouhssine (@KassihMouhssine)"]
programs: ["Sony"]
bugs: ["Reflected XSS"]
publication_date: "2020-05-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4544
scraped_via: "browseros"
---

# Cross-site scripting: The power of the hidden parameters.

Cross-site scripting: The power of the hidden parameters.
Kassih mouhssine
Follow
3 min read
·
May 30, 2020

72

Press enter or click to view image in full size

Hey everyone! This is another XSS writeup that you can learn from, a strange one in fact.

It’s my first writeup so be kind to me. I am just trying to share my findings.

Like any other bug hunter, one day I had the urge to look for a bug, so while browsing HackerOne programs, my eyes caught Sony’s program.

Let’s test sony I said.

I started my recon by opening google and playing with some dorks such as site:*.sony.*

After a while, I found the domain “sony.jp”. I checked it and it seemed like a good start.

As a start, I used amass like below to gather some subdomains.

amass enum -passive -d sony.jp -o sony.txt

After getting a list of subdomains, I passed them to httprobe to only keep the alive ones.

However, if you want to get only working subdomains, you can use amass, httprob like this:

amass enum -passive -d sony.jp -o sony.jp ; cat sony.jp | httprobe | tee sony.txt ; rm sony.jp

I started enumerating the list of subdomains for a while and then I noticed one with a lot of functions.

What I mean by “a lot of functions” is it has many user interactions.

I tried to fetch for bugs like csrf , IDOR , sql , and even rce, but I couldn’t find anything of interest.

What about XSS?!

I started searching for parameters and I got a lot of ones but sadly no xss. :’(

Get Kassih mouhssine’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I checked the source code in the browser. I started looking for hidden parameters, then I found a parameter named “cs”.

Tip: Never forget to look for hidden parameters in the source code. click view source code and search for “hidden”, “input”, or “var” parameters.

I tried injecting a bunch of XSS payloads in it but nothing worked out. :(

While I was about to give up and look for another subdomain, I hyped myself a little and tried the parameter “Couponcode”

Because there was an option to add a coupon code on the page.

redacted.sony.jp/?Couponcode=hunter”><svg/onload=confirm(document.cookie)>

Unfortunately, no XSS.

But when I added the “cs” parameter, the XSS popped up.

So the final url is :

redacted.sony.jp/?Couponcode=hunter”><svg/onload=confirm(document.cookie)>&cs=

Press enter or click to view image in full size

So here’s how it works.

When I put the payload in the “couponcode” parameter the XSS didn’t work out because the payload was filtered, but when I added the cs parameter, a new “<link>” tag was generated in the source code, which had no filter.

<link href=”https://redacted.sony.jp/?Couponcode=hunter"><svg/onload=confirm(document.cookie)>&cs=">

That’s it.

See you in the next writeup.

twitter: https://twitter.com/kassihmouhssine

linkedin : https://www.linkedin.com/in/kassih-mouhssine/
