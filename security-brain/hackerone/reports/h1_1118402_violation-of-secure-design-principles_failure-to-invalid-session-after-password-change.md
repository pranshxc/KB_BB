---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1118402'
original_report_id: '1118402'
title: Failure to Invalid Session after Password Change
weakness: Violation of Secure Design Principles
team_handle: liberapay
created_at: '2021-03-05T18:13:47.292Z'
disclosed_at: '2021-03-12T11:10:52.691Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Failure to Invalid Session after Password Change

## Metadata

- HackerOne Report ID: 1118402
- Weakness: Violation of Secure Design Principles
- Program: liberapay
- Disclosed At: 2021-03-12T11:10:52.691Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary
While conducting my researching I discovered that the application Failure to invalidate session after password. In this scenario changing the password doesn't destroys the other sessions which are logged in with old passwords.

##Reproduction Steps
->Login with the same account in Chrome and Firefox Simultaneously
->Change the pass in Chrome Browser
->Go to firefox and Update any information, information will be update *If attacker login with firefox and user know his password stolen so even user change their password, his account remain insecure and attacker have full access of victim account.

## Impact

If attacker have user password and logged in different places, As other sessions is not destroyed, attacker will be still logged in your account even after changing password, cause his session is still active.. Malicious actor can complete access your account till that session expires! So, your account remains insecure even after the changing of password

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
