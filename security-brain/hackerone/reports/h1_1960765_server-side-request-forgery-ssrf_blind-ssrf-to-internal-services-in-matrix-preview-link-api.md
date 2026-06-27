---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1960765'
original_report_id: '1960765'
title: Blind SSRF to internal services in matrix preview_link API
weakness: Server-Side Request Forgery (SSRF)
team_handle: reddit
created_at: '2023-04-24T21:33:47.707Z'
disclosed_at: '2023-04-26T15:42:47.191Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 298
asset_identifier: '*.reddit.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Blind SSRF to internal services in matrix preview_link API

## Metadata

- HackerOne Report ID: 1960765
- Weakness: Server-Side Request Forgery (SSRF)
- Program: reddit
- Disclosed At: 2023-04-26T15:42:47.191Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Reddit' new chat is based on Matrix software which has preview_link functionality which doesn't filter the URL before sending the request

## Impact:
Attacker can enumerate services by grabbing og:title and port scanning, also possible RCE escalation (Asking for permission on this one)

## Steps To Reproduce:


  1. Visit the https://matrix.redditspace.com/_matrix/media/r0/preview_url/?url=*
  2. Replace * with http://██████ to get og:title ███████
  3. Replace * with http://█████████ to get og:title ███████
 4. Replace * with http://██████████to get og:title ██████
 5. Replace * with ████████ to get og:title █████████

Note: If the request is stuck and not responding in 2 seconds reload the page until it does

## Permit for escalation attempt? 
Since the ███ URL is accessible it may be possible to run ███:
GET █████████

There are also possibilities to test ██████, but I thought that it would be incorrect to do such activity without permission and as such report vulnerability in this state. I also therefore request a permission to try to escalate this to Critical

## Impact

Attacker can enumerate services and launch attacks against them

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
