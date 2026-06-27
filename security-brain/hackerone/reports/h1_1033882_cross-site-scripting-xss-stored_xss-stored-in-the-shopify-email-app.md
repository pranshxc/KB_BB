---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1033882'
original_report_id: '1033882'
title: XSS stored in the Shopify Email app
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2020-11-13T13:54:34.409Z'
disclosed_at: '2020-11-19T23:30:04.714Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS stored in the Shopify Email app

## Metadata

- HackerOne Report ID: 1033882
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2020-11-19T23:30:04.714Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

step:

1、install app `Shopify Email`
{F1076928}

2、Click `General` under `Settings`

3、Change phone number to `1234567"><img src=a onerror=alert(1)>`
{F1076939}

4、Open shopify email app and create an email

5、Show phone number
{F1076940}

6、watch the vedio poc for more information

## Impact

store xss

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
