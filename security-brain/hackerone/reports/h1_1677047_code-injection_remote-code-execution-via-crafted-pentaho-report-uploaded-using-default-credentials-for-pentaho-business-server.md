---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1677047'
original_report_id: '1677047'
title: Remote code execution via crafted pentaho report uploaded using default credentials
  for pentaho business server
weakness: Code Injection
team_handle: mtn_group
created_at: '2022-08-22T18:07:27.314Z'
disclosed_at: '2023-12-31T21:08:44.212Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 52
asset_identifier: mtn.ci
asset_type: URL
max_severity: critical
tags:
- hackerone
- code-injection
---

# Remote code execution via crafted pentaho report uploaded using default credentials for pentaho business server

## Metadata

- HackerOne Report ID: 1677047
- Weakness: Code Injection
- Program: mtn_group
- Disclosed At: 2023-12-31T21:08:44.212Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Good day,
                      While I do recon for mtn.ci domain I found  Pentaho business server at https://sm.mtn.ci:8888/pentaho with default credentials admin/password ,then I figured that I can upload  prpt reports to server which could use some beanshell,js and java to achieve RCE

## Steps To Reproduce:
1. Login to https://sm.mtn.ci:8888/pentaho admin/password  
{F1878259}
2. Use Pentaho report designer to create malicious report file  
{F1878260}
3. Upload and run the report   
{F1878261}  
{F1878262}

## Impact

The impact of an RCE vulnerability can range from malware execution to an attacker gaining full control over a compromised server.

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
