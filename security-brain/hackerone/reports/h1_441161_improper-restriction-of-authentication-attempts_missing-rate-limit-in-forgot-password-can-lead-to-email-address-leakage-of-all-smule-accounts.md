---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '441161'
original_report_id: '441161'
title: Missing Rate Limit in Forgot Password can Lead to email address leakage of
  all smule accounts
weakness: Improper Restriction of Authentication Attempts
team_handle: smule
created_at: '2018-11-15T10:55:59.936Z'
disclosed_at: '2019-05-13T15:32:49.080Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
asset_identifier: '*.smule.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Missing Rate Limit in Forgot Password can Lead to email address leakage of all smule accounts

## Metadata

- HackerOne Report ID: 441161
- Weakness: Improper Restriction of Authentication Attempts
- Program: smule
- Disclosed At: 2019-05-13T15:32:49.080Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Smule,

I have found a vulnerability by which an attacker can get access of all the gmail accounts associated with Smule. The forgot password parameter can be brute forced through which an attacker can get the email address.

##Steps to Reproduce

> Enter your email address and for the forgot password parameter.
> Capture the request in the proxy.
> Brute for the parameter using different email address.
> Check the different request and see the response.

The right email and the wrong email will have different response and request length. Hence, the attack is successful.

## Impact

The impact is obvious here. As you can see, the vulnerability is about the email address leakage of the smule accounts. The email address leakage of the account is said to be prohibited. The confidential data of the Smule application can be leaked.

###Mitigation

Add rate limit on the application.
Use CAPTCHA verification if many request is sent.

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
