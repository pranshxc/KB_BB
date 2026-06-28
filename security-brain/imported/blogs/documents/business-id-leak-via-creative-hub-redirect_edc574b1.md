---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-20_business-id-leak-via-creative-hub-redirect.md
original_filename: 2019-09-20_business-id-leak-via-creative-hub-redirect.md
title: Business ID leak via Creative Hub redirect
category: documents
detected_topics:
- oauth
- command-injection
- otp
- supply-chain
tags:
- imported
- documents
- oauth
- command-injection
- otp
- supply-chain
language: en
raw_sha256: edc574b1626b27d4f3c67d0e4a2f6ae34f0d48de498d85b1f72318beb1d3bb3d
text_sha256: f9840b0fdf883e7440afd5b899d26cab8822aa0159b79b73d30c16c5a003aab3
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Business ID leak via Creative Hub redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-20_business-id-leak-via-creative-hub-redirect.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, otp, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `edc574b1626b27d4f3c67d0e4a2f6ae34f0d48de498d85b1f72318beb1d3bb3d`
- Text SHA256: `f9840b0fdf883e7440afd5b899d26cab8822aa0159b79b73d30c16c5a003aab3`


## Content

---
title: "Business ID leak via Creative Hub redirect"
page_title: "Business ID leak via Creative Hub redirect - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/business-id-leak-via-creative-hub-redirect/"
final_url: "https://philippeharewood.com/business-id-leak-via-creative-hub-redirect/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Open redirect"]
publication_date: "2019-09-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5020
---

Posted on [September 20, 2019](https://philippeharewood.com/business-id-leak-via-creative-hub-redirect/)

# Business ID leak via Creative Hub redirect

**Proof of Concept**  
  
`https://business.facebook.com/ads/creativehub/select/?redirect_uri=http%3A%2F%2Fgoogle.com`  

**Impact**

The account selection screen at Creative Hub does not validate the redirect URL leading to potential UI confusion that will leak the user’s business ID or personal ad account ID to a third-party website.

**Timeline**

Sep 20, 2019 – Report sent  
Sep 20, 2019 – Confirmation of submission by Facebook  
Sep 21, 2019 – Bounty awarded by Facebook  
Sep 26, 2019 – Confirmation of patch by Facebook
