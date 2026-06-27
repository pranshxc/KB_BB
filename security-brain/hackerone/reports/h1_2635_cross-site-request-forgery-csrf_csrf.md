---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2635'
original_report_id: '2635'
title: csrf
weakness: Cross-Site Request Forgery (CSRF)
team_handle: slack
created_at: '2014-03-01T23:07:20.171Z'
disclosed_at: '2014-04-06T19:42:58.224Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# csrf

## Metadata

- HackerOne Report ID: 2635
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: slack
- Disclosed At: 2014-04-06T19:42:58.224Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Anti CSRF token to prevent CSRF attacks are missing on this link https://sehacure.slack.com/help/requests/new

A new request can be submitted by an malicious guy to the support team on behalf of the user.

The victim will never get to know.

1) Go to this link

https://sehacure.slack.com/help/requests/new

2) Open tamper data addon in firefox.
Submit the data .

3) Tamper the reuqest there are no tokens in the requests.

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
