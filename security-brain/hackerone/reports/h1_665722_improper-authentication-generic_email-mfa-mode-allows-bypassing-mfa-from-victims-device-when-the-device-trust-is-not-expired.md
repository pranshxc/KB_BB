---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '665722'
original_report_id: '665722'
title: “email” MFA mode allows bypassing MFA from victim’s device when the device
  trust is not expired
weakness: Improper Authentication - Generic
team_handle: grammarly
created_at: '2019-08-02T02:55:13.236Z'
disclosed_at: '2019-08-12T18:19:39.032Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 66
asset_identifier: auth.grammarly.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# “email” MFA mode allows bypassing MFA from victim’s device when the device trust is not expired

## Metadata

- HackerOne Report ID: 665722
- Weakness: Improper Authentication - Generic
- Program: grammarly
- Disclosed At: 2019-08-12T18:19:39.032Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
It is possible bypass MFA without the need to have the phone code.

**Description:** 
When we turn on the MFA and we have the user and password of the user, it is possible bypass the MFA only changing some values the endpoint POST `auth.grammarly.com//v3/api/login`

## Steps To Reproduce:
Note: 
- Use burp suite or another tool to intercept the requests

  1. Turn on and configure your MFA
  2. Login with your email and password
  3. The page of MFA is going to appear
  4. Enter any random number
  5. when you press the button "sign in securely" intercept the request POST `auth.grammarly.com/v3/api/login` and in the POST message change the fields:
- `"mode":"sms"` by `"mode":"email"`
-  `"secureLogin":true` by `"secureLogin":false`
 6. send the modification and check, you are in your account! It was not necessary to enter the phone code.

## Impact

The attacker can bypass the experimental MFA, If the attacker has the email and password, the attacker can login in the account without the need of the phone code.

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
