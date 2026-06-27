---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '133994'
original_report_id: '133994'
title: No authorization required in iOS device web-application
weakness: Improper Authentication - Generic
team_handle: coinbase
created_at: '2016-06-30T20:10:16.987Z'
disclosed_at: '2016-06-30T20:20:05.100Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# No authorization required in iOS device web-application

## Metadata

- HackerOne Report ID: 133994
- Weakness: Improper Authentication - Generic
- Program: coinbase
- Disclosed At: 2016-06-30T20:20:05.100Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hey, this is Ahsan Tahir! I've found a authorization issue in coinbase! :-)

Issue
=======
When we login to coinbase using PC (not authorized) it asks for authorization using a link, which is sent to our email and we have to authorize it by clicking on that email; but, when we login to a iOS device (using a browser), it doesn't requires any authorization, and we directly login, it shows the transactions and the total balance in our wallet, which is no doubt **Information Disclosure**; further, if we go to this URL https://www.coinbase.com/settings, we can edit our settings [change password, delete account, change other settings] etc.. so this is no doubt **Authorization/Authentication** issue.

### Steps to Reproduce:
1. Login with iOS device (browser, not app). 
2. It won't ask for any authorization, and it will disclose the transactions etc..
3. Go to https://www.coinbase.com/settings.
4. Now you can also *edit* the settings.

How to Fix?
----------------
When we login to iOS device using browser, it *should* ask for authorization! Like sending a mail to the email of that account or other type of authorization!

If you have any other questions or if anything needs clarification, please let me know.

Hoping for you to fix this issue ASAP!

Thanks,
Ahsan Tahir

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
