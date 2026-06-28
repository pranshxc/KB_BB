---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-26_sidefxpoc-user-enumeration-no-rate-limeted-in-send-message-function.md
original_filename: 2019-04-26_sidefxpoc-user-enumeration-no-rate-limeted-in-send-message-function.md
title: '[sidefx][Poc] user enumeration & no rate limeted in send message function'
category: documents
detected_topics:
- rate-limit
- idor
- command-injection
tags:
- imported
- documents
- rate-limit
- idor
- command-injection
language: en
raw_sha256: 3d1b71b6e9979cd8e942f15091f18e4f2e0db19839d4f3060fdca6dc32ed263b
text_sha256: 81e611728b6962603217e1fc2f9c301409da649336afeb4176eae1400c0538ae
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# [sidefx][Poc] user enumeration & no rate limeted in send message function

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-26_sidefxpoc-user-enumeration-no-rate-limeted-in-send-message-function.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `3d1b71b6e9979cd8e942f15091f18e4f2e0db19839d4f3060fdca6dc32ed263b`
- Text SHA256: `81e611728b6962603217e1fc2f9c301409da649336afeb4176eae1400c0538ae`


## Content

---
title: "[sidefx][Poc] user enumeration & no rate limeted in send message function"
url: "https://medium.com/@protostar0/sidefx-poc-user-enumeration-no-rate-limeted-in-send-message-function-953f1662d41"
authors: ["Abdelhak Kharroubi"]
programs: ["SideFX"]
bugs: ["Username enumeration", "Lack of rate limiting"]
bounty: "100"
publication_date: "2019-04-26"
added_date: "2022-10-12"
source: "pentester.land/writeups.json"
original_index: 5286
scraped_via: "browseros"
---

# [sidefx][Poc] user enumeration & no rate limeted in send message function

[sidefx][Poc] user enumeration & no rate limeted in send message function
Abdelhak Kharroubi
Follow
1 min read
·
Apr 26, 2019

64

Describe Vulnerability :

User enumeration is possible through Sent Messages(send message function have no rate limit)

Url Vulnerable:

https://www.sidefx.com/profile/messages/write/ with login account

How to reproduce this issue:

1- go to https://www.sidefx.com/profile/messages/write/

2-put user that you want enumerate (example support or admin )

3- put any data in subject and body

4- if the status of request 301 redirect that means user exist
if the status of request 200 means failed to send message and user doesn’t exist

poc in this video https://www.youtube.com/watch?v=2AVWwz9Qg1U&list=PLwCg7N_pHdKSd1J0Z_snYYpJhpc449Ql_&index=2&t=1s

Get Abdelhak Kharroubi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

impact

Possibility to enumerate in large scale several users existing in the website.

ps

they haven’t limit to send message

any one can make scripte with python or with burp intruder

i test with burp intruder

i found 216 user exist in 2323 request

Press enter or click to view image in full size

whene i return in account the messages was sent

Press enter or click to view image in full size

bounty: 100$ cad :D
