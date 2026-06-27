---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '271950'
original_report_id: '271950'
title: Improper Implementation of Password strength checker
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2017-09-26T12:14:55.204Z'
disclosed_at: '2017-11-10T04:17:37.019Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Improper Implementation of Password strength checker

## Metadata

- HackerOne Report ID: 271950
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2017-11-10T04:17:37.019Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I have seen Improper Implementation of Password strength checker for registration and login page. Once it suggest complex password, one can alter the password but the complexity remain the same  Its usually related to Ajax or auto-reload implementation.  

PoC
-------------------------------------
As a prof of concept see the attached picture, where the complexity says very high but with no password input.

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
