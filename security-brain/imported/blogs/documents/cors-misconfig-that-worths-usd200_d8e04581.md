---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-23_cors-misconfig-that-worths-usd200.md
original_filename: 2021-05-23_cors-misconfig-that-worths-usd200.md
title: CORS misconfig that worths USD200
category: documents
detected_topics:
- command-injection
- otp
- cors
- api-security
tags:
- imported
- documents
- command-injection
- otp
- cors
- api-security
language: en
raw_sha256: d8e0458123dfceaa0584f2abb6376369fe0c5fab866635601412c755e0616b49
text_sha256: 5ce593c973c6583091837db16e7b5b608c22a86308bcc18348c4870fea5fe8d0
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# CORS misconfig that worths USD200

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-23_cors-misconfig-that-worths-usd200.md
- Source Type: markdown
- Detected Topics: command-injection, otp, cors, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `d8e0458123dfceaa0584f2abb6376369fe0c5fab866635601412c755e0616b49`
- Text SHA256: `5ce593c973c6583091837db16e7b5b608c22a86308bcc18348c4870fea5fe8d0`


## Content

---
title: "CORS misconfig that worths USD200"
url: "https://mikekitckchan.medium.com/cors-misconfig-that-worths-usd200-4696eda5ab4c"
authors: ["MikeChan"]
bugs: ["CORS misconfiguration"]
bounty: "200"
publication_date: "2021-05-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3628
scraped_via: "browseros"
---

# CORS misconfig that worths USD200

Member-only story

CORS misconfig that worths USD200
MikeChan
Follow
3 min read
·
May 22, 2021

50

This bug was founded in a private program. So, this post would not disclose any information about the target. In order to not giving out anything about the target, all endpoints, parameters, token names mentioned in this post are made up. This post would name the target as redacted.com.

The bug allows attacker to take advantage of CORS misconfig to steal a token from victim. So, attacker can use that token to utilize unauthorized service of the target on behalf of victim.

Background

I have been working on this target for almost a week. I have tested most of the request and response but nothing much seem interesting to me. So, I have re-checked all request and response in Burpsuite, and I realized one of the request as below is vulnerable to CORS:

GET /token HTTP/1.1
Host: subdomain.redacted.com
Origin: www.redacted.com
Connection: close
Accept: */*
Cookies: some-Cookies=xxxxxxxxxxxx;

And response is like below:

{"some_token":"xxxxxxxxxxxxxxxxxxxxxx"}

This endpoint gives 200 response even I change the Origin header to www.evil.com. So, attacker would able to steal victim’s token. However, if I just report this as a bug, it is most likely to be closed as NA. So, I need to figure out what this token is and how this can be used to create real impact to the target.

The Escalation
