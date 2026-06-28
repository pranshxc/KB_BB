---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-18_for-the-first-bounty-it-takes-a-few-challenging-months-but-only-a-few-days-for-t.md
original_filename: 2022-03-18_for-the-first-bounty-it-takes-a-few-challenging-months-but-only-a-few-days-for-t.md
title: For the first Bounty, it takes a few challenging months, but only a few days
  for the second.
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
raw_sha256: 69b8cd4a4829c057991e652086569efffecae5595265fdff3beaf45ab877c5c7
text_sha256: a6b852d02c421f3a631f73789e321afbc368760e8ace9ce14741898a5cdca02b
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# For the first Bounty, it takes a few challenging months, but only a few days for the second.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-18_for-the-first-bounty-it-takes-a-few-challenging-months-but-only-a-few-days-for-t.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `69b8cd4a4829c057991e652086569efffecae5595265fdff3beaf45ab877c5c7`
- Text SHA256: `a6b852d02c421f3a631f73789e321afbc368760e8ace9ce14741898a5cdca02b`


## Content

---
title: "For the first Bounty, it takes a few challenging months, but only a few days for the second."
url: "https://medium.com/@interc3pt3r/for-the-first-bounty-it-takes-a-few-challenging-months-but-only-a-few-days-for-the-second-7b53259b0199"
authors: ["Aneesha D (@interc3pt3r)"]
bugs: ["Old components with known vulnerabilities"]
bounty: "250"
publication_date: "2022-03-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2804
scraped_via: "browseros"
---

# For the first Bounty, it takes a few challenging months, but only a few days for the second.

Member-only story

For the first Bounty, it takes a few challenging months, but only a few days for the second.
Aneesha D (ohzo)
Follow
2 min read
·
Mar 18, 2022

28

1

Good day, everyone! I spent nearly three hours looking for this bug, but it took me three months to uncover the bug that brought me my first bounty.

And this is the continuation of my article about “On the way to 2nd Bounty”, where I said about XSS and a vulnerable Apache server.

Press enter or click to view image in full size
Photo by Kasia Derenda on Unsplash

The target was “example.net” as I mentioned in my prior post. While signing up, I received the api subdomain “api.example.net” and the version was 2.4.29. The “api.example.net” page was simply an apache default page where I attempted to FUZZ for directories and files but was unsuccessful.

As I was using HTB, I suddenly thought of searching for vulnerabilities in that version and discovered that there are a few vulnerabilities in that version, such as HTTP request smuggling, possible buffer overflow with very large or unbounded LimitXMLRequestBody, and CVE-2017–15710.

Because there had been an article about these issues, I tried to do the tests described in those CVEs, and I…
