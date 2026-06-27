---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1994585'
original_report_id: '1994585'
title: Cache purge requests are not authenticated
weakness: Business Logic Errors
team_handle: curl
created_at: '2023-05-19T19:34:19.757Z'
disclosed_at: '2023-05-20T15:10:42.419Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Cache purge requests are not authenticated

## Metadata

- HackerOne Report ID: 1994585
- Weakness: Business Logic Errors
- Program: curl
- Disclosed At: 2023-05-20T15:10:42.419Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:

Hello team,
Anyone can issue a PURGE request for any resource and invalidate your caches. That can lead to increased bandwidth costs but also potential Denial of Service attacks.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1.{Fundefined}

Unauthenticated cache purge request:

 curl 'https://curl.se/' -X PURGE
{ "status": "ok", "id": "21729-1683784658-593921" }  
  2.{Fundefined}
  

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]
https://sapt.medium.com/apple-hall-of-fame-for-a-small-misconfiguration-unauth-cache-purging-faf81b19419b

## Impact

That can lead to increased bandwidth costs but also potential Denial of Service attacks

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
