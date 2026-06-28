---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-06_how-i-found-open-redirect-on-bug-crowd-public-program-in-2-day.md
original_filename: 2022-07-06_how-i-found-open-redirect-on-bug-crowd-public-program-in-2-day.md
title: How I found Open redirect on Bug crowd public program in 2 day
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: a106d1841784649aa55104dbc14d451bcbd4630d9aefb8382220cf33209e2dfc
text_sha256: 2eb61b7b5c37b1380256bb443bfae6cfcdce83efd0900da7903b7baf130fcd73
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# How I found Open redirect on Bug crowd public program in 2 day

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-06_how-i-found-open-redirect-on-bug-crowd-public-program-in-2-day.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `a106d1841784649aa55104dbc14d451bcbd4630d9aefb8382220cf33209e2dfc`
- Text SHA256: `2eb61b7b5c37b1380256bb443bfae6cfcdce83efd0900da7903b7baf130fcd73`


## Content

---
title: "How I found Open redirect on Bug crowd public program in 2 day"
url: "https://medium.com/@ittipatjitrada_72022/how-i-found-open-redirect-on-bug-crowd-public-program-in-2-day-a217cfb70f3"
authors: ["Ittipatjitrada (@IttipatJitrada)"]
bugs: ["Open redirect"]
publication_date: "2022-07-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2484
scraped_via: "browseros"
---

# How I found Open redirect on Bug crowd public program in 2 day

How I found Open redirect on Bug crowd public program in 2 day
Ittipatjitrada
Follow
2 min read
·
Jul 6, 2022

122

3

Tools :
- Burp suite
- Burp JS Link Finder

Explain :

Get Ittipatjitrada’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First of all, I chose to make this program because it has a new update so I want to do it. On that first day, I didn’t find anything like many programs I’ve done.
Then on the second day I started to think about where to go next. I remember at first I chose to look for the endpoint a bit more but in the end I couldn’t find anything. I remember I had a burp JS Link finder extension.
After searching for a while I found an endpoint similar to that main endpoint is /n/ endpoint and primary endpoint is /s/.

Then I go into the endpoint. Then I found that it was an old web page.
The first thing I thought I would do was go through some old scripts that the dev might have forgotten to remove.
And then I found out that there is a script that can cause an open redirect vulnerability.

Press enter or click to view image in full size

After that I managed to copy endpoint found, use it and change the value to evil.com

Press enter or click to view image in full size
