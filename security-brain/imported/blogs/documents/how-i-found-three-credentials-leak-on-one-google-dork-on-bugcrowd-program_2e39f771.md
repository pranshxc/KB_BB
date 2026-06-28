---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-24_how-i-found-three-credentials-leak-on-one-google-dork-on-bugcrowd-program.md
original_filename: 2022-10-24_how-i-found-three-credentials-leak-on-one-google-dork-on-bugcrowd-program.md
title: How I Found Three Credentials Leak on One Google Dork on Bugcrowd program
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
raw_sha256: 2e39f771881e7cefb3dee301b2f28a28471a7a2df33e4b70cc6f266734152d5a
text_sha256: 060466dc3eab5417c9690b4a206de6e98e3e2cf3a16a6168de14830a613155ef
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found Three Credentials Leak on One Google Dork on Bugcrowd program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-24_how-i-found-three-credentials-leak-on-one-google-dork-on-bugcrowd-program.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `2e39f771881e7cefb3dee301b2f28a28471a7a2df33e4b70cc6f266734152d5a`
- Text SHA256: `060466dc3eab5417c9690b4a206de6e98e3e2cf3a16a6168de14830a613155ef`


## Content

---
title: "How I Found Three Credentials Leak on One Google Dork on Bugcrowd program"
url: "https://medium.com/@ittipatjitrada_72022/how-i-found-three-credentials-leak-on-one-google-dork-on-bugcrowd-3dba9a23ace4"
authors: ["Ittipatjitrada (@IttipatJitrada)"]
programs: ["Cengage"]
bugs: ["Information disclosure"]
publication_date: "2022-10-24"
added_date: "2022-11-01"
source: "pentester.land/writeups.json"
original_index: 2005
scraped_via: "browseros"
---

# How I Found Three Credentials Leak on One Google Dork on Bugcrowd program

How I Found Three Credentials Leak on One Google Dork on Bugcrowd program
Ittipatjitrada
Follow
Oct 24, 2022

62

1

Tool

Google Dork

Explain:

Get Ittipatjitrada’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I use Google Dork like

site:example.com ext:pdf

and this time I put specific after dork command like

site:example.com ext:pdf “{keyword}”

I did this one because I want to find specific word in pdf file such as

password
username
ID
Email

And this time I found 3 Credentials Leak

Done
