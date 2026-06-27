---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143291'
original_report_id: '143291'
title: Password Reset Does Not Confirm the Existence of an Email Address
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-06-06T11:10:09.168Z'
disclosed_at: '2016-06-07T22:16:35.093Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Password Reset Does Not Confirm the Existence of an Email Address

## Metadata

- HackerOne Report ID: 143291
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-06-07T22:16:35.093Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

issue:
1.click forget password as driver or rider [https://login.uber.com/login]
2.input an email which not signed up! 
3. press reset password. 
there will be 'We've sent you an email with a link to reset your password.' message. 

because it can not verify email is signed up or not! 

I'd tried with my personal email. I got the message in webpage but did not get any further email from Uber. 
is that another bug?

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
