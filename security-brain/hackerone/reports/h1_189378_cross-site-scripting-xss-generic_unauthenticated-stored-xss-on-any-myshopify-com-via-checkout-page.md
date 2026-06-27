---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '189378'
original_report_id: '189378'
title: Unauthenticated Stored XSS on <any>.myshopify.com via checkout page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-12-08T02:57:40.937Z'
disclosed_at: '2016-12-16T21:19:38.691Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Unauthenticated Stored XSS on <any>.myshopify.com via checkout page

## Metadata

- HackerOne Report ID: 189378
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-12-16T21:19:38.691Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I have found a stored cross site scripting vulnerability on `<any>.myshopify.com` through customer's first name in the checkout page after the order is completed.

#Details:
While processing an order on `checkout.shopif.com` customers are asked to enter their first name , last name , address details ..etc.
It's been found that the mentioned fields does not accept any HTML tags , so if you entered something like `<script>alert(2);</script>` , it will be rejected and you'll see a message saying `cannot contain HTML tags` . 
However, for some reason the only tag that you can include and it won't be rejected is `<html>` tag itself :D 
So , something like `<html onmouseover=alert(1)>` will be accepted.

After completing the order you'll land at a **thank** page saying that the order was confirmed , the XSS vulnerability lies in that page due to not sanitizing the first name of the customer inside the `<title>` tag.

#Steps to reproduce:
1. As an admin create a product with $0 price and $0 taxes on shipping so that you don't have to to enter any credit card details (the price doesn't matter , it's just to make testing easier).
2. As a user go to the product you created and buy it.
3. You'll be redirected to a page in `checkout.shopify.com` asking you to enter your details.
4. In the first name field enter `</title></head><html onmouseover=alert(2)>` .
5. Fill the other fields then click **Continue to shipping method** --> **Continue to payment method** --> **Complete order** 
6. XSS will trigger on `checkout.shopify.com` , to get the payload executed on `<your_store>.myshopify.com` , just go to `<your_store>.myshopify.com/0/checkouts/<checkout_id>/thank_you`

Here is a live PoC: `https://zh5402.myshopify.com/14372648/checkouts/5e566284338e71d6adc542b6567b4cf0/thank_you`
{F141546}


#Impact:
Through this vulnerability an attacker is able to execute arbitrary JavaScript at `<any>.myshopify.com` on admins and any other users to perform malicious actions such as fetching the CSRF token and using it to perform malicious requests , stealing sensitive information ..etc.

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
