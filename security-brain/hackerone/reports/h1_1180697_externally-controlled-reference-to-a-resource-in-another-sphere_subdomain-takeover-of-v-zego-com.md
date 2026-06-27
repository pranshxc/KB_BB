---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1180697'
original_report_id: '1180697'
title: Subdomain takeover of v.zego.com
weakness: Externally Controlled Reference to a Resource in Another Sphere
team_handle: zego
created_at: '2021-04-29T23:47:33.603Z'
disclosed_at: '2021-06-26T04:22:26.339Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 84
asset_identifier: '*.zego.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- externally-controlled-reference-to-a-resource-in-another-sphere
---

# Subdomain takeover of v.zego.com

## Metadata

- HackerOne Report ID: 1180697
- Weakness: Externally Controlled Reference to a Resource in Another Sphere
- Program: zego
- Disclosed At: 2021-06-26T04:22:26.339Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
v.zego.com points to an AWS EC2 instance at 52.214.138.192 that no longer exists. I was able to take control of this IP address and run my own EC2 instance. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

### PoC
```
% dig +short v.zego.com
52.214.138.192

% curl v.zego.com
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
