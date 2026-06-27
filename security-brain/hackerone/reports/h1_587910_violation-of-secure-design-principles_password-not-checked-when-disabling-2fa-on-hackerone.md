---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '587910'
original_report_id: '587910'
title: Password not checked when disabling 2FA on HackerOne
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2019-05-22T17:19:54.372Z'
disclosed_at: '2019-06-07T22:28:55.689Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 82
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Password not checked when disabling 2FA on HackerOne

## Metadata

- HackerOne Report ID: 587910
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2019-06-07T22:28:55.689Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

when I was submitted a report to a program that request `2FA` ON, I notice that if you try to disable this option will ask for `backup code - password` and if you enter a random password in the request filed and a correct `backup code` it will be successfully disabled the `2FA` without check if the password was correct or not.

#PoC
1. go to your account and activate the `2FA` from `/settings/auth`
2. after active this option click on `Disabled` icon beside `Two-factor authentication`.
3. a new window will open asking for `Authentication or backup code - Password` to confirm the disabled.
{F494646}
4. in the first box enter a valid `Authentication or backup code` and in the password filed enter any random/wrong password and click save.
5. the option will be disabled successful without check the validation of the password.
 
#graphql Request
```json

{"query":"mutation Destroy_two_factor_authentication_credentials_mutation($input_0:DestroyTwoFactorAuthenticationCredentialsInput!,$first_1:Int!,$throttle_time_2:Int!,$first_4:Int!,$size_3:ProfilePictureSizes!) {destroyTwoFactorAuthenticationCredentials(input:$input_0) {clientMutationId,...F1,...F2}} fragment F0 on User {id,totp_supported,totp_enabled,remaining_otp_backup_code_count,account_recovery_phone_number,username,name,_profile_picturePkPpF:profile_picture(size:$size_3)} fragment F1 on DestroyTwoFactorAuthenticationCredentialsPayload {me {id,user_type,_program_health_acknowledgements2aGZgn:program_health_acknowledgements(first:$first_1,throttle_time:$throttle_time_2) {edges {node {id,reason,team_member {user {id},id,team {handle,name,sla_failed_count,id}}},cursor},pageInfo {hasNextPage,hasPreviousPage}},new_feature_notification {name,description,url,id},...F0}} fragment F2 on DestroyTwoFactorAuthenticationCredentialsPayload {me {totp_enabled,remaining_otp_backup_code_count,id},was_successful,_errors3exXYb:errors(first:$first_4) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}",
"variables":{"input_0":{"password":"██████████","otp_code":"███","clientMutationId":"9"},"first_1":1,"throttle_time_2":3600,"first_4":100,"size_3":"small"}}
```

## Impact

user can disable `Two-factor authentication` without entering a valid password

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
