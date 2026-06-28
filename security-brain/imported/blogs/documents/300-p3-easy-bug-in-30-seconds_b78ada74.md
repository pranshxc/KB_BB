---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-22_300-p3-easy-bug-in-30-seconds.md
original_filename: 2020-10-22_300-p3-easy-bug-in-30-seconds.md
title: 300$ P3 Easy Bug in 30 Seconds
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
raw_sha256: b78ada74d96795ef8e8a4a5bb80cecccd5e515762f7aabdc1760eb81909093e5
text_sha256: c384c7e31fa61e5fd123c69cb2293941c70dab4d18cca7aeb1dd70b4c0ed9c8f
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# 300$ P3 Easy Bug in 30 Seconds

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-22_300-p3-easy-bug-in-30-seconds.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `b78ada74d96795ef8e8a4a5bb80cecccd5e515762f7aabdc1760eb81909093e5`
- Text SHA256: `c384c7e31fa61e5fd123c69cb2293941c70dab4d18cca7aeb1dd70b4c0ed9c8f`


## Content

---
title: "300$ P3 Easy Bug in 30 Seconds"
url: "https://medium.com/@seaman00o/300-p3-easy-bug-in-30-seconds-de65ea3d8f50"
authors: ["Omar Hamdy (@seaman00o)"]
bugs: ["Missing authentication", "Broken Access Control"]
bounty: "300"
publication_date: "2020-10-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4185
scraped_via: "browseros"
---

# 300$ P3 Easy Bug in 30 Seconds

Top highlight

Member-only story

300$ P3 Easy Bug in 30 Seconds
Omar Hamdy
Follow
Oct 21, 2020

536

Press enter or click to view image in full size

Hello Everyone,

I’m Omar Hamdy (Seaman), Today I am going to explain one of the coolest and easiest bugs which I found on Private Program in Bugcrowd.

let’s start,

I had a private program, let’s call it redacted.com

I started the Recon stage and extracted the Sub-domains

I Found a subdomain caught my attention :

admin.conversation.redacted.com

While accessing it I got a 403 error on that page. So I thought why not to give a shot to bypass that 403 error after that, I perform some techniques to bypass that 403 error.

Finally, I succeeded in Bypass it.

To bypass this, I Changed the protocol from http to https so that the link becomes like this:
https://admin.conversation.redacted.com

Steps to Reproduce :
Go to : admin.conversation.redacted.com, You will get 403 error on this page
Change the protocol from http to https so that the link becomes like this:
https://admin.conversation.redacted.com
You will access the Admin UI successfully

Thanks for reading ☺

Follow me on twitter @seaman00o
