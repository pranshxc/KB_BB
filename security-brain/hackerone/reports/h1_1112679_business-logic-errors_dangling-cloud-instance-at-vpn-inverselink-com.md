---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1112679'
original_report_id: '1112679'
title: Dangling cloud instance at vpn.inverselink.com
weakness: Business Logic Errors
team_handle: security
created_at: '2021-02-27T04:03:24.620Z'
disclosed_at: '2021-03-11T17:58:20.365Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Dangling cloud instance at vpn.inverselink.com

## Metadata

- HackerOne Report ID: 1112679
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2021-03-11T17:58:20.365Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** `	vpn.inverselink.com` points to `54.202.130.246`, which is currently serving a TLS certificate for `Workday, Inc`. This seems to indicate that the subdomain is no longer controlled by HackerOne.

### Optional: Supporting Material/References (Screenshots)
```
% dig  vpn.inverselink.com +short
54.202.130.246

 % curl -v https://vpn.inverselink.com
*   Trying 54.202.130.246...
* TCP_NODELAY set
* Connected to vpn.inverselink.com (54.202.130.246) port 443 (#0)
[...]
* Server certificate:
*  subject: C=US; ST=California; L=Pleasanton; O=Workday Inc.; CN=*.workdaysuv.com
```

### Optional: Did you use [recon data made available by HackerOne](https://github.com/Hacker0x01/helpful-recon-data) to find this vulnerability?
no

## Impact

Subdomain takeover if Workday releases this IP address

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
