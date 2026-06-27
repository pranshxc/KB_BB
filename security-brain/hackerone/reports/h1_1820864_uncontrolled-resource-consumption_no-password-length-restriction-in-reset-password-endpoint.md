---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1820864'
original_report_id: '1820864'
title: No password length restriction in reset password endpoint
weakness: Uncontrolled Resource Consumption
team_handle: nextcloud
created_at: '2023-01-03T08:44:39.574Z'
disclosed_at: '2023-02-09T13:57:52.319Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# No password length restriction in reset password endpoint

## Metadata

- HackerOne Report ID: 1820864
- Weakness: Uncontrolled Resource Consumption
- Program: nextcloud
- Disclosed At: 2023-02-09T13:57:52.319Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, 

##Summary:
There is no password length restriction in reset password endpoint at https://efss.qloud.my/index.php/login when resetting for new password.


##Steps To Reproduce:
1. Visit https://nextcloud.com/sign-up/ and Sign up.

2. Logout and reset your password.

 3.Go to your email and click on reset password link.
4.Enter 150 characters or more as a password and confirm the characters.
5.You will successfully logged in.

## Impact

Attacker can do denial of service to your server since there is no restriction in the length of password.
Example when he enter like 2500 character, your server will crash for some time 
Below Image is the impact of entering 2500 characters.

##Mitigation :

Restrict user to use less than 40 character as a password, while the restriction should be both on back-end and front-end (with javascript ).

##THANK YOU

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
