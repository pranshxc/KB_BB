---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1465277'
original_report_id: '1465277'
title: Brute force of a current password on a disable 2fa leads to guess password
  and disable 2fa.
weakness: Improper Restriction of Authentication Attempts
team_handle: omise
created_at: '2022-01-31T06:28:15.308Z'
disclosed_at: '2022-07-07T16:35:19.537Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: dashboard2.omise.co
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Brute force of a current password on a disable 2fa leads to guess password and disable 2fa.

## Metadata

- HackerOne Report ID: 1465277
- Weakness: Improper Restriction of Authentication Attempts
- Program: omise
- Disclosed At: 2022-07-07T16:35:19.537Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Summary:
This Attack happen when victim login in other device and forget to logout ,Then attacker can enable 2-factor authentication by brute fore the password of victim endpoints.

## Steps To Reproduce:
(1)Login in https://dashboard.omise.co/signin
(2) Click on your username
(3)Navigate to Two-factor authentication --> Disable 2FA
(4)add random password in Please confirm your identity to register a new Two-Factor Authenticator
(5)Capture the request and send it for fuzz


POC
In screenshot you can see change in length of content when request encounter right password.

## Impact

Attacker can disable 2fa and brute force currrent password.

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
