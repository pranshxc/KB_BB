---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '107213'
original_report_id: '107213'
title: GlassWireSetup.exe subject to EXE planting attack
weakness: Privilege Escalation
team_handle: glasswire
created_at: '2015-12-28T19:04:26.126Z'
disclosed_at: '2016-02-04T20:46:46.381Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# GlassWireSetup.exe subject to EXE planting attack

## Metadata

- HackerOne Report ID: 107213
- Weakness: Privilege Escalation
- Program: glasswire
- Disclosed At: 2016-02-04T20:46:46.381Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

GlassWire recently fixed a DLL hijacking attack whereby trojan DLLs would be loaded from the user's \Downloads\ folder.

However, it appears that GlasswireSetup.exe still uses an unqualified path when running CertUtil.exe and as a consequence a trojaned CertUtil.exe will execute from the \Downloads\ folder. Interestingly, it executes without any security warning that Windows would normally show for a downloaded executable run from the shell (suggesting that CreateProcess was used rather than ShellExecute).

To fix this, it might make the most sense to set the current working directory to the System folder early in the Setup process.

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
