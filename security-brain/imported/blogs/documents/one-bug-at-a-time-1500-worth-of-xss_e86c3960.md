---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-20_one-bug-at-a-time-1500-worth-of-xss.md
original_filename: 2023-09-20_one-bug-at-a-time-1500-worth-of-xss.md
title: 'One Bug at a Time: $1,500 worth of XSS'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: e86c39600cf36c2ecb5a9592f303944a8102b0a3efc43ae76d170e68b0d22124
text_sha256: ec0821c0a52e1c5473928a80355da81524bfb3e123e7d025eced033a3acd4f4a
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# One Bug at a Time: $1,500 worth of XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-20_one-bug-at-a-time-1500-worth-of-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `e86c39600cf36c2ecb5a9592f303944a8102b0a3efc43ae76d170e68b0d22124`
- Text SHA256: `ec0821c0a52e1c5473928a80355da81524bfb3e123e7d025eced033a3acd4f4a`


## Content

---
title: "One Bug at a Time: $1,500 worth of XSS"
url: "https://medium.com/@atomiczsec/one-bug-at-a-time-1-500-worth-of-xss-33455b384b8a"
authors: ["Gavin Kramer (@atomiczsec)"]
bugs: ["Stored XSS", "Reflected XSS"]
bounty: "1,500"
publication_date: "2023-09-20"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 757
scraped_via: "browseros"
---

# One Bug at a Time: $1,500 worth of XSS

Member-only story

One Bug at a Time: $1,500 worth of XSS
Gavin K
Follow
4 min read
·
Sep 20, 2023

210

Welcome back people! Today we will be digging into how to find XSS that others are not finding.

Press enter or click to view image in full size

Bug Number 1: Stored and Reflected XSS on settings page

Looking for a XSS in this site was interesting, no code was popping but I was getting some parsed data like this:

>” 

Instead of my full payload as:

"><img src=x onerror=alert("XSS");>

This meant that the application was taking in my data and not blocking it. From here I went through the entire website seeing if the payload would pop up anywhere else and it did. Upon further investigation, I discovered that the XSS vulnerability I identified on the settings page has a wider impact on the entire website. The issue is related to improper input validation and output encoding, allowing malicious payloads to be executed both in a stored and reflected manner. This meant I could exfiltrate data of the users from their settings page because the data that was shared in the settings page is able to be viewed by other people (Administrators or Researchers).

Impact: This vulnerability poses a significant security risk as it allows attackers to execute arbitrary JavaScript code within the context of other users’ sessions. The potential consequences include:
