---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-07_chaining-an-blind-ssrf-bug-to-get-an-rce.md
original_filename: 2021-04-07_chaining-an-blind-ssrf-bug-to-get-an-rce.md
title: Chaining an Blind SSRF bug to Get an RCE
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: cbe31473ee821d0ef47176755f2346b35bba62ed9bf79d33da356321f5c4741e
text_sha256: 70fa5a2f966184c7f6bd83a279f7a1b489753e98cbe20ac01edf947c511afdb6
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining an Blind SSRF bug to Get an RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-07_chaining-an-blind-ssrf-bug-to-get-an-rce.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `cbe31473ee821d0ef47176755f2346b35bba62ed9bf79d33da356321f5c4741e`
- Text SHA256: `70fa5a2f966184c7f6bd83a279f7a1b489753e98cbe20ac01edf947c511afdb6`


## Content

---
title: "Chaining an Blind SSRF bug to Get an RCE"
url: "https://notifybugme.medium.com/chaining-an-blind-ssrf-bug-to-get-an-rce-92c09de3c0ba"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["Blind SSRF", "RCE"]
publication_date: "2021-04-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3755
scraped_via: "browseros"
---

# Chaining an Blind SSRF bug to Get an RCE

Member-only story

Chaining an Blind SSRF bug to Get an RCE
Santosh Kumar Sha(@killmongar1996)
Follow
3 min read
·
Apr 7, 2021

641

3

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be discussing how I was able to get RCE by using Blind SSRF.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

TOOLS used for the exploitation:

gf (tomnomnom) — https://github.com/tomnomnom/gf
qsreplace(tomnomnom) — https://github.com/tomnomnom/qsreplace)
ffuf — https://github.com/ffuf/ffuf
gau(Corben) — https://github.com/lc/gau
waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls

Background of the Vulnerability:

I always wonder why great bugbounty hunter always tell about chaining the bug. I was doing some recon on target using web achieve I found an blind ssrf on targets with parameter named as “next_image” .

NOW the actual Hunting start:

So, Suppose the target name is example.com and also all subdomain are in scope.Like this

In Scope: *.example.com

While doing some recon on target using web achieve, I extracting all the urls from web achieve using waybackurls and gau . Here is command i used for that

Command used:
