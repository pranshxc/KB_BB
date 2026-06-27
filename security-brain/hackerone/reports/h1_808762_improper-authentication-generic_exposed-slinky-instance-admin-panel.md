---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '808762'
original_report_id: '808762'
title: Exposed Slinky Instance Admin Panel
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2020-03-02T14:47:05.211Z'
disclosed_at: '2021-01-16T06:07:40.241Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: Other
asset_type: OTHER
max_severity: none
tags:
- hackerone
- improper-authentication-generic
---

# Exposed Slinky Instance Admin Panel

## Metadata

- HackerOne Report ID: 808762
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2021-01-16T06:07:40.241Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Last night the following server went from a 404 to a 200:
███████

Upon navigating to this page, I found that there was a slinky admin panel available here with the ability to change and modify URL redirection. 
```
https://slinky-server.shopifycloud.com/
```

## Impact

Ability to modify potentially trusted URL redirects

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
