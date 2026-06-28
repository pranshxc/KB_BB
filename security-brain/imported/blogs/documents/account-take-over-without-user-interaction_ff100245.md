---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-02_account-take-over-without-user-interaction.md
original_filename: 2020-04-02_account-take-over-without-user-interaction.md
title: Account Take Over without user Interaction
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- information-disclosure
language: en
raw_sha256: ff100245f8df03aca3805b3ea0f93669666b0eb1616a8cba7d1245e9b17131bb
text_sha256: 7a8b8f9c912e811fb89ba4e947c66e5d18346613bd2d9a11a6dbd809ec59408e
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Account Take Over without user Interaction

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-02_account-take-over-without-user-interaction.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `ff100245f8df03aca3805b3ea0f93669666b0eb1616a8cba7d1245e9b17131bb`
- Text SHA256: `7a8b8f9c912e811fb89ba4e947c66e5d18346613bd2d9a11a6dbd809ec59408e`


## Content

---
title: "Account Take Over without user Interaction"
url: "https://medium.com/@ravillabharath123/account-take-over-without-user-interaction-f4ed2bf977de"
authors: ["Ravilla Bharath"]
bugs: ["Password reset", "Information disclosure", "Account takeover"]
publication_date: "2020-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4673
scraped_via: "browseros"
---

# Account Take Over without user Interaction

Account Take Over without user Interaction
Ravilla Bharath
Follow
2 min read
·
Apr 2, 2020

117

3

Hello hunters, Hope you doing good.

I want to share you something about my finding, Which went DUPLICATE.

Lets dive into the topic.

Assume the program name Redacted.com .

Get Ravilla Bharath’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Attack Vector :

Application contains forget password functionality. Enter the victim email-id, capture the request and response.
Forget Password Request

2. In response I observed a token transmission. Got clarity after checking the inbox. That the token belongs to Reset password.

Press enter or click to view image in full size
The response contains the token

3. Crafted the reset-password link by using “Token” value from the response :

https://Redacted.com/reset-password/09ef7xxx-xxxx-xxxx-xxxx-xxxxxxxxx62b?partner=

4. BOOM ! Successfully changed the victims password and access the account.

This is my first blog. Thanks for reading :)

GOOD LUCK ! Happy Hunting.
