---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1947376'
original_report_id: '1947376'
title: IDOR  ' can delete any animal from other account  '  at https://www.miroyalcanin.cl/
weakness: Insecure Direct Object Reference (IDOR)
team_handle: mars
created_at: '2023-04-14T15:23:41.011Z'
disclosed_at: '2023-06-23T14:59:57.194Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: '*.miroyalcanin.cl'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR  ' can delete any animal from other account  '  at https://www.miroyalcanin.cl/

## Metadata

- HackerOne Report ID: 1947376
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: mars
- Disclosed At: 2023-06-23T14:59:57.194Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi team
i found IDOR , i can delete any animal from other account easily

1.  Go to registration page (https://www.miroyalcanin.cl/)
2.  Verified your account.
3.  Go to login page and login your account.

For the fastly test, use this credentials to login (my test account)

 * For Attacker

email: wageba9443@snowlash.com
pass: Password

 * For Victim

email: jejab86205@fitzola.com
pass: Password

After login i create 2 account for attacker and victim , in the attacker's account, i delete my animal, and i send request to burp .. i change my animal id to victim animal id so i succeeded

{F2293054}

## Impact

IDOR

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
