---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '449478'
original_report_id: '449478'
title: Brave allows flash to follow 307 redirects to other origins with arbitrary
  content-types
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2018-11-25T07:41:37.412Z'
disclosed_at: '2018-12-12T19:20:29.745Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/brave/brave-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- violation-of-secure-design-principles
---

# Brave allows flash to follow 307 redirects to other origins with arbitrary content-types

## Metadata

- HackerOne Report ID: 449478
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2018-12-12T19:20:29.745Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Steps to reproduce:

Used https://github.com/sp1d3r/swf_json_csrf in latest available version of flash to send a post request cross-domain with a non-simple content type.


Actual results:

The request is sent in firefox.


Expected results:

The request should either not be sent or the content-type should not be allowed to be a non-simple content-type without a cors preflight request being made.

## Impact

https://bugzilla.mozilla.org/show_bug.cgi?id=1436241&fbclid=IwAR1iyg5ooZF46A-9BCtKGBIQgCsxQC419U3BaHzj8VnP9pcx8W_CRmBSbZQ

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
