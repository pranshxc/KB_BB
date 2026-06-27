---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1047124'
original_report_id: '1047124'
title: No rate limit in email subscription
weakness: Business Logic Errors
team_handle: stripo
created_at: '2020-11-30T15:27:54.948Z'
disclosed_at: '2021-01-11T08:48:14.718Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: stripo.email
asset_type: URL
max_severity: medium
tags:
- hackerone
- business-logic-errors
---

# No rate limit in email subscription

## Metadata

- HackerOne Report ID: 1047124
- Weakness: Business Logic Errors
- Program: stripo
- Disclosed At: 2021-01-11T08:48:14.718Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I managed to bypass the following report #1029723 please follow the steps below:

##Description:
No rate limit in Email Subscription, you just have to add a fixed throttle in Burp Suite to avoid the `429` response.

**Note:** I will use tempmail in the screenshots PoC

##Steps:

1. Go to https://stripo.email/ and scroll down to the subscribe field
2. Put an email
3. Click on `Subscribe` and intercept the following request

```
POST /fr/subscribe/ HTTP/1.1
Host: stripo.email
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-CSRF-TOKEN: OC5q3gnsKxUZRrGIN3ke5ZdqEbmneEuknaNmnQUe
X-Requested-With: XMLHttpRequest
Content-Length: 129
Origin: https://stripo.email
Connection: close
Referer: https://stripo.email/

_token=&source=LANDING&subscribe-email=kakema3700%40tdcryo.com&g-recaptcha-response=
```
4.Send the request to Burp intruder, go to the `Positions` tab and clear the `§`
5.Add `§` in the last number of the `Accept-Language` header like this`Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.§3§`
6.Go to `Payloads` tab and choose `Null payloads` in the `Payload type`
7.You can set how much email you want to send.. `50` for example in the `Generate` field
8.Go to `Options` tab and change the `Throttle (milliseconds)` Fixed value to **1500** or more..
9.Click on `Start attack`
You will start receiving emails.

##Suggested Mitigation:
Add a number of requests limit

## Impact

An attacker can send bulk emails to the victim

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
