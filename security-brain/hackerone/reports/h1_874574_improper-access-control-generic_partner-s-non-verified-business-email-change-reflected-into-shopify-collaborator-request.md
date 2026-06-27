---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '874574'
original_report_id: '874574'
title: Partner's non-verified business email change reflected into Shopify Collaborator
  Request
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2020-05-15T02:12:35.036Z'
disclosed_at: '2020-09-14T19:45:34.975Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: partners.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Partner's non-verified business email change reflected into Shopify Collaborator Request

## Metadata

- HackerOne Report ID: 874574
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2020-09-14T19:45:34.975Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Details

In https://partners.shopify.com a Partner must validate his email address prior making a request to manage a store. An email is then being sent to the Shop owner and it only includes the Partner's Business Name and it also links to the **Collaborator Request Review** to either accept or decline it.

Taking that into consideration, if a Partner's change his email address without validating it once a request is sent, the Shopify shop owner's is being displayed the non-verified business email which could lead him to accept a malicious user.

## Steps to reproduce
1. Login to your Partner's account which has a verified email
2. Make a request to add a managed Shopify Store to your account
3. Go to Settings and update your **Business Email** 
4. Login to the managed Shopify shop and review the Collaborator Request, the non-verified email will be displayed

As a side note, this also leads to Information Disclosure (https://hackerone.com/bugs?report_id=853919) as if the above process is done and you do change the Partner's email to let's say victim@shopify.com, once the Collaborator Request is accepted and you Log-in through the Partner's dashboard, you'll be shown victim@shopify.com stores into the dropdown.

## Demo
██████

## Impact

A Partner's is being able to spoof his confirmed email address by a non-verified one in store management request

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
