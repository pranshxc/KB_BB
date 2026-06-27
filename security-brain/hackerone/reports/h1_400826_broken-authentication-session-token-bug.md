---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '400826'
original_report_id: '400826'
title: Broken Authentication – Session Token bug
team_handle: weblate
created_at: '2018-08-27T07:37:28.159Z'
disclosed_at: '2018-09-26T09:22:13.897Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: hosted.weblate.org
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Broken Authentication – Session Token bug

## Metadata

- HackerOne Report ID: 400826
- Weakness: 
- Program: weblate
- Disclosed At: 2018-09-26T09:22:13.897Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found a broken authentitication vuln

POC:

1- Create a https://demo.weblate.org/accounts/profile/ account
2- Confirm your email
3- Now request a password reset for your account.
4- Don’t use the password reset link that was sent to your email.
5- Login to your account, remember don’t use first the reset password link you requested in 3 step
6- Change your password in the Account Settings( url: https://demo.weblate.org/accounts/profile/
Step 5. After you changed your password inside your account, Check now the reset password link you requested in Step 3 in your email.
Step 6. Change your password using the reset password link you requested.


See this link: https://www.owasp.org/index.php/Broken_Authentication_and_Session_Management

## Impact

tokken should expire 


If the site has a token issue, The result is the reset password token in the Step 3 is still usable and did not expire yet. Not invalidating the session token for the reset password is not a good practice for a company.

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
