---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1202590'
original_report_id: '1202590'
title: Webauthn tokens are not removed on user deletion
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2021-05-19T12:07:33.341Z'
disclosed_at: '2021-08-07T14:28:53.107Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Webauthn tokens are not removed on user deletion

## Metadata

- HackerOne Report ID: 1202590
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2021-08-07T14:28:53.107Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. userA has an account on serverA
2. userA enables passwordless login (webauthn) and registers a key/device
3. userA is removed from the system
4. a new user comes along and gets assigned userA as id
5. the old userA tries to login with their key
6. the old userA can see all data of the new userA

## Impact

This can lead to an unauthorized actor gaining full access to the data of another user.
As suggested in https://hackerone.com/reports/1200700 a blocklist of old userids would help here. However the data should all be cleaned up as well of course!

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
