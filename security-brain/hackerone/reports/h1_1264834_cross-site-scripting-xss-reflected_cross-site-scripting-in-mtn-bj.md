---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1264834'
original_report_id: '1264834'
title: 'cross site scripting in : mtn.bj'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2021-07-16T00:56:05.488Z'
disclosed_at: '2022-08-06T11:19:10.472Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: mtn.bj
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# cross site scripting in : mtn.bj

## Metadata

- HackerOne Report ID: 1264834
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2022-08-06T11:19:10.472Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Xss vulnerability in mtn.bj  in file name 

## Steps To Reproduce:


  1.Go to : 
https://www.mtn.bj/business/ressources/formulaires/plan-de-localisation-de-compte/?next=https://www.mtn.bj/business/ressources/formulaires/formulaire-de-souscription/
  2 - fill all inputs with any data 
3 - in file upload upload a file with payload file name such as : "><img src=x onerror=alert(document.cookie);.jpg

4-the payload will executed in the page .

## Supporting Material/References:
1 - video showing poc 
2 - screen shot

## Impact

execute malicious java script in user browser

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
