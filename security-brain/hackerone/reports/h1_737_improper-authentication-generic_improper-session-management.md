---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '737'
original_report_id: '737'
title: Improper session management
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2014-01-16T23:48:19.888Z'
disclosed_at: '2014-02-19T23:57:04.759Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- improper-authentication-generic
---

# Improper session management

## Metadata

- HackerOne Report ID: 737
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2014-02-19T23:57:04.759Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When a request with an invalid authenticity_token is received, the user is logged out (tested for updating user's profile, which is available here: https://hackerone.com/diekatze/profile/edit) and the user receives a new session cookie, which is not authenticated at this point. However, the authenticated session cookie used by a user before logging out is still active.

Regards,
Dawid Czagan

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
