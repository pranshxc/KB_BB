---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-08_hackerone-redacted-usernames-disclosure-in-export-as-pdf-feature.md
original_filename: 2023-08-08_hackerone-redacted-usernames-disclosure-in-export-as-pdf-feature.md
title: HackerOne redacted usernames disclosure in “Export as .pdf” feature
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
raw_sha256: 5f3cf77871991f0bc975566b986e051d0c71beff15ba4b4665235d407a63a6f2
text_sha256: 846ea5424ec069cf25adc5be8f567fbc97639717935a1625463d4b0b2c9c2057
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# HackerOne redacted usernames disclosure in “Export as .pdf” feature

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-08_hackerone-redacted-usernames-disclosure-in-export-as-pdf-feature.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `5f3cf77871991f0bc975566b986e051d0c71beff15ba4b4665235d407a63a6f2`
- Text SHA256: `846ea5424ec069cf25adc5be8f567fbc97639717935a1625463d4b0b2c9c2057`


## Content

---
title: "HackerOne redacted usernames disclosure in “Export as .pdf” feature"
url: "https://medium.com/pinoywhitehat/redacted-usernames-disclosure-in-export-as-pdf-feature-d00ce3f3e2fc"
authors: ["Japz Divino (@japzdivino)"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2023-08-08"
added_date: "2023-08-14"
source: "pentester.land/writeups.json"
original_index: 875
scraped_via: "browseros"
---

# HackerOne redacted usernames disclosure in “Export as .pdf” feature

Member-only story

HackerOne redacted usernames disclosure in “Export as .pdf” feature
Japz Divino
Follow
4 min read
·
Aug 7, 2023

132

Severity: Low (3.4)
Weakness: Sensitive Information Disclosure
Bounty: $500

Hello hunters! I just want to share these new findings on the HackerOne bug bounty platform.

First, I just wanna let you know that I disagree with the rated severity being Low here, but I always respect the team’s decision and final call despite disagreement arising on the report, so I requested a public disclosure for you guys to have full context on the vulnerability report.

Let’s start and make the write-up straight to the point :)

While browsing on HackerOne export report, I observed a new feature called “I want to redact all usernames”.

UI for “I want to redact all usernames” feature
https://hackerone.com/reports/<REPORT-ID>.pdf?redact_usernames=true&pdf_type=reporter

By analyzing the new feature, this means that a user can share the report with anyone but have the option to not disclosed all involved participants’ usernames (maybe for some reason). Please note that the report can be non-disclosed or private reports.

So I proceeded with exporting one of my reports but the .pdf file is a little bit messy.
