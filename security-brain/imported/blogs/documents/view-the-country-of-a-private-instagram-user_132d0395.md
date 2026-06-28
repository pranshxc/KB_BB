---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-07_view-the-country-of-a-private-instagram-user.md
original_filename: 2021-08-07_view-the-country-of-a-private-instagram-user.md
title: View the country of a private Instagram User
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 132d03954e5938e2729756ed87e43039daa736fabeffb35ca43f7f5a557b206d
text_sha256: 8a6fd5d1109e01a14599f1b571e442ab0f4d9394a5ad6360ee29213db5084a0f
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# View the country of a private Instagram User

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-07_view-the-country-of-a-private-instagram-user.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `132d03954e5938e2729756ed87e43039daa736fabeffb35ca43f7f5a557b206d`
- Text SHA256: `8a6fd5d1109e01a14599f1b571e442ab0f4d9394a5ad6360ee29213db5084a0f`


## Content

---
title: "View the country of a private Instagram User"
page_title: "View the country of a private Instagram User - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/view-the-country-of-a-private-instagram-user/"
final_url: "https://philippeharewood.com/view-the-country-of-a-private-instagram-user/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2021-08-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3437
---

Posted on [August 7, 2021August 21, 2021](https://philippeharewood.com/view-the-country-of-a-private-instagram-user/)

# View the country of a private Instagram User

There is a XController that allows information to be returned about an Instagram user. This feature discloses the country of a private account.

Even if this feature is an ad tool, this does not support the privacy of a private account. Additionally the owner has no way of being aware their location is disclosed like this (as opposed to FB page transparency tool)  

`new AsyncRequest('/ads_rights_manager/account_preview_contents/').setData({ig_ent_user_id:"IG_ID"}).send()`

From the response, the field `main_account_location` discloses the country.  
  
Facebook closed this as informative.

_We have discussed the issue at length and concluded that, whilst you reported a valid issue which the team may make changes based on, unfortunately your report falls below the bar for a monetary reward. This is because leaking the county here is not considered as impactful enough in term of privacy. Also there are many ways to infer the country of a user already._

**Timeline**

Aug 7, 2021 – Report sent  
Aug 9, 2021 – Closed by Facebook as informative
