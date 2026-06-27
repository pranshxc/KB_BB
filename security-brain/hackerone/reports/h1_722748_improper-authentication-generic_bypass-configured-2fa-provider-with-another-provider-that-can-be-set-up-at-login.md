---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '722748'
original_report_id: '722748'
title: Bypass configured 2FA provider with another provider that can be set up at
  login
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2019-10-25T12:14:03.111Z'
disclosed_at: '2020-03-01T12:41:32.802Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Bypass configured 2FA provider with another provider that can be set up at login

## Metadata

- HackerOne Report ID: 722748
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2020-03-01T12:41:32.802Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In Nextcloud 17 there is the possibility to set up 2FA providers at login. A missing check allows the following steps

1) Enforce 2FA for all users
2) As a user, configure a 2FA provider (via settings or at login)
3) Log out
4) Log in again (password only)
5) When prompted with the earlier set up provider, go to /login/setupchallenge
6) Set up another provider that hasn't been set up before
7) You're logged in

## Impact

Bypass a user's second-factor authentication protection.

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
