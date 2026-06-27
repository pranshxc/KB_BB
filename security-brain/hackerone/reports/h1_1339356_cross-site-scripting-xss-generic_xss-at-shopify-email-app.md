---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1339356'
original_report_id: '1339356'
title: Xss At Shopify Email App
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2021-09-14T13:04:39.991Z'
disclosed_at: '2021-12-24T09:33:27.714Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Xss At Shopify Email App

## Metadata

- HackerOne Report ID: 1339356
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2021-12-24T09:33:27.714Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,
i have found a Xss on the Shopify email app, but it's a bit wired, it's not executing directly but when i am coping the code it is getting executed.

step-1:  Navigate to https://s1-aug.myshopify.com/admin/apps/shopify-email/editor/3694417
step-2:  Add the xss pay load anywhere  like subject, preview text or in the selection body section. "/><img src=x onerror=alert(document.domain)>
step-3: copy the written code

Xss will be fired.

## Impact

Code injection leads to xss

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
