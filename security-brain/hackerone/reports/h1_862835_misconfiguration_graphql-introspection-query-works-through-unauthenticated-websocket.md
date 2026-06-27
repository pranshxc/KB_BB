---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '862835'
original_report_id: '862835'
title: GraphQL introspection query works through unauthenticated WebSocket
weakness: Misconfiguration
team_handle: nuri
created_at: '2020-04-29T21:02:01.389Z'
disclosed_at: '2021-01-09T08:49:03.025Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: api.app.bitwala.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- misconfiguration
---

# GraphQL introspection query works through unauthenticated WebSocket

## Metadata

- HackerOne Report ID: 862835
- Weakness: Misconfiguration
- Program: nuri
- Disclosed At: 2021-01-09T08:49:03.025Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
It is possible to execute GraphQL introspection query through unauthenticated WebSocket connection. PoC included.

## Steps To Reproduce:
To simplify reproducing I provided a simple html PoC file.

  1. Start python static http server in directory with poc file: `python3 -m http.server` (this step is required to bypass CORS restrictions for opening local file in the browser)
  1. Open file in the browser: http://localhost:8000/ws.html
  1. GraphQL schema dump will be displayed on the page

The problem occurs because of the websocket request with type `start`(maybe others too, I didn't check) allows to pass introspection query in it (`{type: "start", payload: {query: "query IntrospectionQuery{ ... }"}}`)

## Supporting Material/References:

  * [GraphQL — Common vulnerabilities & how to exploit them](https://medium.com/@the.bilal.rizwan/graphql-common-vulnerabilities-how-to-exploit-them-464f9fdce696)

## Impact

This information reveals the full GraphQL API with all methods and data types. This can be used to perform more complex attacks.

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
