---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '294505'
original_report_id: '294505'
title: Cross-site scripting in "Contact customer" form
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2017-12-02T16:03:21.082Z'
disclosed_at: '2017-12-19T09:57:02.421Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Cross-site scripting in "Contact customer" form

## Metadata

- HackerOne Report ID: 294505
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2017-12-19T09:57:02.421Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I found HTML Injection Vulnerability while admin contact with customer.
In this vulnerability admin is attacker whereas customer is victim.

#Steps to Reproduce:

1. Go to **Customers** and Click on **Customer Email Address**.
2. New Pop-Up window will become open, In **Customer Message** field type this html code

><h1>HTML INJECTION</h1>

3 . Click on **Review Email** Button.

HTML will become execute.

Checkout the POC Video.
  
Thanks,

## Impact

Admin of store can redirect any user to any malicious website, and can perform all possible attacks through this vulnerability.

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
