---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2274981'
original_report_id: '2274981'
title: curl cookie mixed case PSL bypass
weakness: Information Exposure Through Sent Data
team_handle: ibb
created_at: '2023-12-06T12:00:29.753Z'
disclosed_at: '2023-12-22T04:11:01.031Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-exposure-through-sent-data
---

# curl cookie mixed case PSL bypass

## Metadata

- HackerOne Report ID: 2274981
- Weakness: Information Exposure Through Sent Data
- Program: ibb
- Disclosed At: 2023-12-22T04:11:01.031Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A vulnerability in curl allows a malicious HTTP server to set "super cookies" in curl that are then passed back to more origins than what is otherwise allowed or possible. This allows a site to set cookies that then would get sent to different and unrelated sites and domains.

It could do this by exploiting a mixed case flaw in curl's function that verifies a given cookie domain against the Public Suffix List (PSL). For example a cookie could be set with domain=co.UK when the URL used a lowercase hostname curl.co.uk, even though co.uk is listed as a PSL domain.

## Impact

Issue supercookies bypassing the Public Suffix List check.

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
