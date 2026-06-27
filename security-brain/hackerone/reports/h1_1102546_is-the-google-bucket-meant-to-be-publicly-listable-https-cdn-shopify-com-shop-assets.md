---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1102546'
original_report_id: '1102546'
title: Is the Google Bucket Meant To Be Publicly Listable? https://cdn.shopify.com/shop-assets/
team_handle: shopify
created_at: '2021-02-13T05:14:37.589Z'
disclosed_at: '2022-02-09T20:59:55.366Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Is the Google Bucket Meant To Be Publicly Listable? https://cdn.shopify.com/shop-assets/

## Metadata

- HackerOne Report ID: 1102546
- Weakness: 
- Program: shopify
- Disclosed At: 2022-02-09T20:59:55.366Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found that https://cdn.shopify.com/shop-assets/ is listing the all objects in https://storage.googleapis.com/arrive-assets-storage-production/

But when I directly visit https://storage.googleapis.com/arrive-assets-storage-production/, it says 

>Anonymous caller does not have storage.objects.list access to the Google Cloud Storage bucket.

So I wonder maybe it is unintentional that user can directly list all the objects in GCP using the link https://cdn.shopify.com/shop-assets/?

PoC

██████

## Impact

List objects in GCP that should be protected from anonymous users

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
