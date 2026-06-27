---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1888915'
original_report_id: '1888915'
title: Reset password link sent over unsecured http protocol
weakness: Improper Access Control - Generic
team_handle: mattermost
created_at: '2023-02-28T10:37:19.575Z'
disclosed_at: '2023-05-10T08:53:31.726Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 400
asset_identifier: h1-*your-own-instance*.cloud.mattermost.com
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Reset password link sent over unsecured http protocol

## Metadata

- HackerOne Report ID: 1888915
- Weakness: Improper Access Control - Generic
- Program: mattermost
- Disclosed At: 2023-05-10T08:53:31.726Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
After creating the workspace, if victim clicks on forgot password then reset password link has been generated and sent over mail and that password link is unsecured http protocol.

## Steps To Reproduce:

  1. Signup to a workspace
  2. Navigate to https://h1-\*your-own-instance\*.cloud.mattermost.com/reset_password and enter signup email
  3. Check email, you will get reset passwork link. {F2201387}
  4. Copy that link paste in notepad and observe the protocol. {F2201388}

## Mitigation:
Generate reset password link with secured https protocol.

## Impact

If the victim opens the reset password link and forgot to update the password, anyone from intermediate computers through network or sniffer can reset the password.

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
