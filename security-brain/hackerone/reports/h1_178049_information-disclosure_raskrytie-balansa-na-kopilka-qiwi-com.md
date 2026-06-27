---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178049'
original_report_id: '178049'
title: Раскрытие баланса на //kopilka.qiwi.com
weakness: Information Disclosure
team_handle: qiwi
created_at: '2016-10-25T15:54:08.216Z'
disclosed_at: '2017-03-10T20:24:32.222Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# Раскрытие баланса на //kopilka.qiwi.com

## Metadata

- HackerOne Report ID: 178049
- Weakness: Information Disclosure
- Program: qiwi
- Disclosed At: 2017-03-10T20:24:32.222Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

При запросе RAW:
```
GET https://edge.qiwi.com/piggybox-service/piggybox/testt HTTP/1.1
Host: edge.qiwi.com
Connection: keep-alive
accept: application/json
content-type: application/json
```

Сервер возвращает:
```
HTTP/1.1 200 OK
Date: Tue, 25 Oct 2016 15:48:24 GMT
Content-Type: application/json
Content-Length: 182
Connection: keep-alive
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Cache-Control, Authorization, Origin, Content-Type, RequestToken
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Origin: https://kopilka.qiwi.com
Access-Control-Max-Age: 86400
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Server: nginx-wallarm
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block

{"alias":"testt","balance":1,"description":"12233321","goal":0,"name":"\u003cB\u003eHI\u003c/B\u003e","owner":"\u003cB\u003eHI\u003c/B\u003e","recommended":1337,"status":1,"type":0}
```

Как видим в JSON структуре вернулся `balance`

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
