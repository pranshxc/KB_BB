---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-16_frequest.md
original_filename: 2022-03-16_frequest.md
title: frequest
category: documents
detected_topics:
- xss
- sqli
- command-injection
tags:
- imported
- documents
- xss
- sqli
- command-injection
language: en
raw_sha256: 398d3f45328fca605b3c20de97f779bee0fbdf647c2a7e5fc7ad63c1cd499776
text_sha256: 3e19bce91521dbe54723b59954fa2d4d0751d98ffbc638e465a01d32c082f397
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# frequest

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-16_frequest.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `398d3f45328fca605b3c20de97f779bee0fbdf647c2a7e5fc7ad63c1cd499776`
- Text SHA256: `3e19bce91521dbe54723b59954fa2d4d0751d98ffbc638e465a01d32c082f397`


## Content

---
title: "frequest"
page_title: "GitHub - takshal/freq: This is go CLI tool for send fast Multiple  get HTTP request. · GitHub"
url: "https://github.com/takshal/freq"
final_url: "https://github.com/takshal/freq"
authors: ["akshal(tojojo)"]
bugs: ["XSS"]
publication_date: "2022-03-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2812
---

# frequest

This is go CLI tool for send fast Multiple get HTTP request.

# How to Use?

you can use this tool for findings xss and sql injection vulnerablity from multi URL.

# How to Install?

go get -u github.com/takshal/freq

or in latest version of go you can use below command

go install github.com/takshal/freq@latest

# smart Use

Using qsreplace you can add your xss payload in every perementer then you can use this tool to find vulnerablity.
