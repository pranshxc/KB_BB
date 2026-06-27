---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15785'
original_report_id: '15785'
title: Session not invalidated after password reset
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-06-10T00:12:06.324Z'
disclosed_at: '2014-06-10T01:45:10.430Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- violation-of-secure-design-principles
---

# Session not invalidated after password reset

## Metadata

- HackerOne Report ID: 15785
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2014-06-10T01:45:10.430Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

After a password reset link is requested and a user's password is then changed, not all existing sessions are logged out automatically. The automatic removal of existing sessions linked to a user whose password was changed is only the case if the session was initiated with the 'Remember me for a week' box NOT checked at the log-in page; sessions with the 'remember' option enabled will persist after the password change.

Logging in with the new password doesn't invalidate the older session either: I could browse HackerOne using two sessions (in two different browsers) which were initiated using two different passwords.

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
