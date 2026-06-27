---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1027949'
original_report_id: '1027949'
title: Exposed Configuration Files at https://www.exodus.io/keybase.txt
team_handle: exodus
created_at: '2020-11-06T05:29:11.010Z'
disclosed_at: '2020-11-06T08:21:48.179Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 14
asset_identifier: '*.exodus.io'
asset_type: WILDCARD
max_severity: high
tags:
- hackerone
---

# Exposed Configuration Files at https://www.exodus.io/keybase.txt

## Metadata

- HackerOne Report ID: 1027949
- Weakness: 
- Program: exodus
- Disclosed At: 2020-11-06T08:21:48.179Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Username, uid information is present in txt file.

## Steps To Reproduce:

  1. Open This link https://www.exodus.io/keybase.txt 
  2. Search for username, uid
  3. You will get some usernames with uid.

## Impact

This information may help attacker in further attacks.

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
