---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1516520'
original_report_id: '1516520'
title: Download full backup  [Mtn.co.rw]
team_handle: mtn_group
created_at: '2022-03-19T14:54:17.673Z'
disclosed_at: '2022-05-14T09:54:06.558Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
asset_identifier: mtn.co.rw
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Download full backup  [Mtn.co.rw]

## Metadata

- HackerOne Report ID: 1516520
- Weakness: 
- Program: mtn_group
- Disclosed At: 2022-05-14T09:54:06.558Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I discovered few critical vulnerabilities here, one of them is exposed backup files via directory listing.


## Steps To Reproduce:

go to https://mtn.co.rw/mtn.zip and download the file
extract the file and open
you will see the full backup of the website

## Similar report:
https://hackerone.com/reports/684838

## Impact

Source code & DB credentials leakage. Attacker can use it to compromise the resource.

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
