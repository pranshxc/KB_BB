---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17227'
original_report_id: '17227'
title: SQL injection, time zoom script, tile ID
weakness: SQL Injection
team_handle: uzbey
created_at: '2014-06-22T21:52:40.294Z'
disclosed_at: '2014-07-18T20:25:51.108Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- sql-injection
---

# SQL injection, time zoom script, tile ID

## Metadata

- HackerOne Report ID: 17227
- Weakness: SQL Injection
- Program: uzbey
- Disclosed At: 2014-07-18T20:25:51.108Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The tile ID parameter to the tile zoom script is vulnerable to SQL injection.

The following will cause the script to run a benchmark, returning an error 8-10 seconds later:

https://staging.uzbey.com/zoom-image/BENCHMARK(10000000,SHA1(1))

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
