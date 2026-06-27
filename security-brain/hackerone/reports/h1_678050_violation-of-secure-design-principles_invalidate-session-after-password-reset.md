---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '678050'
original_report_id: '678050'
title: Invalidate session after password reset
weakness: Violation of Secure Design Principles
team_handle: liberapay
created_at: '2019-08-21T04:31:06.982Z'
disclosed_at: '2019-11-05T08:37:11.687Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Invalidate session after password reset

## Metadata

- HackerOne Report ID: 678050
- Weakness: Violation of Secure Design Principles
- Program: liberapay
- Disclosed At: 2019-11-05T08:37:11.687Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Website doesn't invalidate session after the password is reset which can enable attacker to continue using the compromised session.

Steps:
1) Open same accounts in two different browsers
2) Change password in one browser and you will see that another browser still validate the session after password change (even after refresh the page ).

Recommendation:

As per OWASP, it is recommended to terminate all the active sessions when a password is changed and force the user to re-login.

## Impact

Logging in with the new password doesn't invalidate the older session either: I could browse Liberapay using two sessions (in two different browsers) which were initiated using two different passwords.

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
