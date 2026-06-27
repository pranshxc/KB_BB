---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15412'
original_report_id: '15412'
title: Leaking CSRF token over HTTP resulting in CSRF protection bypass
weakness: Cross-Site Request Forgery (CSRF)
team_handle: coinbase
created_at: '2014-06-07T04:44:03.487Z'
disclosed_at: '2014-10-16T01:53:12.884Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Leaking CSRF token over HTTP resulting in CSRF protection bypass

## Metadata

- HackerOne Report ID: 15412
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: coinbase
- Disclosed At: 2014-10-16T01:53:12.884Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Start a proxy tool like Burp.
2. Authenticate to the Coinbase application.
3. Navigate to the URL https://coinbase.com/docs/api/overview
4. Under Developer Updates, enter your email address and click "Subscribe".
5. Notice that this request is sent over HTTP with the CSRF token in the body of the POST request. 

This means that an attacker can easily perform a MiTM attack and gain access to this CSRF token. The attacker can then trick this authenticated Coinbase user to perform CSRF attacks since the attacker now knows the CSRF token associated with this user. This results in bypassing the existing CSRF protection in the Coinbase application.

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
