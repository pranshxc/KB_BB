---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1182864'
original_report_id: '1182864'
title: Subdomain takeover of fr1.vpn.zomans.com
weakness: Business Logic Errors
team_handle: zomato
created_at: '2021-05-03T08:00:51.110Z'
disclosed_at: '2021-09-17T05:50:51.808Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 91
asset_identifier: '*.zomans.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Subdomain takeover of fr1.vpn.zomans.com

## Metadata

- HackerOne Report ID: 1182864
- Weakness: Business Logic Errors
- Program: zomato
- Disclosed At: 2021-09-17T05:50:51.808Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
fr1.vpn.zomans.com points to an AWS EC2 instance at 52.47.57.107 that no longer exists. I was able to take control of this IP address and run my own EC2 instance. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

Since the risk of employee phishing here is pretty high, along with the risk of existing clients connecting to this server, I think it qualifies as a High per your policy:
> Subdomain Takeover - on a domain that sees heavy traffic or would be a convincing candidate for a phishing attack

### PoC
```
% dig +short fr1.vpn.zomans.com
52.47.57.107

% curl fr1.vpn.zomans.com
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
