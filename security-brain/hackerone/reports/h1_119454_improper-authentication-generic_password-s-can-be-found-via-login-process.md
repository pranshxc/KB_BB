---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119454'
original_report_id: '119454'
title: Password(s) can be found via login process.
weakness: Improper Authentication - Generic
team_handle: veris
created_at: '2016-02-29T13:46:01.134Z'
disclosed_at: '2016-05-13T16:24:03.447Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Password(s) can be found via login process.

## Metadata

- HackerOne Report ID: 119454
- Weakness: Improper Authentication - Generic
- Program: veris
- Disclosed At: 2016-05-13T16:24:03.447Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello security team,

It is possible to find password(s) of other users by enumerate the login process.
The scenario is quiet simple:
1) Go to https://sandbox.veris.in/portal/login/
2) Fill in 'Email ID' and 'Password' and click 'Log In'
3) Capture the request via burp suite and send it to intruder.
4) Set the password field to be enumerate.
5) Set wordlist and run the request(s).

Analyze the results:
1) For 'Good password' you'll get Status code of 200 and code length of 573.
2) For 'Bad password' you'll get Status code of 400 and code length of 507.

Solutions:
1) Set status code and code length to be the same for all requests/response.
2) Set captua after X attempts.
3) Block IP/user
4) Send reset password email.

I run around ~5K words.

Best regards,
Sasi

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
