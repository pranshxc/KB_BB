---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-11_how-i-was-able-to-generate-access-tokens-for-any-facebook-user.md
original_filename: 2018-12-11_how-i-was-able-to-generate-access-tokens-for-any-facebook-user.md
title: How I was able to generate Access Tokens for any Facebook user.
category: documents
detected_topics:
- idor
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- idor
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: a0c0536cea45568ef84e0119f80e18dbabc32d23844c75574aa8f342075b7f4c
text_sha256: 7d03f442346f1f8199b8620c8f2169a1b9b862cf639e7bdcde1d56ff39f65e9e
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to generate Access Tokens for any Facebook user.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-11_how-i-was-able-to-generate-access-tokens-for-any-facebook-user.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `a0c0536cea45568ef84e0119f80e18dbabc32d23844c75574aa8f342075b7f4c`
- Text SHA256: `7d03f442346f1f8199b8620c8f2169a1b9b862cf639e7bdcde1d56ff39f65e9e`


## Content

---
title: "How I was able to generate Access Tokens for any Facebook user."
url: "https://medium.com/bugbountywriteup/how-i-was-able-to-generate-access-tokens-for-any-facebook-user-6b84392d0342"
authors: ["Youssef Sammouda (@samm0uda)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR", "Information disclosure"]
publication_date: "2018-12-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5535
scraped_via: "browseros"
---

# How I was able to generate Access Tokens for any Facebook user.

How I was able to generate Access Tokens for any Facebook user.
Samm0uda
Follow
2 min read
·
Dec 11, 2018

223

1

This bug could allowed a malicious user to generate access tokens for any Facebook user.
I found this bug by mistake when I was testing some Facebook endpoints used in the Rights Manger dashboard which is a dashboard targeting videos’ publishers and editors.

Get Samm0uda’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The vulnerable endpoint returns a page access_token when making a POST request to it along with the parameter page_id.
The issue here is that the endpoint doesn’t check if the provided value for the page_id is actually an id of a “page” and not another object like “user”. This allowed me to make the request and change the page_id value to any Facebook user id and as a response to this request I get the access token of that user.

Press enter or click to view image in full size

Impact
Due to the state of the Access Token (The scopes of the generated access_token are for pages and not users), I wasn’t able to read and modify some data about the user (like see messages) and I wasn’t able to full takeover the account. Nevertheless, I was able to read all private information like emails , credit cards, phones number , managed pages and their access_tokens , managed business/ad-accounts and private posts,photos and videos ….

Fix
The Facebook security team fixed this issue by modifying their APIs to refuse those kind of tokens which are generated this way (user object instead of a page). Also after almost six months, they made a second fix by modifying this endpoint and some others to not generate these types of tokens in the first place by checking if the id provided doesn’t match a user object.

Feb 3, 2018 — Report Sent
Feb 6, 2018 — Further investigation by Facebook
Feb 6, 2018 – Clarification requested by Facebook
Feb 6, 2018 — Clarification sent
Feb 8, 2018 — Fixed by Facebook
Feb 23, 2018 — Bounty Awarded by Facebook
