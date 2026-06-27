---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '160109'
original_report_id: '160109'
title: Brute force login and bypass locked account restrictions via iOS app
weakness: Violation of Secure Design Principles
team_handle: instacart
created_at: '2016-08-17T16:25:03.772Z'
disclosed_at: '2016-09-19T19:01:38.566Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- violation-of-secure-design-principles
---

# Brute force login and bypass locked account restrictions via iOS app

## Metadata

- HackerOne Report ID: 160109
- Weakness: Violation of Secure Design Principles
- Program: instacart
- Disclosed At: 2016-09-19T19:01:38.566Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When logging in to an account on the website, a user's account gets locked out after ~15 tries to prevent an attacker from brute forcing access to the account.

These same restrictions do not apply to the mobile sign-in endpoint (a POST request to `https://www.instacart.com/oauth/token`), which allows an attacker to brute force login of any user's account (I have attempted logging into my account ~50 times, with no restrictions).

In addition, if an account has already been locked from too many sign-ins on the website, an attacker can still log in using the app's endpoint.

POC:

1. Configure a mobile proxy, such as BurpSuite.
2. Make a login request in the Instacart app.
3. Repeat this request to brute force any account's password.

As an example, I found a list of the most common 100 passwords and added my own password somewhere in the list. All invalid passwords returned a 401 error, while the correct password returned a 200 error.

Suggested fix:

Apply the same rate limiting and locking-out to mobile login as web login.

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
