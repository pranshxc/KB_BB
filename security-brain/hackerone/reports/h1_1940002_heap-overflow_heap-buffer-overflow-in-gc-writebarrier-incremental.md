---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1940002'
original_report_id: '1940002'
title: heap-buffer-overflow in gc_writebarrier_incremental
weakness: Heap Overflow
team_handle: ruby
created_at: '2023-04-09T13:21:30.452Z'
disclosed_at: '2023-07-19T09:24:48.110Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 0
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- heap-overflow
---

# heap-buffer-overflow in gc_writebarrier_incremental

## Metadata

- HackerOne Report ID: 1940002
- Weakness: Heap Overflow
- Program: ruby
- Disclosed At: 2023-07-19T09:24:48.110Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

how to reproduce:
build ruby-3.2.2 with asan
cat heap-buffer-overflow | ruby-3.2.2/miniruby -e 'Marshal.load(ARGF.read)'

## Impact

may over access memory

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
