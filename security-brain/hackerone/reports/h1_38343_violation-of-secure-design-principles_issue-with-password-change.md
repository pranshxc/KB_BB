---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38343'
original_report_id: '38343'
title: Issue with password change
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-12-05T17:10:05.265Z'
disclosed_at: '2015-05-28T04:44:05.518Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Issue with password change

## Metadata

- HackerOne Report ID: 38343
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-05-28T04:44:05.518Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When a password is changed in user's profile, then a notification about password change is sent to the user (email). This is good. 

However, user not always gets a notification about password change - when a password is changed via password reset link, then such a notification is not send to the user.

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
