---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '880089'
original_report_id: '880089'
title: Smartsheet employees email disclosure through enpoint after login.
weakness: Information Disclosure
team_handle: smartsheet
created_at: '2020-05-21T22:26:46.684Z'
disclosed_at: '2020-09-09T22:15:47.207Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: app.smartsheet.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Smartsheet employees email disclosure through enpoint after login.

## Metadata

- HackerOne Report ID: 880089
- Weakness: Information Disclosure
- Program: smartsheet
- Disclosed At: 2020-09-09T22:15:47.207Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
[add summary of the vulnerability]
After login  - while validating this issue [#858974](https://hackerone.com/reports/858974) - I notice there is an endpoint call `/b/home?formName=webop&formAction=SheetLabLoadData&to=68000&ss_v=98.0.2` that is bringing emails from some employees.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Login with your account
  2. While tracking traffic with your favorite traffic tracker capture the endpoint mentioned in the summary.
  3. Check the response

I honestly search in the dashboard where this information could be used and didn't founded it. Do we need this endpoint call?

## Bug Behavior
Expected: Do we need this information while loading the dashboard?
Actual: Employees email and name are being disclosed in the response

## Supporting Material/References:
[#858974](https://hackerone.com/reports/858974)

## Impact

Unnecessarily disclosing employee emails via endpoint call.

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
