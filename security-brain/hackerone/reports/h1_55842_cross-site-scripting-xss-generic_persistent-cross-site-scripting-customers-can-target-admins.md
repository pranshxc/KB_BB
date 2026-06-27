---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55842'
original_report_id: '55842'
title: '[persistent cross-site scripting] customers can target admins'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-04-11T07:51:20.741Z'
disclosed_at: '2015-07-01T15:35:20.996Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [persistent cross-site scripting] customers can target admins

## Metadata

- HackerOne Report ID: 55842
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-07-01T15:35:20.996Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**hello**,

Let's say a shop has a checkout button.
when we click buy now , you will be redirected to https://madamcury.myshopify.com/cart/1188733065:1?channel=buy_button&referer=javascript:alert(document.cookie);

Keep an eye on referer parameter in URL 
`referer=javascript:alert(document.cookie);`

A customer can set referer to a xss payload, and the admin will see a referer parameter in his control panel, if the admin clicks on the link the xss triggered. (POC ATTACHED)

Steps to reproduce
==================================
- create a buy now button
- when you click buy now button , you will be redirected to https://madamcury.myshopify.com/cart/1188733065:1?channel=buy_button&referer=javascript:alert(document.cookie);
- set referer parameter in url to javascript:alert(document.cookie);
- finish the order
- now from admin account login into admin panel,
- click the referer link , you will see a xss triggered.

All admins, users of a shop can be targeted with this attack.
Tell me if you any issues reproducing the issue :)

**regards
Wesecureapp**

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
