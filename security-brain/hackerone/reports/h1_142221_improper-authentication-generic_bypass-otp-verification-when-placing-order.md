---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '142221'
original_report_id: '142221'
title: Bypass OTP verification when placing Order
weakness: Improper Authentication - Generic
team_handle: zomato
created_at: '2016-05-31T08:51:40.597Z'
disclosed_at: '2016-06-01T07:28:35.916Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- improper-authentication-generic
---

# Bypass OTP verification when placing Order

## Metadata

- HackerOne Report ID: 142221
- Weakness: Improper Authentication - Generic
- Program: zomato
- Disclosed At: 2016-06-01T07:28:35.916Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

User can bypass the OTP verification needed while placing an order with a restaurant. User can give a random number and intercept the OTP request. If wrong OTP is provided then the error message shows the session code which is the OTP in this case. Hence that session code can be used to verify the phone number and the order can be placed.
Similarly,by intercepting the final order placing request,one can change the number and place N number of orders with restaurant.

Please Refer to the attached POC.

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
