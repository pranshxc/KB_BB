---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-13_how-i-was-able-to-find-a-logical-bug-on-instagram_2.md
original_filename: 2019-12-13_how-i-was-able-to-find-a-logical-bug-on-instagram_2.md
title: How I was able to find a logical bug on Instagram?
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
- api-security
- supply-chain
language: en
raw_sha256: 2589761389d02ba31edbff75d32866df9a98899a57e02dd97fae4d190943fb29
text_sha256: fd52fdbce1f106f4d89b14b24ebd145054e0aaf4806f23d303eabf7038a5de1a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to find a logical bug on Instagram?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-13_how-i-was-able-to-find-a-logical-bug-on-instagram_2.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2589761389d02ba31edbff75d32866df9a98899a57e02dd97fae4d190943fb29`
- Text SHA256: `fd52fdbce1f106f4d89b14b24ebd145054e0aaf4806f23d303eabf7038a5de1a`


## Content

---
title: "How I was able to find a logical bug on Instagram?"
url: "https://medium.com/nassec-cybersecurity-writeups/this-is-how-i-got-xxxx-from-facebook-for-instagram-bug-aaff50342246"
authors: ["Jabir Khan (@Jabirkhan0x0)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2019-12-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4890
scraped_via: "browseros"
---

# How I was able to find a logical bug on Instagram?

How I was able to find a logical bug on Instagram?
jabir khan
Follow
2 min read
·
Dec 13, 2019

294

2

This article is based on a logical bug find that I was able to discover while surfing Instagram. Not only it earned me Hall of Fame on Facebook, but it also gave me a different thinking perspective while doing bug bounty.

I don’t use Instagram much, but, one fine evening I thought of checking my Instagram account on my laptop. I decided to change the password as I hadn’t used Instagram for a long time. I went to settings and changed my password.

Press enter or click to view image in full size

After I changed the password, I decided to test functionalities on the Settings tab to see if I will be to find a loophole or a bug. My eyes caught an option named “Authorized App.” I understood by its name that it should be listing the third-party app to which I may have given permission to access data. I clicked that option and there I found two tabs; Active and Expired. After I clicked the Active Tab I saw “TikTok” as an active authorized app.

Get jabir khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The moment I saw TikTok as an authorized app, it surprised me because I had never created a TikTok account or integrated it on Instagram. Without a second thought, I tried to remove TikTok from the list. Surprisingly it gave an error message at the bottom left corner that displayed “there was a problem revoking access.”

Press enter or click to view image in full size

I recognized that it was a logical bug and quickly reported it to Facebook for a fix. Facebook’s triage team acknowledged the issue and awarded me with bounty. In this way, a simple logical bug on Instagram earned me a bounty and Hall of Fame.

P.S — I would like to thank Mr. Ajay Gautam, Head of Security at Nassec, for helping me report the issue to Facebook.

Author — Jabir is an independent security researcher and a bug bounty hunter. As a security researcher, he has been inducted in Hall of Fame of Facebook. You can follow him on twitter @jabirkhan0x0.

Editor’s Note — We will be publishing write-ups related to cybersecurity every week. We are looking to grow our community. If you are interested in writing about cybersecurity, please email us at blog@nassec.io.
