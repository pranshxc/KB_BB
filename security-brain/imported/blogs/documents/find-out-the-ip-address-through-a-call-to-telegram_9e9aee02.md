---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-28_find-out-the-ip-address-through-a-call-to-telegram.md
original_filename: 2023-05-28_find-out-the-ip-address-through-a-call-to-telegram.md
title: Find out the IP address through a call to Telegram…
category: documents
detected_topics:
- command-injection
- information-disclosure
- supply-chain
tags:
- imported
- documents
- command-injection
- information-disclosure
- supply-chain
language: en
raw_sha256: 9e9aee022c5941cea6041bfbd27ca92be0989471e969f66ada4d973a7a0b6d4e
text_sha256: ed7c8e032f17d2ed320f1a6b689822f37709295100c2e92031c48c01b3bae2b5
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Find out the IP address through a call to Telegram…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-28_find-out-the-ip-address-through-a-call-to-telegram.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `9e9aee022c5941cea6041bfbd27ca92be0989471e969f66ada4d973a7a0b6d4e`
- Text SHA256: `ed7c8e032f17d2ed320f1a6b689822f37709295100c2e92031c48c01b3bae2b5`


## Content

---
title: "Find out the IP address through a call to Telegram…"
url: "https://medium.com/@ibederov_en/find-out-the-ip-address-through-a-call-to-telegram-a899441b1bac"
authors: ["Igor S. Bederov"]
programs: ["Telegram"]
bugs: ["Privacy issue", "Information disclosure"]
publication_date: "2023-05-28"
added_date: "2023-05-29"
source: "pentester.land/writeups.json"
original_index: 1111
scraped_via: "browseros"
---

# Find out the IP address through a call to Telegram…

1

·

Top highlight

Find out the IP address through a call to Telegram…
Igor S. Bederov
Follow
2 min read
·
May 28, 2023

187

6

1️⃣ Download Wireshark (https://www.wireshark.org/download.html), open it and be sure to specify the protocol we need in the filter — STUN.
2️⃣ Click on the “magnifying glass” (find a package) and see how we will have a new line with parameters and a search line. There we select the string option.
3️⃣ In the line we write XDR-MAPPED-ADDRESS.
4️⃣ Turn on Wireshark and call via Telegram. As soon as the user answers the call, we will immediately begin to display data and among them will be the IP address of the user who was called.
5️⃣ To understand what kind of IP we need, click already in the configured search engine Find, look in the line XDR-MAPPED-ADDRESS and what comes after it is the IP we need.

I also suggest taking a closer look at Telegram get remote IP: https://github.com/n0a/telegram-get-remote-ip

Get Igor S. Bederov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

😉👍 And subscribe to https://t.me/irozysk

… join my Medium Blog https://medium.com/@ibederov_en or Telegram https://t.me/ibederov_en!
