---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '965510'
original_report_id: '965510'
title: Password protection can be removed for newly created development store
team_handle: shopify
created_at: '2020-08-24T00:36:27.330Z'
disclosed_at: '2020-09-14T18:59:32.051Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Password protection can be removed for newly created development store

## Metadata

- HackerOne Report ID: 965510
- Weakness: 
- Program: shopify
- Disclosed At: 2020-09-14T18:59:32.051Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Details
Per https://help.shopify.com/en/partners/dashboard/managing-stores/development-stores#the-development-store-password-page, it states that the password **can only be removed once the store has been transferred or switch to a paid plan**.

```
You can remove the password page only after you transfer the store to a merchant or switch the store to a paid plan.
```

However, it is still possible to remove the password by using the GraphQL **PreferencesSave** operation.

## Steps to reproduce
1. Create a development store using a partner account
2. From that shop admin, go to **Online Store > Preferences**
3. Make any change to the page and intercept the request
4. Update the `passwordProtection.enabled` property to `false`

The store is now paswordless.

## Demo
████

## Impact

Disable development store password

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
