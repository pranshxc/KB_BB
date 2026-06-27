---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '291750'
original_report_id: '291750'
title: Link filter protection bypass
weakness: Open Redirect
team_handle: valve
created_at: '2017-11-19T21:27:22.907Z'
disclosed_at: '2018-05-09T22:24:05.700Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 53
asset_identifier: steamcommunity.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Link filter protection bypass

## Metadata

- HackerOne Report ID: 291750
- Weakness: Open Redirect
- Program: valve
- Disclosed At: 2018-05-09T22:24:05.700Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description
Hi, there is a protection bypass in the linkfilter function. By using the character 。 (%E3%80%82 url encoded) instead of a normal dot in urls, it is possible to bypass the blocking.

## PoC
Normal request : https://steamcommunity.com/linkfilter/?url=pornhub.com

{F240919}

Bypass : https://steamcommunity.com/linkfilter/?url=pornhub%E3%80%82com

{F240920}

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
