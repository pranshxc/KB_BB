---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '838231'
original_report_id: '838231'
title: '*.shopify.com - Authentication bypass'
team_handle: shopify
created_at: '2020-04-03T15:35:48.584Z'
disclosed_at: '2020-08-24T16:18:08.375Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
---

# *.shopify.com - Authentication bypass

## Metadata

- HackerOne Report ID: 838231
- Weakness: 
- Program: shopify
- Disclosed At: 2020-08-24T16:18:08.375Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I´ve found a flaw in the authentication process when accessing the website https://upcoming.shopify.com. There seems to be an HTTP Authentication in place to prevent access without authentication. Please follow below POC to get access to https://upcoming.shopify.com without login. The website is full with weird behavior and i´m able to register new accounts via https://upcoming.shopify.com. That could maybe lead to some internal issues.

***Normal request***
{F772305}

***POC**
1) Go to: https://upcoming.shopify.com/tools
2) From that point you can travel to any endpoint

{F772313}
{F772314}
{F772315}

## Impact

High

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
