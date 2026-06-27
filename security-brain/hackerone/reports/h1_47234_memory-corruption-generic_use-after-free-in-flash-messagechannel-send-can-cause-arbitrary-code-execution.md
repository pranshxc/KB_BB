---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47234'
original_report_id: '47234'
title: Use After Free in Flash MessageChannel.send can cause arbitrary code execution
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2015-02-09T18:50:52.771Z'
disclosed_at: '2015-03-25T19:39:16.979Z'
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

# Use After Free in Flash MessageChannel.send can cause arbitrary code execution

## Metadata

- HackerOne Report ID: 47234
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2015-03-25T19:39:16.979Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Sending messages between workers while having the animation reloaded can cause an object to be freed while a reference remains in memory. An attacker can use this issue to control eip and potentially execute arbitrary code.

Identified as CVE-2015-0320, and reported to Adobe via Chrome VRP:
https://helpx.adobe.com/security/products/flash-player/apsb15-04.html

Original report with proof of concept showing how to control eip:
https://code.google.com/p/chromium/issues/detail?id=437441

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
