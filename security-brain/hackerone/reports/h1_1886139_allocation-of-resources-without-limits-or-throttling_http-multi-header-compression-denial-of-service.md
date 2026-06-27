---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1886139'
original_report_id: '1886139'
title: HTTP multi-header compression denial of service
weakness: Allocation of Resources Without Limits or Throttling
team_handle: ibb
created_at: '2023-02-24T15:01:59.498Z'
disclosed_at: '2023-02-24T23:04:06.173Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- allocation-of-resources-without-limits-or-throttling
---

# HTTP multi-header compression denial of service

## Metadata

- HackerOne Report ID: 1886139
- Weakness: Allocation of Resources Without Limits or Throttling
- Program: ibb
- Disclosed At: 2023-02-24T23:04:06.173Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A server can send an HTTP response with many occurrences of Transfer-Encoding and/or Content-Encoding headers. Each listed encoding allocates a buffer. The number of encodings listed within each header is already limited but the number of headers is not, allowing an HTTP response to consume all available memory.

## Impact

Consumes all available memory, resulting in a DoS.

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
