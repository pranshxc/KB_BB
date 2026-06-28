---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-21_how-i-found-my-first-bug-stored-xss-and-earned-my-first-bounty-1000.md
original_filename: 2020-08-21_how-i-found-my-first-bug-stored-xss-and-earned-my-first-bounty-1000.md
title: How I Found My First Bug Stored Xss and Earned My First Bounty 1000$
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
raw_sha256: f45a24abbdf4025d19a5a594ed8436ead11a1daf57be7f4bf3128e1b9857841b
text_sha256: 02b7bfef1305831944bcbe2d9d00b9ffa5ac0f041b6c1a97bfaa57f8e88d93c5
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found My First Bug Stored Xss and Earned My First Bounty 1000$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-21_how-i-found-my-first-bug-stored-xss-and-earned-my-first-bounty-1000.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `f45a24abbdf4025d19a5a594ed8436ead11a1daf57be7f4bf3128e1b9857841b`
- Text SHA256: `02b7bfef1305831944bcbe2d9d00b9ffa5ac0f041b6c1a97bfaa57f8e88d93c5`


## Content

---
title: "How I Found My First Bug Stored Xss and Earned My First Bounty 1000$"
url: "https://medium.com/@0xnazmul/how-i-found-my-first-bug-stored-xss-and-earned-my-first-bounty-1000-33556678d1ed"
authors: ["Nazmul Haque (@0xnazmul)"]
programs: ["Badoo"]
bugs: ["Stored XSS"]
bounty: "1,000"
publication_date: "2020-08-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4301
scraped_via: "browseros"
---

# How I Found My First Bug Stored Xss and Earned My First Bounty 1000$

How I Found My First Bug Stored Xss and Earned My First Bounty 1000$
Nazmul Haque
Follow
2 min read
·
Aug 22, 2020

230

2

Hi guys ,

This is Nazmul Haque a Newbie security researcher from Bangladesh.This is my 1st write-up and also I am not good at XSS so forgive all mistakes.

It was 11/18/2019 and my 1st day of bug hunting.I’m still newbie!

Today I am gonna to Share a Stored Xss vulnerability what was reported by me to Badoo Security team in their Bug Bounty Program in Hackerone.

Get Nazmul Haque’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So as usual i was created an account in Badoo and Visit a user profile and send message with xss payload.

Press enter or click to view image in full size

So I input a Normal payload :-

“><img src=x onerror=prompt(document.cookie)>

After message sent successfully i clicked on chat now option and i got this Response.

Press enter or click to view image in full size

I reported this issue in NOV 18th. Report Triaged within 2 Hour and they paid me 1000$ for reporting this within 6 hour.

Press enter or click to view image in full size

Video POC: https://www.youtube.com/watch?v=RgGz2z5bFBk

Thanks for reading . Happy Hunting .

Contact me:

Twitter: Nazmul Haque

Facebook: Nazmul Haque

LinkedIn: Nazmul Haque
