---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-25_first-valid-bug-finding-at-microsoft-and-i-got-the-acknowledgments-page-microsof.md
original_filename: 2022-01-25_first-valid-bug-finding-at-microsoft-and-i-got-the-acknowledgments-page-microsof.md
title: First Valid BUG Finding At Microsoft And I Got the Acknowledgments Page Microsoft
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
raw_sha256: c8a54ef0ac00a6f2a0b3913e3af17dced5581489be7dda8486f5d8eabfb77055
text_sha256: 8b467b0c290c36cc479d893bf41e0b0bb34b44eb4dcac5da72569ca5482c1f4b
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# First Valid BUG Finding At Microsoft And I Got the Acknowledgments Page Microsoft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-25_first-valid-bug-finding-at-microsoft-and-i-got-the-acknowledgments-page-microsof.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `c8a54ef0ac00a6f2a0b3913e3af17dced5581489be7dda8486f5d8eabfb77055`
- Text SHA256: `8b467b0c290c36cc479d893bf41e0b0bb34b44eb4dcac5da72569ca5482c1f4b`


## Content

---
title: "First Valid BUG Finding At Microsoft And I Got the Acknowledgments Page Microsoft"
url: "https://aidilarf.medium.com/first-valid-bug-finding-at-microsoft-and-i-got-the-acknowledgments-page-microsoft-a2c185c53074"
authors: ["Aidil Arief"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2022-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2984
scraped_via: "browseros"
---

# First Valid BUG Finding At Microsoft And I Got the Acknowledgments Page Microsoft

First Valid BUG Finding At Microsoft And I Got the Acknowledgments Page Microsoft
Aidil Arief
Follow
3 min read
·
Jan 25, 2022

68

1

Hi Everyone.

This time I would like to share an article about the findings of the XSS STORED Vulnerability in one of Microsoft Forum subdomains, namely https://powerusers.microsoft.com/ .

This is my first vulnerability finding in the Microsoft Security Response Center Program (MSRC). And at that time I tried to do an XSS search on all Microsoft subdomains, and the result I did not get any XSS there.

Finding 1 valid vulnerability opening was incredibly difficult, and I decided to just give up.

Until one day I found a post by another Bug Hunter Researcher on one of the Social Media Platforms that uploaded the XSS bug finding at Microsoft, it took me by surprise. Because it’s so easy for them to find XSS there. And that made me excited again to look for XSS there, until finally I found one of the Microsoft Forum subdomains in the form of https://powerusers.microsoft.com/.

At https://powerusers.microsoft.com/ I found many “POST QUESTIONS” upload features. Without waiting long, I tried to find XSS there.

Initially I tried POST QUESTIONS in URL :

https://powerusers.microsoft.com/t5/forums/postpage/choose-node/true/board-id/BuildingFlows?message-subject=undefined

In the Questions form I entered the XSS Payload in the “Subject” section.

Press enter or click to view image in full size

Let’s see the result :

Press enter or click to view image in full size

Turns out it’s not vulnerable. I tried POST QUESTIONS on another Form, and it’s the same, the TEXT output that carries the XSS payload in “Subject” is already sanitized or filtered.

Get Aidil Arief’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Until finally I found one of the forms there, where the form displays the IFRAME of the Youtube Video. I think it might be vulnerable, because the TEXT output carrying the XSS payload is definitely not sanitized there.

Here’s the screenshot :

Press enter or click to view image in full size

Let’s see the result :

Press enter or click to view image in full size

Look, it turns out I was right. There Output Text carrying XSS content in the “Title” Form is not sanitized or filtered, so plain text carrying XSS content will be treated as HTML, then XSS is triggered.

Without waiting long, I then reported this finding to the MSRC Team via https://msrc.microsoft.com/create-report

It was great to find the first bug at Microsoft.

Timeline :

Report : Dec 6, 2021

Review/Repro : Dec 7, 2021

Develop : Dec 13, 2021

PreRelease : Jan 13, 2022

Complete : Jan 13, 2022
