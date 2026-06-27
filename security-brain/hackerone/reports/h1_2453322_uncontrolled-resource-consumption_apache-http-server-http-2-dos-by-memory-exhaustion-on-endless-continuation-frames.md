---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2453322'
original_report_id: '2453322'
title: 'Apache HTTP Server: HTTP/2 DoS by memory exhaustion on endless continuation
  frames'
weakness: Uncontrolled Resource Consumption
team_handle: ibb
created_at: '2024-04-08T20:33:40.286Z'
disclosed_at: '2024-04-24T18:29:50.989Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
asset_identifier: https://github.com/apache/httpd
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Apache HTTP Server: HTTP/2 DoS by memory exhaustion on endless continuation frames

## Metadata

- HackerOne Report ID: 2453322
- Weakness: Uncontrolled Resource Consumption
- Program: ibb
- Disclosed At: 2024-04-24T18:29:50.989Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I'd like to report Apache httpd vulnerability (CVE-2024-27316) that was recently fixed.
* Advisory: https://httpd.apache.org/security/vulnerabilities_24.html

## Impact

HTTP/2 incoming headers exceeding the limit are temporarily buffered in nghttp2 in order to generate an informative HTTP 413 response. If a client does not stop sending headers, this leads to memory exhaustion.

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
