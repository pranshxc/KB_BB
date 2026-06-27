---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '794144'
original_report_id: '794144'
title: Open redirection bypass in /www/admin/campaign-modify.php
weakness: Open Redirect
team_handle: revive_adserver
created_at: '2020-02-12T06:20:31.895Z'
disclosed_at: '2020-03-12T12:54:37.811Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirection bypass in /www/admin/campaign-modify.php

## Metadata

- HackerOne Report ID: 794144
- Weakness: Open Redirect
- Program: revive_adserver
- Disclosed At: 2020-03-12T12:54:37.811Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

### Description
- There is an open redirect on /www/admin/campaign-modify.php?return_url= {F713773}
- By using //// at the start of the link, you can bypass the open redirect filter.

- example: `/www/admin/campaign-modify.php?clientid=&campaignid=&returnurl=%2F%2F%2F%2Fhackerone.com`

## Impact

This vulnerability can be used for phishing attacks

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
