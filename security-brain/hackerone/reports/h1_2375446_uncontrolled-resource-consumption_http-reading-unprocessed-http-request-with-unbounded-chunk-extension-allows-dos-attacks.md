---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2375446'
original_report_id: '2375446'
title: 'http: Reading unprocessed HTTP request with unbounded chunk extension allows
  DoS attacks'
weakness: Uncontrolled Resource Consumption
team_handle: ibb
created_at: '2024-02-15T18:19:30.014Z'
disclosed_at: '2024-03-05T12:09:56.321Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# http: Reading unprocessed HTTP request with unbounded chunk extension allows DoS attacks

## Metadata

- HackerOne Report ID: 2375446
- Weakness: Uncontrolled Resource Consumption
- Program: ibb
- Disclosed At: 2024-03-05T12:09:56.321Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I'd like to report Node.js vulnerability (CVE-2024-22019) that was recently fixed:
- HackerOne report: https://hackerone.com/reports/2233486
- Release notes: https://nodejs.org/en/blog/vulnerability/february-2024-security-releases

## Impact

This is a major issue because it allows unbounded resource (CPU, network bandwidth) consumption of the standard Node.js http server. The standard methods which could help blocking a malicious requests like timeouts and limiting request body size do not seem to work.

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
