---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1132690'
original_report_id: '1132690'
title: Exposed Openapi Token
weakness: Cleartext Storage of Sensitive Information
team_handle: sifchain
created_at: '2021-03-23T01:49:36.386Z'
disclosed_at: '2021-05-07T16:00:37.064Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Exposed Openapi Token

## Metadata

- HackerOne Report ID: 1132690
- Weakness: Cleartext Storage of Sensitive Information
- Program: sifchain
- Disclosed At: 2021-05-07T16:00:37.064Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Summary**
While looking for secrets, I noticed that Developers had removed a swagger spec draft. The URL had a committed token in the history of multiple project files:
ui/core/src/api/transactionsService.ts
ui/core/src/api/tendermintService.ts
ui/core/src/api/stakingService.ts
ui/core/src/api/slashingService.ts
ui/core/src/api/sifdistService.ts
ui/core/src/api/bankService.ts
...etc, etc

**Steps To Reproduce**
1. Look at the file history of the the github ui/core/src/api and check for secrets. I will provide exposed file history if requested further.

**Proof**
 https://raw.githubusercontent.com/Sifchain/sifnode/c1bb5a268da8b519d0fc90f81fa194d31c0f82b3/api/openapi/swagger.yml?token=AAJSXWM6CDXYAEETSC6BJ2S7Q2JLS

## Impact

An attacker can utilize the token on the api.sifchain.finance API

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
