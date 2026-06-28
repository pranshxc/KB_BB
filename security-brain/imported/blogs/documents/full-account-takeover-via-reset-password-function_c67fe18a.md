---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-12_full-account-takeover-via-reset-password-function.md
original_filename: 2018-06-12_full-account-takeover-via-reset-password-function.md
title: Full account Takeover via reset password function
category: documents
detected_topics:
- password-reset
- idor
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- password-reset
- idor
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: c67fe18a71d3387ba010c0087f038b69c44987bad15fdc9b0518ae8276719982
text_sha256: b1006701a4bb73827ebde926efe7953e964c08725c5d9c6a85667c650db7ce1d
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Full account Takeover via reset password function

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-12_full-account-takeover-via-reset-password-function.md
- Source Type: markdown
- Detected Topics: password-reset, idor, access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `c67fe18a71d3387ba010c0087f038b69c44987bad15fdc9b0518ae8276719982`
- Text SHA256: `b1006701a4bb73827ebde926efe7953e964c08725c5d9c6a85667c650db7ce1d`


## Content

---
title: "Full account Takeover via reset password function"
url: "https://medium.com/@khaled.hassan/full-account-takeover-via-reset-password-function-8b6ef15f346f"
authors: ["Khaled Hassan"]
bugs: ["IDOR", "Account takeover", "Password reset"]
bounty: "1,250"
publication_date: "2018-06-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5844
scraped_via: "browseros"
---

# Full account Takeover via reset password function

Full account Takeover via reset password function
Khaled Hassan
Follow
2 min read
·
Jun 12, 2018

630

4

Hey Guys,

This is my second write-up in Bug Hunting community and I hope you like this one ;)

I’m going to talk about a common and strange password reset system that I have seen many times in Bug Hunting, PenTesting, etc. and in many cases this system opens the door to attacker to hack user’s accounts.

The story started when I was going to reset my password on a private HackerOne program, and I found something interesting. After I changed my password successfully via password reset URL, I noticed the following request:

Press enter or click to view image in full size

From the first glance, you thought that this request is vulnerable to IDOR vulnerability, But I tried to change (“Email”) parameter to another email address, and I got 403 response, so I asked myself why this was not working even there is no any password reset token on the request or authorization token.

Hmmm, maybe server checking the permission through cookies? I tried to change the cookie and I got the same response 403.

Get Khaled Hassan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After deep thinking I knew how this system works, This system works as follows.

1. User A starts resetting password of User B.

2. User B receives the reset link and clicks on it.

3. The server now will allow the A user to change the password of User B through this endpoint because the resting URL verification is done. When the user clicks on the password reset. This means to the server that the user has clicked on the reset URL that he requested for but in fact he didn’t, the attacker who is requested the password reset. And after this happens user B can change his password through this endpoint without the need for any authorization tokens.

So then we can takeover the user account in the following cases

1. The case of a user started the reset password via email process but he opened the link of reset token and didn’t complete it , maybe he remembered the password during the process of resetting it now we change his password in that case.

2. The attacker starting reset the password of user via his email address and when the user opens the forget password link he received. The server will give the attacker valid permission to change the password of the user through this endpoint using his email address.

Timeline:

13–2–2018 : Vulnerability reported
15–2–2018 : Vulnerability Confirmed
23–2–2018 : Vulnerability Fixed
23–2–2018 : Bounty reward of $1250 issued
