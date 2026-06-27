---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '203384'
original_report_id: '203384'
title: HTTP trace method is enabled on gip.rocks
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2017-02-04T11:05:16.649Z'
disclosed_at: '2017-04-08T11:06:44.196Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# HTTP trace method is enabled on gip.rocks

## Metadata

- HackerOne Report ID: 203384
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-04-08T11:06:44.196Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

HTTP TRACE method is enabled on your server which should not be enabled. It can lead to cross site tracing !

Cross site tracing: https://www.owasp.org/index.php/Cross_Site_Tracing

```
curl -X TRACE http://gip.rocks/ -vv
* Hostname was NOT found in DNS cache
*   Trying 184.73.218.93...
* Connected to gip.rocks (184.73.218.93) port 80 (#0)
> TRACE / HTTP/1.1
> User-Agent: curl/7.35.0
> Host: gip.rocks
> Accept: */*
> 
< HTTP/1.1 200 OK
< Connection: keep-alive
* Server gunicorn/18.0 is not blacklisted
< Server: gunicorn/18.0
< Date: Sat, 04 Feb 2017 10:59:49 GMT
< Transfer-Encoding: chunked
< Content-Type: text/html; charset=UTF-8
< Via: 1.1 vegur
< 
```

## Mitigation:

Disable TRACE method support on your server.

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
