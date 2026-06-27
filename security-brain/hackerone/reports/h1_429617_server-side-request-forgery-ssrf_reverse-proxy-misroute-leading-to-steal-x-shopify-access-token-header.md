---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '429617'
original_report_id: '429617'
title: Reverse Proxy misroute leading to steal X-Shopify-Access-Token header
weakness: Server-Side Request Forgery (SSRF)
team_handle: shopify
created_at: '2018-10-27T10:16:39.287Z'
disclosed_at: '2019-03-14T10:50:35.082Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 84
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Reverse Proxy misroute leading to steal X-Shopify-Access-Token header

## Metadata

- HackerOne Report ID: 429617
- Weakness: Server-Side Request Forgery (SSRF)
- Program: shopify
- Disclosed At: 2019-03-14T10:50:35.082Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Shopify team! I found out that on /admin/api/graphql endpoint server fetches content of Host header value (${HTTP_Host} + /admin/api/graphql). If my own host was sent to server, request comes from ██████████or ██████████ (your google cloud cluster). Also I can grab all reverse proxy headers including X-Shopify-Access-Token.

example of such request in base64:

```
███
```


Also it returns response your server got on ${HTTP_Host} + /admin/api/graphql address


How to reproduce:
1. POST /admin/api/graphql with Host pointing to external website
2. As external website owner grab incoming headers.

## Impact

SSRF, X-Shopify-Access-Token leakage

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
