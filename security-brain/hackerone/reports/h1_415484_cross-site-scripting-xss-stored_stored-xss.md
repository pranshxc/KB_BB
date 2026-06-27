---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '415484'
original_report_id: '415484'
title: Stored xss
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2018-09-27T22:44:43.839Z'
disclosed_at: '2018-11-07T19:09:57.697Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored xss

## Metadata

- HackerOne Report ID: 415484
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2018-11-07T19:09:57.697Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description :
WAF cut html tages but when put <!--> before tages we can bypass it :) .

#Step to reproduce :
1-Open your store account
2-Navigate to https://xxx.myshopify.com/admin/settings/general
3-Put your street address xss payload (xss"><!--><svg/onload=alert(document.domain)>)
4-Go to https://xxx.myshopify.com/admin/dashboards/live
5-XSS alert message

## Impact

XSS attack

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
