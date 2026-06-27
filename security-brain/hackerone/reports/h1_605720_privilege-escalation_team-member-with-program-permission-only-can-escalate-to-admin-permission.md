---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '605720'
original_report_id: '605720'
title: Team member with Program permission only can escalate to Admin permission
weakness: Privilege Escalation
team_handle: security
created_at: '2019-06-10T23:14:30.649Z'
disclosed_at: '2019-06-26T21:02:41.417Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 258
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Team member with Program permission only can escalate to Admin permission

## Metadata

- HackerOne Report ID: 605720
- Weakness: Privilege Escalation
- Program: security
- Disclosed At: 2019-06-26T21:02:41.417Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

`https://hackerone.com/TEAM/groups` URL is accessible to team members with Program permission, even when "Group Management" and "User Management" menus aren't visible.

I didn't research this further, however, I was able to grant all permissions to the user assigned to a group with `Program` permission.

## PoC

> Tested on a user assigned to a group with Program permissions

1. Go to `https://hackerone.com/TEAM/groups`
2. Select the current user's group
3. Add arbitrary permission (e.g. Admin)

## Additional information disclosure

I noticed that `hackerone.com/teams.json` is accessible to users with "read-only" permission, but `https://hackerone.com/TEAM/groups.json` is accessible to users with at least 1 valid permission. 

That's strange because the data is *identical* and **allows disclosing user ids, assigned groups, groups permissions**.

Reporting 2 issues in one report, because it's hard to understand the real root cause of the broken RBAC.

## Impact

- A team member with 1 valid permission (except "readonly", e.g. Program) can escalate own permissions in the team to arbitrary permissions.
- "readonly" team member can disclose the team's groups, assigned users, groups' permissions and ids/names.

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
