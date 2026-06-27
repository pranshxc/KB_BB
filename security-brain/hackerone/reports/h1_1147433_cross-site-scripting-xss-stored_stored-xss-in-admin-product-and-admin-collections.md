---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1147433'
original_report_id: '1147433'
title: Stored XSS in /admin/product and /admin/collections
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2021-04-03T09:41:30.050Z'
disclosed_at: '2022-12-01T22:44:01.766Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in /admin/product and /admin/collections

## Metadata

- HackerOne Report ID: 1147433
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2022-12-01T22:44:01.766Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Hello Security Team,

I was going through previous reports of XSS and I have found this,
https://hackerone.com/reports/978125

As stated by team on this page even on https://hackerone.com/shopify?type=team under Known issues
 that we can now report XSS under Rich Text Editor on Product description and Collection description. 
I have found XSS on this endpoints /admin/product and /admin/collections

{F1252456}

### Steps to Reproduce:
#### /admin/product

Step1: Go to https://your-store.myshopify.com/admin/products?selectedView=all
Step2: Click on Add product 
Step3: Add anything in Title
Step4: Right side corner in description click on Show HTML
Step5: Add below Payloads and Click on Save

#### Payload: 
">\]<img src=x onerror=alert(document.domain)>  ">\]<img src=x onerror=alert(document.cookie)>
      
XSS will get triggered.

{F1252457}

#### /admin/collections

Step1: Go to https://your-store.myshopify.com/admin/collections
Step2: Click on Create collection
Step3: Add anything in Title
Step4: Right side corner in description click on Show HTML
Step5: Add below Payloads and Click on Save

#### Payload: 
">\]<img src=x onerror=alert(document.domain)>  ">\]<img src=x onerror=alert(document.cookie)>
      
XSS will get triggered.

{F1252455}

I have attached POC Video, Please take a look.

{F1252458}

#### Thank You
Ashish Dhone

## Impact

A malicious user can steal cookies and use them to gain further access even an attacker can use XSS to send requests that appear to be from the victim to the web server.

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
