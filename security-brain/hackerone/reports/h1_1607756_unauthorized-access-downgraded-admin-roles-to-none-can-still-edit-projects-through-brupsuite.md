---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1607756'
original_report_id: '1607756'
title: Unauthorized Access - downgraded admin roles to none can still edit projects
  through brupsuite
team_handle: omise
created_at: '2022-06-20T16:03:43.325Z'
disclosed_at: '2022-07-01T16:48:51.117Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: dashboard.omise.co
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Unauthorized Access - downgraded admin roles to none can still edit projects through brupsuite

## Metadata

- HackerOne Report ID: 1607756
- Weakness: 
- Program: omise
- Disclosed At: 2022-07-01T16:48:51.117Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

hi team,
I found that your site is vulnerable to Unauthorized Access lead to  privilege escalation, where when the owner invites a user with admin roles, the user can still edit anything with admin access, via brupsuite, it should get an error message because the admin role has been removed.


production step:
1. The `owner `invites `user` with admin roles at https://dashboard.omise.co/team
2. Then the `user`, intercept any request using brupsuite, for example edit/add link at https://dashboard.omise.co/v2/links
3. then the `owner` lowers the role to `none`
4. then you will see, the user does not see the create link feature because the role is lost
5. but when the `user` repeats the request step#2 via brupstuite. then it will be valid.

PoC :
██████

## Impact

Unauthorized Access lead to  privilege escalation, downgraded admin roles to none can still edit projects through brupsuite

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
