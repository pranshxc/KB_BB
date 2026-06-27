---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47384'
original_report_id: '47384'
title: Approve topup method by sender of this method
weakness: Improper Authentication - Generic
team_handle: mobilevikings
created_at: '2015-02-11T02:33:08.357Z'
disclosed_at: '2015-03-04T14:17:51.954Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Approve topup method by sender of this method

## Metadata

- HackerOne Report ID: 47384
- Weakness: Improper Authentication - Generic
- Program: mobilevikings
- Disclosed At: 2015-03-04T14:17:51.954Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

user A has a sim and send auth request to user B
user B accepted it and decide to add to shared sim own topup method
user B goes to https://mobilevikings.be/en/account/easypay/auto-sms-topup/  - select shared sim card and select method in section "Choose a payment method" and submit form.
User A get an email with link and get a reminder about this request on website.

link from the mail - https://mobilevikings.be/en/account/easypay/request/approve/scQxc0PMTjRF2G7CrWY69nzUcKxPn9/

link from the https://mobilevikings.be/en/account/requests/#easypay -> https://mobilevikings.be/en/account/easypay/request/287740/approve/1036392/

Let's open this link in context of user B session - he sent this method and user A should accept it not user B
Link from mail - 404 error - good
Link from request page - Easy Payment authorization request approved - ?????!!!!! ( i tested on absolutely another user - and got 404 error, so this work only in context of sender or recipient) 
Let's look closer on request which made by user B to sent this method to user A
POST /en/account/easypay/auto-sms-topup/ HTTP/1.1

csrfmiddlewaretoken=AlEqSERKOXKjZfSdw2WtPY4l7n5b68BM&sim_card=subscription-1036392&payment_method=debtor_287740&name=&birthdate=&iban=&bic=&topup_when_calling_credit_below_treshold_amounts=0

sim_card=subscription-1036392 and payment_method=debtor_287740 - all info for approve request in sender request.

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
