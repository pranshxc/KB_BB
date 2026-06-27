---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '986459'
original_report_id: '986459'
title: Recently change email but still login with old email
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2020-09-20T07:25:16.600Z'
disclosed_at: '2020-09-29T07:46:12.394Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Recently change email but still login with old email

## Metadata

- HackerOne Report ID: 986459
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2020-09-29T07:46:12.394Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi team, 
I have been found vulnerability on email verification which can be account takeover (Authentication bypass)
Recently I have been change my email ████ but still login with old email ██████
--https://efss.qloud.my/index.php/settings/user

## Impact

Impact
If victim's email account is still logged into his/her old gmail account . Then any external attacker can use the unused same email for account takeover
https://efss.qloud.my/index.php/settings/user

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
