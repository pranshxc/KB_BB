---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1688199'
original_report_id: '1688199'
title: Database resource exhaustion for logged-in users via sharee recommendations
  with circles
weakness: Uncontrolled Resource Consumption
team_handle: nextcloud
created_at: '2022-08-31T21:12:53.497Z'
disclosed_at: '2022-11-26T06:52:11.016Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: nextcloud/circles
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Database resource exhaustion for logged-in users via sharee recommendations with circles

## Metadata

- HackerOne Report ID: 1688199
- Weakness: Uncontrolled Resource Consumption
- Program: nextcloud
- Disclosed At: 2022-11-26T06:52:11.016Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Registered users can generate massive database load 

## Steps To Reproduce:

  1. create 9 circles and 6 folders (circles * folder > 50)
  2. share all created folders with all created circles
  3. open an other folder and open the share tab, so the URI /ocs/v2.php/apps/files_sharing/api/v1/sharees_recommended is requested
  4. this requests results in a loop that runs as long as the php value max_execution_time is set; the recommended value for this is 3600 seconds (1h)
  5. a small number of these requests will stress even large servers

Tested with Nextcloud 23.0.8

## Impact

Attacker slow down the system by generating a lot of database/cpu load.

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
