---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2064723'
original_report_id: '2064723'
title: unsanitized input goes to regex function leads to ReDos that make request hangs
weakness: Uncontrolled Resource Consumption
team_handle: ibb
created_at: '2023-07-12T08:54:12.403Z'
disclosed_at: '2023-08-28T16:28:56.866Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/apache/airflow
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# unsanitized input goes to regex function leads to ReDos that make request hangs

## Metadata

- HackerOne Report ID: 2064723
- Weakness: Uncontrolled Resource Consumption
- Program: ibb
- Disclosed At: 2023-08-28T16:28:56.866Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Apache Airflow, versions before 2.6.3, has a vulnerability where an authenticated user can use crafted input to make the current request hang

## Impact

this will help attacker achieve Dos attack with less effort

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
