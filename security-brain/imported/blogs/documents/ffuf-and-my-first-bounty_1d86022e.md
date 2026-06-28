---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-29_ffuf-and-my-first-bounty.md
original_filename: 2020-07-29_ffuf-and-my-first-bounty.md
title: FFUF and my first bounty
category: documents
detected_topics:
- sqli
- idor
- xss
- command-injection
- clickjacking
- information-disclosure
tags:
- imported
- documents
- sqli
- idor
- xss
- command-injection
- clickjacking
- information-disclosure
language: en
raw_sha256: 1d86022e8191d3034c9ea0b940f8038e2726a877025c2684bbcf0c2ebae7175c
text_sha256: 7b4688f052d59d1cfa0332cf59f4c3d58aa5562a39346b8549f6cc46ba34c7af
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# FFUF and my first bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-29_ffuf-and-my-first-bounty.md
- Source Type: markdown
- Detected Topics: sqli, idor, xss, command-injection, clickjacking, information-disclosure
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `1d86022e8191d3034c9ea0b940f8038e2726a877025c2684bbcf0c2ebae7175c`
- Text SHA256: `7b4688f052d59d1cfa0332cf59f4c3d58aa5562a39346b8549f6cc46ba34c7af`


## Content

---
title: "FFUF and my first bounty"
url: "https://medium.com/bugbountywriteup/my-first-bug-bounty-21d3203ffdb0"
authors: ["Suryansh Mansharamani"]
bugs: ["Information disclosure"]
bounty: "300"
publication_date: "2020-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4374
scraped_via: "browseros"
---

# FFUF and my first bounty

Top highlight

Member-only story

FFUF and my first bounty
The beauty of leaked files
suryansh
Follow
4 min read
·
Jul 29, 2020

577

3

Bug bounty hunting is hard.

Photo by Markus Spiske on Unsplash

Especially when you start off, it’s extremely hard. Don’t believe me? Look at this:

Yes, I’ve found some really shitty vulnerabilities, including clickjacking on static pages. Yes, I’ve reported clickjacking without any significant impact. But, at the same time, my first actual valid report was SQL Injection, something definitely rare nowadays, at least in public programs. Guess that’s progress.

Luckily, I was able to find more bugs, and got even more points, just no bounty, yet.

So, what do I recommend?

XSS is huge right now, and it definitely should be one of the top 5 things you should test for along with stuff like IDORS, HTTP Request Smuggling and SQLi. My first bounty wasn’t for any of those. To be honest, there isn’t a single report on H1, at least in my knowledge and by hours of searching, for the vulnerability I found. So what does this mean? It’s probably something overlooked, considering it’s a P4 or P3. Although the overall classification itself is Sensitive Data Exposure, it’s at the following endpoint:

/debug/pprof/
