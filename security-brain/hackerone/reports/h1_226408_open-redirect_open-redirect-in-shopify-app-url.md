---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226408'
original_report_id: '226408'
title: Open Redirect in shopify app URL
weakness: Open Redirect
team_handle: shopify
created_at: '2017-05-05T19:46:13.139Z'
disclosed_at: '2017-07-21T12:17:59.757Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- open-redirect
---

# Open Redirect in shopify app URL

## Metadata

- HackerOne Report ID: 226408
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2017-07-21T12:17:59.757Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The Amazon Alexa app when installing calls a URL https://assistant-client.meteorapp.com/shopify/callback?code=6aae881ab9c4f12d5b264e6c871a108a&hmac=6109806a12b0439d6a2dce2d547344eb1c2c53e9691259f39eefbb93b9c9c97b&shop=pappuza-2.myshopify.com&timestamp=1494008598

The **shop** parameter will accept any domain and redirects. 
Don't know whether meteorapp.com is controlled by you but reporting this as this found as made by shopify in the app store.

If not going to resolve this, please do not mark as NA. I will do the needful.

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
