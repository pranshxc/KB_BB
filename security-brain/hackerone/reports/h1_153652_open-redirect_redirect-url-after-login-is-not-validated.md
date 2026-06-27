---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153652'
original_report_id: '153652'
title: Redirect url after login is not validated
weakness: Open Redirect
team_handle: shopify
created_at: '2016-07-25T09:46:50.564Z'
disclosed_at: '2016-07-28T17:14:12.540Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- open-redirect
---

# Redirect url after login is not validated

## Metadata

- HackerOne Report ID: 153652
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2016-07-28T17:14:12.540Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey,

I have noticed and redirect hidden field in admin/staff login page so I though give it a little shot! 

What happened another user create a Shopify page with bad javascript code in it.

and when any user or owner login with following traversal URL he/she will be redirected to bad js containing a page with any intentional.

"https://capripio.myshopify.com/admin/auth/login?redirect=../pages/about-us"

I am well aware of the following description on your bug bounty page.
"Any issue where a store administrator is able to insert javascript in the storefront area of their own store, including the checkout pages."

But I think security issue is greater here as you were aware of above statement so it might be dangerous to redirect someone to a bad page on a front store, so I submitted.

Please see POC video for more demo. available at private dropbox folder follow link below:
https://www.dropbox.com/s/49odz7owp1oj53t/poc.zip?dl=0

Sorry for my bad English!

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
