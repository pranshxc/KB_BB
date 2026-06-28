---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-28_shodan-is-your-friend-if-you-ignore-him-you-will-lose-many.md
original_filename: 2019-08-28_shodan-is-your-friend-if-you-ignore-him-you-will-lose-many.md
title: Shodan is your friend!!! If you ignore him you will lose many…
category: documents
detected_topics:
- sqli
- sso
- command-injection
- automation-abuse
tags:
- imported
- documents
- sqli
- sso
- command-injection
- automation-abuse
language: en
raw_sha256: 11bfab1273e183702620e839c7561976976201482ba1c7ba4d3ddab7469bd701
text_sha256: 5550147a21c0adfa5b4fd6634a0d36bfe156d5e3d6cbd6ba441161270ba2148e
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: true
---

# Shodan is your friend!!! If you ignore him you will lose many…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-28_shodan-is-your-friend-if-you-ignore-him-you-will-lose-many.md
- Source Type: markdown
- Detected Topics: sqli, sso, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: True
- Raw SHA256: `11bfab1273e183702620e839c7561976976201482ba1c7ba4d3ddab7469bd701`
- Text SHA256: `5550147a21c0adfa5b4fd6634a0d36bfe156d5e3d6cbd6ba441161270ba2148e`


## Content

---
title: "Shodan is your friend!!! If you ignore him you will lose many…"
url: "https://medium.com/@bathinivijaysimhareddy/shodan-is-your-friend-if-you-lose-him-you-will-lose-many-657d07472f75"
authors: ["Vijaysimha Reddy Bathini (@fatratfatrat)"]
bugs: ["SQL injection", "Authentication bypass"]
publication_date: "2019-08-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5057
scraped_via: "browseros"
---

# Shodan is your friend!!! If you ignore him you will lose many…

Top highlight

Shodan is your friend!!! If you ignore him you will lose many…
Vijaysimha Reddy Bathini
Follow
3 min read
·
Aug 29, 2019

240

1

In this blog post, I would like to tell you about my recent finding and it will also show you how effective can be. As it is my first writeup please ignore all my grammatical errors. I have been focusing on my recon procedure from the last couple of months because I just got fed up with monkey testing. I stopped all my hunting for a period and just concentrated on recon. If you don't concentrate on recon you will end up in getting duplicates every time.

Coming to the point on how I discovered a critical bug on a known public program. I love Zseano words “A bigger scope program has the high probability of finding a bug rather than low scope”. I don’t want to mention the program name so I will be mentioning it as redacted.com. As the program consists of wide scope and many got vulnerabilities rewarded almost 600 I thought I cannot find vulnerabilities in those in-scope domains. Then I thought maybe I can find on the IP’s which the company owns. Quickly went to the shodan.io did a query org:” redacted”. It nearly gave me 400 results. Shit, I’m not a robot to check all 400 IP’s. But I tried to find vulnerabilities in 14 results ended up finding nothing. I gave up over there. After a couple of hours, one thing got hit my mind “Does this redacted hosts any services on cloud providers like Amazon cloud, Google Cloud, etc.. I again did a shodan dork against every cloud service provider and I got many results.

Get Vijaysimha Reddy Bathini’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When we query using org:”organization name” in shodan it just gives all the IP’s which belong to the organization. So to get all the IP’s which belong to the organization plus all the IP’s which the organization hosts on cloud service provider we use the SSL filter. To get this we use this shodan query ssl:”organization name”.

I found one IP belongs to redacted because I found that the certificate belongs to redacted. To confirm this I quickly opened that IP it has redacted logo on it. It was a basic authentication page. The first thing that strikes me when I see the login page is authentication bypass using SQLi. Quickly I kept username: admin and password=***REDACTED*** 1=1 — +. I got logged in as admin. I found some developer's profiles and their project files in that domain. I didn’t confirm that those developers belong to redacted blindly. Searched for them on Github and Linkedin and I confirmed that they belong to the redacted company. I thought its enough actually and better to report.

Bug reported to redacted and they triaged it in 30 mins and they rewarded me in less than 3 hrs with $$$$🤑🤑🤑.

Connect to me on twitter

Twitter: https://twitter.com/fatrat_v2
