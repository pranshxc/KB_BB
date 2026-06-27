---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '391390'
original_report_id: '391390'
title: Stored XSS on activity
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2018-08-07T17:31:29.764Z'
disclosed_at: '2018-08-14T20:29:30.810Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 55
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on activity

## Metadata

- HackerOne Report ID: 391390
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2018-08-14T20:29:30.810Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi security team members,

#Description
I found a store xss on the activity which allows an attacker to steal admin account cookies.

#Step to reproduce
1-Create store
2- Add a member in a store
3- Member can choose any name 
4- So change the any member name with hunter"><svg/onload=alert(2)>
5- Now on admain account make changes 
6- That will create activity with attacker malicious payload

#POC
Please see the below image
{F329469}
Let me know if more information is needed to my end.
Best Regards,
Shahzad

## Impact

An attacker(staff member) can takeover admin account.

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
