---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1195423'
original_report_id: '1195423'
title: Information Disclosure at one of your subdomain
weakness: Information Disclosure
team_handle: sifchain
created_at: '2021-05-13T09:51:50.149Z'
disclosed_at: '2021-12-09T17:52:38.121Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 0
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information Disclosure at one of your subdomain

## Metadata

- HackerOne Report ID: 1195423
- Weakness: Information Disclosure
- Program: sifchain
- Disclosed At: 2021-12-09T17:52:38.121Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Dear Team,

Hope you are doing very well and safe.
I was looking into your application and i find some bugs on your application which is disclosing internal port and also the ips.

That can leads an attacker to do lots of serious attacks.

Please verify:-
https://rpc.sifchain.finance/
https://rpc-testnet.sifchain.finance/
https://rpc.sifchain.finance/net_info?
https://rpc-testnet.sifchain.finance/net_info?

## Impact

1. Critical information disclosure leads an attacker to do direct attack on your services and origin ip.

Thanks & Regards
Ome

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
