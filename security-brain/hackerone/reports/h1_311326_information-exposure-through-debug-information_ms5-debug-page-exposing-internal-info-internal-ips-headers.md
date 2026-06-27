---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '311326'
original_report_id: '311326'
title: ms5 debug page exposing internal info (internal IPs, headers)
weakness: Information Exposure Through Debug Information
team_handle: x
created_at: '2018-02-01T13:18:30.362Z'
disclosed_at: '2018-05-11T17:35:50.436Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-exposure-through-debug-information
---

# ms5 debug page exposing internal info (internal IPs, headers)

## Metadata

- HackerOne Report ID: 311326
- Weakness: Information Exposure Through Debug Information
- Program: x
- Disclosed At: 2018-05-11T17:35:50.436Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
Information exposure through /debug in ms5.twitter.com

**Description:** 
Debug page from ms5.twitter.com exposes internal info, such as internal IPs and headers. 

## Steps To Reproduce:

  1. Visit ms5.twitter.com/debug
  1. See internal IP and header-names used
  1. To gather more internal IPs, just refresh (or script curl requests) and you'll get a new internal IP every time.

## Impact: 
If an attacker gains access to your network, knowledge of internal IPs could help them know where to target.

## Supporting Material/References:

I made a script to make requests to see if internal IPs changed and every time I got a new one. Here is the 20 IPs I found using this technique:
> 10.49.205.118
> 10.45.237.113
> 10.81.156.108
> 10.58.127.114
> 10.58.103.105
> 10.58.217.103
> 10.42.70.113
> 10.45.222.103
> 10.58.101.114
> 10.45.221.103
> 10.45.109.100
> 10.42.70.119
> 10.43.71.127
> 10.48.219.111
> 10.44.90.100
> 10.46.246.111
> 10.43.73.138
> 10.46.6.102
> 10.45.65.104
> 10.45.64.108

## Impact

Debug pages should not be public. Giving away internal IPs means that an attacker could use this info for their advantage and know which IPs to target.

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
