---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1448218'
original_report_id: '1448218'
title: Sensitive information disclosure on grafana
team_handle: jetblue
created_at: '2022-01-12T20:27:44.077Z'
disclosed_at: '2024-02-26T22:02:26.158Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 40
asset_identifier: www.jetblue.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Sensitive information disclosure on grafana

## Metadata

- HackerOne Report ID: 1448218
- Weakness: 
- Program: jetblue
- Disclosed At: 2024-02-26T22:02:26.158Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

While running through scan I got some endpoints on jetblue subdomains which discloses sensitive information. I know these are out of scope but I think it is necessary to report them

## Steps To Reproduce:

  1. Visit the urls in browser

`https://████.jetblue.com/metrics`

███

Discloses  grafana metrics  to unauthorized users

```
https://█████████.jetblue.com/sap/public/info
https://████.jetblue.com/sap/public/info
```

██████

Disclose sensitive information about SAP  such as internal IP address and OS

`https://███████.travelproducts.jetblue.com/`

███████

aws bucket listing is enabled which discloses sensitive endpoints to unauthorized users

## Impact

Unauthorized user can access sensitive info about server resources.

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
