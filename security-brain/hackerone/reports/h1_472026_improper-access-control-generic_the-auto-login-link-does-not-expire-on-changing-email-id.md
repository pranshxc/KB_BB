---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '472026'
original_report_id: '472026'
title: The auto login link does not expire on changing email id
weakness: Improper Access Control - Generic
team_handle: chaturbate
created_at: '2018-12-26T04:19:02.276Z'
disclosed_at: '2019-05-16T17:51:34.353Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# The auto login link does not expire on changing email id

## Metadata

- HackerOne Report ID: 472026
- Weakness: Improper Access Control - Generic
- Program: chaturbate
- Disclosed At: 2019-05-16T17:51:34.353Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The auto login link does not expire on changing email and can be reused to login into user account
Eg link : https://chaturbate.com/accounts/autologin/?█████

Attack Scenario:
1: Users email id has been compromised so now user changes emall id & password of account
2:but attacker can login into user account just by using the auto login link as it do not expire on changing email id & password

Steps To Reproduce
1: Change email id and confirm new email
2:now try opening login link
3' you would be logged in into user account

Fix:; Link should expire once used or have some time limit

## Impact

Account takeover

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
