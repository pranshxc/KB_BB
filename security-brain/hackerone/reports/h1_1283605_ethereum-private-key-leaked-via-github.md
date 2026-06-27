---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1283605'
original_report_id: '1283605'
title: ETHEREUM_PRIVATE_KEY leaked via github
team_handle: sifchain
created_at: '2021-07-29T18:01:30.879Z'
disclosed_at: '2021-12-09T17:46:20.458Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# ETHEREUM_PRIVATE_KEY leaked via github

## Metadata

- HackerOne Report ID: 1283605
- Weakness: 
- Program: sifchain
- Disclosed At: 2021-12-09T17:46:20.458Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

ETHEREUM_PRIVATE_KEY 

It is used to sign Ethereum transactions on the Blockchain.

## Steps To Reproduce:
Open this url
https://github.com/Sifchain/sifnode/blob/f96727748e1f44926d3bd72b1021f6c2461dee17/test/integration/start-integration-env.sh



  * POC - screenshot attached

## Impact

It shouldn’t be publicly shared because whoever owns the Private keys can access the funds for that address.
-Private keys are used to create Public addresses using SHA256 hash function.

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
