---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '134894'
original_report_id: '134894'
title: The Anti-CSRF Library fails to restrict token to a particular IP address when
  being behind a reverse-proxy/WAF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: paragonie
created_at: '2016-04-27T00:19:53.388Z'
disclosed_at: '2016-04-27T09:16:17.545Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# The Anti-CSRF Library fails to restrict token to a particular IP address when being behind a reverse-proxy/WAF

## Metadata

- HackerOne Report ID: 134894
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: paragonie
- Disclosed At: 2016-04-27T09:16:17.545Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The Anti-CSRF Library provides the ability to restrict token to a particular IP address using the variable "$hmac_ip". 

When "$hmac_ip" is set to "true", the token is generated using the predefined variable "$_SERVER['REMOTE_ADDR']" which gives the IP address of the client. However, when the web server is behind a reverse-proxy/WAF/Load-balancer/whatever, which is nowadays often the case, this variable will always return the IP address of the reverse-proxy/WAF/Load-balancer/whatever, failing to restrict the token to the client real IP address.

In order to restrict the token to the user real IP address, the Anti-CSRF Library should also check for the X-Forwared-For HTTP header. However, be advised this header can easily be spoofed. To my knowledge, one cannot ensure a client real IP address.

Both version 1.0.0 and 2.0.0 are affected.

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
