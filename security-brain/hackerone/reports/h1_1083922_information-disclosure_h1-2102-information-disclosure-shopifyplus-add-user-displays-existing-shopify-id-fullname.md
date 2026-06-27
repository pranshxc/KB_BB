---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1083922'
original_report_id: '1083922'
title: '[h1-2102] Information disclosure - ShopifyPlus add user displays existing
  Shopify ID fullname'
weakness: Information Disclosure
team_handle: shopify
created_at: '2021-01-22T02:34:04.214Z'
disclosed_at: '2022-02-10T19:45:42.206Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: Plus Web Admin with Single Domain Feature
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# [h1-2102] Information disclosure - ShopifyPlus add user displays existing Shopify ID fullname

## Metadata

- HackerOne Report ID: 1083922
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2022-02-10T19:45:42.206Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I am not sure if this by design but it came to my attention that the **Add users** functionality located at `https://shopify.plus/[id]/users/invite` allow a Shopify Plus user with the **User management** access to retrieve any existing Shopify ID full name.

## Steps to reproduce
1. Log in into **ShopifyPlus**
1. Go to **Users > Add users**
1. Within the email field, enter an email address of any existing Shopify Account ID (i.e: francisbeaudoin+h1-2101@wearehackerone.com)
1. Select any role and click **Send invite**

As a result, if the entered email does have a Shopify ID, its fullname will be displayed within the user page.

## Screenshot of a pending invite
██████████

**Note:** I've a feeling that this is expected but still reporting it as the standard invite flow (non ShopifyPlus) doesn't display that kind of informations unless the user accepts the invite.

## Impact

A **ShopifyPlus** user with **User management** can retrieve the firstname and lastname of any existing ShopifyID account (by email lookup).

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
