---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1745766'
original_report_id: '1745766'
title: Disabled download shares still allow download through preview images
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2022-10-21T13:59:15.382Z'
disclosed_at: '2022-12-31T09:33:06.093Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Disabled download shares still allow download through preview images

## Metadata

- HackerOne Report ID: 1745766
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2022-12-31T09:33:06.093Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

## Steps To Reproduce:

  1. Share a folder and disable the "Allow download" permission
  2. Now as the recipient of the file you can still download the preview of the file

This is an issue for images but also for shared documents where viewing them in Collabora would present them watermarked but the preview would leak the first page without an watermark.

## Impact

Images could be downloaded and previews of documents (first page) can be downloaded without being watermarked.

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
