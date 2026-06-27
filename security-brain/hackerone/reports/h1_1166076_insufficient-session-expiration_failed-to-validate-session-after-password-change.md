---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166076'
original_report_id: '1166076'
title: Failed to validate Session after Password Change
weakness: Insufficient Session Expiration
team_handle: upchieve
created_at: '2021-08-08T17:40:48.686Z'
disclosed_at: '2021-08-31T09:15:19.967Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 7
asset_identifier: hackers.upchieve.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- insufficient-session-expiration
---

# Failed to validate Session after Password Change

## Metadata

- HackerOne Report ID: 1166076
- Weakness: Insufficient Session Expiration
- Program: upchieve
- Disclosed At: 2021-08-31T09:15:19.967Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

While conducting my research I discovered that the application Failed to validate session after password change.  In this scenario changing the password doesn't destroys the other sessions which are logged in with old passwords in another browser.

## Steps To Reproduce:

1) Login with the same account in Chrome and Firefox Simultaneously
2) Change the pass in Chrome Browser
3) Go to firefox and Update any information, information will be update.
--------> If attacker login with firefox and user know his password stolen so even user change their password, his account remain insecure and attacker have full access of victim account.

## Mitigation

When some change in user password, each and every active sessions that belongs to that particular account must be destroyed!
I would like to recommend you to add a process that asks users whether user want to close all open sessions or not right after changing password.
So there is two way, either you let users to choose if they want to keep active sessions or just destroy every active sessions when an users change his/her password!

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
