---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1107726'
original_report_id: '1107726'
title: Stored XSS on apps.shopify.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2021-02-20T00:25:42.461Z'
disclosed_at: '2021-04-08T19:23:55.717Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on apps.shopify.com

## Metadata

- HackerOne Report ID: 1107726
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2021-04-08T19:23:55.717Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps to reProduce:

1> Write payload `luc1d"><img/src="x"onerror=alert(document.domain)>@wearehackerone.com` as `Store contact email` in General Settings page`(*.myshopify.com/admin/settings/general)`

{F1202181}

-- Wait here around 60 mins (maybe more idk, it was 60 mins for me) for the change to reflect --
(You can confirm the change on here `https://apps.shopify.com/shops/<shopId>`)
2> Visit any app page like `https://apps.shopify.com/local-delivery`
3> Click `Get support` link on sidebar
{F1202116}

4> XSS will be triggered
{F1202211}

PoC Video,
{F1202215}

## Impact

Stored XSS

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
