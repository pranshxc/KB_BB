---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '746541'
original_report_id: '746541'
title: SSRF on local storage of iOS mobile
weakness: Server-Side Request Forgery (SSRF)
team_handle: nextcloud
created_at: '2019-11-26T10:37:16.194Z'
disclosed_at: '2020-03-01T10:29:39.050Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: it.twsweb.Nextcloud
asset_type: APPLE_STORE_APP_ID
max_severity: medium
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF on local storage of iOS mobile

## Metadata

- HackerOne Report ID: 746541
- Weakness: Server-Side Request Forgery (SSRF)
- Program: nextcloud
- Disclosed At: 2020-03-01T10:29:39.050Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. The tester uploaded the text file, containing "test ssrf" message, in order to proof SSRF attack.
2. Next, the tester uploaded the common file and then manipulate the content and extension file to html format in order to find the application path: <svg/onload=document.write(document.location)> 
3. The tester access that file and found the application path to use for SSRF local file disclosure.
4. Then, the tester uploaded the common file and then manipulate the content and extension file to html format in order to view the local file via SSRF attack: <iframe src="file://.../ssrfpoc.txt" width="400" height="400"></iframe> 
5. The tester access that file and found that this application allow you to access and read the local file successfully.

## Impact

This allow anyone to use other URLs such as that can access documents on the system/application (using file://) a.k.a Sensitive Data Exposure.

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
