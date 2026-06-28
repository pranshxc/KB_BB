---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-22_my-first-bug-bounty-2-factor-authentication-bypass.md
original_filename: 2020-05-22_my-first-bug-bounty-2-factor-authentication-bypass.md
title: My First Bug Bounty — 2 Factor Authentication Bypass
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- api-security
language: en
raw_sha256: 6bc1e7bf32dd55afacf597fbd4ab00c53db4dc44ca7e2e2788d27f9815e6f870
text_sha256: 7cd4f9a37987ea7b9ab765f3662e5d8ba40b290c175fe7155eb60e00072ed53f
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug Bounty — 2 Factor Authentication Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-22_my-first-bug-bounty-2-factor-authentication-bypass.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `6bc1e7bf32dd55afacf597fbd4ab00c53db4dc44ca7e2e2788d27f9815e6f870`
- Text SHA256: `7cd4f9a37987ea7b9ab765f3662e5d8ba40b290c175fe7155eb60e00072ed53f`


## Content

---
title: "My First Bug Bounty — 2 Factor Authentication Bypass"
url: "https://medium.com/@talatmehmood1995/my-first-bug-bounty-2-factor-authentication-bypass-b034812c8243"
authors: ["Talatmehmood"]
bugs: ["OTP bypass"]
bounty: "100"
publication_date: "2020-05-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4566
scraped_via: "browseros"
---

# My First Bug Bounty — 2 Factor Authentication Bypass

My First Bug Bounty — 2 Factor Authentication Bypass
Talatmehmood
Follow
2 min read
·
May 22, 2020

276

2

Press enter or click to view image in full size

Hello guys, I hope everyone is doing great!
A little introduction about me, My name is Talat Mehmood and I’m an active bounty hunter, Freelancer and Penetration tester since 2017.

A lot of people asked me to writeup about my first ever bug bounty. Today, I finally got the time to write about it. This vulnerability is actually pretty interesting, so here it goes.

“Summary: I was able to Bypass Phone Number Verification by Tampering Parameters during Sign Up!”

Alright, so I was testing the “Sign up” module of the web application (let’s just call it vulnme.com). I found an interesting parameter in Request along with other parameters that was “twoFactorNotificationType”.

Press enter or click to view image in full size
Sign up Request with vulnerable parameter

By default, the value was set as “0". In the normal flow of application, On login an OTP (One time password) was sent to the provided phone number for verification. Once you’ve entered the correct OTP in the application, you’ll be authenticated.

Get Talatmehmood’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I started tweaking this parameter. I found that when I set this parameter (twoFactorNotificationType) as “1” during sign up, the OTP that was supposed to be sent to the phone number was sent to the email instead xD

This could allow a malicious user to bypass his phone number verification. Further, this vulnerability could be elevated to bypass 2 Factor Authentication if the attacker had access of victim’s email.

So, just changing the value of a parameter earned me my first bounty of €100!!

My First Bug Bounty — Parameter Tampering
CONCLUSION:
Always tweak with all the parameters in the Requests.
Think Out of the Box.
Determination is the key! Never give up too early.
