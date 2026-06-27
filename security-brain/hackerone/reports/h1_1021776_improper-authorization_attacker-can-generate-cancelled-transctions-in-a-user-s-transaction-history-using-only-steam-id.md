---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1021776'
original_report_id: '1021776'
title: Attacker can generate cancelled transctions in a user's transaction history
  using only Steam ID
weakness: Improper Authorization
team_handle: cs_money
created_at: '2020-10-29T14:20:09.187Z'
disclosed_at: '2021-02-03T13:05:45.548Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 63
asset_identifier: cs.money
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# Attacker can generate cancelled transctions in a user's transaction history using only Steam ID

## Metadata

- HackerOne Report ID: 1021776
- Weakness: Improper Authorization
- Program: cs_money
- Disclosed At: 2021-02-03T13:05:45.548Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The API endpoint `/create-payment` requires only the steam ID of the account to create the payment. When this endpoint is called using the `cardpay` flow, it returns a transaction ID on the Cardpay system. The attacker can access this transaction, and immediately cancel it (or pay it ;) ), which leads to a visible cancelled transaction in the cs.money user's transaction history.

Although there is no impact to the user, they will certainly be confused.

## Steps To Reproduce:
Invoke the API call `/create-payment` as below:

```
POST https://cs.money/create-payment HTTP/1.1
Host: cs.money
Content-Type: application/json;charset=UTF-8
Cookie: steamid=████████; 

{"merchant":"cardpay","amount":10}
```

You will get a response with a Cardpay order ID and URL:
```
HTTP/1.1 200 OK
...
{"merchant":"cardpay","orderId":2034944,"success":true,"url":"https://cardpay.com/MI/payment.html?uuid=DaG438Bda6GC13h5db1bGD01"}
```

You can then cancel the payment by hitting the Cardpay cancel URL:
```
https://cardpay.com/MI/cancel.html?uuid=DaG438Bda6GC13h5db1bGD01
```

This will result in a cancelled transaction showing in the user's transaction history of the amount specified by the attacker. The attacker could repeat this numerous times until the account is banned by cs.money (this occurred on one of my test accounts).

## Impact

Confusion for the user due to the ability to create many cancelled transactions, potentially leading to the account being banned.

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
