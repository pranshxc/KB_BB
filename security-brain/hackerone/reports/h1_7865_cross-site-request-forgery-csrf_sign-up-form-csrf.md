---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7865'
original_report_id: '7865'
title: Sign-up Form CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localize
created_at: '2014-04-17T18:20:20.847Z'
disclosed_at: '2014-04-18T05:16:58.375Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Sign-up Form CSRF

## Metadata

- HackerOne Report ID: 7865
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localize
- Disclosed At: 2014-04-18T05:16:58.375Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Cross-site request forgery, also known as a one-click attack or session riding and abbreviated as CSRF or XSRF, is a type of malicious exploit of a website whereby unauthorized commands are transmitted from a user that the website trusts.


Form action: http://www.localize.io/pages/sign_up
Form method: POST

Form inputs:

sign_up[type] [Radio]
sign_up[username] [Text]
sign_up[password1] [Password]
sign_up[password2] [Password]


The impact of this vulnerability:-

An attacker may force the users of a web application to execute actions of the attacker's choosing. A successful CSRF exploit can compromise end user data and operation in case of normal user. If the targeted end user is the administrator account, this can compromise the entire web application.

How to fix this vulnerability:-

Check if this form requires CSRF protection and implement CSRF countermeasures if necessary.

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
