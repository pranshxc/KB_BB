---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224072'
original_report_id: '224072'
title: Running 2 accounts with a single email
weakness: Business Logic Errors
team_handle: weblate
created_at: '2017-04-26T14:48:05.355Z'
disclosed_at: '2017-05-18T07:58:05.815Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- business-logic-errors
---

# Running 2 accounts with a single email

## Metadata

- HackerOne Report ID: 224072
- Weakness: Business Logic Errors
- Program: weblate
- Disclosed At: 2017-05-18T07:58:05.815Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

While testing, I found a logic flaw which made me to make two accounts with a single email

###Reproduction Steps
- You need 3 emails (Gmail to be precise)
- Register 2 accounts with 2 different emails
- On account 1, add a new email (3rd email) using the Google Auth
- Then delete the previous email
- add a new email (3rd email) using the Google Auth
- Logout and Login, you'll see one with email and other with Google logo
- Delete the  one with Google logo (Auth) leaving the other
- Navigate to https://myaccount.google.com/permissions and remove `Weblate`
- Do the same on account 2 preferably in another browser without the last step (*Navigate....*)
- Now 2 accounts have one email.
- Logout and login (account 2) and you'll see a message like below

{F179708}

Regards,
Shuaib

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
