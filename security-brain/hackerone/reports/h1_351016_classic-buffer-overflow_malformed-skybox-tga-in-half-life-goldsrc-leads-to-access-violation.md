---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '351016'
original_report_id: '351016'
title: Malformed Skybox .TGA in Half-Life (GoldSRC) leads to Access Violation
weakness: Classic Buffer Overflow
team_handle: valve
created_at: '2018-05-13T01:14:32.363Z'
disclosed_at: '2018-08-28T23:37:17.517Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
asset_identifier: hl.exe
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- classic-buffer-overflow
---

# Malformed Skybox .TGA in Half-Life (GoldSRC) leads to Access Violation

## Metadata

- HackerOne Report ID: 351016
- Weakness: Classic Buffer Overflow
- Program: valve
- Disclosed At: 2018-08-28T23:37:17.517Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A malformed .TGA when loaded as a Skybox on a map in a GoldSRC engine game (Half-Life) can lead to arbitrary code execution on a remote client.

###Reproduction Steps

Load the attached map + resources on a local Half-Life listen server. The game will crash with an Access Violation as soon as the map with the malicious skybox is loaded.

###Exploitability

Since anyone can host a map with custom assets, and the custom assets are loaded onto a remote clients computer, a malicious server can distribute malformed skybox assets (.TGA's) that could cause remote code execution on clients. The inclusion of .DLL's on Steam without ASLR make exploitablility of this bug via ROP quite trivial.

## Impact

###Impact

A malicious server could infect hundreds or perhaps thousands of clients with this bug. This bug could also be used in targeted attacks for the theft / compromise of high-value Steam accounts by attacking their Half-Life client.

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
