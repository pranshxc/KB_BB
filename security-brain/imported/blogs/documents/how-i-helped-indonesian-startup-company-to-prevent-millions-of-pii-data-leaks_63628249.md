---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-10_how-i-helped-indonesian-startup-company-to-prevent-millions-of-pii-data-leaks.md
original_filename: 2024-01-10_how-i-helped-indonesian-startup-company-to-prevent-millions-of-pii-data-leaks.md
title: How I Helped Indonesian Startup Company to Prevent Millions of PII Data Leaks
category: documents
detected_topics:
- access-control
- mobile-security
- command-injection
- information-disclosure
tags:
- imported
- documents
- access-control
- mobile-security
- command-injection
- information-disclosure
language: en
raw_sha256: 636282494d5bb5fc76a076510dbfcd09b58d64f95e7cd02b78582e3b0d98a5ef
text_sha256: 4a3f87685fb0c37d6d54fe7e12cb0a81012b7f0222a63e6a831d833195a370f9
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# How I Helped Indonesian Startup Company to Prevent Millions of PII Data Leaks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-10_how-i-helped-indonesian-startup-company-to-prevent-millions-of-pii-data-leaks.md
- Source Type: markdown
- Detected Topics: access-control, mobile-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `636282494d5bb5fc76a076510dbfcd09b58d64f95e7cd02b78582e3b0d98a5ef`
- Text SHA256: `4a3f87685fb0c37d6d54fe7e12cb0a81012b7f0222a63e6a831d833195a370f9`


## Content

---
title: "How I Helped Indonesian Startup Company to Prevent Millions of PII Data Leaks"
url: "https://medium.com/@blackarazi/how-i-helped-indonesian-startup-company-to-prevent-millions-of-pii-data-leaks-55ef3edbd35d"
authors: ["Azhari Harahap (@blackarazi)"]
bugs: ["Android", "Broken Access Control", "Information disclosure"]
bounty: "500"
publication_date: "2024-01-10"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 564
scraped_via: "browseros"
---

# How I Helped Indonesian Startup Company to Prevent Millions of PII Data Leaks

Member-only story

How I Helped Indonesian Startup Company to Prevent Millions of PII Data Leaks
Azhari Harahap
Follow
6 min read
·
Jan 10, 2024

215

2

Press enter or click to view image in full size
Indonesian Startup Company PII Leaks

Hello everyone,

In this post, I will show you how I discovered a vulnerability in one of the Indonesian Startup Companies that could lead to a Personal Identifiable Information (PII) data leak containing the user's name or email address. By abusing this vulnerability, an attacker could fetch 100 users in one request of a unique query, and based on the total_data data from the response it likely contains millions of users' data.

Who is the target?

The target asked me to not disclose the company name so let’s call it Company X.

Reconnaissance

Reconnaissance is the first phase of a penetration testing engagement. It involves gathering information about the target system or network that is going to be tested. The goal of reconnaissance is to gather as much information as possible about the target so that the penetration tester can understand the target system’s architecture, identify potential vulnerabilities, and develop an attack strategy. The reconnaissance phase is crucial because it helps the tester to understand the target better and to plan their attack accordingly.

Company X is primarily a mobile-based app (Android & iOS), but it also has a web-based app version…
