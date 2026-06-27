---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '46736'
original_report_id: '46736'
title: CSRF token leakage
weakness: Cross-Site Request Forgery (CSRF)
team_handle: enter
created_at: '2015-02-05T13:08:28.993Z'
disclosed_at: '2015-03-23T23:01:24.291Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF token leakage

## Metadata

- HackerOne Report ID: 46736
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: enter
- Disclosed At: 2015-03-23T23:01:24.291Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
I have noticed that when the account verification fails here : https://wallet.robocoin.com/verify/ due to an error, the CSRF token is being leaked via GET method like : https://wallet.robocoin.com/verify/id?_csrf=b8ede20d-0c0b-4e16-9d05-6ad2ed8b72c4
So the authenticity token is being stored in the web browser history and can be retrieved by a malicious attacker in order to mount a successful CSRF attack against the victim. Besides, that the token can be reused multiple times and do not get expired on first use.
Best regards.

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
