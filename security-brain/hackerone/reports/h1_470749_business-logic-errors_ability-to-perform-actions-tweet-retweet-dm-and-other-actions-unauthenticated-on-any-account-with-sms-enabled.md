---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '470749'
original_report_id: '470749'
title: Ability to perform actions (Tweet, Retweet, DM) and other actions, unauthenticated,
  on any account with SMS enabled.
weakness: Business Logic Errors
team_handle: x
created_at: '2018-12-21T20:48:10.158Z'
disclosed_at: '2019-09-26T22:58:00.514Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 99
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Ability to perform actions (Tweet, Retweet, DM) and other actions, unauthenticated, on any account with SMS enabled.

## Metadata

- HackerOne Report ID: 470749
- Weakness: Business Logic Errors
- Program: x
- Disclosed At: 2019-09-26T22:58:00.514Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** By knowing the mobile phone number associated with a Twitter account, or by using random mobile phone numbers! It is possible to perform the following actions against a target without their knowledge or interaction. With no account takeover scenario.

It's a case of, if I know the mobile number... I can control basic functions of the account.

I can do everything that is listed here: https://help.twitter.com/en/using-twitter/sms-commands on an account, completely unauthenticated.


## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Spoof target number, send an SMS to a special short code for the geographical location, as seen here: https://help.twitter.com/en/using-twitter/supported-mobile-carriers


## Impact: Massive. I can remove the SMS two factor of the account. I can DM people without them knowing. If I had the mobile number of Donald Trump, I could send Tweets as him... There is so much wrong here. 

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

https://twitter.com/___Sh4rk___/status/1076204152546619392 this is a tweet I sent from my close friends account. She did not reveal her password or authenticate it at all.

## Impact

Remove 2FA

Tweet on someones behalf.

DM Someone.

Delete someones tweets

Turn off all phone SMS notifications

Follow people

Unfollow people.

Block/Report people - with a little script I could get 10000 phone numbers all reporting innocent tweets. Controlling media etc

More stuff really.

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
