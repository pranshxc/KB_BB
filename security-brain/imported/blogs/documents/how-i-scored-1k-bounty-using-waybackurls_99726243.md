---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-02_how-i-scored-1k-bounty-using-waybackurls.md
original_filename: 2021-08-02_how-i-scored-1k-bounty-using-waybackurls.md
title: How I Scored 1K Bounty Using Waybackurls
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 997262435d6e03f605d356249f49d80d141efcbc2d6060ffa9d0c775126cddd2
text_sha256: 5021faed2823e3503a86ed460c908e08667ad6ad9e4f3167cd4e5f2c03ef8bd7
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I Scored 1K Bounty Using Waybackurls

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-02_how-i-scored-1k-bounty-using-waybackurls.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `997262435d6e03f605d356249f49d80d141efcbc2d6060ffa9d0c775126cddd2`
- Text SHA256: `5021faed2823e3503a86ed460c908e08667ad6ad9e4f3167cd4e5f2c03ef8bd7`


## Content

---
title: "How I Scored 1K Bounty Using Waybackurls"
url: "https://infosecwriteups.com/how-i-scored-1k-bounty-using-waybackurls-717d9673ca52"
authors: ["Sicksec (@OriginalSicksec)"]
bugs: ["Information disclosure"]
bounty: "1,000"
publication_date: "2021-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3445
scraped_via: "browseros"
---

# How I Scored 1K Bounty Using Waybackurls

Member-only story

How I Scored 1K Bounty Using Waybackurls
Sicksec
Follow
2 min read
·
Aug 3, 2021

388

4

Approaching a target from all angles

Press enter or click to view image in full size
Photo by Irvan Smith on Unsplash
Hello Security Researchers,Hackers

In this write-up, I want to share with you a finding that I discovered in a public bug bounty program that ended up paying me 1K just using a single command on the terminal

I won’t be able to disclose the name of the program since the leak was huge and they are still merging all the previous algorithm they used before to a new one and the deprecated API is still reachable

The program exist in Hackerone in more than a decade with big names on them, I was familiar with the services they offer since I was a user so I started to enumerate subdomain where I noticed a weird link that may actually hold sensitive data since they are parsing everything in URL path so my first approach was checking the WaybackURLS since 
TomNomNom
 has a very unique tools I used it as follows
waybackurls requests.redacted.com

I was surprise with the amount of URLS that belongs to users with the tokens and I was like no way they’re valid right ?!

Press enter or click to view image in full size
