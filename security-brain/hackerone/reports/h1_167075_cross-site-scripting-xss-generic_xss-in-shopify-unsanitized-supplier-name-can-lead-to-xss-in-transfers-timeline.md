---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '167075'
original_report_id: '167075'
title: 'XSS in SHOPIFY: Unsanitized Supplier Name  can lead to XSS in Transfers Timeline'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-09-09T10:38:00.021Z'
disclosed_at: '2016-09-19T16:02:32.881Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in SHOPIFY: Unsanitized Supplier Name  can lead to XSS in Transfers Timeline

## Metadata

- HackerOne Report ID: 167075
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2016-09-19T16:02:32.881Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello

I would like to report an XSS happening in Transfer Timeline because the Supplier Name input is not sanitized as it should!

***POC***
Set Supplier Name to "><img src=x onerror=prompt('XSS')>
Create a Transfer with multiple items and cancel on of the items.
Review the timeline
In the timeline you will see `You canceled items in a shipment from SUPPLIER NAME` which since it is unsanitized it will trigger XSS

{F118573}
{F118574}

Live XSS is here https://whitehat-3.myshopify.com/admin/transfers/11073

Hope it will be triaged and fixed

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
