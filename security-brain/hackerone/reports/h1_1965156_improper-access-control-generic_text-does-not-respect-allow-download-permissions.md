---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1965156'
original_report_id: '1965156'
title: Text does not respect 'Allow download' permissions
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2023-04-28T09:52:05.911Z'
disclosed_at: '2023-08-23T14:55:38.293Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: nextcloud/text
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Text does not respect 'Allow download' permissions

## Metadata

- HackerOne Report ID: 1965156
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2023-08-23T14:55:38.293Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. user0 shares a folder of sensitive images to user1 without the 'Allow download' permission
2. user1 just creates a new text file and inserts the images into it
3. Voilla the images appear and can be downloaded easily

These are just previews but still.
For the most common types you can even request the raw image https://github.com/nextcloud/text/blob/main/lib/Controller/AttachmentController.php#L57-L67

## Impact

A user assume that the allow download feature works can still have their sensitive photos leaked.

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
