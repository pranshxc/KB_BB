---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1691888'
original_report_id: '1691888'
title: Firebase credentials leak
team_handle: mtn_group
created_at: '2022-09-06T03:11:17.395Z'
disclosed_at: '2022-12-15T13:28:25.003Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Firebase credentials leak

## Metadata

- HackerOne Report ID: 1691888
- Weakness: 
- Program: mtn_group
- Disclosed At: 2022-12-15T13:28:25.003Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
This report is regarding the fix of #1351329.
The fix is not patched fully, comments are visible to anyone and an attacker can utilize this for further attacks.

## Steps To Reproduce:
go to : view-source:https://mpulse.mtn.ng/
search for 'Initialize Firebase'

as you can see the firebase details are commented.

## Supporting Material/References:
POC attached

## Impact

Unauthorized access to firebase

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
