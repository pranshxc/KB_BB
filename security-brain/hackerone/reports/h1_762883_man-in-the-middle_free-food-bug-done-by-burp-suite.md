---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '762883'
original_report_id: '762883'
title: Free food bug done by burp suite
weakness: Man-in-the-Middle
team_handle: zomato
created_at: '2019-12-21T15:32:33.300Z'
disclosed_at: '2019-12-26T12:48:10.113Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 17
asset_identifier: www.zomatobook.com
asset_type: URL
max_severity: none
tags:
- hackerone
- man-in-the-middle
---

# Free food bug done by burp suite

## Metadata

- HackerOne Report ID: 762883
- Weakness: Man-in-the-Middle
- Program: zomato
- Disclosed At: 2019-12-26T12:48:10.113Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** [By this Vulnerability we can get free food]

**Description:** [This vulnerability is done by paytm wallet]

**Platform(s) Affected:** [www.Zomato.com]

## Browsers Verified In [If Applicable]:

  * [Chrome and version 79.0.3945.88]
  

## Steps To Reproduce:

1. [REQUIRMENTS
1.PC/LAPPY 
2.os Kali
3.burp pro
4. paytm wallet]

  2. [setup burpsuite
create zomato id 
make your cart go to checkout selet paytm wallet option]
  3. [turn on intercept 
refresh the page 
go on params section
do a transaction of any low amount first and capture checksum key copy and save it]
4.[After copying that go to site and add some food to your cart make your food cart ready 
 And go to payment page and refresh the payment page and capture the packets in burp suite]
5.[go to params change the cost value 
and checksum value + time  by the previous one that u saved it 
and forward the request payment will go successfulll]


## Supporting Material/References:

  I dont have screenshots sorry

## Impact

By this u can Book free food and atacker can enjoy freely

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
