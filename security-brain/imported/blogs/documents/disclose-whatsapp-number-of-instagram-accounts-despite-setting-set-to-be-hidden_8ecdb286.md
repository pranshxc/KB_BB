---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-19_disclose-whatsapp-number-of-instagram-accounts-despite-setting-set-to-be-hidden.md
original_filename: 2021-08-19_disclose-whatsapp-number-of-instagram-accounts-despite-setting-set-to-be-hidden.md
title: Disclose WhatsApp Number of Instagram Accounts Despite Setting Set to be Hidden
category: documents
detected_topics:
- command-injection
- information-disclosure
- business-logic
tags:
- imported
- documents
- command-injection
- information-disclosure
- business-logic
language: en
raw_sha256: 8ecdb2869823061b786d2bcd7f630e810dc3a59de5929a93525596e7a4013511
text_sha256: 5e22a9ada230b1638df7649bfadf1ffcd2ce8da0a8f33337edb8ac5a1350d793
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Disclose WhatsApp Number of Instagram Accounts Despite Setting Set to be Hidden

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-19_disclose-whatsapp-number-of-instagram-accounts-despite-setting-set-to-be-hidden.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `8ecdb2869823061b786d2bcd7f630e810dc3a59de5929a93525596e7a4013511`
- Text SHA256: `5e22a9ada230b1638df7649bfadf1ffcd2ce8da0a8f33337edb8ac5a1350d793`


## Content

---
title: "Disclose WhatsApp Number of Instagram Accounts Despite Setting Set to be Hidden"
url: "https://www.yesnaveen.com/whatsapp-number-disclosure"
final_url: "https://www.naveen.sh/2021/12/whatsapp-number-disclosure.html"
authors: ["Naveen (@NaveenHax)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Logic flaw"]
bounty: "1,000"
publication_date: "2021-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3407
---

###  Disclose WhatsApp Number of Instagram Accounts Despite Setting Set to be Hidden 

### 

### Description

An Instagram Endpoint was leaking WhatsApp numbers linked with Instagram Accounts

### Impact

This bug could've been used to view the WhatsApp number linked with Instagram Accounts despite the setting set to be hidden.

### Proof of concept
  
  
  POST
  https://i.instagram.com/api/v1/users/[userID]/info/
  

### Timeline

24 June 2021 - Report Sent

30 June 2021 - Need More Info

28 July 2021 - Triaged

06 August 2021 - Fixed

19 August 2021 - $1000 Bounty Rewarded By Facebook

[ August 19, 2021  ](https://www.naveen.sh/2021/12/whatsapp-number-disclosure.html "permanent link")
