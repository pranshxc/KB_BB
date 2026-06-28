---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-20_how-i-found-29-stored-xss-in-modern-framework.md
original_filename: 2022-11-20_how-i-found-29-stored-xss-in-modern-framework.md
title: How i found 29 stored XSS in modern framework
category: documents
detected_topics:
- xss
- idor
- command-injection
tags:
- imported
- documents
- xss
- idor
- command-injection
language: en
raw_sha256: 554ad7b3ca52990cb021ecffd7a228407efce9f568d13a96ad5e7d0ee21e739a
text_sha256: 101f58acf1f1c47c3070540787ee7ad41a2f780c37cad18ae7b112be4f2ad6ce
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# How i found 29 stored XSS in modern framework

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-20_how-i-found-29-stored-xss-in-modern-framework.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `554ad7b3ca52990cb021ecffd7a228407efce9f568d13a96ad5e7d0ee21e739a`
- Text SHA256: `101f58acf1f1c47c3070540787ee7ad41a2f780c37cad18ae7b112be4f2ad6ce`


## Content

---
title: "How i found 29 stored XSS in modern framework"
url: "https://dewcode.medium.com/how-i-found-29-stored-xss-in-modern-framework-1cfe60a107a0"
authors: ["Dewanand Vishal (@dewcode91)"]
bugs: ["Stored XSS"]
publication_date: "2022-11-20"
added_date: "2022-11-22"
source: "pentester.land/writeups.json"
original_index: 1887
scraped_via: "browseros"
---

# How i found 29 stored XSS in modern framework

Top highlight

How i found 29 stored XSS in modern framework
Dewanand Vishal
Follow
3 min read
·
Nov 20, 2022

289

1

Press enter or click to view image in full size

XSS is a most common vulnerability. It is easy to learn for a beginner but when it comes to modern applications then it makes hard for us to find and exploit. In this article i will share my story, how i was able to find a lot of XSS in modern applications.

Get Dewanand Vishal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I got a private program on Intigriti 3 months ago. When I looked at the Overall stats, 78 submissions have already been made by other researchers.

Press enter or click to view image in full size
Input validation

I decided to test the application and put my all payloads each and every endpoints. like comments, names fields and other endpoints.

Most of the applications implement input validation as first line of the defence. They filter the common html attributes like Angle brackets (< >) and script tag. So firing payloads blindly in generally not worked. I failed to get XSS on any endpoint.

Press enter or click to view image in full size

I put these three payloads each and every endpoints.

"style="position:fixed;top:0;left:0;border:999em solid green;" onmouseover="alert(document.domain)"
{{_c.constructor('alert(1)')()}}
{{constructor.constructor('alert(1)')()}}
XSS on First name, Surname, Info text
Press enter or click to view image in full size

When i put these payloads and save, i didn’t get any pop-up on screen, then i refresh the page and i got pop-up on my screen with green background.

Press enter or click to view image in full size

I spent 3 months in this program and found 29 stored XSS and 20 IDORs.

Press enter or click to view image in full size

Because this was a private program, i can’t disclose the other endpoints. after 3 months, i hit the leaderboard and now i am in the first position.

Press enter or click to view image in full size

Bug bounty tips:

Deep dive into application functionality.
Put your payload each and every endpoint.
Understand the application defence mechanism.

Reference:

Cheatsheet: XSS that works in 2021
It's been a year since my last XSS cheatsheet, and a year of developments in XSS exploitology. Here's a new and updated…

netsec.expert
