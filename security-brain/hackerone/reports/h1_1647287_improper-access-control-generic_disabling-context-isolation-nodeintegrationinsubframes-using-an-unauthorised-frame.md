---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1647287'
original_report_id: '1647287'
title: Disabling context isolation, nodeIntegrationInSubFrames using an unauthorised
  frame.
weakness: Improper Access Control - Generic
team_handle: ibb
created_at: '2022-07-23T04:36:37.661Z'
disclosed_at: '2022-08-11T23:08:15.229Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: https://github.com/Electron
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Disabling context isolation, nodeIntegrationInSubFrames using an unauthorised frame.

## Metadata

- HackerOne Report ID: 1647287
- Weakness: Improper Access Control - Generic
- Program: ibb
- Disclosed At: 2022-08-11T23:08:15.229Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Details can be found in the following github advisory: https://github.com/electron/electron/security/advisories/GHSA-mq8j-3h7h-p8g7

## Impact

Using a renderer exploit, context isolation and nodeIntegrationInSubFrames can be disabled, which enables an attacker to leak IPC module and communicate with the more privileged main process which might eventually lead to Remote Code Execution if there are sensitive IPC handlers on main process.

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
