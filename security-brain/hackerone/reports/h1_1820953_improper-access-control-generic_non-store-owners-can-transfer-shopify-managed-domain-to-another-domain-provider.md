---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1820953'
original_report_id: '1820953'
title: Non-store owners can transfer Shopify-managed domain to another domain provider
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2023-01-03T12:12:32.451Z'
disclosed_at: '2024-01-17T22:23:43.698Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 44
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Non-store owners can transfer Shopify-managed domain to another domain provider

## Metadata

- HackerOne Report ID: 1820953
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2024-01-17T22:23:43.698Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

According to docs [here](https://help.shopify.com/en/manual/domains/managing-domain-ownership/transferring-shopify-domains#transfer-your-shopify-managed-domain-to-another-domain-provider), only store owners can transfer domains to another domain provider.
{F2100708}

This is not enforced as users/staff members without the `Transfer domain to another Shopify store` permission can perform this action as well as staff members that aren't a store owner in themselves.

## Shops Used to Test:
███

## Steps To Reproduce:
1. Login as a staff member with these permissions only:
{F2100711}

2. From your Shopify admin, go to `Settings > Domains`.
3. In the Shopify-managed domains section, click the name of the domain that you want to transfer.
4. Click `Transfer domain > Transfer to another provider`.
5. Review the information, and then click `Confirm`. The domain authorization code is displayed on your domain's information page.
6. Give the domain authorization code to your new domain provider to verify the transfer.
7. Done.

## Supporting Material:
███████

## Impact

Shopify-managed domains can be transferred to another domain provider by a staff member without `Transfer domain to another Shopify store` permission and a non-store owner.

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
