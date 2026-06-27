---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '997350'
original_report_id: '997350'
title: your-store.myshopify.com  preview link  is leak on third party website lead
  to preview all action from store owner Without store Password.
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2020-10-03T21:30:41.389Z'
disclosed_at: '2021-07-12T20:33:47.935Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# your-store.myshopify.com  preview link  is leak on third party website lead to preview all action from store owner Without store Password.

## Metadata

- HackerOne Report ID: 997350
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2021-07-12T20:33:47.935Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Security Team,

#Description
It has been identified that the application is leaking Link to third party sites. In this case it was found that the Linkis being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the Link to catch/preview all action in `your-store.myshopify.com` from store owner without store password.

The owner of that website can perform a security compromise by grabbing those links.


#Solution: 
The solution is very very SIMPLE. Just include the following HTML code in the following in code between <head> tags of the html of the page: <meta name="referrer" content="never" />
This will not send referrer headers to third party websites.

#Reproduction Instructions /
1.Create new products & click Preview .F1013353
2)Now turn burp suite intercept on and click on Click on any social media link(on follow us section). Check for the requests having the Link in `Referrer` as third party website. And copy the Link.
3)Now turn intercept off and Open Link.(with that token) in other tab,browser or  PC.
4)Now you you sucesfully catch/preview all action in `your-store.myshopify.com` from store owner without store password.

>Preview all action/ 

`Store
Products
Collections
Available`


#Proof of Concept
F1013350
F1013351
F1013352
F1013356


#Additional Information:
Note also that if users can author content within the application then an attacker may be able to inject links referring to a domain they control in order to capture data from URLs used within the application.

## Impact

As you can see in the `Referrer` preview Link is getting leaked to third party sites. So, the person who has the complete control over that particular third party site can Use the Link to preview all action in your-store.myshopify.com from store owner without store password.

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
