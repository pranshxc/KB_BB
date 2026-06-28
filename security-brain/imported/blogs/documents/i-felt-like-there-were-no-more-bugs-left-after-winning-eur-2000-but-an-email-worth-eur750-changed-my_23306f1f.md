---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-31_i-felt-like-there-were-no-more-bugs-left-after-winning-2000-but-an-email-worth-7.md
original_filename: 2021-03-31_i-felt-like-there-were-no-more-bugs-left-after-winning-2000-but-an-email-worth-7.md
title: I felt like there were no more bugs left after winning € 2000 … But an email
  worth €750 changed my mind
category: documents
detected_topics:
- access-control
- idor
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- idor
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 23306f1fdd2d4ed2e678169d4793ca10ce9a51a4f628414f5df5c632ed1b6fe2
text_sha256: 1ef47b882114d502944ee141308f2b46aebbfb3dc2458a415e1a9762dcbb7f1f
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# I felt like there were no more bugs left after winning € 2000 … But an email worth €750 changed my mind

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-31_i-felt-like-there-were-no-more-bugs-left-after-winning-2000-but-an-email-worth-7.md
- Source Type: markdown
- Detected Topics: access-control, idor, xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `23306f1fdd2d4ed2e678169d4793ca10ce9a51a4f628414f5df5c632ed1b6fe2`
- Text SHA256: `1ef47b882114d502944ee141308f2b46aebbfb3dc2458a415e1a9762dcbb7f1f`


## Content

---
title: "I felt like there were no more bugs left after winning € 2000 … But an email worth €750 changed my mind"
url: "https://thexssrat.medium.com/i-felt-like-there-were-no-more-bugs-left-after-winning-2000-but-an-email-worth-750-changed-my-c7a507649060"
authors: ["Thexssrat (@theXSSrat)"]
bugs: ["Broken Access Control", "IDOR"]
bounty: "2,750"
publication_date: "2021-03-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3781
scraped_via: "browseros"
---

# I felt like there were no more bugs left after winning € 2000 … But an email worth €750 changed my mind

Member-only story

I felt like there were no more bugs left after winning € 2000 … But an email worth €750 changed my mind
Thexssrat
Follow
7 min read
·
Mar 29, 2021

126

1

Introduction

Hello amazing hacker, i hope you are doing well! Today i am going to tell you the story of how i completely exhausted my target … and then some. Not only did i already receive € 2000 from this target in various medium vulnerabilities that i reported, i managed to grab even more after i had already fully tested the program. Here’s how i did it.

Press enter or click to view image in full size
Photo by Luther.M.E. Bottrill on Unsplash
The beginning

This was a target i loved right from the start, it had all the functionality that i loved and seemed tailored made for me. I started up burp suite, set up my scope and started clicking around.

The more i saw, the more i fell in love with this target. It started out with my target asking me if i wanted to invite other people into my organization. Whenever a target asks me this, my spidey senses go tingling. This is usually a sign that there is Broken Access Control (BAC) possible or at the very least multiple ways of testing for IDORs.

I got to work in creating two companies, we will call them “Yoogle” and “Gahoo” to make things easy, but these are just for example and were not my actual targets of course, nor were the companies that inpsired their named. My target was heavily centered…
