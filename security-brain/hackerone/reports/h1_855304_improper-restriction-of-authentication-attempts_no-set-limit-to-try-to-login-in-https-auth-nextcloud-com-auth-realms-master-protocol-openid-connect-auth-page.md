---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '855304'
original_report_id: '855304'
title: No set limit to try to login in "https://auth.nextcloud.com/auth/realms/master/protocol/openid-connect/auth"
  page.
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2020-04-21T15:44:49.177Z'
disclosed_at: '2021-04-20T13:50:20.712Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: auth.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# No set limit to try to login in "https://auth.nextcloud.com/auth/realms/master/protocol/openid-connect/auth" page.

## Metadata

- HackerOne Report ID: 855304
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2021-04-20T13:50:20.712Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi.
I checked the "https://nextcloud.com" page, and try to go to wp-admin page.
Then, I found the login page "https://auth.nextcloud.com/auth/realms/master/protocol/openid-connect/auth"
In this page, I tried to login more than 10 times!(manually)
I think that I can try to brute force to this login page, because it's no limit to try to login.
You should be better to set the limit to try to login.

## Impact

an attacker can try to brute force attack to login the page until he can success to login.

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
