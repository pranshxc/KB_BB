---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-13_how-i-get-100-in-just-10-minutes-.md
original_filename: 2022-11-13_how-i-get-100-in-just-10-minutes-.md
title: How i get $100 in just 10 minutes !
category: documents
detected_topics:
- command-injection
- rate-limit
- race-condition
- api-security
tags:
- imported
- documents
- command-injection
- rate-limit
- race-condition
- api-security
language: en
raw_sha256: c060cd15ca49c88e412eae050c756b6896d24f66633a3c03deef3060abcde12b
text_sha256: 16e8a2d0a708e1e0d8ed76d223d3a8631c3b8485f73b07bd653fe5377e185b7d
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# How i get $100 in just 10 minutes !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-13_how-i-get-100-in-just-10-minutes-.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, race-condition, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `c060cd15ca49c88e412eae050c756b6896d24f66633a3c03deef3060abcde12b`
- Text SHA256: `16e8a2d0a708e1e0d8ed76d223d3a8631c3b8485f73b07bd653fe5377e185b7d`


## Content

---
title: "How i get $100 in just 10 minutes !"
url: "https://medium.com/@jodyritonga/how-i-get-100-in-just-10-minutes-b018b28645ce"
authors: ["Jody ritonga"]
bugs: ["Race condition"]
bounty: "100"
publication_date: "2022-11-13"
added_date: "2022-11-14"
source: "pentester.land/writeups.json"
original_index: 1919
scraped_via: "browseros"
---

# How i get $100 in just 10 minutes !

How i get $100 in just 10 minutes !
Jody ritonga
Follow
3 min read
·
Nov 13, 2022

84

1

Hello everyone ! this is my first medium write up, im very sorry if i have a bad grammar, because english is not my mother tongue. So a quick explaination about me, i am Jody Ritonga, 19 Y.O from indonesia and ill have interest in web security application so much.

So in my first writeup i will tell you how did i get my $100 in just like 10 minutes by testing a simple feature in a Web application. a quick brief this web application is like linkedin where you can search for a job, connection, and also read about the latest news about some company.

Let say this web application Redacted.com, when i first arrive at the company web application, i usually hunt for no rate limit and poison header injection. But No luck in that feature

And my methodology was if i cant find those two bug, ill try to use the website as like other regular user would do and try to understand every request and feature. And after that i see a feature where you can post and like other people comment. when i see that like button in my mind be like

My bug hunter sense tingling, i was like “Oh i know what to do let test for a race condition and see did God of Luck is on my side.” so go and fired up my burpsuite. turn on my intercept and get this kind of request

Press enter or click to view image in full size

And after that, i send this request to intruder. Oh and btw when i found this bug i didnt know about turbo intruder, so i still using old traditional burp intruder. After i send to intruder ill setting my payload into null payload with 100 request and also my resource pool into this

After that ill send my request and this is what the request look like

and i was like “Omg its a double response ! is it working? is the race condition there?” and then ill go and check the post

Press enter or click to view image in full size

And there we go. we have a negative value of like. and i was like

And ill go report it to the IT manager and yes ill got the bounty. And thats it for my first write up. Hope you can understand and take new knowledge to all of you. Keep hunting hackers !

Get Jody ritonga’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Time Report

07/09/2022 — Report sended to company

12/09/2022 — The report get noticed and they tell its valid

06/11/2022 — The reward is given
