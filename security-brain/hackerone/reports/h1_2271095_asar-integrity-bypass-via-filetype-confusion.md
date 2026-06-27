---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2271095'
original_report_id: '2271095'
title: ASAR Integrity bypass via filetype confusion
team_handle: ibb
created_at: '2023-12-04T06:02:02.108Z'
disclosed_at: '2024-01-20T16:43:37.361Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
asset_identifier: https://github.com/Electron
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# ASAR Integrity bypass via filetype confusion

## Metadata

- HackerOne Report ID: 2271095
- Weakness: 
- Program: ibb
- Disclosed At: 2024-01-20T16:43:37.361Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Maliciously crafted directories mirroring an ASAR file structure could be used to trick apps with ASAR integrity enabled into loading non-validated code.

## Impact

This only impacts apps that have the embeddedAsarIntegrityValidation and onlyLoadAppFromAsar fuses enabled. Apps without these fuses enabled are not impacted. This issue is specific to macOS as these fuses are only currently supported on macOS.

Specifically this issue can only be exploited if your app is launched from a filesystem the attacker has write access too. i.e. the ability to edit files inside the .app bundle on macOS which these fuses are supposed to protect against.

There are no app side workarounds, you must update to a patched version of Electron.

**Fixed Versions**
* `27.0.0-alpha.7`
* `26.2.1`
* `25.8.1`
* `24.8.3`
* `22.3.24`

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
