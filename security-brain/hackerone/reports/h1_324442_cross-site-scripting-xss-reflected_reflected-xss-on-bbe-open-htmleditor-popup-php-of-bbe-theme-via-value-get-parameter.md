---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '324442'
original_report_id: '324442'
title: Reflected XSS on bbe_open_htmleditor_popup.php of BBE Theme via "value"-GET-parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: localtapiola
created_at: '2018-03-11T15:49:03.943Z'
disclosed_at: '2018-04-09T21:32:45.849Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: www.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on bbe_open_htmleditor_popup.php of BBE Theme via "value"-GET-parameter

## Metadata

- HackerOne Report ID: 324442
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: localtapiola
- Disclosed At: 2018-04-09T21:32:45.849Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
The BBE Theme allows unauthorized access to bbe_open_htmleditor_popup.php which echoes unsanitized values of value-GET-parameter leading to reflected XSS. 

**Description:** 
The www.lahitapiolarahoitus.fi has Wordpress with theme BBE Theme v1.52. I did some code review and it seems that a file on the theme contains various problems:
- The following admin URL can be accessed without being logged in: https://www.lahitapiolarahoitus.fi/wp-content/themes/bbe/bbe-engine/assets/actions/bbe_open_htmleditor_popup.php
- The above page uses "value" GET-parameter and fails to sanitize the content.

By combining the above problems, an attacker can craft a URL which triggers an cross-site scripting attack on any user (unauthenticated/authenticated) who opens the URL crafted by the attacker.

**Impact:**
* Make admin-user run malicious javascript which will then be used to access other WP-Admin functionalities --> Remote code execution --> Possibly piivoting to other hosts.
* Make other users run malicious javascript.
* Show spoofed content which can be used in social engineering attacks (such as fake login pages, fake invoices, face contact details, fake announcements etc.).

## Browsers / Apps Verified In:

  * Firefox

## Steps To Reproduce:

  1. Navigate to the following URL: ```https://www.lahitapiolarahoitus.fi/wp-content/themes/bbe/bbe-engine/assets/actions/bbe_open_htmleditor_popup.php?value=%22a%27);//%3C/script%3E%3Cbody%20onload=alert(document.cookie)%3E``` and notice that the XSS triggered.

## Impact

* Make admin-user run malicious javascript which will then be used to access other WP-Admin functionalities --> Remote code execution --> Possibly piivoting to other hosts.
* Make other users run malicious javascript.
* Show spoofed content which can be used in social engineering attacks (such as fake login pages, fake invoices, face contact details, fake announcements etc.).

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
