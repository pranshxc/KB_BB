---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-09_authentication-bypass.md
original_filename: 2019-12-09_authentication-bypass.md
title: Authentication Bypass
category: documents
detected_topics:
- mfa
- command-injection
- otp
- api-security
tags:
- imported
- documents
- mfa
- command-injection
- otp
- api-security
language: en
raw_sha256: 5c37291f48bd9836b010f83be4dd9b3ef99e532467124ca7dfb699947303d37a
text_sha256: d7fd15f06d7c198054dab5e1283f1fa82734cb3dd2f277fa807a6cc54095db4e
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Authentication Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-09_authentication-bypass.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `5c37291f48bd9836b010f83be4dd9b3ef99e532467124ca7dfb699947303d37a`
- Text SHA256: `d7fd15f06d7c198054dab5e1283f1fa82734cb3dd2f277fa807a6cc54095db4e`


## Content

---
title: "Authentication Bypass"
page_title: "WEIRD 2FA BYPASS. Hi everyone, Today, I would like to… | by ultranoob | Medium"
url: "https://medium.com/@ultranoob/weird-and-simple-2fa-bypass-without-any-test-b869e09ac261"
authors: ["Rushiikesh (@u1tran00b)"]
bugs: ["2FA / MFA bypass"]
bounty: "700"
publication_date: "2019-12-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4899
scraped_via: "browseros"
---

# Authentication Bypass

WEIRD 2FA BYPASS
ultranoob
Follow
2 min read
·
Dec 9, 2019

224

4

Hi everyone,
Today, I would like to talk about a weird vulnerability which I found on a private program that allowed me to bypass their 2FA protection without any test.

Pardon me if there are any mistakes as this is my first write-up.!
So let’s get started!

Introduction:

Whenever i start my hunting on any bug bounty program at first, i use the application as a normal user. It allows me to understand how the application’s workflow. And let me understand which features can be interesting to test. I noticed that the application had a 2FA ( Two Factor Authentication) feature, I enabled it and I started to play with it.

Get ultranoob’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As soon as i enabled it, I noticed that it was a Time-based One Time Password 2FA.
Like after every 30 seconds the OTP was changing inside the Google Authenticator app.
But i was provided some backup codes in case i don’t have access to my device for TOTP.
Now that was something interesting.

Damnn!!!

Bypass:
So while playing around the application,
I enabled the 2FA.
After enabling 2FA, i got some backup codes in case i don’t have access to my device for the TOTP.
I have noted all the backup codes. The backup codes were of 8 digits.
I logged out of the application to test the 2fa. :P
So after entering the email address and password.
I was asked to enter the TOTP. But there was option to login to the application using the backup codes.
I clicked on it. And intentionally, put a random 8 digit number instead of that 8 digit backup code and to my surprise,
it was accepted and i was successfully logged in to the application!
In short, there was no validation for the backup code. They were not validated and hence any random 8 digit would work.

Yayyy!!!!

It was weird to me but i knew it’s a security bug. :D :D

Takeaway:

Sometimes, you don’t need any tools to find valid bug. It’s just about having positive mindset while looking for loopholes.
Understand the application workflow and try looking for issues which would affect the functionality of the application.
Always think like a proton.
Expect the UnExpected!!

Timeline:

December 5, 2019 — Initial Report
December 6, 2019 — Report Triaged
December 6, 2019 — Bounty awarded
December 8, 2019 — Bug Fixed

I hope you enjoyed this reading !
Happy Hacking!

Thank you!

~Ultranoob (https://twitter.com/u1tran00b)
