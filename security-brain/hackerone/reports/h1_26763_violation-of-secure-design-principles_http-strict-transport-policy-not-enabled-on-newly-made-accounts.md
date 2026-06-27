---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '26763'
original_report_id: '26763'
title: HTTP Strict Transport Policy not enabled on newly made accounts
weakness: Violation of Secure Design Principles
team_handle: slack
created_at: '2014-09-03T00:52:20.744Z'
disclosed_at: '2014-10-03T23:38:52.854Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# HTTP Strict Transport Policy not enabled on newly made accounts

## Metadata

- HackerOne Report ID: 26763
- Weakness: Violation of Secure Design Principles
- Program: slack
- Disclosed At: 2014-10-03T23:38:52.854Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey
As we know that the HSTS prevents MITM against SSL. I just checked the headers of the account i created localhost.slack.com

SERVER RESPONSE: 200 OK
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Encoding: gzip
Content-Type: text/html; charset="utf-8"
Date: Wed, 03 Sep 2014 00:45:35 GMT
Expires: Mon, 26 Jul 1997 05:00:00 GMT
Pragma: no-cache
Server: Apache
Vary: Accept-Encoding
X-Frame-Options: SAMEORIGIN
X-Robots-Tag: noindex,nofollow
X-XSS-Protection: 0
Content-Length: 4606
Connection: keep-alive

The HSTS is not set here. 
Awaiting your reply

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
