---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1550400'
original_report_id: '1550400'
title: Staff without Manage Themes permissions can update themes
team_handle: shopify
created_at: '2022-04-25T16:01:16.781Z'
disclosed_at: '2024-01-23T18:10:59.189Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 51
asset_identifier: partners.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Staff without Manage Themes permissions can update themes

## Metadata

- HackerOne Report ID: 1550400
- Weakness: 
- Program: shopify
- Disclosed At: 2024-01-23T18:10:59.189Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey team,
as per https://help.shopify.com/en/partners/dashboard/account-access#store-access only people with **Manage themes** can View and edit the theme listing, and **upload a new version to the Shopify Theme Store** but **Manage public listings** 	can only Manage apps, themes, and experts listings. not **upload a new version to the Shopify Theme Store** but when a **Owner** gives his **STAFF** permission of **Manage public listings** , he is able to **upload a new version to the Shopify Theme Store** by just going to the https://themes.shopify.com/services/v2/themes/submission/new


## Shops Used to Test:
https://partners.shopify.com/2450201/


## Steps To Reproduce:

1. **owner** invites the **STAFF** with **Manage public listings** and **STAFF** accept it and Login.
2. Now he goes to https://partners.shopify.com/2450201/themes but he won't have access to it so he directly went to "https://themes.shopify.com/services/v2/themes/submission/new"

███████
3. and now he can Uploads a Theme file from the Partner side

and if these are wrong , let me know if there is any detailed version of Permission on Partners.shopify.com as **Manage public listings** is confusing to me a little because of my previous and this report.
## Supporting Material:
Attached

## Impact

Permission mis-configuration ,**STAFF** with **Manage public listings** permission can Upload Theme which is a feature for **Manage themes**

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
