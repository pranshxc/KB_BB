---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15852'
original_report_id: '15852'
title: Non Validation of session after password reset
weakness: Violation of Secure Design Principles
team_handle: mavenlink
created_at: '2014-06-10T15:30:58.282Z'
disclosed_at: '2014-07-22T19:17:17.021Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Non Validation of session after password reset

## Metadata

- HackerOne Report ID: 15852
- Weakness: Violation of Secure Design Principles
- Program: mavenlink
- Disclosed At: 2014-07-22T19:17:17.021Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

After a password reset link is requested and a user's password is then changed, not all existing sessions are logged out automatically. 
Logging in with the new password doesn't invalidate the older session either: I could browse mavenlink using two sessions (in two different browsers) which were initiated using two different passwords.

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
