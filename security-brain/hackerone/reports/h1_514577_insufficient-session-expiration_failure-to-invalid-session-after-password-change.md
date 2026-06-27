---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '514577'
original_report_id: '514577'
title: Failure to Invalid Session after Password Change
weakness: Insufficient Session Expiration
team_handle: omise
created_at: '2019-03-24T17:48:05.458Z'
disclosed_at: '2019-12-08T17:43:41.548Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: www.omise.co
asset_type: URL
max_severity: high
tags:
- hackerone
- insufficient-session-expiration
---

# Failure to Invalid Session after Password Change

## Metadata

- HackerOne Report ID: 514577
- Weakness: Insufficient Session Expiration
- Program: omise
- Disclosed At: 2019-12-08T17:43:41.548Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

While conducting my researching I discovered that the application Failure to invalidate session after password.  In this scenario changing the password doesn't destroys the other sessions which are logged in with old passwords.

Steps to Reproduce:
----------------------
>Video PoC attached

###Step By Step:
->Login with the same account in Chrome and Firefox Simultaneously
->Change the pass in Chrome Browser
->Go to firefox and Update any information, information will be update *If attacker login with firefox and user know his password stolen so even user change their password, his account remain insecure and attacker have full access of victim account.

###Mitigation
When some change in user password, each and every active sessions that belongs to that particular account must be destroyed!
I would like to recommend you to add a process that asks users whether user want to close all open sessions or not right after changing password.

So there is two way, either you let users to choose if they want to keep active sessions or just destroy every active sessions when an users change his/her password!

Please fix this Vulnerability and let me know. Looking forward to hear from you.

Best Regards

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
