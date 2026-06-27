---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '737058'
original_report_id: '737058'
title: Affiliates - Session Fixation
weakness: Session Fixation
team_handle: clario
created_at: '2019-11-13T19:48:42.782Z'
disclosed_at: '2020-06-14T06:49:20.454Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: '*.kromtech.com'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- session-fixation
---

# Affiliates - Session Fixation

## Metadata

- HackerOne Report ID: 737058
- Weakness: Session Fixation
- Program: clario
- Disclosed At: 2020-06-14T06:49:20.454Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

SEVERITY: Medium

LOCATION:
● https://affiliates.kromtech.com

ISSUE DESCRIPTION:
User can use the same session token after logout. Attacker can repeat request with token that should be marked as invalidated.

PROOF OF VULNERABILITY:
Request made after Logout with the same cookie value.

curl -i -s -k -X $'GET' \
-H $'Host: affiliates.kromtech.com' -H $'Cookie: sid=91iqik6qtblp0vsu9b5j7fgal0;' \
-b $'sid=91iqik6qtblp0vsu9b5j7fgal0' \
$'https://affiliates.kromtech.com/account'

RECOMMENDATIONS:
The logout function should be prominently visible to the user, explicitly invalidate a user’s session and disallow reuse of the session token. Server should provide new session id to user browser after logout.

## Impact

A remote attacker can gain access to victim’s session and perform arbitrary actions with privileges of the user within the compromised session.

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
