---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '642862'
original_report_id: '642862'
title: Option method enabled in kartpay Webservers
weakness: Information Disclosure
team_handle: kartpay
created_at: '2019-07-14T09:57:43.962Z'
disclosed_at: '2019-08-28T15:31:29.878Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: '*.kartpay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Option method enabled in kartpay Webservers

## Metadata

- HackerOne Report ID: 642862
- Weakness: Information Disclosure
- Program: kartpay
- Disclosed At: 2019-08-28T15:31:29.878Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

HTTP OPTIONS method is enabled on this web server. The OPTIONS method provides a list of the methods that are supported by the web server, it represents a request for information about the communication options available on the request/response chain identified by the Request-URI.

Domain :
merchant.kartpay.com

## Impact

The issue was not critical, as the impact of using other methods than GET and POST in this domain is nearly nonexistent. The bounty reflects the criticality of the issue.

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
