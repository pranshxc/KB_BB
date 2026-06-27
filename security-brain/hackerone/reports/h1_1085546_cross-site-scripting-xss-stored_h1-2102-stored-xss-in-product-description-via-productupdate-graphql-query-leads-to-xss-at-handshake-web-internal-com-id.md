---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1085546'
original_report_id: '1085546'
title: '[h1-2102] Stored XSS in product description via `productUpdate` GraphQL query
  leads to XSS at handshake-web-internal.shopifycloud.com/products/[ID]'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2021-01-23T23:22:39.210Z'
disclosed_at: '2022-07-11T21:33:50.391Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: Handshake Marketplace
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [h1-2102] Stored XSS in product description via `productUpdate` GraphQL query leads to XSS at handshake-web-internal.shopifycloud.com/products/[ID]

## Metadata

- HackerOne Report ID: 1085546
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2022-07-11T21:33:50.391Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This is most likely going to be a duplicate, so I'll keep it short.

A stored cross site scripting vulnerability exists at `handshake-web-internal.shopifycloud.com` through the `product description` field.

## Recruirements

A shop with the Handshake plugin enabled and set-up

## Reproduction steps

1. Add a product in your store with the following description (make sure to click the < > button first so you can enter HTML):

> <img src=x onerror=prompt(document.domain)>

then set it to `Active`:

{F1169545}

2. Go to your Handshake portal, pick a price and a category to publish the item:

{F1169544}

3. Check your item in the on the handshake website, XSS will pop up after +/- 3 seconds:

{F1169546}

(I removed the PoC for obvious reasons, please do the same when triaging or everyone will submit)

## Impact

Arbitrary javascript execution (stored) on a shared domain

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
