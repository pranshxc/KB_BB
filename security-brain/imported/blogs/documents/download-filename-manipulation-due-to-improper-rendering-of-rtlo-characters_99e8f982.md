---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-15_download-filename-manipulation-due-to-improper-rendering-of-rtlo-characters.md
original_filename: 2020-12-15_download-filename-manipulation-due-to-improper-rendering-of-rtlo-characters.md
title: Download Filename Manipulation due to improper rendering of RTLO characters
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 99e8f982aff440e45013f7c3bec8698765d4e7f73b552a2fc8e91a5e56cdfb06
text_sha256: 12f3e5c5bdfe570f8f21997e7291623c2c794844cff31c5a8863443de69aeb0d
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Download Filename Manipulation due to improper rendering of RTLO characters

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-15_download-filename-manipulation-due-to-improper-rendering-of-rtlo-characters.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `99e8f982aff440e45013f7c3bec8698765d4e7f73b552a2fc8e91a5e56cdfb06`
- Text SHA256: `12f3e5c5bdfe570f8f21997e7291623c2c794844cff31c5a8863443de69aeb0d`


## Content

---
title: "Download Filename Manipulation due to improper rendering of RTLO characters"
url: "https://jayateerthag.medium.com/download-filename-manipulation-due-to-improper-rendering-of-rtlo-characters-69e2751a8f28"
authors: ["Jayateertha Guruprasad (@JayateerthaG)"]
bugs: ["RTLO"]
publication_date: "2020-12-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4068
scraped_via: "browseros"
---

# Download Filename Manipulation due to improper rendering of RTLO characters

Download Filename Manipulation due to improper rendering of RTLO characters
Jayateertha Guruprasad
Follow
2 min read
·
Dec 17, 2020

6

2

This is one of the easiest bug that I have found in a private bugbounty program.

The program had two of it’s browsers in it’s scope. I was testing for RTLO related bugs,I found that the downloads section of the browser was rendering the rtlo characters in the improper way.

RTLO characters are “Right-To-Left-Override” characters which is rendered from right to left ,unlike English which is rendered from left to right.

I made a quick POC,

<html>
<head><title></title></head>
<body>
<a href="Link_TO_File_With_RTLO" download>apk rendered as txt file in browser downloads click here</a>
</body>
</html>

I named a file as textfile%E2%80%AEtxt.apk, which is a apk.But when downloaded in those two browser was rendered as textfilekpa.txt due to the improper handling of RTLO characters.

Get Jayateertha Guruprasad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

IMPACT: Victim downloads a file thinking it’s text file but ends up installing malicious apk.

The bug was fixed quickly in a month and a new release was rolled out ,The private program also acknowledged me in their HOF and rewarded a small amount.

Liked my article ? Follow me on twitter (@jayateerthaG) and medium for more content about bugbounty, Infosec, cybersecurity and hacking.

References to similar bugs:

Illegal Rendered at Download Feature in Opera Mini that Lead to Extension Manipulation (with RTLO)
The story while you download a file that looks “legitimate” with its extension, but it changes when you execute the…

medium.com

HackerOne disclosed on HackerOne: Domain spoofing in redirect page...
Summary:** Hello, Domains can be spoofed on redirect page using RTLO. **Description (Include Impact):** Using…

hackerone.com

Snapchat disclosed on HackerOne: RTLO char allowed in chat
Hey all, There seems to be no filtering of strange unicode characters such as U+202E which is an…

hackerone.com
