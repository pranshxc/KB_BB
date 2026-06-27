---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '298862'
original_report_id: '298862'
title: It's possible to view configuration and/or source code on uchat.awscorp.uberinternal.com
  without
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2017-12-17T00:36:48.078Z'
disclosed_at: '2017-12-26T11:02:58.464Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# It's possible to view configuration and/or source code on uchat.awscorp.uberinternal.com without

## Metadata

- HackerOne Report ID: 298862
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2017-12-26T11:02:58.464Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary
Configuration file and/or source code information leakage without Uber OneLogin SSO authentication.

## Security Impact
Misconfiguration on the server results in information leakage without authentication.

## Reproduction Steps
https://uchat.awscorp.uberinternal.com/static/main.740f5a0b92c00e72e2e1.js

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
