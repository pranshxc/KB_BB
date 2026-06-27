---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '245304'
original_report_id: '245304'
title: 'Running 2 accounts with a single email #3'
weakness: Business Logic Errors
team_handle: weblate
created_at: '2017-07-02T10:46:46.087Z'
disclosed_at: '2018-08-27T19:06:57.343Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- business-logic-errors
---

# Running 2 accounts with a single email #3

## Metadata

- HackerOne Report ID: 245304
- Weakness: Business Logic Errors
- Program: weblate
- Disclosed At: 2018-08-27T19:06:57.343Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Following the fixes: #241608 & #224072. there's still another way round this.

##Reproduction Steps
1. Register 2 accounts (Preferably using Gmail not third party)
- Login both accounts on separate browsers
- In Browser1, navigate to https://demo.weblate.org/accounts/profile/#auth
- Add a new association with the Google third party link using the registered email address in Browser2
- Fill the Password and Add the Association
- Disconnect the email on the account initially
- Email will be changed to the new one added in (4)
- Now, both browsers have the same email address i.e 2 accounts with a single email
- Logging out any of the account and trying to login leads to a server error.

Screenshots are attached below.

Shuaib.

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
