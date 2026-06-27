---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '874924'
original_report_id: '874924'
title: RCE (Remote code execution) in one of DoD's websites
weakness: Cryptographic Issues - Generic
team_handle: deptofdefense
created_at: '2020-05-15T10:01:24.258Z'
disclosed_at: '2020-07-30T17:47:50.131Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cryptographic-issues-generic
---

# RCE (Remote code execution) in one of DoD's websites

## Metadata

- HackerOne Report ID: 874924
- Weakness: Cryptographic Issues - Generic
- Program: deptofdefense
- Disclosed At: 2020-07-30T17:47:50.131Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The targeted website is vulnerable to CVE-2017-1000486, by only running command was (whoami) to prove that the RCE exist has been run successfully on the target
**Description:**
The target uses a vulnerable version of primefaces : Primetek Primefaces 5.x, that is vulnerable to a weak encryption flaw resulting in remote code execution
## Impact
Critical
## Step-by-step Reproduction Instructions
Using the following exploit : https://github.com/pimps/CVE-2017-1000486
1. python primefaces.py████████/

## Product, Version, and Configuration (If applicable)
Primefaces 5.3.6
## Suggested Mitigation/Remediation Actions
Primefaces has to be updated to a newer version

## Impact

An attacker could execute remote codes on the target system, that could impact all of the CIA triad

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
