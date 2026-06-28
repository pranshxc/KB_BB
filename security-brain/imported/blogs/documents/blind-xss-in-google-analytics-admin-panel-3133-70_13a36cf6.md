---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-08_blind-xss-in-google-analytics-admin-panel-313370.md
original_filename: 2021-01-08_blind-xss-in-google-analytics-admin-panel-313370.md
title: Blind XSS in Google Analytics Admin Panel — $3133.70
category: documents
detected_topics:
- xss
- idor
- access-control
- command-injection
tags:
- imported
- documents
- xss
- idor
- access-control
- command-injection
language: en
raw_sha256: 13a36cf654d6fd7c835f7e25ad52c7db7842b9fea2fa82f318ac150c793f2d57
text_sha256: 534f339e265a04480d62d2a98185a949491a829e5e2b83f8641bcace43f71216
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS in Google Analytics Admin Panel — $3133.70

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-08_blind-xss-in-google-analytics-admin-panel-313370.md
- Source Type: markdown
- Detected Topics: xss, idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `13a36cf654d6fd7c835f7e25ad52c7db7842b9fea2fa82f318ac150c793f2d57`
- Text SHA256: `534f339e265a04480d62d2a98185a949491a829e5e2b83f8641bcace43f71216`


## Content

---
title: "Blind XSS in Google Analytics Admin Panel — $3133.70"
url: "https://ashketchum.medium.com/blind-xss-in-google-analytics-admin-panel-3133-70-2185d1cce82a"
authors: ["Ashish Dhone (@ashketchum_16)"]
programs: ["Google"]
bugs: ["Blind XSS"]
bounty: "3,133.70"
publication_date: "2021-01-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4016
scraped_via: "browseros"
---

# Blind XSS in Google Analytics Admin Panel — $3133.70

Member-only story

Blind XSS in Google Analytics Admin Panel — $3133.70
Ashish Dhone
Follow
3 min read
·
Jan 8, 2021

397

1

Introduction

This article is a write up on how I found a Blind XSS in Google Analytics Admin Panel where I was rewarded with $3133.70

Currently I am ranked in Top 200 at Google Hackers Ranking,

Press enter or click to view image in full size

What is Blind XSS

Blind XSS vulnerabilities are a variant of persistent XSS vulnerabilities. They occur when the attacker input is saved by the web server and executed as a malicious script in another part of the application or in another application. For example, an attacker injects a malicious payload into a contact/feedback page and when the administrator of the application is reviewing the feedback entries the attacker’s payload will be loaded. The attacker input can be executed in a completely different application (for example an internal application where the administrator reviews the access logs or the application exceptions).

Vulnerability exploitation

As we all know Google is having large scope to hack and its very difficult to understand where to find bugs and what to hack. So after getting Stored XSS in Google Ads, this time my target was Google Analytics.

It was almost 4–5 days I was testing on Google Analytics, I tried Privilege Escalation, IDOR, Stored XSS, Logical bugs…
