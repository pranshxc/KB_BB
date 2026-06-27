---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '777957'
original_report_id: '777957'
title: OTP bypass - Unintended disclosure of OTP to client allows attacker to manage
  users' subscriptions
weakness: Incorrect Authorization
team_handle: mtn_group
created_at: '2020-01-19T18:32:44.020Z'
disclosed_at: '2020-04-11T19:29:27.770Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: mtnplay.co.za
asset_type: URL
max_severity: critical
tags:
- hackerone
- incorrect-authorization
---

# OTP bypass - Unintended disclosure of OTP to client allows attacker to manage users' subscriptions

## Metadata

- HackerOne Report ID: 777957
- Weakness: Incorrect Authorization
- Program: mtn_group
- Disclosed At: 2020-04-11T19:29:27.770Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
https://play.mtn.co.za/ authenticates subscribers via OTP before their subscriptions to be changed. However, the request which sends the OTP also returns the OTP in the network response, allowing an attacker to manage a user's usbscriptions.

## Steps To Reproduce:
  1. Visit https://play.mtn.co.za/ and open network inspector (e.g., in Chrome)
  2. Type in a subscriber's number (here, I used a random number, 0787765562)
  3. Type in the `otpKey` in the network response into the OTP prompt field on the website
  4. The OTP prompt field has been bypassed

## Supporting Material/References:

* F689609 - Example of a network response

## Impact

Change a user's subscriptions. This might also be part of a larger issue if the send-otp/ endpoint is used elsewhere.

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
