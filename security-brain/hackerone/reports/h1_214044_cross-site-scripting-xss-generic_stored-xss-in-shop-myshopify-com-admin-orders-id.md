---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '214044'
original_report_id: '214044'
title: Stored XSS in [shop].myshopify.com/admin/orders/[id]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2017-03-17T00:21:07.090Z'
disclosed_at: '2017-03-28T21:01:59.726Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in [shop].myshopify.com/admin/orders/[id]

## Metadata

- HackerOne Report ID: 214044
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2017-03-28T21:01:59.726Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I have found a stored XSS vulnerability in `[shop].myshopify.com/admin/orders/[id]` in conversion details links, it's the same as #55842 but this one is through landing page URL not the referrer.

**Steps to reproduce**: 
1. Navigate to `[shop].myshopify.com/` 
2. Modify `_landing_page` cookie value to `javascript:alert(1)`
{F169421}
3. Add a product to your cart then complete the checkout process.
4. Login with an admin account then navigate to `[shop].myshopify.com/admin/orders/[id]` and click the link for **The first page they visited** and `alert(1)` will be executed.
{F169422}

**Impact**:
This is a customer-to-admin XSS, so an attacker can target admins to do malicious actions such as fetching the CSRF token and using it to submit a request to add himself as an admin to takeover the store.

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
