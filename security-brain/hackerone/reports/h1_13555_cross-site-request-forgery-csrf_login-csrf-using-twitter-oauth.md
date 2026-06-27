---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13555'
original_report_id: '13555'
title: Login CSRF using Twitter oauth
weakness: Cross-Site Request Forgery (CSRF)
team_handle: factlink
created_at: '2014-05-27T08:06:02.615Z'
disclosed_at: '2014-07-05T14:33:43.579Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Login CSRF using Twitter oauth

## Metadata

- HackerOne Report ID: 13555
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: factlink
- Disclosed At: 2014-07-05T14:33:43.579Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

this bug allows a user to be logged in as the attacker. The main reason is that no state is maintained in the authentication flow. Although the Twitter flow still uses OAuth 1.0A, which has no state parameter as in OAuth 2, it is still possible to prevent this type of attack by setting an additional parameter in the oauth_callback value.

An attacker could exploit this bug as follows:

Attacker initiates Twitter OAuth process with Phabricator
Attacker allows access to Phabricator app
Attacker records and drops redirection to Phabricator (in order not to consume token)
Attacker directs victim to /auth/login/twitter:twitter.com/?oauth_token={attacker_token}&oauth_verifier={attacker_verifier}
Victim is now logged in as attacker
To mitigate this vulnerability, either maintain state in the authentication flow by adding a parameter in the callback value or, as Twitter seems to support OAuth 2, use that instead

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
