---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1167958'
original_report_id: '1167958'
title: Nextcloud deck sharee search leaks searches to lookupserver by default
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2021-04-18T20:17:32.028Z'
disclosed_at: '2021-05-26T10:01:52.352Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud/deck
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Nextcloud deck sharee search leaks searches to lookupserver by default

## Metadata

- HackerOne Report ID: 1167958
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2021-05-26T10:01:52.352Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

So, in short this is related to the other 2 reports https://hackerone.com/reports/1167916 and https://hackerone.com/reports/1167919

While I could not find deck on your h1 page. I kind of assume it is in scope as well as this is something you sell with the 'groupware' subscription (
https://nextcloud.com/groupware/ ).

In short. In the default setup if you search for people to share a deck board with the query will be send to the lookup server. Which the user is not told about.

## Impact

See the other reports.

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
