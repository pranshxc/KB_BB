---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '21083'
original_report_id: '21083'
title: Account Hijacking (Only rare case scenario)
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2014-07-22T19:40:36.283Z'
disclosed_at: '2014-08-23T18:23:38.527Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Account Hijacking (Only rare case scenario)

## Metadata

- HackerOne Report ID: 21083
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2014-08-23T18:23:38.527Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
This is a logical flaw in the application which may allow any arbitrary user to obtain account access of another user.
Below is the exploit scenario which may lead to potential account takeover in certain circumstances:
* User changes email while he is logged in his own account (Some wrong email)
* User enters an incorrect mail
* Another user (user-2) receives the verification link
* User- 2 clicks on the link (as of yet the new email doesn't get assoc. with the account)
* Now, User-2 clicks on forgot password - the reset link is sent on the User-2 's email address.
* User-2 clicks on that link, and changes the password.

Successfully gains any hackerone's account.

The glitch - User-1 needs to set wrong email by-mistake.

Possible Fix: 
> Authentication after the reset link is sent via the old creds.
> Use Codes which can be sent to emails and not Links for verification

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
