---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '415350'
original_report_id: '415350'
title: Missing CSRF Protection in  /stats EndPoint.
weakness: Cross-Site Request Forgery (CSRF)
team_handle: chaturbate
created_at: '2018-09-27T16:46:30.865Z'
disclosed_at: '2018-10-09T00:14:14.151Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Missing CSRF Protection in  /stats EndPoint.

## Metadata

- HackerOne Report ID: 415350
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: chaturbate
- Disclosed At: 2018-10-09T00:14:14.151Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

##EndPoint /affiliates/stats. doesnot verify the CSRF Tokens##


## Steps To Reproduce:

 1. Login with the your account 
 2. Navigate to the URL https://chaturbate.com/affiliates/stats.. 
 3. Check the stats in default its todays date or this week in select period.
4. Intercept the request and change the parameter to whatever you want to set.
5. generate the POC And open it in browser
6. You can see the changes in the form.

## Supporting Material/References:
Please find attached for the CSRF POC and CSRF_1 for PreCSRF And CSRF_2 For Post CSRF.

## Impact

Attacker may change the parameters in stat or may force user to download the malicious .

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
