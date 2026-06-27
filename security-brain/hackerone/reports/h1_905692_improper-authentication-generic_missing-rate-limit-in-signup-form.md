---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '905692'
original_report_id: '905692'
title: Missing rate limit in signup Form
weakness: Improper Authentication - Generic
team_handle: trycourier
created_at: '2020-06-22T21:34:47.895Z'
disclosed_at: '2020-07-28T22:51:46.926Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: www.trycourier.app
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Missing rate limit in signup Form

## Metadata

- HackerOne Report ID: 905692
- Weakness: Improper Authentication - Generic
- Program: trycourier
- Disclosed At: 2020-07-28T22:51:46.926Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team ,
##Description 
When signing up for an account, you enter your email. When this email is already in use, the server
 responds with 
``
{"UserConfirmed":true,"UserSub":"ae294fff-6d55-407d-9676-1f3518029037"}
``
This in not a problem, but the fact that you could send this request unlimited times is the issue.

This way we can easily get a list of all users emails signed up at" trycourier App" .
 
Vulnerable Endpoint :https://www.trycourier.app/register/email

POC : Watch The Video Please .

Link OF POC in Video : https://drive.google.com/file/d/1aA6MHjLx5u29RhzqOZzlNqKYuOPbwBrE/view?usp=sharing

Now i have 200 responses with status 200 .

that 's mean that i have created 200 new account

when the request repeat with same email it response with 500 
``
{"__type":"UsernameExistsException","message":"An account with the given email already exists."}
``
that mean it just in the Bucket  [recorded in DB ].

##Fix

to fix this issue, you could implement an timeout after a number of requests in a period of time.

to return "429 Too Many Requests" when making multiple requests in a short period of time

or use capatcha .

## Impact

the attacker can make for example 1 M request that lead to fill your DB with fake accounts .

report From H1 : https://hackerone.com/reports/275186

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
