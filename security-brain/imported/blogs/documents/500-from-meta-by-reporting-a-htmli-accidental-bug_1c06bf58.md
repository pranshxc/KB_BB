---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-16_500-from-meta-by-reporting-a-htmliaccidental-bug.md
original_filename: 2024-08-16_500-from-meta-by-reporting-a-htmliaccidental-bug.md
title: 500$ From Meta by reporting a HTMLi(Accidental Bug)
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 1c06bf58a1c4923f8d4a4128a6bded2817fe5bc53ae1ab42d446c7f2455b35a2
text_sha256: c2283a0c8806a78af483bb3639ee7c87cccf8afc869a6c5b315cf9be60c13edf
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# 500$ From Meta by reporting a HTMLi(Accidental Bug)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-16_500-from-meta-by-reporting-a-htmliaccidental-bug.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `1c06bf58a1c4923f8d4a4128a6bded2817fe5bc53ae1ab42d446c7f2455b35a2`
- Text SHA256: `c2283a0c8806a78af483bb3639ee7c87cccf8afc869a6c5b315cf9be60c13edf`


## Content

---
title: "500$ From Meta by reporting a HTMLi(Accidental Bug)"
url: "https://armx64.medium.com/500-from-meta-by-reporting-a-htmli-accidental-bug-fef2e5a0f4c4"
authors: ["A.R Maheer"]
programs: ["Meta / Facebook"]
bugs: ["HTML injection"]
bounty: "500"
publication_date: "2024-08-16"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 64
scraped_via: "browseros"
---

# 500$ From Meta by reporting a HTMLi(Accidental Bug)

500$ From Meta by reporting a HTMLi(Accidental Bug)
Abdur Rahman Maheer
Follow
2 min read
·
Aug 16, 2024

128

4

Press enter or click to view image in full size

This is maybe the shortest article on my medium blog, this is all about a simple “HTMLi on Messenger Group (Nickname)”.

Get Abdur Rahman Maheer’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While casually looking through our community group, I unintentionally tapped on a message. Like always, Messenger revealed the names of those who had read it. One name in the ‘seen’ list stood out as it was noticeably larger than the rest. Initially, I dismissed it as a glitch. However, when I checked the nicknames in the group chat, I discovered that the name displayed in an unusually large font on the ‘seen’ list was actually written in an H1 HTML tag. It wasn’t a glitch; HTML code was being executed within the list of people who had seen the message.

I was unable to show much impact as this was only executing one way, with some restrictions, as i reported meta, they took 14 day to resolve the bug.

Press enter or click to view image in full size

Thanks for reading.
