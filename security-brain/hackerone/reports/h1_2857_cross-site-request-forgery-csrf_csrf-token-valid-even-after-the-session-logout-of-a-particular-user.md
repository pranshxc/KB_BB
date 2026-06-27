---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2857'
original_report_id: '2857'
title: CSRF token valid even after the session logout of a particular user
weakness: Cross-Site Request Forgery (CSRF)
team_handle: phabricator
created_at: '2014-03-03T17:30:44.366Z'
disclosed_at: '2014-06-26T20:39:32.164Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF token valid even after the session logout of a particular user

## Metadata

- HackerOne Report ID: 2857
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: phabricator
- Disclosed At: 2014-06-26T20:39:32.164Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

To reproduce the issue:

1) Login to your https://secure.phabricator.com account and copy your Anti CSRF token.

2) Now logout and again login after sometime.

3) Open up your burp suite to modify the request and now submit any form with your old CSRF token.

The request will be completed.

So let's suppose i am somehow able to get CSRF token of a particular user then i can use the same token again and again to perform the attack.

The token should be thrown from the db after the session logout.

Please have a look.

Best regards,
Anand

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
