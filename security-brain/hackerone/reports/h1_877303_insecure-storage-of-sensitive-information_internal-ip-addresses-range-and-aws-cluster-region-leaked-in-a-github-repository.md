---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '877303'
original_report_id: '877303'
title: Internal IP addresses range and AWS cluster region leaked in a Github repository
weakness: Insecure Storage of Sensitive Information
team_handle: kubernetes
created_at: '2020-05-18T17:25:09.627Z'
disclosed_at: '2020-07-24T00:43:28.230Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: https://github.com/kubernetes/kubernetes
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Internal IP addresses range and AWS cluster region leaked in a Github repository

## Metadata

- HackerOne Report ID: 877303
- Weakness: Insecure Storage of Sensitive Information
- Program: kubernetes
- Disclosed At: 2020-07-24T00:43:28.230Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Report Submission Form

## Summary:
I was exploring the GitHub repository and found some internal IP address and its cluster region related to AWS cluster. So i decided to report it to you. Please have a look and let me know.

## Steps To Reproduce:
VISIT THIS LINK : 
Repository - kubernetes / kubernetes 
File Link - https://github.com/kubernetes/kubernetes/blob/d4d02a9028337e41b4f7a76e4e7de50067e8529e/cluster/aws/config-default.sh


## Supporting Material/References:
Reference:
https://hackerone.com/reports/329791
https://hackerone.com/reports/271700
https://hackerone.com/reports/310036

## Impact

1. These IPs are related to AWS cloud, if someone get enter in the Vnet can also exploit machine on the machines already known.
2. Gives the idea of the organization of internal network. 
3. Revealing the AWS cluster region can also narrow down the search of any hacker and make their work easy
4. This will allow attackers to gain access to an internal IP of a DOD website along with other sensitive information that may be leaked with the request

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
