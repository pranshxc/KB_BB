---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2078527'
original_report_id: '2078527'
title: Bypassing Garbage Collection with Uppercase Endpoint
team_handle: indrive
created_at: '2023-07-21T01:25:09.109Z'
disclosed_at: '2023-10-04T10:37:25.533Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
asset_identifier: injob.indriver.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Bypassing Garbage Collection with Uppercase Endpoint

## Metadata

- HackerOne Report ID: 2078527
- Weakness: 
- Program: indrive
- Disclosed At: 2023-10-04T10:37:25.533Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
This report highlights a vulnerability in the garbage collection process, where the endpoint "/metrics" can be bypassed by using uppercase letters.
Additionally, it is important to note that if your system contains similar endpoints, they might also be susceptible to the same bypass method. This report aims to provide comprehensive information about the vulnerability and its potential impact.

##  Steps To Reproduce:
1. Make an HTTP request to the URL: https://injob.indriver.com/api/metrics
- ```curl -X GET "https://injob.indriver.com/api/metrics" -H "Content-Type: application/json"```
- Observe the response, which is expected to be "forbidden" (HTTP 403).
- {F2523755}

2.Make another HTTP request to the URL: https://injob.indriver.com/api/METRICS
- ```curl -X GET "https://injob.indriver.com/api/METRICS" -H "Content-Type: application/json"```

- Observe the response, which is expected to be "success" (HTTP 200).
- {F2523756}

## Impact

The impact of this vulnerability includes unauthorized access to sensitive information or resources, potential data manipulation, and a potential risk of further escalation in the system. Furthermore, if other endpoints with similar patterns exist in your system, they might also be vulnerable to the same bypass method, exposing the system to additional security risks.

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
