---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2160178'
original_report_id: '2160178'
title: default credentials at https://52.42.105.71/
weakness: Improper Authentication - Generic
team_handle: trellix
created_at: '2023-09-16T09:13:33.558Z'
disclosed_at: '2024-02-01T16:13:20.093Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 60
asset_identifier: '*.trellix.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# default credentials at https://52.42.105.71/

## Metadata

- HackerOne Report ID: 2160178
- Weakness: Improper Authentication - Generic
- Program: trellix
- Disclosed At: 2024-02-01T16:13:20.093Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

hi team i able to login in one of your servers by default credentials

## Steps to reproduce:
1.go to link : https://52.42.105.71/
1.enter this credentials
```
password=admin
username=admin
```

## PoC

{F2703747}

{F2703748}

## How to remediate the vulnerability

Change the password of the user or disable the account

## Impact

the website was misconfigured in a manner that may have allowed a malicious user to login with administrator for the default organization account credentials.

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
