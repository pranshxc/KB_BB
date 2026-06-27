---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '305974'
original_report_id: '305974'
title: Inappropriate URL parsing may cause security risk!
weakness: Server-Side Request Forgery (SSRF)
team_handle: ibb
created_at: '2018-01-17T17:30:00.770Z'
disclosed_at: '2019-11-12T09:18:33.734Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 57
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Inappropriate URL parsing may cause security risk!

## Metadata

- HackerOne Report ID: 305974
- Weakness: Server-Side Request Forgery (SSRF)
- Program: ibb
- Disclosed At: 2019-11-12T09:18:33.734Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description
-----
The behaviors in parse_url and http_wrap/cURL are different
　

## Original bug report
-----
- https://bugs.php.net/bug.php?id=74192

　
## Note
-----
- CVE-2017-7189 assigned


　
Thanks :)

## Impact

SSRF

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
