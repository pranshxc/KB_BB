---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-23_bug-bounty-101-always-check-the-source-code.md
original_filename: 2019-02-23_bug-bounty-101-always-check-the-source-code.md
title: Bug Bounty 101 — Always Check The Source Code
category: documents
detected_topics:
- rate-limit
- command-injection
- information-disclosure
tags:
- imported
- documents
- rate-limit
- command-injection
- information-disclosure
language: en
raw_sha256: 2c57fc283ae05df5f9a05cddebad4c5065ba218717e8d88be57f37110db17c47
text_sha256: 659d046e580b0cf3dc7cdd3e20c6868a6d1cda2dede94f71034154b4d3e35b7f
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty 101 — Always Check The Source Code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-23_bug-bounty-101-always-check-the-source-code.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `2c57fc283ae05df5f9a05cddebad4c5065ba218717e8d88be57f37110db17c47`
- Text SHA256: `659d046e580b0cf3dc7cdd3e20c6868a6d1cda2dede94f71034154b4d3e35b7f`


## Content

---
title: "Bug Bounty 101 — Always Check The Source Code"
page_title: "Bug Bounty 101 — Always Check The Source Code | by Spazzy | Medium"
url: "https://medium.com/@spazzyy/bug-bounty-101-always-check-the-source-code-1adaf3f59567"
authors: ["Spazzy"]
bugs: ["Lack of rate limiting", "Information disclosure"]
publication_date: "2019-02-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5391
scraped_via: "browseros"
---

# Bug Bounty 101 — Always Check The Source Code

Bug Bounty 101 — Always Check The Source Code
Spazzy
Follow
1 min read
·
Feb 23, 2019

29

Never miss out on checking out the source code! In a recent bounty program for a company I can’t disclose, I found a hilarious information disclosure that is a great example of why you should always check out the source code.

This vulnerability sat inside a enrollment portal that was meant for people to redeem discounts that worked for affiliated companies. It required you to enter any email, and the account phone number. In the next step, it required some extra steps of verification. One being, the last 4 of the SSN which turned out not to have a request limit….oops? LOL

Get Spazzy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This vulnerability started out being no request limit turning into an information disclosure, as I reported this to the company soon after checking to see if they fixed it I happened to check out the source code on the next step. That’s when I found more that adds to the information disclosure! It included a HTML comment that I originally believed to only contain filler info…but no it actually was information of the account. It contained the account number and the answer to one of the extra verification steps! Crazy right? I couldn’t believe a company this large, to have something so simple.

With this someone with malicious intent would be able to complete the verification, know the customers last 4 of the ssn, and the extra verification info that included the answer in the source code.

Simple but toxic, proves never miss out looking at changes in the source code!
