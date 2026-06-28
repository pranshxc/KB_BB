---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-18_from-google-dorking-to-information-disclosure.md
original_filename: 2021-09-18_from-google-dorking-to-information-disclosure.md
title: From Google Dorking to Information Disclosure
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: f05a7292aeced394caa1330b7aeed6b79facab5c91260222c5e9d3f0ddf07e09
text_sha256: 27ead76b40cddfd3cba6004288d372ce2031dabe0640a6b2f844964cbbb77c2a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# From Google Dorking to Information Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-18_from-google-dorking-to-information-disclosure.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `f05a7292aeced394caa1330b7aeed6b79facab5c91260222c5e9d3f0ddf07e09`
- Text SHA256: `27ead76b40cddfd3cba6004288d372ce2031dabe0640a6b2f844964cbbb77c2a`


## Content

---
title: "From Google Dorking to Information Disclosure"
url: "https://mikekitckchan.medium.com/from-google-dorking-to-information-disclosure-5da4f1d771e5"
authors: ["MikeChan"]
bugs: ["Information disclosure", "Missing authentication"]
publication_date: "2021-09-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3306
scraped_via: "browseros"
---

# From Google Dorking to Information Disclosure

Top highlight

Member-only story

From Google Dorking to Information Disclosure
MikeChan
Follow
2 min read
·
Sep 18, 2021

114

Press enter or click to view image in full size
Photo by Christian Wiediger on Unsplash

This is a story about how I used google dorking to find sensitive information exposed in a private VDP program. This is a rather short story but I think it is quite interesting. So, I was like why not sharing it?

So, it was just another day of hunting. I was hunting on a private VDP program. Let’s call it redacted.com. I just started hunting on it. So, I was like why not try to find something juicy from google? So, I just put in some random google dorking in its search box and nothing seems interesting to me until the one below:

site:redacted.com inurl:admin "@gmail.com"

I found a page where exposed all user’s email addresses of my target. Then, I found an edit button next to each address. So, I just click on it. And the below screen popped:

Press enter or click to view image in full size

And Boom! It disclosed all information including password of the users which stored in PLAIN TEXT!! Also, I can even edit or delete these records. This endpoint exposed over 38k user’s record.

So, I quickly reported this issue to the program. The issue was latter fixed but as this is a VDP program, bounty for this bug was zero. Nevertheless, I earned 100% appreciation from the company.

Hope you enjoy this writeup and see you next time.
