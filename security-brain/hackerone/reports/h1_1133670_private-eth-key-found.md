---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1133670'
original_report_id: '1133670'
title: Private eth key found
team_handle: sifchain
created_at: '2021-04-30T14:03:21.540Z'
disclosed_at: '2021-06-10T15:00:17.485Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Private eth key found

## Metadata

- HackerOne Report ID: 1133670
- Weakness: 
- Program: sifchain
- Disclosed At: 2021-06-10T15:00:17.485Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hello, team! 

Found private ethereum key at file: 
https://github.com/Sifchain/sifnode/blob/develop/smart-contracts/.env.example 

This key points to wallet balance: 
{F1284232}

As I understood, private key allows to spend this coins, so it may need to be masked or hidden.

## Impact

eth private key disclosure

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
