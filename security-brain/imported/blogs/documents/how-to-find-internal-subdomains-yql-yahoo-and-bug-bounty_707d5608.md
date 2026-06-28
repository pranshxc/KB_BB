---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-16_how-to-find-internal-subdomains-yql-yahoo-and-bug-bounty.md
original_filename: 2017-07-16_how-to-find-internal-subdomains-yql-yahoo-and-bug-bounty.md
title: How to find internal subdomains? YQL, Yahoo! and bug bounty.
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: 707d5608514ded78739d066363708f868d2b59115278ceaa023aa08f9ca77498
text_sha256: 8d80f7423d3597df8ff72f058ec4b8aa3c90ed6c85920694687e1dbc633a2017
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How to find internal subdomains? YQL, Yahoo! and bug bounty.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-16_how-to-find-internal-subdomains-yql-yahoo-and-bug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `707d5608514ded78739d066363708f868d2b59115278ceaa023aa08f9ca77498`
- Text SHA256: `8d80f7423d3597df8ff72f058ec4b8aa3c90ed6c85920694687e1dbc633a2017`


## Content

---
title: "How to find internal subdomains? YQL, Yahoo! and bug bounty."
url: "https://hackernoon.com/how-to-find-internal-subdomains-yql-yahoo-and-bug-bounty-d7730b374d77"
final_url: "https://hackernoon.com/how-to-find-internal-subdomains-yql-yahoo-and-bug-bounty-d7730b374d77"
authors: ["Wojciech"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Information disclosure"]
publication_date: "2017-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6155
---

Discover Anything __

[![Hackernoon logo](https://hackernoon.imgix.net/hn-icon.png?auto=format%2Ccompress&w=128)Hackernoon](/)

Signup[Write](/new)

 ______

__ 6,233 reads

# How to find internal subdomains? YQL, Yahoo! and bug bounty.

by

[**Wojciech**](/u/woj_ciech)

[![Wojciech](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=96) byWojciech@woj_ciech](/u/woj_ciech)

Security researcher

Subscribe

[July 15th, 2017](/archives/2017/07/15)

![Read on Terminal Reader](https://hackernoon.imgix.net/computer.png?auto=format%2Ccompress&w=48)![Print this story](https://hackernoon.imgix.net/images/Print%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)![Read this story w/o Javascript](https://hackernoon.imgix.net/images/Lite%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)

TLDR __

![Read on Terminal Reader](https://hackernoon.imgix.net/computer.png?auto=format%2Ccompress&w=48)![Print this story](https://hackernoon.imgix.net/images/Print%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)![Read this story w/o Javascript](https://hackernoon.imgix.net/images/Lite%20Icon%20%4025px.png?auto=format%2Ccompress&w=48)

__![featured image - How to find internal subdomains? YQL, Yahoo! and bug bounty.](https://hackernoon.imgix.net/hn-images/1*B0NJFzcsb--rHszomqHxnA.png?auto=format%2Ccompress&w=3840)

![Wojciech](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=96)

by Wojciech@woj_ciech

[![Wojciech](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=96)byWojciech@woj_ciech](/u/woj_ciech)

Security researcher

Subscribe

 ____

__

________[__](mailto:?subject=I'd like to share a link with you &body=)

![Wojciech](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=3840)

[![Wojciech](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=96)by Wojciech@woj_ciech](/u/woj_ciech)

Security researcher

Subscribe

 ____

__

________[__](mailto:?subject=I'd like to share a link with you &body=)

[Up Next → OSINT investigation based on GAO report about firearm sales in Dark Web + Bitcoin tracking with…](/osint-investigation-based-on-gao-report-about-firearm-sales-in-dark-web-bitcoin-tracking-with-a0dcfa7d8daf)

### About Author

[![Wojciech HackerNoon profile picture](https://hackernoon.imgix.net/avatars/robot-b5.png?auto=format%2Ccompress&w=3840)](/u/woj_ciech)

[**Wojciech** | @woj_ciech](/u/woj_ciech)

Subscribe

Security researcher

[Read my stories](/u/woj_ciech)[About @woj_ciech](/about/woj_ciech)

#### Comments

![avatar](https://hackernoon.imgix.net/images/fallback-feat.png?auto=format%2Ccompress&w=3840)

#### TOPICS

[Software Engineering](/c/engineering)

[#hacking](/tagged/hacking)[#osint](/tagged/osint)[#bug-bounty](/tagged/bug-bounty)[#yahoo](/tagged/yahoo)[#security](/tagged/security)
