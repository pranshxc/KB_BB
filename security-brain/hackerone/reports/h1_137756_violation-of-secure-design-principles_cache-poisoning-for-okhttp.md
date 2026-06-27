---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137756'
original_report_id: '137756'
title: Cache poisoning for okhttp
weakness: Violation of Secure Design Principles
team_handle: square-open-source
created_at: '2016-05-11T06:54:13.587Z'
disclosed_at: '2016-08-31T04:05:23.772Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Cache poisoning for okhttp

## Metadata

- HackerOne Report ID: 137756
- Weakness: Violation of Secure Design Principles
- Program: square-open-source
- Disclosed At: 2016-08-31T04:05:23.772Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

If an attacker can control the Host header this can be used to poison the cache. This becomes extra dangerous if the library were to be used to build a caching proxy.

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
