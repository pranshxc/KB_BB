---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '194454'
original_report_id: '194454'
title: Exposed Unencrypted Telnet Endpoint
team_handle: starbucks
created_at: '2016-12-28T18:02:44.662Z'
disclosed_at: '2017-02-08T00:51:09.048Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
---

# Exposed Unencrypted Telnet Endpoint

## Metadata

- HackerOne Report ID: 194454
- Weakness: 
- Program: starbucks
- Disclosed At: 2017-02-08T00:51:09.048Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I'm not sure where to submit this as I know it is a low/medium risk issue on an asset which is out of scope. Essentially I stumbled across the endpoint whilst looking at other Starbucks domains within scope, the affected host is:
`franchisee.starbucks.com:23` it was found to be running an instance of telnet that is brute-forcible however given the host is out of scope, no attempts have been made to acquire access. When connecting to the host via telnet or netcat the following banner is presented:
`N4-DC4-STARBUCKS-RTR-01 (ttyp0)`

I'd recommend this host/endpoint be locked down ensuring that telnet is only reachable from VPN or inside the firewall. 

Thanks,

@ZephrFish

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
