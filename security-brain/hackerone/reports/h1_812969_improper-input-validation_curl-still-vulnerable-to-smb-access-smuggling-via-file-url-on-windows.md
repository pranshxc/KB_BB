---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '812969'
original_report_id: '812969'
title: curl still vulnerable to SMB access smuggling via FILE URL on Windows
weakness: Improper Input Validation
team_handle: curl
created_at: '2020-03-08T01:06:41.661Z'
disclosed_at: '2021-01-08T14:16:03.527Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# curl still vulnerable to SMB access smuggling via FILE URL on Windows

## Metadata

- HackerOne Report ID: 812969
- Weakness: Improper Input Validation
- Program: curl
- Disclosed At: 2021-01-08T14:16:03.527Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
The released fix for CVE-2019-15601, SMB access smuggling via FILE URL on Windows, leaves curl still vulnerable to SMB access smuggling via FILE URLs.
 - FILE URLs formatted as `file:////smb_server/smb_share/file` are not filtered.
 - FILE URLs which point to the global DOS name space, \??\, and formatted as `file:///%3f%3f/UNC/smb_server/smb_share/file_name` or `file:///%3f%3f/GLOBAL/UNC/smb_server/smb_share/file` are not filtered.

## Steps To Reproduce:

  1. `curl file:////localhost/c$/windows/win.ini`
  2. `curl file:///%3f%3f/UNC/localhost/c$/windows/win.ini`
  3. `curl file:///%3f%3f/GLOBAL/UNC/localhost/c$/windows/win.ini`

The above examples will return the contents of C:\Windows\win.ini utilizing SMB to fetch the file via the local administrative share for the C drive. This will also work with remote shares.

## Impact

A properly crafted URL could cause a user to unknowingly access a remote file.

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
