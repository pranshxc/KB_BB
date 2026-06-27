---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '62427'
original_report_id: '62427'
title: XSS in myshopify.com Admin site in TAX Overrides
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-05-14T17:15:39.076Z'
disclosed_at: '2015-06-09T20:55:33.836Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in myshopify.com Admin site in TAX Overrides

## Metadata

- HackerOne Report ID: 62427
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-06-09T20:55:33.836Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

POC:
If you create a collection such as "><IMG SRC=x onerror=prompt(7)> and then go to Settings / Taxes and select "Add a tax override" then on the "Add Tax Override for Rest of World" select the previously created collection of "><IMG SRC=x onerror=prompt(7)> you can see it on the screen (addtax.png).

If you press the recycle bin "Delete Entire Override" (delete.png) then  XSS is happening (xss.png)

Thanks

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
