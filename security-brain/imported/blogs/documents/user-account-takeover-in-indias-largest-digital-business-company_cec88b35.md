---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-16_user-account-takeover-in-indias-largest-digital-business-company.md
original_filename: 2018-09-16_user-account-takeover-in-indias-largest-digital-business-company.md
title: User Account takeover in India’s largest digital business company
category: documents
detected_topics:
- command-injection
- otp
tags:
- imported
- documents
- command-injection
- otp
language: en
raw_sha256: cec88b356244ff471b339e52ab16d030cdd0d1036a1bf277e34157c7369c6efa
text_sha256: 367cb0235a18e04721166e3044def65aa2874a5582c92067d48daf9d4b616258
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# User Account takeover in India’s largest digital business company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-16_user-account-takeover-in-indias-largest-digital-business-company.md
- Source Type: markdown
- Detected Topics: command-injection, otp
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `cec88b356244ff471b339e52ab16d030cdd0d1036a1bf277e34157c7369c6efa`
- Text SHA256: `367cb0235a18e04721166e3044def65aa2874a5582c92067d48daf9d4b616258`


## Content

---
title: "User Account takeover in India’s largest digital business company"
url: "https://medium.com/bugbountywriteup/user-account-takeover-in-indias-largest-digital-business-company-c7b6d61dadb9"
authors: ["Minali Arora (@AroraMinali)"]
bugs: ["Account takeover", "OTP bypass"]
publication_date: "2018-09-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5697
scraped_via: "browseros"
---

# User Account takeover in India’s largest digital business company

User Account takeover in India’s largest digital business company
Minali Arora
Follow
1 min read
·
Sep 16, 2018

197

2

Hi Everyone,

Recently, I found this vulnerability in one of the India’s largest digital business organization. Although, this is not exactly aimed for bug bounty but what worries me more is that in this Internet dominated era, our data is exposed and is at heightened risk of getting abused.

Get Minali Arora’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While signing up as a new user, the OTP is sent to the mobile number registered with the account. Submit the OTP value from your mobile device and intercept the request. Edit the mobile number with an already registered number. You can login as another user in the application and perform action on his behalf. The response includes the user’s email address, name and contact number.

Press enter or click to view image in full size
Press enter or click to view image in full size

The OTP is not mapped with the user’s mobile number during sign up and is not validated at server end. It is always mandatory to implement server side validations. Client side controls should never be trusted.
