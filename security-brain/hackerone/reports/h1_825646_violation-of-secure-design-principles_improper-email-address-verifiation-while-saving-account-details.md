---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '825646'
original_report_id: '825646'
title: Improper email address verifiation while saving Account Details
weakness: Violation of Secure Design Principles
team_handle: stagingdoteverydotorg
created_at: '2020-03-20T20:22:07.550Z'
disclosed_at: '2020-03-23T08:31:07.262Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 32
asset_identifier: staging.every.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Improper email address verifiation while saving Account Details

## Metadata

- HackerOne Report ID: 825646
- Weakness: Violation of Secure Design Principles
- Program: stagingdoteverydotorg
- Disclosed At: 2020-03-23T08:31:07.262Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Attacker could be able change its email to any email address even already created another user's email address.(Even though UI doesnot allow it)
## Steps To Reproduce:

  0. Set up proxy.
  1. Singup with any email address
  2. Go to profile section 
  3. Click on update button
  4. Monitor call in reverse proxy and change email field to any user's email address
 5. Done! Attacker is able to change its email address to any email address even registered one's

## Supporting Material/References:
https://hackerone.com/reports/30975
[list any additional material (e.g. screenshots, logs, etc.)]

## Impact

Attacker might be able to impersonate as any other user

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
