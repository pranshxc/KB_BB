---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '93921'
original_report_id: '93921'
title: Unauthorized access to all collections, products, pages from other stores
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-10-14T22:52:59.241Z'
disclosed_at: '2015-10-20T16:00:36.331Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Unauthorized access to all collections, products, pages from other stores

## Metadata

- HackerOne Report ID: 93921
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-10-20T16:00:36.331Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi

I found a vulnerability in shopify that can leak other shops hidden objects include collection,product,page,blog

steps:

- go to "/admin/link_lists"
- click on "add link list"
- select one object from list for example collection
- open "Inspect Element"
- change value of element "link_list[links][][subject_id]" to any id from other shops
- click on save then when page reloaded you will see data in box 

this works for hidden collection, products, pages

Regards

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
