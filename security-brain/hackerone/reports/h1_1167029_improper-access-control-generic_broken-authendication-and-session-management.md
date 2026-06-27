---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1167029'
original_report_id: '1167029'
title: Broken Authendication And Session Management
weakness: Improper Access Control - Generic
team_handle: reddit
created_at: '2021-04-17T02:50:19.602Z'
disclosed_at: '2021-10-21T19:56:05.907Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Broken Authendication And Session Management

## Metadata

- HackerOne Report ID: 1167029
- Weakness: Improper Access Control - Generic
- Program: reddit
- Disclosed At: 2021-10-21T19:56:05.907Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
Broken Authendication And Session Management On reddit.com

Here I'm Using 2 Browsers
1.Chrome (victim Browser)
2.Firefox(attacker browser)

## Steps To Reproduce:

  1. Login your Account (Chrome Browser)
  2. Copy Cookies 
3. Paste it in firefox Browser and reload
4. you login without username and password

## Supporting Material/References:


  * broken auth POC.mkv

## Impact

An attacker can access victim account without entering username and password

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
