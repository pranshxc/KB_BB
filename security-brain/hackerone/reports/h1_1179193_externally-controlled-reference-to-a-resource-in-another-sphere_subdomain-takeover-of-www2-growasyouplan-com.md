---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1179193'
original_report_id: '1179193'
title: Subdomain takeover of www2.growasyouplan.com
weakness: Externally Controlled Reference to a Resource in Another Sphere
team_handle: palo_alto_software
created_at: '2021-04-28T23:41:24.216Z'
disclosed_at: '2021-05-29T19:29:40.612Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: www.liveplan.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- externally-controlled-reference-to-a-resource-in-another-sphere
---

# Subdomain takeover of www2.growasyouplan.com

## Metadata

- HackerOne Report ID: 1179193
- Weakness: Externally Controlled Reference to a Resource in Another Sphere
- Program: palo_alto_software
- Disclosed At: 2021-05-29T19:29:40.612Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
www2.growasyouplan.com points to an AWS EC2 instance at 67.202.62.93 that no longer exists. I was able to take control of this IP address and run my own EC2 instance. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

### Proof of scope
`growasyouplan.com` is owned by the same company as `paloalto.com`.

```
% whois growasyouplan.com | grep Org
Registrant Organization: Palo Alto Software, Inc.
```

### PoC
```
% dig +short www2.growasyouplan.com
67.202.62.93

% curl www2.growasyouplan.com
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
