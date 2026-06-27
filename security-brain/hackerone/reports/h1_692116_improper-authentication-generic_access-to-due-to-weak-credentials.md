---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '692116'
original_report_id: '692116'
title: Access to ██████████████ due to weak credentials
weakness: Improper Authentication - Generic
team_handle: 8x8
created_at: '2019-09-11T01:26:26.441Z'
disclosed_at: '2020-01-08T20:37:28.809Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
asset_identifier: '*.8x8.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Access to ██████████████ due to weak credentials

## Metadata

- HackerOne Report ID: 692116
- Weakness: Improper Authentication - Generic
- Program: 8x8
- Disclosed At: 2020-01-08T20:37:28.809Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team

**Description:** 
During the analysis, It was found that the `█████████████████████` ask's for credentials from the users to access the ██████, But the weak credentials set `█████:██████` allows anyone to login.

## Steps To Reproduce:

  1. Open █████████████████████████
  1. Enter `█████████` ███████ username and password field.
  1. You now have access to the analytical data. 

## POC
███

## Remediation
Use strong set of password instead of common████generic ones like `████:██████`

## Impact

An attacker can bypass the authentication check and access the internal analytical data.

PS: apart from the analytical data, I wasn't able to find much.

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
