---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-07_an-unusual-way-to-find-xss-injection-in-one-minute.md
original_filename: 2022-06-07_an-unusual-way-to-find-xss-injection-in-one-minute.md
title: An unusual way to find XSS injection in one minute
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: bdecd2287fcf24c9f79a473cd319f51bc435e8fb9e3daec83f5c5efe5c6e8ede
text_sha256: 418074a0c9233dc8d1b783ee74c9d898291387c0166358cd35c2b8b4e92ca711
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# An unusual way to find XSS injection in one minute

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-07_an-unusual-way-to-find-xss-injection-in-one-minute.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `bdecd2287fcf24c9f79a473cd319f51bc435e8fb9e3daec83f5c5efe5c6e8ede`
- Text SHA256: `418074a0c9233dc8d1b783ee74c9d898291387c0166358cd35c2b8b4e92ca711`


## Content

---
title: "An unusual way to find XSS injection in one minute"
url: "https://medium.com/@ao64400225/an-unusual-way-to-find-xss-injection-in-one-minute-9ed2c7e2a848"
authors: ["Andrey Onishchenko"]
programs: ["TimeWeb"]
bugs: ["CSTI", "XSS"]
publication_date: "2022-06-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2582
scraped_via: "browseros"
---

# An unusual way to find XSS injection in one minute

Alexander Onishchenko
 highlighted

Alexander Onishchenko
 highlighted

An unusual way to find XSS injection in one minute
Alexander Onishchenko
Follow
3 min read
·
Jun 7, 2022

908

13

Hi there! I think that many developers have heard that you can’t trust any user input, and indeed it is. However, there are some places that are often overlooked, which lead to vulnerabilities.

And one of those places is ……. registration 🤔. This is probably not what you wanted to hear, but let me explain.

When registering a new user or updating his data, the developers don’t forget to validate the input fields, but what happens if we put the payload directly into the Google account (In the first and last name fields), and then register on the site through this account? We can get Stored XSS.

Let’s move on to an example

About a month ago, i started my research on one of the bug bounty programs, and with their permission I can reveal the details. it was TimeWeb Ltd — a Russian hosting provider.

As always, I started by registering an account in order to expand my scope area. To save time, i decided to register through social networks using a Yandex account for this (Yandex — Russian analogue of Google) where my full name is “>{{7*7}}<img>

Press enter or click to view image in full size

And after registration through this malicious Yandex account, in my TimeWeb public profile i saw “>49<img>. The code has been executed, which means that we are able to perform XSS attack. We just need to register a Yandex account with the following name:

{{constructor.constructor(‘alert(`XSS`)’)()}}

But here’s the problem. We can not register such an account due to restrictions on the number of special characters in the first name field. The solution is quite simple, split the payload into two parts, one part for the first name and the other for the last name. And since the full name is in one <span> tag, the payload will be concatenated.

Press enter or click to view image in full size

We just have to register through a Yandex account on the target site.

Get Alexander Onishchenko’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And Boom…. We have XSS vulnerability.

Press enter or click to view image in full size

I’ve also managed to hack quite a few sites this way.

PS:

A Google account can’t be used to exploit XSS like this as Google restricts some character input, but it can still be used to find a ton of other bugs. However, there are several other services, like Steam, Amazon, that can be useful for such attacks

Useful links:

HackTricks — Client Side Template Injection (CSTI)
