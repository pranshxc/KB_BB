---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-14_false2true-match-and-replace-bug-hunting-a-cautionary-tale.md
original_filename: 2020-08-14_false2true-match-and-replace-bug-hunting-a-cautionary-tale.md
title: False2True, Match and Replace bug hunting — A cautionary tale
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 19a6d0c8222cd39b5ff2e8e493c6f870e05ff652207fcf21ae5b3ceaecb0779a
text_sha256: 1c8b0001df4494844610b9d915caee86c823d077904f1f54038c68edc9c46f44
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# False2True, Match and Replace bug hunting — A cautionary tale

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-14_false2true-match-and-replace-bug-hunting-a-cautionary-tale.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `19a6d0c8222cd39b5ff2e8e493c6f870e05ff652207fcf21ae5b3ceaecb0779a`
- Text SHA256: `1c8b0001df4494844610b9d915caee86c823d077904f1f54038c68edc9c46f44`


## Content

---
title: "False2True, Match and Replace bug hunting — A cautionary tale"
url: "https://medium.com/bugbountywriteup/false2true-match-and-replace-bug-hunting-a-cautionary-tale-fbe7020f02ad"
authors: ["Vuk Ivanovic"]
bugs: ["Privilege escalation"]
publication_date: "2020-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4325
scraped_via: "browseros"
---

# False2True, Match and Replace bug hunting — A cautionary tale

Member-only story

False2True, Match and Replace bug hunting — A cautionary tale
Vuk Ivanovic
Follow
4 min read
·
Aug 14, 2020

56

Press enter or click to view image in full size

False positives are a bane of… well, everything. Scientists have to deal with it, and so do pentesters and bug bounty hunters. The difference is that as a bug bounty hunter if something is false positive and you’ve spent hours on it, you just got burned. You’ve earned some experience, though. That has to count for something.

Either way, if you are really serious about bug hunting, or hacking in general, you have to be up-to-date with new attacks, new tricks, and tips, etc. But, because these attacks are new to you, it means you may not be aware of the potential pitfalls within those attacks.

False2True:

This one was quite a revelation when I first heard about it. Here’s the link that got me started down that path.

The basic idea is to keep an eye for the Response bit of requests (I had more luck with responses to POST requests rather than GET) and note places where it shows “isAdmin”:false, “staff”:false, “userLevel”:basic, etc. You get the idea. Experiment, basically.

The attack is to use Match & Replace in burp (you don’t need the pro version either) and to add the rule like this:
