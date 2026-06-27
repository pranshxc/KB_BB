---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '673723'
original_report_id: '673723'
title: Leak of Internal IP addresses
team_handle: trint
created_at: '2019-08-14T15:44:27.994Z'
disclosed_at: '2021-03-12T15:31:56.472Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
asset_identifier: graphql2.trint.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Leak of Internal IP addresses

## Metadata

- HackerOne Report ID: 673723
- Weakness: 
- Program: trint
- Disclosed At: 2021-03-12T15:31:56.472Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The leak of Internal IP Addresses.
IP Addresses:-
   10.6.96.4 
   10.6.136.194
   10.6.127.182  

### Assessment:
[add your assessment of the vulnerability]

## Steps To Reproduce:
        1. Open request page of (graphql2.trint.com)  with "getUser" Operation name.
        2. Remove "authorization: Bearer" line and error will raise.
        3. You can see ("ip":"::ffff:10.6.127.182) and ("data":{"user":null}) in error.
It is happening only on "getUser" operation name.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]
F555596

## Impact

The leak of Internal IP Addresses will allow the attacker to get more information about the server.

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
