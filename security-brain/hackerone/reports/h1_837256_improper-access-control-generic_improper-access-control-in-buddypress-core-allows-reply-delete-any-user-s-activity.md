---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '837256'
original_report_id: '837256'
title: Improper Access Control in Buddypress core allows reply,delete any user's activity
weakness: Improper Access Control - Generic
team_handle: wordpress
created_at: '2020-04-02T15:09:51.209Z'
disclosed_at: '2020-05-22T00:33:25.125Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: BuddyPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Improper Access Control in Buddypress core allows reply,delete any user's activity

## Metadata

- HackerOne Report ID: 837256
- Weakness: Improper Access Control - Generic
- Program: wordpress
- Disclosed At: 2020-05-22T00:33:25.125Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description:

Improper Access Control in Buddypress core allows reply,delete any user's activity in other public group,which they don't join.

## Steps To Reproduce:
Step 1: Create two account A, B with two public groups
Step 2: In group A-account A, create a new activity [id_A]
Step 3: In group B-account B, create a new activity [id_B]
Step 4: In group A-account A select reply/delete action, use proxy to capture this request
Step 5: Change id_A by id_B
Step 6: Done, you deleted or reply user's activity without joining group
## Recommendations
Valid access control with their roles 

PoC with video

## Impact

Attacker without joining to group performs to reply,delete any activities without permission.

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
