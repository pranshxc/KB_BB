---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '900208'
original_report_id: '900208'
title: Unsecured Grafana instance on https://monitoring.prow-canary.k8s.io/dashboards
weakness: Improper Authentication - Generic
team_handle: kubernetes
created_at: '2020-10-07T11:24:29.118Z'
disclosed_at: '2021-01-07T18:32:43.812Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 2
asset_identifier: k8s.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Unsecured Grafana instance on https://monitoring.prow-canary.k8s.io/dashboards

## Metadata

- HackerOne Report ID: 900208
- Weakness: Improper Authentication - Generic
- Program: kubernetes
- Disclosed At: 2021-01-07T18:32:43.812Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi,
I was looking at  https://monitoring.prow-canary.k8s.io Grafana webapp. I'm not sure if it is for demo purposes, but I can access the main dashboard and view all graphs. 
`https://monitoring.prow-canary.k8s.io/dashboards`

If indeed it is for demo purposes, please let me close the report myself.
looking forward to hearing from you
Thank you

## Impact

access charts on various server resource usage.

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
