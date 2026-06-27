---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1943252'
original_report_id: '1943252'
title: Response Manipulation lead to bypass verification code while making appointment
  at `█████████`
weakness: Business Logic Errors
team_handle: mars
created_at: '2023-04-12T06:46:56.606Z'
disclosed_at: '2023-08-30T15:46:47.850Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: '*.banfield.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Response Manipulation lead to bypass verification code while making appointment at `█████████`

## Metadata

- HackerOne Report ID: 1943252
- Weakness: Business Logic Errors
- Program: mars
- Disclosed At: 2023-08-30T15:46:47.850Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Steps To Reproduce:

1. Go to this URL https://www.███/visit-information/schedule-appointment/
2. Make an appointment
3. Choose send verification code to email
4. Enter random code 
5. Intercept the request using burp
4. Click do intercept response and forward
5. Change false to true

## Impact

bypass verification code

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
