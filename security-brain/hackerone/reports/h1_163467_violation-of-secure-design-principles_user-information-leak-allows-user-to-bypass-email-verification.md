---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163467'
original_report_id: '163467'
title: User Information leak allows user to bypass email verification.
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2016-08-26T02:48:11.338Z'
disclosed_at: '2016-09-12T18:47:08.559Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- violation-of-secure-design-principles
---

# User Information leak allows user to bypass email verification.

## Metadata

- HackerOne Report ID: 163467
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2016-09-12T18:47:08.559Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When a user is logged on, the following is sent:

```
██████
```

This contains some sensitive information, most notably the email token. A user can use this to bypass email verification and verify any email.

In addition, the hashed password is leaked, which could present a vulnerability if a user's account is compromised without compromising the password.

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
