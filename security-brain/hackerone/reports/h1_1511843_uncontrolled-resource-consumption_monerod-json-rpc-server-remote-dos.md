---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1511843'
original_report_id: '1511843'
title: monerod JSON RPC server remote DoS
weakness: Uncontrolled Resource Consumption
team_handle: monero
created_at: '2022-03-15T00:16:28.708Z'
disclosed_at: '2022-09-12T21:50:10.819Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- uncontrolled-resource-consumption
---

# monerod JSON RPC server remote DoS

## Metadata

- HackerOne Report ID: 1511843
- Weakness: Uncontrolled Resource Consumption
- Program: monero
- Disclosed At: 2022-09-12T21:50:10.819Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Monero daemon (monerod)  does not limit Content-length variable when processing incoming HTTP requests.
We can force monerod to allocate arbitrary amount of memory.


How to reproduce:
1) compile monero https://github.com/monero-project/monero
2) run it:
$ ulimit -Sv 1000000000
$ ./bin/monerod --rpc-login test:test  --rpc-bind-ip 0.0.0.0 --confirm-external-bind

3) run attached script m1.py
$ python2 ./m1.py 192.168.1.34

4) after some time OOM killer will stop monerod

## Impact

monerod process can be stopped remotely, no authentication is required. 
An access to JSON RPC port is enough.

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
