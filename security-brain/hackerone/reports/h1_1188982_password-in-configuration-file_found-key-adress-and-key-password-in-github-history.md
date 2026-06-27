---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1188982'
original_report_id: '1188982'
title: Found key_adress and key_password in GitHub history
weakness: Password in Configuration File
team_handle: sifchain
created_at: '2021-05-08T12:09:21.166Z'
disclosed_at: '2021-05-08T17:24:10.086Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- password-in-configuration-file
---

# Found key_adress and key_password in GitHub history

## Metadata

- HackerOne Report ID: 1188982
- Weakness: Password in Configuration File
- Program: sifchain
- Disclosed At: 2021-05-08T17:24:10.086Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
I found in your GitHub history key_adress and key_passwords

## Steps To Reproduce:
  1. Open url https://github.com/Sifchain/sifnode/commit/f21dcf05c7953693b82bba119bba5ca48982b6d0#diff-3b3ced8ca40f67dd52fd8031d9c2b5147c249a8c66b3aa066e355c0ee12fa14c
  2. search for "key_password" and you will find 2 key_password's

## Supporting Material/References:
  * see screenshot: F1293770

## Impact

An attacker can maybe use these information if they are still valid.

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
