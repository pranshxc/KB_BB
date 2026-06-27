---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '42780'
original_report_id: '42780'
title: Web Server information disclosure.
weakness: Information Disclosure
team_handle: nearby
created_at: '2015-01-07T17:08:33.742Z'
disclosed_at: '2015-12-20T03:52:34.116Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Web Server information disclosure.

## Metadata

- HackerOne Report ID: 42780
- Weakness: Information Disclosure
- Program: nearby
- Disclosed At: 2015-12-20T03:52:34.116Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear sirs.

Seems to have a vulnerability that exposed Web System information through the HTTP Headers Methods.

As a PoC run:

# nc -vv www.wnmlive.com 80
DNS fwd/rev mismatch: www.wnmlive.com != ec2-54-67-11-12.us-west-1.compute.amazonaws.com
www.wnmlive.com [54.67.11.12] 80 (http) open
OPTIONS / HTTP/1.1
Host: www.wnmlive.com

HTTP/1.1 200 OK
Cache-Control: no-transform
Allow: OPTIONS, TRACE, GET, HEAD, POST
Server: Microsoft-IIS/8.0
Public: OPTIONS, TRACE, GET, HEAD, POST
X-Powered-By: ASP.NET
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Access-Control-Request-Method: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Headers: Content-Type, Accept, origin, referring-domain, X-UNIT-MEASUREMENT, X-AUTH-TOKEN, X-DEVICE-TYPE, X-SOFTWARE-VERSION
Date: Wed, 07 Jan 2015 17:00:11 GMT
Content-Length: 0
^C sent 42, rcvd 518

Expose information which let anyone know that Microsoft-IIS/8.0 with ASP.NET is running.

Also the Methods Allow: OPTIONS, TRACE, GET, HEAD, POST

Thank you for your attention.

Best Regards,

Javier Romero

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
