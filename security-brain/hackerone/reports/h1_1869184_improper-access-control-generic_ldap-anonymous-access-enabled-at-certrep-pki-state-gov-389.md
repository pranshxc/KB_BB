---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1869184'
original_report_id: '1869184'
title: LDAP anonymous access enabled at certrep.pki.state.gov:389
weakness: Improper Access Control - Generic
team_handle: us-department-of-state
created_at: '2023-02-09T22:50:24.405Z'
disclosed_at: '2023-05-11T21:04:38.541Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.STATE.GOV'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# LDAP anonymous access enabled at certrep.pki.state.gov:389

## Metadata

- HackerOne Report ID: 1869184
- Weakness: Improper Access Control - Generic
- Program: us-department-of-state
- Disclosed At: 2023-05-11T21:04:38.541Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi us-department-of-state Security Team.

I have found that this subdomain certrep.pki.state.gov Is vulnerable LDAP Anonymous access enabled as you can see in the following screenshots:-

██████████

███████

████████

## Steps To Reproduce:
1. Run nmap -n -Pn --script "ldap* and not brute" certrep.pki.state.gov
2. You can use ldapadmin tool as showing above at screenshots.

## Supporting Material/References:
- https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap
- https://hackerone.com/reports/205908

Please let me know if need more info.
Best Regards.
@doosec101

## Impact

Improper access to LDAP with anonymous login.

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
