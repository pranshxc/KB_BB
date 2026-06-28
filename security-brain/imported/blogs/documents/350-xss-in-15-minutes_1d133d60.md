---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-23_350-xss-in-15-minutes.md
original_filename: 2022-12-23_350-xss-in-15-minutes.md
title: $350 XSS in 15 minutes
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
raw_sha256: 1d133d60a97ded424d9ac028c86b3f73502ffc1ed126cfb4d9ccbf6c804bb6c1
text_sha256: 6f135d371ecd633fd27e1bdffcbe444d1cf1e711b80e25ed06a352c37699c824
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# $350 XSS in 15 minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-23_350-xss-in-15-minutes.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `1d133d60a97ded424d9ac028c86b3f73502ffc1ed126cfb4d9ccbf6c804bb6c1`
- Text SHA256: `6f135d371ecd633fd27e1bdffcbe444d1cf1e711b80e25ed06a352c37699c824`


## Content

---
title: "$350 XSS in 15 minutes"
url: "https://therceman.medium.com/350-xss-in-15-minutes-dcb74ad93d5f"
authors: ["Anton (@therceman)"]
bugs: ["DOM XSS", "JSONP"]
bounty: "350"
publication_date: "2022-12-23"
added_date: "2022-12-26"
source: "pentester.land/writeups.json"
original_index: 1741
scraped_via: "browseros"
---

# $350 XSS in 15 minutes

Member-only story

$350 XSS in 15 minutes
Bug Bounty Writeup about DOM XSS via JSONP + Parameter pollution
Anton (therceman)
Follow
3 min read
·
Dec 23, 2022

701

7

Press enter or click to view image in full size
Photo by Pepi Stojanovski on Unsplash

Hello 👋

This is my first and last Bug Bounty Writeup this year. 😀

I am sharing with you my latest XSS finding, which I’ve found 2 weeks ago.

This was the fastest and a bit unusual flow that I normally do when I search for XSS.

So let’s dive in…

Company asked me to retest an old XSS report.
I’ve checked that XSS and confirmed that it was fixed properly.
The specific endpoint had name a param that was vulnerable to Reflected XSS injection.
example.com/profile?name=<img+src=1+onerror=alert(1337)>
I’ve started to search for a bypass and used the Search function in Chrome Developer tools to search this endpoint /profile in all JS files to check for another vulnerable param, but found another endpoint:
example.com/services
The first idea that came to my mind was to put this URL in the google search engine and see if this endpoint was cached somewhere on the google web space with params.
After the first try, I found a cached endpoint with params on the first page of the results, the endpoint had ID…
