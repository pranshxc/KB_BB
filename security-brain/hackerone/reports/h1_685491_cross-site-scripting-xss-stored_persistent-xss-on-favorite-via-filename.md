---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '685491'
original_report_id: '685491'
title: Persistent XSS on favorite via filename
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nextcloud
created_at: '2019-08-31T11:38:01.777Z'
disclosed_at: '2019-12-12T09:42:51.382Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Persistent XSS on favorite via filename

## Metadata

- HackerOne Report ID: 685491
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nextcloud
- Disclosed At: 2019-12-12T09:42:51.382Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

CVSS
----

Medium 6.4 [CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N)

Description
-----------

The name of a file is echoed without encoding when favoring the file, leading to persistent XSS. 

POC
---

To place the payload:

- Create a file called `test'"><img src=x onerror=alert(document.location)>.pdf` and upload it. 

To trigger the payload:

- click on ... next to the file followed by "add to favorites". The payload will trigger here.

## Impact

With a successful attack, an attacker can access all data the attacked user has access to, as well as perform arbitrary requests in the name of the attacked user.

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
