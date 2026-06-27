---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2688'
original_report_id: '2688'
title: State parameter missing on google OAuth
weakness: Cross-Site Request Forgery (CSRF)
team_handle: slack
created_at: '2014-03-02T07:24:30.026Z'
disclosed_at: '2014-04-06T19:40:03.977Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# State parameter missing on google OAuth

## Metadata

- HackerOne Report ID: 2688
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: slack
- Disclosed At: 2014-04-06T19:40:03.977Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

State parameter i.e anti-csrf token to prevent session hijacking attacks is missing on Google OAuth

i.e. https://accounts.google.com/o/oauth2/auth?response_type=code&redirect_uri=https%3A%2F%2Fslack.com%2Fservices%2Fauth%2Fgdrive&client_id=19570130570-tfuuvh6hutjd09bq64is5sao643q67jg.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&access_type=offline&approval_prompt=force&state=sehacure

As we can see in above URL there is no state parameter to maintain session identity.

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
