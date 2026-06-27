---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243049'
original_report_id: '243049'
title: Call back number not verified
weakness: Business Logic Errors
team_handle: airbnb
created_at: '2017-06-25T14:58:59.408Z'
disclosed_at: '2017-07-20T21:53:29.165Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- business-logic-errors
---

# Call back number not verified

## Metadata

- HackerOne Report ID: 243049
- Weakness: Business Logic Errors
- Program: airbnb
- Disclosed At: 2017-07-20T21:53:29.165Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The issue is with the "Confirm via call functionality" 

While adding mobile number,the application does not verify the number that is being called back. A malicious user can change the number to any premium rate numbers which charge particular amount from the caller.

It was further noticed that there was not limit to number of tries that can be made from the application. Even if the call is answered, same request can be used multiple times and the application still calls back.

The attached screenshot shows that the phone number value can be changed and premium rate numbers can be used. The number used while testing is a test call number for Eurocall24 (premium number provider).

An attacker can thereby steal money by manipulating the request to make call to premium numbers.

Affected functionality:  /phone_numbers/create

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
