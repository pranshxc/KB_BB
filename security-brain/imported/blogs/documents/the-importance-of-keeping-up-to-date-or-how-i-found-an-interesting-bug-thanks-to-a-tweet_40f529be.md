---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-29_the-importance-of-keeping-up-to-date-or-how-i-found-an-interesting-bug-thanks-to.md
original_filename: 2020-08-29_the-importance-of-keeping-up-to-date-or-how-i-found-an-interesting-bug-thanks-to.md
title: The Importance of keeping up to date, or how I found an interesting bug thanks
  to a tweet
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
raw_sha256: 40f529bea71c41ab8f6afd9d6063131ab18042b9b19a109671683b26e3d5e46d
text_sha256: 6b4866baa77a1d6b48f9d7ed5d2a21f0f02c88cd80a9c0c962092a3721842f2c
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# The Importance of keeping up to date, or how I found an interesting bug thanks to a tweet

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-29_the-importance-of-keeping-up-to-date-or-how-i-found-an-interesting-bug-thanks-to.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `40f529bea71c41ab8f6afd9d6063131ab18042b9b19a109671683b26e3d5e46d`
- Text SHA256: `6b4866baa77a1d6b48f9d7ed5d2a21f0f02c88cd80a9c0c962092a3721842f2c`


## Content

---
title: "The Importance of keeping up to date, or how I found an interesting bug thanks to a tweet"
url: "https://medium.com/bugbountywriteup/the-importance-of-keeping-up-to-date-or-how-i-found-an-interesting-bug-thanks-to-a-tweet-2ec6ba9a5e1e"
authors: ["Vuk Ivanovic"]
bugs: ["Stored XSS"]
publication_date: "2020-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4288
scraped_via: "browseros"
---

# The Importance of keeping up to date, or how I found an interesting bug thanks to a tweet

Member-only story

The Importance of keeping up to date, or how I found an interesting bug thanks to a tweet
Vuk Ivanovic
Follow
4 min read
·
Aug 29, 2020

118

1

Press enter or click to view image in full size

During your bug hunting adventures, you may find yourself deep in the cyber mud. Shower of ones and zeros getting you soaked. Failed payload after failed payload making you miserable. Hitting a wall, and I don’t mean firewall, I mean the wall that gets you truly stuck. And, you may think, this is one of those walls that can’t be bypassed, it’s not a waf, it’s mental wall. This article will show that at times there are ways to bypass even those types of walls.

The wall:

A new bug bounty program. How exciting. The endless possibilities of finding all kinds of bugs. Different challenges, but different security holes, possibly, hopefully.

I went in ready for action. I clicked things, I observed my burp history. I tried to understand how the website in question functions. What is its role? How is it meant to be used? How is it meant to respond to users’ activities? And similar, very important questions if you really want to find bugs.

Until… Nothing there. I clicked everything, I tried the usual xss payloads, I tried django related bugs (because the website was built on django), I tried fuzzing user inputs that seemed promising. I found some silly bugs, but too small to matter. There was nothing, and yet, the complex…
