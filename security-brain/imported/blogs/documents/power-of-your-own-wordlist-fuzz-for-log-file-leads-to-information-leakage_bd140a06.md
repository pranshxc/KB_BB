---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-09_power-of-your-own-wordlist-fuzz-for-log-file-leads-to-information-leakage.md
original_filename: 2021-10-09_power-of-your-own-wordlist-fuzz-for-log-file-leads-to-information-leakage.md
title: Power of Your Own Wordlist — Fuzz for Log File Leads to Information Leakage
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: bd140a0613da848137d35dbaeb67dbb6fe949f3dfe26930e71edaf08749c957f
text_sha256: 6bd1fa5602ee1f43e0fee0031973bc96b72d35b88993397b35445d8dd1aa2885
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Power of Your Own Wordlist — Fuzz for Log File Leads to Information Leakage

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-09_power-of-your-own-wordlist-fuzz-for-log-file-leads-to-information-leakage.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `bd140a0613da848137d35dbaeb67dbb6fe949f3dfe26930e71edaf08749c957f`
- Text SHA256: `6bd1fa5602ee1f43e0fee0031973bc96b72d35b88993397b35445d8dd1aa2885`


## Content

---
title: "Power of Your Own Wordlist — Fuzz for Log File Leads to Information Leakage"
url: "https://mikekitckchan.medium.com/power-of-your-own-wordlist-fuzz-for-log-file-leads-to-information-leakage-ad46958b4729"
authors: ["MikeChan"]
bugs: ["Information disclosure"]
publication_date: "2021-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3254
scraped_via: "browseros"
---

# Power of Your Own Wordlist — Fuzz for Log File Leads to Information Leakage

Member-only story

Power of Your Own Wordlist — Fuzz for Log File Leads to Information Leakage
MikeChan
Follow
3 min read
·
Oct 9, 2021

40

1

Press enter or click to view image in full size
Photo by Roman Kraft on Unsplash

This is another story of my recent finding of sensitive information leakage. The target is a big hotel and resort Group which has operation in over 10 countries over the world. As I am not allowed to disclose the detail, I would use redacted.com as the target site and all parameters and directories shown in below passage are all made up.

This passage mainly about how I use my own wordlist to find this sensitive endpoint and how you can make a wordlist on your own. So, let’s begin:

Recon

During Recon stage, I found a subdomain called api.redacted.com. So, I try to access api.redacted.com but it returns 404. But it arouse my interest of what may contain in the subdomain. Thus, I decided to fuzz this subdomain mainpoint using ffuf.

Fuzzing

In case you are not familiar with ffuf, you may refer to my previous story about it. I then fuzz the endpoints of this subdomain like this:

ffuf -u https://api.redacted.com/FUZZ -w wordlist.txt

I currently maintained a bunch of wordlist myself. Most of these are recorded from my previous research work. In one of the wordlists of sensitive information disclosure, I found that the below endpoint returns 200:
