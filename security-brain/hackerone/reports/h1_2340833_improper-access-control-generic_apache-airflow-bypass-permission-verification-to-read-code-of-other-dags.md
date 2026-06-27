---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2340833'
original_report_id: '2340833'
title: 'Apache Airflow: Bypass permission verification to read code of other dags'
weakness: Improper Access Control - Generic
team_handle: ibb
created_at: '2024-01-31T07:20:55.910Z'
disclosed_at: '2024-03-12T02:19:57.277Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: https://github.com/apache/airflow
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Apache Airflow: Bypass permission verification to read code of other dags

## Metadata

- HackerOne Report ID: 2340833
- Weakness: Improper Access Control - Generic
- Program: ibb
- Disclosed At: 2024-03-12T02:19:57.277Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Apache Airflow, versions before 2.8.1, have a vulnerability that allows an authenticated user to access the source code of a DAG to which they don't have access. This vulnerability is considered low since it requires an authenticated user to exploit it. Users are recommended to upgrade to version 2.8.1, which fixes this issue.

**Email form the project maintainer**
██████████

## Impact

Apache Airflow<2.8.1

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
