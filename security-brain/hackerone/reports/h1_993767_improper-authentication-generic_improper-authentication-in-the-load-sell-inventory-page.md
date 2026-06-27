---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '993767'
original_report_id: '993767'
title: Improper authentication in the load sell inventory page
weakness: Improper Authentication - Generic
team_handle: cs_money
created_at: '2020-09-29T04:32:08.957Z'
disclosed_at: '2020-10-08T09:39:17.953Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: cs.money
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Improper authentication in the load sell inventory page

## Metadata

- HackerOne Report ID: 993767
- Weakness: Improper Authentication - Generic
- Program: cs_money
- Disclosed At: 2020-10-08T09:39:17.953Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:

Hello team,

I found an endpoint response all data relate to sell mode inventory that doesn't have improper authentication in the link: 
https://cs.money/load_sell_mode_inventory

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Open directly the link:
https://cs.money/load_sell_mode_inventory
  2. Observe the result

## Supporting Material/References:


  * [attachment / reference]

## Impact

All most data in the site to view then user have to login the first. I think that you are missing authentication for these pages.

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
