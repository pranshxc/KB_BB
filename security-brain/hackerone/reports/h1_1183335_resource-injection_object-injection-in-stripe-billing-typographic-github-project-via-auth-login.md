---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1183335'
original_report_id: '1183335'
title: Object injection in `stripe-billing-typographic` GitHub project via /auth/login
weakness: Resource Injection
team_handle: stripe
created_at: '2021-05-03T22:14:22.670Z'
disclosed_at: '2023-03-06T14:03:26.851Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: Stripe Open Source
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- resource-injection
---

# Object injection in `stripe-billing-typographic` GitHub project via /auth/login

## Metadata

- HackerOne Report ID: 1183335
- Weakness: Resource Injection
- Program: stripe
- Disclosed At: 2023-03-06T14:03:26.851Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
It is possible to use an object injection failure to achieve a sql injection, where attacker uses the means to bypass authentication, requiring only a valid password within the database.

The vulnerable code is:  https://github.com/stripe/stripe-billing-typographic

For a failure to occur, it is necessary that the environment is configuring with the mysql database.  

The same scenario is seen in the demonstration environment: https://typographic.io/

## Steps To Reproduce:

  1. Register a simple user in the application, with a password at your desire. Ex:
```
user: test@test.com
password:123
```
  2. Send a request to /auth/login like this:
```
POST /auth/login

{"email":{"email":1},"password":"1234"}
```
  3. You will then see that the login was performed without the need to provide a valid user!

{F1287585}


## Supporting Material/References:
Well, the failure occurs due to the possibility of an object reaching the query, which will be handled by a dependency called sqlstring, performing some scapes, where it will cause a confusion to the query.

Sqlstring will handle {,} replacing with `. 
So your login query will be:
```
SELECT * FROM `accounts` WHERE `email`=`email`=1
```
The sql string library is a dependency on the mysql library, which is used by knex.

## Mitigation

Is a simple step, use JSON.stringfy e resolve your problem, because JSON.stringfy will transform the malicious object into a string, preventing treatment during a query.

## Impact

This vulnerability to the applied scenario makes it easier for the attacker to acquire accounts, as the attacker only needs to discover a valid password to gain access to the victim's account.

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
