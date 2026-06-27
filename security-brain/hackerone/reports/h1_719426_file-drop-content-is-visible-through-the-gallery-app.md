---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '719426'
original_report_id: '719426'
title: File-drop content is visible through the gallery app
team_handle: nextcloud
created_at: '2019-10-21T22:54:00.915Z'
disclosed_at: '2020-01-31T10:36:24.922Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 68
asset_identifier: nextcloud/gallery
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# File-drop content is visible through the gallery app

## Metadata

- HackerOne Report ID: 719426
- Weakness: 
- Program: nextcloud
- Disclosed At: 2020-01-31T10:36:24.922Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I set up a file-drop on NC 17 (btw, according to https://nextcloud.com/security/ NC17 is not covered - but it should be once it's released!): created folder, set share as upload-only. I access that folder as https://cloud.domain.com/s/randompath - fine: I get the upload interface and cannot see what's in the folder. I (or anyone else) upload(s) something. Still fine. Now I use https://cloud.domain.com/apps/gallery/s/randompath and see everything that gallery can display. In my case, it was an upload folder for pictures, so everything is displayed (and can be downloaded, even if I set "hide download"!).

## Impact

Access all media files uploaded to a (not so secure) file-drop (https://nextcloud.com/file-drop/) folder. Could be critical in, say, a hospital, police, etc.

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
