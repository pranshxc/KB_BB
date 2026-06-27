---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '100956'
original_report_id: '100956'
title: Cookie securing your "Opening soon" store is not secured against XSS
weakness: Violation of Secure Design Principles
team_handle: shopify
created_at: '2015-11-22T14:09:32.822Z'
disclosed_at: '2015-12-01T22:39:11.668Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Cookie securing your "Opening soon" store is not secured against XSS

## Metadata

- HackerOne Report ID: 100956
- Weakness: Violation of Secure Design Principles
- Program: shopify
- Disclosed At: 2015-12-01T22:39:11.668Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC:
1) Protect your e-shop with a password (Storefront password)
2) Go to your e-shop URL and enter the password to access the store
3) There is a cookie created - name: storefront_digest - this cookie contains the password (in a secure way) which protects your store
4) This cookie is not marked as HttpOnly, so if there is e.g. XSS, anyone can steal this cookie
5) With this cookie anyone can access your "Opening soon" e-shop, even if he doesn't know the password

Before you answered I would like to confirm that I read shopify terms and:
1) I don't care about he password strength. It is not important in that case
2) I am pretty sure that this cookie - storefront_digest - is a sensitive cookie since by stealing this cookie you can access resources you shouldn't be able to...

Thank you.

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
