---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1486417'
original_report_id: '1486417'
title: '[Bypass] Ability to invite a new member in  sandbox Organization'
weakness: Business Logic Errors
team_handle: security
created_at: '2022-02-20T11:24:53.082Z'
disclosed_at: '2022-04-14T17:11:30.935Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# [Bypass] Ability to invite a new member in  sandbox Organization

## Metadata

- HackerOne Report ID: 1486417
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2022-04-14T17:11:30.935Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Able to bypass the restriction set in Organization sandbox (automatically created when you created sandbox program) to send an invite to another security researcher.

**Description:**
In the default UI of (sandbox)Hackerone Organization, inviting another security researcher is restricted ex.: https://hackerone.com/organizations/hackycorp_demo/users/invite . 
There is a grayed message:
*You have reached the maximum number of team member invitations for this program. Please contact support@hackerone.com if you need to lift the rate limit.*

But using this  endpoint i found in https://hackerone.com/assets/static/js/30.8f8e2bc5.chunk.js https://hackerone.com/organizations/hackycorp_demo/users/new_invite ==I can send an invite to anyone.==



### Steps To Reproduce
Demo Organization: hackycorp_demo
Test User : 0620  
Invited using: 0620@wearehackerone.com
Real email address: ████

1. Open this URLhttps://hackerone.com/organizations/hackycorp_demo/users/new_invite
2. Type the email address of another security researcher
3. Please see attached video for the demo:
████

## Impact

Bypass the restriction in the sandbox currently configured to send an invite to ane security researcher.

Similar to the report https://hackerone.com/reports/1088966 but on the Organization level.

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
