---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1746098'
original_report_id: '1746098'
title: potential denial of service attack via the locale parameter
weakness: Uncontrolled Resource Consumption
team_handle: ibb
created_at: '2022-10-21T21:33:21.558Z'
disclosed_at: '2022-11-28T18:31:27.075Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/django
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# potential denial of service attack via the locale parameter

## Metadata

- HackerOne Report ID: 1746098
- Weakness: Uncontrolled Resource Consumption
- Program: ibb
- Disclosed At: 2022-11-28T18:31:27.075Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

In Django 3.2 before 3.2.16, 4.0 before 4.0.8, and 4.1 before 4.1.2, internationalized URLs were subject to a denial of service attack via the locale parameter, which is treated as a regular expression.

## Impact

By crafting a Python regex, a vulnerable site could suffer a DOS attack. The attack was most likely to happen on sites that processes locale IDs from URL parameters.

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
