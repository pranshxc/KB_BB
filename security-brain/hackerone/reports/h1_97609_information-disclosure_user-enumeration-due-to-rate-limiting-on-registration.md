---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97609'
original_report_id: '97609'
title: 'User Enumeration : Due to rate limiting on registration'
weakness: Information Disclosure
team_handle: deriv
created_at: '2015-11-04T09:15:31.447Z'
disclosed_at: '2015-11-05T06:41:15.626Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# User Enumeration : Due to rate limiting on registration

## Metadata

- HackerOne Report ID: 97609
- Weakness: Information Disclosure
- Program: deriv
- Disclosed At: 2015-11-05T06:41:15.626Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

There is no rate limiting or improper rate limiting on registration action. So it poses risk of user enumeration vulnerability.

Attacker will fire brute force on following http request (for email parameter) and will analysis results as below : 

If response code : 302 ==> User doesn't exist
If response code : 200 ==> User exists.


HTTP Request : 

POST /new_account/virtual?l=EN HTTP/1.1
Host: www.binary.com
Connection: keep-alive
Content-Length: 101
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: https://www.binary.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Referer: https://www.binary.com/home?l=EN
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: __cfduid=d42e78e7d99272d770a0bf38b3f7ce18f1446628023; _ga=GA1.2.1195925713.1446628044; _dc_gtm_UA-40877026-3=1; hbv_3710=fv%3A1446628047%7Clv%3A1446628047%7Clf%3A0%7Cnv%3A1%7Crf%3A%7Crd%3A%7Cpu%3Abinary.com/home/%3Fl%3Den%7Cdt%3A2015-11-04%7Cdv%3Acomputer; hbs_3710=; __cid=70c6dd2a-5592-4aa9-942e-845dbbda7588; language=EN

residence=in&Email=hacky4594%40gmail.com&chooseapassword=X&chooseapassword_2=X&l=EN

There should be proper rate limiting at this endpoint.

Best.
Shaileshh

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
