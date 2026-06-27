---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1021906'
original_report_id: '1021906'
title: '[Information Disclosure] Amazon S3 Bucket of Shopify Ping (iOS) have public
  access of other users image'
weakness: Information Disclosure
team_handle: shopify
created_at: '2020-10-29T15:37:26.104Z'
disclosed_at: '2020-11-21T14:17:04.854Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 129
asset_identifier: Shopify Mobile Applications
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# [Information Disclosure] Amazon S3 Bucket of Shopify Ping (iOS) have public access of other users image

## Metadata

- HackerOne Report ID: 1021906
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2020-11-21T14:17:04.854Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Shopify, when testing Shopify Ping share image function, I discovered an Amazon S3 bucket which has public access which allows an attacker to view all the image of other merchant & users.

## Steps To Reproduce:
1. Install Shopify Ping on your phone then enable Shopify Chat for your store.
2. Go to your Shopify Store and start chatting as a customer. ███
3. Log in to Staff account on Shopify Ping and click on send image ████████
4. Back to Shopify Store as Customer and inspect the website code, you will find the URL of image ██████████ https://ping-api-production.s3.us-west-2.amazonaws.com/oks██████
5. Now visit https://ping-api-production.s3.us-west-2.amazonaws.com, you can view all images of other stores. █████████

## Impact

Using this Bucket access, a hacker can steal all private images of other stores and the user who shared through Shopify Ping.

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
