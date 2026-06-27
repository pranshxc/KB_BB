---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1763266'
original_report_id: '1763266'
title: Public Github Repo Leaking Internal Credentials
team_handle: yelp
created_at: '2022-11-05T19:16:51.786Z'
disclosed_at: '2022-11-07T23:45:12.278Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 10
asset_identifier: '*.yelp.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Public Github Repo Leaking Internal Credentials

## Metadata

- HackerOne Report ID: 1763266
- Weakness: 
- Program: yelp
- Disclosed At: 2022-11-07T23:45:12.278Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
In Github I found some credentials to use in a mesos.apache.org 
Github:
https://github.com/Yelp/Tron/blob/master/yelp_package/itest_dockerfiles/mesos/mesos-secrets
https://github.com/Yelp/Tron/blob/master/yelp_package/itest_dockerfiles/mesos/mesos-slave-secret

## POC ss

{F2021070}
{F2021071}

Login documentation https://mesos.apache.org
https://mesos.apache.org/documentation/latest/authentication/

## Impact

Unauthorized account access  /information disclosure

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
