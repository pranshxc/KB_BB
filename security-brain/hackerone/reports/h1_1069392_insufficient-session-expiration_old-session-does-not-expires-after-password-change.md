---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1069392'
original_report_id: '1069392'
title: Old Session Does Not Expires After Password Change
weakness: Insufficient Session Expiration
team_handle: deptofdefense
created_at: '2020-12-31T18:51:17.719Z'
disclosed_at: '2021-01-25T19:58:42.331Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- insufficient-session-expiration
---

# Old Session Does Not Expires After Password Change

## Metadata

- HackerOne Report ID: 1069392
- Weakness: Insufficient Session Expiration
- Program: deptofdefense
- Disclosed At: 2021-01-25T19:58:42.331Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Hello Team,
I am Hemant Patidar working as a security researcher and I found a bug in your site.
Report of bug is as follows:-

##Description:
While conducting my research I discovered that the application Failure to invalidate the session after the password change. In this scenario changing the password doesn't destroy the other sessions which are logged in with old passwords.

##Steps to reproduce:
1. Login with the same account in Chrome and Firefox Simultaneously using the URL: https://█████
2. Change the pass in Chrome Browser using the URL: https://██████
3. Go to firefox and Update any information, the information will be updated 

##POC:
███████

##Mitigation
When some change in user password, each and every active session that belongs to that particular account must be destroyed!
I would like to recommend you to add a process that asks users whether user want to close all open sessions or not right after changing password.
So there is two way, either you let users choose if they want to keep active sessions or just destroy every active session when users change his/her password!

## Impact

* If the attacker has a user password and logged in different places, As other sessions are not destroyed, the attacker will be still logged in to your account even after changing the password, cause his session is still active. A malicious actor can complete access your account till that session expires! So, your account remains insecure even after the changing of password

Please fix this Vulnerability and let me know. Looking forward to hearing from you.

Best Regards
Hemant Patidar

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
