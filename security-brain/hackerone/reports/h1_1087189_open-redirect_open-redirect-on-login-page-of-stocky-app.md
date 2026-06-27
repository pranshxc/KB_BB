---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1087189'
original_report_id: '1087189'
title: Open Redirect on Login Page of Stocky App
weakness: Open Redirect
team_handle: shopify
created_at: '2021-01-26T04:31:23.721Z'
disclosed_at: '2021-02-11T19:18:29.723Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- open-redirect
---

# Open Redirect on Login Page of Stocky App

## Metadata

- HackerOne Report ID: 1087189
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2021-02-11T19:18:29.723Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerable app is Stocky,
1. Visit login page of app with vulnerable parameter & malicious website address`(?return_to=//evil.com)` like `https://stocky.shopifyapps.com/users/login?return_to=//evil.com`
2. Then login to account
3. Open Redirect is executed

PoC Video:
{F1172071}

## Impact

Open Redirect

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
