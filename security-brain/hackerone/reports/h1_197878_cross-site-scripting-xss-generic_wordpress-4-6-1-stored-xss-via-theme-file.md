---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '197878'
original_report_id: '197878'
title: WordPress <= 4.6.1 Stored XSS Via Theme File
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2017-01-12T16:46:19.823Z'
disclosed_at: '2017-01-13T02:43:57.000Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# WordPress <= 4.6.1 Stored XSS Via Theme File

## Metadata

- HackerOne Report ID: 197878
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2017-01-13T02:43:57.000Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello __Team__,

__Description__:-
>Vulnerable code is located at /wp-admin/includes/class-theme-installer-skin.php

__POC__:-
https://nextcloud.com/readme.html

{F151887}



__FIX__:-
Upgrade wordpress to latest


__Refer__:-
>https://wpvulndb.com/vulnerabilities/8718
>https://www.mehmetince.net/low-severity-wordpress/

__Attack Scenario__:-
1 – Attacker uploads a theme as a zip file.
2 – Webmaster who just want to download a theme and then upload, takes a theme file.
3 – And upload it without verify content of zip file.


__Regards__,
Santhosh

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
