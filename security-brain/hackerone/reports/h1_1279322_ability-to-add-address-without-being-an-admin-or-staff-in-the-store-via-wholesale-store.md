---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1279322'
original_report_id: '1279322'
title: Ability to add address without being an admin or staff in the store via wholesale
  store
team_handle: shopify
created_at: '2021-07-27T14:20:53.616Z'
disclosed_at: '2021-12-03T13:02:24.526Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
---

# Ability to add address without being an admin or staff in the store via wholesale store

## Metadata

- HackerOne Report ID: 1279322
- Weakness: 
- Program: shopify
- Disclosed At: 2021-12-03T13:02:24.526Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Customers in the shopify store can be added manually or automatically, an example is added automatically when you want to checkout (here we don't need to checkout) just by proceeding to "Continue to shipping" information will be sent directly to the customer such as email address and other things but when we do this again by filling in the same email with a different address then the address on the customer overview admin will not change or be added maybe this is the behavior expected by shopify because to avoid someone without access to change and add an address on existing customer but I found a vulnerability here that causes attackers to add addresses to customers even though they do not have admin rights or staff 

Step to reproduce :

1. Setting your shopify wholesale store and activate "Customers must provide an address" then save
2. Register and add business address at wholesale store and using another customers email then click sign up
3. Now on the shopify store, check on the customer whose email we used to register at wholesale, there will be an address that we just added via wholesale registration.

It will be dangerous if the shopify wholesale store activates the "Customers must provide an address" feature because attackers can add default addresses to customers without having any admin acces or staff and this maybe idor because we can add other customer addresses without having access but you can decide for yourself

## Impact

Vulnerabilities that cause attackers to add customer default addresses without having admin/staff rights should be only admins and staff can change and add customer default addresses, but here attackers who have no access admin/staff can add default addresses to customers, this can have an impact takeover default addresses that attackers can use to replace the default addresses of other customers

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
