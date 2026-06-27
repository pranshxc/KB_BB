---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '64666'
original_report_id: '64666'
title: Bypass verification of email while creating account(No rate limiting enable
  for verification code)
weakness: Improper Authentication - Generic
team_handle: maplogin
created_at: '2015-05-29T19:53:43.315Z'
disclosed_at: '2016-08-25T22:59:21.848Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- improper-authentication-generic
---

# Bypass verification of email while creating account(No rate limiting enable for verification code)

## Metadata

- HackerOne Report ID: 64666
- Weakness: Improper Authentication - Generic
- Program: maplogin
- Disclosed At: 2016-08-25T22:59:21.848Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Bug type : Authentication bypass(Missing rate limiting)

Description : While creating a account user needs to enter a email id and verification has been sent to his email ID.It is a 4 digits code.But there is no rate limiting enable while checking the verification on server side.So basically Any one can use account by any email ID in the world.

Exploite : 
1.Attacker creates a account with victim's email ID Ex: victim@gmail.com
2.Now he doesn't know the verification code.Attacker will start brute force attack to get the correct verification code.Once Attacker gets the verification code,He will be able to use the Email id of victim on Maplogin account.


Solution : Enable rate limiting on verifying the code (Ex: User can try only 10 times after that he's blocked for sometime)

This is a critical authentication issue,kindly look into it asap.

Regards !

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
