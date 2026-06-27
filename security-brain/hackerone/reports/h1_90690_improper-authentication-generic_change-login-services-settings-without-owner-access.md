---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '90690'
original_report_id: '90690'
title: change Login Services settings without owner access
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-09-27T20:38:00.359Z'
disclosed_at: '2015-10-14T19:54:09.411Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# change Login Services settings without owner access

## Metadata

- HackerOne Report ID: 90690
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-10-14T19:54:09.411Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi

in settings -> account owner can set login service for staff members!
this is only available for owners, and full access admins can't see or change this values!

admin with setting access can send a "POST" request to shop.json and change this settings!


steps:

- get access token for one full access admin (you can send request to xauth or sniff it from mobile device)
- send request with POST method to "https://~ShopName~.myshopify.com/admin/shop.json"

data:

{"shop":{"google_apps_domain":"anydomain","google_apps_login_enabled":true}}

google_apps_login_enabled
google_apps_domain


so any admin just with setting access can modify this option,this must limited to owner!

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
