---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '767066'
original_report_id: '767066'
title: Information Disclosure Microsoft IIS Server service.cnf in a mtn website
weakness: Information Disclosure
team_handle: mtn_group
created_at: '2020-01-02T09:34:18.586Z'
disclosed_at: '2020-04-03T11:58:12.770Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: mtn.co.za
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information Disclosure Microsoft IIS Server service.cnf in a mtn website

## Metadata

- HackerOne Report ID: 767066
- Weakness: Information Disclosure
- Program: mtn_group
- Disclosed At: 2020-04-03T11:58:12.770Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there i found a information disclosure Microsoft IIS Server service.cnf file in the website https://www.mtn.co.za/ using firefox.

In the following steps i will demonstrate how to reproduce the vulnerability.

POC:
1ºGo to the following url:
https://www.mtn.co.za/_vti_pvt/service.cnf

you will see:
vti_encoding:SR|utf8-nl
vti_extenderversion:SR|15.0.0.5179

service.jpg

Remediation:
Remove the service.cnf file from the web server or restrict access to this file.

Example:
For more detailed information please check the References section first link.

References:
https://www.acunetix.com/vulnerabilities/web/vulnerability/microsoft-iis-server-service-cnf-file-found/
https://blogs.msdn.microsoft.com/fabdulwahab/2015/08/15/security-protecting-sharepoint-server-applications/

Best Regards Miguel Santareno

## Impact

Attackers can read /_vti_pvt/service.cnf and gather more information about the system

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
