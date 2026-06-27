---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2070212'
original_report_id: '2070212'
title: Apache Airflow path traversal by authenticated user
weakness: Path Traversal
team_handle: ibb
created_at: '2023-07-15T03:20:46.196Z'
disclosed_at: '2023-09-14T17:50:47.985Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/apache/airflow
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# Apache Airflow path traversal by authenticated user

## Metadata

- HackerOne Report ID: 2070212
- Weakness: Path Traversal
- Program: ibb
- Disclosed At: 2023-09-14T17:50:47.985Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an attacker to perform unauthorized file access outside the intended directory structure by manipulating the run_id parameter.

## Impact

Denial of Service (DoS): By traversing to system directories and attempting to access large or resource-intensive files, an attacker can cause a denial of service condition. This can lead to system crashes, resource exhaustion, or degraded performance.

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
