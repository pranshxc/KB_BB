---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '93004'
original_report_id: '93004'
title: unauthorized access to all collections name
weakness: Privilege Escalation
team_handle: shopify
created_at: '2015-10-08T21:23:04.635Z'
disclosed_at: '2015-10-14T19:45:27.215Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# unauthorized access to all collections name

## Metadata

- HackerOne Report ID: 93004
- Weakness: Privilege Escalation
- Program: shopify
- Disclosed At: 2015-10-14T19:45:27.215Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi

admins can set tax rates in shopify admin panel
https://SHOP.myshopify.com/admin/settings/taxes/* or ...
they can add "Tax override" for specific collection, but this action didn't check ShopID! so we can add any collection id, and it will be add to our shop

this also will works for "Hidden" collections on any shop!


steps:

-  goto https://SHOP.myshopify.com/admin/settings/taxes/*
- click on "Add a tax override"
- click on "Select a collection" and select on of your collection
- open "Inspect Element"  and find element with name "tax_override[collection_id]"
- change it to a collection_id from another shop like "137861635" and click on save

done! tax rate will be add to shop, and you can find collection name right in "Tax overrides" table!

Another way is send this request directly:

URL: /admin/settings/taxes/*/override

data:

authenticity_token= __TOKEN__
tax_override[is_shipping]=false
tax_override[collection_id]= collection_id
tax_override[tax_override_regions_attributes][0][zone]=state::TX
tax_override[tax_override_regions_attributes][0][rate]=50

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
