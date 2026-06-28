---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-12_cache-poisoning-of-wget.md
original_filename: 2020-08-12_cache-poisoning-of-wget.md
title: Cache poisoning of wget
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
raw_sha256: 719103bee11cb1b3178eef1257432eb87167f3d728fce482562cd3d9db3172e4
text_sha256: e7530bfb693552257c74f10d94931d5ac1ee05a27949be719de789118dfc3e8d
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Cache poisoning of wget

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-12_cache-poisoning-of-wget.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `719103bee11cb1b3178eef1257432eb87167f3d728fce482562cd3d9db3172e4`
- Text SHA256: `e7530bfb693552257c74f10d94931d5ac1ee05a27949be719de789118dfc3e8d`


## Content

---
title: "Cache poisoning of wget"
url: "https://medium.com/bugbountywriteup/cache-poisoning-of-wget-94a4d70104b1"
authors: ["Vuk Ivanovic"]
bugs: ["Web cache poisoning"]
publication_date: "2020-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4329
scraped_via: "browseros"
---

# Cache poisoning of wget

Member-only story

Cache poisoning of wget
Vuk Ivanovic
Follow
4 min read
·
Aug 12, 2020

24

Press enter or click to view image in full size
(edited to hide the affected company) a real world example of the cache poison detection

Another interesting case of cache poisoning (you can read about the first one here). This one, however, isn’t as “sexy” as the previous one. You have been warned.

There are times when burp and web browser (be it firefox or chrome) don’t quite agree on how to present the response to the issued request (especially if the request has xss payload). This is one of those stories.

My default approach to bug hunting is to browse the target website with burp as a proxy. And, if the waf is so kind I can have Param Miner enabled without getting blocked, and with the box attempt cache poison checked.

Press enter or click to view image in full size

And, if the web server is not configured correctly, or to be honest, if the stars are aligned, the result is a useful cache poison, as the link from earlier. But, this is not that story. Not to say that the case in this story is not useful, it’s just harder to sell it.

Enough chit-chat/exposition, let’s dig into it:

After browsing the target website and doing all sorts of tests, getting nothing, I figured time to review. I checked the burp pro dashboard, and as a nice boost I noticed that Param Miner had found something. But, from past experiences, I…
