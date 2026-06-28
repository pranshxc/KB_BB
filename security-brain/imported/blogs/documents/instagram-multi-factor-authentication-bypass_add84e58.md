---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-27_instagram-multi-factor-authentication-bypass.md
original_filename: 2018-11-27_instagram-multi-factor-authentication-bypass.md
title: Instagram Multi-factor authentication Bypass
category: documents
detected_topics:
- mfa
- access-control
- command-injection
tags:
- imported
- documents
- mfa
- access-control
- command-injection
language: en
raw_sha256: add84e58d8b80921479f05e356a5537f03c890793a074b101b597adce9564d5a
text_sha256: 24d77e43525263859d7da089199df0ee3d9c4bbc626cb0ac27cc9584f8772472
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Instagram Multi-factor authentication Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-27_instagram-multi-factor-authentication-bypass.md
- Source Type: markdown
- Detected Topics: mfa, access-control, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `add84e58d8b80921479f05e356a5537f03c890793a074b101b597adce9564d5a`
- Text SHA256: `24d77e43525263859d7da089199df0ee3d9c4bbc626cb0ac27cc9584f8772472`


## Content

---
title: "Instagram Multi-factor authentication Bypass"
url: "https://medium.com/@vishnu0002/instagram-multi-factor-authentication-bypass-924d963325a1"
authors: ["Vishnuraj"]
programs: ["Meta / Facebook"]
bugs: ["2FA / MFA bypass"]
publication_date: "2018-11-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5560
scraped_via: "browseros"
---

# Instagram Multi-factor authentication Bypass

Top highlight

Instagram Multi-factor authentication Bypass
vishnuraj
Follow
2 min read
·
Nov 27, 2018

304

5

Hi ,

This post is regarding one of my findings in Facebook, which could have allowed anyone to bypass Multi-factor authentication.

Vulnerability Type :

Privilege Escalation/bypass authorization

Product Area:

Instagram

Description

Two-factor authentication is a security mechanism that requires two types of credentials for authentication and is designed to provide an additional layer of validation, minimizing security breaches.

Impact

Two-factor authentication can be bypassed using the add instagram account feature in facebook business . While merging the victim account with the attacker facebook account, 2FA of victim account gets automatically bypassed which an attacker use 2fa enabled victim account without entering 2FA process.

Get vishnuraj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Proof of Concept

1) User “A” creates a business account and Adds victim Two-factor authentication enabled account.

Press enter or click to view image in full size

2) add victim username and password (2FA enabled account)

Press enter or click to view image in full size

3) here you can see 2FA check skipped when a Business Manager tries to link an Instagram Account

I would like to thanks Facebook Security Team for this awesome Response .

Press enter or click to view image in full size

Thanks again!

Have a great day ahead ☺
