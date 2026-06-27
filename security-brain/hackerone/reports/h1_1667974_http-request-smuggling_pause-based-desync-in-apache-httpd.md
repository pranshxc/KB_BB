---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1667974'
original_report_id: '1667974'
title: Pause-based desync in Apache HTTPD
weakness: HTTP Request Smuggling
team_handle: ibb
created_at: '2022-08-12T17:34:36.454Z'
disclosed_at: '2022-08-25T07:02:46.335Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 66
asset_identifier: https://github.com/apache/httpd
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- http-request-smuggling
---

# Pause-based desync in Apache HTTPD

## Metadata

- HackerOne Report ID: 1667974
- Weakness: HTTP Request Smuggling
- Program: ibb
- Disclosed At: 2022-08-25T07:02:46.335Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Apache was vulnerable to a pause-based desync. This vulnerability is described in detail in my whitepaper here: https://portswigger.net/research/browser-powered-desync-attacks#pause

## Impact

This enables server-side HTTP Request Smuggling when Apache is deployed as a back-end server, and it also enables MITM attackers to inject arbitrary JavaScript in spite of TLS.

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
