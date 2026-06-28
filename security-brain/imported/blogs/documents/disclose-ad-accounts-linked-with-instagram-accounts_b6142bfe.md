---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-02_disclose-ad-accounts-linked-with-instagram-accounts.md
original_filename: 2021-12-02_disclose-ad-accounts-linked-with-instagram-accounts.md
title: Disclose Ad Accounts linked with Instagram Accounts
category: documents
detected_topics:
- command-injection
- otp
- graphql
- information-disclosure
- business-logic
tags:
- imported
- documents
- command-injection
- otp
- graphql
- information-disclosure
- business-logic
language: en
raw_sha256: b6142bfeaca57c89e6a7b3e91338f2c7cc7cdb3ab1e70c4fb5a37cf2f00e2971
text_sha256: cc173fce9d46c5a4b883300967a67eed15bbc36d01a7bfe704d4337b51c60ac6
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Disclose Ad Accounts linked with Instagram Accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-02_disclose-ad-accounts-linked-with-instagram-accounts.md
- Source Type: markdown
- Detected Topics: command-injection, otp, graphql, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `b6142bfeaca57c89e6a7b3e91338f2c7cc7cdb3ab1e70c4fb5a37cf2f00e2971`
- Text SHA256: `cc173fce9d46c5a4b883300967a67eed15bbc36d01a7bfe704d4337b51c60ac6`


## Content

---
title: "Disclose Ad Accounts linked with Instagram Accounts"
url: "https://www.yesnaveen.com/Instagram-ad-account-disclosure"
final_url: "https://www.naveen.sh/2021/12/Instagram-ad-account-disclosure.html"
authors: ["Naveen (@NaveenHax)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Logic flaw", "GraphQL"]
bounty: "1,500"
publication_date: "2021-12-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3118
---

###  Disclose Ad Accounts linked with Instagram Accounts 

### 

### Description

There exists a GraphQL endpoint in Instagram which allowed me to view Ad account linked to an Instagram Profile.

### Impact

A malicious user could've used this bug in order to retrieve Ad account linked to an Instagram Account, which would lead to Identification/De-anonymization.

  

### Proof of concept
  
  
  POST
  https://i.instagram.com/api/v1/ads/graphql
  
  doc_id=REDACTED&query_params=
  {"query_params":{"access_token":"","id":"userID"}}
  
  
  
  

### Timeline

6 November 2021 - Report sent

8 November 2021 - Need More Info

11 November 2021 - Triaged

2 December 2021 - 1500$ Bounty rewarded by Meta

[ December 02, 2021  ](https://www.naveen.sh/2021/12/Instagram-ad-account-disclosure.html "permanent link")
