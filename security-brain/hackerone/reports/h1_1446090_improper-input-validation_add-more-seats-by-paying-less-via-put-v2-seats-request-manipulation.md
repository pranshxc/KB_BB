---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1446090'
original_report_id: '1446090'
title: Add more seats by paying less via PUT /v2/seats request manipulation
weakness: Improper Input Validation
team_handle: krisp
created_at: '2022-01-11T02:51:39.239Z'
disclosed_at: '2022-06-20T15:41:33.357Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: account.krisp.ai
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# Add more seats by paying less via PUT /v2/seats request manipulation

## Metadata

- HackerOne Report ID: 1446090
- Weakness: Improper Input Validation
- Program: krisp
- Disclosed At: 2022-06-20T15:41:33.357Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I could not fully test this vulnerability because the test plan must be completed for the payment process, that is, 30 days. But the price value in api also changes and if payment is made according to this value, wrong billing will occur.

The annual pro option for Team plan billing is $60 per seat. However, if the user enters a decimal number instead of an integer while adding a seat, the number is rounded up, but the price is only multiplied by the integer part. For example it would be like this :

```javascript
seats = 5
amount = 300
bady.seats = 1.1

seats += Math.ceil(bady.seats)
// 5  +=             2
// seats : 7 

amount += Math.floor(bady.seats) * 60
// 300 +=                 1      * 60
// amount : 360 
```

## Steps To Reproduce:

* Register the app and finish the installation. [help document](https://help.krisp.ai/hc/en-us/articles/360017564739-Creating-a-Krisp-personal-account)
* Create a new team.
* Go to billing and listen to traffic with burp.
* Add seat and capture the request with burp.
* Replace the number of seats with 1.9 
* You will see that you have added 2 seats but the price has increased by $60.

We can reduce the price by adding and deleting seats.

Poc video -|

{F1574747}

## Impact

Attacker can manipulate membership price

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
