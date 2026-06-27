---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '709378'
original_report_id: '709378'
title: Session is not expire after logout
weakness: Improper Authentication - Generic
team_handle: owox
created_at: '2019-10-08T05:43:52.672Z'
disclosed_at: '2019-11-08T13:12:23.420Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- improper-authentication-generic
---

# Session is not expire after logout

## Metadata

- HackerOne Report ID: 709378
- Weakness: Improper Authentication - Generic
- Program: owox
- Disclosed At: 2019-11-08T13:12:23.420Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Reproduction:

step no 1:Open URL:https://www.owox.com/products/ or open your user account 

step no 2: copy URL or paste another tab

step no 3:Go back again first tab or logout your account

step no 4: And check the copied URL section is working properly 

Reference From :#244875
Reference From :#263873
Reference From :#249798

Hope you fix this soon ;)

Best Regards,
SAQIB_ARIF

## Impact

An attacker can get the user's session cookies by using Session Spoofer, Cookie Staler, etc. and thus, can get access to the user account.

Perform action:
Changes profile
Delete account

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
