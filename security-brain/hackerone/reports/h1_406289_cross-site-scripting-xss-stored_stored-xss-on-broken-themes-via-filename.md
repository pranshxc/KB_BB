---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '406289'
original_report_id: '406289'
title: Stored XSS on Broken Themes via filename
weakness: Cross-site Scripting (XSS) - Stored
team_handle: wordpress
created_at: '2018-09-06T06:37:59.749Z'
disclosed_at: '2020-08-25T15:56:24.873Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: WordPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on Broken Themes via filename

## Metadata

- HackerOne Report ID: 406289
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: wordpress
- Disclosed At: 2020-08-25T15:56:24.873Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, I've found something here, 

##Description 
XSS Stored because filename of theme when broken, So when theme is broken, Wordpress will inform the name of  theme who has been broken which is the folder name of  theme and inform the error with description message.

{F342862}

Looks like the filename is reflected, on the `Name` of the detail broken themes. I try to rename the folder to malicious name ( payload : <img src=x onerror=alert(1)> ) and the payload it'll be execute.

{F342863}

##POC
1. Upload theme
1. Delete the style.css ( or you can make new folder on theme path with payload name )
1.  Rename the folder to `<img src=x onerror=alert(1)>` 
1. See theme page. 

##Video 
https://youtu.be/IuJrcR_BoKo

## Impact

XSS will be execute , because the filename is stored on page without any filter, and this is possible to make stored XSS.

It'll be good to filter / encoding the illegal character, like wordpress do on themes upload.

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
