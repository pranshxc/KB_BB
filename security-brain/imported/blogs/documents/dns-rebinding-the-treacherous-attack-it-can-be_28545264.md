---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-25_dns-rebinding-the-treacherous-attack-it-can-be.md
original_filename: 2020-07-25_dns-rebinding-the-treacherous-attack-it-can-be.md
title: DNS Rebinding, The treacherous attack it can be
category: documents
detected_topics:
- ssrf
- command-injection
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- cloud-security
language: en
raw_sha256: 28545264f4e0cff68d2c8863f738acd60c136d1f19287e1f294760ce64bd25c4
text_sha256: da4a92e0ceadfd79e5a43d1cbf9a89c82d9bc6afb447604f01b11411be3390be
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# DNS Rebinding, The treacherous attack it can be

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-25_dns-rebinding-the-treacherous-attack-it-can-be.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `28545264f4e0cff68d2c8863f738acd60c136d1f19287e1f294760ce64bd25c4`
- Text SHA256: `da4a92e0ceadfd79e5a43d1cbf9a89c82d9bc6afb447604f01b11411be3390be`


## Content

---
title: "DNS Rebinding, The treacherous attack it can be"
url: "https://medium.com/bugbountywriteup/dns-rebinding-the-treacherous-attack-it-can-be-b367c61b4372"
authors: ["Vuk Ivanovic"]
bugs: ["DNS rebinding"]
publication_date: "2020-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4387
scraped_via: "browseros"
---

# DNS Rebinding, The treacherous attack it can be

Member-only story

DNS Rebinding, The treacherous attack it can be
Vuk Ivanovic
Follow
7 min read
·
Jul 25, 2020

116

Truly. An awful, awful thing to stumble upon. And luckily, most of the time you end up stumbling on it by accident, it’s not something that you find on purpose, most of the time. Granted, maybe it picks you to mess with your head, who can tell. Either way, I’ve been through that ringer, around four times… so far. Of four times, only once I actually got it to work.

This won’t be a story of how it worked until it didn’t, or something happened that caused it to stop working properly, etc. This is about how I actually got it to work, I got the results, and…. the aws instance in question didn’t belong to the bbp in question. Go figure.

What is it and how does it work:

First, why would you get into DNS rebinding attack, especially when doing bug hunting? Because you got a HTTP pingback, and bonus points the IP address resolves to aws.

But, what is DNS rebinding attack? In a simplest explanation (there are far longer and prettier visually presented essays, almost, on the subject, but this isn’t that) it is a way to trick a victim (or a headless web browser with javascript support, which is essential) to cause the attacker’s server to connect to it and then quickly to switch into a local IP address. With that “cover” attacker is able to extract internal network information that is usually blocking external IP addresses, but not the local ones. Which, in the case of aws, means that if you mask yourself as a localhost IP address then you will be able to get to…
