---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1927360'
original_report_id: '1927360'
title: Previously created sessions continue being valid after 2FA activation
weakness: Improper Access Control - Generic
team_handle: wordpress
created_at: '2023-03-31T10:04:49.018Z'
disclosed_at: '2023-10-07T15:25:11.130Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: Official WordPress plugins
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Previously created sessions continue being valid after 2FA activation

## Metadata

- HackerOne Report ID: 1927360
- Weakness: Improper Access Control - Generic
- Program: wordpress
- Disclosed At: 2023-10-07T15:25:11.130Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

WordPress has a function called "2fa". I have found a bug in this function. As a result of this bug, every site that uses the 2fa function in WordPress is affected.

## Steps To Reproduce:
1/ Access the same account on example.com in two devices 
2/ On device 'A' go to  example.com> complete all steps to activate the 2FA system
Now the 2FA is activated for this account
3/ Back to device 'B' reload the page
The session still active

##Same to Same Report Link https://hackerone.com/reports/667739

## Impact

In this scenario when 2FA is activated the other sessions of the account are not invalidated.
2FA is required to login. I believe the expected and recommended behavior here is to terminate the other sessions> request a new login> request the 2FA code> so then give the account access again

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
