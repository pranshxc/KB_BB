---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-19_bug-bounty-600-info-disclosure-obtain-any-users-backup-data.md
original_filename: 2021-01-19_bug-bounty-600-info-disclosure-obtain-any-users-backup-data.md
title: '[Bug Bounty] 600$ Info Disclosure: obtain any user’s backup data'
category: documents
detected_topics:
- idor
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: 0c86a5820186eb5b815b217254bf3dd5f5761b2f194ae9c06847e32ff7e3990e
text_sha256: 554a682f87346d594eb999a03504db6a21c9453b1b82816bfb004cc81fd01ec4
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: true
---

# [Bug Bounty] 600$ Info Disclosure: obtain any user’s backup data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-19_bug-bounty-600-info-disclosure-obtain-any-users-backup-data.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: True
- Raw SHA256: `0c86a5820186eb5b815b217254bf3dd5f5761b2f194ae9c06847e32ff7e3990e`
- Text SHA256: `554a682f87346d594eb999a03504db6a21c9453b1b82816bfb004cc81fd01ec4`


## Content

---
title: "[Bug Bounty] 600$ Info Disclosure: obtain any user’s backup data"
url: "https://medium.com/bugbountywriteup/bug-bounty-600-info-disclosure-a-token-is-not-the-same-on-all-endpoints-febf5b7ea745"
authors: ["Tommaso De Ponti"]
bugs: ["Information disclosure", "IDOR"]
publication_date: "2021-01-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3981
scraped_via: "browseros"
---

# [Bug Bounty] 600$ Info Disclosure: obtain any user’s backup data

Member-only story

[Bug Bounty] 600$ Info Disclosure: obtain any user’s backup data
[Friend Link] Obtaining any user’s Backup data via Mishandled token in Backup endpoint
Tommaso De Ponti
Follow
3 min read
·
Jan 19, 2021

231

Press enter or click to view image in full size
Photo by Daan Mooij on Unsplash

Friend Link for those without a Medium Paid subscription: https://medium.com/@tdpdev/febf5b7ea745?source=friends_link&sk=***REDACTED-SUSPECT-TOKEN***Hi y'all guys, I haven’t been writing for a long time as I focused more on bounties. Wanted to share with you one of the many bugs I found on one public program in H1. However, they don’t have public disclosure so I’ll redact the target.

Also, this gives an important takeaway, which we’ll see later.

So, approaching the target. Every time I logged in to the app, a call was made to a backup endpoint. Returning a user’s backup data. No cookies were used, only a token in the POST data. It looked like this: 1234-randomletters.

Didn’t come to my mind any interesting attack surface here, I tried with another token, same length, etc. And skipped the endpoint and jumped right in using the app. It’s important to note that I had just decided to start hunting on that program, and in my process, I don’t go directly into exploitation, so I didn’t spend time trying to hijack the token, or using any other technique to bypass it.
