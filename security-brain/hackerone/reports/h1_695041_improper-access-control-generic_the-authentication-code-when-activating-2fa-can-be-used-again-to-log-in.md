---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '695041'
original_report_id: '695041'
title: The authentication code when activating 2FA can be used again to log in
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2019-09-15T03:02:44.866Z'
disclosed_at: '2021-02-11T19:06:02.695Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: accounts.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# The authentication code when activating 2FA can be used again to log in

## Metadata

- HackerOne Report ID: 695041
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2021-02-11T19:06:02.695Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
Summary:
======================
I noticed that when activating 2FA by sms, you can also use that 2FA activation code, to use as an authentication code when logging in.
Steps:
=========================
1, Go to: https://accounts.shopify.com/accounts/36430415/security and log in
2, Activate 2FA by sms for the account and save the code sent in your phone
3, Log out and perform login again
4, After entering the password and being asked to enter the verification code, you only need to replay the code used to activate the previous 2FA.
5, Logged in successfully.

## Impact

Assuming the hacker knows the authentication code when activating the victim's 2FA, he can reuse the victim's code to replay and log in successfully without the victim knowing.

Recommend:
============
Each authentication code should only be used once.

Best regards,
john

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
