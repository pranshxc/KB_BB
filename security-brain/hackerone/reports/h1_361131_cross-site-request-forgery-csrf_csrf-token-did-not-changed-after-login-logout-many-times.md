---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361131'
original_report_id: '361131'
title: csrf token did not changed after login/logout many times
weakness: Cross-Site Request Forgery (CSRF)
team_handle: liberapay
created_at: '2018-06-02T16:53:08.720Z'
disclosed_at: '2018-06-04T12:01:55.967Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 8
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# csrf token did not changed after login/logout many times

## Metadata

- HackerOne Report ID: 361131
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: liberapay
- Disclosed At: 2018-06-04T12:01:55.967Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hello team, 
your csrf token did not expired and after login and logout many times , i found that your csrf token is generated same as last one.

## Impact

if an attacker found an xss on your domain and you fixed it but attacker still has csrf token of user, attacker can use it to perform any action.

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
