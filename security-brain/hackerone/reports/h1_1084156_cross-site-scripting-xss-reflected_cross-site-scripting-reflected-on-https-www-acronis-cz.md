---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1084156'
original_report_id: '1084156'
title: Cross Site Scripting (Reflected) on https://www.acronis.cz/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: acronis
created_at: '2021-01-22T07:48:16.525Z'
disclosed_at: '2021-11-17T10:00:49.225Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Cross Site Scripting (Reflected) on https://www.acronis.cz/

## Metadata

- HackerOne Report ID: 1084156
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: acronis
- Disclosed At: 2021-11-17T10:00:49.225Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
You can post javascript and html code in form fields

steps :
1-go to vulnerability link : https://www.acronis.cz/poptavka-acronis/
2- enter this javascript code "><script>alert(1);</script> in form field for xss and enter <a+href="https://bing.com">Test</a> for html injection.

## Impact

Impact
1- Cookie stealing
2- Pishing attacks
3- URL redirection

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
