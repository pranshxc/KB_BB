---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '918381'
original_report_id: '918381'
title: Failure to Invalid Session after Password Change
team_handle: rockset
created_at: '2020-08-13T11:57:28.837Z'
disclosed_at: '2021-11-09T21:14:24.945Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 0
asset_identifier: console.rockset.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Failure to Invalid Session after Password Change

## Metadata

- HackerOne Report ID: 918381
- Weakness: 
- Program: rockset
- Disclosed At: 2021-11-09T21:14:24.945Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary:
While conducting my researching I discovered that the application Failure to invalidate session after password. In this scenario changing the password doesn't destroys the other sessions which are logged in with old passwords.

## Steps To Reproduce:


  1. Login with the same account in Chrome and Firefox Simultaneously
  2. Change the pass in Chrome Browser
  3. Go to firefox and Update any information (example:if you are a admin you can delete user from users), information will be update *If attacker login with firefox and user know his password stolen so even user change their password, his account remain insecure and attacker have full access of victim account.



Mitigation

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
