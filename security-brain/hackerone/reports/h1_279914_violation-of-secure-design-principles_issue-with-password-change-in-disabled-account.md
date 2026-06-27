---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '279914'
original_report_id: '279914'
title: Issue with password change in Disabled Account
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2017-10-18T16:32:40.515Z'
disclosed_at: '2017-11-16T23:24:17.010Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Issue with password change in Disabled Account

## Metadata

- HackerOne Report ID: 279914
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2017-11-16T23:24:17.010Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Hackerone,

**Summary:**
I have found that #38343 is not yet fully fixed, disabled user is not always gets notification about password change when a password is changed via password reset link, then such a notification is not send to the disabled user.

**Description (Include Impact):**
When a password changed in user's profile `When a password changed in user's profile` or `password reset links` for `enabled/active user` receives a notification via email containing that the password was recently changed. This is the fixed that reported in #38343. 

However, it defeats the fix in #38343 because when a password changed in `password reset links` for `disabled/inactive user` does not receive notification via email containing that password was recently changed.

__POC__ 
https://vimeo.com/214135835
password: protection

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
