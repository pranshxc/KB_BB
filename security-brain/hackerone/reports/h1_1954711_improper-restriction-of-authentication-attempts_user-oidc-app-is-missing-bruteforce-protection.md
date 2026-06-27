---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1954711'
original_report_id: '1954711'
title: user_oidc app is missing bruteforce protection
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2023-04-19T14:53:04.250Z'
disclosed_at: '2023-06-23T09:44:42.159Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: nextcloud/user_oidc
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# user_oidc app is missing bruteforce protection

## Metadata

- HackerOne Report ID: 1954711
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2023-06-23T09:44:42.159Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Various controllers of the user_oidc app are not bruteforce protected, allowing attackers to iterate over data until they find valid one.

* Id4meController::login
* Id4meController::code
* LoginController::login
* LoginController::code
* LoginController::csingleLogoutService
* LoginController::cbackChannelLogout

## Impact

Authentication can be broken/bypassed

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
