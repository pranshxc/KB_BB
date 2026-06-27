---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '437863'
original_report_id: '437863'
title: SVG file that HTML Included is able to upload via File Manager
weakness: Cross-site Scripting (XSS) - Stored
team_handle: concretecms
created_at: '2018-11-09T08:44:33.319Z'
disclosed_at: '2019-04-20T05:49:28.258Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 26
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# SVG file that HTML Included is able to upload via File Manager

## Metadata

- HackerOne Report ID: 437863
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: concretecms
- Disclosed At: 2019-04-20T05:49:28.258Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Concrete5 has the whitelist for restricting that malicious file is uploaded.
( concrete/config/concrete.php, Line no. 86~88 )

The extension whitelist allows to upload SVG file.

However, SVG can has the HTML elements in its code.
(Ref. https://www.w3.org/TR/SVG2/intro.html#W3CCompatibility )

If web browser accesses the SVG file that has the 'script' tag of HTML element  directly,
browser executes the JavaScript placed in SVG file.

Example SVG file likes below.
```
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 105">
<html><head><title>test</title></head><body><script>alert('xss');</script></body></html>
</svg>
```
It can be occur the XSS vulnerability.


* Test Scenario

1. Make the SVG
{F373015}

2. Login as administrator and select the File Manager feature.

3. Upload the file we made.
{F373008}

4. We can check the upload path in "Right click -> Properties"
{F373009}

5. For the test to triggering SVG file, we edit portfolio section.
Move to "portfolio > project Title #" and Edit / Add slides like this.
{F373010}

6. We can confirmed the execution of JavaScript in the SVG file.
{F373011}

Thank you for reading my report.

PS.
When I was the kid, My father gave me the crayon as the Christmas gift.

## Impact

Concrete5 prohibited  the upload the HTML files, but this method is bypass the file upload filtering.
Attacker who got the administrator authority can inject and hide malicious html tags to target service.

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
