---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '298990'
original_report_id: '298990'
title: Configuration and/or source code files on uchat-staging.uberinternal.com can
  be viewed without OneLogin SSO Authentication
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2017-12-17T22:29:41.572Z'
disclosed_at: '2017-12-26T11:03:14.669Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Configuration and/or source code files on uchat-staging.uberinternal.com can be viewed without OneLogin SSO Authentication

## Metadata

- HackerOne Report ID: 298990
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2017-12-26T11:03:14.669Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary
Configuration file and/or source code information leakage without Uber OneLogin SSO authentication.

## Security Impact
Misconfiguration on the server results in information leakage without authentication.

## Reproduction Steps
https://uchat-staging.uberinternal.com/static/main.740f5a0b92c00e72e2e1.js

## Specifics
* http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-2169
* http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-0202
* https://www.owasp.org/index.php/Testing_for_Local_File_Inclusion

## Impact

Access to internal configuration files, system names, and source code.

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
