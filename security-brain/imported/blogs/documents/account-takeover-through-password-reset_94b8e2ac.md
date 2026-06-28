---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-14_account-takeover-through-password-reset.md
original_filename: 2020-11-14_account-takeover-through-password-reset.md
title: Account takeover through password reset
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- api-security
language: en
raw_sha256: 94b8e2ac4ae37feefd051c3f343704e16647ca6f17ed872a0435cbc635e1cce9
text_sha256: b061baca2c0cee332f3b6ddb0dff32881c668746c6078dc3354a2ce149676fc3
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Account takeover through password reset

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-14_account-takeover-through-password-reset.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `94b8e2ac4ae37feefd051c3f343704e16647ca6f17ed872a0435cbc635e1cce9`
- Text SHA256: `b061baca2c0cee332f3b6ddb0dff32881c668746c6078dc3354a2ce149676fc3`


## Content

---
title: "Account takeover through password reset"
url: "https://medium.com/@seaman00o/account-takeover-through-password-reset-82adc0c19248"
authors: ["Omar Hamdy (@seaman00o)"]
bugs: ["Account takeover", "Password reset"]
bounty: "2,000"
publication_date: "2020-11-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4134
scraped_via: "browseros"
---

# Account takeover through password reset

Member-only story

Account takeover through password reset
Omar Hamdy
3 min read
·
Nov 14, 2020

--

2

--

Press enter or click to view image in full size

Hello Everyone,

I’m Omar Hamdy (Seaman), Today I am going to explain one of the coolest bugs which I found on Private Program in Bugcrowd

Let’s Start,

I had a private program, let’s call it redacted.com, After a while of reconnaissance the program, I began to examine the password reset function, Usually I look for vulnerabilities like (ATO, Host Header injection)

Simply, When the user wants to reset his password, he enters his first & last name and e-mail. A password reset link will be sent to his email.

I requested a password reset for my account and then intercepted the request (via Zap proxy) to examine it closely.

I found the request as this :

Press enter or click to view image in full size

And the password reset link is :

https://redacted.com/Reset?token=04294876770750

So far nothing exciting, I used the link, changed my password and Intercepted the Request, Here I found something very interesting.

I found the request as this :
