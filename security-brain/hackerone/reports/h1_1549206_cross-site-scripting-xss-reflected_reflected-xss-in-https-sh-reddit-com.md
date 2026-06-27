---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1549206'
original_report_id: '1549206'
title: Reflected xss in https://sh.reddit.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: reddit
created_at: '2022-04-24T06:11:22.366Z'
disclosed_at: '2022-05-08T07:36:43.558Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 143
asset_identifier: sh.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected xss in https://sh.reddit.com

## Metadata

- HackerOne Report ID: 1549206
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: reddit
- Disclosed At: 2022-05-08T07:36:43.558Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Reflected cross-site scripting (or XSS) arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.

## Impact:
attacker can execute malicious java script and steal cookies 

## Steps To Reproduce:
[add details for how we can reproduce the issue]

Hi team ,

Navigate to below url 
scroll to page end find a option see more
Move mouse over there and observe the execution of javascript 
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

attacker can execute malicious java script and steal cookies

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
