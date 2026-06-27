---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '29234'
original_report_id: '29234'
title: Credit Card Validation Issue
team_handle: coinbase
created_at: '2014-09-27T04:34:52.509Z'
disclosed_at: '2015-03-12T19:01:21.440Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# Credit Card Validation Issue

## Metadata

- HackerOne Report ID: 29234
- Weakness: 
- Program: coinbase
- Disclosed At: 2015-03-12T19:01:21.440Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Coinbase, I'm not sure if this counts as a bug, but it definitely counts as a vulerability.  The issue is in your credit card verification for instant purchases.  The system does not (or rarely) check the validity of a credit card after it is added.  This allows me to make instant buy purchases, without the need for a working credit card.

After I add my credit card, I can cancel it, either specifically to exploit coinbase, or another situation (like if it gets stolen) where one would cancel their card.  The system currently has no way to determine if a credit card is still active after it is validated the first time.  I still can instant buy, and if my bank transfer either maliciously or non-maliciously fails, the credit card will also fail.

This leads to a potential loss of funds and I believe it is in scope.  Please let me know if this is incorrect.

Thanks,

Whit

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
