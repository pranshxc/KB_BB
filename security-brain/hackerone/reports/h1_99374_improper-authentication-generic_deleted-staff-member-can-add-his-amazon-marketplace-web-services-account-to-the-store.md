---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99374'
original_report_id: '99374'
title: deleted staff member can add his amazon marketplace web services account to
  the store.
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-11-12T22:17:32.980Z'
disclosed_at: '2015-11-18T20:23:47.415Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# deleted staff member can add his amazon marketplace web services account to the store.

## Metadata

- HackerOne Report ID: 99374
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-11-18T20:23:47.415Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , I have found that if a staff member had access to `settings` for one single time , he can add his amazon marketplace web services account to the store anytime he wants even after he is deleted from the admins which allows him to fulfill orders for the online store using his own inventory stored at Amazon fulfilment center.
#Scenario: 
Let's say that the store owner added a new staff member and gave him access to `settings` then he decided to delete him for some reason. 
After the staff member is deleted he can still  activate Amazon Fulfillment services by adding any number of amazon accounts to the store and even the store owner can't do anything to prevent this. 
#Steps to reproduce:
1. Add a new staff member and give him access to `settings`. 
2. Login with the Staff member account and go to `https://<your_store>.myshopify.com/admin/fulfillment_services/signup_for_mws` , you'll be redirected to a link in amazon.com that looks like this :

```
https://sellercentral.amazon.com/gp/mws/registration/register.html/188-6388224-3450104?ie=UTF8&AWSAccessKeyId=<KEY>&Signature=<Sginature>&SignatureMethod=HmacSHA256&SignatureVersion=2&id=<id>&returnPathAndParameters=%3Fshop_id%3D000000&signInPageDisplayed=1
```
3.- Save this link then logout and login with the owner account after that delete the staff member account you have added. 
5.- Open a new browser , go to the link you have saved , login with your amazon account , authorize shopify and the account will be added to the store.
6.- login to the store admin then go to `https://<your_store>.myshopify.com/admin/settings/shipping/fulfillment_dropshipping` and you'll see that the account was added.
7 - Do the step #5 more and more and the account will be added more and more times. 

This means that the link you saved can be used anytime to add unlimited malicious amazon marketplace web services account without any need of admin access.

The cause of the vulnerability is that the endpoint used to add the amazon account is (`https://app.shopify.com/services/ping/amazon_mws?shop_id=<Shop_id> `) and doesn't validate for any admin permissions.

Please tell me if you are having any issue reproducing this , I can send you a PoC video.

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
