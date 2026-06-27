---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1035742'
original_report_id: '1035742'
title: Able to authenticate as administrator by navigating to https://█████/admin/
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2020-11-16T19:20:12.555Z'
disclosed_at: '2021-01-12T21:35:13.552Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Able to authenticate as administrator by navigating to https://█████/admin/

## Metadata

- HackerOne Report ID: 1035742
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2021-01-12T21:35:13.552Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The endpoint at https://███████/admin/ authenticates the user  to the administrator user.

## Step-by-step Reproduction Instructions

1. Navigate to https://███/ and youll notice you will need to log in.
2. Navigating to https://██████████/admin/ will show you admin malformed page, with the ability to "log out"

As for now as we can see by the picture no data is present at the administrator panel, sure this might change at the future exposing sensitive ifnormation

████████


## Suggested Mitigation/Remediation Actions

Issuing 403 response when trying to access the /admin endpoint.

##Best regards
nagli

## Impact

Admin authentication bypass

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
