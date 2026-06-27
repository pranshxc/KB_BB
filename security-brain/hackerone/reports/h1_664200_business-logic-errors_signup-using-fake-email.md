---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '664200'
original_report_id: '664200'
title: SignUp using Fake Email
weakness: Business Logic Errors
team_handle: nextcloud
created_at: '2019-07-31T08:19:02.886Z'
disclosed_at: '2019-08-02T08:29:13.360Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# SignUp using Fake Email

## Metadata

- HackerOne Report ID: 664200
- Weakness: Business Logic Errors
- Program: nextcloud
- Disclosed At: 2019-08-02T08:29:13.360Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

In this trial I used the email 'ardi@ardi.ardi' and after pressing the SIGN UP button it will automatically redirect to https://ppp.woelkli.com/apps/preferred_providers/password/set/emailfakeforregister/H2qlEWHxQ3yiJgCsEXkR8, not through the account verification process first.

For full the link PoC can see on the link this: https://drive.google.com/file/d/1VX5MBh7WR__Zj2lIup4TtS81VawPy0F7/view?usp=drivesdk

Thank you.

## Impact

This will enable someone to create multiple accounts at once without verification.

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
