---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1188188'
original_report_id: '1188188'
title: A password in plain text in conf file
weakness: Password in Configuration File
team_handle: sifchain
created_at: '2021-05-07T19:01:12.763Z'
disclosed_at: '2021-05-07T20:33:50.090Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- password-in-configuration-file
---

# A password in plain text in conf file

## Metadata

- HackerOne Report ID: 1188188
- Weakness: Password in Configuration File
- Program: sifchain
- Disclosed At: 2021-05-07T20:33:50.090Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

I found a password in plain text in \sifnode-develop\ui\e2e\config.js in the source code. 
password: "coolguy21"

## Impact

I don't know actually how does this affects but passwords in plaintexts are always dangerous.

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
