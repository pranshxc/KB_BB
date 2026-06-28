---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-02_from-disclosure-to-high-severity-leveraging-dyte-api-key-for-maximum-impact.md
original_filename: 2024-01-02_from-disclosure-to-high-severity-leveraging-dyte-api-key-for-maximum-impact.md
title: 'From Disclosure to High Severity: Leveraging Dyte API Key for Maximum Impact'
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- otp
- information-disclosure
- mobile-security
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- otp
- information-disclosure
- mobile-security
language: en
raw_sha256: ad8dd864d2dce992d326350ef7395e9d6b1b969d3d5ff5e6c85c79cb0766d0a2
text_sha256: 3f9b5329de32e10d2399331ee0427e652bd1d34a7a3a58b160202b90a1c9a009
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# From Disclosure to High Severity: Leveraging Dyte API Key for Maximum Impact

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-02_from-disclosure-to-high-severity-leveraging-dyte-api-key-for-maximum-impact.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, otp, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `ad8dd864d2dce992d326350ef7395e9d6b1b969d3d5ff5e6c85c79cb0766d0a2`
- Text SHA256: `3f9b5329de32e10d2399331ee0427e652bd1d34a7a3a58b160202b90a1c9a009`


## Content

---
title: "From Disclosure to High Severity: Leveraging Dyte API Key for Maximum Impact"
url: "https://padsalatushal.medium.com/from-disclosure-to-high-severity-leveraging-dyte-api-key-for-maximum-impact-468c444963c6"
authors: ["Padsala Tushal (@PadsalaTushal)"]
bugs: ["Hardcoded API keys", "Information disclosure"]
publication_date: "2024-01-02"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 587
scraped_via: "browseros"
---

# From Disclosure to High Severity: Leveraging Dyte API Key for Maximum Impact

From Disclosure to High Severity: Leveraging Dyte API Key for Maximum Impact
Padsala Tushal
Follow
3 min read
·
Jan 2, 2024

73

Press enter or click to view image in full size
Introduction:

As a bug bounty hunter engaged in a VDP program, I recently uncovered a JavaScript file that unveiled a trove of sensitive API keys and tokens. Among them was the Dyte API key, an unfamiliar entity in my exploration. This discovery revealed a mix of widely recognized keys like Google Developer, Stripe API, and Firebase credentials — each holding significant sensitivity. Curiously, while scouring through resources like the Keyhacks GitHub repo, I found no information on exploiting the Dyte API key, particularly the DYTE_ORG_ID and DYTE_KEY.

In this article, I aim to delve into the intricacies of exploiting the Dyte API key, exploring its vulnerabilities and potential impact.

So the javascript file look like this:

Press enter or click to view image in full size

I did a quick Google search to find out more about what the Dyte API key is all about. Turns out, Dyte offers a solution for real-time video and voice integration into websites, mobile apps, and desktop applications. It’s all about making those video and voice calls.

Exploitation:

I stumbled upon the Dyte API documentation at https://docs.dyte.io/guides/rest-apis/quickstart.

Get Padsala Tushal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In Dyte’s API documentation, I discovered that their APIs rely on API Keys for request authentication through HTTP Basic Auth. The process involves sending an HTTP request that includes an Authorization header. This header contains the term ‘Basic,’ followed by a space and a base64-encoded string comprising the organizationId and apiKey. This method ensures secure validation of requests made to Dyte’s APIs.

Press enter or click to view image in full size

I promptly encoded the values of the Dyte organization ID and Dyte key using Base64 in the format ‘organizationId:apiKey’, maintaining the specified order.

Now i have Authorization header value now it is time to test . After i craft following curl request with authoriazaiton header to create a simple test meeting.

curl — request POST \
 — url https://api.dyte.io/v2/meetings \
 — header ‘Authorization: Basic BASE64_VALUE’ \
 — header ‘Content-Type: application/json’ \
 — data ‘{
 “title”: “Sample meeting”,
 “preferred_region”: “ap-south-1”,
 “record_on_start”: false
}’
Press enter or click to view image in full size
Timeline:

14/12/2023 : Discover and Reported

16/12/2023: Changed the state to Triaged

19/12/2023: Changed the state to Resolved

Suggestions are most welcome as always. I will try to keep posting my findings. If you got anything from it, you can press the clap icon below, and don’t forget to follow me on Twitter & Linkedin as well.
See you all next time. :)
