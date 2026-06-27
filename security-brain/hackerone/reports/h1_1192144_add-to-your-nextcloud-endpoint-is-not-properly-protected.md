---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1192144'
original_report_id: '1192144'
title: Add to your nextcloud endpoint is not properly protected
team_handle: nextcloud
created_at: '2021-05-11T13:56:27.016Z'
disclosed_at: '2021-08-11T09:24:19.106Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Add to your nextcloud endpoint is not properly protected

## Metadata

- HackerOne Report ID: 1192144
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-08-11T09:24:19.106Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This is related to https://hackerone.com/reports/1173684

The endpoint you hit does have bruteforce protection
https://github.com/nextcloud/server/blob/master/apps/federatedfilesharing/lib/Controller/MountPublicLinkController.php#L126

But this is only triggered by finding a share that is password protected
https://github.com/nextcloud/server/blob/master/apps/federatedfilesharing/lib/Controller/MountPublicLinkController.php#L157

Or a file drop public share
https://github.com/nextcloud/server/blob/master/apps/federatedfilesharing/lib/Controller/MountPublicLinkController.php#L166

In other words this endpoint can also be used to try to brute force share tokens.

## Impact

Low just like on the other report. But should be fixed non the less.

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
