---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-05_make-featured-product-in-any-video.md
original_filename: 2020-07-05_make-featured-product-in-any-video.md
title: Make Featured Product in any video
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
raw_sha256: c92edf6900444b52d22d5584c311b42c34e2f73693a79aca445a5fa14af2375d
text_sha256: 36c0b3a75cd547a6d5261e4cf527880bc11a5c8e1c243493c0d260ef5d072e36
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Make Featured Product in any video

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-05_make-featured-product-in-any-video.md
- Source Type: markdown
- Detected Topics: idor, command-injection, graphql
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `c92edf6900444b52d22d5584c311b42c34e2f73693a79aca445a5fa14af2375d`
- Text SHA256: `36c0b3a75cd547a6d5261e4cf527880bc11a5c8e1c243493c0d260ef5d072e36`


## Content

---
title: "Make Featured Product in any video"
url: "https://medium.com/@yaala/make-featured-product-in-any-video-ec2bd4816ae4"
authors: ["abdellah yaala (@yaalaab)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2020-07-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4433
scraped_via: "browseros"
---

# Make Featured Product in any video

abdellah yaala
Follow
1 min read
·
Jul 5, 2020

13

Make Featured Product in any video

Description/Impact

Victim have upload video or live video that have lot of visitors , an attacker can tags his product as Featured Product in the video.

Impact

=====

Make Featured Product in any video on Facebook

Repro Steps

===

Get abdellah yaala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

-Users: userA admin or editor on pageA

userA create shop section and product P_id

video_B : video not owned by userA (any video on Facebook)

POST /api/graphql/ HTTP/1.1

Host: www.facebook.com

doc_id=2781671041948682&variables={“input”:{“client_mutation_id”:”1",”actor_id”:”actor_id”,”video_id”:”[video_B_id]”,”product_item_id”:”[P_id]”}}

product P_id tagged on the vicitm video and attacker can get more visitor on his products , product can’t be removed , the only solution is delete video

Press enter or click to view image in full size

Thanks

https://twitter.com/yaalaab
