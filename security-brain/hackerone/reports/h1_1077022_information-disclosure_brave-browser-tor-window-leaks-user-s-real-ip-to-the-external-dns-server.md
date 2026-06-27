---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1077022'
original_report_id: '1077022'
title: Brave Browser Tor Window leaks user's real IP to the external DNS server
weakness: Information Disclosure
team_handle: brave
created_at: '2021-01-12T13:44:50.222Z'
disclosed_at: '2021-06-17T05:25:38.585Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 276
asset_identifier: https://laptop-updates.brave.com/latest/linux64
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Brave Browser Tor Window leaks user's real IP to the external DNS server

## Metadata

- HackerOne Report ID: 1077022
- Weakness: Information Disclosure
- Program: brave
- Disclosed At: 2021-06-17T05:25:38.585Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

When a user navigates to a URL in Tor Window, the DNS requests are sent directly without using the Tor proxy, which leaks the user's real IP address and the requested domain name to the user's ISP and the DNS server.

## Products affected: 

 * OS: Ubuntu 18.04.5 LTS x86_64
 * Brave: Version 1.18.78 Chromium: 87.0.4280.141 (Official Build) (64-bit)

## Steps To Reproduce:

 * Open WireShark, and start capturing traffic on the Internet interface. Set WireShark's display filter to `dns`.
 * Open Brave Browser. Then open new private window with Tor.
 * On the Tor window, navigate to https://tools.ietf.org/ (or any other URLs)
 * In WireShark, you can see a DNS request for tools.ietf.org sent to your DNS server.

## Supporting Material/References:

  * a screenshot attached

## Impact

Brave's Tor window passively leaks users' IP addresses and requests to DNS servers. This undermines the user's anonymity.

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
