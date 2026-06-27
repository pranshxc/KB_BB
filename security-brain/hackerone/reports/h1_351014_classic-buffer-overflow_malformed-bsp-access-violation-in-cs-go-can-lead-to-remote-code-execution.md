---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '351014'
original_report_id: '351014'
title: Malformed .BSP Access Violation in CS:GO can lead to Remote Code Execution
weakness: Classic Buffer Overflow
team_handle: valve
created_at: '2018-05-13T00:57:18.088Z'
disclosed_at: '2018-07-19T21:55:29.472Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 149
asset_identifier: csgo.exe
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- classic-buffer-overflow
---

# Malformed .BSP Access Violation in CS:GO can lead to Remote Code Execution

## Metadata

- HackerOne Report ID: 351014
- Weakness: Classic Buffer Overflow
- Program: valve
- Disclosed At: 2018-07-19T21:55:29.472Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A malformed .BSP can trigger an Access Violation on CS:GO that can lead to arbitrary code execution on a remote computer. I have attached a copy of the malformed .BSP which reliably triggers an Access Violation on CS:GO.

## Impact

An attacker hosting a malicious server could compromise a remote client by having them download a custom map, triggering remote code execution on the victim's computer.

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
