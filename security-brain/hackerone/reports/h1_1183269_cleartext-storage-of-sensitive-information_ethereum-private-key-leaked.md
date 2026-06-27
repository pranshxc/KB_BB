---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1183269'
original_report_id: '1183269'
title: ETHEREUM_PRIVATE_KEY leaked
weakness: Cleartext Storage of Sensitive Information
team_handle: sifchain
created_at: '2021-05-03T20:09:07.319Z'
disclosed_at: '2021-05-07T16:04:28.047Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# ETHEREUM_PRIVATE_KEY leaked

## Metadata

- HackerOne Report ID: 1183269
- Weakness: Cleartext Storage of Sensitive Information
- Program: sifchain
- Disclosed At: 2021-05-07T16:04:28.047Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
I found  below private key for ethereum wallet leaked via public code in github repository  
```
ETHEREUM_PRIVATE_KEY="c87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3"
```
## Steps To Reproduce:
You can find private key via below link :
>https://github.com/Sifchain/sifnode/blob/5d222e51f10665322ddb5301a4eb54df37974310/smart-contracts/Deployment.md

## Impact :
This private key for ethereum wallet  allow to someone to send Ether from the address to another address  .

I didn't try anything with this key to avoid violation policy  of program .

## Impact

ETHEREUM_PRIVATE_KEY leaked

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
