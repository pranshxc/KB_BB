---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1391549'
original_report_id: '1391549'
title: Request line injection via HTTP/2 in Apache mod_proxy
team_handle: ibb
created_at: '2021-11-04T13:39:46.337Z'
disclosed_at: '2021-11-04T16:11:57.185Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: https://github.com/apache/httpd
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Request line injection via HTTP/2 in Apache mod_proxy

## Metadata

- HackerOne Report ID: 1391549
- Weakness: 
- Program: ibb
- Disclosed At: 2021-11-04T16:11:57.185Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I've written this issue up fully here: https://portswigger.net/research/http2#request

In case it's useful, here's the original report as sent to Apache:

> I'd like to report a vulnerability in Apache mod_proxy when used with HTTP/2 enabled. 
> 
> It fails to reject HTTP requests that contain spaces in the :method HTTP/2 pseudo-header. This leads to a request-line injection vulnerability when it downgrades the requests to HTTP/1.1 and routes them on to the backend.
> 
> Attacker HTTP/2 request:
> ```
> :method: GET /anything HTTP/1.1
> :path: /
> :authority: psres.net
> Accept-Encoding: gzip, deflate
> ```
> Resulting request forwarded to the backend by mod_proxy:
> ```
> GET /anything HTTP/1.1 / HTTP/1.1
> Host:: psres.net
> Accept-Encoding: gzip, deflate  
> ```
> Provided the back-end server tolerates trailing junk in request lines, this enables attackers to bypass front-end security rules, poison web caches, and > change the protocol to HTTP/0.9 or 1.0, potentially enabling further attacks. I have identified some vulnerable systems in the wild.

Please let me know if you'd like any additional information

## Impact

This lets attackers bypass front-end security rules like block-rules and escape subfolders. In some cases it may enable further attacks via protocol-downgrades and cache poisoning.

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
