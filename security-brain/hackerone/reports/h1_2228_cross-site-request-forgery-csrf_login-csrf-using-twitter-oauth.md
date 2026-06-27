---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2228'
original_report_id: '2228'
title: Login CSRF using Twitter OAuth
weakness: Cross-Site Request Forgery (CSRF)
team_handle: phabricator
created_at: '2014-02-23T17:25:25.462Z'
disclosed_at: '2014-03-26T01:09:32.610Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Login CSRF using Twitter OAuth

## Metadata

- HackerOne Report ID: 2228
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: phabricator
- Disclosed At: 2014-03-26T01:09:32.610Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This bug is related to bug report [#774 (Log in a user to another account)](https://hackerone.com/reports/774) by @dawidczagan as this bug also allows a user to be logged in as the attacker. The main reason is that no state is maintained in the authentication flow. Although the Twitter flow still uses OAuth 1.0A, which has no `state` parameter as in OAuth 2, it is still possible to prevent this type of attack by setting an additional parameter in the `oauth_callback` value.

An attacker could exploit this bug as follows:

1. Attacker initiates Twitter OAuth process with Phabricator
2. Attacker allows access to Phabricator app
3. Attacker records and drops redirection to Phabricator (in order not to consume token)
4. Attacker directs victim to `/auth/login/twitter:twitter.com/?oauth_token={attacker_token}&oauth_verifier={attacker_verifier}`
5. Victim is now logged in as attacker

To mitigate this vulnerability, either maintain state in the authentication flow by adding a parameter in the callback value or, as Twitter seems to support OAuth 2, use that instead.

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
