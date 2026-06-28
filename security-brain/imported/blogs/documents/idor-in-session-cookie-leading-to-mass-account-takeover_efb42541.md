---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-29_idor-in-session-cookie-leading-to-mass-account-takeover.md
original_filename: 2020-05-29_idor-in-session-cookie-leading-to-mass-account-takeover.md
title: IDOR in session cookie leading to Mass Account Takeover
category: documents
detected_topics:
- idor
- command-injection
- otp
- csrf
tags:
- imported
- documents
- idor
- command-injection
- otp
- csrf
language: en
raw_sha256: efb425411057bd84996f547cde9a1eb8157f48232e89fa203255d1f072666229
text_sha256: a53c50b97d4ac5761e927a20a1568f8d92933f3b0baf922676455a8df647053a
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR in session cookie leading to Mass Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-29_idor-in-session-cookie-leading-to-mass-account-takeover.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `efb425411057bd84996f547cde9a1eb8157f48232e89fa203255d1f072666229`
- Text SHA256: `a53c50b97d4ac5761e927a20a1568f8d92933f3b0baf922676455a8df647053a`


## Content

---
title: "IDOR in session cookie leading to Mass Account Takeover"
url: "https://zonduu.medium.com/idor-in-session-cookie-leading-to-mass-account-takeover-d815ff3732d5"
authors: ["Zonduhackerone (@zonduu1)"]
bugs: ["IDOR", "Account takeover"]
bounty: "2,000"
publication_date: "2020-05-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4550
scraped_via: "browseros"
---

# IDOR in session cookie leading to Mass Account Takeover

IDOR in session cookie leading to Mass Account Takeover
Zonduhackerone
Follow
2 min read
·
May 30, 2020

890

2

If you are familiar with what IDOR is, you will know that it can be anywhere from url, request body, GET or POST requests and yes, in cookies too..

After spending quite a lot of time in a private program i was invited, i started to learn how everything works, and that usually means (not every time) that you are more likely to find more bugs, and that’s what happened to me… i ended up in top 1 in the leader-board next to a few well-known Hackers :)

Press enter or click to view image in full size

Ok back to the write-up.

When testing/analyzing the workflow of a web application i am usually looking for any type of token/ID that can be used to gain information or perform sensitive actions that can lead to IDOR.

Get Zonduhackerone’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In was trying to reproduce a CSRF issue when i noticed that in the cookies there was one called shoppingID that resulted to be the Session Cookie.

After taking a closer look at the cookie’s value i realized something that quickly got my attention:

shoppingID=88ea39539e74fa67c09a4fc0bc8ebe6d00978392PEr9ySESSIONID3552522PXGLkC;

Have you noticed? If not, please don’t continue and look at it again.

If you noticed it then congratulations, you might have a quick eye for possible IDORs.

MOVING THIS POST INTO MY SITE →

https://zonduu.me/posts/idor-session-cookie/
