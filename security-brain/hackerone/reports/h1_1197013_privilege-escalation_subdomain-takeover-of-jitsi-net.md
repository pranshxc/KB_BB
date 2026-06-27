---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1197013'
original_report_id: '1197013'
title: Subdomain takeover of ████.jitsi.net
weakness: Privilege Escalation
team_handle: 8x8
created_at: '2021-05-14T06:14:09.975Z'
disclosed_at: '2021-05-14T17:35:31.575Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.jitsi.net'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover of ████.jitsi.net

## Metadata

- HackerOne Report ID: 1197013
- Weakness: Privilege Escalation
- Program: 8x8
- Disclosed At: 2021-05-14T17:35:31.575Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
█████.jitsi.net points to an AWS EC2 instance at 18.195.93.116 that no longer exists. I was able to take control of this IP address and run my own EC2 instance. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

```
% dig +short ██████.jitsi.net
18.195.93.116

% curl ██████████.jitsi.net
<!-- hackerone.com/ian -->
```

## Impact

Subdomain takeover

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
