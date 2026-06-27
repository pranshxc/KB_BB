---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '666722'
original_report_id: '666722'
title: Email enumeration at SignUp page
weakness: Information Disclosure
team_handle: omise
created_at: '2019-08-03T10:13:32.763Z'
disclosed_at: '2019-09-04T07:42:59.298Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 58
asset_identifier: go.exchange
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Email enumeration at SignUp page

## Metadata

- HackerOne Report ID: 666722
- Weakness: Information Disclosure
- Program: omise
- Disclosed At: 2019-09-04T07:42:59.298Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi.

There's bad security practise at https://trade.go.exchange/en/auth/sign-up against User enumeration.

#### Description:

At the signup page here https://trade.go.exchange/en/auth/sign-up , when you enter an existing user's mail , a msg box says "Email is invalid."

F546294

The problem is that any used email gets the same error message. while when you enter any other e-mail regardless whether it is fake or not & valid or no it get accepted. which means any Email (could be fake) is valid except registred emails in the database.
so an attacker can compare both responses (success & failure) and enumerate users' emails in large scale.

#### Mitigation:
A better security practise is by simply saying that you sent a link to the e-mail no matter if they have an account already or no. If they have already registred and another process is done, the Email message must say that "someone tried to signup with that Email adress, if that's you please log in."

## Impact

- Leaking users' emails. / Information Disclosure.

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
