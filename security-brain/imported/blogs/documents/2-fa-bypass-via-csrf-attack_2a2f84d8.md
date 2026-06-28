---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-23_2-fa-bypass-via-csrf-attack.md
original_filename: 2019-12-23_2-fa-bypass-via-csrf-attack.md
title: 2 FA Bypass via CSRF Attack
category: documents
detected_topics:
- mfa
- oauth
- command-injection
- password-reset
- otp
- rate-limit
tags:
- imported
- documents
- mfa
- oauth
- command-injection
- password-reset
- otp
- rate-limit
language: en
raw_sha256: 2a2f84d8ecc06238c9b9be8b014c84e4ca056779deafe5e785f922ad82f47ac0
text_sha256: f3d60fcb58bca939d18d0acd0b5285ad75cad2d461d902e65cb0ef6d6ed7cb0a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# 2 FA Bypass via CSRF Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-23_2-fa-bypass-via-csrf-attack.md
- Source Type: markdown
- Detected Topics: mfa, oauth, command-injection, password-reset, otp, rate-limit
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2a2f84d8ecc06238c9b9be8b014c84e4ca056779deafe5e785f922ad82f47ac0`
- Text SHA256: `f3d60fcb58bca939d18d0acd0b5285ad75cad2d461d902e65cb0ef6d6ed7cb0a`


## Content

---
title: "2 FA Bypass via CSRF Attack"
url: "https://medium.com/@vbharad/2-fa-bypass-via-csrf-attack-8f2f6a6e3871"
authors: ["Vishal Bharad"]
programs: ["Mail.ru"]
bugs: ["2FA / MFA bypass", "CSRF"]
publication_date: "2019-12-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4874
scraped_via: "browseros"
---

# 2 FA Bypass via CSRF Attack

Member-only story

2 FA Bypass via CSRF Attack
Vishal Bharad
Follow
2 min read
·
Dec 23, 2019

271

Introduction :

Hello Guys Again, I am Vishal Bharad, I’m here again to share about my findings on How I Bypass 2 Factor Authentication via CSRF (Cross Site Request Forgery).

About the Vulnerability :

You all know about the 2FA Bypass Vulnerability. There are some Techniques.

Bypassing 2fa using conventional session management
Bypassing 2fa Via OAuth mechanism
Bypassing 2fa via brute force
Bypassing 2fa using race conditions (RARE)
Bypassing 2fa using modifies response
Bypassing 2fa using Activation link
Bypassing 2fa in password reset page

But here I am able to disable the 2FA via Client side attack which is CSRF.

For Discovering the bug I have tried to Disable 2FA using CSRF file. But I have seen that there is token is generated in the CSRF poc. But when I tried this html file that token is never get expired. This token is used again and again to disable 2FA on another Account.

Note : Always try to Disable 2FA using CSRF Attack.

So the program is Mail.ru which is Available on Hackerone.
