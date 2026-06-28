---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-07_access-to-crowdtangle-deletion-framework-api.md
original_filename: 2021-08-07_access-to-crowdtangle-deletion-framework-api.md
title: Access to CrowdTangle Deletion Framework API
category: documents
detected_topics:
- access-control
- command-injection
- otp
- graphql
tags:
- imported
- documents
- access-control
- command-injection
- otp
- graphql
language: en
raw_sha256: 60a7c4ab2520249deaebb089b70fcd85f0aeb54eb00812538cb63efca2639acc
text_sha256: 5c7a836a96564de69e7011ace5b8f001aa684a9bc1c21d5b116ff9bbc81eac79
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Access to CrowdTangle Deletion Framework API

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-07_access-to-crowdtangle-deletion-framework-api.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `60a7c4ab2520249deaebb089b70fcd85f0aeb54eb00812538cb63efca2639acc`
- Text SHA256: `5c7a836a96564de69e7011ace5b8f001aa684a9bc1c21d5b116ff9bbc81eac79`


## Content

---
title: "Access to CrowdTangle Deletion Framework API"
page_title: "Access to CrowdTangle Deletion Framework API - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/access-to-crowdtangle-deletion-framework-api/"
final_url: "https://philippeharewood.com/access-to-crowdtangle-deletion-framework-api/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "GraphQL"]
publication_date: "2021-08-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3436
---

Posted on [August 7, 2021August 25, 2021](https://philippeharewood.com/access-to-crowdtangle-deletion-framework-api/)

# Access to CrowdTangle Deletion Framework API

There is a root GraphQL query that gives one access to numerous CrowdTangle API calls including one that lists the deleted objects for popular Facebook entities by date.

Regular users shouldn’t have access to CrowdTangle this way. The data was of the form  
  
{`"__typename":"CrowdTangleDeletionResult","id":"111111","parent_id":"22222","system":"fb"}`  
  
From my understanding, this was a result that contained a Facebook post. The parent_id supposedly points to the CrowdTangle/Facebook account owner/board. I downloaded ~40,000 results for the period of August 4th, 5th, 7th and 8th. This was a large enough sample size to convince myself that the parent_id was in some cases with a high level of confidence one of the following:  
  
1\. A recently deleted page (I cross checked with a simple Google search and Google cache)  
2\. A page with a high following that recently deleted posts in bulk  
  
According to Facebook, this wasn’t enough to pass the bar for a bounty.  
  
_Please note that here the original impact described in this issue, being able to know the ids and parent_id of deleted object was falling below the bar for a monetary reward, but we will reward this report because we discovered security hardening opportunity that we implemented._

**Timeline**

Aug 7, 2021 – Report sent  
Aug 17, 2021 – Fixed by Facebook
