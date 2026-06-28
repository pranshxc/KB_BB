---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-28_url-redirection-to-dom-xss-on-hackerone-programs-bug-bounty-tuesday.md
original_filename: 2023-12-28_url-redirection-to-dom-xss-on-hackerone-programs-bug-bounty-tuesday.md
title: URL Redirection To DOM XSS on Hackerone Programs — Bug Bounty Tuesday
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 8a0c5f46ad1b36d06949597bdb129318ec1a3f27d25589a0ca8800405abbc818
text_sha256: c3bfefacf8c74ac0aa633feb2c700866a6634996c0511ad089ea0d7002ca2c82
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# URL Redirection To DOM XSS on Hackerone Programs — Bug Bounty Tuesday

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-28_url-redirection-to-dom-xss-on-hackerone-programs-bug-bounty-tuesday.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `8a0c5f46ad1b36d06949597bdb129318ec1a3f27d25589a0ca8800405abbc818`
- Text SHA256: `c3bfefacf8c74ac0aa633feb2c700866a6634996c0511ad089ea0d7002ca2c82`


## Content

---
title: "URL Redirection To DOM XSS on Hackerone Programs — Bug Bounty Tuesday"
page_title: "Exploiting URL Redirection to DOM XSS on HackerOne | Medium"
url: "https://medium.com/@kerstan/dom-xss-on-hackerone-programs-bug-bounty-tuesday-8973ecf6af95"
authors: ["kerstan"]
bugs: ["DOM XSS", "Open redirect"]
publication_date: "2023-12-28"
added_date: "2024-01-02"
source: "pentester.land/writeups.json"
original_index: 591
scraped_via: "browseros"
---

# URL Redirection To DOM XSS on Hackerone Programs — Bug Bounty Tuesday

Press enter or click to view image in full size

Member-only story

URL Redirection To DOM XSS on Hackerone Programs
Exploiting URL Redirection to DOM XSS on HackerOne
kerstan
Follow
3 min read
·
Dec 27, 2023

108

2

kerstan - Medium
Read writing from kerstan on Medium. AI | Programming Knowledge | Bug Bounty Hunter X: https://x.com/kerstan_hunter

medium.com

👉 Subscribed Me.

👉 Follow me: X.

Hello everyone, I am excited to introduce a new series I’ve been preparing titled ‘Bug Bounty Tuesdays’, where each week I’ll be sharing an article discussing vulnerabilities, bug bounties, or related tools. I hope to sustain this series and if you find these pieces useful, feel free to follow or cap me.

In today’s piece, I’d like to delve into the process of uncovering a DOM xss bug bounty, a fascinating case from the past. So, let’s dive right in.

1 Find Endpoint

While engaging with burp history, I spotted a link, https://XXX/qrcode?k=url&v=https://testtest.com/&s=0. I proceeded with examining its front-end code and observed that:

It retrieves the values of parameters `k` and `v`.
When `k` equals `url`, The value of `v` is fed into the handleUrl function for processing.
