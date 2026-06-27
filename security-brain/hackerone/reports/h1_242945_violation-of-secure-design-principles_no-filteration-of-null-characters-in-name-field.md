---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '242945'
original_report_id: '242945'
title: No filteration of null characters in name field
weakness: Violation of Secure Design Principles
team_handle: weblate
created_at: '2017-06-24T22:20:00.883Z'
disclosed_at: '2017-07-27T11:51:03.039Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# No filteration of null characters in name field

## Metadata

- HackerOne Report ID: 242945
- Weakness: Violation of Secure Design Principles
- Program: weblate
- Disclosed At: 2017-07-27T11:51:03.039Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

##Description:
The account settings page, https://demo.weblate.org/accounts/profile/#account, allows a user to set their username as a null character! A user intercepts the request using a proxy and changes the user name field to %00. 

##Mitigation:
I recommend you have filtering of null characters on your account settings page.

Thanks!

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
