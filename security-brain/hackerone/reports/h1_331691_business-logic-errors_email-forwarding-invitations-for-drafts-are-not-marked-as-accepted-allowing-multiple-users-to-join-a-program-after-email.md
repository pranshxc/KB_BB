---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '331691'
original_report_id: '331691'
title: Email Forwarding invitations for Drafts are not marked as accepted, allowing
  multiple users to join a program after disabling Email Forwarding
weakness: Business Logic Errors
team_handle: security
created_at: '2018-03-31T23:35:36.633Z'
disclosed_at: '2018-04-18T21:32:02.265Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Email Forwarding invitations for Drafts are not marked as accepted, allowing multiple users to join a program after disabling Email Forwarding

## Metadata

- HackerOne Report ID: 331691
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2018-04-18T21:32:02.265Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###STEPS TO REPRODUCE:

1. I have found a sandboxed team in hackerone,named █████.
2. The manager of that team sends an invitation to: ██████████ ( which email was not exist on hackerone account)
3. Now the invitation link receive was ========> ████
4. I logged in from multiple researcher account and visited the link and accepted the request. 
5. Now the invitation link was still live.

So, a member  can pass this token to other people and they will be added to the team.I used this token multiple times and it's still live.

## Impact

The invitation token can be use in multiple times.

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
