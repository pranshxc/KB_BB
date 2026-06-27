---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '422331'
original_report_id: '422331'
title: attacker can book unlimited tickets in free at https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2
weakness: Business Logic Errors
team_handle: aaf
created_at: '2018-10-11T07:10:09.324Z'
disclosed_at: '2019-04-25T04:57:10.936Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 63
asset_identifier: aaf.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# attacker can book unlimited tickets in free at https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2

## Metadata

- HackerOne Report ID: 422331
- Weakness: Business Logic Errors
- Program: aaf
- Disclosed At: 2019-04-25T04:57:10.936Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear Team,

**Summary:** [add summary of the vulnerability]
After looking into https://aaf.com/
i get to know that there is way where i can book a ticket and can play around , but it asked for valid credit card and all stuff
so , i tried to bypass and bought a ticket 23 with 0$

Live PoC:
https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2  (check this one)

**Description:** [add more details about this vulnerability]
attacker can book unlimited tickets in free at https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2

## Steps To Reproduce:

1. go to aaf.com and login with your account
2. click on ticket option and select San Antonio Commanders Season and click on that and select 3 or any ticket and intercept that request ,
and change from 3-seats-3 to 10-seats-10
{F358789}
snip:

```
Content-Disposition: form-data; name="addon-268-number-of-seats-0"

10-seats-10
```
{F358788}
3. click on add tickets and you can see your order is 0$

and book any number of ticket at 0$

## Supporting Material/References:

Please find attachment

Thanks,
Vishal

## Impact

attacker can book unlimited tickets in free at https://aaf.com/checkout/order-received/21237/?key=wc_order_5bbef48fa35b2

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
