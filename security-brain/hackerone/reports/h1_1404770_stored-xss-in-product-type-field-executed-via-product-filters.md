---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1404770'
original_report_id: '1404770'
title: Stored XSS in "product type" field executed via product filters
team_handle: judgeme
created_at: '2021-11-18T23:47:51.394Z'
disclosed_at: '2022-04-26T16:11:42.156Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Stored XSS in "product type" field executed via product filters

## Metadata

- HackerOne Report ID: 1404770
- Weakness: 
- Program: judgeme
- Disclosed At: 2022-04-26T16:11:42.156Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI @judgeme!
I found Stored XSS!)
I Install judge.me in Shopify E-Commerce. Step to reproduce:
1. Log in to our shopify dev store and install "judgeme" app.
2. Create random product in our Shopify store (make it active) and insert XSS playload  "><img src=x onerror=prompt(document.domain)> in "PRODUCT TYPE" field and SAVE


{F1518888}


3. Then go to our judgeme app https://xxx.myshopify.com/admin/apps/judgeme/products. There is a filter field TYPE . Click on it and select our playload from the list 
{F1518897}
4. And it works )))



{F1518898}

I attached video POC

## Impact

Session Hijacking, Cookie Stealing.

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
