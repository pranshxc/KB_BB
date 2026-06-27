---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '147182'
original_report_id: '147182'
title: No email verification required when we change email from settings
weakness: Uncontrolled Resource Consumption
team_handle: fantasytote
created_at: '2016-06-25T13:58:07.150Z'
disclosed_at: '2016-07-23T17:34:22.961Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- uncontrolled-resource-consumption
---

# No email verification required when we change email from settings

## Metadata

- HackerOne Report ID: 147182
- Weakness: Uncontrolled Resource Consumption
- Program: fantasytote
- Disclosed At: 2016-07-23T17:34:22.961Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey, this is Ahsan Tahir!

Issue:
---------
When we try to signup with an email, it asks us for clicking a email validation link which is sent to our email, then we have to login, without clicking that link, we cannot login, but when we change email from user settings page/edit settings page, it doesn't asks us for validation..

Impact:
----------
For example, a user creates an account with his email (user@example.com) and verifies it using the link which has been sent to his email, as he/she have access to user@example.com, but next he goes  to settings and in email change mechanism, he can put any email like (president@whitehouse.gov) and no verification is required, and the user can login with that email and access his account with the email president@whitehouse.gov, and do some abusive or not good activities and the company will be blamed!

Steps To Reproduce:-
-------------------------
1. Go to sign up form.
2. Enter Any Email.
3. Create account
* The Account will be activated with any email verification!

How to fix?
-------------------
Email verification/validation should be required when a user changed email from user settings page..

I hope you'll fix it soon. :-)

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
