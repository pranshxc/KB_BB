---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '504951'
original_report_id: '504951'
title: Malformed playlist.txt in GoldSrc games leads to Access Violation & arbitrary
  code execution
weakness: Stack Overflow
team_handle: valve
created_at: '2019-03-04T22:02:57.059Z'
disclosed_at: '2019-09-17T17:34:09.603Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 62
asset_identifier: hl.exe
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- stack-overflow
---

# Malformed playlist.txt in GoldSrc games leads to Access Violation & arbitrary code execution

## Metadata

- HackerOne Report ID: 504951
- Weakness: Stack Overflow
- Program: valve
- Disclosed At: 2019-09-17T17:34:09.603Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A crafted `playlist.txt` can be used to exploit a stack overflow vulnerability in `GameUI.dll` that can lead to arbitrary code execution.

# Reproduction
Place attached `playlist.txt` in game directory (`valve`, `cstrike`, etc.). The game will crash when it tries to play `Splash` track.

# Exploitability
The file can be sent from server with `precache_generic` function (custom `mp.dll`, amxx plugins, etc.). I don't know ant way to force reload the playlist, so for the exploit to trigger, the client must be restarted. In my opinion, it's still dangerous. And this method won't work if the client already had `playlist.txt` in the game directory.

## Impact

The attacker can use this to do many things, from crashing the client to stealing important data.

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
