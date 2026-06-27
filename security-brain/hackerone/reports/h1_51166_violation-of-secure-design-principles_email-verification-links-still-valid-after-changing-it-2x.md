---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '51166'
original_report_id: '51166'
title: Email verification links still valid after changing it 2x
weakness: Violation of Secure Design Principles
team_handle: irccloud
created_at: '2015-03-12T17:47:11.177Z'
disclosed_at: '2015-03-13T11:08:45.280Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Email verification links still valid after changing it 2x

## Metadata

- HackerOne Report ID: 51166
- Weakness: Violation of Secure Design Principles
- Program: irccloud
- Disclosed At: 2015-03-13T11:08:45.280Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

When creating a new account on IRCCloud.com the user is asked to confirm his email address. The email verification link is formatted in the following way: ircloud.com/verify-emai/{user_id}/{email_address}/{hash_value}.

If the user decides to change his email address before he confirmed it, a new confirmation mail is sent to his newly entered address. At this point the old verification link is not valid anymore. However, if the user again changes it's email address, and uses the same address as he originally used to create his account the same verification link is sent again as the original one. The hash value in the URL seems to be generated based on the entered email address. This tells me that the hash is not very strong. I would would have expected some randomness here as well, at least to make sure that a new hash is generated the second time the user changed his email address. This can for example be done by adding a random salt to the hash. Ofcourse you will need to store this random value also to be able to recalculate the hash during verification.

In short:
- User creates account and receives verification link: verify-email/1/test@test.com/12345
- User changes email address. A new confirmation mail is sent with the following verification link: verify-email/1/otheraddress@test.com/85264
- Now the first verification link is not valid anymore.
- User changes email address back to test@test.com. He now receives the exact same link as before: verify-email/1/test@test.com/12345.

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
