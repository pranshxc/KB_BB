---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '64626'
original_report_id: '64626'
title: Not Completed Accounts Take Over (Urgent bug)
weakness: Improper Authentication - Generic
team_handle: maplogin
created_at: '2015-05-29T18:43:47.049Z'
disclosed_at: '2015-06-09T17:36:31.625Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Not Completed Accounts Take Over (Urgent bug)

## Metadata

- HackerOne Report ID: 64626
- Weakness: Improper Authentication - Generic
- Program: maplogin
- Disclosed At: 2015-06-09T17:36:31.625Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello MapLogin Security Team, 

I just found a problem in Authentication for you.
Attacker Can take over any accounts that "Not Completed Yet" by easy way and here is the details:

1- From any browser you can register using your email "diaa.diab.2012@gmail.com"
2- You will recieve a verification code to enter.
3- Enter the code that you have now from your email.
4- Don't complete your account.

5- Now open a private window from another browser.
6- Try to login with this email and you will get the message like the fisrt SS i attached.
7- Now you can click on Create New Account.
8- By using the victim email "Not Completed yet" and fill first, last name and phone.
9- Now Click Next Button and here is the problem ..... You are logged in with the victim email "diaa.diab.2012@gmail.com"


If you need more information i will be very happy to help...Thank you 
Diaa

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
