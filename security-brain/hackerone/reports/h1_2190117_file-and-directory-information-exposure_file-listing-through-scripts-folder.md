---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2190117'
original_report_id: '2190117'
title: File listing through scripts folder
weakness: File and Directory Information Exposure
team_handle: tennessee-valley-authority
created_at: '2023-10-02T18:52:44.480Z'
disclosed_at: '2024-02-09T12:12:41.419Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 40
asset_identifier: http://tvavirtual.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- file-and-directory-information-exposure
---

# File listing through scripts folder

## Metadata

- HackerOne Report ID: 2190117
- Weakness: File and Directory Information Exposure
- Program: tennessee-valley-authority
- Disclosed At: 2024-02-09T12:12:41.419Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
It's possible to list all hidden files that are located within the TVAVirtual.com Sharepoint folder structure.

## Steps To Reproduce:

1. Navigate to TvaVirtual.com
2. Open the pages source code and notice that its build using sharepoint pages.
3. Confirm that you see a listing for /SiteAssets/Scripts/js.cookie.min.js. Click on it to navigate to the page
4. Once https://tvavirtual.com/SiteAssets/Scripts/js.cookie.min.js loads, then remove js.cookie.min.js from the url
5. Confirm that TvaVirtual.com now shows the script folder listing on the page.
6. Remove the extra folder from the url to list the root folder at https://tvavirtual.com/SiteAssets/Forms/AllItems.aspx?RootFolder=
7. Navigate through the directory listing in an attempt to find sensitive files, enumerate publishing users and version history.

## Supporting Material/References:
I've attached jpgs showing what is available. You may see a login from bugs@tobiasdiehl.com where I was confirming cross tenant access to the files.

## Impact

Attackers can potentially enumerate sensitive information and files that would otherwise be protected

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
