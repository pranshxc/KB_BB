---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1594627'
original_report_id: '1594627'
title: 'Apache HTTP Server: mod_proxy_ajp: Possible request smuggling'
team_handle: ibb
created_at: '2022-06-08T10:29:46.564Z'
disclosed_at: '2022-07-09T19:25:47.839Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: https://github.com/apache/httpd
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Apache HTTP Server: mod_proxy_ajp: Possible request smuggling

## Metadata

- HackerOne Report ID: 1594627
- Weakness: 
- Program: ibb
- Disclosed At: 2022-07-09T19:25:47.839Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling') vulnerability in mod_proxy_ajp of Apache HTTP Server allows an attacker to smuggle requests to the AJP server it forwards requests to.  This issue affects Apache HTTP Server Apache HTTP Server 2.4 version 2.4.53 and prior versions.

## Impact

Information disclosure, RCE

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
