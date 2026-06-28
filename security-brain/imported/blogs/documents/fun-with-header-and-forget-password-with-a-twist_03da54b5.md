---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-18_fun-with-header-and-forget-password-with-a-twist.md
original_filename: 2020-08-18_fun-with-header-and-forget-password-with-a-twist.md
title: 'Fun with header and forget password, with a twist:'
category: documents
detected_topics:
- password-reset
- ssrf
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- password-reset
- ssrf
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: 03da54b576438fae4346987a93f42e503fb46062735e9f877f465594b901e065
text_sha256: e85cc250bfc5c8cc0838ea9ad2aacabd727a4651c707498f5d0015a1a5a44ae3
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Fun with header and forget password, with a twist:

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-18_fun-with-header-and-forget-password-with-a-twist.md
- Source Type: markdown
- Detected Topics: password-reset, ssrf, command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `03da54b576438fae4346987a93f42e503fb46062735e9f877f465594b901e065`
- Text SHA256: `e85cc250bfc5c8cc0838ea9ad2aacabd727a4651c707498f5d0015a1a5a44ae3`


## Content

---
title: "Fun with header and forget password, with a twist:"
url: "https://medium.com/bugbountywriteup/fun-with-header-and-forget-password-with-a-twist-af095b426fb2"
authors: ["Vuk Ivanovic"]
bugs: ["Password reset", "Host header injection"]
publication_date: "2020-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4307
scraped_via: "browseros"
---

# Fun with header and forget password, with a twist:

Member-only story

Fun with header and forget password, with a twist:
Vuk Ivanovic
Follow
4 min read
·
Aug 18, 2020

112

Headers are quite something to play with. The most usual ones are X-Forwarded-For (usually used for waf bypass), and X-Forwarded-Host (personally, interesting one for achieving dns/http pingbacks, sometimes ssrf).

This article will cover the case where I was able to use one of those headers to trick the website to send a forget password link that included the domain of my choosing.

X-Forwarded-Host and forgot password link, with a not so fun twist:

Spoiler alert, the twist, together with the nature of this bug, resulted in a lower payout, much lower than if it weren’t for the said twist.

The initial phase:

This one is easy to test for, but easy to miss testing for. To be honest, without going through twitter and finding this through #BugBountyTip

---For waf bypass, and similar---
X-Forwarded-Host
X-Forwarded-Port
X-Forwarded-Scheme
Origin: null
Origin: [siteDomain].attacker.com
X-Frame-Options: Allow
X-Forwarded-For: 127.0.0.1
X-Client-IP: 127.0.0.1
Client-IP: 127.0.0.1
