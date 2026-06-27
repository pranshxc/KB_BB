---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '450006'
original_report_id: '450006'
title: flatmap-stream malicious package (distributed via the popular events-stream)
weakness: Embedded Malicious Code
team_handle: nodejs-ecosystem
created_at: '2018-11-26T18:28:49.050Z'
disclosed_at: '2018-11-26T22:26:43.896Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: flatmap-stream
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- embedded-malicious-code
---

# flatmap-stream malicious package (distributed via the popular events-stream)

## Metadata

- HackerOne Report ID: 450006
- Weakness: Embedded Malicious Code
- Program: nodejs-ecosystem
- Disclosed At: 2018-11-26T22:26:43.896Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a case of malicious package (flat-stream) that made it's way into many other npm packages. One such popular package is `event-stream` (user dominictarr transferred the ownership of an npm module to another user because he wasn't actively maintaining it. That user then added malicious dependency to the package)

See discussion here: 
https://github.com/dominictarr/event-stream/issues/116

# Module

**module name:**  flatmap-stream
**version:** [MODULE VERSION]
**npm page:** `https://www.npmjs.com/package/flatmap-stream` (removed from npm by now)

## Module Description

It is not yet clear what the malicious code was doing. 
See discussion here: https://github.com/dominictarr/event-stream/issues/116#issuecomment-441737695

## Module Stats

> Replace stats below with numbers from npm’s module page:

flatmap-stream is not popular, but event-stream is very popular (1,996,440 downloads per week)

## Impact

RCE

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
