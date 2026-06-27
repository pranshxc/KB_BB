---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1183302'
original_report_id: '1183302'
title: Default Nextcloud allows http federated shares
team_handle: nextcloud
created_at: '2021-05-03T21:13:30.007Z'
disclosed_at: '2021-05-11T11:38:49.919Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Default Nextcloud allows http federated shares

## Metadata

- HackerOne Report ID: 1183302
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-05-11T11:38:49.919Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

1. userA on serverA runs on http only
2. userA sends a federated share to userB on serverB
3. userB is a normal user so he has no clue that there is no secure transport used and accepts the share
4. all the data written to and read from is now no longer protected by TLS

## Impact

While maybe a bit far fetched. But this would allow for man in the middle attacks. Nextcloud just seems to allow plain http communication by default.
It is in my opinion not sensible at all to expect end users to know the difference here.

I propose:

1. Allow only https by default (certificates are easy and cheap these days)
2. If it is for local debugging then only allow http when debugging
3. If really needed for some edge case make this explicit opt in in config.php

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
