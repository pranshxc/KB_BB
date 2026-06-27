---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '94899'
original_report_id: '94899'
title: Paid account can review\download any invoice of any other shop
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-10-20T20:15:09.077Z'
disclosed_at: '2015-10-22T20:44:39.830Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Paid account can review\download any invoice of any other shop

## Metadata

- HackerOne Report ID: 94899
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-10-22T20:44:39.830Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Shopify Team
I would like to report serious security issue within admin panel of Paid Myshopify account
Paid Customer [after been detached from Development account and valid payment detailes entered] able to review any other invoice, issues to any other client, and download it.
In web variant of invoice, financial details revealed.
**In PDF variant - address of web shop, owner's email and all billing information [name\address\money amount etc] disclosed **

POC:
1. Authenticate in Paid [not Developer] Shop as Shop Owner 
2. Go to invoices and alter url by changing invoice number at the end of URL:     

          hxx0s://myshop.myshopify.com/admin/settings/account/invoice/1746632

 3. To download PDF and review other paid user's data, use link:

            hxx0s://myshop.myshopify.com/admin/invoices/1746632.pdf

Please note, that due to limitation of Developer's account, this test cannot be performed on Dev store. 
I also prefer do not attach any screenshots or files, since it will be violation of valid customer's privacy.
If anyway more details needed - please feel free to contact me here for more POC details.
Regards
dvl

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
