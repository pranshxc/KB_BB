---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3923'
original_report_id: '3923'
title: Adding an user email address to the list before confirming.
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-03-13T12:46:37.460Z'
disclosed_at: '2014-06-11T09:02:59.746Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 8
tags:
- hackerone
- violation-of-secure-design-principles
---

# Adding an user email address to the list before confirming.

## Metadata

- HackerOne Report ID: 3923
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2014-06-11T09:02:59.746Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I know many of the penetration tester's email address.And many of them will be interested to join on hackerone.
Well lets think of a scenario.
I used some other penetration tester's email address to create an account on hackerone.And I choosed the username to be "something_erotic"
I know that users account will not be created untill they click on the confirmation key.
Ok,now think the real owner of that email address came to hackerone,and tried to create an account.He wont be able to create account that time.Cause the email address was already used.This is a bug.Obviously,you should not mark an email address as "USED" untill they have been confirmed.And if the real user tries forget password option also,he will have to take trouble of sending email to your support,to change his username.

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
