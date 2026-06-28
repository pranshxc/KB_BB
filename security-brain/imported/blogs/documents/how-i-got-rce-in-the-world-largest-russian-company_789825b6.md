---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-20_how-i-got-rce-in-the-world-largest-russian-company.md
original_filename: 2021-08-20_how-i-got-rce-in-the-world-largest-russian-company.md
title: How I got RCE In The World Largest Russian Company
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 789825b6fe0a3fb451e0d79e0b65f27d97a83a984d5f5d84365f2f491f48b0c4
text_sha256: f0bdfd821eaf55d138193c99c79ea84b003e7bc48d2fecc8e7d8bc5c8fa5236a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I got RCE In The World Largest Russian Company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-20_how-i-got-rce-in-the-world-largest-russian-company.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `789825b6fe0a3fb451e0d79e0b65f27d97a83a984d5f5d84365f2f491f48b0c4`
- Text SHA256: `f0bdfd821eaf55d138193c99c79ea84b003e7bc48d2fecc8e7d8bc5c8fa5236a`


## Content

---
title: "How I got RCE In The World Largest Russian Company"
url: "https://infosecwriteups.com/how-i-got-rce-in-the-world-largest-russian-company-8e6e8288bc4e"
authors: ["Sicksec (@OriginalSicksec)"]
programs: ["Mail.ru"]
bugs: ["RCE"]
publication_date: "2021-08-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3406
scraped_via: "browseros"
---

# How I got RCE In The World Largest Russian Company

Member-only story

How I got RCE In The World Largest Russian Company
Thinking outside the box
Sicksec
Follow
3 min read
·
Aug 19, 2021

191

Press enter or click to view image in full size
Photo by Christian Wiediger on Unsplash

Hello Security Researchers & Hackers

In this writeup I will explain how I was able to find RCE in Mail.ru which is considered the world largest internet company,
Before starting to hack I was wondering on how I should approach the target and what most people would miss in the program, they have a huge scope which means it should be something out there sitting for me to find XD

I started looking with the Favicon using This Where I replace the link with the Mail.ru favicon, once generate I go to shodan.io and search for it

Press enter or click to view image in full size

Now we search this hash on shodan.io with the http.favicon.hash syntax

Press enter or click to view image in full size

Now I went to see page by page and look for something suspicious with an unusual port number so I kept going till I found a host with port 8080
That has a Welcome to Nginx page
Once found I wanted to dig further on what’s going on, so I started to FUZZ directories and I…
