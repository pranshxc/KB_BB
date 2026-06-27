---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411364'
original_report_id: '411364'
title: Brute Force of fabric-ca server admin account
weakness: Improper Restriction of Authentication Attempts
team_handle: hyperledger
created_at: '2018-09-19T07:34:01.745Z'
disclosed_at: '2022-08-06T17:36:44.655Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 60
asset_identifier: https://github.com/hyperledger/fabric-ca
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Brute Force of fabric-ca server admin account

## Metadata

- HackerOne Report ID: 411364
- Weakness: Improper Restriction of Authentication Attempts
- Program: hyperledger
- Disclosed At: 2022-08-06T17:36:44.655Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## fabric-ca server
- Default configuration maxenrollments value -1(enable outside enrollment)
- Listening 0.0.0.0:7054(easily discoved and can be reached)
- No limit to wrong password try
Above conditions result in brute force to CA server admin account

## Impact

## Attack gain a high-level permissioned account to permissioned network and can add\delete\update\query

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
