---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-31_broken-function-level-authorization-leads-to-disclosing-pii-information-of-all-c.md
original_filename: 2023-01-31_broken-function-level-authorization-leads-to-disclosing-pii-information-of-all-c.md
title: Broken Function Level Authorization leads to disclosing PII Information of
  all company users
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 9da86c2fad6c2f5dc50349f5edc3d84f997d275507e4d20fa7e363af3e97f86d
text_sha256: 78f47fa45e570d1f060d62abc50e2313a73123af86550c7913754282e52baca6
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Broken Function Level Authorization leads to disclosing PII Information of all company users

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-31_broken-function-level-authorization-leads-to-disclosing-pii-information-of-all-c.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `9da86c2fad6c2f5dc50349f5edc3d84f997d275507e4d20fa7e363af3e97f86d`
- Text SHA256: `78f47fa45e570d1f060d62abc50e2313a73123af86550c7913754282e52baca6`


## Content

---
title: "Broken Function Level Authorization leads to disclosing PII Information of all company users"
url: "https://webresearcher007.medium.com/broken-function-level-authorization-leads-to-disclosing-pii-information-of-all-company-users-35aee60b287b"
authors: ["Mirza Muhammad Fauzan"]
bugs: ["Broken Function Level Authorization", "Information disclosure"]
publication_date: "2023-01-31"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1598
scraped_via: "browseros"
---

# Broken Function Level Authorization leads to disclosing PII Information of all company users

Broken Function Level Authorization leads to disclosing PII Information of all company users
Mirza Muhammad Fauzan
Follow
2 min read
·
Jan 31, 2023

58

بسم الله الرحمن الرحيم

What is PII?

Personal data, also known as personal information or personally identifiable information, is any information related to an identifiable person.

PII

I found a BFLA (Broken Function Level Authorization) vulnerability during API pen testing in which PII information was disclosed to all company users.

What is BFLA (Broken Function Level Authorization)?

Broken function-level authorization is similar to Broken object-level authorization. Both relate to attackers accessing API endpoints that they are not authorized to, due to inadequate or improper authorization mechanisms to validate user requests.

Get Mirza Muhammad Fauzan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I do API penetration testing through the Postman tool. I configured a Postman tool with the burp suite and I forwarded all traffic to the burp suite through Postman. I attached a video link about how you can configure the Postman with the burp suite.

Configure Postman with Burp

My company gave me an API collection for pen testing. I can't disclose the company URL because it is confidential. I just go to the Postman and import API collection into the Postman. I saw a PATCH request in an API collection for a User update profile.

Press enter or click to view image in full size
PATCH Request of Update User Profile

I just intercept the burp and send a request to the Burp suite.

Original Request

I just remove the body parameter username of a request and remove the user-id from the URL and change the request PATCH to GET .

Modified Request

Forward the modified request to the repeater tab and I saw a response with PII information disclosed to all company users.

Press enter or click to view image in full size
PII Information disclosed to all company users

No reward for this finding because this is my full-time job :)

Thanks for reading this article.
