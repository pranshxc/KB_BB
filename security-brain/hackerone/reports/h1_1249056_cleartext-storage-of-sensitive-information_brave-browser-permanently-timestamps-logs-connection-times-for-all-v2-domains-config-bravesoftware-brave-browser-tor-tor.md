---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1249056'
original_report_id: '1249056'
title: Brave Browser permanently timestamps & logs connection times for all v2 domains
  ~/.config/BraveSoftware/Brave-Browser/tor/data/tor.log
weakness: Cleartext Storage of Sensitive Information
team_handle: brave
created_at: '2021-07-01T08:53:07.800Z'
disclosed_at: '2021-08-16T17:57:43.188Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: https://github.com/brave/brave-core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Brave Browser permanently timestamps & logs connection times for all v2 domains ~/.config/BraveSoftware/Brave-Browser/tor/data/tor.log

## Metadata

- HackerOne Report ID: 1249056
- Weakness: Cleartext Storage of Sensitive Information
- Program: brave
- Disclosed At: 2021-08-16T17:57:43.188Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

A vulnerability in the Brave Browser v1.28.43 and below allows a local or physical attacker to view the exact timestamps that a user connected to a v2 onion address. A local or physical attacker could read  ~/.config/BraveSoftware/Brave-Browser/tor/data/tor.log identify the exact moment a user connected to a new site, easily triangulating the user via a complete log of connection timestamps, which could be easily compared with a server connection log, a compromised Tor end point, or other related Tor attack, affecting the confidentiality & integrity of a user's Tor session.

## Products affected: 

 * operating system, Brave version or Brave website page, etc.

Tor Desktop Browser (All platforms)

## Steps To Reproduce:

 * List the steps needed to reproduce the vulnerability

Visit http://wikitoronionlinks.com/ while using Tor Private Browsing.

Click on an assortment of .onion v2 URLs.

Inspect `~/.config/BraveSoftware/Brave-Browser/tor/data/tor.log`

## Supporting Material/References:

```
Jul 01 08:40:50.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:50.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:51.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:51.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:51.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:52.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:53.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:59.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:40:59.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:00.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:02.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:02.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:02.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:07.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:07.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:09.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:09.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:09.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:10.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline
Jul 01 08:41:12.000 [warn] Warning! You've just connected to a v2 onion address. These addresses are deprecated for security reasons, and are no longer supported in Tor. Please encourage the site operator to upgrade. For more information see https://blog.torproject.org/v2-deprecation-timeline

```

## Impact

Violate the confidentiality & integrity of a user's Tor session.

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
