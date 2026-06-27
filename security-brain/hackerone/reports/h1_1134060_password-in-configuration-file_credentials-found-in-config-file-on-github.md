---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1134060'
original_report_id: '1134060'
title: credentials found in config file on github
weakness: Password in Configuration File
team_handle: blockfi
created_at: '2021-03-24T12:40:57.158Z'
disclosed_at: '2021-04-28T16:32:58.019Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 46
asset_identifier: '*.blockfi.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- password-in-configuration-file
---

# credentials found in config file on github

## Metadata

- HackerOne Report ID: 1134060
- Weakness: Password in Configuration File
- Program: blockfi
- Disclosed At: 2021-04-28T16:32:58.019Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hi, credentials belonging to blockfi.com was found exposed on github, these credentials can lead to attackers gaining access into the network and stealing information and destroying servers

## Steps To Reproduce:

https://github.com/paw2py/ETH_API/blob/8658c39d1742f07ac7b5f0e41b82ad164f3ba099/config.py

https://github.com/naboagye-blockfi/ecs-pipeline/blob/38b1417d4dfff624eb6f649d27256758f395aa65/COPY/prometheus/prometheus.yml

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

these credentials can lead to attackers gaining access into the network and stealing information and destroying servers

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
