---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-22_how-i-discovered-ssrf-on-hackerone-program.md
original_filename: 2023-12-22_how-i-discovered-ssrf-on-hackerone-program.md
title: How I Discovered SSRF on Hackerone Program
category: documents
detected_topics:
- idor
- ssrf
- command-injection
tags:
- imported
- documents
- idor
- ssrf
- command-injection
language: en
raw_sha256: 6a9e5c2271c4e47e2ad43436db8578b9784698ecadf7d0a0426f746ed55338bd
text_sha256: 9d946621e1db46a286eb5dff6595949116dfde3cc8a9eab6e487ffd4dfaf0d5c
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# How I Discovered SSRF on Hackerone Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-22_how-i-discovered-ssrf-on-hackerone-program.md
- Source Type: markdown
- Detected Topics: idor, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `6a9e5c2271c4e47e2ad43436db8578b9784698ecadf7d0a0426f746ed55338bd`
- Text SHA256: `9d946621e1db46a286eb5dff6595949116dfde3cc8a9eab6e487ffd4dfaf0d5c`


## Content

---
title: "How I Discovered SSRF on Hackerone Program"
url: "https://medium.com/@kerstan/how-i-discovered-ssrf-on-hackerone-program-7bbe72334f74"
authors: ["kerstan"]
bugs: ["SSRF"]
publication_date: "2023-12-22"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 598
scraped_via: "browseros"
---

# How I Discovered SSRF on Hackerone Program

1

Press enter or click to view image in full size

Member-only story

Featured

How I Discovered SSRF on Hackerone Program
kerstan
Follow
5 min read
·
Dec 15, 2023

569

1

kerstan - Medium
Read writing from kerstan on Medium. AI | Programming Knowledge | Bug Bounty Hunter X: https://x.com/kerstan_hunter…

medium.com

👉 Subscribed Me.

👉 Follow me: X.

Hi guys, I am Kerstan. Today, I will share you how I discoverd SSRF on hackerone Program.

T
he process of discovering bugs can be lengthy, but the results are often rewarding. Keep trying harder, bro!

If this writing has been helpful to you, please consider giving it a clap and following. Thanks bro.

So, let’s get started.

1. Sensitive endpoint discovered
Press enter or click to view image in full size
Photo by Dayne Topkin on Unsplash

First, I gathered some business information from the Program scope on Hackerone.

I conducted regular tests such as web bug and IDOR, but I found absolutely no opportunity. The filters and authentication mechanisms were very robust, and users were authenticated using uuid as parameters.
