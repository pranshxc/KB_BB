---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '761158'
original_report_id: '761158'
title: SharePoint exposed web services in a  subdomain
weakness: Improper Access Control - Generic
team_handle: mtn_group
created_at: '2019-12-18T17:46:39.674Z'
disclosed_at: '2020-05-16T13:06:35.089Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 27
asset_identifier: mtn.co.za
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# SharePoint exposed web services in a  subdomain

## Metadata

- HackerOne Report ID: 761158
- Weakness: Improper Access Control - Generic
- Program: mtn_group
- Disclosed At: 2020-05-16T13:06:35.089Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there
I found a subdomain that is sharepoint configuration is poorly implemented
Because of improper configuration an anonymous user can access to the SharePoint Web Services.

POC:
Go to the following url:
https://www.mtn.co.za/_vti_bin/lists.asmx?WSDL

services.jpg

Remediation
Restrict access to this page.

References:
https://www.acunetix.com/vulnerabilities/web/vulnerability/sharepoint-exposed-web-services/
https://blogs.msdn.microsoft.com/fabdulwahab/2015/08/15/security-protecting-sharepoint-server-applications/

Best Regards Miguel Santareno

## Impact

Attackers can know the full structure off the application.

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
