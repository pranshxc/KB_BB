---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411690'
original_report_id: '411690'
title: Stored xss in address field in billing activity at https://shop.aaf.com/Order/step1/index.cfm
weakness: Cross-site Scripting (XSS) - Stored
team_handle: aaf
created_at: '2018-09-20T09:00:49.170Z'
disclosed_at: '2019-05-25T09:08:06.032Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 238
asset_identifier: shop.aaf.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored xss in address field in billing activity at https://shop.aaf.com/Order/step1/index.cfm

## Metadata

- HackerOne Report ID: 411690
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: aaf
- Disclosed At: 2019-05-25T09:08:06.032Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear Team,

**Summary:** [add summary of the vulnerability]
After looking into https://shop.aaf.com/Order/step1/index.cfm i get to know that there is address field is vulnerable to stored xss which can lead to steal any user's cookie and can lead to complete account takeover

**Description:** [add more details about this vulnerability]

## Steps To Reproduce:

  1. go to https://shop.aaf.com and click on any products , tshirt
  2. add that in cart and click on proceed
  3. enter xss payload (a"><svg/onload=prompt(1)> ) in every address field and click on OK proceed
  4. xss will popup 

## Supporting Material/References:

XSS OWASP

Thanks,
Vishal

## Impact

Stored xss in address field in billing activity at https://shop.aaf.com/Order/step1/index.cfm

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
