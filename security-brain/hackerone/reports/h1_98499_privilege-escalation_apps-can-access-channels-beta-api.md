---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '98499'
original_report_id: '98499'
title: Apps can access 'channels' beta api
weakness: Privilege Escalation
team_handle: shopify
created_at: '2015-11-07T19:43:56.968Z'
disclosed_at: '2015-11-18T21:03:22.247Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Apps can access 'channels' beta api

## Metadata

- HackerOne Report ID: 98499
- Weakness: Privilege Escalation
- Program: shopify
- Disclosed At: 2015-11-18T21:03:22.247Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hello,**

As documented here, an app can access to the following scopes :
https://docs.shopify.com/api/authentication/oauth#scopes. 
But an app can request/get access to a lots more scopes, and some of those scope shouldn't be accessible.

**PoC**

    https://victim.myshopify.com/admin/oauth/authorize?client_id=fc49e813f5aad9c8d8f65117031a9684&scope=read_apps,write_apps,write_content,read_content,write_customers,read_customers,read_disputes,write_fulfillments,read_fulfillments,write_gift_cards,read_gift_cards,write_orders,read_orders,read_products,write_products,read_script_tags,write_script_tags,write_scripts,read_scripts,read_shipping,write_shipping,write_social_network_accounts,read_social_network_accounts,read_themes,write_themes,read_channels,write_channels&redirect_uri=http://while42.myshopify.com/&state=123&shop=while42
    
Then request the access_token, and use it to access to any of those scopes.

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
