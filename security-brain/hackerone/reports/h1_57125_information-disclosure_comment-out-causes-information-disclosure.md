---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '57125'
original_report_id: '57125'
title: comment out causes information disclosure
weakness: Information Disclosure
team_handle: shopify
created_at: '2015-04-18T06:24:47.747Z'
disclosed_at: '2015-04-19T14:33:13.205Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# comment out causes information disclosure

## Metadata

- HackerOne Report ID: 57125
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2015-04-19T14:33:13.205Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there

Go to General setting (https://your-domain.myshopify.com/admin/settings/general), set Homepage Title to <!-- and change Name to "> plus HTML Tag like words. Some data will be leaked in the place of Title in the home page. This is dangerous because sometimes title contains highly confidential data such as cart_token, checkout_token, email, session_hash, and so on. Ticket ID is 1559798.

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
