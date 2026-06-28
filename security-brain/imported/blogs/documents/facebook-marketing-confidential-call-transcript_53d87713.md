---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-24_facebook-marketing-confidential-call-transcript.md
original_filename: 2019-03-24_facebook-marketing-confidential-call-transcript.md
title: Facebook Marketing Confidential Call Transcript
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 53d87713b4b3adb37dc9c73cafa17b9edee8e20d2e0538e4185b5956fec17c0d
text_sha256: 173b058d75a9263447a11363ac8f8324ccff7a3a62b49475636c8c6d4433662a
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Marketing Confidential Call Transcript

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-24_facebook-marketing-confidential-call-transcript.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `53d87713b4b3adb37dc9c73cafa17b9edee8e20d2e0538e4185b5956fec17c0d`
- Text SHA256: `173b058d75a9263447a11363ac8f8324ccff7a3a62b49475636c8c6d4433662a`


## Content

---
title: "Facebook Marketing Confidential Call Transcript"
page_title: "Facebook Marketing Confidential Call Transcript - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/facebook-marketing-confidential-call-transcript/"
final_url: "https://philippeharewood.com/facebook-marketing-confidential-call-transcript/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2019-03-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5345
---

Posted on [March 24, 2019](https://philippeharewood.com/facebook-marketing-confidential-call-transcript/)

# Facebook Marketing Confidential Call Transcript

fburl.com URLs are normally only accessible for Facebook employees. Via a specific misconfiguration, it was possible to resolve short links. 

fburl.com/<redacted>

This contained a 1 hour long transcript between Facebook Marketing Team and a large known web company. I didn’t opt to review the full conversation as a few minutes in, it was stated from one of the employees that the conversation should be confidential.

**Impact**  
  
A call transcript was publicly accessible which could have disclosed internal information.

**Reference**  
  
<https://shubs.io/exploiting-url-shortners-to-discover-sensitive-resources-2/>

**Timeline**

Mar 24, 2019 – Report Sent  
Mar 30, 2019 – Further investigation by Facebook  
Mar 30, 2019 – $500 Bounty Awarded by Facebook during BountyCon  
May 2, 2019 – Transcript removed
