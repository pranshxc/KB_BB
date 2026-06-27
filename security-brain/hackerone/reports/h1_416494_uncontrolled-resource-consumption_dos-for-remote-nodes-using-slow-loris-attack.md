---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '416494'
original_report_id: '416494'
title: DoS for remote nodes using Slow Loris attack
weakness: Uncontrolled Resource Consumption
team_handle: monero
created_at: '2018-09-30T14:16:46.633Z'
disclosed_at: '2019-02-21T17:44:52.823Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- uncontrolled-resource-consumption
---

# DoS for remote nodes using Slow Loris attack

## Metadata

- HackerOne Report ID: 416494
- Weakness: Uncontrolled Resource Consumption
- Program: monero
- Disclosed At: 2019-02-21T17:44:52.823Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 

Using the slow loris attack it's possible to make the the daemon unresponsive to all RPC requests without at least a restart.

**Description:** 

I used this node.js application (https://www.npmjs.com/package/sloww) to perform the attack on one of my remote nodes, but any other implementation of the attack should also work fine.

## Releases Affected:

  * Ubuntu 16.04 x64 - Monero v0.12.3.0 was affected so all releases before should be affected as well.
  
## Steps To Reproduce:

  1. Start the daemon with standard remote node parameters like `./monerod --rpc-bind-ip 0.0.0.0 --confirm-external-bind`
  2. Start the slow loris attack, I tested with 1000 sockets opened and 700 milliseconds as rate at which 
      packets should be sent.
  3. Try sending a normal RPC command like `curl -X POST http://IP:18089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_block_count"}' -H 'Content-Type: application/json'` there will not be any response from the RPC a few seconds after the attack was started.

## Impact

An attacker could target a large number of remote nodes for example the ones under https://moneroworld.com/, with just a single PC.

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
