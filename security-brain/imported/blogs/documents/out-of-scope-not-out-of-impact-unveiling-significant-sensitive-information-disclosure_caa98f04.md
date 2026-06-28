---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-23_out-of-scope-not-out-of-impact-unveiling-significant-sensitive-information-discl.md
original_filename: 2023-12-23_out-of-scope-not-out-of-impact-unveiling-significant-sensitive-information-discl.md
title: 'Out-of-Scope, Not Out-of-Impact: Unveiling Significant Sensitive Information
  Disclosure'
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: caa98f04c864b909792452675bab609404c41eba896f17393eefe253d85c254a
text_sha256: 22c927c079ef6665593b94a63db033da83a0deb8aa1529232b83cbadbc972ca2
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Out-of-Scope, Not Out-of-Impact: Unveiling Significant Sensitive Information Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-23_out-of-scope-not-out-of-impact-unveiling-significant-sensitive-information-discl.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `caa98f04c864b909792452675bab609404c41eba896f17393eefe253d85c254a`
- Text SHA256: `22c927c079ef6665593b94a63db033da83a0deb8aa1529232b83cbadbc972ca2`


## Content

---
title: "Out-of-Scope, Not Out-of-Impact: Unveiling Significant Sensitive Information Disclosure"
url: "https://padsalatushal.medium.com/out-of-scope-not-out-of-impact-unveiling-significant-sensitive-information-disclosure-c8e76c1806e8"
authors: ["Padsala Tushal (@PadsalaTushal)"]
bugs: ["Information disclosure"]
publication_date: "2023-12-23"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 597
scraped_via: "browseros"
---

# Out-of-Scope, Not Out-of-Impact: Unveiling Significant Sensitive Information Disclosure

Out-of-Scope, Not Out-of-Impact: Unveiling Significant Sensitive Information Disclosure
Padsala Tushal
Follow
2 min read
·
Dec 23, 2023

120

As a bug bounty hunter, navigating the complexities of subdomain vulnerabilities often leads to intriguing discoveries. One such revelation, though initially deemed out of scope, unearthed a significant vulnerability with unforeseen implications.

The Discovery

I was invited in private program on yeswehack. The program have small scope not wildcard scope. i struggle to get time to hunt mannually because of collage exam. but still i ran my recontool for getting recon data like subdomains and sensitive information disclosure on wildcard domain. i knew that it is better to look in wildcard subdomains because program scope and assest are small. it is not big funcationlity webapp. Reconscript took bit long time on my vps.

Get Padsala Tushal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The next day i check recon output and i found wp-config.php.old file exposes critical database credentials and cryptographic keys, which could potentially be exploited to gain unauthorized access to sensitive data or manipulate the target’s WordPress installation.

Press enter or click to view image in full size

i knew that it is out of scope finding but still i reported with well written impact. and after few days i got accepted as medium severity and i got half of half of normal reward amount.

Press enter or click to view image in full size

Timeline:

18/11/2023: Discovery and Reported

20/11/2023: Under Review

01/12/2023: Accepted and got Reward
