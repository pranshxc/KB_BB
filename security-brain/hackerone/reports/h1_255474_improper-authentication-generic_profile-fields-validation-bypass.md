---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '255474'
original_report_id: '255474'
title: Profile fields validation bypass
weakness: Improper Authentication - Generic
team_handle: legalrobot
created_at: '2017-08-01T11:28:17.370Z'
disclosed_at: '2017-09-01T17:47:30.974Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Profile fields validation bypass

## Metadata

- HackerOne Report ID: 255474
- Weakness: Improper Authentication - Generic
- Program: legalrobot
- Disclosed At: 2017-09-01T17:47:30.974Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello
I recently found a bug that without entering First and Last name the profile got updated, means a user can able to put his/her full name blank. In your website there is a validation for first and last name. If a user fill the first name then he has to fill the last name too and vice-versa but if he put both the field blank then he can update his profile and put his full name blank.
POC is attached with this report.
Thank you
Regards 
Prince Sinha

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
