---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '761617'
original_report_id: '761617'
title: Information Disclosure FrontPage Configuration Information /_vti_inf.html in
  https://www.mtn.co.za/
weakness: Improper Access Control - Generic
team_handle: mtn_group
created_at: '2019-12-19T11:03:44.896Z'
disclosed_at: '2020-04-03T11:57:50.369Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: mtn.co.za
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Information Disclosure FrontPage Configuration Information /_vti_inf.html in https://www.mtn.co.za/

## Metadata

- HackerOne Report ID: 761617
- Weakness: Improper Access Control - Generic
- Program: mtn_group
- Disclosed At: 2020-04-03T11:57:50.369Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there i found a information disclosure Microsoft FrontPage configuration in the subdomain https://www.mtn.co.za/ that allows me to see version number and scripting paths off sharepoint using firefox.

POC:
Go to the following url:
https://www.mtn.co.za/_vti_inf.html and you will see a blank page.

blank.jpg

Then just go to view-source:https://www.mtn.co.za/_vti_inf.html all you will be able to see the FrontPage Configuration Information:

<!-- FrontPage Configuration Information 
FPVersion="15.00.0.000"
FPShtmlScriptUrl="_vti_bin/shtml.dll/_vti_rpc"
FPAuthorScriptUrl="_vti_bin/_vti_aut/author.dll"
FPAdminScriptUrl="_vti_bin/_vti_adm/admin.dll"
TPScriptUrl="_vti_bin/owssvr.dll"
-->


sharepoint.jpg

Remediation:
Remove the /_vti_inf.html file from the web server or restrict access to this file.

Example:
For more detailed information please check the References section first link.

References:
https://fortiguard.com/encyclopedia/ips/103284772
https://blogs.msdn.microsoft.com/fabdulwahab/2015/08/15/security-protecting-sharepoint-server-applications/

Best Regards Miguel Santareno

## Impact

Attackers can know the version and scripting paths information of Sharepoint FrontPage Configuration.

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
