---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1258871'
original_report_id: '1258871'
title: Exposed Cortex API at https://cortex-ingest.shopifycloud.com/
weakness: Misconfiguration
team_handle: shopify
created_at: '2021-07-12T22:00:58.874Z'
disclosed_at: '2022-12-02T22:25:03.258Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 88
asset_identifier: '*.shopifycloud.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- misconfiguration
---

# Exposed Cortex API at https://cortex-ingest.shopifycloud.com/

## Metadata

- HackerOne Report ID: 1258871
- Weakness: Misconfiguration
- Program: shopify
- Disclosed At: 2022-12-02T22:25:03.258Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there, to be honest this is the first time I have seen this type of asset, but I think it is interesting/not supposed to be exposed. There is a Cortex metrics server running without authentication on https://cortex-ingest.shopifycloud.com/. This allows us to see the config for the server, call various Cortex APIs, and also exposes a Golang pprof debugger where we can see all the command-line arguments and DoS the server.

Example URLs:
* Cortex home: https://cortex-ingest.shopifycloud.com/
* Cortex config: https://cortex-ingest.shopifycloud.com/config
* Golang pprof home: https://cortex-ingest.shopifycloud.com/debug/pprof/
* Golang pprof cmdline: https://cortex-ingest.shopifycloud.com/debug/pprof/cmdline?debug=1

I see that the Cortex API offers many endpoints, some of which work and some of which do not: https://cortexmetrics.io/docs/api/#endpoints. I will take a look and see what impact I can find there.

## Impact

Information disclosure, no authentication

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
