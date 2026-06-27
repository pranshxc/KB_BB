---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '11722'
original_report_id: '11722'
title: 'Simultaneous Session Logon : Improper Session Management'
weakness: Improper Authentication - Generic
team_handle: coinbase
created_at: '2014-05-10T21:23:50.011Z'
disclosed_at: '2014-08-26T06:09:59.286Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Simultaneous Session Logon : Improper Session Management

## Metadata

- HackerOne Report ID: 11722
- Weakness: Improper Authentication - Generic
- Program: coinbase
- Disclosed At: 2014-08-26T06:09:59.286Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
I would like to report this bug related to improper simultaneous logon. 

Issue: 
1) When a user is logged in to the application (already authenticated), visits the login page https://coinbase.com/signin he/she should directly get redirected to their home page as there is already a session running for the same user, but this is not happening in coinbase website. 

2) If one already logged in user visits the login page and enter the credentials to login as a different user, he gets logged in (provided the credentials are correct), but the session of the older user account is still alive this might cause session hijacking.

3) As already logged in users can also visit the login page again and re-authenticate themselves, the activities page shows one more session running for the same account whereas the session identifier is same for all the sessions. 

I have tried showing all the three issues in the POC, please let me know if you need the POC video as i can't upload it here because of some issues. 

Root Cause: I guess for simultaneous session logon you guys are not using the device id parameter, hence same user can reauth himself again and again from the same device. Secondly,. the login page is not checking whether the user already have an active session or not and hence redirecting.

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
