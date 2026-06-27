---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17502'
original_report_id: '17502'
title: Price Manipulation
weakness: Violation of Secure Design Principles
team_handle: uzbey
created_at: '2014-06-25T06:41:40.368Z'
disclosed_at: '2014-08-29T20:51:56.882Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Price Manipulation

## Metadata

- HackerOne Report ID: 17502
- Weakness: Violation of Secure Design Principles
- Program: uzbey
- Disclosed At: 2014-08-29T20:51:56.882Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey guys,

I put this down as a 2nd bug as it may have been overlooked from the previous report and I figured it'd be easier to track a fix and add comments separately...

When completing an order it looks like it may be possible to pay an arbitrary amount - what happens is a request is generated to Paypal such as...

https://www.paypal.com/cgi-bin/webscr?cmd=_cart&charset=utf-8&notify_url=https://staging.uzbey.com/uc_paypal/ipn/147&cancel_return=https://staging.uzbey.com/uc_paypal/wps/cancel&no_note=1&no_shipping=1&return=https://staging.uzbey.com/uc_paypal/wps/complete/147&rm=1&currency_code=USD&handling_cart=0.00&invoice=147-340&tax_cart=0.00&business=uzbey.securatary-facilitator@gmail.com&upload=1&lc=US&country=US&email=dmchell@gmail.com&paymentaction=authorization&amount_1=0.00&item_name_1=128x128%20Square&item_number_1=128X128&quantity_1=2&on0_1=Price%20for%20128X128%20Sqaure&os0_1=20%20additional%20squares&amount_2=0.00&item_name_2=128x128%20Square&item_number_2=128X128-1-128&quantity_2=1&on0_2=Price%20for%20128X128%20Sqaure&os0_2=1%20additional%20square&amount_3=&item_name_3=&item_number_3=&quantity_3=&on0_3=&os0_3=&form_build_id=form-qllawsSylHhupaCP_DDy8XKN0rTD3vtE4QCVMG2inSw&form_token=nLeB9irRa2t_rckebJLbgi_JU3saATtFi_Fw5FrGISs&form_id=uc_paypal_wps_form&op=form-qllawsSylHhupaCP_DDy8XKN0rTD3vtE4QCVMG2inSw

If we intercept and modify this there are a few amount fields (which I set to 0.00 in this example)and it appears to be able to let me set an arbitrary price that I want to pay on the transaction :)

I have tried to complete the payment with payment for a smaller amount and it errored - but it's the same error I get when trying to complete a payment without any tampering and with valid info - so I can only assume that this doesnt work in staging? I tried card payments also with valid info and they too failed. So overall it's difficult to say this bug exists because the payment code doesn't seem to fully work, but I suspect it does :)

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
