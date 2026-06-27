---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1040373'
original_report_id: '1040373'
title: 'Password authentication when changing information bypass. Bypass of report
  #721341'
weakness: Unverified Password Change
team_handle: khanacademy
created_at: '2020-11-22T01:40:47.181Z'
disclosed_at: '2021-02-11T23:08:27.883Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- unverified-password-change
---

# Password authentication when changing information bypass. Bypass of report #721341

## Metadata

- HackerOne Report ID: 1040373
- Weakness: Unverified Password Change
- Program: khanacademy
- Disclosed At: 2021-02-11T23:08:27.883Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#SUMMARY
When reading the disclosed reports of your program, i see this one report #721341 . The reporter reported a lack of password confirmation when linking accounts. A fix was applied, adding password confirmation when linking account to other services. But i found a way to bypass this, The password confirmation is only done in the client side. This is bad because such methods are vulnerable to response manipulation. I will add a video poc 

#STEPS TO REPRODUCE
1. Open a browser in which a user has previously logged into an account, but hasn't logged out.
2. Open another browser and login using your account
3. Try to link gmail using your account, it will prompt for a password confirmation, enter your password
4. Intercept the response and copy it
5. Go to the victims account and link to gmail again
6. This time enter any password and intercept response
7. Paste the copied response from the attacker account

#POC
██████████

## Impact

An attacker can take over an account and lock a user out by resetting the password.

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
