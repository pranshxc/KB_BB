---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1015283'
original_report_id: '1015283'
title: 'Bypass For #997350 your-store.myshopify.com preview link is leak on third
  party website Via Online Store'
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2020-10-21T13:47:53.938Z'
disclosed_at: '2022-02-10T19:42:54.345Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Bypass For #997350 your-store.myshopify.com preview link is leak on third party website Via Online Store

## Metadata

- HackerOne Report ID: 1015283
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2022-02-10T19:42:54.345Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Security Team,

#Description
Full Description in #997350 


The owner of that website can perform a security compromise by grabbing those links.

#Solution:
The solution is very very SIMPLE. Just include the following HTML code in the following in code between <head> tags of the html of the page: <meta name="referrer" content="never" />
This will not send referrer headers to third party websites.

#Reproduction Instructions /
1)Open your Store & add  social media Links.
2)Click  F1045363. 
3)Now turn burp suite intercept on and click on Click on any social media link(on follow us section). Check for the requests having the Link in Referrer as third party website. And copy the Link.
4)Now turn intercept off and Open Link.(with that token) in other tab,browser or PC.
5)Now you you sucesfully catch/preview all action in your-store.myshopify.com from store owner without store password.

>Preview all action/Login

#Proof of Concept
F1045355
F1045356
F1045357
F1045358
F1045359
F1045360

#Additional Information:
Note also that if users can author content within the application then an attacker may be able to inject links referring to a domain they control in order to capture data from URLs used within the application.

## Impact

As you can see in the Referrer preview Link is getting leaked to third party sites. So, the person who has the complete control over that particular third party site can Use the Link to preview all action in your-store.myshopify.com from store owner without store password.

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
