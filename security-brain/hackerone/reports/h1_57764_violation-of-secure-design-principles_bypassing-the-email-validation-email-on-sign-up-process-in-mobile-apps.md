---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '57764'
original_report_id: '57764'
title: ByPassing the email Validation Email on Sign up process in mobile apps
weakness: Violation of Secure Design Principles
team_handle: coinbase
created_at: '2015-04-22T14:41:56.344Z'
disclosed_at: '2016-11-28T18:13:55.836Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# ByPassing the email Validation Email on Sign up process in mobile apps

## Metadata

- HackerOne Report ID: 57764
- Weakness: Violation of Secure Design Principles
- Program: coinbase
- Disclosed At: 2016-11-28T18:13:55.836Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

According to the design When the new user sign up using mobile apps(android,ios).It will ask for the confirmation of the email.It will send a confirmation mail to mail id and a screen will also appear in the mobile app. The user needs to open the email in the device then the screen will Off and user will successfully login.

Bypass:

Here simply we can bypass this validation and can successfully login to the application without verifying the validation email which comes to the user.Using this the attacker can create so many spoofed accounts.

1.Sign for new user using email id and password
2.Next screen will appear saying please click on the validation which sent to proceed further
3.Here in the second screen click the back button now you will go to Login screen
4.Now login with the creds which you have given in the registration process
5.Now you will successfully login to the application
6.Here it is not asking for email verification email.

Pls follow above procedure to reproduce the issue.

Pls respond to remaining bugs which I had reported 

Thanks,
kaleem

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
