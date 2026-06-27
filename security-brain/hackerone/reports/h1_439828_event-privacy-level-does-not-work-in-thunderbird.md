---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '439828'
original_report_id: '439828'
title: Event privacy level does not work in Thunderbird
team_handle: nextcloud
created_at: '2018-11-13T11:04:09.674Z'
disclosed_at: '2020-03-01T13:55:46.779Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: Desktop Client
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
---

# Event privacy level does not work in Thunderbird

## Metadata

- HackerOne Report ID: 439828
- Weakness: 
- Program: nextcloud
- Disclosed At: 2020-03-01T13:55:46.779Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Events in shared calendar with changed privacy level to any other than public are shown in Thunderbird as public anyway (with all details)
How to reproduce:
1 - create an event in user A's calendar shared to user B
2 - change privacy setting of this event to any other than public
3 - open Thunderbird as user B
4 - connect to user A's calendar
5 - behold the test event show as public with all details, not "Busy" brick for "show only busy"  or nothing for "private"

## Impact

Thunderbird user with read access can see all events with all details despite restrictions and thus can get some private info.

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
