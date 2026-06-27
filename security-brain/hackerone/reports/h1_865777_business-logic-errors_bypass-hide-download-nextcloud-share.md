---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '865777'
original_report_id: '865777'
title: Bypass hide download Nextcloud Share
weakness: Business Logic Errors
team_handle: nextcloud
created_at: '2020-05-04T14:12:42.165Z'
disclosed_at: '2020-10-05T10:41:01.211Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Bypass hide download Nextcloud Share

## Metadata

- HackerOne Report ID: 865777
- Weakness: Business Logic Errors
- Program: nextcloud
- Disclosed At: 2020-10-05T10:41:01.211Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary
Hello everyone, accidentally browsing through nextcloud, I have found a small vulnerability on nextcloud server. This vulnerability allow download the file when the download function has been hidden
Here is the error details.
If anything is wrong please respond to me. Thanks you.
## Description
I sharing folder for another ( download not hide)
{F814529}
{F814531}
Of course, the download function is still enabled, I will have the download request as below
{F814536}
I then disabled download on the entire file folder  
{F814542}
{F814546}
But the download link created on the server does not change or change the permissions, I can completely download the file to continue
{F814548}
{F814549}
{F814552}

## Platform(s) Affected:
Nextcloud Server

## Impact

Sensitive documents after sharing that do not allow downloading will be reloaded even if disabled, for anyone

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
