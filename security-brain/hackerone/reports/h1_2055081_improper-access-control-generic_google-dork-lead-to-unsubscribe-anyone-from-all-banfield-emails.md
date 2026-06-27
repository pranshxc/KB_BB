---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2055081'
original_report_id: '2055081'
title: Google dork lead to unsubscribe anyone from all Banfield emails
weakness: Improper Access Control - Generic
team_handle: mars
created_at: '2023-07-07T14:04:18.464Z'
disclosed_at: '2023-08-30T15:45:38.308Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: '*.banfield.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Google dork lead to unsubscribe anyone from all Banfield emails

## Metadata

- HackerOne Report ID: 2055081
- Weakness: Improper Access Control - Generic
- Program: mars
- Disclosed At: 2023-08-30T15:45:38.308Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi there,

while checking on shodan i found an ip "13.111.140.217" which was issued to info.banfield.com.

and this was giving me 404 status code. while checking on web archive i found out some link like:

https://info.banfield.com/unsub-confirm?qs=9546b5587fbb95c5b3a14830c24ac1fe1c121408594657fcede21ae3dc4d5f308e77e063c684899e30e2a0eaadb128905d44ba371e41050fd4817ae60ed2fece919c87e1bca306f5

when i did a google search i found out the endpoint for unsubscribe where i can unsubscribe any banfield users from their email without authentication and authorization.

endpoint: https://info.banfield.com/unsub?EmailAddress=█████████

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. do a google dork site:info.banfield.com
  1.click on second link and it will direct you to https://info.banfield.com/unsub?EmailAddress=████████
  1. put authenticated user email and confirm. This will lead to unsubscribe them from banfield emails.

For user enum or email enum this can be done from 

POST /Security/SendClientIdMail HTTP/2
Host: www.banfield.com
Cookie: ███████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.banfield.com/
Content-Type: application/x-www-form-urlencoded; charset=utf-8
X-Requested-With: XMLHttpRequest
Content-Length: 159
Origin: https://www.banfield.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

__RequestVerificationToken=qBYfU3x7qqHqWdyKBzxZxsmqgsz2EDemFmpfyys2agu6FhVHrRQ_v2p7n40f7N46t3a9n51kgkkxQJN2qrNEX0JLMYo1&email=█████████&returnUrl=

On this there is no rate limit so email enum can be done.

## Supporting Material/References:
██████████

  * [attachment / reference]
I added screen shot as a proof of concepts. 

Thank you very much. Wish you a good day.

## Impact

Can unsubscribe anyone from all Banfield emails

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
