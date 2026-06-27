---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1212235'
original_report_id: '1212235'
title: Reflected XSS on dailydeals.mtn.co.za
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2021-05-28T19:27:15.402Z'
disclosed_at: '2021-12-24T08:49:47.377Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
asset_identifier: mtn.co.za
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on dailydeals.mtn.co.za

## Metadata

- HackerOne Report ID: 1212235
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2021-12-24T08:49:47.377Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello MTN Team.
i found Reflected XSS on``` https://dailydeals.mtn.co.za/index.cfm?GO=DEALS```  vi ```cpID``` parameter with POST method 

## Steps To Reproduce:
1. Intercept the https://dailydeals.mtn.co.za/index.cfm?GO=DEALS 
2. Change Method to POST
3. Add empty line after last header
4. Write this code 
>category_id=7&cpID=1%22%3e%20%3cimg%20src%3da%20onerror%3dalert("XSS")%3e<!--

{F1319085}
5. Sent the Request.
6. Right Click on response area, then Click on ```Show response in browser```
7. copy the link, and put it on browser use BurpSuite as proxy 
8. press the Enter key, then you will see the ```XSS``` on your browser
{F1319086}

## Impact

attacker can convinces a victim to visit a URL then he can:
1. steal users cookies
2. redirect the user to malicious website

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
