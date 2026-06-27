---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '335608'
original_report_id: '335608'
title: 'Denial of Service: nghttp2 use of uninitialized pointer'
weakness: NULL Pointer Dereference
team_handle: nodejs
created_at: '2018-04-10T18:46:30.736Z'
disclosed_at: '2020-02-13T23:47:23.557Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- null-pointer-dereference
---

# Denial of Service: nghttp2 use of uninitialized pointer

## Metadata

- HackerOne Report ID: 335608
- Weakness: NULL Pointer Dereference
- Program: nodejs
- Disclosed At: 2020-02-13T23:47:23.557Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

While investigating https://hackerone.com/reports/335533 and while following the same reproduction steps, I uncovered a bug in nghttp2 that causes use of an uninitialized pointer for an altsvc frameresulting in crash. The error can be easily triggered by a remote attacker by sending malformed ALTSVC and GOAWAY frames to the server, or by a malicious server sending same to the client. For Node.js, the result is a crashed process. The report has been submitted to the nghttp2 author who is working on a fix and is working on a fixed release.

## Impact

Crashing the Node.js process causing a Denial of Service

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
