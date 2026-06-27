---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17225'
original_report_id: '17225'
title: SQL injection, tile ID
weakness: Command Injection - Generic
team_handle: uzbey
created_at: '2014-06-22T21:46:18.611Z'
disclosed_at: '2014-08-07T18:50:00.534Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- command-injection-generic
---

# SQL injection, tile ID

## Metadata

- HackerOne Report ID: 17225
- Weakness: Command Injection - Generic
- Program: uzbey
- Disclosed At: 2014-08-07T18:50:00.534Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The tile ID parameter to the tile image script is vulnerable to SQL injection.

The following will cause the script to run a benchmark, returning 8-10 seconds later:

https://staging.uzbey.com/tiles1600/693/sleep(10)

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
