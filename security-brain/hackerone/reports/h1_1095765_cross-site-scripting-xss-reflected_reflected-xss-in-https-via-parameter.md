---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1095765'
original_report_id: '1095765'
title: Reflected XSS in https://██████████ via "████████" parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-02-04T20:54:26.938Z'
disclosed_at: '2021-04-02T18:48:31.884Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in https://██████████ via "████████" parameter

## Metadata

- HackerOne Report ID: 1095765
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-04-02T18:48:31.884Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Security Team,
I would like to report the XSS vulnerability on your system.
The `██████████` parameter is not escaped properly for URL encoded values.

██████

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim, or for phishing attacks.

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit the following POC link:
https://█████████/█████████CE399%22%3E%3C/script%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E&int_crse_eff_acad_yr=2002&int_crse_eff_term=4&sbjct_srch=true&sbjct_txt=the

## Suggested Mitigation/Remediation Actions
Sanitize the input on that parameter

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
