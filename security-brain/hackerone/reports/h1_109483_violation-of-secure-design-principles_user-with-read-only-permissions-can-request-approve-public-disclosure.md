---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '109483'
original_report_id: '109483'
title: User with Read-Only permissions can request/approve public disclosure
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-01-09T03:03:35.455Z'
disclosed_at: '2016-02-19T11:11:36.502Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# User with Read-Only permissions can request/approve public disclosure

## Metadata

- HackerOne Report ID: 109483
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-02-19T11:11:36.502Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found out that a user who belongs to a group with Read-Only permission can still request and approuve public disclosure when the report is closed by privileged admin although that these permissions are only allowed if the user group has **Report** scope.

Consequently, the team member with limited scope can also post public comment through public dislosure request and that contradicts what was expected.

**Proof Of Concept :**
1. Create a new user group with Read-Only permission
2. Add a user to the group.
3. Log in with that user account and browse a Closed report, you should now be able to request public disclosure.

Kind regards.
Yassine ABOUKIR

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
