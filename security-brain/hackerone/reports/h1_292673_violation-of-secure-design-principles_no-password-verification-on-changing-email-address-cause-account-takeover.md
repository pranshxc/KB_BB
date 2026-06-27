---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '292673'
original_report_id: '292673'
title: No Password Verification on  Changing Email Address Cause Account takeover
weakness: Violation of Secure Design Principles
team_handle: coursera
created_at: '2017-11-23T19:15:27.613Z'
disclosed_at: '2018-05-19T12:42:08.859Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: www.coursera.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# No Password Verification on  Changing Email Address Cause Account takeover

## Metadata

- HackerOne Report ID: 292673
- Weakness: Violation of Secure Design Principles
- Program: coursera
- Disclosed At: 2018-05-19T12:42:08.859Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In coursera.org website, there is no password verification on changing email id. 

Generally when user try to change the password , they were asked to verify the request by entering old password. For the same reason a verification should be there on changing email.

But the worst part is, when user change email address then coursera.org website send verification mail on new mail id without asking current password or inform to old email id.

## Impact

if some one left his account open on public computer(say office or cafe), then attacker can change the email ,verify it himself. Then abuse forgot password field to take over whole account.

Suggested mitigation: 
a password field can be applied (just like Facebook do) or verification mail should be send on old email id registered.


If you required any POC then Let me know. 

Thanks

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
