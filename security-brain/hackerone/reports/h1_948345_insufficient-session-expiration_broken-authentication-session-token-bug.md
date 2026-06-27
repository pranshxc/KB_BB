---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '948345'
original_report_id: '948345'
title: Broken Authentication Session Token Bug
weakness: Insufficient Session Expiration
team_handle: trycourier
created_at: '2020-07-31T06:00:12.896Z'
disclosed_at: '2022-02-16T23:43:27.076Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: www.trycourier.app
asset_type: URL
max_severity: critical
tags:
- hackerone
- insufficient-session-expiration
---

# Broken Authentication Session Token Bug

## Metadata

- HackerOne Report ID: 948345
- Weakness: Insufficient Session Expiration
- Program: trycourier
- Disclosed At: 2022-02-16T23:43:27.076Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team 
Hope your are good I have found a broken authentication issue in https://www.trycourier.app

Steps to reproduce 

1. Create a courier account or use existing one.
2. Confirm Your email address.
3. Now log out from your account and request for password reset code for your account .
4. Don't use the code that has been sent to your email address.
5. In new tab or new browser log in back to your account.
6. Go to account setting and change your password .
7. Now go to email and check the password reset code that we requested in step 3.
8. Change Your password using that reset password code .
9. You can see that your password has been changed.

The reset code is not expired after changing the password

## Impact

If the site has a token issue, The result is the reset password token in the Step 3 is still usable and did not expire yet. 
If the victims opens his mail in cybercafe or in attackers device and forgot to log out then attacker can access that system and can reset the password of his account.

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
