---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-17_my-fourth-account-takeover-through-password-reset_2.md
original_filename: 2021-05-17_my-fourth-account-takeover-through-password-reset_2.md
title: My Fourth Account takeover through password reset
category: documents
detected_topics:
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- api-security
language: en
raw_sha256: cf109ac727b21c3a233f9f8ed89b740d1cdc12e2536000d256dff89bbe943f2e
text_sha256: 63c3b013b3028121ede41aefddae26dd4744044ff57af771432545ced1f48528
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# My Fourth Account takeover through password reset

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-17_my-fourth-account-takeover-through-password-reset_2.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `cf109ac727b21c3a233f9f8ed89b740d1cdc12e2536000d256dff89bbe943f2e`
- Text SHA256: `63c3b013b3028121ede41aefddae26dd4744044ff57af771432545ced1f48528`


## Content

---
title: "My Fourth Account takeover through password reset"
url: "https://seaman00o.medium.com/my-fourth-account-takeover-through-password-reset-28a36dfebaf"
authors: ["Omar Hamdy (@seaman00o)"]
bugs: ["Account takeover", "Password reset"]
publication_date: "2021-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3648
scraped_via: "browseros"
---

# My Fourth Account takeover through password reset

Member-only story

My Fourth Account takeover through password reset
Omar Hamdy
Follow
2 min read
·
May 17, 2021

489

Press enter or click to view image in full size

Hello Everyone,

I’m Omar Hamdy (Seaman), Today I am going to explain one of the coolest bugs which I found on Private Program in Bugcrowd

Let’s Start,

I had a private program, let’s call it redacted.com, After a while of reconnaissance the program, I began to examine the my Favorite Function password reset, Usually I look for vulnerabilities like (ATO, Host Header injection).

Simply, When the user wants to reset his password, he enters his email then A password reset link will be sent to his email.

I requested a password reset for my account and the password reset link was :

https://redacted.com/update-password/12d52catcbc344ec-9871-85ac6390d863/1621264272

The password reset link consists of two parts: The user ID and a random 10-digit code.

What I found very interesting here which enables me to takeover any user account is that the 10-digit code is a serial code so that a random value is not generated, but rather a serial value, meaning that if you asked to reset the password for your account and the code was “1618963650”, then you requested a reset The password for the victim’s account will be the code “1618963720”, where the last 3 numbers differed only, allowing us to carry out…
