---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '908880'
original_report_id: '908880'
title: Private IP addresses Disclosure
weakness: Information Disclosure
team_handle: kubernetes
created_at: '2020-06-26T12:31:32.945Z'
disclosed_at: '2020-07-23T17:59:10.593Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: kubernetes.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Private IP addresses Disclosure

## Metadata

- HackerOne Report ID: 908880
- Weakness: Information Disclosure
- Program: kubernetes
- Disclosed At: 2020-07-23T17:59:10.593Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The following URL leaks the Private IP Addresses:- kubernetes.io/feed.xml

The following Server’s Cluster RFC 1918 IP addresses were disclosed in the response: 
•	10.1.2.3 
•	10.104.207.136 
•	10.224.0.0 
•	10.250.0.0 
•	10.250.112.0 
•	10.250.96.0 
•	10.55.252.216 
•	10.96.0.0 
•	10.96.0.1 
•	10.96.15.180 
•	10.97.125.254 
•	10.97.62.68 
•	172.17.0.4 
•	192.168.1.4 
•	192.168.1.7 
•	192.168.99.100


Steps to reproduce:- Simply by opening the above mentioned link we can extract the server's Cluster IP Addresses.

References:- Attached Snaps  
CWE-200: Information Exposure

## Impact

Attackers can use this information to exploit the ip addresses.

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
