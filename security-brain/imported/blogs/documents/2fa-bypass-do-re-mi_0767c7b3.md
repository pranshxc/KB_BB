---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-16_2fa-bypass-do-re-mi.md
original_filename: 2022-08-16_2fa-bypass-do-re-mi.md
title: 2FA Bypass Do Re Mi
category: documents
detected_topics:
- mfa
- command-injection
- otp
tags:
- imported
- documents
- mfa
- command-injection
- otp
language: en
raw_sha256: 0767c7b3559756c12d1254cb61a914d0359c9e7bc4d7564a2134e8155499923f
text_sha256: c3e9cb280fb1906edaa3f1e186a4537e862edbbb6d9655b5cd76888e5fef7026
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# 2FA Bypass Do Re Mi

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-16_2fa-bypass-do-re-mi.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, otp
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `0767c7b3559756c12d1254cb61a914d0359c9e7bc4d7564a2134e8155499923f`
- Text SHA256: `c3e9cb280fb1906edaa3f1e186a4537e862edbbb6d9655b5cd76888e5fef7026`


## Content

---
title: "2FA Bypass Do Re Mi"
url: "https://medium.com/@ashlyn.lau_17206/2fa-bypass-do-re-mi-cfcfc3775d2e"
authors: ["Ashlyn Lau (@ashlyn_lau)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2022-08-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2300
scraped_via: "browseros"
---

# 2FA Bypass Do Re Mi

2FA Bypass Do Re Mi
Ashlyn L
Follow
2 min read
·
Aug 16, 2022

28

2

Not all 2FA bypass techniques are made equal, the most common scenario I came across are either one of the following:

Protected endpoint without 2FA check
2FA token disclosure in the server response

This is the new scenario encountered. After submitting the valid user id and password for authentication, the application will request for the second factor authentication as proof of identity for the “something only the user has” component.

Press enter or click to view image in full size

Enter any random M-token (eg 123456) value and select “login”. As expected, the 2FA login will be rejected due to M-token value entered yielded a different hash value in comparison to the M-token secret value.

Press enter or click to view image in full size
Server Response with Invalid M-Token

With the developer intuition, there are 3 parameter values that stood out and may potentially slip through the cracks. The 3 parameters to manipulate are:

Do: mtoken

Get Ashlyn L’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Re: mtoken_secret

Mi: mtoken_t

This is not a rocket science that we usually start with default empty or false values eg “” or 0; with anticipation that the program will skip the 2FA check if certain flag is false or value is null/empty, and then continue to modify the values to create another distinctive combination.

Press enter or click to view image in full size
Do Re Mi (attempt 1)

To cut the chase, the final combi below hit the jackpot! The server returned the authenticated session token (bypassing 2FA authentication).

Do: mtoken = 0

Re: mtoken_secret #The value return from the first login server response

Mi: mtoken_t = “”

Press enter or click to view image in full size

The end….:)
