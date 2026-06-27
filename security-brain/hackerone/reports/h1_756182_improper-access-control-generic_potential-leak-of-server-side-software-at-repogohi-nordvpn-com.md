---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '756182'
original_report_id: '756182'
title: Potential leak of server side software at repogohi.nordvpn.com
weakness: Improper Access Control - Generic
team_handle: nordsecurity
created_at: '2019-12-11T15:14:05.640Z'
disclosed_at: '2020-02-16T18:51:39.626Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: '*.nordvpn.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Potential leak of server side software at repogohi.nordvpn.com

## Metadata

- HackerOne Report ID: 756182
- Weakness: Improper Access Control - Generic
- Program: nordsecurity
- Disclosed At: 2020-02-16T18:51:39.626Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I found a public Git Repository at https://repogohi.nordvpn.com/. It looks like the software components in this repository are part of the VPN Servers. So I'm afraid there's a certain risk.

The following packages are among others publicly available:

```
openvpn-xor_2.4.5-stretch1nord_amd64.deb 
openvpn_2.4.5-stretch1nord_amd64.deb  
squid-langpack-nord_20180226-1_all.deb 
```

Furthermore I found the Origin-IP (behind Cloudflare): https://95.216.8.4/
This allows an attacker to bypass all security features of Cloudflare.

Feel free to correct my assumption and Severity of this report :)

## Impact

- Leak of server side software components (VPN Infrastructure)
- Simplifies the reengineering of the used software

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
