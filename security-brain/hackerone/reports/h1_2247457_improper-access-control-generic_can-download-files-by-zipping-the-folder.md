---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2247457'
original_report_id: '2247457'
title: Can download files by zipping the folder
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2023-11-10T07:55:38.856Z'
disclosed_at: '2024-02-17T08:38:25.368Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 35
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Can download files by zipping the folder

## Metadata

- HackerOne Report ID: 2247457
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2024-02-17T08:38:25.368Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. Create folder and share it as view-only

{F2846936}

2. Access this folder with Testuser

{F2846943}


3. Go one level up and compress the whole folder

{F2846942}

4. The zip file can be downloaded and extracted locally

{F2846939}
{F2846941}


5. The folder itself can not be downloaded directly

{F2846937}

## Impact

Can download files without download permissions

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
