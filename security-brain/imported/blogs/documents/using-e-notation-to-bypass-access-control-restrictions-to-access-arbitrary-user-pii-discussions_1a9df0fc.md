---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-12_using-e-notation-to-bypass-access-control-restrictions-to-access-arbitrary-user-.md
original_filename: 2024-04-12_using-e-notation-to-bypass-access-control-restrictions-to-access-arbitrary-user-.md
title: Using E-Notation to bypass Access Control restrictions to access arbitrary
  user PII-discussions
category: documents
detected_topics:
- access-control
- idor
- ssrf
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- idor
- ssrf
- command-injection
- api-security
language: en
raw_sha256: 1a9df0fc638407ac600b5729449d86132088669c9441c42e8f6e916f8f8d02c3
text_sha256: 00addd134894483463792f5c26edeef1ea5928d9779cfcb98c5ead128201ac4d
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Using E-Notation to bypass Access Control restrictions to access arbitrary user PII-discussions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-12_using-e-notation-to-bypass-access-control-restrictions-to-access-arbitrary-user-.md
- Source Type: markdown
- Detected Topics: access-control, idor, ssrf, command-injection, api-security
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `1a9df0fc638407ac600b5729449d86132088669c9441c42e8f6e916f8f8d02c3`
- Text SHA256: `00addd134894483463792f5c26edeef1ea5928d9779cfcb98c5ead128201ac4d`


## Content

---
title: "Using E-Notation to bypass Access Control restrictions to access arbitrary user PII-discussions"
url: "https://medium.com/@keizobugbounty/using-e-notation-to-bypass-access-control-restrictions-to-access-arbitrary-user-pii-discussions-1fa014b544d4"
authors: ["Keizo (@KeiZo_Zo)"]
bugs: ["IDOR", "Broken Access Control"]
publication_date: "2024-04-12"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 344
scraped_via: "browseros"
---

# Using E-Notation to bypass Access Control restrictions to access arbitrary user PII-discussions

Using E-Notation to bypass Access Control restrictions to access arbitrary user PII-discussions
Keizo
Follow
4 min read
·
Apr 12, 2024

781

7

Press enter or click to view image in full size

The company targeted in this bug bounty research is a large cap company with over 2 million customers worldwide. More specifically the host discussed in this article is a multi-user website with various functions, including discussions feature between the company employees and its users. These discussions are regarded as highly sensitive and include PII data which should be protected accordingly. During the investigation, a vulnerability was discovered that allowed unauthorized access to other users’ discussions through an access control bypass method and IDOR.

Sensitive details about the company and requests are redacted and the requests shown do not represent any real user.

The website’s discussion function utilized a user ID in the API request “GET /api/v1/user/123/discussions” Initially, the ID was protected against IDOR, returning a 403 error if the user lacked access to the entered ID. However, it was noted that entering IDs in unconventional formats, such as “123a” resulted in a 400 error with the message “error from discussions API.” Interestingly, querying a different API request with unconventional user ID format on the same host, such as “GET /api/v1/information/users/123a” returned the same result as the standard request “GET /api/v1/information/users/123” highlighting abnormal behavior in the firstly introduced discussions API.

Press enter or click to view image in full size
Normal request to fetch user’s discussions

Multiple attempts were made to exploit the discussions API user ID validation, revealing inconsistent responses to different ID formats.

”123aaa” —> 400 – ”Error from discussions api”
”123” —> 200 – ”Discussions for user 123: …”
”123.0” —> 200 – ”Discussions for user 123: …”
”123.2” —> 200 – ”Discussions for user 123: …”
”111.0” —> 403 – ”User has no access to this id”
”1234” —> 403 – ”User has no access to this id”
”123+1” —> 400 – ”Error from discussions api”
”123/1” —> 400 – ”Error from discussions api”
”123*1” —> 400 – ”Error from discussions api”
”123–0” —> 400 – ”Error from discussions api”

Despite attempts to manipulate IDs using arithmetic operations, they proved ineffective. However, it was observed that modifying the value so that it would result in correct numeric representation to the correct ID allowed successful requests.

Get Keizo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As there are different ways of expressing numbers. This was the next point of focus. The expression could not be hex (123 = 0x7B) and it could not include any characters that are not “url safe” since it had to start with the correct user id. So… here comes the scientific operation called E-notation to the rescue. E-notation is normally used to represent really large or really small numbers that would be too long to conveniently represent in decimal form. For example 100 in E-notation would be represented as 10e1 or 1000e-1 or possibly as 10.0e1. There is a great calculator that was used during this case that helped a lot with finding the correct representation.

Since the correct expression that is valid to the access control validation, needed to start with the correct user ID. This needed to be taken into consideration. By incorporating the correct user ID with the E-notation into the request, the access control validation was successfully bypassed:

“123e0” (123 in decimal) —> 200 – “Discussions for user 123: …”
“123e1” (1230) —> 200 – “Discussions for user 1230: You should not see this…”
Press enter or click to view image in full size
Incorporating E-notation to the request allowed bypass of access control validation (user data in photo is fictive)

This method effectively circumvented access controls by including the necessary pieces for validation while “smuggling” additional values into the backend call. Validation only validated the first numeric characters inputted and the rest was disregarded if the representation was the correct numeric value (e.g. 123.0, 123.3, 123e3).

Press enter or click to view image in full size
Discussions fetch flow that represents inconsistencies in the numeric representation

However, this approach has limitations, restricting traversal to only IDs higher than the user’s own ID by a factor of 10 (e.g., ID 123 could access discussions for users 1230 and above):

“123e1” —> 1230
“123.1e1” —> 1231
“123.2e1” —> 1232

Furthermore, certain edge cases allowed access to users included in the requester’s ID:

“123e-1” —> 12.3 —> user 12
“123e-2” —> 1.23 —> user 1

This vulnerability was caused by the possibility to “smuggle” values into the backend calls to fetch user’s discussions. This was made possible by inconsistent handling of different numeric representations by the backends.

Upon discovery, this vulnerability was promptly reported to the affected company, recognized as a critical severity issue, and rewarded with a significant four-digit bounty.

Diagrams by: https://sequencediagram.org/

E-Notation calculator: https://www.calculatorsoup.com/calculators/math/scientific-notation-converter.php

Sample requests by: https://ssrf.cvssadvisor.com/
