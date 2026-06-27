---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '261297'
original_report_id: '261297'
title: Disabled user can reset their password
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2017-08-18T09:25:33.954Z'
disclosed_at: '2020-03-01T15:01:45.393Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Disabled user can reset their password

## Metadata

- HackerOne Report ID: 261297
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2020-03-01T15:01:45.393Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Steps:
1) Create user and disable the account
2) Goto reset password and enter disabled user's email address. Password reset link sent and he can reset the password using that link.
 
The point is : Disabled user can still access their account via reset password page. This is a very minor issue

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
