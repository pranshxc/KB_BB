---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36264'
original_report_id: '36264'
title: mod_proxy_fcgi buffer overflow
team_handle: ibb
created_at: '2014-09-17T00:00:00.000Z'
disclosed_at: '2014-11-12T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: Apache (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# mod_proxy_fcgi buffer overflow

## Metadata

- HackerOne Report ID: 36264
- Weakness: 
- Program: ibb
- Disclosed At: 2014-11-12T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

_This issue was reported directly to the Apache team._

A buffer overflow was found in mod_proxy_fcgi. A malicious FastCGI server could send a carefully crafted response which could lead to a heap buffer overflow.

http://httpd.apache.org/security/vulnerabilities_24.html#2.4.11-dev

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
