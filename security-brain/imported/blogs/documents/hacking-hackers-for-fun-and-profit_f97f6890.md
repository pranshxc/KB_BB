---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-09_hacking-hackers-for-fun-and-profit.md
original_filename: 2023-01-09_hacking-hackers-for-fun-and-profit.md
title: Hacking Hackers for fun and profit
category: documents
detected_topics:
- xss
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: f97f68909ab4d985d497a7de6c838f5ed6a78709ea2dca69b7ca435eec3f0551
text_sha256: b723c96c77ab53ed42ed5833e72bd4c70c9260c963952e3c88268002684f4767
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Hackers for fun and profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-09_hacking-hackers-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `f97f68909ab4d985d497a7de6c838f5ed6a78709ea2dca69b7ca435eec3f0551`
- Text SHA256: `b723c96c77ab53ed42ed5833e72bd4c70c9260c963952e3c88268002684f4767`


## Content

---
title: "Hacking Hackers for fun and profit"
url: "https://krevetk0.medium.com/hacking-hackers-for-fun-and-profit-784e6c7897e8"
authors: ["Valeriy Shevchenko (@Krevetk0Valeriy)"]
bugs: ["Self-XSS", "Blind XSS"]
bounty: "5,000"
publication_date: "2023-01-09"
added_date: "2023-01-11"
source: "pentester.land/writeups.json"
original_index: 1688
scraped_via: "browseros"
---

# Hacking Hackers for fun and profit

Member-only story

Hacking Hackers for fun and profit
Valeriy Shevchenko
Follow
6 min read
·
Jan 9, 2023

116

2

This story will be in several parts. In each of the situations, I had to face unexpected results. By and large, these are stories that have arisen from the exploitation of the XSS vulnerability in wildlife. I hope you find something useful in these stories.

Press enter or click to view image in full size
Self XSS as a Critical Vulnerability

Many of you know that there are several types of XSS vulnerabilities. And most of you will think that Self XSS is hard to consider a valid vulnerability. Especially to be accepted on the bug bounty. Moreover, almost no one can believe that the Self XSS can become a critical problem. But one day it did.

A few years ago I decided to update my LinkedIn profile and just out of curiosity I put a Blind XSS in the skills area of my profile.

Press enter or click to view image in full size

Nothing happened for a year. But a year later I got a very interesting result. I got a huge list of people from the security industry for my region in the XSS Hunter panel. There were names, addresses, and phone numbers. All the things you could call PII Data. And the surprising thing was something else. The javascript execution didn’t happen somewhere on Linkedin’s own internal systems. It happened…
