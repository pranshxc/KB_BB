---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1916583'
original_report_id: '1916583'
title: Authenticated but unauthorized users may enumerate Application names via the
  API
weakness: Information Exposure Through an Error Message
team_handle: ibb
created_at: '2023-03-24T08:50:46.515Z'
disclosed_at: '2023-05-25T19:49:06.641Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: https://github.com/argoproj/argoproj
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-exposure-through-an-error-message
---

# Authenticated but unauthorized users may enumerate Application names via the API

## Metadata

- HackerOne Report ID: 1916583
- Weakness: Information Exposure Through an Error Message
- Program: ibb
- Disclosed At: 2023-05-25T19:49:06.641Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

All versions of Argo CD starting with v0.5.0 are vulnerable to an information disclosure bug allowing unauthorized users to enumerate application names by inspecting API error messages. 

STEPS:
1. Login argocd with a user who has not application module's priviledge.
2. The user request 'api/v1/application/**/logs' restful api to download a log file.
3. The log file's content lead a information disclosure bug, which allowing unauthorized users to enumerate application names by inspecting API error messages. The error messages like 'error gettingg applicaiton by name: ** not found'.

## Impact

An attacker could use the discovered application names as the starting point of another attack. For example, the attacker might use their knowledge of an application name to convince an administrator to grant higher privileges (social engineering).

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
