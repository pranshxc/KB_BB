---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '783258'
original_report_id: '783258'
title: 2-factor authentication can be disabled when logged in without confirming account
  password
weakness: Business Logic Errors
team_handle: localizejs
created_at: '2020-01-25T17:17:25.773Z'
disclosed_at: '2020-02-10T15:36:39.970Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 144
asset_identifier: localizestaging.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# 2-factor authentication can be disabled when logged in without confirming account password

## Metadata

- HackerOne Report ID: 783258
- Weakness: Business Logic Errors
- Program: localizejs
- Disclosed At: 2020-02-10T15:36:39.970Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
===
When users wants to Disable his/her TwoFactor Authentication, they have to know their account password. But using this vulnerability They don't need password to disable it. this will allow hacker who get someone cookie to disabling twofactor auth and also Fullytakeover the account.

How To Reproduce
===
1. Open Your BurpSuite and Turn on the intercept
2. Go To 2Factor Authentication page click the red buttons "Disable two factor ...."
3. Put any wrong password and copy all the header
4. Go to repeater and make a POST request to `https://localizestaging.com/api/user/two-factor/set` also Paste the header here.
5. add a body request like this `method=sms&phone=%2B62-hacker-phone-number` then click GO
6. Bypassed !

## Impact

disable twofactor authentication without needing to know the password

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
