---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '287758'
original_report_id: '287758'
title: Bypass insecure password validation
team_handle: infogram
created_at: '2017-11-06T16:00:11.463Z'
disclosed_at: '2017-11-16T08:08:29.922Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Bypass insecure password validation

## Metadata

- HackerOne Report ID: 287758
- Weakness: 
- Program: infogram
- Disclosed At: 2017-11-16T08:08:29.922Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

## Summary:

Registration is checking the password creation __if the password is insecure__ , but the password reset page was not doing the same validation, so when i input an insecure password using the password reset, the validation on the password creation can be bypass because the password reset was not doing the same validation.

## Steps to reproduce:

  1. Try to create/signup an account here: https://infogram.com/signup with password `1234567890` and the error message will appear: `Insecure password`.
  2. Now lets bypass it, assuming i already created an account, now go to forgot password: https://infogram.com/forgot and enter you email.
  3. The password reset link will send, click the link and it will redirect to password reset page.
  4. On password reset, enter `1234567890` as your new password.
  5. Password accepted! , insecure password validation has been bypassed.

Let me know if you need more information.

Regards
Japz

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
