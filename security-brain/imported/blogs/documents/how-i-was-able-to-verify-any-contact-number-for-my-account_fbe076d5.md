---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-17_how-i-was-able-to-verify-any-contact-number-for-my-account.md
original_filename: 2020-03-17_how-i-was-able-to-verify-any-contact-number-for-my-account.md
title: How I was able to verify any contact number for my account?
category: documents
detected_topics:
- mfa
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- mfa
- command-injection
- path-traversal
- otp
language: en
raw_sha256: fbe076d5fb015d227bc43460a5b2e32c86912c833f2c3a2330d51267d69e15af
text_sha256: 03546003ff830bf60cc22ccf999fdb8b812fa181752d75c5d788acc675b3a8f9
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to verify any contact number for my account?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-17_how-i-was-able-to-verify-any-contact-number-for-my-account.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `fbe076d5fb015d227bc43460a5b2e32c86912c833f2c3a2330d51267d69e15af`
- Text SHA256: `03546003ff830bf60cc22ccf999fdb8b812fa181752d75c5d788acc675b3a8f9`


## Content

---
title: "How I was able to verify any contact number for my account?"
url: "https://medium.com/@parasarora06/how-i-was-able-to-verify-any-contact-number-for-my-account-57c939dab202"
authors: ["Paras Arora (@parasarora06)"]
bugs: ["OTP bypass", "2FA / MFA bypass"]
publication_date: "2020-03-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4704
scraped_via: "browseros"
---

# How I was able to verify any contact number for my account?

How I was able to verify any contact number for my account?
Paras Arora
Follow
1 min read
·
Mar 17, 2020

17

OTP Bypass | Second Factor Authentication (2FA) Bypass

Let’s come to the point directly.

Goal: Adding and verifying any phone number without providing OTP

Website name changed to : Redacted.com

I was enumerating a subdomain of redacted.com i.e subdomain.redacted.com

Registered and made account on this and was struggling to find something in this portal.

I got a feature of adding a phone number, I thought to add. my phone number so I provided mine and verified the OTP but I intercepted the response and analysed it.

Try1: I edited my phone number to my other phone number and again it sent an OTP but this time I decided to not provide correct OTP, I started manipulating the response and failed.

Get Paras Arora’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I compared the response of correct OTP and Invalid OTP

the difference was in response code and a JSON message

Incorrect OTP Response code: 400

Failed JSON message : {“verificationCode”:[{“Code”:”invalid.code”}]}

Bypass: I modified the response code to 204 NO CONTENT Which means The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.

Question : Why I changed response code to 204?

Answer: Because when I registered my own number with valid OTP I analysed the response and It was having valid response with a code of 204.

That was simple though !!

Linkedin: Paras Arora

Twitter: Paras Arora
