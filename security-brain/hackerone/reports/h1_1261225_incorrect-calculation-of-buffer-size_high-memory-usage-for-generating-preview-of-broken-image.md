---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1261225'
original_report_id: '1261225'
title: High memory usage for generating preview of broken image
weakness: Incorrect Calculation of Buffer Size
team_handle: nextcloud
created_at: '2021-07-14T10:18:51.886Z'
disclosed_at: '2022-03-09T07:22:46.512Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- incorrect-calculation-of-buffer-size
---

# High memory usage for generating preview of broken image

## Metadata

- HackerOne Report ID: 1261225
- Weakness: Incorrect Calculation of Buffer Size
- Program: nextcloud
- Disclosed At: 2022-03-09T07:22:46.512Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When the attached file is uploaded and a preview is generated (e.g. in the folder overview of the files app), the PHP process allocates a very large amount of memory (on my machine it was shortly around 5 GByte)  and CPU.

Tested with latest master (1366b35081f1d92429787696f4175c19a602858a)  on Ubuntu 20.04 (php7.4-fpm). Option "memory_limit" is set to 512M.

## Impact

An attacker can cause a denial of service by uploading lots of such files which will cause the server to allocate too much memory / CPU.

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
