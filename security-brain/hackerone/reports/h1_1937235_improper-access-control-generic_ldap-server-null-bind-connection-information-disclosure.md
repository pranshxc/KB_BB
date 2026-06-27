---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1937235'
original_report_id: '1937235'
title: LDAP Server NULL Bind Connection Information Disclosure
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2023-04-06T18:14:09.346Z'
disclosed_at: '2023-05-15T15:07:05.908Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-access-control-generic
---

# LDAP Server NULL Bind Connection Information Disclosure

## Metadata

- HackerOne Report ID: 1937235
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2023-05-15T15:07:05.908Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
The remote LDAP server allows anonymous access

## References
  - https://www.tenable.com/plugins/nessus/10723
  - https://ldap.com/ldapv3-wire-protocol-reference-bind

## Impact

information  disclosure

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. run $ `nmap -n -sV --script "ldap* and not brute" -p 389 ██████████`

check the response
## POC
██████

## Suggested Mitigation/Remediation Actions
Configure the service to disallow NULL BINDs.

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
