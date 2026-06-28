---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-29_pii-disclosure-worth-750.md
original_filename: 2023-11-29_pii-disclosure-worth-750.md
title: PII Disclosure Worth $750
category: documents
detected_topics:
- sso
- command-injection
- information-disclosure
tags:
- imported
- documents
- sso
- command-injection
- information-disclosure
language: en
raw_sha256: 3c4ef502bcdb07999fff351de4e96e12d077c207143180826fa90d42db72de4f
text_sha256: 380260275b4d1263f6e21d032ae1c2539d39c4e0b17b09485c927ea96c037728
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# PII Disclosure Worth $750

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-29_pii-disclosure-worth-750.md
- Source Type: markdown
- Detected Topics: sso, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `3c4ef502bcdb07999fff351de4e96e12d077c207143180826fa90d42db72de4f`
- Text SHA256: `380260275b4d1263f6e21d032ae1c2539d39c4e0b17b09485c927ea96c037728`


## Content

---
title: "PII Disclosure Worth $750"
url: "https://vijetareigns.medium.com/pii-disclosure-worth-750-758b72e7e8ca"
authors: ["the_unluck_guy (@7he_unlucky_guy)"]
bugs: ["Information disclosure"]
bounty: "750"
publication_date: "2023-11-29"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 662
scraped_via: "browseros"
---

# PII Disclosure Worth $750

Member-only story

PII Disclosure Worth $750
the_unlucky_guy
Follow
3 min read
·
Nov 29, 2023

1K

7

FREE ARTICLE LINK👈

Hello hackers, I am back with a new bug bounty write-up. In this blog, I am going to show how I found PII disclosure in one of the Unicorn of India. The company is having a public bug bounty program on Hackerone. I will be using redacted.com as the main domain.

The company is a technology platform through which customers book different types of services.

www.redacted.com and api.redacted.com are in scope. As usual, I started exploring the application and capturing every request in the proxy tool burp suite. redacted.com is the main domain but all the traffic routes through api.redacted.com. I used the company in the past to book some services so I have some bookings in my account.

After exploring the application, I started reviewing all the requests and responses from the api.redacted.com. There is one endpoint https://api.redacted.com/api/v2/help-recovery/gethelp/getHelpFlow POST request to the endpoint with body {"user_type":"customer","flow_type":"request","request_id":"XXXXX","group_key":"view_payment_summary_group","mode":"published"} is used to fetch the payment summary of the booked service. During reviewing the response of the endpoint. I found that the personal contact details of the service provider in key masked_number are exposed in plain text.

Press enter or click to view image in full size
