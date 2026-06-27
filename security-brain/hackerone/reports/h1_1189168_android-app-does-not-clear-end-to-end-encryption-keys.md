---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1189168'
original_report_id: '1189168'
title: Android app does not clear end to end encryption keys
team_handle: nextcloud
created_at: '2021-05-08T19:36:02.461Z'
disclosed_at: '2021-06-16T08:57:38.495Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
---

# Android app does not clear end to end encryption keys

## Metadata

- HackerOne Report ID: 1189168
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-06-16T08:57:38.495Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. userA on serverA sets up end to end encryption on their android device
2. userA has some end to end encrypted data
3. userA removes their account on serverA from their android device (for whatever reason)
4. attacker (evil admin) obtains the device of userA
5. attacker (evil admin) logs in on the account of userA  (reset the pw and just log in)
6. attacker (evil admin) can see and access all encrypted files

## Impact

While I believe the impact is minimal since you need to obtain the device of the victim.
Once you remove your account all information regarding that account should be removed.

* the keys
* the mnemonic

And certainly when you re-add an account you should be asked to enter your mnemonic!

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
