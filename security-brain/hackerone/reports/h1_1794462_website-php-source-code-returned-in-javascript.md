---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1794462'
original_report_id: '1794462'
title: Website PHP source code returned in javascript
team_handle: nextcloud
created_at: '2022-12-06T04:51:12.555Z'
disclosed_at: '2023-04-10T12:46:08.650Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Website PHP source code returned in javascript

## Metadata

- HackerOne Report ID: 1794462
- Weakness: 
- Program: nextcloud
- Disclosed At: 2023-04-10T12:46:08.650Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Source code disclosure:
----------------------------------



Summary:
--------------------

Severity             : Low
Confidence      : Tentative
Host                      : https://nextcloud.com
Path                       : /wp-content/themes/theme-package/dist/js/main.js


Issue detail:
------------------------------------
The application appears to disclose some server-side source code written in PHP.

Issue background:
---------------------------------------

Source code intended to be kept server-side can sometimes end up being disclosed to users. Such code may contain sensitive information such as database passwords and secret keys, which may help malicious users formulate attacks against the application.



Issue remediation:
---------------------------------

Server-side source code is normally disclosed to clients as a result of typographical errors in scripts or because of misconfiguration, such as failing to grant executable permissions to a script or directory. Review the cause of the code disclosure and prevent it from happening.


References:
--------------------------------------

Web Security Academy: Information disclosure

Vulnerability classifications:
------------------------------------------

    CWE-18: Source Code
    CWE-200: Information Exposure
    CWE-388: Error Handling
    CWE-540: Information Exposure Through Source Code
    CWE-541: Information Exposure Through Include Source Code
    CWE-615: Information Exposure Through Comments
    CAPEC-37: Retrieve Embedded Sensitive Data

## Impact

Source code intended to be kept server-side can sometimes end up being disclosed to users. Such code may contain sensitive information such as database passwords and secret keys, which may help malicious users formulate attacks against the application.

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
