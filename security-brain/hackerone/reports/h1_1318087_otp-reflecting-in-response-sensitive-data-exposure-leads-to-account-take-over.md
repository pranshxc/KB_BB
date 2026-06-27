---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1318087'
original_report_id: '1318087'
title: OTP reflecting in response sensitive data exposure leads to account take over
team_handle: upchieve
created_at: '2021-08-24T17:10:12.743Z'
disclosed_at: '2022-03-26T18:00:23.038Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
tags:
- hackerone
---

# OTP reflecting in response sensitive data exposure leads to account take over

## Metadata

- HackerOne Report ID: 1318087
- Weakness: 
- Program: upchieve
- Disclosed At: 2022-03-26T18:00:23.038Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
Sensitive data that is otp is reflecting in the response of phone number otp verification in https://app.upchieve.org 

## Steps To Reproduce:


  1. Signin with a account
  2.After signin it will ask for phone number for otp verification.
3.Capture the request using burpsuite and see the response 
4.Now otp is exposing in the response.
5.Account take over is happening.

## Impact

Any attacker can login into user account with his/her otp verification which is a high impact of this website.sensitive data is exposing here

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
