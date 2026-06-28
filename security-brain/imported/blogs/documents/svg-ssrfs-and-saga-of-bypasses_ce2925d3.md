---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-11_svg-ssrfs-and-saga-of-bypasses.md
original_filename: 2022-04-11_svg-ssrfs-and-saga-of-bypasses.md
title: SVG SSRFs and saga of bypasses
category: documents
detected_topics:
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- command-injection
language: en
raw_sha256: ce2925d3618b461b545d7d4b714d974ac416c01a0084bd96db68ade5fc098b9a
text_sha256: 35cdf98d4173b92d845a7c1b80b9695c6926df55855fe5ee998555d4cadb0dcf
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# SVG SSRFs and saga of bypasses

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-11_svg-ssrfs-and-saga-of-bypasses.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `ce2925d3618b461b545d7d4b714d974ac416c01a0084bd96db68ade5fc098b9a`
- Text SHA256: `35cdf98d4173b92d845a7c1b80b9695c6926df55855fe5ee998555d4cadb0dcf`


## Content

---
title: "SVG SSRFs and saga of bypasses"
url: "https://infosecwriteups.com/svg-ssrfs-and-saga-of-bypasses-777e035a17a7"
authors: ["Preetham Bomma (@cyber01_)"]
bugs: ["SSRF", "HTML injection"]
publication_date: "2022-04-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2727
scraped_via: "browseros"
---

# SVG SSRFs and saga of bypasses

Member-only story

SVG SSRFs and saga of bypasses
Hi all, hope you are keeping well and staying safe. This blog is about my recent experiences with SVG, HTML to PDF SSRF, and bypasses for the patches applied.
Preetham Bomma
Follow
4 min read
·
Apr 11, 2022

347

Introduction

I was testing an app that was a web-based analytics solution that dealt with research institutions worldwide to analyze new, emerging research trends, and create reports.

As the application heavily deals with data analytics, the app had functionalities to show the research data as pie charts, graphs, tables, etc. Reports can also be prepared with the data and shared with co-researchers.

These pie charts, reports, and graphs could be exported to DOCX, PDF, and PNG. You see where I’m going right?

Exploitation

As we learned earlier, the research data is shown in the form of charts. Below is a screenshot for the same.

Press enter or click to view image in full size

To the right of the screenshot, we see the option to “Export the chart as an image”

Upon clicking the “Export chart as an image”, we see a POST request going to with the image content like in the below screenshot.
