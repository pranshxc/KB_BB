---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '219215'
original_report_id: '219215'
title: Client can redirect payment, causing payment discrepancy between Harvest and
  PayPal
weakness: Business Logic Errors
team_handle: harvest
created_at: '2017-04-07T04:58:46.028Z'
disclosed_at: '2017-04-12T06:24:00.742Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
tags:
- hackerone
- business-logic-errors
---

# Client can redirect payment, causing payment discrepancy between Harvest and PayPal

## Metadata

- HackerOne Report ID: 219215
- Weakness: Business Logic Errors
- Program: harvest
- Disclosed At: 2017-04-12T06:24:00.742Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Vulnerability details
When a client views an invoice through the web interface, it'll show a "Pay with PayPal" button when a standard PayPal integration has been enabled. Clicking this button will submit a `POST` request to PayPal. This request contains a `business` parameter, which is the receiver of the funds. When the client would have two PayPal addresses, it can send money to itself, while the invoice in Harvest will be marked as paid. This causes a discrepancy between Harvest and PayPal.

# Proof of concept
To reproduce this vulnerability, make sure you've set up a Harvest account that has PayPal payments enabled. This can be done at `https://subdomain.harvestapp.com/invoices/configure#online_payment_edit`. After that, send an invoice to a client and make sure the web view is enabled. The client will receive an email with the invoice and will be able to view the invoice.

{F173955}

When the client clicks on the button, a request similar to the one shown below will be send to PayPal:

**Request**
```
...
----------1635625368
Content-Disposition: form-data; name="quantity"

1
----------1635625368
Content-Disposition: form-data; name="business"

paypal@myconsultancy.com
----------1635625368
Content-Disposition: form-data; name="item_number"

2
----------1635625368
Content-Disposition: form-data; name="item_name"

Invoice #2 from Michiel's Ranch - That second invoice you asked for!
...
----------1635625368--

```

The parameter to look out for is the `business` parameter. As can be seen in the request above, it contains the value the Harvest account holder has put in - paypal@myconsultancy.com. When the client (the attacker) changes this to a non-existing email address and checks out with its own PayPal account, it'll send the money to itself. After the checkout, the callback to Harvest will actually set the Harvest invoice to paid.

{F173957}

Even though I understand that it's the consultant's responsibility to double-check funds that've received in its PayPal account, it can cause a lot of fuss if the invoice in Harvest has been marked as paid and has a valid PayPal transaction ID linked to it. From what I've seen, it isn't possible to see where the money actually went. This may cause friction between the consultant and client if the client decides to go down this path.

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
