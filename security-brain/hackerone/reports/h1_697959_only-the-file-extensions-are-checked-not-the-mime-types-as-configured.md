---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '697959'
original_report_id: '697959'
title: Only the file extensions are checked, not the MIME types as configured
team_handle: nextcloud
created_at: '2019-09-19T16:29:18.610Z'
disclosed_at: '2020-03-14T10:10:41.596Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: nextcloud/files_accesscontrol
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Only the file extensions are checked, not the MIME types as configured

## Metadata

- HackerOne Report ID: 697959
- Weakness: 
- Program: nextcloud
- Disclosed At: 2020-03-14T10:10:41.596Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The tool is not working as hoped. File access control speaks of MIME types that are blocked or not blocked. In fact, only the file extensions are checked. If a user renames an unauthorized file to an allowed file, he can upload and download it. The MIME type of the current file is insignificant, only the file extension is checked. 

A company administrator prohibits the upload of exe files using file access control and MIME types. One user 
copies his remote access application as a txt file to Nextcloud and downloads it in his professional environment.

A user on github has created a patch that has not yet found its way into the public repository.

## Impact

An attacker could upload malicious files that have been blocked by the administrator.

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
