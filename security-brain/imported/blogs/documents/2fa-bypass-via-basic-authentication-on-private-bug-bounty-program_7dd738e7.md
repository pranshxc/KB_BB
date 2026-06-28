---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-14_2fa-bypass-via-basic-authentication-on-private-bug-bounty-program.md
original_filename: 2022-06-14_2fa-bypass-via-basic-authentication-on-private-bug-bounty-program.md
title: 2FA Bypass via Basic Authentication on private bug bounty program
category: documents
detected_topics:
- mfa
- command-injection
- api-security
tags:
- imported
- documents
- mfa
- command-injection
- api-security
language: en
raw_sha256: 7dd738e75b94c04b60b3b07f2ac6b1f37075bd7c76487564c55209ea3f62b7ba
text_sha256: 3b984d892787a3a66659f978d81f5e6fb1d57407b45fa5048eb1f46a0331fee9
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# 2FA Bypass via Basic Authentication on private bug bounty program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-14_2fa-bypass-via-basic-authentication-on-private-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `7dd738e75b94c04b60b3b07f2ac6b1f37075bd7c76487564c55209ea3f62b7ba`
- Text SHA256: `3b984d892787a3a66659f978d81f5e6fb1d57407b45fa5048eb1f46a0331fee9`


## Content

---
title: "2FA Bypass via Basic Authentication on private bug bounty program"
url: "https://medium.com/@sharp488/2fa-bypass-via-basic-authentication-on-private-bug-bounty-program-93bb457cd065"
authors: ["Sharat Kaikolamthuruthil (@sharp488)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2022-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2553
scraped_via: "browseros"
---

# 2FA Bypass via Basic Authentication on private bug bounty program

2FA Bypass via Basic Authentication on private bug bounty program
Sharat Kaikolamthuruthil
Follow
2 min read
·
Jun 14, 2022

160

2

2FA bypass via basic authentication

Hello Friends,

Get Sharat Kaikolamthuruthil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is yet another 2FA bypass that I discovered in a private bug bounty program. So I had found a couple of bugs including a 2FA bypass in this application & was hunting for mores bugs.

While trying to append different extensions such as .html, .aspx, .js, ,php etc to an already existing page I suddenly triggered a Basic Authentication pop up.
So if the program has a URL say “example.com/edit”, I simply changed it to “example.com/edit.aspx” and a Basic Authentication popped up which was otherwise hidden in the application.
Press enter or click to view image in full size
Basic Authentication
The first thought that came to my mind was to try out the user credentials to check if it is being accepted.
As soon as I entered the credentials, the account logged in successfully and I was able to bypass the 2FA enabled in the account which was kinda surprising.
This application did not have any API keys so it was pretty obvious that we could only try valid login credentials.
I immediately reported this and it was triaged as High severity bug.

Hope you guys enjoyed it, have a good day. 😃

Disclaimer: For educational purpose only please do not try for illegal activities.
