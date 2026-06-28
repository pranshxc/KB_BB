---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-27_500-for-no-rate-limit-on-forgot-password-page.md
original_filename: 2021-01-27_500-for-no-rate-limit-on-forgot-password-page.md
title: $500 For No Rate Limit On Forgot Password Page
category: documents
detected_topics:
- password-reset
- rate-limit
- command-injection
- otp
- csrf
tags:
- imported
- documents
- password-reset
- rate-limit
- command-injection
- otp
- csrf
language: en
raw_sha256: 6dcce8821d5db8e1cf6f125159276fbdd97cd3c6c42de33774cdb932867f5418
text_sha256: 158ad290850d06afef7fafdf065ab2095d688a3fb0fef93a5e09eee8a6e65a9e
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: true
---

# $500 For No Rate Limit On Forgot Password Page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-27_500-for-no-rate-limit-on-forgot-password-page.md
- Source Type: markdown
- Detected Topics: password-reset, rate-limit, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: True
- Raw SHA256: `6dcce8821d5db8e1cf6f125159276fbdd97cd3c6c42de33774cdb932867f5418`
- Text SHA256: `158ad290850d06afef7fafdf065ab2095d688a3fb0fef93a5e09eee8a6e65a9e`


## Content

---
title: "$500 For No Rate Limit On Forgot Password Page"
url: "https://bugbountyhunter.medium.com/500-for-no-rate-limit-on-forgot-password-page-d534d1d750db"
authors: ["BBHC (@community_bug)"]
bugs: ["Lack of rate limiting", "Password reset"]
bounty: "500"
publication_date: "2021-01-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3964
scraped_via: "browseros"
---

# $500 For No Rate Limit On Forgot Password Page

$500 For No Rate Limit On Forgot Password Page
BBHC
Follow
2 min read
·
Jan 27, 2021

308

Introduction:-

A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.
In case a client made too many requests within a given time frame, HTTP-Servers can respond with status code 429: Too Many Requests

Steps To Reproduce The Issue

Step 1- Go To This Link www.example.com

Enter Email Click On Forget Password

Step 2- Intercept This Request In Burp And Forward Till You Found YOur Number In Request Like (“email”:your email here”)

Get BBHC’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

POST /api/v1/users/password/remind HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://example.com/lost-password
Content-Type: application/json
X-CSRF-TOKEN: xxxxxxxxxxxxxxxxxxxxxx***REDACTED-SUSPECT-TOKEN***Origin: https://example.com
Content-Length: 33
Connection: close
Cookie: __cfduid=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx***REDACTED-SUSPECT-TOKEN***(“email”;”your email here”)

Step 3- Now Send This Request To Intruder And Repeat It 100 Time By Fixing Any Arbitrary Payload Which Doesn’t No Effect Request I Choose Accept-Language: en-US,en;q=0.$5$

Step 4 — See You Will Get 200 ok Status Code & 100 + Email In Your INBOX
See It Is Resulting In Mass Mailing Or Email Bombing To Your Users Which Is Bad For Business Impact

Thank you for reading Follow for more

https://twitter.com/community_bug
