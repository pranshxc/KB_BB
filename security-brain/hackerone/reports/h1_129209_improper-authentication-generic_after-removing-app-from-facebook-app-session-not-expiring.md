---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '129209'
original_report_id: '129209'
title: After removing app from facebook app session not expiring.
weakness: Improper Authentication - Generic
team_handle: gratipay
created_at: '2016-04-08T09:52:59.847Z'
disclosed_at: '2017-08-21T13:33:08.401Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# After removing app from facebook app session not expiring.

## Metadata

- HackerOne Report ID: 129209
- Weakness: Improper Authentication - Generic
- Program: gratipay
- Disclosed At: 2017-08-21T13:33:08.401Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

When a user login with facebook 0Auth and then he removes the app from facebook app setting the session is not expiring.
Poc:-

Step1: Go to gratipay login page.
Step2: Click on login with facebook 0 auth and login with facebook.
Step3: Go to facebook then app setting.
Step4: Now remove the gratipay app from here and go back to gratipay site.
Step5: You will see that you are still logged in.

Hence session is not expiring so it is vulnerable.

Thanks
Sushil Saini (Cyber Security Researcher)

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
