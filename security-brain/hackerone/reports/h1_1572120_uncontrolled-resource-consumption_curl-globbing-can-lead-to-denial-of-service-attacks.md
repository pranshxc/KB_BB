---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1572120'
original_report_id: '1572120'
title: curl "globbing" can lead to denial of service attacks
weakness: Uncontrolled Resource Consumption
team_handle: curl
created_at: '2022-05-16T15:19:36.811Z'
disclosed_at: '2022-06-16T15:14:32.454Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# curl "globbing" can lead to denial of service attacks

## Metadata

- HackerOne Report ID: 1572120
- Weakness: Uncontrolled Resource Consumption
- Program: curl
- Disclosed At: 2022-06-16T15:14:32.454Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
[add summary of the vulnerability]

The curl "globbing" allows too much scope, which can cause the server to be denied service or used to attack third-party websites. The globbing allow [1-9999999999999999999] to parse in the url. So when curl request for 'http://127.0.0.1/[1-9999999999999999999]', the can cause 300 requests in the server.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Listen 8000 port: python -m SimpleHTTPServer 8000
  2.  command: nohup ./curl -vv 'http://127.0.0.1:8000/[1-9999999999999999999]/' &
  3. Check the server resource process. There are a lot of network requests and CPU consumption. 

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

With this function, the resources of the server running curl request can be excessively consumed or a large number of URL accesses to other websites can be initiated, resulting in denial of service.

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
