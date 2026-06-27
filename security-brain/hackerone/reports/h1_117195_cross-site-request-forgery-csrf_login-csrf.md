---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '117195'
original_report_id: '117195'
title: Login csrf.
weakness: Cross-Site Request Forgery (CSRF)
team_handle: gratipay
created_at: '2016-02-18T19:27:22.866Z'
disclosed_at: '2017-08-21T13:29:29.202Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Login csrf.

## Metadata

- HackerOne Report ID: 117195
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: gratipay
- Disclosed At: 2017-08-21T13:29:29.202Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi , 

There is no state parameter in bitbucket login request .

https://bitbucket.org/site/oauth1/authorize?oauth_token=ZmCHb7dnyYVYKTYRNt .

As you can see that there is no state parameter in above request there it is possible to exploit login csrf.

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
