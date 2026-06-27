---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '344145'
original_report_id: '344145'
title: '[www.zomato.com] IDOR - Gold Subscription Details, Able to view "Membership
  ID" and "Validity Details" of other Users'
weakness: Insecure Direct Object Reference (IDOR)
team_handle: zomato
created_at: '2018-04-28T06:02:35.953Z'
disclosed_at: '2018-04-28T11:35:17.190Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# [www.zomato.com] IDOR - Gold Subscription Details, Able to view "Membership ID" and "Validity Details" of other Users

## Metadata

- HackerOne Report ID: 344145
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: zomato
- Disclosed At: 2018-04-28T11:35:17.190Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Zomato,

The following URL : https://www.zomato.com/gold/payment-success?subscription_id=██████████&user_id=█████████ is vulnerable to IDOR in `subscription_id` field. Anyone can get Subscription Start & End Date and Plan Duration of a Membership ID just by changing the `subscription_id` parameter. 
{F291153}

MEMBERSHIP ID : ████
STARTED ON : 22 Dec 2017
VALID UP TO : 22 Jun 2018
Subscription Plan :  6 month plan

## Impact

Anyone can get Subscription Start & End Date and Plan Duration of a Membership ID.

___Cheers!
Riya___

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
