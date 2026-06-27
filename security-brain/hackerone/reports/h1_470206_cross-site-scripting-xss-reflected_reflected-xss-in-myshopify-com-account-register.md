---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '470206'
original_report_id: '470206'
title: Reflected XSS in *.myshopify.com/account/register
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2018-12-20T09:55:07.127Z'
disclosed_at: '2019-03-12T16:21:08.480Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 98
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in *.myshopify.com/account/register

## Metadata

- HackerOne Report ID: 470206
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2019-03-12T16:21:08.480Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Shopify allows shop admin to enable customer registration. When a customer registers with a short password and HTML content as the first name and last name then customer redirects to *.myshopify.com/account/register with error messages and the provided data. As there is no Cross-site Scripting validation and CSRF protection anyone can force the customers to execute  XSS on that page.

{F394911}

## Impact

By exploiting this Vulnerability
An attacker can force the customer to execute XSS and 
1. Steal user's cookie.
2. Launch advanced phishing attacks by rendering arbitrary HTML forms.
3. Force users to download malware/viruses.
4. Execute browser-based attacks etc.

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
