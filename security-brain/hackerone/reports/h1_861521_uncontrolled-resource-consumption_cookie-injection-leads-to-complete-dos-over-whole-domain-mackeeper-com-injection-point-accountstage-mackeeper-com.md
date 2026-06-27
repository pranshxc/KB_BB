---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '861521'
original_report_id: '861521'
title: Cookie injection leads to complete DoS over whole domain *.mackeeper.com. Injection
  point accountstage.mackeeper.com/
weakness: Uncontrolled Resource Consumption
team_handle: clario
created_at: '2020-04-28T14:42:51.068Z'
disclosed_at: '2020-10-21T09:21:06.712Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: '*.mackeeper.com'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Cookie injection leads to complete DoS over whole domain *.mackeeper.com. Injection point accountstage.mackeeper.com/

## Metadata

- HackerOne Report ID: 861521
- Weakness: Uncontrolled Resource Consumption
- Program: clario
- Disclosed At: 2020-10-21T09:21:06.712Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
 The cookie bomb works by setting large cookies that are way too big making the server decline any request send with them for having a too long request header.

##PoC
1.  Open below link and click on link
https://unequaledfloor.htmlpasta.com/

2.  Now open https://accountstage.mackeeper.com/ or https://.mackeeper.com/ , these domains won't open anymore.

## Impact

The escape function is used, which means a value consisting of special symbols will become three times longer. For example ,,, will turn into %2C. That means an attacker can create a valid link of proper length accepted both by the browser and the server, which however will make the cookie too long.

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
