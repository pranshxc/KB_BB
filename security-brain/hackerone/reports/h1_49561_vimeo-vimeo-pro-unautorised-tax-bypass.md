---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49561'
original_report_id: '49561'
title: Vimeo + & Vimeo PRO Unautorised Tax bypass
team_handle: vimeo
created_at: '2015-02-28T05:41:33.817Z'
disclosed_at: '2015-04-18T08:35:39.009Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# Vimeo + & Vimeo PRO Unautorised Tax bypass

## Metadata

- HackerOne Report ID: 49561
- Weakness: 
- Program: vimeo
- Disclosed At: 2015-04-18T08:35:39.009Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello !

I've found a Vuln' which allows to override the taxification applied when buying Vimeo + or Vimeo PRO (tested by selecting France as country)

Comparing data sent when attempting to purchase on demand movie, I noticed a field named "vin_Transaction_transactionItems_0_taxClassification" with the value "TaxExempt". No tax is present in the final purchase summary on paypal. (view Proof1 and Proof2 screencapture)

When attempting to purchase a Vimeo + account or Vimeo PRO, the same field exists, but the value are set to "OtherTaxable." In the end, we note in the purchase summary on paypal, in addition to the price account (49 € or 159 €), tax is added (in the amount of € 9.99 for vimeo+ account and € 31.80 for vimeo PRO account) (view proof3 screencapture)

Finally, in a statement attempted purchase Vimeo+ or  Vimeo PRO, if you set the field "vin_Transaction_transactionItems_0_taxClassification" to "TaxExempt" although we reach paypal and we see in the summary that taxes are not been added to the price. (view Proof4 and proof5 for VimeoPRO, view Proof6 and Proof7 for Vimeo+)

PoC Video : https://vimeo.com/user37862177/vimeo-tax-bypass-vulnerability

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
