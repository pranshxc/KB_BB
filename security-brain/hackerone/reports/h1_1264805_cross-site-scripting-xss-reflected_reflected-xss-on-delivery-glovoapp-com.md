---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1264805'
original_report_id: '1264805'
title: Reflected XSS on delivery.glovoapp.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: glovo
created_at: '2021-07-15T23:55:34.979Z'
disclosed_at: '2021-08-18T07:02:21.112Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 32
asset_identifier: '*.glovoapp.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on delivery.glovoapp.com

## Metadata

- HackerOne Report ID: 1264805
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: glovo
- Disclosed At: 2021-08-18T07:02:21.112Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi, there's a reflected XSS vulnerability present on the https://delivery.glovoapp.com/referrals/ endpoint.

## Steps To Reproduce:
Opening the following URL should trigger the prompt() window specified in the request parameters, indicating that arbitrary javascript can be injected into the page.
- https://delivery.glovoapp.com/referrals/?email=%22%3E%3CsCriPt%20class%3Ddalfox%3Eprompt%281%29%3C%2Fscript%3E&lang=rs

## Impact

An attacker can do several client-side attacks on Glovo customers.

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
