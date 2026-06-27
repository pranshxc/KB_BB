---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '803028'
original_report_id: '803028'
title: Monero wallet password change is confirmed when not matching
weakness: Unverified Password Change
team_handle: monero
created_at: '2020-02-24T01:54:23.945Z'
disclosed_at: '2020-03-11T23:13:39.302Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- unverified-password-change
---

# Monero wallet password change is confirmed when not matching

## Metadata

- HackerOne Report ID: 803028
- Weakness: Unverified Password Change
- Program: monero
- Disclosed At: 2020-03-11T23:13:39.302Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
If you change your wallet password in gui, the confirmation does not need to match the new password.

## Releases Affected:

  * [list each version and OS of the application affected]
  * [list each version and OS of the application affected]

## Steps To Reproduce:
Open your wallet.
Go to settings.
Change wallet password.
Enter old password.
You now have prompt with two passwords.
Enter your new password in the first line.
Leaving confirmation blank press enter.
Password is changed successfully without confirmation.

## Supporting Material/References:
I have personally attempted this many times.

## Housekeeping

1. Be sure to read our policy before submitting
2. Provide an XMR address within the report if you wish to receive bounty (assuming that the report is valid)
    - PoC within a report will most likely result in more bounty than not

45vSCZ1DhEQCjXtPHzgr7m1jCkD31J9ZDCmDakuNV1Sw7mo5ywUPxVxXacJwtiBg7zdRQa4qjzy9Lg8NJdNMDdV3QH8xkPe

## Impact

User can lock themselves out of wallet.

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
