---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1165225'
original_report_id: '1165225'
title: '[dubsmash] Username and password bruteforce'
weakness: Improper Restriction of Authentication Attempts
team_handle: reddit
created_at: '2021-04-14T20:04:50.188Z'
disclosed_at: '2021-12-13T22:48:54.994Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: www.dubsmash.com
asset_type: URL
max_severity: low
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# [dubsmash] Username and password bruteforce

## Metadata

- HackerOne Report ID: 1165225
- Weakness: Improper Restriction of Authentication Attempts
- Program: reddit
- Disclosed At: 2021-12-13T22:48:54.994Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Due to less complexity of password and no rate limiting attacker can bruteforce user name and password and takeover the victim account

Login Page- No rate limits
Password length is minimum five character with no variations. Plain  password are easy to bruteforce 
Reset Password page- No rate limits

Attacker can send as many request with no restrictions

## Impact:
Account takeover

## Steps To Reproduce:


  1. To get the username attacker bruteforce through reset password page with selecting email parameter
 2. It shows 200 status for every request but 

for valid user it respond with {status :true}

{"data":{"resetPassword":{"status":true,"__typename":"ResetPasswordOutput"}}}

For invalid user

{"data":{"resetPassword":{"status":false,"__typename":"ResetPasswordOutput"}}}

 3.Login with victim email and any password.
4.Intercept request with burp and send to intruder with selecting password parameter
6.Load the desired password list and start attack
7.It shows status 200 for every request but for valid password it gives jwt token in response
  

## Supporting Material/References:

f_user.jpg: Username is invalid
r_user.jpg: Right username is found.
r_pass.jpg: Valid password is found.

  * [attachment / reference]

## Impact

Account take over even if the user password is  long but not complex.

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
