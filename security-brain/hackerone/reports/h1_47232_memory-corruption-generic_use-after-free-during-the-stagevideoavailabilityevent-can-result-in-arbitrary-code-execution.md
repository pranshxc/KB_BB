---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47232'
original_report_id: '47232'
title: Use after free during the StageVideoAvailabilityEvent can result in arbitrary
  code execution
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2015-02-09T18:44:09.226Z'
disclosed_at: '2015-03-25T19:39:16.982Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# Use after free during the StageVideoAvailabilityEvent can result in arbitrary code execution

## Metadata

- HackerOne Report ID: 47232
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2015-03-25T19:39:16.982Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An attacker can register the StageVideoAvailabilityEvent and have the SWF movie reloaded at the same time with LoadMovie. During this process, an object may be freed allowing the attacker to take control of the code flow.

Identified as CVE-2015-0315, and reported to Adobe via Chrome VRP:
https://helpx.adobe.com/security/products/flash-player/apsb15-04.html

Original report with an exploit for Chrome:
https://code.google.com/p/chromium/issues/detail?id=429276

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
