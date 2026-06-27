---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1264832'
original_report_id: '1264832'
title: 'Reflected Cross-Site scripting in : mtn.bj'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2021-07-16T00:42:21.271Z'
disclosed_at: '2021-09-26T12:59:03.117Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
asset_identifier: mtn.bj
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected Cross-Site scripting in : mtn.bj

## Metadata

- HackerOne Report ID: 1264832
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2021-09-26T12:59:03.117Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team 
I have found a Reflected XSS vulnerability in mtn.jb by file name 


## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. go to : 
████
  2. enter any email and press  Suivant
  3. fill all the inputs by any data .
  4. in file upload upload any photo with payload file name : "><img src=x onerror=alert(document.cookie);.jpg

  5 . the payload executed in the page  


Supporting Material/References:
1 - video showing poc 
2 - screenshot

## Impact

An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page

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
