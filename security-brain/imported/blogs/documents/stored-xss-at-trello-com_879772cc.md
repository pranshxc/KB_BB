---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-04_stored-xss-at-trellocom.md
original_filename: 2021-03-04_stored-xss-at-trellocom.md
title: Stored XSS at Trello.com
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
raw_sha256: 879772cc6a248ebc805c997ed93e25289ba2744c7dfaf15c24572e422d2007a6
text_sha256: 8f2421f402d041ba7eacb953c3ba76fda00a4f8e39c347c935f6c9ffad58b204
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS at Trello.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-04_stored-xss-at-trellocom.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `879772cc6a248ebc805c997ed93e25289ba2744c7dfaf15c24572e422d2007a6`
- Text SHA256: `8f2421f402d041ba7eacb953c3ba76fda00a4f8e39c347c935f6c9ffad58b204`


## Content

---
title: "Stored XSS at Trello.com"
url: "https://maordayanofficial.medium.com/stored-xss-at-trello-com-ef2e3d1ed24b"
authors: ["Maor Dayan (@mord1234)"]
programs: ["Trello"]
bugs: ["Stored XSS"]
publication_date: "2021-03-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3842
scraped_via: "browseros"
---

# Stored XSS at Trello.com

Stored XSS at Trello.com
Maor Dayan - מאור דיין
Follow
2 min read
·
Mar 3, 2021

140

First let’s start with what is Trello?

Trello is a web-based, Kanban-style, list-making application and is a subsidiary of Atlassian.[5] Originally created by Fog Creek Software in 2011, it was spun out to form the basis of a separate company in 2014[6][7] and later sold to Atlassian in January 2017.[8] The company is based in New York City, U.S.[9] - Wikipedia

Press enter or click to view image in full size

Vulnerabilities:
1. Stored XSS — Stored XSS, also known as persistent XSS, is the more damaging of the two. It occurs when a malicious script is injected directly into a vulnerable web application. “imperva”

_________________________________________________________________

Get Maor Dayan - מאור דיין’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found out by looking around the site that i can upload and open SVG files without getting blocked or auto redirected to the download of the file, so i created a SVG file with an XSS payload inside. this is how it looks :

Press enter or click to view image in full size

This code is a normal code of an SVG file but with a JavaScript code in it, you can see it below:

<script type=”text/javascript”>

alert(document.domain);

</script>

_________________________________________________________________

PoC video

This has been reported and Trello Team response and fix for this vulnerability was very quick!

Press enter or click to view image in full size

Maor Dayan.
