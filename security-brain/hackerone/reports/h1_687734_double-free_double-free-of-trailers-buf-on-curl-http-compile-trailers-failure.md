---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '687734'
original_report_id: '687734'
title: Double-free of `trailers_buf' on `Curl_http_compile_trailers()` failure
weakness: Double Free
team_handle: curl
created_at: '2019-09-04T12:49:57.663Z'
disclosed_at: '2021-01-12T13:12:04.613Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- double-free
---

# Double-free of `trailers_buf' on `Curl_http_compile_trailers()` failure

## Metadata

- HackerOne Report ID: 687734
- Weakness: Double Free
- Program: curl
- Disclosed At: 2021-01-12T13:12:04.613Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
When `Curl_http_compile_trailers()` fails, `trailers_buf` is freed twice, because we don't pass to this function the pointer value by reference.

## Steps To Reproduce:
Did not actually reproduce, please double check patch attached and analysis.

## Impact

Some memory corruption due to the double-free.

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
