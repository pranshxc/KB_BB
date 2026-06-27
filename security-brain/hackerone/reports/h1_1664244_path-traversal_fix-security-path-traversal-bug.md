---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1664244'
original_report_id: '1664244'
title: fix(security):Path Traversal Bug
weakness: Path Traversal
team_handle: hyperledger
created_at: '2022-08-09T17:07:15.177Z'
disclosed_at: '2022-08-11T19:53:16.714Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
asset_identifier: https://github.com/hyperledger/fabric
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# fix(security):Path Traversal Bug

## Metadata

- HackerOne Report ID: 1664244
- Weakness: Path Traversal
- Program: hyperledger
- Disclosed At: 2022-08-11T19:53:16.714Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Unsanitized input from CLI argument flows into `io.ioutil.ReadFile`, where it is used as a path. This may result in a Path Traversal vulnerability and allow an attacker to read arbitrary files.

See this fix : https://github.com/hyperledger/fabric/pull/3573

## Impact

There is a path traversal vulnerability in the source code of fabric

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
