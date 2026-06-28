---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-16_view-the-ranked-messenger-users-for-any-page.md
original_filename: 2019-11-16_view-the-ranked-messenger-users-for-any-page.md
title: View the ranked messenger users for any page
category: documents
detected_topics:
- access-control
- command-injection
- otp
- graphql
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- otp
- graphql
- information-disclosure
language: en
raw_sha256: 1162445bafbf183cbf72d344b195c8b885167e77d252489a05dda4c112ee3d0a
text_sha256: d8f707cd4b7248d915f2cd36af818e5a7941d02e9e6a419747f2ec9e714a0a76
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# View the ranked messenger users for any page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-16_view-the-ranked-messenger-users-for-any-page.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql, information-disclosure
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `1162445bafbf183cbf72d344b195c8b885167e77d252489a05dda4c112ee3d0a`
- Text SHA256: `d8f707cd4b7248d915f2cd36af818e5a7941d02e9e6a419747f2ec9e714a0a76`


## Content

---
title: "View the ranked messenger users for any page"
page_title: "View the ranked messenger users for any page - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/view-the-ranked-messenger-users-for-any-page/"
final_url: "https://philippeharewood.com/view-the-ranked-messenger-users-for-any-page/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Broken authorization"]
publication_date: "2019-11-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4940
---

Posted on [November 16, 2019](https://philippeharewood.com/view-the-ranked-messenger-users-for-any-page/)

# View the ranked messenger users for any page

In Creator Studio there is a new feature to rank messenger users. This isn’t scoped to admins so a user can see which of their friends messaged any page.  
  
`graphql?doc_id=3204638226276173&variables={pageID:113702895386410}`  
  
For pages where the admin disabled messaging, this also causes a page admin disclosure as the the only users still on the list will be those with admin roles who can test messaging on the page. The caveat is the user (with the admin role) must have messaged the page.  
  
**Impact**  
  
An attacker can see which of their friends have messaged a particular page.  
  
**Timeline**  
  
Nov 16, 2019 – Report sent  
Nov 19, 2019 – Confirmation of submission by Facebook  
Nov 27, 2019 – Confirmation of patch by Facebook  
Dec 5, 2019 – Bounty awarded by Facebook
