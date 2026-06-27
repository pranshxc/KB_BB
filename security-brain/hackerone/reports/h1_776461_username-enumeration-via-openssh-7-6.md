---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '776461'
original_report_id: '776461'
title: Username enumeration via Openssh 7.6
team_handle: kubernetes
created_at: '2020-01-16T15:04:02.098Z'
disclosed_at: '2020-02-04T01:59:32.669Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 12
asset_identifier: prow.k8s.io
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Username enumeration via Openssh 7.6

## Metadata

- HackerOne Report ID: 776461
- Weakness: 
- Program: kubernetes
- Disclosed At: 2020-02-04T01:59:32.669Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Username enumeration
I have found a vulnerability in your site that  allows me to verify if an user exits in the ssh due to the use of OpenSSH 7.6p1.

PoC
1  Download and compile the given exploit file
2  open a terminal and run the exploit
I have attached a Screenshot if  detailed PoC is needed please inform me.

## Impact

The attacker can get a list of users available in the ssh.

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
