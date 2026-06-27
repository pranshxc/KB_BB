---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1806223'
original_report_id: '1806223'
title: Reference fetch can saturate the server bandwidth for 10 seconds
weakness: Uncontrolled Resource Consumption
team_handle: nextcloud
created_at: '2022-12-15T09:44:50.560Z'
disclosed_at: '2023-04-29T08:12:58.786Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Reference fetch can saturate the server bandwidth for 10 seconds

## Metadata

- HackerOne Report ID: 1806223
- Weakness: Uncontrolled Resource Consumption
- Program: nextcloud
- Disclosed At: 2023-04-29T08:12:58.786Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
When posting a message on talk, a reference is fetched for any link in the message
There is a hardcoded mandatory 10sec timeout. But the ressource is still fetched for those entire 10 seconds.

For high-bandwidth servers, this can result in disk space being temporarily filled and saturate the server bandwidth.
Tested on my 2.5gbps network, I was easily able to find 10GB ressources online that have higher network speed and fully saturate the netwrok for a few seconds and a few messages.

## Steps To Reproduce:

  1. Open a talk room
  1. Post multiple messages containing a link to a high availability ressource like https://speed.hetzner.de/10GB.bin

## Impact

Can severly impact server performances and/or lead to a denial of service

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
