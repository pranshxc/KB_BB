---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-11_finding-reflected-xss-in-a-strange-way.md
original_filename: 2022-11-11_finding-reflected-xss-in-a-strange-way.md
title: Finding Reflected XSS In A Strange Way
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 17297ec9e26602aff7ed2f5aa0548cd773d004953cd8f36570318b78ea3f3f3e
text_sha256: 9257a347fc64c7acec2ccbc12ea7a85233a82ee294de15a1c244d79790211341
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Finding Reflected XSS In A Strange Way

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-11_finding-reflected-xss-in-a-strange-way.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `17297ec9e26602aff7ed2f5aa0548cd773d004953cd8f36570318b78ea3f3f3e`
- Text SHA256: `9257a347fc64c7acec2ccbc12ea7a85233a82ee294de15a1c244d79790211341`


## Content

---
title: "Finding Reflected XSS In A Strange Way"
url: "https://medium.com/@raymond-lind/finding-reflected-xss-in-a-strange-way-289a4f3fa630"
authors: ["Raymond Lind"]
bugs: ["XSS"]
publication_date: "2022-11-11"
added_date: "2022-11-14"
source: "pentester.land/writeups.json"
original_index: 1920
scraped_via: "browseros"
---

# Finding Reflected XSS In A Strange Way

Member-only story

Finding Reflected XSS In A Strange Way
Raymond Lind
Follow
9 min read
·
Nov 11, 2022

34

Press enter or click to view image in full size

Today I will be talking about finding a reflected XSS (“Cross Site Scripting”) vulnerability in a very popular bug bounty program and walk through the details regarding how I came to find this bug and why it was a very interesting finding which may be the first of its kind.

Overview

Throughout this post, I will be going over the details of how I found an XSS vulnerability on a bug bounty program this year. Bug bounty programs or BBPs are companies that allow ethical hackers to analyze their software/application and attempt to find vulnerabilities either for an award, recognition, or experience.

This bug came to me while actually utilizing a website for personal purposes, this was because I decided to still pay attention to details and see if I could find any strange behavior while using the site regularly. Which resulted in a great outcome since I came across this very strange bug which was considered a high severity issue by their team. For those who are unaware, we will first go over what exactly an XSS attack is and how it’s leveraged by attackers.

What Are XSS Attacks?

XSS (Cross-Site Scripting) is a vulnerability in which attackers are able to provide input into an application that includes a javascript payload to break out of the intended code context…
