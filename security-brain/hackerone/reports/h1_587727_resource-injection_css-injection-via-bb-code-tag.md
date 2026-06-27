---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '587727'
original_report_id: '587727'
title: CSS injection via BB code tag "█████"
weakness: Resource Injection
team_handle: phpbb
created_at: '2019-05-22T10:48:40.010Z'
disclosed_at: '2019-09-26T14:57:09.048Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 27
asset_identifier: https://github.com/phpbb/phpbb
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- resource-injection
---

# CSS injection via BB code tag "█████"

## Metadata

- HackerOne Report ID: 587727
- Weakness: Resource Injection
- Program: phpbb
- Disclosed At: 2019-09-26T14:57:09.048Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The input to the "█████" BBcode tag is not properly filtered. It gets converted into a CSS style attribute for a span HTML element.

Quotes (") are removed, so there's no way to break out of the CSS style attributed. However it is possible to arbitrarily dress the resulting span element.

To illustrate this here's an example:

███████

This will place a skull on the top of the page (by using position:fixed). I'll attach a screenshot as well.

The power of CSS pretty much allows arbitrary placement of elements across the page. This may also be used in UI redressing attacks.

## Impact

Attacker can arbitrarily redress page via forum posts.

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
