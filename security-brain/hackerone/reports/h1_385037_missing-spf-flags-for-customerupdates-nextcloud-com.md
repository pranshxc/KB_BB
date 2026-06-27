---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '385037'
original_report_id: '385037'
title: Missing SPF flags for customerupdates.nextcloud.com
team_handle: nextcloud
created_at: '2018-07-21T20:20:57.651Z'
disclosed_at: '2020-03-01T13:56:05.848Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: customerupdates.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Missing SPF flags for customerupdates.nextcloud.com

## Metadata

- HackerOne Report ID: 385037
- Weakness: 
- Program: nextcloud
- Disclosed At: 2020-03-01T13:56:05.848Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey,

I just checked for SPF records for the customerupdates.nextcloud.com domain, and there are none. The fake message reaches the inbox from this domain. Not spam.

 You can validate by testing yourself here: http://www.kitterman.com/spf/validate.html

This subdomain too: update.nextcloud.com

## Impact

Attacker could send fake email.

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
