---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1195432'
original_report_id: '1195432'
title: Found a url on source code which was disclosing different juicy informations
  like ip addresses and available endponts
weakness: Information Exposure Through Directory Listing
team_handle: sifchain
created_at: '2021-05-13T10:04:06.439Z'
disclosed_at: '2021-05-14T15:25:29.993Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-exposure-through-directory-listing
---

# Found a url on source code which was disclosing different juicy informations like ip addresses and available endponts

## Metadata

- HackerOne Report ID: 1195432
- Weakness: Information Exposure Through Directory Listing
- Program: sifchain
- Disclosed At: 2021-05-14T15:25:29.993Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
I found a link in " https://github.com/Sifchain/sifnode/blob/develop/deploy/rake/cluster.rake" page which was exposing ip adresses and different endpoints which could be missused by hackers. 
Link Is=https://rpc.sifchain.finance/

## Steps To Reproduce:
1. Visit  https://rpc.sifchain.finance/ 

## Supporting Material/References:
{F1299908}
 Sample:
found on https://rpc.sifchain.finance/net_info? 
"remote_ip": "52.215.172.88"
      },
      {
        "node_info": {
          "protocol_version": {
            "p2p": "7",
            "block": "10",
            "app": "0"
          },
          "id": "5a03d7636ad9899e6ffb06ec929cdb9c963d5d3d",
          "listen_addr": "46.137.53.38:26656",
          "network": "sifchain",
          "version": "0.33.9",
          "channels": "4020212223303800",
          "moniker": "sarah",
          "other": {
            "tx_index": "on",
            "rpc_address": "tcp://0.0.0.0:26657"
          }
        },

## Impact

Internal Ip adresses , endpoints and other sensitive info related to company are revealed which can be used by attacker for Bad purpose.Attacker can use those endpoints for further attack

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
