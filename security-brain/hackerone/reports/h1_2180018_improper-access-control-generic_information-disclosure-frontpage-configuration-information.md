---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2180018'
original_report_id: '2180018'
title: Information Disclosure FrontPage Configuration Information
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2023-09-25T17:08:26.024Z'
disclosed_at: '2023-10-20T17:14:08.467Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- improper-access-control-generic
---

# Information Disclosure FrontPage Configuration Information

## Metadata

- HackerOne Report ID: 2180018
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2023-10-20T17:14:08.467Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there i found a information disclosure Microsoft FrontPage configuration in the subdomain ██████████hat allows me to see version number and scripting paths off sharepoint using firefox.

POC:
Go to the following url:
https://███████/_vti_inf.html
and you will see the code

<!-- FrontPage Configuration Information 
FPVersion="16.00.0.000"
FPShtmlScriptUrl="_vti_bin/shtml.dll/_vti_rpc"
FPAuthorScriptUrl="_vti_bin/_vti_aut/author.dll"
FPAdminScriptUrl="_vti_bin/_vti_adm/admin.dll"
TPScriptUrl="_vti_bin/owssvr.dll"
-->
██████████

For more detailed information please check the References section first link.

## References
https://fortiguard.com/encyclopedia/ips/103284772
https://blogs.msdn.microsoft.com/fabdulwahab/2015/08/15/security-protecting-sharepoint-server-applications/

## Impact

Attackers can know the version and scripting paths information of Sharepoint FrontPage Configuration.

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Just follow the URL provided

## Suggested Mitigation/Remediation Actions

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
