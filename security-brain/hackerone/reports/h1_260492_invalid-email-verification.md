---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260492'
original_report_id: '260492'
title: Invalid Email Verification
team_handle: legalrobot
created_at: '2017-08-15T20:27:34.102Z'
disclosed_at: '2017-08-28T18:34:17.383Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Invalid Email Verification

## Metadata

- HackerOne Report ID: 260492
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-08-28T18:34:17.383Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

URL: https://app.legalrobot.com/sign-in
Email verification is not proper in register page. for ex. john.smith@example.org this is the valid format but john*smith@example.org is also acceptable during registration.

Thanks and regards,
Prathamesh

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
